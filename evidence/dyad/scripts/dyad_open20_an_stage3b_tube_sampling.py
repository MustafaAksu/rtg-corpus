#!/usr/bin/env python3
"""dyad_open20_an_stage3b_tube_sampling.py -- OPEN 20 analytic branch, stage 3b DESIGN: [NUM] sampling of the two
inequalities of the tube lemma (records/dyad/DYAD_OPEN20_AN_STAGE3B_DESIGN.md).

STATUS OF EVERY NUMBER: [NUM] feasibility sampling at finitely many points, in floating point at 100 digits.  Not a
certificate, not theorem evidence, no interval arithmetic, no bound between sample points.  No sectorial value, jump or
Stokes-type quantity is computed here; the stage-2b value of the jump is read from its output file for one comparison.

Objects (design record sections 3 and 4).  Pilot branch of F = T^6, raw chart (z, w), xi = c z, truncated series
w = phi_N(z) = sum_{k=2..N} a_k z^k (stage 2).  Normal deviation in the lifted unit:  d = (w - phi_N(z)) / z^2.
  tau(xi)  four-term Fatou coordinate of the restricted map on the series curve:
           tau = A3 z^-3 + A2 z^-2 + A1 z^-1 + kappa log z   (coefficients from the Abel equation, as in stage 2b).
  h0(tau) = Re(e^{i theta0} tau),  h1(tau) = Re(-e^{-i theta0} tau),  theta0 = pi/2 - eta0.
  Local domains through the common point xi* = 0.40 e^{i pi/6}, tau* = tau(xi*).  Each is cut out of a bounded chart
  sector on which log z and log xi are the principal branches:
           chart0 = { 0 < |xi| < 0.60, -0.20 pi < arg xi < 0.30 pi },  chart1 = { 0 < |xi| < 0.60, 0.03 pi < arg xi < 0.50 pi },
           D0 = { xi in chart0:  Re tau > Re tau* - ds,  h0(tau) > h0(tau*) - dc }     (forward map F),
           D1 = { xi in chart1:  Re tau < Re tau* + ds,  h1(tau) > h1(tau*) - dc }     (inverse map G = F^-1).
  Guard property: D0 lies in core0 = { |xi| <= 0.47, -0.08 pi <= arg xi <= 0.20 pi } and D1 in
  core1 = { |xi| <= 0.42, 0.09 pi <= arg xi <= 0.43 pi }; the rest of each chart (the guard zone) has no point that
  satisfies both wedge conditions.  Without the chart the two conditions hold again for |xi| > 0.7 (co-owner review R1).
  Tube radius  R0(xi) = eps |xi^alpha| (Re tau - s0 + 1)^(-q1/3) h0(tau)^(-q2/3)   on D0, s0 = Re tau* - ds,
               R1(xi) = eps |xi^alpha| (s1 - Re tau + 1)^(-q1/3) h1(tau)^(-q2/3)   on D1, s1 = Re tau* + ds,
           eps fixed by R(xi*) = RSTAR.  xi^alpha = exp(alpha log xi), principal log on the sector used.
For a base point xi and the map M (F on D0, G on D1), with (xi', d') = M(xi, d):
  E = d'(xi, 0);  mu0 = derivative of d' in d at d = 0;  nl = max over the sampled circle |d| = R of
  |d' - E - mu0 d| / (|mu0| R);  Rsup = max of R(xi') over the circle.
  (A)  both wedge functionals increase (the first: Re tau - s0, resp. s1 - Re tau; the second: h0, resp. h1), the
       relative step |xi'/xi - 1| is at most KAPPA = 0.15, and the image base point lies in the same domain.
  (B)  strong form:  |mu0| (1 - nl) R(xi) - |E|  >  Rsup.     margin_B = (|mu0|(1 - nl) R - |E|)/Rsup - 1.
       model gain = (q1/3)/first + (q2/3) sin(eta0)/second  (what the leading-order normal form predicts).

Gates (exit 0 iff all pass):
  G0    input hashes (stage-2 coefficients, stage-2b output); both report all_pass.
  F1    A3 = -1/(3 ell) to 1e-30 (the Fatou coordinate belongs to this branch).
  INV   G(F(p)) = p to 1e-80 at 20 sample points (the numerical inverse is the inverse).
  A0, A1   (A) on every sample of D0, D1: first functional gains >= 0.5, second >= 0.2, and every sampled image base
           point satisfies the wedge conditions and lies in the core.
  STEP     |xi'/xi - 1| <= 0.15 on every sample (with the guard zones, a step cannot leave the chart).
  GUARD0, GUARD1   no grid point of the guard zone satisfies the wedge conditions (grid: radii up to 0.595).
  XISTAR   the common point xi* itself, 64 fibre directions: xi* lies in D0 and D1; (A), (B) and |E|/R <= 0.1 hold.
  B0, B1   (B) strong form on every sample of D0, D1: margin_B > 0, and margin_B >= 0.5 * model gain.
  E0, E1   |E| / R <= 0.1 on every sample (the truncated series is well inside its tube).
  NL    nl <= 0.01 on every sample.
  PATH  the curve tau = Re tau* - i t, t from -Im tau* to 3000 (29 points): each point has a preimage xi in the sector
        0 < arg xi < pi/3 (Newton, continued along the curve) with |xi| decreasing; it lies in D0 and in D1 by
        construction.  Reported: |xi| and arg xi at the far end.
  SEP   feasibility of the last step at xi*: 2 R0(xi_end)/amp0 + 2 R1(xi_start) con1 <= 1e-3 * |Delta_Y| (stage 2b),
        where amp0 is the sampled normal amplification of F^n from xi* to xi_end (|xi_end| about 0.096, n = 334) and
        con1 the sampled normal contraction of F^n from xi_start (|xi_start| about 0.099, on the S_1 side) to xi*.
Negative controls (each must exit 1 at the named gates):
  --control SWAP       the two maps exchanged (G on D0, F on D1):  A0, A1, B0, B1 and XISTAR fail.
  --control SHIFTCOEF  a_5 multiplied by 1 + 1e-6 (the tube is centred on a polynomial that is not the formal curve):
                       E0, E1, B0 and B1 fail.
Two controls were tried and dropped (design record section 7): a tube with |xi^(-alpha)| in place of |xi^alpha| still
passes on these wedges, so it is not a negative control; q1 = q2 = 0 gives a tube whose radius grows without bound as
xi -> 0, where the map is no longer evaluated near the curve.
Usage: python3 -I -B dyad_open20_an_stage3b_tube_sampling.py --stage2 scout_N216_dps840.json --stage2b jump_scout.json
          --out OUT.json [--stride k] [--control SWAP|SHIFTCOEF]
"""
import os, sys, json, argparse, hashlib, time
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mpmath as mp
import dyad_open20_an_stage2b_law as LW

