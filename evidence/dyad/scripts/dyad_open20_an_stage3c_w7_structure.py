#!/usr/bin/env python3
"""dyad_open20_an_stage3c_w7_structure.py -- stage 3c-a, W7: exact derivation of the structural facts S1, S2, S3, S5.

Exact arithmetic only (Python fractions for the jet of F = T^6 in (rho, eta); sympy for the change to (z, w) over
Q(sqrt 3, i)).  No floating point, no balls.

Chart.  T(rho, eta) = (rho - sin eta, eta + e^rho - 1 - sin eta);  z = rho + omega eta,  w = rho + conj(omega) eta,
omega = e^{2 pi i/3};  so eta = (z - w)/(i sqrt 3), rho = z - omega eta.  F_z, F_w are the components of T^6 in (z, w).
Cutoff.  The Taylor polynomial of T^6 at 0 is computed exactly through total degree 5 (every monomial z^p w^q with
p + 2q <= 5 has total degree at most 5, and the change of chart is linear, so it preserves total degree).

Gates (exit 0 iff all pass):
  LIN   the linear part of T has order 6 (its sixth power is the identity); F = identity + (terms of degree >= 3).
  S5Z   F_z - z has no monomial z^p w^q with p + 2q < 4            (this is S1; with S2 as the case q = 1)
  S5W   F_w - w has no monomial z^p w^q with p + 2q < 5            (S3 is the case q >= 1; the case q = 0 is used in S4)
  P4    F_z has no monomial w^2                                    (P4(0) = 0)
  LEAD  the coefficients of z^4, z^2 w in F_z and of z w^2, z^3 w, z^5 in F_w are C40, MU, conj(MU), D31, CC as
        used by the library (stage-1 constants); F_w(z, w) = conj(F_z)(w, z) on these monomials (real structure).
Controls (each must exit 1):
  --control SCALE   e^rho - 1 replaced by (11/10)(e^rho - 1): the linear part no longer has order 6   -> LIN, S5Z, S5W
  --control SHIFT   sin(eta) replaced by sin(eta) + eta^2/10                                          -> LEAD only
                    (S5 survives: with a linear part of order 6 and no resonance in degree 2, the sixth iterate
                    has no quadratic terms whatever the quadratic terms of T are; the constants change)
Usage: python3 -I -B dyad_open20_an_stage3c_w7_structure.py --out OUT.json [--control SCALE|SHIFT]
"""
import sys, json, argparse
from fractions import Fraction as Fr
import sympy as sp

DEG = 5


def pmul(a, b):
    out = {}
    for (i, j), u in a.items():
        for (k, l), v in b.items():
            if i + j + k + l <= DEG:
                out[(i + k, j + l)] = out.get((i + k, j + l), 0) + u * v
    return {k: v for k, v in out.items() if v != 0}


def padd(a, b, s=1):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, 0) + s * v
    return {k: v for k, v in out.items() if v != 0}


