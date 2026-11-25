#!/usr/bin/env python3
"""dyad_open20_an_stage2b_jump_scout.py -- OPEN 20 analytic branch, stage 2b: [NUM] scouting of the sectorial jump itself.

Authorized by the PI on 11 November 2026 (design record records/dyad/DYAD_OPEN20_AN_SECTORIAL_PILOT_DESIGN.md section 9).
STATUS OF EVERY NUMBER: [NUM] scouting. Not a certificate, not theorem evidence. No error bound is proved.

What is measured.  Pilot branch w = phi(z) of F = T^6 (root a_pil, Im a > 0), with formal series sum_{k=2..N} a_k z^k
(stage 2, evidence/dyad/open20-an/stage2/scout_N216_dps840.json).  xi = c z, c the principal cube root of -ell, so that
xi' = xi - xi^4 + ... on the curve.  Forward orbits tend to 0 along arg xi = 0 (sector S_0); backward orbits along
arg xi = pi/3 (sector S_1).  For a point xi* on arg xi = pi/6 (centre of the overlap S_0 and S_1, design D7), z* = xi*/c:
  phi_1(z*)  value of the curve of S_1 at z*: the w-coordinate of F^n(z_0, phi_N(z_0)), where z_0 is a point of small |xi|
             near arg xi = pi/3 on the truncated series, chosen (secant iteration) so that the z-coordinate after n steps is
             exactly z*.  Forward iteration is used throughout; along S_1 it contracts transversally.
  phi_0(z*)  value of the curve of S_0 at z*: the w for which the forward orbit of (z*, w), after m steps, lies on the
             truncated series at small |xi| near arg xi = 0 (Newton iteration on w; forward iteration expands transversally,
             so the condition determines w sharply).
  Delta(z*) = phi_1(z*) - phi_0(z*)   (design D9: the jump on the overlap of S_0 and S_1, at one common point).
Delta_Y = Delta / z*^2 is the same difference in the lifted coordinate (w = z^2 (a + y)).
If the formal curve converged, both values would be the same analytic function and Delta would vanish.

The map is the full map (complex sin and expm1 at working precision), never a jet.  Only the starting and matching points use
the truncated series, at |xi| about r_m, where its terms are far below the working accuracy of the stored coefficients
(80 digits).  The measurement is repeated with other r_m, N and precision; the same z* is hit each time.  The base configuration
finds its start point from the leading time model; the others start from the base start point, moved along the same
orbit (forward by the map, or backward by inverting the restricted map on the series curve), then refined by the secant.

Model for comparison only: leading law |Delta_Y| ~ const * exp(-(2 pi/3)/|xi*|^3) (Borel singularity 2 pi i in the time
t = 1/(3 xi^3)); stage 2 could not fix this scale (A_xi between 1.77 and 2.09).

Control with an exactly zero jump (ZERO): the time-one map of the vector field  xi' = -xi^4, Y' = -alpha xi^3 Y + xi^5
(same k = 3 and the same alpha), which has the polynomial invariant curve Y = xi^2/(alpha - 2).  The same harness must
return |Delta_Y| at rounding level.

Gates (exit 0 iff all pass):
  G0   input hash: stage-2 N=216 file SHA-256 6ca8c663...477e; its all_pass is true.
  G_ON the map and the series agree near the start: |w_j - phi_N(z_j)| <= 1e-60 |w_j| on the first three steps.
  G_SEC, G_NEWTON  the secant iteration for z_0 and the Newton iteration for w converged (last step below 1e-(dps-20)
       relative).  The first-order value D/A of the jump (mismatch after the forward leg divided by the amplification) is
       reported with its relative difference from the converged value; it is not a gate (the difference is of second order
       in the jump and reaches several per cent at the largest radius).
  G_STAB for every radius, the jump agrees across the configurations (N, r_m, dps) to 1e-6 relative.
  G_ZERO the ZERO control returns |Delta_Y| < 1e-(dps-50) at every radius.
Not a gate (the finding): whether Delta is nonzero, its size, and the fitted exponent.
Radii above about 0.45 are outside the harness: the start-point iteration leaves the neighbourhood of 0 (observed at 0.50).
Negative controls (each must exit 1): --control SHIFTCOEF (a_5 changed by 1e-20 relative: G_ON and G_STAB fail),
  --control WRONGMAP (sin(eta) in the second component of T multiplied by 1 + 1e-20: G_ON fails).
An orbit that leaves the neighbourhood of 0 is reported as the failed gate G_ORBIT, not as a crash.
Usage: python3 -I -B dyad_open20_an_stage2b_jump_scout.py --stage2 scout_N216_dps840.json --out OUT.json
          [--radii 0.45,0.40,...] [--quick] [--control SHIFTCOEF|WRONGMAP]
"""
import sys, json, argparse, hashlib, time
sys.dont_write_bytecode = True
import mpmath as mp

