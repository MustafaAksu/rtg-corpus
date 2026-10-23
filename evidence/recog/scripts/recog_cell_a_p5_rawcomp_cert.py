#!/usr/bin/env python3
"""
recog_cell_a_p5_rawcomp_cert.py
================================
RECOG CELL-A — exact raw-composition certificate for p=5.

Purpose
-------
Close the p=5 cubic return-order cell without reconstructing the archived
one-step normalisation engine.

The primitive p-resonant generator is

    rho' = rho - sin(eta)
    eta' = eta + K_p (exp(rho)-1) - K_p sin(eta)

with

    p = 5,
    lam = exp(2*pi*i/5),
    K_5 = 2 - lam - lam^-1.

The eigenframe is

    u = 1/(1-lam),
    rho = u Z + ubar W,
    eta = Z + W,    W = Zbar.

All algebra through degree 3 is performed exactly in

    Q(zeta_5) = Q[lam] / (1 + lam + lam^2 + lam^3 + lam^4).

Checks
------
(1) one-step linear part is exactly (lam Z, lam^-1 W),
(2) five-step linear part is identity,
(3) five-step quadratic residual vanishes identically,
(4) five-step cubic residual is confined to the resonant (2,1) channel,
(5) the exact raw cubic return coefficient is

        mu_5 = (-13 - 11 lam - 4 lam^2 - 12 lam^3)/2,

    hence mu_5 != 0 and k_ret(5)=3,
(6) using the Dyadic bridge theorem

        mu_p = p conj(lam) nu_3^(1,p),

    the implied one-step normalised coefficient is

        nu_3^(1,5)
          = (12 - lam + lam^2 + 8 lam^3)/10,

(7) Re(mu_5) < 0 in the chosen positive-lam eigenframe (diagnostic radial
    contraction), and arg(mu_5) is printed for frame-invariant cross-p
    comparison under Z -> c Z.

Scope
-----
* Exact algebraic certificate for the p=5 member of the postulated p-resonant
  generator family.
* The nu_3 value is inferred from the certified general bridge theorem; this
  script does NOT implement or reconstruct the archived full p=5 one-step
  Birkhoff normaliser.
* Magnitudes of mu_p must not be compared across p without a frame-normalisation
  bridge.  Vanishing/nonvanishing and arg(mu_p), with the same orientation
  convention lam=exp(+2*pi*i/p), are invariant under Z -> c Z.
"""

from __future__ import annotations

from fractions import Fraction
import cmath
import math
import sys
from typing import Dict, Tuple

P = 5
MAX_DEG = 3
Monomial = Tuple[int, int]


# =============================================================================
# Exact Q(zeta_5) arithmetic
# =============================================================================

