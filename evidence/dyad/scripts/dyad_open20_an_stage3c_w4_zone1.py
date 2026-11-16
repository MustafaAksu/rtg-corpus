#!/usr/bin/env python3
"""dyad_open20_an_stage3c_w4_zone1.py -- stage 3c-a, work package W4: zone I of the tube lemma, 0 < |xi| <= xi0.

DEVELOPMENT RUN.  Not a certificate; no statement about the jump or about divergence is drawn from it.

What is done.  For both sides (F on Omega_0, G on Omega_1) the hypotheses (G), (A1), (A2), (B) of the tube lemma are
reduced to inequalities between constants: sup bounds of the series on one disc at 0, and elementary bounds of tau,
of the functionals and of the tube radius (lib: zone1_check, with the derivation in its header).  For G the two
conditions of the local inverse lemma are checked in the same way.  The inequalities are homogeneous: each is divided
by the power of |x| it scales with, so one check covers every 0 < |xi| <= xi0.

Gates (exit 0 iff all pass):
  G0     stage-2 file hash; its all_pass.
  ENG    engine: structural zeros consistent, tails below 1e-6, theta < 1 on the remainder circle.
  Z1F    side F: preconditions and every margin of zone1_check positive.
  Z1G    side G: the same, with the three margins of the local inverse lemma.
  SEAM   the two zone-II outputs of W3 are present with the recorded hashes, pass Z2, and start at rho0 <= xi0:
         zones I and II together cover 0 < |xi| <= 0.60 of each chart sector.
  SND    semantics, by an independent evaluation (mpmath, 110 digits; the full map and its numerical inverse from the
         stage-3b sampling module; own formulas): on a grid of |xi| in {xi0, 0.03, 0.01, 0.003} x 41 arguments across
         each chart sector, every point of D_j lies in the guard core, and with |d| = R the step satisfies (A1), (A2)
         and the exit inequality.
Controls (each must exit 1 at the named gate):
  --control BIGZONE   xi0 = 0.10                                  -> Z1F and Z1G ((A1) for the second functional)
  --control SIGMA     sigma = 0.5                                 -> Z1F and Z1G (and SND)
  --control CORE      core of Omega_0 cut to arg xi <= 0.10 pi    -> Z1F (guard arc) and SND
  --control ALPHA     alpha replaced by alpha + 10 (design P11)   -> Z1F and Z1G ((B); a small change of alpha is
                      absorbed by the gain of the functionals, so the control uses a large one)
  --control BRANCH    the formal curve of the other root of the quadratic for a_2 (a valid formal curve, with its own
                      series), against the tube data of the pilot branch (alpha, c, tau) (design P11)   -> Z1F and Z1G
Usage: python3 -I -B dyad_open20_an_stage3c_w4_zone1.py --stage2 scout_N216_dps840.json --w3dir DIR --out OUT.json
"""
import os, sys, json, argparse, hashlib
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from flint import acb, arb, ctx
import mpmath as mp
import dyad_open20_an_stage3c_lib as L
import dyad_open20_an_stage3b_tube_sampling as T

