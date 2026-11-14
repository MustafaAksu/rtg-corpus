#!/usr/bin/env python3
"""dyad_open20_an_stage3c_w3_zone2.py -- stage 3c-a, work package W3: zone II of the tube lemma on a cover by pieces.

DEVELOPMENT RUN.  Not a certificate; no statement about the jump or about divergence is drawn from it.

What is done.  The part  rho0 <= |xi| <= 0.60  of the chart sector Omega_j (design 3b r2, section 3) is tiled by
rectangles in (log|xi|, arg xi).  Each rectangle is covered by one disc in x = xi / c (a "piece").  A piece is
  out    a wedge condition of D_j fails on the whole piece (no point of D_j in it), or
  pass   it lies in the guard core and (A1), (A2), (B) hold for every point of it that satisfies the wedge conditions
         (lib: piece_check; for j = 1 the step is the inverse step, taken through the local inverse lemma).
A piece that is neither is cut into four (the four parts are examined next, depth first); the first piece that is
neither at the largest depth ends the run with a failure.
If every piece is out or pass, then on the covered part: (G) holds (every point of D_j is in a pass piece, and pass
pieces lie in the core), and (A1), (A2), (B) hold on D_j.

Gates (exit 0 iff all pass):
  G0    stage-2 file hash; its all_pass.
  ENG   engine: structural zeros consistent, tails below 1e-6, theta < 1 on both remainder circles.
  Z2    every piece of the cover is out or pass.
  SND   semantics, by an independent evaluation (mpmath, 60 digits, the full map and its numerical inverse from the
        stage-3b sampling module, with its own formulas for tau, the functionals and the tube radius): at random points
        of D_j in pass pieces, with |d| = R, the step satisfies (A1), (A2) and the exit inequality |d_new| > R(xi_new).
Reported: counts by status and depth, the smallest margins and where they occur.
Controls (each must exit 1 at Z2; run on the outer part |xi| >= 0.40 only):
  --control CORE     the guard core is shrunk to |xi| <= 0.44          (guard property must fail)
  --control SIGMA    sigma = 0.5                                        ((A1) must fail)
  --control QZERO    tube exponents q1 = q2 = 0: R = eps |xi^alpha|     ((B) must fail: no gain along orbits)
Usage: python3 -I -B dyad_open20_an_stage3c_w3_zone2.py --stage2 scout_N216_dps840.json --side 0|1 --rho0 R --out OUT.json
"""
import os, sys, json, math, argparse, hashlib, random, collections
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from flint import acb, arb, ctx
import mpmath as mp
import dyad_open20_an_stage3c_lib as L
import dyad_open20_an_stage3b_tube_sampling as T

