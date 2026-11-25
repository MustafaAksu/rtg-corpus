#!/usr/bin/env python3
"""dyad_open20_an_stage3c_w2_check.py -- stage 3c-a, work package W2 (first half): development check of the jets in d,
the tail bounds and the evaluation on discs.

DEVELOPMENT RUN.  Not a certificate; no statement about the jump or about divergence is drawn from it.

What is checked.  The four order-zero series G0, Q4, M3, ET44 (lib docstring), their Cauchy constants on |x| = X, and
the one-step quantities g, dtau, mu0, E, dx'/dd on discs, against an independent evaluation of the full map at random
points (mpmath, 60 digits; the map and coefficient values of the stage-3b sampling module, a separate code path).

Gates (exit 0 iff all pass):
  G0   stage-2 file hash; its all_pass.
  S    consistency of the structural zeros S1-S4: every coefficient that is 0 by structure comes out as a ball that
       contains 0, of radius below 1e-150.  (A consistency check; the zeros are proved in the proof record, not here.)
  C0   leading coefficients: G0(0) = ell and Q4(0) = mu (balls contain the exact constants); M3(0) - (2 + alpha) G0(0)
       contains 0 (the identity behind the cancellation in the normal multiplier).
  M    the circle bounds are finite, and the tails of all four series at |x| = 1.02 are below 1e-7.
  SND  soundness on discs: for 21 discs (|x| from 0.01 to 1.0; relative radius 2%, 0.5% and 1e-6) and 5 random points each,
       the independent values of g, dtau, mu0, dx'/dd lie in the enclosures; for E the test is made where the
       independent value is resolved (|x| >= 0.2).  The discs of relative radius 1e-6 have enclosures of relative
       radius about 1e-5, so they make the test sharp.
  ACC  accuracy at relative radius 0.5%, for |x| <= 0.87 (the common point has |x| = 0.867): the enclosures of g, dtau,
       mu0 - 1 and dx'/dd have relative radius below 10%.  At |x| = 1.0, near the outer edge of D0, the radii are
       reported only; smaller discs are needed there.
Control (must exit 1 at SND): --control TAMPER (the coefficient of x^7 in G0 is changed by 1e-3).
Usage: python3 -I -B dyad_open20_an_stage3c_w2_check.py --stage2 scout_N216_dps840.json --out OUT.json [--control TAMPER]
"""
import os, sys, json, argparse, hashlib, random
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from flint import acb, arb, ctx
import mpmath as mp
import dyad_open20_an_stage3c_lib as L
import dyad_open20_an_stage3b_tube_sampling as T