STAGE2_SHA = '6ca8c663061ce2fa9e062938a1e6046c932da4cbddccc6e3e2c3de4df68c477e'
W3_SHA = {'w3_zone2_F.json': 'bbfac730ec743056b6e2d36c1f60bdd7e2cd3e7d36440bb891eff7cddda029f3', 'w3_zone2_G.json': 'e8874133be8500f902d71c72b2fdcbe83fc2296da0030b8e1376624fd5f4cba0'}
XI0, SIGMA, KAPPA = '0.05', '0.05', '0.15'
MARGINS = ('guard_low', 'guard_high', 'A1_first', 'A1_second', 'A2', 'B')
MARGINS_INV = ('inv_disc', 'inv_i', 'inv_ii')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--stage2', required=True); ap.add_argument('--w3dir', required=True); ap.add_argument('--out', required=True)
    ap.add_argument('--control', choices=['BIGZONE', 'SIGMA', 'CORE', 'ALPHA', 'BRANCH'])
    o = ap.parse_args()
    raw = open(o.stage2, 'rb').read(); d2 = json.loads(raw.decode('utf-8'))
    g, info = {}, {}
    g['G0_stage2_input'] = hashlib.sha256(raw).hexdigest() == STAGE2_SHA and d2.get('all_pass') is True
    K, a, SER, MC, rep = L.build_engine(rem=((0.90, 8000),), root='other' if o.control == 'BRANCH' else 'pilot')
    g['ENG_engine'] = bool(rep['structural_zeros_consistent'] and rep['max_tail_at_1p02'] < 1e-6
                           and all(m['theta'] < 1 for m in rep['remainder_constants']))
    TAU = L.tau_coefficients()
    if o.control == 'ALPHA':
        K.ALPHA = K.ALPHA + 10
    xi0 = '0.10' if o.control == 'BIGZONE' else XI0
    sigma = '0.5' if o.control == 'SIGMA' else SIGMA
    core_hi0 = '0.10' if o.control == 'CORE' else '0.20'
    for j, name in ((0, 'Z1F_zone1_side_F'), (1, 'Z1G_zone1_side_G')):
        TB = L.Tube(K, TAU, j)
        if j == 0:
            TB.core = (TB.core[0], TB.core[1], arb(core_hi0))
        z = L.zone1_check(K, SER, MC, TB, xi0, sigma, kappa=KAPPA)
        keys = MARGINS + (MARGINS_INV if j == 1 else ())
        g[name] = bool(z.get('preconditions') and all(z.get(k, -1.0) > 0 for k in keys))
        info[name] = {k: (float('%.5g' % v) if isinstance(v, float) else v) for k, v in z.items()}

    # ---- SEAM ---------------------------------------------------------------------------------------------------------
    seam = True; rows = {}
    for fn, sha in W3_SHA.items():
        p = os.path.join(o.w3dir, fn)
        try:
            rw = open(p, 'rb').read(); d = json.loads(rw.decode('utf-8'))
            okf = (hashlib.sha256(rw).hexdigest() == sha and d['all_pass'] is True and d['control'] is None
                   and d['gates']['Z2_every_piece_out_or_pass'] is True and d['info']['Z2']['rho0'] <= float(xi0)
                   and d['info']['Z2']['rmax'] == 0.60)
            rows[fn] = dict(rho0=d['info']['Z2']['rho0'], rmax=d['info']['Z2']['rmax'], ok=bool(okf))
        except (OSError, KeyError, ValueError):
            okf = False; rows[fn] = dict(ok=False)
        seam = seam and okf
    g['SEAM_zones_cover_the_sector'] = seam
    info['SEAM'] = dict(xi0=float(xi0), w3=rows)

    # ---- SND ----------------------------------------------------------------------------------------------------------
    mp.mp.dps = 110
    S = T.Branch(d2['info'], 40); c = S.c
    tc = [mp.mpc(mp.mpf(re), mp.mpf(im)) for re, im in L.TAU_DECIMALS]
    tau = lambda x: tc[0] / x ** 3 + tc[1] / x ** 2 + tc[2] / x + tc[3] * mp.log(x)
    al = mp.mpc(mp.mpf(-102) / 19, -16 * mp.sqrt(3) / 19); th0 = mp.pi / 2 - mp.pi / 8
    xis = mp.mpf('0.4') * mp.expj(mp.pi / 6); ts = tau(xis / c)
    snd = True; info['SND'] = {}
    for j in (0, 1):
        sg = 1 if j == 0 else -1
        rot = mp.expj(th0) if j == 0 else -mp.expj(-th0)
        s_j = ts.real - sg * mp.mpf('0.25'); c_j = (rot * ts).real - mp.mpf('0.15')
        fun = lambda xi: (sg * (tau(xi / c).real - s_j) + 1, (rot * tau(xi / c)).real)
        eps = mp.mpf('0.002') / (mp.exp((al * mp.log(xis)).real) * mp.mpf('1.25') ** (-3) * (c_j + mp.mpf('0.15')) ** (-3))

        def R(xi):
            f, sec = fun(xi)
            return eps * mp.exp((al * mp.log(xi)).real) * f ** (-3) * sec ** (-3)
        ch = ((-0.20, 0.30), (0.03, 0.50))[j]; co = ((-0.08, float(core_hi0)), (0.09, 0.43))[j]
        tested = 0; bad = []; smallest = None
        for r in (mp.mpf(xi0), mp.mpf('0.03'), mp.mpf('0.01'), mp.mpf('0.003')):
            for k in range(41):
                ar = ch[0] + (ch[1] - ch[0]) * (k + 0.5) / 41
                xi = r * mp.expj(ar * mp.pi)
                f, sec = fun(xi)
                if not (f > 1 and sec > c_j):
                    continue
                tested += 1
                d = R(xi) * mp.expj(mp.mpf(k))
                xin, dn = S.dev_step(S.F if j == 0 else S.G, xi, d)
                fn_, secn = fun(xin)
                ex = abs(dn) / R(xin)
                okp = (co[0] <= ar <= co[1] and fn_ > 1 and secn >= sec + mp.mpf(sigma)
                       and abs(xin / xi - 1) <= mp.mpf(KAPPA) and ex > 1)
                smallest = ex if smallest is None else min(smallest, ex)
                if not okp:
                    bad.append([float(r), float('%.4g' % ar)])
        snd = snd and tested >= 40 and not bad
        info['SND']['side_%s' % 'FG'[j]] = dict(points_of_D_tested=tested, violations=bad[:10],
                                                smallest_exit_ratio_minus_1=None if smallest is None else float(mp.nstr(smallest - 1, 4)))
    g['SND_independent_semantics'] = snd

    g = {k: bool(v) for k, v in g.items()}; ok = all(g.values())
    for k in sorted(g):
        print(k, 'PASS' if g[k] else 'FAIL')
    print('RESULT', 'PASS' if ok else 'FAIL', '(control %s)' % o.control if o.control else '', L.run_tail('| development run; not a certificate'))
    with open(o.out, 'w', encoding='utf-8', newline='\n') as f:
        json.dump({'gates': g, 'info': info, 'all_pass': ok, 'control': o.control,
                   'status': L.run_status('stage 3c-a development run; not a certificate'), 'script': 'dyad_open20_an_stage3c_w4_zone1.py'},
                  f, indent=1, sort_keys=True)
        f.write('\n')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
