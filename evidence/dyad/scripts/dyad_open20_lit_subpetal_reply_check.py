#!/usr/bin/env python3
"""dyad_open20_lit_subpetal_reply_check.py -- owner check of the numbers and the one inequality in LIT's reply on subpetal
orbit constants (pipes/DYAD/20261111-LIT-subpetal-orbit-constant-search.md; LIT report at rtg-lit e053e73e..., SESSION).

Nothing here is a certificate for the dyad map. No map value is computed. Inputs: the stage-3a route output (lower bounds
K1, K2 of the m = 2 chart) and the stage-2b output (the matching radii that were used).

INF-009 (as transcribed in dyad_open20_an_stage3_apriori_route_check.py), k = 3:
  A(rho) = rho^k + K rho^(k+1);  E(rho) = K rho + (k+1)/2 rho^k (1 + K rho)^2 (1 - A)^(-k-2);
  (i) A <= min(1/2, sin(2 eta/k));  (ii) eps0 = E(rho) < min(sin eta, cos eta/(cos eta + sin eta)).
LIT's claim (screen section 3): under (i) and eps0 < sin eta,
  |f^n(x)|^k <= |x|^k / ((1 - eps0/sin eta) |1 + k n x^k|),  and  |1 + z| >= cos(theta/2) (1 + |z|) for arg z = theta.

Gates (exit 0 iff all pass):
  G0  input hashes; both inputs report all_pass.
  T1  LIT's radius table for K = 13.52: the caps for eps0 = 0.25, < 0.5, < sin(pi/4), < 1, rounded down to four decimals,
      are 0.0184, 0.0369, 0.0522, 0.0737.
  T2  the owner's stage-3a cap "rho <= 0.019" (design record section 8) is the cap of the class used there:
      K = 2 K1 + K2 (the radius-2 ball of INF-010) with eps0 < 1/2 at eta = pi/4; (i) is not binding at that rho.
      Reported, not gated: LIT's four caps recomputed for that class.
  T3  exact identity |1 + t e^(i theta)|^2 - c(theta)^2 (1 + t)^2 = (1 - cos theta)(1 - t)^2 / 2 with c = cos(theta/2)
      (sympy), and on a grid of (t, theta) the inequality |1 + t e^(i theta)| >= c(theta)(1 + t) holds, with equality
      at t = 1 (the constant is sharp).
  T4  LIT's example constants at eta = pi/4, eps0 = 0.25: 1.5469 (modulus form), 2.1877 (at arg x^k = pi/2), 4.0423
      (all of the domain, theta = pi - eta), and INF-009's C = 7.66.
  T5  [NUM] illustration, not a proof: for f = x - x^4 + K u x^5 with |u| = 1 (so |g| = K |x|^5), K = 13.52, rho with
      eps0 = 0.25, eta = pi/4, delta = rho^3/2, the modulus-form bound holds along 40 orbits of 2000 steps started at
      seeded random points of the principal component.
  T6  every matching radius used in stage 2b (r_m) is larger than the largest cap of T1 (eps0 < 1): the points where
      the stage-2b harness meets the truncated series lie outside every domain this criterion admits in this chart.
Controls (each must exit 1 at the named gate): --control KCLASS (T1 computed with K = 2 K1 + K2),
  --control SEC (c(theta) = cos(theta/3) in T3).
Usage: python3 -I -B dyad_open20_lit_subpetal_reply_check.py --route route_check.json --scout jump_scout.json --out OUT.json
"""
import sys, json, argparse, hashlib, random
import mpmath as mp
import sympy as sp

sys.dont_write_bytecode = True
ROUTE_SHA = 'eb23e4ba165e017149bb36b08a9a7886367c2de296ae0e45e6de084a71732f0d'
SCOUT_SHA = '610433e549415492a3a5772531a14e596c5d0cee11bed306acd9e6acabd3a268'
k = 3
mp.mp.dps = 40


