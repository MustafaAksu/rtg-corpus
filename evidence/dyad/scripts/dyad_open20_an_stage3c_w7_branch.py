#!/usr/bin/env python3
"""dyad_open20_an_stage3c_w7_branch.py -- stage 3c-a, W7: the computations behind "one analytic inverse branch for G".

DEVELOPMENT RUN.  Not a certificate; no statement about the jump or about divergence is drawn from it.

The argument (proof record, section on the inverse branch) needs three computed facts.
  INJ    On the convex sector  S1 = {|xi| <= 0.47, 0.03 pi <= arg xi <= 0.50 pi}  (in x = xi/c) the base map of the
         reference curve, b0(x) = x + x^4 G0(x), satisfies sup |b0' - 1| < 1.  So b0 is injective on S1.
         Checked on a cover: the disc |xi| <= 0.05 (sup bounds at 0) and rectangles in (log|xi|, arg xi), one disc each.
  SRC    For every pass piece of the zone-II cover of Omega_1 (the cover of W3, repeated here): the source disc B of the
         local inverse lemma lies in S1, and sup_B |E| <= the fibre radius of the piece's target set.  The counts of the
         cover must equal those recorded by W3.
  SRC1   Zone I: the source disc of every target of D1 with |xi| <= 0.05 lies in S1 (the targets of D1 there lie in the
         guard core, by W4; the disc has relative radius 2 t sup|G0|), and |E| on it is below the tube radius at the target.
Gates (exit 0 iff all pass): G0, ENG, INJ, SRC, SRC1.
Control (must exit 1):
  --control SMALLSECTOR   S1 cut to |xi| <= 0.30      -> SRC (the sources of the outer pieces are not in it)
Usage: python3 -I -B dyad_open20_an_stage3c_w7_branch.py --stage2 scout_N216_dps840.json --w3 w3_zone2_G.json --out OUT.json
"""
import os, sys, json, math, argparse, hashlib, collections
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from flint import acb, arb, ctx
import dyad_open20_an_stage3c_lib as L

