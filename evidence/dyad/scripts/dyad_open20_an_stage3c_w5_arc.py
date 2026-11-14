#!/usr/bin/env python3
"""dyad_open20_an_stage3c_w5_arc.py -- stage 3c-a, work package W5: the common arc gamma (design 3b r2, section 5 step 2).

DEVELOPMENT RUN.  Not a certificate; no statement about the jump or about divergence is drawn from it.

The arc is the solution of  tau(gamma(t)) = Re tau* - i t,  t >= t* = -Im tau*,  gamma(t*) = xi*.
  compact part   t* <= t <= t_K: validated continuation by discs (lib: arc_chain), each disc inside both guard cores;
  tail           t >= tM: one inequality between constants gives a unique solution in a disc around the leading
                 approximation, for every such t (lib: arc_tail); the tail lies inside both guard cores and tends to 0;
  link           t_K >= tM, and the solution of the last disc at t_K lies in the tail disc at t_K.
Together with the wedge conditions along the half-line this gives: gamma is a continuous (analytic) arc from xi* to 0
inside D0 and D1 (statement C2 of the design; the open neighbourhood U follows because D0 and D1 are open).

Gates (exit 0 iff all pass):
  WEDGE  at tau* the four wedge conditions hold with the design margins (0.25, 0.25, 0.15, 0.15), and both second
         functionals grow along the half-line (slope sin(theta0) > 0); Re tau* < 0.
  CHAIN  arc_chain reaches tM: every segment covered, consecutive solutions agree, every disc in both guard cores.
  TAIL   arc_tail: margin > 0, the tail in both guard cores.
  LINK   the chain ends at t_K >= tM and its last solution lies in the tail disc at t_K.
  SND    an independent continuation (mpmath, 50 digits, Newton steps in t with ratio 1.05, own formula for tau): each
         of its points lies in the disc of the chain that covers its t, or in the tail disc; and the point nearest to
         t = 3000 has |xi| and arg xi as recorded in the sampling of the design (0.047, 0.1634 pi).
Controls (each must exit 1 at the named gate):
  --control BIGSTEP   segments 1.5 times longer than the step rule            -> CHAIN (LINK and SND fail with it)
  --control CORE      the core of Omega_0 cut to arg xi <= 0.16 pi           -> CHAIN (and TAIL)
  --control BRANCH    the tail uses another cube root                        -> TAIL, LINK (and SND)
  --control LOGBRANCH tau of D1 on another branch of the logarithm (tau + 2 pi i kappa) against the walls of the
                      principal branch (design P11)                           -> WEDGE
Usage: python3 -I -B dyad_open20_an_stage3c_w5_arc.py --out OUT.json [--control NAME]
"""
import os, sys, json, argparse
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from flint import acb, arb, ctx
import mpmath as mp
import dyad_open20_an_stage3c_lib as L

