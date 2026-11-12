#!/usr/bin/env python3
"""Owner check for AZ (DYAD inbox of 12 Nov 2026): the two-component reading of DYAD-ALG-Q3-DEG2-CANCEL printed in
AZ v0.8 section 8.  Exact, SymPy.  SESSION check; it registers nothing and changes no grade.

Claim checked (component (b)).  Let f(W) = lam W + c20 W^2 + c11 W conj(W) + c02 conj(W)^2 + (degree >= 3), |lam| = 1.
Then the (0,2) coefficient of the s-fold composition f^s is
        A_s = c02 lam^(s-1) sum_{j=0}^{s-1} lam^(-3j),
whatever the other coefficients are (degree 2 has no cascade).  For lam a primitive p-th root of unity, 3 | p, s = p/3:
lam^(-3) is a primitive s-th root of unity, so the sum vanishes iff s >= 2, that is p > 3.

Gates: FORMULA (symbolic composition, s = 1..8), VANISH (p = 6, 9, ..., 30: exact division by the cyclotomic polynomial),
controls P3 (p = 3, s = 1: the coefficient is c02, not 0) and WRONGS (s = p/3 + 1: no cancellation)."""
import json, sys
import sympy as sp

W, Wb, lam = sp.symbols('W Wb lam')
c20, c11, c02, d20, d11, d02 = sp.symbols('c20 c11 c02 d20 d11 d02')     # d..: the conjugate coefficients (independent symbols)


def trunc2(e):
    e = sp.expand(e)
    return sum(e.coeff(W, a).coeff(Wb, b) * W ** a * Wb ** b for a in range(3) for b in range(3 - a))


def step(g, gb):        # one application of f to the jet (g, gb); conj(lam) = 1/lam
    return (trunc2(lam * g + c20 * g ** 2 + c11 * g * gb + c02 * gb ** 2),
            trunc2(gb / lam + d20 * gb ** 2 + d11 * g * gb + d02 * g ** 2))


def main(out):
    g, info = {}, {}
    ok = True; jet = (W, Wb)
    for s in range(1, 9):
        jet = step(*jet)
        A = sp.expand(jet[0]).coeff(W, 0).coeff(Wb, 2)
        pred = c02 * lam ** (s - 1) * sum(lam ** (-3 * j) for j in range(s))
        ok = ok and sp.simplify(A - pred) == 0
    g['FORMULA_coefficient_02_of_the_s_step_map'] = bool(ok)
    x = sp.symbols('x'); rows = {}; van = True
    for p in range(6, 31, 3):
        s = p // 3
        P = sp.Poly(sum(x ** (3 * (s - 1 - j)) for j in range(s)), x)       # lam^(3(s-1)) times the sum
        r = sp.rem(P, sp.Poly(sp.cyclotomic_poly(p, x), x))
        rows[str(p)] = dict(s=s, remainder_is_zero=bool(r.is_zero)); van = van and r.is_zero
    g['VANISH_p_6_to_30_step_3'] = bool(van); info['VANISH'] = rows
    P3 = sp.rem(sp.Poly(1, x), sp.Poly(sp.cyclotomic_poly(3, x), x))
    g['CONTROL_P3_no_cancellation_for_p_3'] = bool(not P3.is_zero)
    bad = []
    for p in range(6, 31, 3):
        s = p // 3 + 1
        P = sp.Poly(sum(x ** (3 * (s - 1 - j)) for j in range(s)), x)
        if sp.rem(P, sp.Poly(sp.cyclotomic_poly(p, x), x)).is_zero:
            bad.append(p)
    g['CONTROL_WRONGS_no_cancellation_for_s_plus_1'] = bool(not bad)
    res = dict(script='dyad_inbox_20261112_q3_deg2_check.py', status='SESSION owner check; registers nothing',
               sympy=sp.__version__, gates=g, info=info, all_pass=all(g.values()))
    json.dump(res, open(out, 'w'), indent=1, sort_keys=True)
    for k in sorted(g):
        print(k, 'PASS' if g[k] else 'FAIL')
    print('RESULT', 'PASS' if res['all_pass'] else 'FAIL')
    return 0 if res['all_pass'] else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