class Cyclo5:
    """Element of Q(zeta_5) in basis 1, lam, lam^2, lam^3."""

    __slots__ = ("c",)

    def __init__(self, coeffs=None):
        if coeffs is None:
            coeffs = [0, 0, 0, 0]
        cc = [Fraction(x) for x in coeffs]
        if len(cc) != 4:
            raise ValueError("Cyclo5 expects exactly four coefficients")
        self.c = tuple(cc)

    @staticmethod
    def zero():
        return Cyclo5()

    @staticmethod
    def one():
        return Cyclo5([1, 0, 0, 0])

    @staticmethod
    def q(x):
        return Cyclo5([Fraction(x), 0, 0, 0])

    @staticmethod
    def basis_power(n: int):
        r = n % 5
        if r <= 3:
            out = [Fraction(0)] * 4
            out[r] = Fraction(1)
            return Cyclo5(out)
        # lam^4 = -(1 + lam + lam^2 + lam^3)
        return Cyclo5([-1, -1, -1, -1])

    def __add__(self, other):
        other = to_cyclo(other)
        return Cyclo5([a + b for a, b in zip(self.c, other.c)])

    __radd__ = __add__

    def __neg__(self):
        return Cyclo5([-a for a in self.c])

    def __sub__(self, other):
        return self + (-to_cyclo(other))

    def __rsub__(self, other):
        return to_cyclo(other) - self

    def __mul__(self, other):
        other = to_cyclo(other)
        out = [Fraction(0)] * 4
        for i, a in enumerate(self.c):
            if not a:
                continue
            for j, b in enumerate(other.c):
                if not b:
                    continue
                red = Cyclo5.basis_power(i + j)
                for k, q in enumerate(red.c):
                    out[k] += a * b * q
        return Cyclo5(out)

    __rmul__ = __mul__

    def inverse(self):
        if self.is_zero():
            raise ZeroDivisionError("zero cyclotomic element")

        # Rational Gaussian elimination for multiplication by self.
        aug = []
        for row in range(4):
            aug.append(
                [(self * Cyclo5.basis_power(col)).c[row] for col in range(4)]
                + [Fraction(1 if row == 0 else 0)]
            )

        n = 4
        for col in range(n):
            pivot = next((r for r in range(col, n) if aug[r][col] != 0), None)
            if pivot is None:
                raise ZeroDivisionError("non-invertible cyclotomic element")
            if pivot != col:
                aug[col], aug[pivot] = aug[pivot], aug[col]

            pv = aug[col][col]
            aug[col] = [x / pv for x in aug[col]]

            for r in range(n):
                if r == col:
                    continue
                f = aug[r][col]
                if f:
                    aug[r] = [aug[r][k] - f * aug[col][k]
                              for k in range(n + 1)]

        return Cyclo5([aug[i][-1] for i in range(n)])

    def __truediv__(self, other):
        return self * to_cyclo(other).inverse()

    def __rtruediv__(self, other):
        return to_cyclo(other) * self.inverse()

    def __eq__(self, other):
        return self.c == to_cyclo(other).c

    def is_zero(self):
        return all(x == 0 for x in self.c)

    def conjugate(self):
        out = Cyclo5.zero()
        for i, a in enumerate(self.c):
            if a:
                out += Cyclo5.q(a) * Cyclo5.basis_power(-i)
        return out

    def to_complex(self):
        lam_num = cmath.exp(2j * math.pi / 5)
        return sum(float(a) * lam_num**i for i, a in enumerate(self.c))

    def __repr__(self):
        return f"Cyclo5{self.c}"


def to_cyclo(x):
    return x if isinstance(x, Cyclo5) else Cyclo5.q(x)


def lam_pow(n: int):
    return Cyclo5.basis_power(n)


# =============================================================================
# Truncated bivariate polynomials in Z,W
# =============================================================================

class Poly:
    def __init__(self, terms: Dict[Monomial, object] | None = None):
        self.t: Dict[Monomial, Cyclo5] = {}
        if terms:
            for k, v in terms.items():
                if sum(k) > MAX_DEG:
                    continue
                vv = to_cyclo(v)
                if not vv.is_zero():
                    self.t[k] = vv

    def __add__(self, other):
        out = dict(self.t)
        for k, v in other.t.items():
            out[k] = out.get(k, Cyclo5.zero()) + v
        return Poly(out)

    __radd__ = __add__

    def __neg__(self):
        return Poly({k: -v for k, v in self.t.items()})

    def __sub__(self, other):
        return self + (-other)

    def scale(self, s):
        s = to_cyclo(s)
        return Poly({k: s * v for k, v in self.t.items()})

    def __mul__(self, other):
        out = {}
        for (a, b), c1 in self.t.items():
            for (c, d), c2 in other.t.items():
                k = (a + c, b + d)
                if sum(k) <= MAX_DEG:
                    out[k] = out.get(k, Cyclo5.zero()) + c1 * c2
        return Poly(out)

    def power(self, n: int):
        out = Poly({(0, 0): 1})
        for _ in range(n):
            out = out * self
        return out

    def compose(self, Zp, Wp):
        out = Poly()
        for (a, b), c in self.t.items():
            out = out + (Zp.power(a) * Wp.power(b)).scale(c)
        return out

    def degree(self, d: int):
        return {k: v for k, v in self.t.items() if sum(k) == d}

    def coeff(self, a: int, b: int):
        return self.t.get((a, b), Cyclo5.zero())


# =============================================================================
# Primitive p=5 map in the exact eigenframe
# =============================================================================

lam = lam_pow(1)
lamb = lam.conjugate()
K = Cyclo5.q(2) - lam - lamb

u = Cyclo5.q(1) / (Cyclo5.q(1) - lam)
ub = u.conjugate()

Z = Poly({(1, 0): 1})
W = Poly({(0, 1): 1})

rho = Z.scale(u) + W.scale(ub)
eta = Z + W

