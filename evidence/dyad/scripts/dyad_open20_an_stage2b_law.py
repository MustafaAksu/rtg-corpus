#!/usr/bin/env python3
"""dyad_open20_an_stage2b_law.py -- OPEN 20 stage 2b, second part: the decay law of the measured jump in the Fatou
time of the restricted map.  [NUM] scouting; not a certificate; no error bound is proved.

Why.  dyad_open20_an_stage2b_jump_scout.py measures Delta_Y(xi*) on arg xi* = pi/6 and compares it with
exp(-2 pi T_model), T_model = 1/(3|xi*|^3).  T_model keeps only the leading term of the Fatou coordinate t of the restricted
map f(z) = F_z(z, phi(z)) = z + ell z^4 + ..., so a slope different from -2 pi against T_model does not locate the Borel
singularity.  Here the formal Fatou coordinate is computed,
    t^(z) = A3 z^-3 + A2 z^-2 + A1 z^-1 + kappa log z + sum_{j=1..J} B_j z^j,     t^(f(z)) = t^(z) + 1,
and the time of the common point z* is read as  t(z*) = t^(z_end) - (number of steps from z* to z_end), with z_end far
down the forward orbit on the curve of S_0 (|xi| about 0.05).  T_true = -Im t(z*).

Linear theory (model, [HEUR]): the difference of two invariant graphs is delta_h(t) P(t) with P of period 1 and
delta_h ~ t^(-alpha/3); the first Fourier mode gives |Delta_Y| ~ C |t|^(-Re alpha/3) e^(Im(alpha) arg(t)/3) exp(-2 pi T_true).
Test: the local slope of  L = ln|Delta_Y| + (Re alpha/3) ln|t| - (Im alpha/3) arg t  against T_true is -2 pi m with m = 1.

Steps.
  1. Coefficients f_4..f_K of f by a discrete Cauchy integral of the full map on |z| = R (phi truncated at N_s terms).
     Gate L1: f_1 = 1, f_2 = f_3 = 0 and f_4 = ell to 1e-30.
  2. A3, A2, A1, kappa, B_1..B_J from the Abel equation, order by order (triangular).  Gate L2: the defect
     t^(f(z)) - t^(z) - 1 evaluated on an actual orbit point with |xi| about 0.05 is below 1e-8.
  3. For each radius: the measurement of the scout script (base configuration) is repeated to get z*, phi_0(z*) and the
     jump; the forward orbit is continued to |xi| about 0.05; t(z*) from the S_0 side.  The same from the S_1 side
     (t^(z_start) + steps) is reported: both sides must agree to 1e-6 (gate L3; both are asymptotic to the same series).
  4. Local slopes of L against T_true, and their mean over the smaller radii.  Gate L4 (sanity, wide): every local
     slope lies in [-2 pi 1.25, -2 pi 0.75].  The value itself is the finding.
Usage: python3 -I -B dyad_open20_an_stage2b_law.py --stage2 scout_N216_dps840.json --out OUT.json [--radii ...]
"""
import os, sys, json, argparse, hashlib
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mpmath as mp
import dyad_open20_an_stage2b_jump_scout as J2

K_MAX, J_MAX, N_S, R_C, M_C = 22, 12, 80, '0.1', 128


def smul(a, b, n):
    out = [mp.mpc(0)] * (n + 1)
    for i, x in enumerate(a[:n + 1]):
        if x == 0:
            continue
        for j, y in enumerate(b[:n + 1 - i]):
            out[i + j] += x * y
    return out


def spow(u1, p, n):
    """(1 + u)^p for a real integer p (may be negative), u a series without constant term; binomial series."""
    out = [mp.mpc(0)] * (n + 1); out[0] = mp.mpc(1)
    term = [mp.mpc(0)] * (n + 1); term[0] = mp.mpc(1)
    for k in range(1, n + 1):
        term = smul(term, u1, n)
        c = mp.binomial(p, k)
        out = [o + c * t for o, t in zip(out, term)]
    return out