STAGE2_SHA = '6ca8c663061ce2fa9e062938a1e6046c932da4cbddccc6e3e2c3de4df68c477e'
H0, MAXDEPTH, SIGMA, KAPPA, RMAX, XENG, RHO0 = 0.02, 5, '0.05', '0.15', 0.60, 1.03, 0.05    # the cover of W3
S_RAD, S_LO, S_HI = 0.47, 0.03, 0.50


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--stage2', required=True); ap.add_argument('--w3', required=True); ap.add_argument('--out', required=True)
    ap.add_argument('--control', choices=['SMALLSECTOR'])
    o = ap.parse_args()
    raw = open(o.stage2, 'rb').read(); d2 = json.loads(raw.decode('utf-8'))
    g, info = {}, {}
    g['G0_stage2_input'] = hashlib.sha256(raw).hexdigest() == STAGE2_SHA and d2.get('all_pass') is True
    K, a, SER, MC, rep = L.build_engine()
    g['ENG_engine'] = bool(rep['structural_zeros_consistent'] and rep['max_tail_at_1p02'] < 1e-6
                           and all(m['theta'] < 1 for m in rep['remainder_constants']))
    TAU = L.tau_coefficients(); eng = L.MapEngine(SER, TAU, MC)
    s_rad = 0.30 if o.control == 'SMALLSECTOR' else S_RAD
    cabs = float(abs(K.c).mid()); carg = float(K.c.arg().mid())

    def piece(s, t, hs, ht):
        xc = acb(arb(s - math.log(cabs)), arb(t - carg)).exp(); xc = acb(xc.real.mid(), xc.imag.mid())
        return xc, float(abs(xc).upper()) * (math.exp(math.hypot(hs, ht)) - 1) * (1 + 1e-9)

    # ---- INJ: sup |b0' - 1| on a cover of S1 ----------------------------------------------------------------------------
    TB = L.Tube(K, TAU, 1)
    X0 = float((arb(RHO0) / arb(abs(K.c).lower()) * (1 + arb('1e-9'))).upper())
    Linner = float(L._up(eng.b0p(acb(0), X0) - 1).upper())
    alo, ahi = S_LO * math.pi, S_HI * math.pi
    ns = math.ceil((math.log(S_RAD) - math.log(RHO0)) / H0); nt = math.ceil((ahi - alo) / H0)
    hs = (math.log(S_RAD) - math.log(RHO0)) / ns / 2; ht = (ahi - alo) / nt / 2
    Lmax, where = Linner, [0.0, 0.0]
    for i in range(ns):
        for k in range(nt):
            s, t = math.log(RHO0) + (2 * i + 1) * hs, alo + (2 * k + 1) * ht
            xc, r = piece(s, t, hs, ht)
            v = float(L._up(eng.b0p(xc, r) - 1).upper())
            if v > Lmax:
                Lmax, where = v, [float('%.5g' % math.exp(s)), float('%.5g' % (t / math.pi))]
    g['INJ_base_map_injective_on_the_sector'] = bool(Lmax < 1)
    info['INJ'] = dict(sector=dict(abs_xi_max=S_RAD, arg_over_pi=[S_LO, S_HI]), pieces=ns * nt, sup_on_inner_disc=float('%.5g' % Linner),
                       sup_abs_b0prime_minus_1=float('%.6g' % Lmax), attained_near=where)

    # ---- SRC: the sources of the zone-II cover of Omega_1 ---------------------------------------------------------------
    alo, ahi = float(TB.chart[1]) * math.pi, float(TB.chart[2]) * math.pi
    ns = math.ceil((math.log(RMAX) - math.log(RHO0)) / H0); nt = math.ceil((ahi - alo) / H0)
    hs = (math.log(RMAX) - math.log(RHO0)) / ns / 2; ht = (ahi - alo) / nt / 2
    stack = [(math.log(RHO0) + (2 * i + 1) * hs, alo + (2 * k + 1) * ht, hs, ht, 0) for i in range(ns) for k in range(nt)]
    cnt = collections.Counter(); bad = []; ext = dict(abs_xi=0.0, arg_lo=9.0, arg_hi=-9.0, E_margin=None, rho=0.0, r_over_rp=0.0)
    while stack:
        s, t, hs_, ht_, dep = stack.pop()
        xc, r = piece(s, t, hs_, ht_)
        if float(abs(xc).upper()) + r >= XENG:
            f, sec = TB.functionals(xc + acb(arb(0, r), arb(0, r)))
            st, inf = ('out', {}) if (f <= 1 or sec <= TB.cw) else ('guard', {})
        else:
            st, inf = L.piece_check(SER, MC, TB, xc, r, SIGMA, kappa=KAPPA, inverse=True)
        if st in ('fail', 'guard'):
            if dep < MAXDEPTH:
                for ds in (-hs_ / 2, hs_ / 2):
                    for dt in (-ht_ / 2, ht_ / 2):
                        stack.append((s + ds, t + dt, hs_ / 2, ht_ / 2, dep + 1))
                cnt['cut'] += 1
                continue
            bad.append(dict(abs_xi=float('%.5g' % math.exp(s)), arg_over_pi=float('%.5g' % (t / math.pi)), why='unresolved'))
            break
        cnt[st] += 1
        if st == 'pass':
            ax, a1, a2, em, rho = inf['src']
            ext['abs_xi'] = max(ext['abs_xi'], ax); ext['arg_lo'] = min(ext['arg_lo'], a1); ext['arg_hi'] = max(ext['arg_hi'], a2)
            ext['E_margin'] = em if ext['E_margin'] is None else min(ext['E_margin'], em)
            ext['rho'] = max(ext['rho'], rho); ext['r_over_rp'] = max(ext['r_over_rp'], inf['r_over_rp'])
            if not (ax <= s_rad and a1 >= S_LO and a2 <= S_HI and em > 0):
                bad.append(dict(abs_xi=float('%.5g' % math.exp(s)), arg_over_pi=float('%.5g' % (t / math.pi)),
                                source=[float('%.5g' % v) for v in (ax, a1, a2, em)]))
    try:
        w3 = json.load(open(o.w3)); same = (w3['all_pass'] is True and w3['info']['Z2']['side'] == 1 and w3['info']['Z2']['counts'] == dict(cnt))
    except (OSError, KeyError, ValueError):
        same = False
    g['SRC_sources_of_zone_II_in_the_sector'] = bool(not bad and same)
    info['SRC'] = dict(counts=dict(cnt), counts_equal_those_of_W3=bool(same), not_in_sector=bad[:10], not_in_sector_total=len(bad),
                       sources=dict(largest_abs_xi=float('%.5g' % ext['abs_xi']), arg_over_pi=[float('%.5g' % ext['arg_lo']), float('%.5g' % ext['arg_hi'])],
                                    smallest_fibre_radius_minus_sup_E=None if ext['E_margin'] is None else float('%.4g' % ext['E_margin']),
                                    largest_fibre_radius_rho=float('%.5g' % ext['rho']), largest_r_over_rp=float('%.5g' % ext['r_over_rp'])))

    # ---- SRC1: zone I -----------------------------------------------------------------------------------------------------
    z = L.zone1_check(K, SER, MC, TB, str(RHO0), SIGMA, kappa=KAPPA, extra=True)
    da = math.asin(z['src_rel_radius']) / math.pi
    ok1 = bool(z.get('preconditions') and z['guard_low'] > 0 and z['guard_high'] > 0 and z['inv_i'] > 0 and z['inv_ii'] > 0
               and float(TB.core[1]) - da >= S_LO and float(TB.core[2]) + da <= S_HI and z['E_over_R'] < 1 and z['X'] * cabs <= s_rad)
    g['SRC1_sources_of_zone_I_in_the_sector'] = ok1
    info['SRC1'] = dict(relative_radius_of_the_source_disc=float('%.4g' % z['src_rel_radius']), sup_E_over_R=float('%.4g' % z['E_over_R']),
                        sup_abs_b0prime_minus_1_on_the_disc=float('%.4g' % z['L_disc']))

    g = {k: bool(v) for k, v in g.items()}; ok = all(g.values())
    for k in sorted(g):
        print(k, 'PASS' if g[k] else 'FAIL')
    print('RESULT', 'PASS' if ok else 'FAIL', '(control %s)' % o.control if o.control else '', '| development run; not a certificate')
    with open(o.out, 'w', encoding='utf-8', newline='\n') as f:
        json.dump({'gates': g, 'info': info, 'all_pass': ok, 'control': o.control,
                   'status': 'stage 3c-a development run; not a certificate', 'script': 'dyad_open20_an_stage3c_w7_branch.py'},
                  f, indent=1, sort_keys=True)
        f.write('\n')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
