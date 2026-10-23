#!/usr/bin/env python3
"""dyad_lh2012_transfer_check.py -- owner check of the finite algebraic inputs used to apply
López-Hernanz, "Summable formal invariant curves of diffeomorphisms", ETDS 32 (2012) 211-221 (LH2012)
to the two smooth formal branches Gamma_+/- of F = T^6 tangent to [1:0] (OPEN 20, analytic branch).

Route: T^6 composed in exact rationals in the real chart (rho, eta) to total degree 5 (functions shared with
dyad_h4_real_route_check.py), then re-expressed in the complexified raw frame z = rho + omega*eta,
w = rho + conj(omega)*eta, omega = exp(2*pi*i/3) (z = W), with exact sympy arithmetic.
Gates:
  L1 linear part identity; quadratic part zero
  L2 weighted divisibility for the chart (z, w) = (x, x^2 u): [F_z]_{3,0} = [F_w]_{3,0} = [F_w]_{2,1} = [F_w]_{4,0} = 0
  L3 coefficients mu = [F_z]_{2,1}, c40 = [F_z]_{4,0}, d31 = [F_w]_{3,1}, C = [F_w]_{5,0}, [F_w]_{1,2} = conj(mu)
  L4 reduced quadratic P(a) = A a^2 + B a + C with A = conj(mu) - 2 mu, B = d31 - 2 c40 (values as recorded)
  L5 ell_+/- = c40 + mu a_+/- nonzero and ell_- = -ell_+
  L6 eigenvalue ratio alpha = P'(a)/ell = -102/19 - 16 i sqrt3/19 for both roots (not a positive rational)
  L7 a_+ + a_- = (1 + i sqrt3)/12
  L8 one-step T: linear part (lambda z, conj(lambda) w), lambda = exp(i pi/3); [T_w]_{2,0} = -1/6
  L9 induced map on the leading coefficient a -> (conj(lambda) a - 1/6)/lambda^2 = (1 + i sqrt3)/12 - a swaps a_+ and a_-
Finite algebra only: this checks the inputs of the imported theorems, not the theorems themselves.
Usage: python -B dyad_lh2012_transfer_check.py [--control C|S]   C: altered C coefficient (L3 fails); S: altered T
coefficient sign (L8/L9 fail).   Exit 0 PASS / 1 FAIL / 3 crash.
"""
import os, sys
from fractions import Fraction as Fr
from math import factorial
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dyad_h4_real_route_check import T6, padd, compose


def main():
    import argparse, sympy as sp
    ap = argparse.ArgumentParser(); ap.add_argument('--control', choices=['C', 'S']); a_ = ap.parse_args()
    s3, I = sp.sqrt(3), sp.I
    om = sp.Rational(-1, 2) + I * s3 / 2; omb = sp.Rational(-1, 2) - I * s3 / 2
    z, w, a = sp.symbols('z w a')
    eta = (z - w) / (om - omb); rho = z - om * eta
    sym = lambda p: sum(sp.Rational(v.numerator, v.denominator) * rho ** i * eta ** j for (i, j), v in p.items())
    co = lambda P, i, j: sp.nsimplify(sp.radsimp(sp.expand(P.coeff_monomial(z ** i * w ** j))))
    eq = lambda x, y: sp.simplify(sp.expand(x - y)) == 0
    R, E = T6(5)
    Fz = sp.Poly(sp.expand(sym(R) + om * sym(E)), z, w); Fw = sp.Poly(sp.expand(sym(R) + omb * sym(E)), z, w)
    G = {}
    G['L1'] = (co(Fz, 1, 0), co(Fz, 0, 1), co(Fw, 1, 0), co(Fw, 0, 1)) == (1, 0, 0, 1) and all(co(P, i, 2 - i) == 0 for P in (Fz, Fw) for i in range(3))
    G['L2'] = all(co(P, i, j) == 0 for P, i, j in [(Fz, 3, 0), (Fw, 3, 0), (Fw, 2, 1), (Fw, 4, 0)])
    mu, c40, d31, C, mub = co(Fz, 2, 1), co(Fz, 4, 0), co(Fw, 3, 1), co(Fw, 5, 0), co(Fw, 1, 2)
    if a_.control == 'C': C = C + sp.Rational(1, 6480)
    G['L3'] = (eq(mu, -sp.Rational(1, 2) - 2 * I * s3 / 3) and eq(mub, -sp.Rational(1, 2) + 2 * I * s3 / 3) and eq(c40, -sp.Rational(1, 16) + 7 * I * s3 / 144)
               and eq(d31, sp.Rational(1, 3) - I * s3 / 9) and eq(C, -sp.Rational(61, 2160) + 43 * I * s3 / 6480))
    A, B = mub - 2 * mu, d31 - 2 * c40
    G['L4'] = eq(A, sp.Rational(1, 2) + 2 * I * s3) and eq(B, sp.Rational(11, 24) - 5 * I * s3 / 24)
    roots = sp.solve(A * a ** 2 + B * a + C, a)
    ells = [sp.simplify(c40 + mu * r) for r in roots]
    G['L5'] = len(roots) == 2 and all(abs(complex(sp.N(l, 30))) > 1e-6 for l in ells) and eq(ells[0], -ells[1])
    alphas = [sp.simplify((2 * A * r + B) / l) for r, l in zip(roots, ells)]
    G['L6'] = all(eq(x, -sp.Rational(102, 19) - 16 * I * s3 / 19) for x in alphas)
    G['L7'] = eq(roots[0] + roots[1], (1 + I * s3) / 12)
    sc = [Fr(0) if n % 2 == 0 else Fr((-1) ** (n // 2), factorial(n)) for n in range(3)]
    ec = [Fr(0)] + [Fr(1, factorial(n)) for n in range(1, 3)]
    r1, e1 = {(1, 0): Fr(1)}, {(0, 1): Fr(1)}
    s = compose(sc, e1, 2); R1, E1 = padd(r1, s, -1), padd(padd(e1, compose(ec, r1, 2)), s, -1)
    Tz = sp.Poly(sp.expand(sym(R1) + om * sym(E1)), z, w); Tw = sp.Poly(sp.expand(sym(R1) + omb * sym(E1)), z, w)
    lam = sp.Rational(1, 2) + I * s3 / 2
    q = co(Tw, 2, 0)
    if a_.control == 'S': q = -q
    G['L8'] = eq(co(Tz, 1, 0), lam) and co(Tz, 0, 1) == 0 and eq(co(Tw, 0, 1), sp.conjugate(lam)) and co(Tw, 1, 0) == 0 and eq(q, -sp.Rational(1, 6))
    img = lambda x: (sp.conjugate(lam) * x + q) / lam ** 2
    G['L9'] = eq(img(a), (1 + I * s3) / 12 - a) and eq(img(roots[0]), roots[1]) and eq(img(roots[1]), roots[0])
    print('mu =', mu, '; c40 =', c40, '; d31 =', d31, '; C =', C)
    print('alpha =', [sp.nsimplify(sp.radsimp(x)) for x in alphas])
    print('a_+/- =', [str(sp.N(r, 15)) for r in roots]); print('ell_+/- =', [str(sp.N(l, 15)) for l in ells])
    ok = all(G.values())
    for k in sorted(G, key=lambda x: int(x[1:])): print(k, 'PASS' if G[k] else 'FAIL')
    print('RESULT', 'PASS' if ok else 'FAIL')
    return 0 if ok else 1


if __name__ == '__main__':
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except Exception as ex:
        print('CRASH', type(ex).__name__, ex); sys.exit(3)
