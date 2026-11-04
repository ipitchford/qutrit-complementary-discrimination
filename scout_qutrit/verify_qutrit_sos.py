#!/usr/bin/env python3
"""Verify the qutrit triangular-discrimination certificate using exact arithmetic.

Dependencies: python-flint and sympy.  No SDP solver, random search, numerical
eigenvalue calculation, pickle file, or certificate-generation code is used.

Run: python verify_qutrit_sos.py [exact_sos_certificate.json]

Every check is unconditional (it does not use Python's assert statement), so
the verifier behaves identically under python -O.  Any failed check prints a
REJECTED message and exits with status 1.
"""
import os
os.environ.setdefault('SYMPY_GROUND_TYPES', 'flint')
import argparse
from collections import defaultdict
from itertools import combinations
import json
from pathlib import Path
import time

from flint import fmpq
import sympy as s


def require(condition, message):
    """Unconditional proof check: never stripped by python -O."""
    if not condition:
        raise SystemExit('REJECTED: ' + message)


def decode_poly(items):
    out = {}
    for e, c in items:
        e = tuple(e)
        require(len(e) == 5 and all(isinstance(k, int) and k >= 0 for k in e),
                'malformed exponent vector %r' % (e,))
        require(e not in out, 'repeated monomial %r' % (e,))
        q = fmpq(c)
        if q:
            out[e] = q
    return out


def add_product(out, p, q, coefficient):
    if not coefficient:
        return
    for a, ca in p.items():
        for b, cb in q.items():
            e = tuple(x+y for x, y in zip(a, b))
            out[e] += coefficient*ca*cb


def from_sympy(expr, variables):
    return {e: fmpq(int(s.numer(c)), int(s.denom(c)))
            for e, c in s.Poly(s.expand(expr), *variables).terms() if c}


