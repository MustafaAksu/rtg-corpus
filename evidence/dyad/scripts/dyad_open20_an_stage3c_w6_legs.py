#!/usr/bin/env python3
"""dyad_open20_an_stage3c_w6_legs.py -- stage 3c-a, work package W6: the two legs at xi* and the two-disc test
(design 3b r2, section 5, steps 3 to 5).

DEVELOPMENT RUN.  Not a certificate.  No statement about the jump, about divergence, or about B-an and B-6 is drawn
from its output.  A certificate exists only after stage 3c-b (fixed command, replay, review, PI decision).

What is done.  d0* and d1* are the deviations at xi* of the two sectorial curves from phi_N, in one coordinate.  Each
is enclosed in a disc by the forward-backward enclosure of its orbit (lib: leg_F, leg_G; method and formulas in the
header of the W6 block).  The hypotheses used: the orbit of (xi*, dj*) stays in the tube over D_j (the conclusion of
the tube lemma, whose hypotheses W3 and W4 check), and the remainder constants of W2b.

Gates (exit 0 iff all pass):
  G0     stage-2 file hash; its all_pass.
  ENG    engine: structural zeros consistent, tails below 1e-6, theta < 1 on both remainder circles.
  LEGF   leg F ran through; every disc X_k lies in the guard core of Omega_0.
  LEGG   leg G ran through (local inverse lemma found at every step of the first round); every X_k in the core of Omega_1.
  SEP    two-disc test: |c1 - c0| > r0 + r1, in ball arithmetic.
  SND    an independent computation of both values (mpmath, 80 digits, the full map and its numerical inverse from the
         stage-3b sampling module): a point of the reference curve far along the orbit is carried back by 150 steps and
         its start is adjusted until the base point is xi*.  Both values lie in the discs (tolerance 1e-11).
Controls (each must exit 1 at SEP):
  --control ZEROJUMP   the zero-jump model of design P11 (lib: ModelEngine) in place of the map: the two discs must
                       overlap; both must contain the known common value, and the model curve must lie in the tube
  --control SHORT      legs of 10 steps: the discs are too wide to separate
W8 options (the form for a certification run; the W6 development run used neither):
  --full-fibre   leg G calls the local inverse lemma for the whole a-priori fibre (proof record 4.3)
  --strict-snd   SND requires the independent values to lie in the discs, with no tolerance
Usage: python3 -I -B dyad_open20_an_stage3c_w6_legs.py --stage2 scout_N216_dps840.json --out OUT.json [--control NAME]
"""
import os, sys, json, argparse, hashlib
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from flint import acb, arb, ctx
import mpmath as mp
import dyad_open20_an_stage3c_lib as L
import dyad_open20_an_stage3b_tube_sampling as T