def A_(r, K): return r ** k + K * r ** (k + 1)
def E_(r, K): return K * r + mp.mpf(k + 1) / 2 * r ** k * (1 + K * r) ** 2 * (1 - A_(r, K)) ** (-k - 2)


def cap(K, eps):
    """The rho with E(rho) = eps (E is increasing on the range used); bisection."""
    lo, hi = mp.mpf(0), mp.mpf(1) / (2 * K)
    while E_(hi, K) < eps: hi *= 2
    for _ in range(200):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if E_(mid, K) < eps else (lo, mid)
    return lo


def down4(x): return mp.floor(x * 10 ** 4) / 10 ** 4


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--route', required=True); ap.add_argument('--scout', required=True)
    ap.add_argument('--out', required=True); ap.add_argument('--control', choices=['KCLASS', 'SEC'])
    a = ap.parse_args()
    gates, info = {}, {}
    hr = hashlib.sha256(open(a.route, 'rb').read()).hexdigest(); hs = hashlib.sha256(open(a.scout, 'rb').read()).hexdigest()
    route = json.load(open(a.route)); scout = json.load(open(a.scout))
    gates['G0_route_hash'] = hr == ROUTE_SHA; gates['G0_scout_hash'] = hs == SCOUT_SHA
    gates['G0_inputs_all_pass'] = bool(route['all_pass']) and bool(scout['all_pass'])
    lb = route['info']['lower_bounds_from_stage1_jets']
    K1, K2 = mp.mpf(lb['K1']), mp.mpf(lb['K2'])
    K_lit = mp.mpf('13.52'); K_own = 2 * K1 + K2
    info['K_lit'] = '13.52'; info['K1_plus_K2'] = mp.nstr(K1 + K2, 8); info['K_owner_2K1_plus_K2'] = mp.nstr(K_own, 8)
    gates['G0_K_lit_below_K1_plus_K2'] = K_lit <= K1 + K2          # 13.52 is a rounded-down value of K1 + K2
    eta = mp.pi / 4
    eps_rows = [('0.25', mp.mpf('0.25')), ('0.5', mp.mpf('0.5')), ('sin(pi/4)', mp.sin(eta)), ('1', mp.mpf(1))]

    # T1
    K_t1 = K_own if a.control == 'KCLASS' else K_lit
    printed = ['0.0184', '0.0369', '0.0522', '0.0737']
    caps = [cap(K_t1, e) for _, e in eps_rows]
    info['T1_caps'] = {n: mp.nstr(c, 8) for (n, _), c in zip(eps_rows, caps)}
    gates['T1_lit_radius_table'] = all(down4(c) == mp.mpf(p) for c, p in zip(caps, printed))

    # T2
    c_own = cap(K_own, mp.mpf('0.5'))
    info['T2_owner_cap'] = mp.nstr(c_own, 8); info['T2_A_at_cap'] = mp.nstr(A_(c_own, K_own), 6)
    info['T2_caps_owner_class'] = {n: mp.nstr(cap(K_own, e), 8) for n, e in eps_rows}
    gates['T2_owner_cap_is_0.019'] = mp.nstr(c_own, 2) == '0.019'
    gates['T2_condition_i_not_binding'] = A_(c_own, K_own) < min(mp.mpf('0.5'), mp.sin(2 * eta / k))
    gates['T2_ii_bound_is_one_half'] = mp.almosteq(min(mp.sin(eta), mp.cos(eta) / (mp.cos(eta) + mp.sin(eta))), mp.mpf('0.5'))

    # T3
    t, th = sp.symbols('t theta', real=True)
    div = 3 if a.control == 'SEC' else 2
    c_sym = sp.cos(th / div)
    resid = sp.simplify(sp.expand_trig(sp.expand((1 + 2 * t * sp.cos(th) + t ** 2) - c_sym ** 2 * (1 + t) ** 2
                                                 - (1 - sp.cos(th)) * (1 - t) ** 2 / 2)))
    gates['T3_exact_identity'] = resid == 0
    worst, eq_gap = mp.mpf(1), mp.mpf(0)
    for i in range(1, 60):
        theta = mp.pi * i / 60
        cc = mp.cos(theta / div)
        for j in range(0, 81):
            tt = mp.power(10, mp.mpf(j - 40) / 10)
            worst = min(worst, abs(1 + tt * mp.expjpi(theta / mp.pi)) - cc * (1 + tt))
        eq_gap = max(eq_gap, abs(abs(1 + mp.expjpi(theta / mp.pi)) - 2 * mp.cos(theta / 2)))
    info['T3_min_slack_on_grid'] = mp.nstr(worst, 6); info['T3_equality_gap_at_t_1'] = mp.nstr(eq_gap, 3)
    gates['T3_inequality_on_grid'] = worst >= -mp.mpf(10) ** (-30)
    gates['T3_sharp_at_t_1'] = eq_gap < mp.mpf(10) ** (-30)

    # T4
    e0 = mp.mpf('0.25'); m0 = 1 / (1 - e0 / mp.sin(eta))
    vals = dict(modulus=m0, at_half_pi=m0 * mp.sec(mp.pi / 4), whole_domain=m0 * mp.sec((mp.pi - eta) / 2),
                C_inf009=(3 + 2 * e0) / (mp.sin(eta) - e0))
    info['T4'] = {n: mp.nstr(v, 8) for n, v in vals.items()}
    gates['T4_example_constants'] = (mp.nstr(vals['modulus'], 5) == '1.5469' and mp.nstr(vals['at_half_pi'], 5) == '2.1877'
                                     and mp.nstr(vals['whole_domain'], 5) == '4.0423' and mp.nstr(vals['C_inf009'], 3) == '7.66')

    # T5 [NUM] illustration
    mp.mp.dps = 25
    rho = cap(K_lit, e0); delta = rho ** k / 2; fac = 1 / (1 - e0 / mp.sin(eta))
    rnd = random.Random(20261111); max_ratio = mp.mpf(0); ok = True
    for _ in range(40):
        theta = (mp.pi / 2 - eta) * (2 * rnd.random() - 1)
        xk = delta * mp.expj(theta) + delta * mp.sqrt(rnd.random()) * 0.999 * mp.expj(2 * mp.pi * rnd.random())
        x0 = mp.root(xk, k); u = mp.expj(2 * mp.pi * rnd.random()); x = x0; x0k = x0 ** k
        for n in range(1, 2001):
            x = x - x ** 4 + K_lit * u * x ** 5
            ratio = abs(x) ** k * abs(1 + k * n * x0k) / (fac * abs(x0k))
            max_ratio = max(max_ratio, ratio)
            if ratio > 1: ok = False
    mp.mp.dps = 40
    info['T5_rho'] = mp.nstr(rho, 6); info['T5_max_ratio_to_bound'] = mp.nstr(max_ratio, 4)
    gates['T5_NUM_no_violation_40x2000'] = ok

    # T6
    rms = sorted({mp.mpf(c['r_m']) for c in scout['configs']})
    sup_cap = cap(K_lit, mp.mpf(1))
    info['T6_stage2b_matching_radii'] = [mp.nstr(r, 3) for r in rms]; info['T6_sup_cap'] = mp.nstr(sup_cap, 6)
    gates['T6_matching_radii_outside_every_cap'] = min(rms) > sup_cap

    allp = all(gates.values())
    out = dict(script='dyad_open20_lit_subpetal_reply_check.py', control=a.control, gates=gates, info=info, all_pass=allp,
               status='owner check of a LIT reply; SESSION; not a certificate for the dyad map', mpmath=mp.__version__,
               sympy=sp.__version__)
    json.dump(out, open(a.out, 'w'), indent=1, sort_keys=True)
    for g, v in sorted(gates.items()): print(('PASS ' if v else 'FAIL ') + g)
    for n, v in sorted(info.items()): print(f'  {n}: {v}')
    print('RESULT ' + ('PASS' if allp else 'FAIL'))
    sys.exit(0 if allp else 1)


if __name__ == '__main__':
    main()