def unpack_upper(values, size):
    require(len(values) == size*(size+1)//2, 'wrong packed matrix length')
    mat = [[fmpq(0) for _ in range(size)] for _ in range(size)]
    k = 0
    for i in range(size):
        for j in range(i, size):
            mat[i][j] = mat[j][i] = fmpq(values[k])
            k += 1
    return mat


def require_positive_ldl(mat):
    """Sylvester's criterion via exact rational LDL, with no pivoting."""
    size = len(mat)
    lower = [[fmpq(0) for _ in range(size)] for _ in range(size)]
    diagonal = []
    for j in range(size):
        pivot = mat[j][j] - sum(
            (lower[j][k]**2*diagonal[k] for k in range(j)), fmpq(0))
        require(pivot > 0, 'nonpositive exact LDL pivot at index %d' % j)
        diagonal.append(pivot)
        lower[j][j] = fmpq(1)
        for i in range(j+1, size):
            lower[i][j] = (mat[i][j] - sum(
                (lower[i][k]*lower[j][k]*diagonal[k] for k in range(j)),
                fmpq(0)))/pivot


def derive_gate_polynomial(variables):
    """Derive Q=(prod D)/2 det(4I/3-A_W), without choosing a basis of W."""
    r, a, b, c, d = variables
    root3 = s.sqrt(3)
    omega = (-1+s.I*root3)/2
    w = s.Matrix([r, a+s.I*root3*b, c+s.I*root3*d])
    n = s.expand((w.conjugate().T*w)[0])
    vectors = ([s.eye(3)[:, j] for j in range(3)] +
               [s.Matrix([1, omega**j, omega**(2*j)]) for j in range(3)])
    lengths = [1, 1, 1, 3, 3, 3]
    overlap = {}
    for i in range(6):
        for j in range(i, 6):
            z = s.expand(n*(vectors[i].conjugate().T*vectors[j])[0]
                         -(vectors[i].conjugate().T*w)[0]
                         *(w.conjugate().T*vectors[j])[0])
            overlap[i, j] = z
            overlap[j, i] = s.conjugate(z).expand()
    B = [overlap[i, i] for i in range(6)]
    D = [s.expand(lengths[i]*B[i]) for i in range(6)]
    require(s.expand(sum(B[i]/lengths[i] for i in range(6))-4*n) == 0,
            'frame trace identity failed')
    N = s.Poly(n, *variables)
    M = {}
    for i in range(6):
        for j in range(i, 6):
            M[i, j] = M[j, i] = s.expand(
                overlap[i, j]*overlap[j, i]-B[i]*B[j]/2)
    raw = -s.Rational(32, 27)*N*s.Poly(s.prod(D), *variables)
    for i, j in combinations(range(6), 2):
        minor = s.Poly(s.expand(M[i, i]*M[j, j]-M[i, j]**2), *variables)
        quotient, remainder = s.div(minor, N)
        require(remainder.is_zero, 'pair minor not divisible by nu')
        rest = s.Poly(s.prod(D[k] for k in range(6) if k not in (i, j)), *variables)
        raw += s.Rational(4, 3)*quotient*rest
    for i, j, k in combinations(range(6), 3):
        # Direct determinant formula, independent of the Bargmann-invariant
        # shortcut used when the certificate was discovered.
        determinant = s.expand(M[i, i]*M[j, j]*M[k, k]
                              +2*M[i, j]*M[j, k]*M[k, i]
                              -M[i, i]*M[j, k]**2
                              -M[j, j]*M[k, i]**2
                              -M[k, k]*M[i, j]**2)
        quotient, remainder = s.div(s.Poly(determinant, *variables), N*N)
        require(remainder.is_zero, 'triple minor not divisible by nu^2')
        rest = s.Poly(s.prod(D[h] for h in range(6) if h not in (i, j, k)), *variables)
        raw -= quotient*rest
    Q, remainder = s.div(raw, 2*N)
    require(remainder.is_zero, 'gate polynomial not divisible by 2 nu')
    require(Q.total_degree() == 12, 'gate polynomial is not of degree twelve')
    return from_sympy(Q.as_expr(), variables)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('certificate', nargs='?', type=Path,
                        default=Path(__file__).with_name('exact_sos_certificate.json'))
    args = parser.parse_args()
    started = time.monotonic()
    cert = json.loads(args.certificate.read_text())
    variables = s.symbols('r a b c d', real=True)
    target = decode_poly(cert['polynomial'])
    require(len(target) > 0 and all(sum(e) == 12 for e in target),
            'target is not a nonzero homogeneous degree-12 polynomial')
    reconstructed = defaultdict(lambda: fmpq(0))
    block_bases = {}
    for block in cert['blocks']:
        basis = [decode_poly(p) for p in block['basis']]
        size = len(basis)
        require(1 <= size <= 43, 'block size outside 1..43')
        require(all(p and all(sum(e) == 6 for e in p) for p in basis),
                'basis entry is not a nonzero homogeneous sextic')
        exact = unpack_upper(block['gram_upper'], size)
        rounded = unpack_upper(block['ground_upper'], size)
        test = [[rounded[i][j]-(fmpq(1, 4) if i == j else 0)
                 for j in range(size)] for i in range(size)]
        require_positive_ldl(test)
        require(all(abs(exact[i][j]-rounded[i][j]) <= fmpq(1, 1000)
                    for i in range(size) for j in range(size)),
                'Gram matrix differs from its auxiliary matrix by more than 1/1000')
        # ||exact-rounded||_2 <= ||exact-rounded||_infinity <= 43/1000;
        # exact therefore dominates (1/4-43/1000) I = (207/1000) I.
        for i in range(size):
            for j in range(i, size):
                add_product(reconstructed, basis[i], basis[j],
                            exact[i][j]*(1 if i == j else 2))
        block_bases[tuple(block['key'])] = basis
        print('Exact positive Gram block:', block['key'], 'size', size, flush=True)
    reconstructed = {e: q for e, q in reconstructed.items() if q}
    require(len(cert['blocks']) == 4, 'expected exactly four Gram blocks')
    require(reconstructed == target,
            'sum of squares does not reproduce the target coefficients')
    print('All 1,820 degree-12 monomial coefficients agree exactly.', flush=True)

    r, a, b, c, d = variables
    z = a+s.I*s.sqrt(3)*b
    t = c+s.I*s.sqrt(3)*d
    h1 = r*r*z*(z**3+r**3-2*r*z*t)
    h2 = r*r*t*(t**3+r**3-2*r*z*t)
    h3 = r*r*z*t*(z*t-r*r)
    expected = {'Re(h1+h2)': s.re(h1+h2), 'Re(h1-h2)': s.re(h1-h2),
                'Im(h1+h2)/sqrt(3)': s.im(h1+h2)/s.sqrt(3),
                'Im(h1-h2)/sqrt(3)': s.im(h1-h2)/s.sqrt(3),
                'Re(h3)': s.re(h3), 'Im(h3)/sqrt(3)': s.im(h3)/s.sqrt(3)}
    require(len(cert['equality_witnesses']) == 6 and
            {w['name'] for w in cert['equality_witnesses']} == set(expected),
            'equality witnesses are not exactly the six expected identities')
    for witness in cert['equality_witnesses']:
        basis = block_bases[tuple(witness['key'])]
        coefficients = [fmpq(q) for q in witness['coefficients']]
        require(len(coefficients) == len(basis), 'witness length mismatch')
        combination = defaultdict(lambda: fmpq(0))
        for q, p in zip(coefficients, basis):
            for e, c0 in p.items():
                combination[e] += q*c0
        combination = {e: c0 for e, c0 in combination.items() if c0}
        require(combination == decode_poly(witness['polynomial']),
                'witness combination differs from its stored polynomial: ' + witness['name'])
        require(combination == from_sympy(expected[witness['name']], variables),
                'witness combination differs from the defining sextic: ' + witness['name'])
    print('All six equality-classification identities agree exactly.', flush=True)

    gate = derive_gate_polynomial(variables)
    require(gate == target, 'independently derived gate differs from the target')
    print('Independent exact Gram-minor derivation matches the gate polynomial.', flush=True)
    print('VERIFIED: exact SOS, strict Gram positivity, gate normalization, and equality witnesses.', flush=True)
    print('Elapsed seconds:', round(time.monotonic()-started, 3), flush=True)


if __name__ == '__main__':
    main()
