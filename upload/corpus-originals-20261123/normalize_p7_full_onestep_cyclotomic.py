#!/usr/bin/env python3
"""
normalize_p7_full_onestep_cyclotomic.py
=======================================
RTG OPEN 9 — exact full 1-step Birkhoff normalization for p=7.

Purpose
-------
Upgrade the previous p=7 h3-only / partial-convention exact coefficient to a
full sequential one-step Birkhoff normalization through degree 5 in the true
cyclotomic field Q(zeta_7).

Field
-----
All coefficients are represented exactly in

    Q(zeta_7) = Q[lam] / (1 + lam + lam^2 + ... + lam^6),
    lam = exp(2*pi*i/7).

Implementation uses a small exact rational arithmetic class, not floating point
and not SymPy quotient reductions.  Numerical evaluations are printed only as
checks.

Map
---
    rho' = rho - sin(eta)
    eta' = eta + K_7*(exp(rho)-1) - K_7*sin(eta)
    K_7 = 2 - lam - lam^6.

Eigenframe
----------
    u = 1/(1-lam),  ubar = conjugate(u),
    rho = u Z + ubar W,
    eta = Z + W,  W = Zbar.

Normalization convention
------------------------
Sequential near-identity conjugation

    G = Phi^{-1} o F o Phi,    Phi(Z)=Z+h_d(Z,W),

for d=2,3,4.  For a monomial Z^a W^b, the linear homological term is

    c_new = c + (lam - lam^(a-b)) h_ab,

so the nonresonant killer is

    h_ab = c / (lam^(a-b) - lam).

Resonance condition for p=7:

    a - b == 1 mod 7.

Thus up to degree 5:
  - degree 3 retains only (2,1),
  - degree 5 retains only (3,2),
  - no degree-5 lattice harmonic exists for p=7.

Outputs
-------
1. Raw cubic coefficient check against the general p theorem.
2. Full normalized nu3^(7) after h2.
3. Full normalized nu5^(7) after h2,h3,h4.
4. Optional h5 cleanup check showing nonresonant degree-5 terms can be removed
   without changing the retained (3,2) coefficient.
5. Comparison against the older archived h3-only/partial-convention coefficient.

Status interpretation
---------------------
The full nu5 printed by this script is the full one-step Birkhoff coefficient
for this explicit normalization convention.  It should be compared against the
previous tilde_nu5 h3-only object; both are exact but convention-distinct.
"""

from __future__ import annotations

from fractions import Fraction
import argparse
import cmath
import math
from typing import Dict, Tuple

MAX_DEG = 5
Monomial = Tuple[int, int]


# =============================================================================
# Q(zeta_7) exact arithmetic
# =============================================================================

