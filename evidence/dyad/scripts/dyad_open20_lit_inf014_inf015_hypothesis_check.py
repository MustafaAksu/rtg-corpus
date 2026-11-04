#!/usr/bin/env python3
"""dyad_open20_lit_inf014_inf015_hypothesis_check.py -- exact owner check of the DYAD-side hypotheses that the LIT findings
INF-014 (flower theorem, Lopez-Hernanz--Rosas 2025, Thm 1.3 form (A)) and INF-015 (Lopez-Hernanz--Raissy--Ribon--Sanz 2021,
Thms 5.1/7.1) take from DYAD (pipes/DYAD/20261103-LIT-flower-thm13-lifted-germs.md, 20261104-LIT-imrn2021-asymptotic-orbits.md).

Exact arithmetic in Q(i sqrt3) and E = Q(i sqrt3)[a]/(P), reusing the classes and constants of the stage-1 script
(dyad_open20_an_stage1_prep.py; F = T^6 jets from dyad_h4_real_route_check.T6). No floating point is used for any gate.
Gates (exit 0 iff all pass):
  G0  stage1_prep.json SHA-256 = 2c9ae637...4739, all_pass, k = 3, m = 2.
  H1  2A = alpha mu and B = alpha c40, hence P'(u) = 2Au + B = alpha (c40 + mu u) = alpha G(0,u) identically, with
      alpha = -102/19 - 16 sqrt3/19 i (INF-014 Step 2).  So b/a = P'(a_sigma)/ell_sigma = alpha on both branches.
  H2  ell_sigma = c40 + mu a_sigma != 0 on both branches: the only zero of u -> c40 + mu u is u0 = -c40/mu, and P(u0) != 0.
      Also ell_+ + ell_- = 2 c40 - mu B/A = 0 (INF-014's ell_- = -ell_+, by Vieta).
  H3  Re alpha = -102/19 < 0 and alpha not in Q_{>0} (alpha is not real).
  H4  the lift (z, w) = (x, x^2 u) of the FULL analytic germ has order 4 with x' - x = x^4 G: every raw monomial z^p w^q of F_z
      with p + 2q < 4, other than z, and of F_w with p + 2q < 5, other than w, has coefficient 0. All such monomials have total
      degree <= 4, so the exact degree-4 jet of F decides it for the analytic germ (F = T^6 is entire).
  H5  the degree-2 and degree-3 raw terms are only the identity, mu z^2 w (in F_z) and conj(mu) z w^2 (in F_w).
Controls (exit 1): --control ALPHA (alpha + 1/19 used in H1), --control MUBAR (conj(mu) in place of mu in H1).
Usage: python3 -I -B dyad_open20_lit_inf014_inf015_hypothesis_check.py --stage1 stage1_prep.json --out OUT.json [--control C]
"""
import os, sys, json, argparse, hashlib
from fractions import Fraction as Fr
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import dyad_open20_an_stage1_prep as S1
from dyad_h4_real_route_check import T6

STAGE1_SHA = '2c9ae6376e0c482f2ba520a7ea8e2b38606a6821f7ac3bfa259d4d6020d04739'
Qs = S1.Qs