STAGE2_SHA = '6ca8c663061ce2fa9e062938a1e6046c932da4cbddccc6e3e2c3de4df68c477e'


class Dyad:
    """F = T^6 in the real chart, complexified; x = z, y = w."""
    def __init__(self, data, N, control=None):
        info = data['info']
        self.N = N
        self.a = {k: mp.mpc(mp.mpf(info['coefficients'][str(k)][0]), mp.mpf(info['coefficients'][str(k)][1])) for k in range(2, N + 1)}
        if control == 'SHIFTCOEF':
            self.a[5] = self.a[5] * (1 + mp.mpf(10) ** (-20))
        self.c = mp.mpc(mp.mpf(info['c_pil'][0]), mp.mpf(info['c_pil'][1]))
        self.om = mp.mpc(-0.5, mp.sqrt(3) / 2)
        self.den = mp.mpc(0, mp.sqrt(3))            # omega - conj(omega)
        self.fac = 1 + mp.mpf(10) ** (-20) if control == 'WRONGMAP' else 1
        self.name = 'DYAD F = T^6'

    def series(self, z):
        s = mp.mpc(0)
        for k in range(self.N, 1, -1):
            s = s * z + self.a[k]
        return s * z * z

    def state(self, z, w):
        eta = (z - w) / self.den
        return (z - self.om * eta, eta)

    def xy(self, st):
        rho, eta = st
        return rho + self.om * eta, rho + mp.conj(self.om) * eta

    def step(self, st):
        rho, eta = st
        for _ in range(6):
            if abs(rho) > 8 or abs(eta) > 8:
                raise ArithmeticError('orbit left the neighbourhood of 0 (|rho| or |eta| > 8): radius too large for this harness')
            s = mp.sin(eta)
            rho, eta = rho - s, eta + mp.expm1(rho) - s * self.fac
        return (rho, eta)

    def xi(self, z):
        return self.c * z


class Zero:
    """Time-one map of xi' = -xi^4, Y' = -alpha xi^3 Y + xi^5; invariant curve Y = xi^2/(alpha-2); jump exactly 0."""
    def __init__(self, alpha):
        self.al = alpha; self.name = 'ZERO control (time-one map of a vector field)'

    def series(self, x):
        return x * x / (self.al - 2)

    def state(self, x, y):
        return (x, y)

    def xy(self, st):
        return st

    def step(self, st):
        x, y = st
        u = 1 + 3 * x ** 3
        x1 = x * mp.exp(-mp.log(u) / 3)
        return (x1, self.series(x1) + (y - self.series(x)) * mp.exp(-self.al * mp.log(u) / 3))

    def xi(self, x):
        return x


def iterate(S, st, n):
    for _ in range(n):
        st = S.step(st)
    return st