STAGE2_SHA = '6ca8c663061ce2fa9e062938a1e6046c932da4cbddccc6e3e2c3de4df68c477e'
STAGE2B_SHA = '610433e549415492a3a5772531a14e596c5d0cee11bed306acd9e6acabd3a268'
N_TUBE, N_FATOU = 40, 80
Q1, ETA_DIV, RSTAR, DS, DC = 9, 8, '2e-3', '0.25', '0.15'      # q1 = q2 = Q1
R_STAR, ARG_STAR_OVER_PI = '0.40', mp.mpf(1) / 6
# Local chart domains (arg in units of pi) and their cores; D_j = {xi in chart: wedge conditions}.  KAPPA_STEP bounds |xi'/xi - 1|.
CHART = {'D0': dict(rmax='0.60', arg=(mp.mpf('-0.20'), mp.mpf('0.30')), core_r='0.47', core_arg=(mp.mpf('-0.08'), mp.mpf('0.20'))),
         'D1': dict(rmax='0.60', arg=(mp.mpf('0.03'), mp.mpf('0.50')), core_r='0.42', core_arg=(mp.mpf('0.09'), mp.mpf('0.43')))}
KAPPA_STEP = '0.15'
EXTRA_RADII = ['0.40', '0.405', '0.41', '0.415', '0.42', '0.44', '0.445', '0.45', '0.455', '0.46', '0.465', '0.47', '0.48',
               '0.50', '0.53', '0.56', '0.595']


def cplx(p):
    return mp.mpc(mp.mpf(p[0]), mp.mpf(p[1]))


