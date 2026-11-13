#!/usr/bin/env python3
"""dyad_open20_an_seed_q1_check.py -- owner check of the explicit inequalities in the co-owner's written argument for
the seed (Q1), (Q2) of the tube lemma (draft PR #257, commit def878f5; design 3b r2, section 4).

DEVELOPMENT / SESSION CHECK.  Not a certificate.  It proves no seed: (Q2) rests on a literature statement (L1) whose
constant is not computed, and the tube hypotheses (G), (A), (B) are development results.  No statement about the jump.

Objects (design 3b section 3; the tau of the certificate has the fixed decimal coefficients of the library):
    xi = c x,  tau(x) = A3 x^-3 + A2 x^-2 + A1 x^-1 + kappa log x   (principal logs),
    D0 = {xi in Omega0: Re tau > s0, h0 > c0},  D1 = {xi in Omega1: Re tau < s1, h1 > c1},  D_j(H) = D_j and {h_j > H}.
Identity:  3 xi^3 tau = 3 A3 c^3 + 3 A2 c^2 xi + 3 A1 c xi^2 + 3 kappa xi^3 (log xi - log c).
Owner correction to the draft: A3 is a 15-digit decimal, so 3 A3 c^3 = 1 + e3 with e3 != 0; e3 enters the bound:
    |3 xi^3 tau - 1| <= E(r) = |e3| + a2 r + a1 r^2 + k3 r^3 (|log r| + |log c| + pi/2),   0 < r <= 1/e,
    a2 = |3 A2 c^2|, a1 = |3 A1 c|, k3 = 3 |kappa|   (|arg xi| < pi/2 on both chart sectors).
(Q1.2)  E(r0) + 3 S r0^3 < sin(pi/8),  S = max(|s0|, |s1|)   =>  D_j and {r <= r0} lies in the angular window of S_j.
(Q1.3)  |tau| <= M(r0) on r0 <= r < 0.60;  H > max(c0, c1, M(r0))  =>  D_j(H) inside {r < r0}.
(Q2.1)  R_j >= K_j r^(18 + Re alpha) on D_j and {r <= r0},  K_j = eps_j e^(-|Im alpha| pi/2) C_B^-3 C_tau^-3,
        C_tau = |A3 c^3| + (a2 r0 + a1 r0^2 + k3 r0^3 (|log r0| + |log c| + pi/2))/3,  C_B = C_tau + (1 + S) r0^3.

Gates (exit 0 iff all pass):
  ANG    exact: the chart edges -1/5 and 1/2 lie inside the windows of S_0 and S_1; cos(5 pi/8) = -sin(pi/8) and
         cos(3 pi/8) = sin(pi/8) to ball accuracy.
  COEF   the bounds proposed in the draft hold: a2 <= 2, a1 <= 2, k3 <= 10, |log c| <= 3, S <= 4; and |e3| < 1e-13.
  Q12    (Q1.2) holds at r0 (ball arithmetic); the largest grid value k/200 at which it holds is recorded, and it
         holds at every smaller grid value and at r = 1e-3 (the draft's value).
  Q13    M(r0) and the level H are finite positive balls; H > c0, c1.
  Q2     18 + Re alpha = 240/19 and 39 - 240/19 = 501/19 exactly; K_0, K_1 > 0.
  SND    independent sampling (mpmath, 30 digits, own formulas, 41 radii x 201 angles per sector inside r <= r0, and
         60 x 201 on the annulus): |3 xi^3 tau - 1| <= E(r); every sample of D_j lies in the window of S_j; on D_j
         the two tube factors are <= C_B r^-3 and <= C_tau r^-3 and R_j >= K_j r^(240/19); |tau| <= M(r0) on the
         annulus; both D_j have samples.
Controls (each must exit 1 at the named gate):
  --control BIG    r0 = 0.30                               -> Q12
  --control HALFE  the sampling compares with E(r)/2       -> SND
Usage: python3 -I -B dyad_open20_an_seed_q1_check.py --out OUT.json [--control NAME]
"""
import os, sys, json, argparse
from fractions import Fraction as Fr
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from flint import acb, arb, ctx
import mpmath as mp
import dyad_open20_an_stage3c_lib as L


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', required=True); ap.add_argument('--control', choices=['BIG', 'HALFE'])
    o = ap.parse_args()
    ctx.prec = 200
    g, info = {}, {}
    K = L.Consts(); TAU = L.tau_coefficients(); A3, A2, A1, KA = TAU; c = K.c
    up = L._up
    TB = [L.Tube(K, TAU, 0), L.Tube(K, TAU, 1)]
    pi = arb.pi(); s8 = (pi / 8).sin()

    # ANG
    ang = (Fr(-1, 5) > Fr(-5, 24)) and (Fr(1, 2) < Fr(1, 3) + Fr(5, 24)) and (Fr(1, 3) - Fr(5, 24) == Fr(1, 8))
    ang = ang and ((5 * pi / 8).cos() + s8).contains(0) and ((3 * pi / 8).cos() - s8).contains(0)
    g['ANG_chart_edges_and_cosines'] = bool(ang)

    # constants
    e3 = up(3 * A3 * c ** 3 - 1); a2 = up(3 * A2 * c * c); a1 = up(3 * A1 * c); k3 = 3 * up(KA); lc = up(c.log())
    S = up(acb(TB[0].s)).max(up(acb(TB[1].s))); A3c = up(A3 * c ** 3)
    g['COEF_bounds_of_the_draft'] = bool(a2 <= 2 and a1 <= 2 and k3 <= 10 and lc <= 3 and S <= 4 and e3 < arb('1e-13'))
    f6 = lambda v: float('%.6g' % float(arb(v).upper()))
    info['constants'] = dict(e3_upper=f6(e3), a2=f6(a2), a1=f6(a1), k3=f6(k3), abs_log_c=f6(lc), S=f6(S),
                             s0=float('%.6g' % float(TB[0].s.mid())), s1=float('%.6g' % float(TB[1].s.mid())),
                             c0=float('%.6g' % float(TB[0].cw.mid())), c1=float('%.6g' % float(TB[1].cw.mid())),
                             sin_pi_8=float('%.6g' % float(s8.mid())))

    def bracket(r):
        return abs(r.log()) + lc + pi / 2

    def E(r):
        assert r < arb(-1).exp() and r > 0
        return e3 + a2 * r + a1 * r ** 2 + k3 * r ** 3 * bracket(r)

    def q12(r):
        return bool(E(r) + 3 * S * r ** 3 < s8)

    grid = [arb(k) / 200 for k in range(1, 73)]                 # 0.005 ... 0.36 < 1/e
    okg = [q12(r) for r in grid]
    kmax = max([i for i, v in enumerate(okg) if v], default=-1)
    rmax = Fr(kmax + 1, 200) if kmax >= 0 else None
    r0q = Fr(3, 10) if o.control == 'BIG' else rmax
    r0 = arb(r0q.numerator) / r0q.denominator
    g['Q12_inequality_at_r0'] = bool(kmax >= 0 and q12(r0) and all(okg[:kmax + 1]) and q12(arb('0.001')))
    info['Q12'] = dict(r0=float(r0q), largest_grid_value_passing=float(rmax) if rmax else None,
                       lhs_at_r0=f6(E(r0) + 3 * S * r0 ** 3), lhs_at_0p05=f6(E(arb('0.05')) + 3 * S * arb('0.05') ** 3),
                       lhs_at_0p001=f6(E(arb('0.001')) + 3 * S * arb('0.001') ** 3))

    # Q13
    def M(r):
        return A3c / r ** 3 + a2 / (3 * r * r) + a1 / (3 * r) + (k3 / 3) * bracket(r)
    rows = {}
    okm = True
    for name, r in (('r0', r0), ('0.05', arb('0.05')), ('0.001', arb('0.001'))):
        m = M(r); H = m.max(TB[0].cw).max(TB[1].cw)
        okm = okm and bool(m > 0 and m.is_finite() and H >= TB[0].cw and H >= TB[1].cw)
        rows[name] = dict(M_upper=f6(m), level_H_must_exceed=f6(H))
    g['Q13_levels'] = bool(okm); info['Q13'] = rows

    # Q2
    ex = Fr(18) + Fr(-102, 19)
    Ct = A3c + (a2 * r0 + a1 * r0 ** 2 + k3 * r0 ** 3 * bracket(r0)) / 3
    Cb = Ct + (1 + S) * r0 ** 3
    low = lambda v: arb(v.lower())
    Kj = [low(TB[j].eps) * (-up(acb(K.ALPHA.imag)) * pi / 2).exp() / (Cb ** 3 * Ct ** 3) for j in (0, 1)]
    g['Q2_exponents_and_constants'] = bool(ex == Fr(240, 19) and Fr(39) - ex == Fr(501, 19) and K.ALPHA.real.contains(arb(-102) / 19)
                                           and all(k > 0 for k in Kj))
    info['Q2'] = dict(exponent_of_the_tube_bound='240/19', exponent_of_the_ratio='501/19', C_tau=f6(Ct), C_B=f6(Cb),
                      K0_lower=float('%.6g' % float(Kj[0].lower())), K1_lower=float('%.6g' % float(Kj[1].lower())),
                      eps0=float('%.6g' % float(TB[0].eps.mid())), eps1=float('%.6g' % float(TB[1].eps.mid())))

    # SND: independent sampling
    mp.mp.dps = 30
    tm = lambda z: mp.mpc(mp.mpf(z.real.mid().str(40, radius=False)), mp.mpf(z.imag.mid().str(40, radius=False)))
    cm = tm(c); T = [mp.mpc(mp.mpf(re), mp.mpf(im)) for re, im in L.TAU_DECIMALS]
    al = mp.mpc(mp.mpf(-102) / 19, -16 * mp.sqrt(3) / 19); th0 = mp.pi / 2 - mp.pi / 8

    def tau(xi):
        x = xi / cm
        return T[0] / x ** 3 + T[1] / x ** 2 + T[2] / x + T[3] * mp.log(x)
    ts = tau(mp.mpf('0.4') * mp.expjpi(mp.mpf(1) / 6))
    rot = [mp.expj(th0), -mp.expj(-th0)]
    sw = [ts.real - mp.mpf('0.25'), ts.real + mp.mpf('0.25')]; cw = [(rot[j] * ts).real - mp.mpf('0.15') for j in (0, 1)]
    xia = lambda xi: mp.exp((al * mp.log(xi)).real)
    epsm = [mp.mpf('0.002') / (xia(mp.mpf('0.4') * mp.expjpi(mp.mpf(1) / 6)) * mp.mpf('1.25') ** (-3) * (cw[j] + mp.mpf('0.15')) ** (-3))
            for j in (0, 1)]
    chart = [(mp.mpf('-0.20'), mp.mpf('0.30')), (mp.mpf('0.03'), mp.mpf('0.50'))]
    fu = lambda v: mp.mpf(arb(v).upper().str(30, radius=False))
    fl = lambda v: mp.mpf(arb(v).lower().str(30, radius=False))
    e3m, a2m, a1m, k3m, lcm, Sm = [fu(v) for v in (e3, a2, a1, k3, lc, S)]
    Em = lambda r: e3m + a2m * r + a1m * r ** 2 + k3m * r ** 3 * (abs(mp.log(r)) + lcm + mp.pi / 2)
    fac = mp.mpf('0.5') if o.control == 'HALFE' else mp.mpf(1)
    r0m = mp.mpf(r0q.numerator) / r0q.denominator; Ctm, Cbm, Mm = fu(Ct), fu(Cb), fu(M(r0)); Km = [fl(k) for k in Kj]
    bad = dict(E=0, window=0, factors=0, radius=0, annulus=0); nD = [0, 0]; worstE = mp.mpf(0); outer = [0, 0]
    for j in (0, 1):
        lo, hi = chart[j]
        for a in range(201):
            th = (lo + (hi - lo) * (mp.mpf(a) + mp.mpf('0.5')) / 201) * mp.pi
            for k in range(41):
                r = r0m * mp.mpf(10) ** (-mp.mpf(k) / 8)
                xi = r * mp.expj(th); t = tau(xi)
                dev = abs(3 * xi ** 3 * t - 1); worstE = max(worstE, dev / Em(r))
                if dev > fac * Em(r):
                    bad['E'] += 1
                first = (1 if j == 0 else -1) * (t.real - sw[j]) + 1; second = (rot[j] * t).real
                if first > 1 and second > cw[j]:
                    nD[j] += 1
                    if abs(th - j * mp.pi / 3) > 5 * mp.pi / 24:
                        bad['window'] += 1
                    if first > Cbm / r ** 3 or second > Ctm / r ** 3:
                        bad['factors'] += 1
                    if epsm[j] * xia(xi) * first ** (-3) * second ** (-3) < Km[j] * r ** (mp.mpf(240) / 19):
                        bad['radius'] += 1
            for k in range(60):
                r = r0m + (mp.mpf('0.60') - r0m) * mp.mpf(k) / 60
                xi = r * mp.expj(th); t = tau(xi)
                if abs(t) > Mm:
                    bad['annulus'] += 1
                first = (1 if j == 0 else -1) * (t.real - sw[j]) + 1; second = (rot[j] * t).real
                if first > 1 and second > cw[j] and abs(th - j * mp.pi / 3) > 5 * mp.pi / 24:
                    outer[j] += 1
    g['SND_independent_sampling'] = bool(not any(bad.values()) and nD[0] > 0 and nD[1] > 0)
    info['SND'] = dict(samples_per_sector=201 * 41, annulus_samples_per_sector=201 * 60, violations=bad, samples_in_D0=nD[0],
                       samples_in_D1=nD[1], largest_ratio_deviation_over_E=float(mp.nstr(worstE, 6)),
                       samples_of_D_j_outside_the_window_at_radius_above_r0=dict(D0=outer[0], D1=outer[1]))

    g = {k: bool(v) for k, v in g.items()}; ok = all(g.values())
    for k in sorted(g):
        print(k, 'PASS' if g[k] else 'FAIL')
    print('RESULT', 'PASS' if ok else 'FAIL', '(control %s)' % o.control if o.control else '', '| SESSION check; not a certificate; no seed is proved')
    with open(o.out, 'w', encoding='utf-8', newline='\n') as f:
        json.dump({'gates': g, 'info': info, 'all_pass': ok, 'control': o.control,
                   'status': 'SESSION owner check of explicit inequalities; not a certificate; no seed is proved',
                   'script': 'dyad_open20_an_seed_q1_check.py'}, f, indent=1, sort_keys=True)
        f.write('\n')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
