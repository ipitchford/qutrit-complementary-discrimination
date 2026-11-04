"""Exact rational check of the certified CQC margins (Lemma 4.4 of the paper).

Standard library only (fractions, math).  Every check is unconditional
(no assert statements), so the script behaves identically under python -O.
A failed check prints CHECK FAILED and exits with status 1.

For 0<r<1, t>0, r+2t<1, c in [0,1] the lemma gives
    G(r,c,t) <= Qbar t^2/2 + N_c^2 t^4 / (24 L^3),
    N_c^2 = (1+sqrt(1-c^2))/8 = ||delta||^2,  L = (1-r)/4 - t*Nbar > 0,
    Qbar  = (1-c)/(1-r^2) + (1+c) Abar(r) - 2/(1-r^2/2),
where Nbar >= N_c and Abar(r) >= arctanh(r)/r are rational upper bounds:
    Abar(r) = sum_{k=0}^{40} r^{2k}/(2k+1) + r^{82}/(83(1-r^2)).
"""
from fractions import Fraction as Fr
import math


def require(condition, message):
    if not condition:
        raise SystemExit("CHECK FAILED: " + message)


def abar(r, K=40):
    head = sum(r ** (2 * k) / (2 * k + 1) for k in range(K + 1))
    return head + r ** (2 * K + 2) / ((2 * K + 3) * (1 - r * r))


def sqrt_up(x, den=10 ** 12):
    y = Fr(math.isqrt(int(x * den * den)) + 1, den)
    require(y * y >= x, "rational square-root upper bound")
    return y


def n2_up(c):
    """Rational upper bound for ||delta||^2 = (1+sqrt(1-c^2))/8."""
    return (1 + sqrt_up(1 - c * c)) / 8


def bound(r, t, c):
    r, t, c = Fr(r), Fr(t), Fr(c)
    require(0 < r < 1 and t > 0 and r + 2 * t < 1, "separable range r+2t<1")
    require(1 - r - t > 0, "classical cells positive")
    n2 = n2_up(c)
    L = (1 - r) / 4 - t * sqrt_up(n2)
    require(L > 0, "lambda_min lower bound L>0")
    A = abar(r)
    # Monotonicity in c: dQbar/dc = Abar(r) - 1/(1-r^2) < 0.
    require(A < 1 / (1 - r * r), "Abar(r) < 1/(1-r^2), so the bound decreases in c")
    Q = (1 - c) / (1 - r * r) + (1 + c) * A - 2 / (1 - r * r / 2)
    return Q * t * t / 2 + n2 * t ** 4 / (24 * L ** 3)


def main():
    # Main theorem: uniform over c in [3/5,1], hence every n >= 4.
    r, t, m = Fr(61, 200), Fr(421, 20000), Fr(-9, 20000000)
    require(bound(r, t, Fr(3, 5)) < m, "uniform margin at c=3/5")
    for k in range(41):
        c = Fr(3, 5) + Fr(2, 5) * Fr(k, 40)
        require(bound(r, t, c) < m, "uniform margin on grid c=%s" % c)
    print("PROVED uniform: (r,t)=(%s,%s), every c in [3/5,1]: G < %s" % (r, t, m))

    # Earlier, cruder constant from the same lemma.
    old = Fr(-17117, 114750000000)
    v = bound(Fr(1, 3), Fr(1, 100), Fr(3, 5))
    require(v < old, "earlier constant at (1/3,1/100)")
    print("earlier witness (1/3,1/100): bound %.4e < %s" % (float(v), old))

    table = [(4, Fr(1), Fr(113, 200), Fr(2851, 50000), Fr(-529, 5000000)),
             (5, Fr(3, 5), Fr(61, 200), Fr(421, 20000), Fr(-1143, 2500000000)),
             (6, Fr(2, 3), Fr(19, 50), Fr(2881, 100000), Fr(-1261, 500000000)),
             (7, Fr(5, 7), Fr(421, 1000), Fr(3301, 100000), Fr(-5673, 10 ** 9)),
             (8, Fr(3, 4), Fr(223, 500), Fr(3569, 100000), Fr(-9249, 10 ** 9)),
             (9, Fr(7, 9), Fr(93, 200), Fr(1879, 50000), Fr(-161, 12500000)),
             (10, Fr(4, 5), Fr(239, 500), Fr(39, 1000), Fr(-1639, 10 ** 8)),
             (11, Fr(9, 11), Fr(61, 125), Fr(1003, 25000), Fr(-1971, 10 ** 8)),
             (12, Fr(5, 6), Fr(62, 125), Fr(4103, 100000), Fr(-2281, 10 ** 8))]
    for n, c, r, t, m in table:
        require(n == 4 or c == 1 - Fr(2, n), "overlap for n=%d" % n)
        require(bound(r, t, c) < m, "per-n margin n=%d" % n)
        print("PROVED n=%d (c=%s): (r,t)=(%s,%s) G < %s = %.4e" % (n, c, r, t, m, float(m)))
    print("ALL MARGIN CHECKS PASSED")


if __name__ == "__main__":
    main()