XI_M, EPS_TAIL, EPS_CHAIN, STEP = '0.04', 0.03, 0.02, 0.8


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', required=True); ap.add_argument('--control', choices=['BIGSTEP', 'CORE', 'BRANCH', 'LOGBRANCH'])
    o = ap.parse_args()
    g, info = {}, {}
    ctx.dps = 400
    K = L.Consts()
    ctx.prec = 160
    TAU = L.tau_coefficients()
    TB = [L.Tube(K, TAU, 0), L.Tube(K, TAU, 1)]
    if o.control == 'CORE':
        TB[0].core = (TB[0].core[0], TB[0].core[1], arb('0.16'))
    if o.control == 'LOGBRANCH':
        tau_principal = TB[1].tau
        TB[1].tau = lambda x: tau_principal(x) + acb(0, 2) * arb.pi() * TAU[3]
    xs = acb('0.4') * (acb(0, 1) * arb.pi() / 6).exp() / K.c
    f0, s0 = TB[0].functionals(xs); f1, s1 = TB[1].functionals(xs)
    g['WEDGE_conditions_along_the_half_line'] = bool(
        f0 > 1 and f1 > 1 and s0 > TB[0].cw and s1 > TB[1].cw and TB[0].rot.imag > 0 and TB[1].rot.imag > 0
        and TB[0].tau(xs).real < 0)
    t_fam = TB[0].tau(xs).imag * (-1) + (TB[1].cw - s0) / TB[0].rot.imag
    info['WEDGE'] = dict(first_minus_1=[float((f0 - 1).mid()), float((f1 - 1).mid())],
                         second_minus_c=[float((s0 - TB[0].cw).mid()), float((s1 - TB[1].cw).mid())],
                         slope_of_second=float(TB[0].rot.imag.mid()),
                         second0_exceeds_c1_for_t_above=float('%.6g' % float(t_fam.upper())))

    tl = L.arc_tail(K, TAU, XI_M, eps=EPS_TAIL, cores=TB, branch=1 if o.control == 'BRANCH' else 0)
    g['TAIL_unique_solution_for_large_t'] = bool(tl['margin'] > 0 and tl['in_cores'] and tl['epp'] < tl['eps'] and tl['re_tau_star_negative'])
    info['TAIL'] = {k: (float('%.6g' % v) if isinstance(v, float) else v) for k, v in tl.items() if k != 'x0'}

    ch = L.arc_chain(K, TAU, tl['tM'], eps=EPS_CHAIN, step=1.5 * STEP / 0.8 if o.control == 'BIGSTEP' else STEP, cores=TB)
    g['CHAIN_validated_continuation'] = bool(ch['ok'])
    info['CHAIN'] = dict(ok=bool(ch['ok']), why=ch.get('why'), segments=ch.get('segments'), eps=EPS_CHAIN, step=STEP)
    link = False
    if ch['ok']:
        c = K.c
        ab = [float(abs(c * x).mid()) for _, _, x, _ in ch['discs']]; ar = [float(((c * x).arg() / arb.pi()).mid()) for _, _, x, _ in ch['discs']]
        info['CHAIN'].update(t_star=float('%.10g' % ch['t_star']), t_reached=float('%.8g' % ch['t_reached']),
                             abs_xi_of_centres=[float('%.5g' % min(ab)), float('%.5g' % max(ab))],
                             arg_xi_over_pi_of_centres=[float('%.5g' % min(ar)), float('%.5g' % max(ar))],
                             every_20th_disc=[dict(t=float('%.6g' % d[0]), abs_xi=float('%.5g' % ab[i]), arg_over_pi=float('%.5g' % ar[i]))
                                              for i, d in enumerate(ch['discs']) if i % 20 == 0])
        xK, tK, bK = ch['last']; x0 = tl['x0'](tK)
        dist = (L._up(xK - x0) + bK) / arb(abs(x0).lower())
        link = bool(tK >= tl['tM'] and dist < arb(tl['eps']))
        info['LINK'] = dict(t_K=float('%.8g' % tK), tM=float('%.8g' % tl['tM']), relative_distance_to_tail_centre=float('%.4g' % float(dist.upper())))
    g['LINK_chain_meets_tail'] = link

    # ---- SND: independent continuation ---------------------------------------------------------------------------------
    mp.mp.dps = 50
    tc = [mp.mpc(mp.mpf(re), mp.mpf(im)) for re, im in L.TAU_DECIMALS]
    tau = lambda x: tc[0] / x ** 3 + tc[1] / x ** 2 + tc[2] / x + tc[3] * mp.log(x)
    dtau = lambda x: -3 * tc[0] / x ** 4 - 2 * tc[1] / x ** 3 - tc[2] / x ** 2 + tc[3] / x
    tomp = lambda v: mp.mpc(mp.mpf(v.real.mid().str(45, radius=False)), mp.mpf(v.imag.mid().str(45, radius=False)))
    cm = tomp(K.c); x = mp.mpf('0.4') * mp.expj(mp.pi / 6) / cm; ts = tau(x); t = -ts.imag
    bad = []; n = 0; near3000 = None
    while t < 4 * tl['tM'] and ch['ok']:
        t = t * mp.mpf('1.05')
        for _ in range(12):
            x = x - (tau(x) - (ts.real - 1j * t)) / dtau(x)
        n += 1
        tf = float(t)
        if tf <= ch['t_reached']:
            hit = [d for d in ch['discs'] if d[0] <= tf <= d[1]]
            okp = bool(hit) and all(abs(x - tomp(d[2])) < d[3] for d in hit)
        else:
            x0 = tomp(tl['x0'](tf)); okp = abs(x - x0) < tl['epp'] * abs(x0) * (1 + 1e-9)
        if not okp:
            bad.append(float('%.6g' % tf))
        if near3000 is None and tf >= 3000:
            xi = cm * x; near3000 = dict(t=float('%.6g' % tf), abs_xi=float(mp.nstr(abs(xi), 5)), arg_over_pi=float(mp.nstr(mp.arg(xi) / mp.pi, 5)))
    okd = near3000 is not None and abs(near3000['abs_xi'] - 0.047) < 0.001 and abs(near3000['arg_over_pi'] - 0.1634) < 0.0006
    g['SND_independent_continuation'] = bool(n >= 100 and not bad and okd)
    info['SND'] = dict(points=n, outside=bad[:10], near_t_3000=near3000)

    g = {k: bool(v) for k, v in g.items()}; ok = all(g.values())
    for k in sorted(g):
        print(k, 'PASS' if g[k] else 'FAIL')
    print('RESULT', 'PASS' if ok else 'FAIL', '(control %s)' % o.control if o.control else '', L.run_tail('| development run; not a certificate'))
    with open(o.out, 'w', encoding='utf-8', newline='\n') as f:
        json.dump({'gates': g, 'info': info, 'all_pass': ok, 'control': o.control,
                   'status': L.run_status('stage 3c-a development run; not a certificate'), 'script': 'dyad_open20_an_stage3c_w5_arc.py'},
                  f, indent=1, sort_keys=True)
        f.write('\n')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