def to_zw(D):
    """Exact (z, w) coefficients of F = T^6 to total degree D, z = rho + omega eta, w = rho + conj(omega) eta."""
    R, E = T6(D)
    om, omb = S1.OMEGA, S1.OMEGA.conj()
    den = om - omb                      # = i sqrt3
    # rho = (-omb z + om w)/den, eta = (z - w)/den: linear forms as dicts {(p,q): coeff}
    rho = {(1, 0): -omb / den, (0, 1): om / den}
    eta = {(1, 0): Qs(1) / den, (0, 1): Qs(-1) / den}

    def mul(a, b):
        out = {}
        for (p1, q1), c1 in a.items():
            for (p2, q2), c2 in b.items():
                if p1 + q1 + p2 + q2 <= D:
                    key = (p1 + p2, q1 + q2); out[key] = out.get(key, Qs(0)) + c1 * c2
        return out

    powr = {0: {(0, 0): Qs(1)}}; powe = {0: {(0, 0): Qs(1)}}
    for n in range(1, D + 1):
        powr[n] = mul(powr[n - 1], rho); powe[n] = mul(powe[n - 1], eta)

    def subst(P):
        out = {}
        for (i, j), c in P.items():
            for key, v in mul(powr[i], powe[j]).items():
                out[key] = out.get(key, Qs(0)) + Qs(c) * v
        return {k: v for k, v in out.items() if not v.iszero()}

    Rz, Ez = subst(R), subst(E)
    keys = set(Rz) | set(Ez)
    Fz = {k: Rz.get(k, Qs(0)) + om * Ez.get(k, Qs(0)) for k in keys}
    Fw = {k: Rz.get(k, Qs(0)) + omb * Ez.get(k, Qs(0)) for k in keys}
    return ({k: v for k, v in Fz.items() if not v.iszero()}, {k: v for k, v in Fw.items() if not v.iszero()})


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--stage1', required=True); ap.add_argument('--out', required=True)
    ap.add_argument('--control', choices=['ALPHA', 'MUBAR']); o = ap.parse_args()
    raw = open(o.stage1, 'rb').read(); d = json.loads(raw.decode('utf-8'))
    g, info = {}, {}
    g['G0_stage1'] = hashlib.sha256(raw).hexdigest() == STAGE1_SHA and d.get('all_pass') is True and d.get('k') == 3 and d.get('m') == 2
    MU, C40, A, B, CC = S1.MU, S1.C40, S1.A_, S1.B_, S1.CC
    alpha = Qs(Fr(-102, 19), Fr(-16, 19))
    g['G0_alpha_equals_stage1'] = alpha == S1.ALPHA
    al = alpha + Fr(1, 19) if o.control == 'ALPHA' else alpha
    mu_used = MU.conj() if o.control == 'MUBAR' else MU
    g['H1_2A_eq_alpha_mu'] = (2 * A) == al * mu_used
    g['H1_B_eq_alpha_c40'] = B == al * C40
    info['A'] = repr(A); info['B'] = repr(B); info['alpha_mu'] = repr(al * mu_used); info['alpha_c40'] = repr(al * C40)
    u0 = -C40 / MU
    Pu0 = A * u0 * u0 + B * u0 + CC
    g['H2_ell_nonzero_both_branches'] = not Pu0.iszero()
    info['u0'] = repr(u0); info['P(u0)'] = repr(Pu0)
    g['H2_ell_plus_plus_ell_minus_zero'] = (2 * C40 - MU * B / A).iszero()
    g['H3_Re_alpha_negative'] = alpha.p < 0 and alpha.p == Fr(-102, 19)
    g['H3_alpha_not_real'] = alpha.q != 0
    Fz, Fw = to_zw(4)
    bad_z = {k: repr(v) for k, v in Fz.items() if k[0] + 2 * k[1] < 4 and k != (1, 0)}
    bad_w = {k: repr(v) for k, v in Fw.items() if k[0] + 2 * k[1] < 5 and k != (0, 1)}
    g['H4_lift_order4_full_germ'] = not bad_z and not bad_w and Fz.get((1, 0)) == 1 and Fw.get((0, 1)) == 1
    info['H4_offending'] = {'Fz': {str(k): v for k, v in bad_z.items()}, 'Fw': {str(k): v for k, v in bad_w.items()}}
    low_z = {k: v for k, v in Fz.items() if sum(k) <= 3}; low_w = {k: v for k, v in Fw.items() if sum(k) <= 3}
    g['H5_low_degree_terms'] = (set(low_z) == {(1, 0), (2, 1)} and low_z[(2, 1)] == MU
                                and set(low_w) == {(0, 1), (1, 2)} and low_w[(1, 2)] == MU.conj())
    g['H5_c40_d31_from_jet'] = Fz.get((4, 0)) == C40 and Fw.get((3, 1)) == S1.D31
    info['F_z_low'] = {str(k): repr(v) for k, v in sorted(low_z.items())}; info['F_w_low'] = {str(k): repr(v) for k, v in sorted(low_w.items())}
    g = {k: bool(v) for k, v in g.items()}; ok = all(g.values())
    for k in sorted(g): print(k, 'PASS' if g[k] else 'FAIL')
    print('RESULT', 'PASS' if ok else 'FAIL', '(control %s)' % o.control if o.control else '')
    with open(o.out, 'w', encoding='utf-8', newline='\n') as f:
        json.dump({'gates': g, 'info': info, 'all_pass': ok, 'control': o.control,
                   'script': 'dyad_open20_lit_inf014_inf015_hypothesis_check.py'}, f, indent=1, sort_keys=True); f.write('\n')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
