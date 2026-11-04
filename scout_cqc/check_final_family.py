"""Numerical regression checks; none is a premise of the analytic theorem.

Every check is unconditional (no assert statements), so the script behaves
identically under python -O.  A failed check exits with status 1.

Checked: the explicit separable decomposition, the closed-form spectrum, the
original fine-outcome measurement tables against the compressed binary
tables, and the certified gap bound, for
  * canonical Fourier pairs (n = 5, 6, 7, 11, 20) and the canonical
    order-four Hadamard family H(a);
  * randomly prescribed, non-canonical MUB pairs on both parties:
    n = 4 via an arbitrary frame V = U D1 P1 with Q = V (D1 P1)^{-1},
    R = V H(a) P2 D2; n = 5..8 via random unitary frames applied to
    Fourier pairs (and the non-Fourier pair F2 x F2 x F2 at n = 8),
    with random diagonal phases and permutations.
"""
from fractions import Fraction
import numpy as np

MARGIN = 9 / 20000000
r, t = 61 / 200, 421 / 20000
rng = np.random.default_rng(20261103)


def require(condition, message):
    if not condition:
        raise SystemExit('FAILED: ' + message)


def entropy(p):
    p = np.real(p)
    p = p[p > 1e-14]
    return -np.sum(p * np.log(p))


def mi(p):
    return entropy(p.sum(0)) + entropy(p.sum(1)) - entropy(p.ravel())


def haar_unitary(n):
    z = (rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))) / np.sqrt(2)
    q, rr = np.linalg.qr(z)
    return q * (np.diag(rr) / np.abs(np.diag(rr)))


def phases(n):
    return np.diag(np.exp(2j * np.pi * rng.random(n)))


def perm(n):
    return np.eye(n)[:, rng.permutation(n)]


def fourier(n):
    k = np.arange(n)
    return np.exp(2j * np.pi * k[:, None] * k / n) / np.sqrt(n)


def hadamard4(a):
    return np.array([[1, 1, 1, 1], [1, a, -1, -a],
                     [1, -1, 1, -1], [1, -a, -1, a]]) / 2


def observable(basis):
    """Binary observable +1 on the first basis vector, -1 on the second."""
    return (np.outer(basis[:, 0], basis[:, 0].conj())
            - np.outer(basis[:, 1], basis[:, 1].conj()))


def compression(Q, R):
    """Lemma (binary compression) for a prescribed MUB pair, n >= 5."""
    q0, r0 = Q[:, 0], R[:, 0]
    basis, _ = np.linalg.qr(np.column_stack([q0, r0]))
    P = basis @ basis.conj().T
    B1 = 2 * np.outer(q0, q0.conj()) - P
    B2 = P - 2 * np.outer(r0, r0.conj())
    return P, B1, B2


def verify(QA, RA, QB, RB, P, B1, B2, name):
    n = QB.shape[0]
    require(np.allclose(QB.conj().T @ QB, np.eye(n)), name + ': Q_B not unitary')
    require(np.allclose(np.abs(QB.conj().T @ RB) ** 2, 1 / n),
            name + ': Bob pair not mutually unbiased')
    require(np.allclose(np.abs(QA.conj().T @ RA) ** 2, 1 / 2),
            name + ': Alice pair not mutually unbiased')
    Z, X = observable(QA), observable(RA)
    I2 = np.eye(2)
    alpha = (I2 + r * (X + Z) / np.sqrt(2)) / 2
    sigma = np.kron(alpha, P / 2)
    delta = (np.kron(Z, B1) - np.kron(X, B2)) / 4
    rho = sigma + t * delta
    separated = np.zeros_like(rho)
    for b in [-1, 1]:
        separated += np.kron(alpha + b * t * Z, (P + b * B1) / 2) / 4
        separated += np.kron(alpha - b * t * X, (P + b * B2) / 2) / 4
    require(np.linalg.norm(rho - separated) < 1e-12,
            name + ': separable decomposition mismatch')
    for b in [-1, 1]:
        for M in (alpha + b * t * Z, alpha - b * t * X,
                  (P + b * B1) / 2, (P + b * B2) / 2):
            require(np.min(np.linalg.eigvalsh(M)) > -1e-12,
                    name + ': a product factor is not positive')
    ev = np.linalg.eigvalsh(rho)
    require(ev[-4] > 0.1 and np.min(ev) > -1e-12, name + ': spectrum check')
    UQ = np.kron(QA, QB)
    UR = np.kron(RA, RB)
    pz = np.real(np.diag(UQ.conj().T @ rho @ UQ)).reshape(2, n)
    px = np.real(np.diag(UR.conj().T @ rho @ UR)).reshape(2, n)
    IQ = entropy(np.linalg.eigvalsh(alpha)) + np.log(2) - entropy(ev)
    G = IQ - mi(pz) - mi(px)
    c = np.trace(B1 @ B2).real / 2
    if abs(c - 1) < 1e-12:
        c = 1.0
    four = np.array([(1 + eta * t * np.sqrt(max(0, 1 - c))
                      + xi * np.sqrt(r * r + (1 + c) * t * t)) / 4
                     for eta in [-1, 1] for xi in [-1, 1]])
    require(np.max(np.abs(np.sort(four) - ev[-4:])) < 1e-12,
            name + ': closed-form spectrum mismatch')
    table = np.array([[(1 + a * r / np.sqrt(2) + a * b * t) / 4 for b in [-1, 1]]
                      for a in [-1, 1]])
    require(abs(mi(pz) - mi(table)) < 1e-12, name + ': Q table mismatch')
    require(abs(mi(px) - mi(table)) < 1e-12, name + ': R table mismatch')
    require(G < -MARGIN, name + ': gap not below the certified margin')
    print(f"{name}: c={c:.12f}, G={G:.12g}, min support eigenvalue={ev[-4]:.12g}")