class Branch:
    """F = T^6 and its numerical inverse in the raw chart; truncated series of the pilot branch."""
    def __init__(self, info, N):
        self.N = N
        self.a = {k: cplx(info['coefficients'][str(k)]) for k in range(2, N + 1)}
        self.c = cplx(info['c_pil']); self.al = cplx(info['alpha']); self.ell = cplx(info['ell'])
        self.om = mp.mpc(-0.5, mp.sqrt(3) / 2); self.den = mp.mpc(0, mp.sqrt(3))

    def series(self, z):
        s = mp.mpc(0)
        for k in range(self.N, 1, -1):
            s = s * z + self.a[k]
        return s * z * z

    def F(self, z, w):
        eta = (z - w) / self.den; rho = z - self.om * eta
        for _ in range(6):
            s = mp.sin(eta); rho, eta = rho - s, eta + mp.expm1(rho) - s
        return rho + self.om * eta, rho + mp.conj(self.om) * eta

    def G(self, z, w):
        eta = (z - w) / self.den; rho = z - self.om * eta
        tol = mp.mpf(10) ** (-(mp.mp.dps - 6))
        for _ in range(6):                      # one inverse step of T: Newton on the old eta
            e = eta
            for _ in range(80):
                s = mp.sin(e)
                de = (e + mp.expm1(rho + s) - s - eta) / (1 + mp.exp(rho + s) * mp.cos(e) - mp.cos(e))
                e -= de
                if abs(de) < tol:
                    break
            rho, eta = rho + mp.sin(e), e
        return rho + self.om * eta, rho + mp.conj(self.om) * eta

    def dev_step(self, mapf, xi, d):
        z = xi / self.c
        z1, w1 = mapf(z, self.series(z) + z * z * d)
        return self.c * z1, (w1 - self.series(z1)) / z1 ** 2