# Exact Taylor jet through cubic order.
sin_eta = eta - eta.power(3).scale(Fraction(1, 6))
exp_m1 = (
    rho
    + rho.power(2).scale(Fraction(1, 2))
    + rho.power(3).scale(Fraction(1, 6))
)

rho1 = rho - sin_eta
eta1 = eta + exp_m1.scale(K) - sin_eta.scale(K)

# Solve rho' = u Z' + ubar W', eta' = Z' + W'.
FZ = (rho1 - eta1.scale(ub)).scale(Cyclo5.q(1) / (u - ub))
FW = (eta1.scale(u) - rho1).scale(Cyclo5.q(1) / (u - ub))


def compose_pair(FZ, FW, GZ, GW):
    """Return F o G, truncated to MAX_DEG."""
    return FZ.compose(GZ, GW), FW.compose(GZ, GW)


# =============================================================================
# Five-step raw composition
# =============================================================================

GZ, GW = FZ, FW
for _ in range(P - 1):
    oldZ, oldW = GZ, GW
    GZ, GW = compose_pair(FZ, FW, oldZ, oldW)

DZ = GZ - Z
DW = GW - W


# =============================================================================
# Checks and reporting
# =============================================================================

ok = True

def check(name, cond):
    global ok
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    ok = ok and bool(cond)


check("one-step Z linear part is lam*Z",
      FZ.coeff(1, 0) == lam and FZ.coeff(0, 1).is_zero())
check("one-step W linear part is lam^-1*W",
      FW.coeff(0, 1) == lamb and FW.coeff(1, 0).is_zero())

check("five-step linear residual vanishes",
      all(v.is_zero() for v in DZ.degree(1).values())
      and all(v.is_zero() for v in DW.degree(1).values()))

check("five-step quadratic residual vanishes",
      all(v.is_zero() for v in DZ.degree(2).values())
      and all(v.is_zero() for v in DW.degree(2).values()))

check("Z cubic residual confined to (2,1)",
      all(v.is_zero() for k, v in DZ.degree(3).items() if k != (2, 1)))

mu5 = DZ.coeff(2, 1)
mu5_expected = (
    -Cyclo5.q(13)
    - Cyclo5.q(11) * lam
    - Cyclo5.q(4) * lam_pow(2)
    - Cyclo5.q(12) * lam_pow(3)
) / Cyclo5.q(2)

check("exact mu_5 coefficient",
      mu5 == mu5_expected)
check("mu_5 is nonzero", not mu5.is_zero())

# General Dyadic bridge theorem: mu_p = p conj(lam) nu_3^(1,p).
nu3 = mu5 / (Cyclo5.q(P) * lamb)
nu3_expected = (
    Cyclo5.q(12)
    - lam
    + lam_pow(2)
    + Cyclo5.q(8) * lam_pow(3)
) / Cyclo5.q(10)

check("bridge-implied nu_3^(1,5)",
      nu3 == nu3_expected)

# Reality consistency of the W component.
check("W-return cubic is conjugate of Z-return cubic",
      DW.coeff(1, 2) == mu5.conjugate()
      and all(v.is_zero()
              for k, v in DW.degree(3).items()
              if k != (1, 2)))

mu_num = mu5.to_complex()
nu_num = nu3.to_complex()

check("Re(mu_5) < 0", mu_num.real < 0)

print()
print("Exact results")
print("-------------")
print("mu_5 basis (1,lam,lam^2,lam^3) =", mu5.c)
print("mu_5 =", "(-13 - 11*lam - 4*lam^2 - 12*lam^3)/2")
print("nu_3^(1,5) basis =", nu3.c)
print("nu_3^(1,5) =", "(12 - lam + lam^2 + 8*lam^3)/10")
print()
print("Numerical checks")
print("----------------")
print(f"K_5 = {K.to_complex().real:.18f}")
print(f"mu_5 = {mu_num.real:.18f}{mu_num.imag:+.18f}i")
print(f"|mu_5| = {abs(mu_num):.18f}")
print(f"arg(mu_5) = {math.degrees(cmath.phase(mu_num)):.15f} deg")
print(f"nu_3^(1,5) = {nu_num.real:.18f}{nu_num.imag:+.18f}i")
print()
print("Conclusion")
print("----------")
print("mu_5 != 0, therefore k_ret(5) = 3.")
print("CERTIFICATE PASS" if ok else "CERTIFICATE FAIL")

sys.exit(0 if ok else 1)