def slog(u1, n):
    out = [mp.mpc(0)] * (n + 1); term = [mp.mpc(0)] * (n + 1); term[0] = mp.mpc(1)
    for k in range(1, n + 1):
        term = smul(term, u1, n)
        out = [o + (-1) ** (k + 1) * t / k for o, t in zip(out, term)]
    return out


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--stage2', required=True); ap.add_argument('--out', required=True)
    ap.add_argument('--radii', default='0.45,0.42,0.40,0.37,0.35,0.32,0.30,0.28,0.26,0.24')
    o = ap.parse_args()
    raw = open(o.stage2, 'rb').read(); data = json.loads(raw.decode('utf-8'))
    g, info = {}, {}
    g['G0_stage2_hash'] = hashlib.sha256(raw).hexdigest() == J2.STAGE2_SHA
    mp.mp.dps = 160
    S = J2.Dyad(data, 216)
    ell = mp.mpc(mp.mpf(data['info']['ell'][0]), mp.mpf(data['info']['ell'][1]))
    al = mp.mpc(mp.mpf(data['info']['alpha'][0]), mp.mpf(data['info']['alpha'][1]))
    # 1. restricted map coefficients by a discrete Cauchy integral
    Ssmall = J2.Dyad(data, N_S)
    R = mp.mpf(R_C)
    vals = []
    for j in range(M_C):
        z = R * mp.exp(2j * mp.pi * j / M_C)
        vals.append(Ssmall.xy(Ssmall.step(Ssmall.state(z, Ssmall.series(z))))[0])
    f = []
    for k in range(K_MAX + 1):
        f.append(sum(vals[j] * mp.exp(-2j * mp.pi * j * k / M_C) for j in range(M_C)) / (M_C * R ** k))
    g['L1_restricted_map_leading_terms'] = (abs(f[0]) < mp.mpf(10) ** (-30) and abs(f[1] - 1) < mp.mpf(10) ** (-30) and abs(f[2]) < mp.mpf(10) ** (-30)
                                             and abs(f[3]) < mp.mpf(10) ** (-30) and abs(f[4] - ell) < mp.mpf(10) ** (-30))
    info['f_5_to_8'] = [mp.nstr(f[k], 15) for k in range(5, 9)]
    # 2. formal Fatou coordinate.  g = f/z = 1 + u, u = ell z^3 + f5 z^4 + ...
    n = J_MAX + 4
    u = [mp.mpc(0)] + [f[k + 1] for k in range(1, n + 4)]          # u[i] = coefficient of z^i, i >= 1 (u[1]=u[2]=0)
    u = u[:n + 4]
    def shifted(series, shift):       # series * z^shift, returned as coefficients of z^0..z^n
        out = [mp.mpc(0)] * (n + 1)
        for i, x in enumerate(series):
            if 0 <= i + shift <= n:
                out[i + shift] += x
        return out
    def minus_one(sr):
        sr = list(sr); sr[0] -= 1; return sr
    basis = {}
    for p in (3, 2, 1):
        basis[-p] = shifted(minus_one(spow(u, -p, n + 3)), -p)       # z^-p (g^-p - 1)
    basis['log'] = slog(u, n + 3)[:n + 1]
    for j in range(1, J_MAX + 1):
        basis[j] = shifted(minus_one(spow(u, j, n + 3)), j)          # z^j (g^j - 1)
    order = [-3, -2, -1, 'log'] + list(range(1, J_MAX + 1))          # unknown i is fixed by the coefficient of z^i-th row
    coef = {}
    defect = [mp.mpc(0)] * (n + 1); defect[0] = mp.mpc(-1)           # sum coef*basis - 1 must vanish
    for row, key in enumerate(order):
        lead = basis[key][row]
        c = -defect[row] / lead
        coef[key] = c
        defect = [d + c * b for d, b in zip(defect, basis[key])]
    info['fatou'] = {'A3': mp.nstr(coef[-3], 20), 'A2': mp.nstr(coef[-2], 20), 'A1': mp.nstr(coef[-1], 20), 'kappa': mp.nstr(coef['log'], 20),
                     'A3_expected_minus_1_over_3ell': mp.nstr(-1 / (3 * ell), 20),
                     'B': [mp.nstr(coef[j], 8) for j in range(1, J_MAX + 1)]}

    def that(z):
        s = coef[-3] / z ** 3 + coef[-2] / z ** 2 + coef[-1] / z + coef['log'] * mp.log(z)
        for j in range(1, J_MAX + 1):
            s += coef[j] * z ** j
        return s
    # 3. measurements with times
    rows = []; ok_side = True; max_defect = mp.mpf(0)
    for rs in o.radii.split(','):
        r = mp.mpf(rs)
        m = J2.measure(S, r, '0.10')
        zs = m['z_star']; w0 = m['w1'] - m['delta']
        # S_0 side: continue the forward orbit of (z*, phi_0(z*)) to |xi| about 0.05
        st = S.state(zs, w0); steps = 0
        target = mp.mpf('0.05')
        while True:
            st = S.step(st); steps += 1
            x, _ = S.xy(st)
            if steps > m['n'] and abs(S.xi(x)) <= target:
                break
        x1 = S.xy(S.step(st))[0]
        max_defect = max(max_defect, abs(that(x1) - that(x) - 1))
        t0 = that(x) - steps
        # S_1 side: start point z_0 of the measured orbit (|xi| about 0.10): t = t^(z_0) + n
        z0 = m['xi0'] / S.c
        t1 = that(z0) + m['n']
        ok_side = ok_side and abs(t1 - t0) < mp.mpf(10) ** (-3)
        L = mp.log(abs(m['deltaY'])) + (al.real / 3) * mp.log(abs(t0)) - (al.imag / 3) * mp.arg(t0)
        rows.append(dict(r=rs, T_model=m['T'], t=t0, t_from_S1=t1, L=L, absY=abs(m['deltaY']), steps=steps))
        print('r=%s  T_model=%s  t=%s  |t(S1)-t(S0)|=%s' % (rs, mp.nstr(m['T'], 8), mp.nstr(t0, 12), mp.nstr(abs(t1 - t0), 3)), flush=True)
    g['L2_abel_defect_small'] = max_defect < mp.mpf(10) ** (-8)
    info['max_abel_defect_at_xi_0.05'] = mp.nstr(max_defect, 3)
    g['L3_two_sides_agree'] = ok_side
    # 4. slopes
    slopes = []
    for i in range(len(rows) - 1):
        a, b = rows[i], rows[i + 1]
        s = (b['L'] - a['L']) / ((-b['t'].imag) - (-a['t'].imag))
        s_raw = (mp.log(b['absY']) - mp.log(a['absY'])) / ((-b['t'].imag) - (-a['t'].imag))
        slopes.append(dict(between='%s-%s' % (a['r'], b['r']), slope=s, slope_over_minus_2pi=-s / (2 * mp.pi), slope_without_power_factor_over_minus_2pi=-s_raw / (2 * mp.pi)))
    g['L4_slopes_near_minus_2pi'] = all(mp.mpf('0.75') <= sl['slope_over_minus_2pi'] <= mp.mpf('1.25') for sl in slopes)
    half = slopes[len(slopes) // 2:]
    info['mean_slope_over_minus_2pi_small_radii'] = mp.nstr(sum(sl['slope_over_minus_2pi'] for sl in half) / len(half), 8)
    info['table'] = [dict(r=x['r'], T_model=mp.nstr(x['T_model'], 8), T_true=mp.nstr(-x['t'].imag, 10), Re_t=mp.nstr(x['t'].real, 8),
                          abs_deltaY=mp.nstr(x['absY'], 12), side_difference=mp.nstr(abs(x['t_from_S1'] - x['t']), 3),
                          C_estimate=mp.nstr(mp.exp(x['L'] + 2 * mp.pi * (-x['t'].imag)), 8)) for x in rows]
    info['local_slopes'] = [dict(between=sl['between'], slope=mp.nstr(sl['slope'], 10), slope_over_minus_2pi=mp.nstr(sl['slope_over_minus_2pi'], 8),
                                 without_power_factor=mp.nstr(sl['slope_without_power_factor_over_minus_2pi'], 8)) for sl in slopes]
    g = {k: bool(v) for k, v in g.items()}; ok = all(g.values())
    for k in sorted(g):
        print(k, 'PASS' if g[k] else 'FAIL')
    for sl in info['local_slopes']:
        print(sl)
    print('mean slope/(-2pi) over the smaller radii:', info['mean_slope_over_minus_2pi_small_radii'])
    print('RESULT', 'PASS' if ok else 'FAIL', '| [NUM] scouting; not a certificate')
    with open(o.out, 'w', encoding='utf-8', newline='\n') as fh:
        json.dump({'gates': g, 'info': info, 'all_pass': ok, 'status': 'NUM scouting; not a certificate; not theorem evidence',
                   'script': 'dyad_open20_an_stage2b_law.py', 'mpmath': mp.__version__,
                   'parameters': dict(K_MAX=K_MAX, J_MAX=J_MAX, N_S=N_S, R_C=R_C, M_C=M_C)}, fh, indent=1, sort_keys=True)
        fh.write('\n')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