def fatou4(S):
    """A3, A2, A1, kappa of the formal Fatou coordinate of f(z) = F_z(z, phi(z)) (procedure of the stage-2b law script)."""
    K_MAX, J_MAX, M_C = 22, 12, 128
    R = mp.mpf('0.1'); vals = []
    for j in range(M_C):
        z = R * mp.exp(2j * mp.pi * j / M_C)
        vals.append(S.F(z, S.series(z))[0])
    f = [sum(vals[j] * mp.exp(-2j * mp.pi * j * k / M_C) for j in range(M_C)) / (M_C * R ** k) for k in range(K_MAX + 1)]
    n = J_MAX + 4
    u = ([mp.mpc(0)] + [f[k + 1] for k in range(1, n + 4)])[:n + 4]

    def shifted(series, shift):
        out = [mp.mpc(0)] * (n + 1)
        for i, x in enumerate(series):
            if 0 <= i + shift <= n:
                out[i + shift] += x
        return out

    def minus_one(sr):
        sr = list(sr); sr[0] -= 1; return sr
    basis = {-p: shifted(minus_one(LW.spow(u, -p, n + 3)), -p) for p in (3, 2, 1)}
    basis['log'] = LW.slog(u, n + 3)[:n + 1]
    coef = {}; defect = [mp.mpc(0)] * (n + 1); defect[0] = mp.mpc(-1)
    for row, key in enumerate([-3, -2, -1, 'log']):
        c = -defect[row] / basis[key][row]; coef[key] = c
        defect = [d + c * b for d, b in zip(defect, basis[key])]
    return coef


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--stage2', required=True); ap.add_argument('--stage2b', required=True); ap.add_argument('--out', required=True)
    ap.add_argument('--stride', type=int, default=1); ap.add_argument('--control', choices=['SWAP', 'SHIFTCOEF'])
    # exploration only (the recorded run uses the defaults): other tube parameters, and a lower cut on the radius index
    ap.add_argument('--q', type=int, default=Q1); ap.add_argument('--rstar', default=RSTAR); ap.add_argument('--dc', default=DC)
    ap.add_argument('--ds', default=DS); ap.add_argument('--eta-div', type=int, default=ETA_DIV); ap.add_argument('--first-index', type=int, default=0)
    o = ap.parse_args()
    t_start = time.time()
    mp.mp.dps = 100
    raw2 = open(o.stage2, 'rb').read(); raw2b = open(o.stage2b, 'rb').read()
    d2 = json.loads(raw2.decode('utf-8')); d2b = json.loads(raw2b.decode('utf-8'))
    g, info = {}, {}
    g['G0_inputs'] = (hashlib.sha256(raw2).hexdigest() == STAGE2_SHA and hashlib.sha256(raw2b).hexdigest() == STAGE2B_SHA
                      and d2.get('all_pass') is True and d2b.get('all_pass') is True)
    S = Branch(d2['info'], N_TUBE)
    co = fatou4(Branch(d2['info'], N_FATOU))
    g['F1_A3_is_minus_one_over_3ell'] = abs(co[-3] + 1 / (3 * S.ell)) < mp.mpf(10) ** (-30)
    info['fatou4'] = {'A3': mp.nstr(co[-3], 15), 'A2': mp.nstr(co[-2], 15), 'A1': mp.nstr(co[-1], 15), 'kappa': mp.nstr(co['log'], 15)}
    q1 = mp.mpf(o.q); q2 = mp.mpf(o.q)
    al_w = S.al
    if o.control == 'SHIFTCOEF':
        S.a[5] = S.a[5] * (1 + mp.mpf(10) ** (-6))
    eta0 = mp.pi / o.eta_div; th0 = mp.pi / 2 - eta0; ds = mp.mpf(o.ds); dc = mp.mpf(o.dc); rstar = mp.mpf(o.rstar)

    def tau(xi):
        z = xi / S.c
        return co[-3] / z ** 3 + co[-2] / z ** 2 + co[-1] / z + co['log'] * mp.log(z)

    def dtau(xi):                                     # d tau / d xi
        z = xi / S.c
        return (-3 * co[-3] / z ** 4 - 2 * co[-2] / z ** 3 - co[-1] / z ** 2 + co['log'] / z) / S.c
    h0 = lambda t: (mp.expj(th0) * t).real
    h1 = lambda t: (-mp.expj(-th0) * t).real
    xis = mp.mpf(R_STAR) * mp.expjpi(ARG_STAR_OVER_PI); ts = tau(xis)
    s0, s1, c0, c1 = ts.real - ds, ts.real + ds, h0(ts) - dc, h1(ts) - dc
    info['parameters'] = dict(N=N_TUBE, q1=o.q, q2=o.q, eta0='pi/%d' % o.eta_div, R_at_xi_star=o.rstar, ds=o.ds, dc=o.dc, xi_star_abs=R_STAR,
                              xi_star_arg='pi/6', tau_star=mp.nstr(ts, 12), s0=mp.nstr(s0, 8), s1=mp.nstr(s1, 8), c0=mp.nstr(c0, 8),
                              c1=mp.nstr(c1, 8), stride=o.stride, dps=100, first_index=o.first_index)
    map0, map1 = (S.G, S.F) if o.control == 'SWAP' else (S.F, S.G)
    sides = {'D0': (lambda t: t.real - s0 + 1, h0, lambda t: t.real > s0 and h0(t) > c0, map0),
             'D1': (lambda t: s1 - t.real + 1, h1, lambda t: t.real < s1 and h1(t) > c1, map1)}
    Rfun = {}
    for side, (first, second, inD, mapf) in sides.items():
        raw_w = (lambda first, second: lambda xi: abs(mp.exp(al_w * mp.log(xi))) * first(tau(xi)) ** (-q1 / 3) * second(tau(xi)) ** (-q2 / 3))(first, second)
        norm = rstar / raw_w(xis)
        Rfun[side] = (lambda raw_w, norm: lambda xi: norm * raw_w(xi))(raw_w, norm)

    # INV
    worst_inv = mp.mpf(0)
    for i in range(20):
        z = mp.mpf('0.05') * (1 + i) / S.c * mp.expjpi(mp.mpf(i) / 37) / 2
        w = S.series(z) * (1 + mp.mpf(i) / 1000)
        z2, w2 = S.G(*S.F(z, w))
        worst_inv = max(worst_inv, abs(z2 - z) + abs(w2 - w))
    g['INV_G_inverts_F'] = worst_inv < mp.mpf(10) ** (-80); info['INV_max_error'] = mp.nstr(worst_inv, 3)

    # sampling of (A), (B) on the local domains
    def in_box(xi, rmax, arg):
        a = mp.arg(xi) / mp.pi
        return 0 < abs(xi) <= mp.mpf(rmax) and arg[0] <= a <= arg[1]

    def sample(side, xi, ndir):
        """E, mu0, nl, margin_B, model gain, gains of the two functionals, relative step, image-in-domain flag at one base point."""
        first, second, inD, mapf = sides[side]; R = Rfun[side]; ch = CHART[side]
        t = tau(xi); Rx = R(xi)
        _, E = S.dev_step(mapf, xi, mp.mpc(0))
        hh = Rx * mp.mpf(10) ** (-20)
        mu0 = (S.dev_step(mapf, xi, hh)[1] - E) / hh
        nl = mp.mpf(0); Rsup = mp.mpf(0); g1 = mp.inf; g2 = mp.inf; step = mp.mpf(0); image_ok = True
        for k in range(ndir):
            d = Rx * mp.expjpi(2 * mp.mpf(k) / ndir)
            xp, dp = S.dev_step(mapf, xi, d); tp = tau(xp)
            g1 = min(g1, first(tp) - first(t)); g2 = min(g2, second(tp) - second(t))
            step = max(step, abs(xp / xi - 1))
            image_ok = image_ok and inD(tp) and in_box(xp, ch['core_r'], ch['core_arg'])
            nl = max(nl, abs(dp - E - mu0 * d) / (abs(mu0) * Rx)); Rsup = max(Rsup, R(xp))
        margin = (abs(mu0) * (1 - nl) * Rx - abs(E)) / Rsup - 1
        model = (q1 / 3) / first(t) + (q2 / 3) * mp.sin(eta0) / second(t)
        return dict(margin=margin, model=model, E_over_R=abs(E) / Rx, nl=nl, g1=g1, g2=g2, step=step, image_ok=image_ok)

    radii = [mp.mpf('0.01') * mp.mpf(10) ** (mp.mpf(ir) / 25) for ir in range(o.first_index, 42, o.stride)]
    radii += [mp.mpf(x) for x in EXTRA_RADII]
    radii = sorted(set(radii))
    bands = [('0.01', '0.03'), ('0.03', '0.06'), ('0.06', '0.10'), ('0.10', '0.15'), ('0.15', '0.20'), ('0.20', '0.25'),
             ('0.25', '0.30'), ('0.30', '0.35'), ('0.35', '0.41'), ('0.41', '0.48')]
    max_step = mp.mpf(0)
    for side, (first, second, inD, mapf) in sides.items():
        ch = CHART[side]
        tot = dict(points=0, min_first_gain=mp.inf, min_second_gain=mp.inf, min_margin=mp.inf, min_margin_over_model=mp.inf,
                   max_E_over_R=mp.mpf(0), max_nl=mp.mpf(0), max_abs_xi=mp.mpf(0), min_arg_over_pi=mp.inf, max_arg_over_pi=-mp.inf,
                   max_rel_step=mp.mpf(0), worst_at=None)
        guard = dict(grid_points_in_chart=0, grid_points_in_guard_zone=0, wedge_points_in_guard_zone=0, images_outside_domain=0)
        per = {b: dict(points=0, min_margin=mp.inf, model_gain_there=None, max_E_over_R=mp.mpf(0)) for b in bands}
        ia_lo = int(mp.ceil(ch['arg'][0] * 96 + mp.mpf('0.001'))); ia_hi = int(mp.floor(ch['arg'][1] * 96 - mp.mpf('0.001')))
        for r in radii:
            for ia in range(ia_lo, ia_hi + 1, o.stride):
                xi = r * mp.expjpi(mp.mpf(ia) / 96); t = tau(xi)
                guard['grid_points_in_chart'] += 1
                core = in_box(xi, ch['core_r'], ch['core_arg'])
                if not core:
                    guard['grid_points_in_guard_zone'] += 1
                if not inD(t):
                    continue
                if not core:
                    guard['wedge_points_in_guard_zone'] += 1
                    continue
                m = sample(side, xi, 8)
                tot['points'] += 1; tot['max_abs_xi'] = max(tot['max_abs_xi'], r)
                tot['min_arg_over_pi'] = min(tot['min_arg_over_pi'], mp.mpf(ia) / 96); tot['max_arg_over_pi'] = max(tot['max_arg_over_pi'], mp.mpf(ia) / 96)
                tot['min_first_gain'] = min(tot['min_first_gain'], m['g1']); tot['min_second_gain'] = min(tot['min_second_gain'], m['g2'])
                tot['max_rel_step'] = max(tot['max_rel_step'], m['step'])
                if not m['image_ok']:
                    guard['images_outside_domain'] += 1
                if m['margin'] < tot['min_margin']:
                    tot['min_margin'] = m['margin']; tot['worst_at'] = '|xi|=%s arg=%s pi' % (mp.nstr(r, 4), mp.nstr(mp.mpf(ia) / 96, 4))
                tot['min_margin_over_model'] = min(tot['min_margin_over_model'], m['margin'] / m['model'])
                tot['max_E_over_R'] = max(tot['max_E_over_R'], m['E_over_R']); tot['max_nl'] = max(tot['max_nl'], m['nl'])
                for b in bands:
                    if mp.mpf(b[0]) <= r < mp.mpf(b[1]):
                        per[b]['points'] += 1; per[b]['max_E_over_R'] = max(per[b]['max_E_over_R'], m['E_over_R'])
                        if m['margin'] < per[b]['min_margin']:
                            per[b]['min_margin'] = m['margin']; per[b]['model_gain_there'] = m['model']
        k = side[-1]; max_step = max(max_step, tot['max_rel_step'])
        g['A%s_base_moves_inward' % k] = (tot['points'] > 0 and tot['min_first_gain'] >= 0.5 and tot['min_second_gain'] >= 0.2
                                          and guard['images_outside_domain'] == 0)
        g['B%s_strong_exit_inequality' % k] = tot['points'] > 0 and tot['min_margin'] > 0 and tot['min_margin_over_model'] >= 0.5
        g['E%s_series_inside_tube' % k] = tot['points'] > 0 and tot['max_E_over_R'] <= 0.1
        g['GUARD%s_local_component_inside_core' % k] = guard['grid_points_in_guard_zone'] > 0 and guard['wedge_points_in_guard_zone'] == 0
        g.setdefault('NL_nonlinearity_small', True)
        g['NL_nonlinearity_small'] = g['NL_nonlinearity_small'] and tot['max_nl'] <= 0.01
        info[side] = {a: (mp.nstr(b, 6) if isinstance(b, mp.mpf) else b) for a, b in tot.items()}
        info[side + '_guard'] = dict(guard, chart=dict(rmax=ch['rmax'], arg_over_pi=[mp.nstr(x, 4) for x in ch['arg']]),
                                     core=dict(rmax=ch['core_r'], arg_over_pi=[mp.nstr(x, 4) for x in ch['core_arg']]))
        info[side + '_by_radius'] = [dict(band='%s-%s' % b, points=per[b]['points'],
                                          min_margin_B=(mp.nstr(per[b]['min_margin'], 4) if per[b]['points'] else None),
                                          model_gain_there=(mp.nstr(per[b]['model_gain_there'], 4) if per[b]['points'] else None),
                                          max_E_over_R=mp.nstr(per[b]['max_E_over_R'], 3)) for b in bands]
        print('%s: %d points, |xi| <= %s, min margin_B %s (%s), min margin/model %s, max |E|/R %s, max nl %s, gains >= %s, %s, rel step <= %s; guard zone: %d grid points, %d in wedge' % (
            side, tot['points'], mp.nstr(tot['max_abs_xi'], 4), mp.nstr(tot['min_margin'], 4), tot['worst_at'], mp.nstr(tot['min_margin_over_model'], 4),
            mp.nstr(tot['max_E_over_R'], 3), mp.nstr(tot['max_nl'], 3), mp.nstr(tot['min_first_gain'], 3), mp.nstr(tot['min_second_gain'], 3),
            mp.nstr(tot['max_rel_step'], 3), guard['grid_points_in_guard_zone'], guard['wedge_points_in_guard_zone']), flush=True)
    g['STEP_relative_step_below_kappa'] = max_step <= mp.mpf(KAPPA_STEP)
    info['STEP'] = dict(max_relative_step=mp.nstr(max_step, 4), kappa=KAPPA_STEP)

    # XISTAR: the common point itself, 64 fibre directions
    xs = {}; xs_ok = True
    for side, (first, second, inD, mapf) in sides.items():
        ch = CHART[side]
        m = sample(side, xis, 64)
        member = inD(ts) and in_box(xis, ch['core_r'], ch['core_arg'])
        xs[side] = dict(in_domain=bool(member), margin_B=mp.nstr(m['margin'], 5), first_gain=mp.nstr(m['g1'], 5), second_gain=mp.nstr(m['g2'], 5),
                        E_over_R=mp.nstr(m['E_over_R'], 4), nl=mp.nstr(m['nl'], 4), image_in_domain=bool(m['image_ok']))
        xs_ok = xs_ok and member and m['margin'] > 0 and m['g1'] >= 0.5 and m['g2'] >= 0.2 and m['image_ok'] and m['E_over_R'] <= 0.1
    g['XISTAR_common_point'] = xs_ok; info['XISTAR'] = xs

    # PATH
    path_ok = True; xi = xis; prev = abs(xis) * (1 + mp.mpf(10) ** (-30)); path = []
    for i in range(29):
        t_im = -ts.imag * (mp.mpf(3000) / (-ts.imag)) ** (mp.mpf(i) / 28)
        target = mp.mpc(ts.real, -t_im)
        for _ in range(60):
            dx = (tau(xi) - target) / dtau(xi); xi = xi - dx
            if abs(dx) < mp.mpf(10) ** (-80) * abs(xi):
                break
        ok = abs(tau(xi) - target) < mp.mpf(10) ** (-60) and 0 < mp.arg(xi) < mp.pi / 3 and abs(xi) < prev
        ok = ok and sides['D0'][2](mp.mpc(ts.real, -t_im)) and sides['D1'][2](mp.mpc(ts.real, -t_im))
        path_ok = path_ok and ok; prev = abs(xi); path.append((mp.nstr(t_im, 6), mp.nstr(abs(xi), 6), mp.nstr(mp.arg(xi) / mp.pi, 6)))
    g['PATH_common_curve_reaches_small_xi'] = path_ok
    info['PATH_first_and_last'] = dict(first=path[0], last=path[-1], columns='-Im tau, |xi|, arg xi / pi')

    # SEP
    row = [x for x in d2b['info']['table_base'] if mp.mpf(x['r']) == mp.mpf(R_STAR)][0]
    n = int(row['n']); dY = mp.mpf(row['abs_deltaY'])
    # forward leg from xi*: sampled amplification of the normal deviation over n steps
    def leg(xi_a, d_a):
        x, d = xi_a, d_a
        for _ in range(n):
            x, d = S.dev_step(S.F, x, d)
        return x, d
    e = mp.mpf(10) ** (-40)
    xe, de0 = leg(xis, mp.mpc(0)); _, de1 = leg(xis, e)
    amp0 = abs(de1 - de0) / e
    xi_start = mp.mpf(row['abs_xi0']) * mp.expjpi(mp.mpf(row['arg_xi0_over_pi']))
    xb, db0 = leg(xi_start, mp.mpc(0)); _, db1 = leg(xi_start, e)
    con1 = abs(db1 - db0) / e
    r0_end = Rfun['D0'](xe); r1_start = Rfun['D1'](xi_start)
    width = 2 * r0_end / amp0 + 2 * r1_start * con1
    info['SEP'] = dict(n=n, abs_deltaY_stage2b=row['abs_deltaY'], xi_end_abs=mp.nstr(abs(xe), 6), R0_at_xi_end=mp.nstr(r0_end, 4),
                       amplification_forward=mp.nstr(amp0, 6), xi_start_abs=mp.nstr(abs(xi_start), 6), R1_at_xi_start=mp.nstr(r1_start, 4),
                       contraction_from_S1_side=mp.nstr(con1, 6), end_of_S1_leg_abs_xi=mp.nstr(abs(xb), 6),
                       estimated_total_width=mp.nstr(width, 4), width_over_abs_deltaY=mp.nstr(width / dY, 4),
                       in_wedges=bool(sides['D0'][2](tau(xe)) and sides['D1'][2](tau(xi_start))))
    g['SEP_width_far_below_jump'] = width <= mp.mpf(10) ** (-3) * dY and info['SEP']['in_wedges']

    info['seconds'] = round(time.time() - t_start, 1)
    g = {k: bool(v) for k, v in g.items()}; ok = all(g.values())
    for k in sorted(g):
        print(k, 'PASS' if g[k] else 'FAIL')
    print('RESULT', 'PASS' if ok else 'FAIL', '(control %s)' % o.control if o.control else '', '| [NUM] sampling for a design; not a certificate')
    seconds = info.pop('seconds')
    with open(o.out, 'w', encoding='utf-8', newline='\n') as f:
        json.dump({'gates': g, 'info': info, 'all_pass': ok, 'control': o.control,
                   'status': 'NUM feasibility sampling for the stage-3b design; not a certificate; not theorem evidence',
                   'script': 'dyad_open20_an_stage3b_tube_sampling.py', 'mpmath': mp.__version__}, f, indent=1, sort_keys=True)
        f.write('\n')
    print('seconds', seconds)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
