#!/usr/bin/env python3
"""dyad_open20_an_stage3c_w2b_check.py -- stage 3c-a, work package W2 (second half): development check of the
second-order jets in d, the remainder in d, the one-step quantities on tube pieces, and the local inverse.

DEVELOPMENT RUN.  Not a certificate; no statement about the jump or about divergence is drawn from it.

What is checked.  The six order-zero series (lib: order_zero_from_jets), the constants M3, MZ3 of the remainder in d
beyond second order (lib: d_remainder_constants), the enclosures of a forward step on a tube piece
{|x - xc| <= r} x {|d| <= rho} (lib: tube_step), and the local inverse lemma (lib: inverse_conditions, inverse_step),
against an independent evaluation of the full map and of its numerical inverse at random points (mpmath, 60 digits; the
map of the stage-3b sampling module, a separate code path).

Gates (exit 0 iff all pass):
  G0    stage-2 file hash; its all_pass.
  J2    second-order series: every coefficient that is 0 by structure (S1-S5) comes out as a ball that contains 0, of
        radius below 1e-150 (a consistency check, not a proof); leading coefficients G0(0) = ell, Q4(0) = mu,
        M3(0) = (2 + alpha) G0(0), S2(0) = conj(mu), P4(0) = 0; and the four series shared with W2a, computed there by a
        different routine, overlap coefficient by coefficient.
  M     circle bounds finite; tails of the six series at |x| = 1.02 below 1e-6.
  C2    soundness of the second-order coefficients c2 and (1/2) d^2x'/dd^2 on discs: independent second differences
        lie in the enclosures.
  REM   remainder constants: finite on both circles, theta < 1; at sampled points of the polydiscs the independent
        remainders |Phi - E - mu0 d - c2 d^2| and |Z - Z0 - Z1 d - Z2 d^2| are below M3 |x|^3 |d|^3 and
        MZ3 |x|^4 |d|^3.  The largest ratio true/bound is reported.
  TUBE  tube pieces: for random (x, d) in the piece with |d| = rho, the independent x'/x - 1 and tau(x') - tau(x) lie
        in the enclosures, their differences from the values at d = 0 are below gt_dev and dtau_dev, and
        dev_lo <= |d'| <= dev_hi.  The largest ratios true/bound of the two differences are reported.
  INV   local inverse: on every test target the two conditions of the lemma are verified, and for random (x', d') in
        the target the independent preimage (numerical inverse of the full map) lies in the disc and in the fibre
        radius of the lemma, with x/x' - 1 and tau(x) - tau(x') in the enclosures.
Reported, not gated ([NUM]): the growth of the coefficients of the formal inverse along the curve (the finding that
made the plan drop the inverse series; plan record 2.5).
Controls (each must exit 1 at the named gate):
  --control SHRINKREM   M3 and MZ3 are multiplied by 1e-3                          -> REM (TUBE fails as well)
  --control SHIFTINV    the preimage disc of the lemma is displaced by 3 radii     -> INV
Usage: python3 -I -B dyad_open20_an_stage3c_w2b_check.py --stage2 scout_N216_dps840.json --out OUT.json [--control NAME]
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
RHO_D = 0.02
REM_CIRCLES = ((0.90, 8000), (1.03, 32000))
N_INV = 240


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--stage2', required=True); ap.add_argument('--out', required=True)
    ap.add_argument('--control', choices=['SHRINKREM', 'SHIFTINV'])
    o = ap.parse_args()
    raw = open(o.stage2, 'rb').read(); d2 = json.loads(raw.decode('utf-8'))
    g, info = {}, {}
    g['G0_stage2_input'] = hashlib.sha256(raw).hexdigest() == STAGE2_SHA and d2.get('all_pass') is True
    f5 = lambda v: float('%.5g' % v)

    # ---- series -----------------------------------------------------------------------------------------------------
    ctx.dps = 400
    K = L.Consts(); a = L.coefficients(K, N)
    Zj, Wj = L.forward_jets(K, a, D + N + 6)
    ser, rep = L.order_zero_from_jets(a, Zj, Wj, D)
    old, _ = L.order_zero_series(K, a, D)
    overlap = all(ser[k][i].overlaps(old[k][i]) for k in old for i in range(D + 1))
    lead = (ser['G0'][0].contains(K.ell) and ser['Q4'][0].contains(K.MU) and ser['S2'][0].contains(K.MU.conjugate())
            and ser['P4'][0].contains(acb(0)) and (ser['M3'][0] - (2 + K.ALPHA) * ser['G0'][0]).contains(acb(0)))
    g['J2_second_order_series'] = bool(rep['all_contain_zero'] and rep['max_radius'] < 1e-150 and lead and overlap)
    info['J2'] = dict(report=rep, leading_coefficients_ok=bool(lead), overlap_with_w2a_series=bool(overlap))

    # ---- [NUM] growth of the formal inverse along the curve (not gated; skipped in control runs) ---------------------
    if not o.control:
        z, w = L.inverse_curve(K, a, N_INV)
        roots = {str(k): [f5(float(abs(z[k]).mid()) ** (1.0 / k)), f5(float(abs(w[k]).mid()) ** (1.0 / k))] for k in range(60, N_INV, 60)}
        ratios = {str(k): f5(float((abs(z[k + 1]) / abs(z[k])).mid())) for k in range(N_INV - 42, N_INV - 1, 10)}
        info['NUM_inverse_series'] = dict(n=N_INV, kth_roots_of_z_and_w_coefficients=roots, ratios_of_successive_z_coefficients=ratios,
                                          max_ball_radius=float(max(float(t.rad()) for t in z + w)),
                                          note='observation only: ratios above 1 mean a radius of convergence below 1 in x; '
                                               'the points of D1 near the common point have |x| up to about 0.9')

    # ---- Cauchy constants, remainder constants ----------------------------------------------------------------------
    ctx.prec = 160
    M, sup = L.circle_sup(K, a, X_TAIL, NARC, second=True)
    SER = {k: L.Series(ser[k], X_TAIL, M[k]) for k in ser}
    tails = {k: float(SER[k].tail(1.02).upper()) for k in SER}
    g['M_circle_bounds_and_tails'] = all(v < 1e-6 for v in tails.values())
    info['M'] = dict(X=X_TAIL, arcs=NARC, D=D, cauchy_constants={k: f5(v) for k, v in M.items()},
                     tails_at_1p02={k: float('%.3g' % v) for k, v in tails.items()})
    MC = [L.d_remainder_constants(K, a, X, RHO_D, n) for X, n in REM_CIRCLES]
    info['REM_constants'] = [dict(X=m['X'], rho=m['rho'], arcs=n, M3=f5(m['M3']), MZ3=f5(m['MZ3']), theta=f5(m['theta']))
                             for m, (_, n) in zip(MC, REM_CIRCLES)]
    rem_ok = all(m['theta'] < 1 and m['M3'] < float('inf') and m['MZ3'] < float('inf') for m in MC)
    if o.control == 'SHRINKREM':
        for m in MC:
            m['M3'] *= 1e-3; m['MZ3'] *= 1e-3
    TAU = L.tau_coefficients()

    # ---- independent evaluation -------------------------------------------------------------------------------------
    mp.mp.dps = 60
    S = T.Branch(d2['info'], N); c = S.c
    tc = [mp.mpc(mp.mpf(re), mp.mpf(im)) for re, im in L.TAU_DECIMALS]
    tau = lambda x: tc[0] / x ** 3 + tc[1] / x ** 2 + tc[2] / x + tc[3] * mp.log(x)
    tomp = lambda v: mp.mpc(mp.mpf(v.real.mid().str(50, radius=False)), mp.mpf(v.imag.mid().str(50, radius=False)))
    toacb = lambda v: acb(arb(mp.nstr(v.real, 50)), arb(mp.nstr(v.imag, 50)))
    hi = lambda v: mp.mpf(v.upper().str(30, radius=False)); lo = lambda v: mp.mpf(v.lower().str(30, radius=False))
    rnd = random.Random(20261112)

    def centre(rx, argxi):
        xc = acb(rx) * (acb(0, 1) * (arb(argxi) * arb.pi() - K.c.arg())).exp()
        return acb(xc.real.mid(), xc.imag.mid())

    def inside(ball, v, slack=0.0):
        e = toacb(v)
        return bool(ball.contains(e) or float(abs(ball - e).lower()) <= slack * float(abs(v)))

    # C2: second-order coefficients at d = 0
    rows = []; c2_ok = True
    for rx in ('1.0', '0.87', '0.5', '0.2', '0.05'):
        for s in ('0.005', '0.000001'):
            xc = centre(rx, '0.1'); r = float(s) * float(rx)
            q = L.tube_step(SER, TAU, None, xc, r, 0)
            miss = []
            for _ in range(4):
                x = tomp(xc) + r * mp.sqrt(rnd.random()) * mp.expj(2 * mp.pi * rnd.random()); xi = c * x; h = mp.mpf(10) ** (-12)
                x0, E0 = S.dev_step(S.F, xi, mp.mpc(0)); xp, Ep = S.dev_step(S.F, xi, h); xm, Em = S.dev_step(S.F, xi, -h)
                v = dict(c2=(Ep + Em - 2 * E0) / (2 * h * h), d2xdd2=(xp + xm - 2 * x0) / (2 * h * h) / c, mu0=(Ep - Em) / (2 * h))
                miss += [k for k in v if not inside(q[k], v[k], 1e-14)]
            rows.append(dict(abs_x=rx, relative_radius=s, misses=miss, relrad_c2=float('%.3g' % (float(q['c2'].rad()) / float(abs(q['c2']).mid())))))
            c2_ok = c2_ok and not miss
    g['C2_second_order_coefficients_sound'] = c2_ok
    info['C2'] = rows

    # REM: remainders at sampled points of the polydiscs (Fourier coefficients in d on a circle, 24 points)
    rows = []; worst = 0.0
    for rx in (1.02, 0.95, 0.87, 0.5, 0.2):
        wp = wz = 0.0
        for th in range(12):
            x = rx * mp.expj(2 * mp.pi * th / 12 + mp.mpf('0.1')); xi = c * x; n = 24
            for rs in (RHO_D, RHO_D / 4):
                ds = [rs * mp.expj(2 * mp.pi * j / n) for j in range(n)]
                v = [S.dev_step(S.F, xi, d) for d in ds]
                cf = [sum(v[j][1] * mp.expj(-2 * mp.pi * j * k / n) for j in range(n)) / n / rs ** k for k in range(3)]
                cz = [sum(v[j][0] / c * mp.expj(-2 * mp.pi * j * k / n) for j in range(n)) / n / rs ** k for k in range(3)]
                rem = max(abs(v[j][1] - cf[0] - cf[1] * ds[j] - cf[2] * ds[j] ** 2) for j in range(n))
                remz = max(abs(v[j][0] / c - cz[0] - cz[1] * ds[j] - cz[2] * ds[j] ** 2) for j in range(n))
                mc = L.pick_constants(MC, arb(rx), rs)
                wp = max(wp, float(rem / (mc['M3'] * rx ** 3 * rs ** 3))); wz = max(wz, float(remz / (mc['MZ3'] * rx ** 4 * rs ** 3)))
        rows.append(dict(abs_x=rx, true_over_bound_Phi=float('%.3g' % wp), true_over_bound_Z=float('%.3g' % wz)))
        worst = max(worst, wp, wz)
    g['REM_remainder_constants_sound'] = bool(rem_ok and worst <= 1.0)
    info['REM_samples'] = rows

    # TUBE: forward step on tube pieces
    rows = []; tube_ok = True
    for rx, rho in (('1.0', 5e-3), ('0.87', 5e-3), ('0.87', 2e-3), ('0.5', 1e-4), ('0.2', 1e-8), ('0.05', 1e-12)):
        for s in ('0.005', '0.000001'):
            xc = centre(rx, '0.1'); r = float(s) * float(rx)
            q = L.tube_step(SER, TAU, MC, xc, r, rho)
            miss = []; tg = tt = 0.0
            for _ in range(6):
                x = tomp(xc) + r * mp.sqrt(rnd.random()) * mp.expj(2 * mp.pi * rnd.random())
                d = rho * mp.expj(2 * mp.pi * rnd.random())
                xi1, d1 = S.dev_step(S.F, c * x, d); x1 = xi1 / c
                xi0, _ = S.dev_step(S.F, c * x, mp.mpc(0)); x0 = xi0 / c
                if not inside(q['gt'], x1 / x - 1):
                    miss.append('gt')
                if not inside(q['dtau'], tau(x1) - tau(x)):
                    miss.append('dtau')
                if not lo(q['dev_lo']) <= abs(d1) <= hi(q['dev_hi']):
                    miss.append('dev')
                rg = abs(x1 / x - x0 / x) / hi(q['gt_dev']); rt = abs(tau(x1) - tau(x0)) / hi(q['dtau_dev'])
                if rg > 1:
                    miss.append('gt_dev')
                if rt > 1:
                    miss.append('dtau_dev')
                tg = max(tg, float(rg)); tt = max(tt, float(rt))
            mid = lambda v: float(abs(v).mid())
            rows.append(dict(abs_x=rx, relative_radius=s, rho=rho, misses=miss,
                             gt_dev_over_abs_g=float('%.3g' % (float(q['gt_dev'].upper()) / mid(q['g']))),
                             dtau_dev_over_abs_dtau0=float('%.3g' % (float(q['dtau_dev'].upper()) / mid(q['dtau0']))),
                             true_over_bound_gt_dev=float('%.3g' % tg), true_over_bound_dtau_dev=float('%.3g' % tt),
                             dev_lo_over_rho=f5(float(q['dev_lo'].lower()) / rho), dev_hi_over_rho=f5(float(q['dev_hi'].upper()) / rho)))
            tube_ok = tube_ok and not miss
    g['TUBE_step_on_tube_pieces_sound'] = tube_ok
    info['TUBE'] = rows

    # INV: local inverse on targets in the sector of D1 (arg xi = 0.26 pi)
    rows = []; inv_ok = True
    for rx, Rp in (('0.87', 5e-3), ('0.87', 2e-3), ('0.6', 1e-4), ('0.3', 1e-7), ('0.1', 1e-10), ('0.03', 1e-14)):
        for s in ('0.005', '0.000001'):
            xcp = centre(rx, '0.26'); rp = float(s) * float(rx)
            iv = L.inverse_step(SER, TAU, MC, xcp, rp, Rp)
            if iv is None:
                rows.append(dict(abs_x=rx, relative_radius=s, Rp=Rp, found=False)); inv_ok = False
                continue
            cc, verified = iv['c'], True
            if o.control == 'SHIFTINV':
                cc = iv['c'] + 3 * iv['r']
                verified = L.inverse_conditions(SER, TAU, MC, cc, iv['r'], iv['rho'], xcp, rp, Rp)[0]
            miss = []
            for _ in range(6):
                x1 = tomp(xcp) + rp * mp.sqrt(rnd.random()) * mp.expj(2 * mp.pi * rnd.random())
                d1 = Rp * mp.sqrt(rnd.random()) * mp.expj(2 * mp.pi * rnd.random())
                xi, d = S.dev_step(S.G, c * x1, d1); x = xi / c
                if not abs(x - tomp(cc)) < iv['r']:
                    miss.append('x')
                if not abs(d) < iv['rho']:
                    miss.append('d')
                if not inside(iv['gG'], x / x1 - 1):
                    miss.append('gG')
                if not inside(iv['dtauG'], tau(x) - tau(x1)):
                    miss.append('dtauG')
            det = iv['details']
            rows.append(dict(abs_x=rx, relative_radius=s, Rp=Rp, found=True, conditions_verified=bool(verified), misses=miss,
                             r_over_rp=f5(iv['r'] / rp), rho_over_Rp=f5(iv['rho'] / Rp), L=float('%.3g' % det['L']),
                             margin_i=float('%.3g' % det['margin_i']), margin_ii=float('%.3g' % det['margin_ii'])))
            inv_ok = inv_ok and verified and not miss
    g['INV_local_inverse_verified_and_sound'] = inv_ok
    info['INV'] = rows

    g = {k: bool(v) for k, v in g.items()}; ok = all(g.values())
    for k in sorted(g):
        print(k, 'PASS' if g[k] else 'FAIL')
    print('RESULT', 'PASS' if ok else 'FAIL', '(control %s)' % o.control if o.control else '', L.run_tail('| development run; not a certificate'))
    with open(o.out, 'w', encoding='utf-8', newline='\n') as f:
        json.dump({'gates': g, 'info': info, 'all_pass': ok, 'control': o.control,
                   'status': L.run_status('stage 3c-a development run; not a certificate'), 'script': 'dyad_open20_an_stage3c_w2b_check.py'},
                  f, indent=1, sort_keys=True)
        f.write('\n')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
