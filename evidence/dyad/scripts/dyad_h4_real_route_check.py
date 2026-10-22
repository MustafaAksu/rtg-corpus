#!/usr/bin/env python3
"""dyad_h4_real_route_check.py -- second-route check of the archival h4 field label (OPEN 13; DYAD-ALG-LIEGAUGE-NORM).

Route: compose T^6 in exact rationals in the real chart (rho, eta), T(rho, eta) = (rho - sin eta, eta + expm1(rho) - sin eta),
truncated at total degree 4 (fractions.Fraction; no sympy in the composition). Then re-express the degree-4 part of
Z o T^6, Z = rho + i*EP*eta (EP = sqrt3/2 + i/2, the frame of normalize_p6_liegauge_exact.py), in (Z, Zb) with sympy.
This differs from dyad_h4_archival_exact_check.py, which composes the complex form of the map in (Z, Zb) with sympy.
Also checks: linear part of T^6 = identity, degree-2 part of T^6 = 0 (so the degree-4 part is not fed by degree-2 terms).
Result: h4 coefficients equal the closed forms recorded in DSN section 1 / section 8 (DYAD-ART-NORM-P6); they are non-real,
so the field is Q(i*sqrt3), not Q(sqrt3).  Evidence key: EV-INDEP relative to the first route (same definitions, different
composition engine and chart); not an independent re-derivation of the archival gauge convention.
Usage: python -B dyad_h4_real_route_check.py [--control K]   (K: alters one claimed coefficient; must exit 1)
Exit 0 PASS / 1 FAIL / 3 crash.
"""
import sys
from fractions import Fraction as Fr
from math import factorial
sys.dont_write_bytecode = True


def padd(a, b, s=1):
    c = dict(a)
    for k, v in b.items():
        c[k] = c.get(k, 0) + s * v
        if c[k] == 0: del c[k]
    return c


def pmul(a, b, D):
    c = {}
    for (i, j), u in a.items():
        for (k, l), v in b.items():
            if i + j + k + l <= D: c[(i + k, j + l)] = c.get((i + k, j + l), 0) + u * v
    return {k: v for k, v in c.items() if v != 0}


def compose(coeffs, x, D):
    out, pw = {}, {(0, 0): Fr(1)}
    for n in range(D + 1):
        if n > 0: pw = pmul(pw, x, D)
        if coeffs[n] != 0: out = padd(out, {k: coeffs[n] * v for k, v in pw.items()})
    return out


def T6(D):
    sin_c = [Fr(0) if n % 2 == 0 else Fr((-1) ** (n // 2), factorial(n)) for n in range(D + 1)]
    exm_c = [Fr(0)] + [Fr(1, factorial(n)) for n in range(1, D + 1)]
    R, E = {(1, 0): Fr(1)}, {(0, 1): Fr(1)}
    for _ in range(6):
        s = compose(sin_c, E, D)
        R, E = padd(R, s, -1), padd(padd(E, compose(exm_c, R, D)), s, -1)
    return R, E


def main():
    import argparse, sympy as sp
    ap = argparse.ArgumentParser(); ap.add_argument('--control', choices=['K']); a = ap.parse_args()
    R, E = T6(4)
    hom = lambda p, d: {k: v for k, v in p.items() if sum(k) == d}
    ok = hom(R, 1) == {(1, 0): 1} and hom(E, 1) == {(0, 1): 1} and not hom(R, 2) and not hom(E, 2)
    print('linear part identity, degree-2 part zero:', ok)
    s3, I = sp.sqrt(3), sp.I
    Z, Zb = sp.symbols('Z Zb')
    EP, EM = s3 / 2 + I / 2, s3 / 2 - I / 2
    rho, eta = (EM * Z + EP * Zb) / s3, (-I * Z + I * Zb) / s3
    ok = ok and sp.simplify(rho + I * EP * eta - Z) == 0 and sp.simplify(rho - sp.conjugate(rho).subs({sp.conjugate(Z): Zb, sp.conjugate(Zb): Z}, simultaneous=True)) == 0
    sym = lambda p: sum(sp.Rational(v.numerator, v.denominator) * rho ** i * eta ** j for (i, j), v in p.items())
    P = sp.Poly(sp.expand(sym(hom(R, 4)) + I * EP * sym(hom(E, 4))), Z, Zb)
    claimed = {(1, 3): sp.Rational(1, 3) + s3 / 9 * I, (2, 2): -sp.Rational(5, 24) - 11 * s3 / 24 * I,
               (3, 1): -sp.Rational(1, 6) - 2 * s3 / 9 * I, (4, 0): -sp.Rational(1, 16) + 7 * s3 / 144 * I, (0, 4): sp.Integer(0)}
    if a.control == 'K': claimed[(1, 3)] = sp.Rational(1, 3) + s3 / 8 * I
    for m in sorted(claimed):
        v = sp.nsimplify(sp.radsimp(sp.expand(P.coeff_monomial(Z ** m[0] * Zb ** m[1]))))
        d = sp.simplify(v - claimed[m]); ok = ok and d == 0
        print(m, v, 'exact match' if d == 0 else 'DIFF', '' if sp.im(v) == 0 else '(non-real)')
    print('RESULT', 'PASS' if ok else 'FAIL')
    return 0 if ok else 1


if __name__ == '__main__':
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except Exception as ex:
        print('CRASH', type(ex).__name__, ex); sys.exit(3)