def compose(coeffs, p):
    """sum_n coeffs[n] p^n, truncated (p has no constant term)."""
    out = {}; pw = {(0, 0): Fr(1)}
    for n, c in enumerate(coeffs):
        if n:
            pw = pmul(pw, p)
        if c:
            out = padd(out, {k: c * v for k, v in pw.items()})
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', required=True); ap.add_argument('--control', choices=['SCALE', 'SHIFT'])
    o = ap.parse_args()
    SIN = [Fr(0), Fr(1), Fr(0), Fr(-1, 6), Fr(0), Fr(1, 120)]
    EXPM1 = [Fr(0), Fr(1), Fr(1, 2), Fr(1, 6), Fr(1, 24), Fr(1, 120)]
    if o.control == 'SHIFT':
        SIN = [Fr(0), Fr(1), Fr(1, 10), Fr(-1, 6), Fr(0), Fr(1, 120)]
    if o.control == 'SCALE':
        EXPM1 = [c * Fr(11, 10) for c in EXPM1]

    def T(r, e):
        s = compose(SIN, e)
        return padd(r, s, -1), padd(padd(e, compose(EXPM1, r)), s, -1)
    r0, e0 = {(1, 0): Fr(1)}, {(0, 1): Fr(1)}
    r, e = r0, e0
    lin = None
    for _ in range(6):
        r, e = T(r, e)
    g = {}
    linr = {k: v for k, v in r.items() if sum(k) == 1}; line = {k: v for k, v in e.items() if sum(k) == 1}
    low = [k for k in list(r) + list(e) if sum(k) == 2]
    g['LIN_identity_plus_degree_3'] = (linr == {(1, 0): Fr(1)} and line == {(0, 1): Fr(1)} and not low)
    z, w = sp.symbols('z w')
    s3 = sp.sqrt(3); om = sp.Rational(-1, 2) + sp.I * s3 / 2; omb = sp.conjugate(om)
    eta = (z - w) / (sp.I * s3); rho = z - om * eta

    def to_zw(p):
        ex = sum(sp.Rational(v.numerator, v.denominator) * rho ** i * eta ** j for (i, j), v in p.items())
        return sp.Poly(sp.expand(ex), z, w)
    R, E = to_zw(r), to_zw(e)
    Fz = sp.Poly(sp.expand(R.as_expr() + om * E.as_expr()), z, w)
    Fw = sp.Poly(sp.expand(R.as_expr() + omb * E.as_expr()), z, w)
    cz = {m: sp.nsimplify(sp.simplify(c)) for m, c in Fz.terms()}; cw = {m: sp.nsimplify(sp.simplify(c)) for m, c in Fw.terms()}
    cz = {m: sp.simplify(c) for m, c in cz.items() if sp.simplify(c) != 0}; cw = {m: sp.simplify(c) for m, c in cw.items() if sp.simplify(c) != 0}
    bad_z = sorted(m for m in cz if m != (1, 0) and m[0] + 2 * m[1] < 4)
    bad_w = sorted(m for m in cw if m != (0, 1) and m[0] + 2 * m[1] < 5)
    g['S5Z_Fz_minus_z_weighted_order_ge_4'] = (cz.get((1, 0)) == 1 and not bad_z)
    g['S5W_Fw_minus_w_weighted_order_ge_5'] = (cw.get((0, 1)) == 1 and not bad_w)
    g['P4_no_w2_in_Fz'] = (0, 2) not in cz
    Q = lambda p, q: sp.Rational(p) + sp.Rational(q) * s3 * sp.I
    MU, C40 = Q('-1/2', '-2/3'), Q('-1/16', '7/144'); D31, CC = Q('1/3', '-1/9'), Q('-61/2160', '43/6480')
    eq = lambda a_, b_: sp.simplify(a_ - b_) == 0
    lead = (eq(cz.get((4, 0), 0), C40) and eq(cz.get((2, 1), 0), MU) and eq(cw.get((1, 2), 0), sp.conjugate(MU))
            and eq(cw.get((3, 1), 0), D31) and eq(cw.get((5, 0), 0), CC))
    real = all(eq(cw.get((q_, p_), 0), sp.conjugate(c)) for (p_, q_), c in cz.items() if p_ + q_ <= 5)
    g['LEAD_constants_and_real_structure'] = bool(lead and real)
    g = {k: bool(v) for k, v in g.items()}; ok = all(g.values())
    info = dict(total_degree=DEG,
                Fz_monomials_weighted_order_le_5={str(m): str(c) for m, c in sorted(cz.items()) if m[0] + 2 * m[1] <= 5},
                Fw_monomials_weighted_order_le_5={str(m): str(c) for m, c in sorted(cw.items()) if m[0] + 2 * m[1] <= 5},
                offending_Fz=[str(m) for m in bad_z], offending_Fw=[str(m) for m in bad_w])
    for k in sorted(g):
        print(k, 'PASS' if g[k] else 'FAIL')
    print('RESULT', 'PASS' if ok else 'FAIL', '(control %s)' % o.control if o.control else '', '| exact algebra')
    with open(o.out, 'w', encoding='utf-8', newline='\n') as f:
        json.dump({'gates': g, 'info': info, 'all_pass': ok, 'control': o.control,
                   'script': 'dyad_open20_an_stage3c_w7_structure.py'}, f, indent=1, sort_keys=True)
        f.write('\n')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