def alice_canonical():
    HA = np.array([[1.0, 1.0], [1.0, -1.0]]) / np.sqrt(2)
    return np.eye(2, dtype=complex), HA.astype(complex)


def alice_random():
    V = haar_unitary(2)
    return V @ perm(2) @ phases(2), V @ fourier(2) @ perm(2) @ phases(2)


# Canonical instances (as in the previous release).
QA, RA = alice_canonical()
for n in [5, 6, 7, 11, 20]:
    QB, RB = np.eye(n, dtype=complex), fourier(n)
    verify(QA, RA, QB, RB, *compression(QB, RB), f"Fourier n={n}")

for theta in [0, np.pi / 2, 0.731]:
    a = np.exp(1j * theta)
    QB, RB = np.eye(4, dtype=complex), hadamard4(a)
    u = np.array([1, 0, 1, 0]) / np.sqrt(2)
    v = np.array([0, 1, 0, -1]) / np.sqrt(2)
    P = np.outer(u, u) + np.outer(v, v)
    B = np.outer(u, u) - np.outer(v, v)
    verify(QA, RA, QB, RB, P, B, B, f"Hadamard4 theta={theta:.6f}")

# Random non-canonical n = 4 instances: V = U D1 P1 is the frame of the proof.
for trial in range(4):
    QA, RA = alice_random()
    U, D1, P1, D2, P2 = haar_unitary(4), phases(4), perm(4), phases(4), perm(4)
    a = np.exp(2j * np.pi * rng.random())
    V = U @ D1 @ P1
    QB = U                                  # = V (D1 P1)^{-1}
    RB = U @ D1 @ P1 @ hadamard4(a) @ P2 @ D2  # = V H(a) P2 D2
    u = V @ np.array([1, 0, 1, 0]) / np.sqrt(2)
    v = V @ np.array([0, 1, 0, -1]) / np.sqrt(2)
    P = np.outer(u, u.conj()) + np.outer(v, v.conj())
    B = np.outer(u, u.conj()) - np.outer(v, v.conj())
    verify(QA, RA, QB, RB, P, B, B, f"random n=4 trial {trial}")

# Random prescribed pairs n = 5..8.
for n in [5, 6, 7, 8]:
    hadamards = [fourier(n)]
    if n == 8:
        F2 = fourier(2)
        hadamards.append(np.kron(np.kron(F2, F2), F2))
    for k, H in enumerate(hadamards):
        for trial in range(2):
            QA, RA = alice_random()
            U = haar_unitary(n)
            QB = U @ perm(n) @ phases(n)
            RB = U @ phases(n) @ perm(n) @ H @ perm(n) @ phases(n)
            label = 'F2xF2xF2' if k == 1 else 'Fourier'
            verify(QA, RA, QB, RB, *compression(QB, RB),
                   f"random n={n} ({label} class) trial {trial}")

# Hand-checkable earlier constant (Remark rem:old-constant).
q_bound = Fraction(12, 5) * Fraction(1123, 1620) - Fraction(567, 340)
require(q_bound == -Fraction(181, 45900), 'rational curvature bound')
t_exact = Fraction(1, 100)
gap_bound = q_bound * t_exact * t_exact / 2 + Fraction(24, 5) * t_exact ** 4
require(gap_bound == -Fraction(17117, 114750000000), 'rational gap bound')
print("Exact rational gap bound:", gap_bound)
print("ALL CHECKS PASSED")