def measure(S, r, r_m, guess=None):
    """Jump at xi* = r e^{i pi/6}.  Returns a dict of mp numbers and convergence flags."""
    tol = mp.mpf(10) ** (-(mp.mp.dps - 20))
    xis = r * mp.exp(1j * mp.pi / 6)
    one = S.xi(mp.mpc(1))
    zs = xis / one                                  # x-coordinate of the common point
    T = 1 / (3 * r ** 3)
    tm = 1 / (3 * mp.mpf(r_m) ** 3)
    n = int(mp.ceil(mp.sqrt(max(tm * tm - T * T, 1))))

    def end_x(z0):
        st = iterate(S, S.state(z0, S.series(z0)), n)
        return S.xy(st), st

    # start point: a first guess, then secant on z_0
    if guess is None:                                # t-model fixed point (base configuration)
        tstar = 1 / (3 * xis ** 3)
        t0 = tstar - n
        for _ in range(8):
            xi0 = mp.exp(mp.log(1 / (3 * t0)) / 3)  # principal cube root: arg in (pi/6, pi/3)
            (zn, wn), _ = end_x(xi0 / one)
            t0 = t0 - (1 / (3 * S.xi(zn) ** 3) - tstar)
        z_a = mp.exp(mp.log(1 / (3 * t0)) / 3) / one
    else:                                            # from the base configuration's start point (z_g, n_g), same orbit
        z_a, n_g = guess
        if n < n_g:                                  # start later on the same orbit: iterate forward
            z_a = S.xy(iterate(S, S.state(z_a, S.series(z_a)), n_g - n))[0]
        for _ in range(n - n_g):                     # start earlier: invert the restricted map on the series curve
            fz = lambda zz: S.xy(S.step(S.state(zz, S.series(zz))))[0]
            zz = z_a - (fz(z_a) - z_a)
            for _ in range(60):
                e = fz(zz) - z_a
                if abs(e) <= tol * abs(z_a):
                    break
                hh = zz * mp.mpf(10) ** (-(mp.mp.dps // 3))
                zz = zz - e * hh / (fz(zz + hh) - fz(zz))
            z_a = zz
    z_b = z_a * (1 + mp.mpf(10) ** (-12))
    g_a = end_x(z_a)[0][0] - zs; g_b = end_x(z_b)[0][0] - zs
    sec_ok = False
    for _ in range(40):
        if abs(g_b) <= tol * abs(zs):
            sec_ok = True; break
        z_a, z_b, g_a = z_b, z_b - g_b * (z_b - z_a) / (g_b - g_a), g_b
        g_b = end_x(z_b)[0][0] - zs
    z0 = z_b
    # on-curve residual on the first three steps
    st = S.state(z0, S.series(z0)); on = mp.mpf(0)
    for _ in range(3):
        st = S.step(st); x, y = S.xy(st)
        on = max(on, abs(y - S.series(x)) / abs(y))
    (zn, w1), _ = end_x(z0)                          # w1 = phi_1(z*)
    # forward leg: G(w) = y_m - series(x_m) for the orbit of (z*, w)
    def G(w):
        x, y = S.xy(iterate(S, S.state(zs, w), n))
        return y - S.series(x), x
    D, x_end = G(w1)
    h = abs(w1) * mp.mpf(10) ** (-(mp.mp.dps // 3))
    A = (G(w1 + h)[0] - D) / h
    first_order = D / A
    w = w1; newt_ok = False                         # Newton on w with the derivative recomputed at every step
    for _ in range(40):
        g, _ = G(w)
        dg = (G(w + h)[0] - g) / h
        step = g / dg
        w = w - step
        if abs(step) <= tol * abs(w1):
            newt_ok = True; break
    delta = w1 - w
    return dict(r=r, T=T, n=n, z_star=zs, xi0=S.xi(z0), xi_end=S.xi(x_end), w1=w1, D=D, A=A, first_order=first_order,
                delta=delta, deltaY=delta / zs ** 2, on_curve=on, sec_ok=sec_ok, newt_ok=newt_ok)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--stage2', required=True); ap.add_argument('--out', required=True)
    ap.add_argument('--radii', default='0.45,0.42,0.40,0.37,0.35,0.32,0.30,0.28,0.26,0.24')
    ap.add_argument('--quick', action='store_true', help='base configuration only (no stability matrix)')
    ap.add_argument('--control', choices=['SHIFTCOEF', 'WRONGMAP'])
    o = ap.parse_args()
    t_start = time.time()
    raw = open(o.stage2, 'rb').read(); data = json.loads(raw.decode('utf-8'))
    g, info = {}, {}
    g['G0_stage2_hash'] = hashlib.sha256(raw).hexdigest() == STAGE2_SHA and data.get('all_pass') is True
    radii = [mp.mpf(x) for x in o.radii.split(',')]
    configs = [dict(N=216, r_m='0.10', dps=160, tag='base')]
    if not o.quick:
        configs += [dict(N=216, r_m='0.08', dps=160, tag='smaller matching radius'),
                    dict(N=216, r_m='0.12', dps=160, tag='larger matching radius'),
                    dict(N=144, r_m='0.10', dps=160, tag='fewer coefficients'),
                    dict(N=216, r_m='0.10', dps=230, tag='higher precision')]
    res = {}
    ok_on = ok_sec = ok_newt = True
    try:
        for cf in configs:
            mp.mp.dps = cf['dps']
            S = Dyad(data, cf['N'], o.control)
            for r in radii:
                key = mp.nstr(r, 4)
                gs = None if cf['tag'] == 'base' else (res[('base', key)]['xi0'] / S.c, res[('base', key)]['n'])
                m = measure(S, r, cf['r_m'], gs)
                res[(cf['tag'], key)] = m
                ok_on = ok_on and m['on_curve'] <= mp.mpf(10) ** (-60)
                ok_sec = ok_sec and m['sec_ok']; ok_newt = ok_newt and m['newt_ok']
                print('%-26s r=%s  n=%d  |Delta_Y|=%s  on-curve=%s' % (cf['tag'], mp.nstr(r, 4), m['n'], mp.nstr(abs(m['deltaY']), 12), mp.nstr(m['on_curve'], 3)), flush=True)
        g['G_ORBIT_stays_near_0'] = True
    except ArithmeticError as e:
        g['G_ORBIT_stays_near_0'] = False
        info['orbit_error'] = str(e)
    if not g['G_ORBIT_stays_near_0']:
        for k in sorted(g):
            print(k, 'PASS' if g[k] else 'FAIL')
        print('RESULT FAIL', '(control %s)' % o.control if o.control else '', '| [NUM] scouting; not a certificate')
        with open(o.out, 'w', encoding='utf-8', newline='\n') as f:
            json.dump({'gates': {k: bool(v) for k, v in g.items()}, 'info': info, 'all_pass': False, 'control': o.control,
                       'script': 'dyad_open20_an_stage2b_jump_scout.py'}, f, indent=1, sort_keys=True); f.write('\n')
        return 1
    g['G_ON_map_and_series_agree'] = ok_on
    g['G_SEC_secant_converged'] = ok_sec
    g['G_NEWTON_converged'] = ok_newt
    # stability
    mp.mp.dps = 60
    stab = {}; ok_stab = True
    for r in radii:
        key = mp.nstr(r, 4); base = res[('base', key)]['delta']
        spread = mp.mpf(0)
        for cf in configs[1:]:
            spread = max(spread, abs(res[(cf['tag'], key)]['delta'] - base) / abs(base))
        stab[key] = mp.nstr(spread, 3)
        ok_stab = ok_stab and spread <= mp.mpf(10) ** (-6)
    g['G_STAB_across_N_rm_dps'] = ok_stab if not o.quick else True
    info['stability_max_relative_spread'] = stab
    # ZERO control
    mp.mp.dps = 160
    al = mp.mpc(mp.mpf(data['info']['alpha'][0]), mp.mpf(data['info']['alpha'][1]))
    Z = Zero(al); zero = {}; ok_zero = True
    for r in radii:
        m = measure(Z, r, '0.10')
        zero[mp.nstr(r, 4)] = mp.nstr(abs(m['deltaY']), 3)
        ok_zero = ok_zero and abs(m['deltaY']) < mp.mpf(10) ** (-(160 - 50)) and m['sec_ok']
    g['G_ZERO_control_at_rounding_level'] = ok_zero
    info['zero_control_abs_deltaY'] = zero
    # table and fits (base configuration)
    mp.mp.dps = 60
    rows = []
    for r in radii:
        m = res[('base', mp.nstr(r, 4))]
        rows.append(dict(r=mp.nstr(r, 4), T=mp.nstr(m['T'], 8), n=m['n'],
                         abs_delta_w=mp.nstr(abs(m['delta']), 15), abs_deltaY=mp.nstr(abs(m['deltaY']), 15),
                         arg_deltaY_over_pi=mp.nstr(mp.arg(m['deltaY']) / mp.pi, 10),
                         model_exp_minus_2piT=mp.nstr(mp.exp(-2 * mp.pi * m['T']), 6),
                         ratio_to_model=mp.nstr(abs(m['deltaY']) / mp.exp(-2 * mp.pi * m['T']), 8),
                         amplification_A=mp.nstr(abs(m['A']), 6),
                         first_order_rel_diff=mp.nstr(abs(m['first_order'] - m['delta']) / abs(m['delta']), 3),
                         re_im_deltaY=[mp.nstr(m['deltaY'].real, 20), mp.nstr(m['deltaY'].imag, 20)],
                         abs_xi0=mp.nstr(abs(m['xi0']), 6), arg_xi0_over_pi=mp.nstr(mp.arg(m['xi0']) / mp.pi, 6),
                         abs_xi_end=mp.nstr(abs(m['xi_end']), 6), arg_xi_end_over_pi=mp.nstr(mp.arg(m['xi_end']) / mp.pi, 6)))
    info['table_base'] = rows
    Ts = [res[('base', mp.nstr(r, 4))]['T'] for r in radii]
    Ls = [mp.log(abs(res[('base', mp.nstr(r, 4))]['deltaY'])) for r in radii]
    local = []
    for i in range(len(Ts) - 1):
        s = (Ls[i + 1] - Ls[i]) / (Ts[i + 1] - Ts[i])
        local.append(dict(between='%s-%s' % (mp.nstr(radii[i], 4), mp.nstr(radii[i + 1], 4)), slope=mp.nstr(s, 10), A_xi=mp.nstr(-s / 3, 10)))
    info['local_slopes_dlnDelta_dT'] = local
    if len(Ts) >= 6:   # the fits need enough radii; the negative controls use two
        # least squares ln|Delta_Y| = c0 - 3 A T + beta ln T
        M = mp.matrix([[1, -3 * t, mp.log(t)] for t in Ts]); b = mp.matrix(Ls)
        sol = mp.lu_solve(M.T * M, M.T * b)
        resid = max(abs((M * sol)[i] - b[i]) for i in range(len(Ts)))
        info['fit_c0_A_beta'] = dict(c0=mp.nstr(sol[0], 10), A_xi=mp.nstr(sol[1], 12), beta_lnT=mp.nstr(sol[2], 10), max_abs_residual_ln=mp.nstr(resid, 3),
                                     model_A_xi=mp.nstr(2 * mp.pi / 3, 12))
        # fit with A fixed at the model value: ln|Delta_Y| + 2 pi T = c0 + beta ln T
        M2 = mp.matrix([[1, mp.log(t)] for t in Ts]); b2 = mp.matrix([Ls[i] + 2 * mp.pi * Ts[i] for i in range(len(Ts))])
        sol2 = mp.lu_solve(M2.T * M2, M2.T * b2)
        resid2 = max(abs((M2 * sol2)[i] - b2[i]) for i in range(len(Ts)))
        info['fit_A_fixed_2pi_over_3'] = dict(c0=mp.nstr(sol2[0], 10), beta_lnT=mp.nstr(sol2[1], 10), max_abs_residual_ln=mp.nstr(resid2, 3))
        # the same two fits on the smaller half of the radii (larger T)
        half = len(Ts) // 2
        Mh = mp.matrix([[1, -3 * t, mp.log(t)] for t in Ts[half:]]); bh = mp.matrix(Ls[half:])
        solh = mp.lu_solve(Mh.T * Mh, Mh.T * bh)
        info['fit_c0_A_beta_small_radii'] = dict(radii=[mp.nstr(r, 4) for r in radii[half:]], c0=mp.nstr(solh[0], 10), A_xi=mp.nstr(solh[1], 12), beta_lnT=mp.nstr(solh[2], 10))
    else:
        info['fit_c0_A_beta'] = None
    info['finding_jump_nonzero_numerically'] = all(abs(res[('base', mp.nstr(r, 4))]['deltaY']) > mp.mpf(10) ** (-70) for r in radii)
    info['seconds'] = round(time.time() - t_start, 1)
    g = {k: bool(v) for k, v in g.items()}; ok = all(g.values())
    for k in sorted(g):
        print(k, 'PASS' if g[k] else 'FAIL')
    if info['fit_c0_A_beta']:
        print('fit: A_xi =', info['fit_c0_A_beta']['A_xi'], ' (model 2pi/3 =', info['fit_c0_A_beta']['model_A_xi'], '), beta =', info['fit_c0_A_beta']['beta_lnT'])
    print('RESULT', 'PASS' if ok else 'FAIL', '(control %s)' % o.control if o.control else '', '| [NUM] scouting; not a certificate')
    with open(o.out, 'w', encoding='utf-8', newline='\n') as f:
        json.dump({'gates': g, 'info': info, 'all_pass': ok, 'control': o.control, 'quick': o.quick,
                   'configs': configs, 'status': 'NUM scouting; not a certificate; not theorem evidence',
                   'script': 'dyad_open20_an_stage2b_jump_scout.py', 'mpmath': mp.__version__}, f, indent=1, sort_keys=True)
        f.write('\n')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