class Cyclo7:
    """Element of Q(zeta_7), represented in basis 1,lam,...,lam^5."""

    __slots__ = ("c",)

    def __init__(self, coeffs=None):
        if coeffs is None:
            self.c = (Fraction(0),) * 6
        else:
            cc = [Fraction(x) for x in coeffs]
            if len(cc) != 6:
                raise ValueError("Cyclo7 expects exactly 6 coefficients")
            self.c = tuple(cc)

    @staticmethod
    def zero():
        return Cyclo7()

    @staticmethod
    def one():
        return Cyclo7([1, 0, 0, 0, 0, 0])

    @staticmethod
    def q(x):
        return Cyclo7([Fraction(x), 0, 0, 0, 0, 0])

    @staticmethod
    def basis_power(n: int):
        """Return lam^n reduced into the 1..lam^5 basis."""
        r = n % 7
        if r <= 5:
            arr = [Fraction(0)] * 6
            arr[r] = Fraction(1)
            return Cyclo7(arr)
        # lam^6 = -(1+lam+...+lam^5)
        return Cyclo7([-1, -1, -1, -1, -1, -1])

    def __add__(self, other):
        other = to_cyclo(other)
        return Cyclo7([a + b for a, b in zip(self.c, other.c)])

    __radd__ = __add__

    def __neg__(self):
        return Cyclo7([-a for a in self.c])

    def __sub__(self, other):
        return self + (-to_cyclo(other))

    def __rsub__(self, other):
        return to_cyclo(other) - self

    def __mul__(self, other):
        other = to_cyclo(other)
        out = [Fraction(0)] * 6
        for i, a in enumerate(self.c):
            if not a:
                continue
            for j, b in enumerate(other.c):
                if not b:
                    continue
                r = (i + j) % 7
                val = a * b
                if r <= 5:
                    out[r] += val
                else:
                    # lam^6 = -sum_{k=0}^5 lam^k
                    for k in range(6):
                        out[k] -= val
        return Cyclo7(out)

    __rmul__ = __mul__

    def __truediv__(self, other):
        return self * to_cyclo(other).inverse()

    def __rtruediv__(self, other):
        return to_cyclo(other) * self.inverse()

    def __eq__(self, other):
        return self.c == to_cyclo(other).c

    def is_zero(self):
        return all(a == 0 for a in self.c)

    def conjugate(self):
        """Complex conjugation: lam -> lam^-1."""
        res = Cyclo7.zero()
        for i, a in enumerate(self.c):
            if a:
                res += Cyclo7.q(a) * Cyclo7.basis_power(-i)
        return res

    def inverse(self):
        """Exact inverse by rational Gaussian elimination on multiplication matrix."""
        # columns are self * lam^col in the basis
        mat = []
        for row in range(6):
            mat.append([(self * Cyclo7.basis_power(col)).c[row] for col in range(6)]
                       + [Fraction(1 if row == 0 else 0)])
        n = 6
        for col in range(n):
            pivot = None
            for r in range(col, n):
                if mat[r][col] != 0:
                    pivot = r
                    break
            if pivot is None:
                raise ZeroDivisionError(f"non-invertible cyclotomic element: {self}")
            if pivot != col:
                mat[col], mat[pivot] = mat[pivot], mat[col]
            pv = mat[col][col]
            mat[col] = [x / pv for x in mat[col]]
            for r in range(n):
                if r == col:
                    continue
                f = mat[r][col]
                if f:
                    mat[r] = [mat[r][k] - f * mat[col][k] for k in range(n + 1)]
        return Cyclo7([mat[i][-1] for i in range(n)])

    def to_complex(self):
        lam_num = cmath.exp(2j * math.pi / 7)
        z = 0j
        for i, a in enumerate(self.c):
            z += float(a) * (lam_num ** i)
        return z

    def common_denominator_terms(self):
        den = 1
        for a in self.c:
            den = den * a.denominator // math.gcd(den, a.denominator)
        nums = [a.numerator * (den // a.denominator) for a in self.c]
        return nums, den

    def __str__(self):
        terms = []
        for i, a in enumerate(self.c):
            if not a:
                continue
            if i == 0:
                terms.append(f"{a}")
            elif i == 1:
                terms.append(f"{a}*lam")
            else:
                terms.append(f"{a}*lam^{i}")
        return " + ".join(terms) if terms else "0"

    __repr__ = __str__


def to_cyclo(x) -> Cyclo7:
    if isinstance(x, Cyclo7):
        return x
    return Cyclo7.q(x)


def lam_pow(n: int) -> Cyclo7:
    return Cyclo7.basis_power(n)


# =============================================================================
# Bivariate polynomial in Z,W with Q(zeta_7) coefficients
# =============================================================================

class DictPoly:
    def __init__(self, terms: Dict[Monomial, object] | None = None):
        self.t: Dict[Monomial, Cyclo7] = {}
        if terms:
            for (a, b), c in terms.items():
                if a < 0 or b < 0:
                    raise ValueError("negative monomial exponent")
                if a + b > MAX_DEG:
                    continue
                cc = to_cyclo(c)
                if not cc.is_zero():
                    self.t[(int(a), int(b))] = cc

    def __add__(self, other):
        res = dict(self.t)
        for k, c in other.t.items():
            res[k] = res.get(k, Cyclo7.zero()) + c
        return DictPoly(res)

    __radd__ = __add__

    def __neg__(self):
        return DictPoly({k: -v for k, v in self.t.items()})

    def __sub__(self, other):
        return self + (-other)

    def scale(self, scalar):
        scalar = to_cyclo(scalar)
        return DictPoly({k: scalar * v for k, v in self.t.items()})

    def __mul__(self, other):
        out = {}
        for (a1, b1), c1 in self.t.items():
            for (a2, b2), c2 in other.t.items():
                k = (a1 + a2, b1 + b2)
                if k[0] + k[1] <= MAX_DEG:
                    out[k] = out.get(k, Cyclo7.zero()) + c1 * c2
        return DictPoly(out)

    def degree(self, d):
        return DictPoly({k: v for k, v in self.t.items() if sum(k) == d})

    def coeff(self, a, b):
        return self.t.get((a, b), Cyclo7.zero())

    def conjugate(self):
        return DictPoly({(b, a): c.conjugate() for (a, b), c in self.t.items()})

    def compose(self, Z_poly, W_poly):
        Zp = [DictPoly({(0, 0): 1})]
        Wp = [DictPoly({(0, 0): 1})]
        for i in range(1, MAX_DEG + 1):
            Zp.append(Zp[-1] * Z_poly)
            Wp.append(Wp[-1] * W_poly)
        res = DictPoly()
        for (a, b), c in self.t.items():
            res = res + (Zp[a] * Wp[b]).scale(c)
        return res

    def sorted_terms(self):
        return sorted(self.t.items(), key=lambda kv: (sum(kv[0]), kv[0]))

    def __str__(self):
        return str(self.t)


IdZ = DictPoly({(1, 0): 1})
IdW = DictPoly({(0, 1): 1})


def inverse_near_identity(hZ: DictPoly, hW: DictPoly, iterations: int = 8):
    """Inverse of (Id+hZ, Id+hW) to degree MAX_DEG."""
    Zin, Win = IdZ, IdW
    for _ in range(iterations):
        Zin_new = IdZ - hZ.compose(Zin, Win)
        Win_new = IdW - hW.compose(Zin, Win)
        Zin, Win = Zin_new, Win_new
    return Zin, Win


def conjugate_forward(FZ: DictPoly, hZ: DictPoly):
    """G = Phi^{-1} o F o Phi with Phi=Id+h."""
    FW = FZ.conjugate()
    hW = hZ.conjugate()
    PhiZ, PhiW = IdZ + hZ, IdW + hW
    F_Phi_Z = FZ.compose(PhiZ, PhiW)
    F_Phi_W = FW.compose(PhiZ, PhiW)
    InvZ, InvW = inverse_near_identity(hZ, hW)
    return InvZ.compose(F_Phi_Z, F_Phi_W)


# =============================================================================
# p=7 map construction
# =============================================================================

def raw_p7_map() -> DictPoly:
    print("  -> Constructing raw p=7 map through degree 5 in exact Q(zeta_7)")
    K = Cyclo7.q(2) - lam_pow(1) - lam_pow(6)
    u = Cyclo7.q(1) / (Cyclo7.q(1) - lam_pow(1))
    ub = u.conjugate()
    invD = Cyclo7.q(1) / (u - ub)

    rho = DictPoly({(1, 0): u, (0, 1): ub})
    eta = DictPoly({(1, 0): 1, (0, 1): 1})

    expm1 = (rho
             + (rho * rho).scale(Fraction(1, 2))
             + (rho * rho * rho).scale(Fraction(1, 6))
             + (rho * rho * rho * rho).scale(Fraction(1, 24))
             + (rho * rho * rho * rho * rho).scale(Fraction(1, 120)))
    sineta = (eta
              - (eta * eta * eta).scale(Fraction(1, 6))
              + (eta * eta * eta * eta * eta).scale(Fraction(1, 120)))

    rprime = rho - sineta
    eprime = eta + expm1.scale(K) - sineta.scale(K)
    return (rprime - eprime.scale(ub)).scale(invD)


# =============================================================================
# Homological normalization
# =============================================================================

def is_resonant(a: int, b: int, p: int = 7) -> bool:
    return ((a - b - 1) % p) == 0


def build_h_for_degree(F: DictPoly, degree: int):
    """Build h_degree that kills all nonresonant degree terms."""
    h_terms = {}
    retained = {}
    for (a, b), c in F.degree(degree).t.items():
        if is_resonant(a, b, 7):
            retained[(a, b)] = c
        else:
            denom = lam_pow(a - b) - lam_pow(1)
            h_terms[(a, b)] = c / denom
    return DictPoly(h_terms), DictPoly(retained)


def normalize_full(F: DictPoly, verbose: bool = False):
    G = F
    hs = {}
    retained = {}
    for d in (2, 3, 4):
        h, ret = build_h_for_degree(G, d)
        hs[d] = h
        retained[d] = ret
        print(f"  -> degree {d}: h{d} channels {sorted(h.t.keys())}")
        if ret.t:
            print(f"     retained degree {d}: {ret.t}")
        G = conjugate_forward(G, h)
        bad = [(k, v) for k, v in G.degree(d).t.items()
               if not is_resonant(*k) and not v.is_zero()]
        if bad:
            print(f"     [WARN] degree-{d} nonresonants remain: {bad}")
        else:
            print(f"     [PASS] degree-{d} nonresonants eliminated")
        if verbose:
            for k, v in h.sorted_terms():
                print(f"       h{d}{k} = {v}")
    return G, hs, retained


def cleanup_degree5(G: DictPoly):
    h5, ret5 = build_h_for_degree(G, 5)
    G5 = conjugate_forward(G, h5)
    bad = [(k, v) for k, v in G5.degree(5).t.items()
           if not is_resonant(*k) and not v.is_zero()]
    return h5, ret5, G5, bad


# =============================================================================
# Formatting helpers
# =============================================================================

def fmt_common(c: Cyclo7) -> str:
    nums, den = c.common_denominator_terms()
    pieces = []
    for i, n in enumerate(nums):
        if n == 0:
            continue
        if i == 0:
            pieces.append(f"{n}")
        elif i == 1:
            pieces.append(f"{n}*lam")
        else:
            pieces.append(f"{n}*lam^{i}")
    if not pieces:
        return "0"
    return "(" + " + ".join(pieces) + f")/{den}"


def print_coeff(label: str, c: Cyclo7):
    z = c.to_complex()
    print(f"{label}")
    print(f"  exact  = {fmt_common(c)}")
    print(f"  basis  = {c}")
    print(f"  numeric= {z.real:.18f}{z.imag:+.18f}i")


# =============================================================================
# Main
# =============================================================================

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()

    print("=" * 76)
    print("OPEN 9 — full p=7 one-step cyclotomic normalization")
    print("=" * 76)
    print("Field: Q(zeta_7), exact rational arithmetic")
    print("Conjugation: G = Phi^{-1} o F o Phi")
    print("Scope: full h2,h3,h4 normalization through degree 5")

    F = raw_p7_map()

    # Raw cubic theorem check.
    raw_c21 = F.coeff(2, 1)
    raw_c21_thm = -lam_pow(1) * (lam_pow(2) - Cyclo7.q(2) * lam_pow(1) + Cyclo7.q(2)) / (Cyclo7.q(2) * (lam_pow(2) - Cyclo7.q(1)))
    print("\nRaw Z_p-frame cubic theorem check:")
    if raw_c21 == raw_c21_thm:
        print("  [PASS] raw c21 matches general p theorem")
    else:
        print("  [FAIL] raw c21 does not match theorem")
    print_coeff("  raw c21", raw_c21)

    # Archived h3-only/partial coefficient, for reference.
    partial_archived = (Cyclo7.q(3827) * lam_pow(5)
                        - Cyclo7.q(359) * lam_pow(4)
                        + Cyclo7.q(3460) * lam_pow(3)
                        + Cyclo7.q(768) * lam_pow(2)
                        + Cyclo7.q(1899) * lam_pow(1)
                        + Cyclo7.q(2592)) / Cyclo7.q(84)
    print("\nArchived h3-only / partial-convention coefficient:")
    print_coeff("  tilde_nu5^(7)", partial_archived)
    print("  trig form:")
    print("    Re = (-3285 c1 - 589 c2 - 2083 c3)/84")
    print("    Im = (1899 s1 - 3059 s2 + 3819 s3)/84")
    print("  scope: [ALG within implemented h3-only convention]")

    # Full normalization.
    print("\nFull sequential normalization:")
    G, hs, retained = normalize_full(F, verbose=args.verbose)

    nu3_full = G.coeff(2, 1)
    nu5_full = G.coeff(3, 2)

    print("\nFull normalized coefficients:")
    print_coeff("  nu3_full^(7)", nu3_full)
    print_coeff("  nu5_full^(7)", nu5_full)

    print("\nFull-vs-partial shift:")
    print_coeff("  nu5_full - tilde_nu5", nu5_full - partial_archived)

    print("\nDegree-5 cleanup verification:")
    h5, ret5, G_after_h5, bad = cleanup_degree5(G)
    if bad:
        print("  [WARN] degree-5 nonresonants remain after h5:")
        for k, v in bad:
            print(f"    {k}: {v}")
    else:
        print("  [PASS] h5 eliminates all degree-5 nonresonants")
    if G_after_h5.coeff(3, 2) == nu5_full:
        print("  [PASS] retained (3,2) unchanged by h5")
    else:
        print("  [FAIL] retained (3,2) changed by h5")
        print_coeff("  after h5", G_after_h5.coeff(3, 2))

    print("\nGalois note:")
    print("  K7 = 2 - lam - lam^6 is not rational; true Galois maps move K7.")
    print("  Fixed-K7 while lam -> lam^j is [FAIL] for Galois conjugates.")

    print("\nSTATUS")
    print("  raw c21 theorem:                 [THM] in specified Z_p frame")
    print("  tilde_nu5^(7):                   [ALG within h3-only partial convention]")
    print("  nu5_full^(7):                    [ALG] for full h2,h3,h4 1-step convention")
    print("  compare both before exporting to DSN/Genesis layers")


if __name__ == "__main__":
    main()