STAGE2_SHA = '6ca8c663061ce2fa9e062938a1e6046c932da4cbddccc6e3e2c3de4df68c477e'
N_STEPS, ROUNDS = 334, 5


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--stage2', required=True); ap.add_argument('--out', required=True)
    ap.add_argument('--control', choices=['ZEROJUMP', 'SHORT'])
    ap.add_argument('--full-fibre', action='store_true'); ap.add_argument('--strict-snd', action='store_true')
    o = ap.parse_args()
    raw = open(o.stage2, 'rb').read(); d2 = json.loads(raw.decode('utf-8'))
    g, info = {}, {}
    g['G0_stage2_input'] = hashlib.sha256(raw).hexdigest() == STAGE2_SHA and d2.get('all_pass') is True
    model = o.control == 'ZEROJUMP'
    n = 10 if o.control == 'SHORT' else N_STEPS
    if model:
        ctx.dps = 400
        K0 = L.Consts()
        ctx.prec = 160

        class KM:
            c = acb(1); ALPHA = K0.ALPHA
        K = KM; TAU = (acb(1) / 3, acb(0), acb(0), acb(0)); eng = L.ModelEngine(K0.ALPHA)
        g['ENG_engine'] = True
        info['ENG'] = 'zero-jump model: explicit formulas, no series engine'
    else:
        K, a, SER, MC, rep = L.build_engine()
        g['ENG_engine'] = bool(rep['structural_zeros_consistent'] and rep['max_tail_at_1p02'] < 1e-6
                               and all(m['theta'] < 1 for m in rep['remainder_constants']))
        TAU = L.tau_coefficients(); eng = L.MapEngine(SER, TAU, MC)
        info['ENG'] = dict(remainder_constants=[{k: float('%.5g' % v) for k, v in m.items()} for m in rep['remainder_constants']])
    xs = acb('0.4') * (acb(0, 1) * arb.pi() / 6).exp() / K.c
    res = {}
    for j, name, fn in ((0, 'LEGF_leg_F', L.leg_F), (1, 'LEGG_leg_G', L.leg_G)):
        TB = L.Tube(K, TAU, j)
        try:
            D0, hist, X, D = fn(eng, TB, xs, n, ROUNDS, full_fibre=True) if (j == 1 and o.full_fibre) else fn(eng, TB, xs, n, ROUNDS)
        except (ArithmeticError, AssertionError) as e:
            g[name] = False; info[name] = dict(error=str(e) or type(e).__name__)
            continue
        incore = all(TB.in_core(x + L._disc0(r)) is True for x, r in X)
        xin = K.c * X[n][0]
        row = dict(steps=n, rounds=ROUNDS, radius_after_each_round=[float('%.4g' % h) for h in hist],
                   centre=[D0[0].real.mid().str(30, radius=False), D0[0].imag.mid().str(30, radius=False)],
                   radius=float('%.6g' % float(D0[1].upper())),
                   every_disc_in_the_core=bool(incore),
                   end_of_orbit=dict(abs_xi=float('%.5g' % float(abs(xin).mid())), arg_over_pi=float('%.4g' % float((xin.arg() / arb.pi()).mid())),
                                     relative_radius_of_X=float('%.3g' % (float(X[n][1]) / float(abs(X[n][0]).mid()))),
                                     a_priori_radius=float('%.4g' % float(D[n][1]))))
        if model:
            dr = eng.dref(xs)
            row['contains_the_known_value'] = bool(L._up(dr - D0[0]) <= D0[1])
            worst = max(float((L._up(eng.dref(x + L._disc0(r))) / L.R_upper(TB, x + L._disc0(r))).upper()) for x, r in X)
            row['model_curve_over_tube_radius_max'] = float('%.4g' % worst)
            row['known_value'] = [dr.real.mid().str(30, radius=False), dr.imag.mid().str(30, radius=False)]
        g[name] = bool(incore and (not model or (row['contains_the_known_value'] and worst <= 1)))
        info[name] = row; res[j] = D0
    sep = False
    if 0 in res and 1 in res:
        diff = res[1][0] - res[0][0]
        gap = arb(abs(diff).lower()) - res[0][1] - res[1][1]
        sep = bool(gap > 0)
        info['SEP'] = dict(abs_c1_minus_c0=[float('%.10g' % float(abs(diff).lower())), float('%.10g' % float(abs(diff).upper()))],
                           c1_minus_c0=[diff.real.mid().str(20, radius=False), diff.imag.mid().str(20, radius=False)],
                           r0_plus_r1=float('%.6g' % float((res[0][1] + res[1][1]).upper())),
                           gap=float('%.6g' % float(gap.lower())),
                           note='development output; no statement about the jump is drawn from it')
    g['SEP_two_disc_test'] = sep

    # ---- SND: independent values (skipped for the model) --------------------------------------------------------------
    if model:
        g['SND_independent_values'] = True; info['SND'] = 'not applicable: the model value is known in closed form'
    elif not (0 in res and 1 in res):
        g['SND_independent_values'] = False
    else:
        mp.mp.dps = 80
        S = T.Branch(d2['info'], 40); c = S.c
        xi_s = mp.mpf('0.4') * mp.expj(mp.pi / 6); NB = 150
        tomp = lambda v: mp.mpc(mp.mpf(v.real.mid().str(60, radius=False)), mp.mpf(v.imag.mid().str(60, radius=False)))
        out = {}; snd = True
        for j, (out_map, back_map) in enumerate(((S.F, S.G), (S.G, S.F))):
            y = xi_s
            for _ in range(NB):                       # base orbit along the reference curve (d reset to 0 at every step)
                y, _d = S.dev_step(out_map, y, mp.mpc(0))

            def carry(y0):
                p, d = y0, mp.mpc(0)
                for _ in range(NB):
                    p, d = S.dev_step(back_map, p, d)
                return p, d
            p0, dd = carry(y); h = y * mp.mpf(10) ** (-20)
            for _ in range(4):                        # adjust the start until the base point is xi*
                p1, _d = carry(y + h)
                y = y - (p0 - xi_s) * h / (p1 - p0)
                p0, dd = carry(y)
            dev = abs(dd - tomp(res[j][0]))
            tol = mp.mpf(0) if o.strict_snd else mp.mpf(10) ** (-11)
            okj = abs(p0 - xi_s) < mp.mpf(10) ** (-40) and dev <= mp.mpf(float(res[j][1].lower())) + tol
            snd = snd and bool(okj)
            out['leg_%s' % 'FG'[j]] = dict(value=[mp.nstr(dd.real, 15), mp.nstr(dd.imag, 15)],
                                           distance_to_centre=float(mp.nstr(dev, 4)), base_error=float(mp.nstr(abs(p0 - xi_s), 3)))
            out['d%d' % j] = dd
        out['abs_difference'] = mp.nstr(abs(out.pop('d1') - out.pop('d0')), 10)
        if o.full_fibre or o.strict_snd:
            out['options'] = dict(full_fibre=bool(o.full_fibre), strict_snd=bool(o.strict_snd))
        g['SND_independent_values'] = snd; info['SND'] = out

    g = {k: bool(v) for k, v in g.items()}; ok = all(g.values())
    for k in sorted(g):
        print(k, 'PASS' if g[k] else 'FAIL')
    print('RESULT', 'PASS' if ok else 'FAIL', '(control %s)' % o.control if o.control else '', L.run_tail('| development run; not a certificate'))
    with open(o.out, 'w', encoding='utf-8', newline='\n') as f:
        json.dump({'gates': g, 'info': info, 'all_pass': ok, 'control': o.control,
                   'status': L.run_status('stage 3c-a development run; not a certificate; no statement about the jump is drawn'),
                   'script': 'dyad_open20_an_stage3c_w6_legs.py'}, f, indent=1, sort_keys=True)
        f.write('\n')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