STAGE2_SHA = '6ca8c663061ce2fa9e062938a1e6046c932da4cbddccc6e3e2c3de4df68c477e'
N, D, X_TAIL, NARC = 40, 360, 1.10, 16000


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--stage2', required=True); ap.add_argument('--out', required=True)
    ap.add_argument('--control', choices=['TAMPER'])
    o = ap.parse_args()
    raw = open(o.stage2, 'rb').read(); d2 = json.loads(raw.decode('utf-8'))
    g, info = {}, {}
    g['G0_stage2_input'] = hashlib.sha256(raw).hexdigest() == STAGE2_SHA and d2.get('all_pass') is True
    ctx.dps = 400
    K = L.Consts(); a = L.coefficients(K, N)
    ser, rep = L.order_zero_series(K, a, D)
    g['S_structural_zeros_consistent'] = (all(rep[k] for k in ('S1_Z0_minus_x', 'S2_Z1', 'S3_bracket', 'S4_defect'))
                                          and rep['max_radius_of_vanishing_coefficients'] < 1e-150)
    info['S'] = rep
    g['C0_leading_coefficients'] = bool(ser['G0'][0].contains(K.ell) and ser['Q4'][0].contains(K.MU)
                                        and (ser['M3'][0] - (2 + K.ALPHA) * ser['G0'][0]).contains(acb(0)))
    if o.control == 'TAMPER':
        ser['G0'][7] = ser['G0'][7] + acb('0.001')
    ctx.prec = 160
    M, sup = L.circle_sup(K, a, X_TAIL, NARC)
    SER = {k: L.Series(ser[k], X_TAIL, M[k]) for k in ser}
    tails = {k: float(SER[k].tail(1.02).upper()) for k in SER}
    g['M_circle_bounds_and_tails'] = all(v < 1e-7 for v in tails.values())
    info['M'] = dict(X=X_TAIL, arcs=NARC, D=D, cauchy_constants={k: float('%.5g' % v) for k, v in M.items()},
                     sup_on_circle={k: float('%.5g' % v) for k, v in sup.items()}, tails_at_1p02={k: float('%.3g' % v) for k, v in tails.items()})
    TAU = L.tau_coefficients()
    # independent point evaluation
    mp.mp.dps = 60
    S = T.Branch(d2['info'], N); c = S.c
    tc = [mp.mpc(mp.mpf(re), mp.mpf(im)) for re, im in L.TAU_DECIMALS]
    tau_mp = lambda x: tc[0] / x ** 3 + tc[1] / x ** 2 + tc[2] / x + tc[3] * mp.log(x)

    def indep(x):
        xi = c * x
        xi1, E = S.dev_step(S.F, xi, mp.mpc(0)); h = mp.mpf(10) ** (-25)
        xi2, E2 = S.dev_step(S.F, xi, h)
        x1 = xi1 / c
        return dict(g=x1 / x - 1, dtau=tau_mp(x1) - tau_mp(x), mu0=(E2 - E) / h, E=E, dxdd=(xi2 - xi1) / h / c)
    tomp = lambda v: mp.mpc(mp.mpf(v.real.mid().str(50, radius=False)), mp.mpf(v.imag.mid().str(50, radius=False)))
    rnd = random.Random(20261111); rows = []; snd = True; acc = True
    for rx in ('1.0', '0.87', '0.65', '0.4', '0.2', '0.05', '0.01'):
        for s in ('0.02', '0.005', '0.000001'):
            xc = acb(rx) * (acb(0, 1) * (arb('0.1') * arb.pi() - K.c.arg())).exp()       # arg xi = 0.1 pi
            xc = acb(xc.real.mid(), xc.imag.mid()); r = float(s) * float(rx)
            q = L.step_quantities(SER, TAU, xc, r)
            miss = []
            for _ in range(5):
                x = tomp(xc) + r * mp.sqrt(rnd.random()) * mp.expj(2 * mp.pi * rnd.random()); v = indep(x)
                for k in ('g', 'dtau', 'mu0', 'E', 'dxdd'):
                    if k == 'E' and float(rx) < 0.2:
                        continue
                    e = acb(arb(mp.nstr(v[k].real, 55)), arb(mp.nstr(v[k].imag, 55)))
                    slack = 1e-18 * float(abs(v[k])) if k in ('mu0', 'dxdd') else 1e-45 * float(abs(v[k]))   # finite difference / printing
                    if not (q[k].contains(e) or float(abs(q[k] - e).lower()) <= slack):
                        miss.append(k)
            rel = lambda v, sub=0: float(v.rad()) / float(abs(acb(v.real.mid(), v.imag.mid()) - sub).upper())
            row = dict(abs_x=rx, relative_radius=s, misses=miss, relrad_g=float('%.3g' % rel(q['g'])), relrad_dtau=float('%.3g' % rel(q['dtau'])),
                       relrad_mu0_minus_1=float('%.3g' % rel(q['mu0'], 1)), relrad_dxdd=float('%.3g' % rel(q['dxdd'])))
            rows.append(row); snd = snd and not miss
            if s == '0.005' and float(rx) <= 0.87:
                acc = acc and max(row['relrad_g'], row['relrad_dtau'], row['relrad_mu0_minus_1'], row['relrad_dxdd']) < 0.10
    g['SND_independent_values_inside_enclosures'] = snd
    g['ACC_relative_radius_below_10_percent'] = acc
    info['discs'] = rows
    g = {k: bool(v) for k, v in g.items()}; ok = all(g.values())
    for k in sorted(g):
        print(k, 'PASS' if g[k] else 'FAIL')
    print('RESULT', 'PASS' if ok else 'FAIL', '(control %s)' % o.control if o.control else '', L.run_tail('| development run; not a certificate'))
    with open(o.out, 'w', encoding='utf-8', newline='\n') as f:
        json.dump({'gates': g, 'info': info, 'all_pass': ok, 'control': o.control,
                   'status': L.run_status('stage 3c-a development run; not a certificate'), 'script': 'dyad_open20_an_stage3c_w2_check.py'},
                  f, indent=1, sort_keys=True)
        f.write('\n')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