STAGE2_SHA = '6ca8c663061ce2fa9e062938a1e6046c932da4cbddccc6e3e2c3de4df68c477e'
H0, MAXDEPTH, SIGMA, KAPPA, RMAX, XENG = 0.02, 5, '0.05', '0.15', 0.60, 1.03


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--stage2', required=True); ap.add_argument('--out', required=True)
    ap.add_argument('--side', type=int, choices=[0, 1], required=True)
    ap.add_argument('--rho0', type=float, required=True)
    ap.add_argument('--control', choices=['CORE', 'SIGMA', 'QZERO'])
    o = ap.parse_args()
    raw = open(o.stage2, 'rb').read(); d2 = json.loads(raw.decode('utf-8'))
    g, info = {}, {}
    g['G0_stage2_input'] = hashlib.sha256(raw).hexdigest() == STAGE2_SHA and d2.get('all_pass') is True
    K, a, SER, MC, rep = L.build_engine()
    g['ENG_engine'] = bool(rep['structural_zeros_consistent'] and rep['max_tail_at_1p02'] < 1e-6
                           and all(m['theta'] < 1 for m in rep['remainder_constants']))
    TAU = L.tau_coefficients()
    j = o.side
    TB = L.Tube(K, TAU, j, q=0 if o.control == 'QZERO' else 9)
    if o.control == 'CORE':
        TB.core = (arb('0.44'), TB.core[1], TB.core[2])
    sigma = '0.5' if o.control == 'SIGMA' else SIGMA
    cabs = float(abs(K.c).mid()); carg = float(K.c.arg().mid())
    alo, ahi = float(TB.chart[1]) * math.pi, float(TB.chart[2]) * math.pi
    ns = math.ceil((math.log(RMAX) - math.log(o.rho0)) / H0); nt = math.ceil((ahi - alo) / H0)
    hs = (math.log(RMAX) - math.log(o.rho0)) / ns / 2; ht = (ahi - alo) / nt / 2
    stack = [(math.log(o.rho0) + (2 * i + 1) * hs, alo + (2 * k + 1) * ht, hs, ht, 0) for i in range(ns) for k in range(nt)]
    cnt = collections.Counter(); bydepth = collections.Counter(); unresolved = []; passed = []
    mins = dict(dre=None, dh=None, margin_B=None); where = {}; max_a2 = 0.0; max_rr = 0.0
    while stack:
        s, t, hs_, ht_, dep = stack.pop()
        xc, r = L.piece_disc(K, s, t, hs_, ht_)                # with the machine check of the covering claim (W8)
        if float(abs(xc).upper()) + r >= XENG:                  # outside the range of the engine: only 'out' is possible
            f, sec = TB.functionals(xc + acb(arb(0, r), arb(0, r)))
            st, inf = ('out', {}) if (f <= 1 or sec <= TB.cw) else ('guard', {})
        else:
            st, inf = L.piece_check(SER, MC, TB, xc, r, sigma, kappa=KAPPA, inverse=(j == 1))
        if st in ('fail', 'guard'):
            if dep < MAXDEPTH:
                for ds in (-hs_ / 2, hs_ / 2):
                    for dt in (-ht_ / 2, ht_ / 2):
                        stack.append((s + ds, t + dt, hs_ / 2, ht_ / 2, dep + 1))
                cnt['cut'] += 1
                continue
            unresolved.append(dict(abs_xi=float('%.5g' % math.exp(s)), arg_over_pi=float('%.5g' % (t / math.pi)), status=st,
                                   why=inf.get('why')))
            break                                                # stop rule: the run ends at the first unresolved piece
        cnt[st] += 1; bydepth['%s_depth%d' % (st, dep)] += 1
        if st == 'pass':
            passed.append((s, t, hs_, ht_))
            for k in mins:
                if mins[k] is None or inf[k] < mins[k]:
                    mins[k] = inf[k]; where[k] = [float('%.5g' % math.exp(s)), float('%.5g' % (t / math.pi))]
            max_a2 = max(max_a2, inf['a2']); max_rr = max(max_rr, inf.get('r_over_rp', 0.0))
    g['Z2_every_piece_out_or_pass'] = not unresolved
    info['Z2'] = dict(side=j, rho0=o.rho0, rmax=RMAX, h0=H0, max_depth=MAXDEPTH, sigma=sigma, kappa=KAPPA,
                      counts=dict(cnt), by_depth=dict(sorted(bydepth.items())),
                      smallest={k: (None if v is None else float('%.4g' % v)) for k, v in mins.items()}, smallest_at=where,
                      largest_relative_step=float('%.4g' % max_a2), largest_preimage_disc_ratio=float('%.4g' % max_rr),
                      unresolved=unresolved, stopped_at_first_unresolved_piece=bool(unresolved))
    info['ENG'] = dict(max_tail_at_1p02=float('%.3g' % rep['max_tail_at_1p02']),
                       remainder_constants=[{k: float('%.5g' % v) for k, v in m.items()} for m in rep['remainder_constants']])

    # ---- SND: independent semantics check at random points of D_j in pass pieces ----------------------------------------
    mp.mp.dps = 60
    S = T.Branch(d2['info'], 40); c = S.c
    tc = [mp.mpc(mp.mpf(re), mp.mpf(im)) for re, im in L.TAU_DECIMALS]
    tau = lambda x: tc[0] / x ** 3 + tc[1] / x ** 2 + tc[2] / x + tc[3] * mp.log(x)
    al = mp.mpc(mp.mpf(-102) / 19, -16 * mp.sqrt(3) / 19); th0 = mp.pi / 2 - mp.pi / 8
    xis = mp.mpf('0.4') * mp.expj(mp.pi / 6); ts = tau(xis / c)
    sg = 1 if j == 0 else -1
    rot = mp.expj(th0) if j == 0 else -mp.expj(-th0)
    s_j = ts.real - sg * mp.mpf('0.25'); c_j = (rot * ts).real - mp.mpf('0.15')
    fun = lambda xi: (sg * (tau(xi / c).real - s_j) + 1, (rot * tau(xi / c)).real)
    q3 = 0 if o.control == 'QZERO' else 3
    eps = mp.mpf('0.002') / (mp.exp((al * mp.log(xis)).real) * mp.mpf('1.25') ** (-q3) * (c_j + mp.mpf('0.15')) ** (-q3))

    def R(xi):
        f, sec = fun(xi)
        return eps * mp.exp((al * mp.log(xi)).real) * f ** (-q3) * sec ** (-q3)
    rnd = random.Random(20261113 + j); tested = 0; bad = []; smallest_exit = None
    order = list(range(len(passed))); rnd.shuffle(order)
    for idx in order:
        if tested >= 60:
            break
        s, t, hs_, ht_ = passed[idx]
        xi = mp.exp(s + hs_ * (2 * rnd.random() - 1)) * mp.expj(t + ht_ * (2 * rnd.random() - 1))
        f, sec = fun(xi)
        if not (f > 1 and sec > c_j):
            continue
        d = R(xi) * mp.expj(2 * mp.pi * rnd.random())
        xin, dn = S.dev_step(S.F if j == 0 else S.G, xi, d)
        fn, secn = fun(xin)
        ex = abs(dn) / R(xin)
        okp = fn > 1 and secn >= sec + mp.mpf(sigma) and abs(xin / xi - 1) <= mp.mpf(KAPPA) and ex > 1
        tested += 1
        smallest_exit = ex if smallest_exit is None else min(smallest_exit, ex)
        if not okp:
            bad.append([float(abs(xi)), float(mp.arg(xi) / mp.pi)])
    g['SND_independent_semantics'] = bool(tested >= 20 and not bad) if not unresolved else bool(not bad)
    info['SND'] = dict(points_tested=tested, violations=bad[:10],
                       smallest_exit_ratio=None if smallest_exit is None else float(mp.nstr(smallest_exit, 6)))

    g = {k: bool(v) for k, v in g.items()}; ok = all(g.values())
    for k in sorted(g):
        print(k, 'PASS' if g[k] else 'FAIL')
    print('RESULT', 'PASS' if ok else 'FAIL', '(control %s)' % o.control if o.control else '', L.run_tail('| development run; not a certificate'))
    with open(o.out, 'w', encoding='utf-8', newline='\n') as f:
        json.dump({'gates': g, 'info': info, 'all_pass': ok, 'control': o.control,
                   'status': L.run_status('stage 3c-a development run; not a certificate'), 'script': 'dyad_open20_an_stage3c_w3_zone2.py'},
                  f, indent=1, sort_keys=True)
        f.write('\n')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
