# spiral_phase_fit.py
#
# OPEN 3 / OPEN 5 / c_theta joint fitting pipeline.
#
# Fits (m, Q, Theta) block data to:
#   Q_m  ~= C / (m+kappa) + A * m^{-3/2} * cos(tau*log(m) + phi)
#   DTheta_m ~= -tau*Q_m + c_theta*Q_m^2 + B*m^{-3/2}*cos(tau*log(m) + phi_theta)
#
# IMPORTANT NOTES:
#
# 1. Signal-to-noise: c_theta*Q^2 ~ Q^2, spiral oscillation ~ Q^{3/2}.
#    The ratio is O(sqrt(Q)) -> 0 along the orbit.
#    This means c_theta extraction needs very late windows (Q << 1)
#    AND many blocks to average down the spiral.
#    Recommended: use m-min > 10^5 blocks, window > 10^4 blocks.
#
# 2. Grid search vs gradient: the kappa and phi grids can be coarse initially.
#    Once a good kappa is found from the Q-fit, refine with a finer grid.
#
# 3. Phase unwrapping: Theta is computed by atan2 and wraps. The CSV generator
#    writes raw atan2 values; this script unwraps heuristically. Check the
#    unwrapped phase plot if results look wrong.
#
# 4. Window sensitivity: always report c_theta for at least two different
#    m-windows to check stability. A drifting c_theta indicates the spiral
#    model is not yet a good fit and more blocks are needed.
#
# 5. The grid is O(N * kappa_steps * phi_steps) operations. For 10^5 data
#    points and 400*360 grid, this is ~1.4e10 operations -- use dps=30 for
#    the grid search, then refine at dps=80 around the best point.

from __future__ import annotations
import argparse, csv, json, math, sys
import mpmath as mp

# ── Configurable precision ────────────────────────────────────────────────────
GRID_DPS    = 30   # fast grid search
REFINE_DPS  = 80   # final refinement

def set_dps(d): mp.mp.dps = d

# ── Utilities ─────────────────────────────────────────────────────────────────
def wrap_to_pi(x):
    x = float(x)
    while x <= -math.pi: x += 2*math.pi
    while x >   math.pi: x -= 2*math.pi
    return x

def unwrap_phase(theta_list):
    if not theta_list: return []
    out = [float(theta_list[0])]
    for t in theta_list[1:]:
        dt = wrap_to_pi(float(t) - out[-1])
        out.append(out[-1] + dt)
    return out

def read_csv(path):
    ms, qs, ths = [], [], []
    with open(path, 'r', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            ms.append(int(row['m']))
            qs.append(float(row['Q']))
            ths.append(float(row['Theta']))
    return ms, qs, ths

def rms(resid):
    if not resid: return float('nan')
    return math.sqrt(sum(r*r for r in resid)/len(resid))

def linfit_1d(xs, ys):
    """y = a*x, return a."""
    num = sum(x*y for x,y in zip(xs,ys))
    den = sum(x*x for x in xs)
    return num/den if abs(den) > 1e-100 else 0.0

def linfit_2d(X1, X2, Y):
    """Y = a*X1 + b*X2, return (a,b) via normal equations."""
    n = len(Y)
    s11 = sum(x*x for x in X1); s12 = sum(x*y for x,y in zip(X1,X2))
    s22 = sum(x*x for x in X2); s1y = sum(x*y for x,y in zip(X1,Y))
    s2y = sum(x*y for x,y in zip(X2,Y))
    D = s11*s22 - s12**2
    if abs(D) < 1e-100: return 0.0, 0.0
    return (s1y*s22 - s2y*s12)/D, (s11*s2y - s12*s1y)/D

# ── Q-skeleton fit ─────────────────────────────────────────────────────────────
def fit_q_skeleton(ms, qs, C, tau, kappa_grid, phi_grid):
    """
    Fit Q_m = C/(m+kappa) + A*m^{-3/2}*cos(tau*log(m)+phi).
    Grid over kappa and phi, linear solve for A.
    Returns best dict.
    """
    best = None
    best_score = float('inf')
    C = float(C); tau = float(tau)
    for kappa in kappa_grid:
        base = [qs[i] - C/(ms[i]+kappa) for i in range(len(ms))]
        for phi in phi_grid:
            col = [ms[i]**(-1.5)*math.cos(tau*math.log(ms[i])+phi) for i in range(len(ms))]
            A = linfit_1d(col, base)
            resid = [base[i] - A*col[i] for i in range(len(ms))]
            score = rms(resid)
            if score < best_score:
                best_score = score
                best = {'kappa': kappa, 'A': A, 'phi': phi, 'score': score}
    return best

# ── Phase increment fit ────────────────────────────────────────────────────────
def fit_phase(ms, q_model_vals, ths_unwrapped, tau, phi_theta_grid):
    """
    Fit DTheta_m = -tau*Q + c_theta*Q^2 + B*m^{-3/2}*cos(tau*log(m)+phi_theta).
    Grid over phi_theta, linear solve for (c_theta, B).
    Returns best dict.
    """
    tau = float(tau)
    dth = [ths_unwrapped[i+1]-ths_unwrapped[i] for i in range(len(ths_unwrapped)-1)]
    ms_mid = ms[:-1]
    qm = q_model_vals[:-1]
    # RHS: dth + tau*Q
    rhs = [dth[i] + tau*qm[i] for i in range(len(dth))]

    best = None
    best_score = float('inf')
    for phi_theta in phi_theta_grid:
        X1 = [qm[i]**2 for i in range(len(dth))]
        X2 = [ms_mid[i]**(-1.5)*math.cos(tau*math.log(ms_mid[i])+phi_theta) for i in range(len(dth))]
        c_theta, B = linfit_2d(X1, X2, rhs)
        resid = [rhs[i] - c_theta*X1[i] - B*X2[i] for i in range(len(dth))]
        score = rms(resid)
        if score < best_score:
            best_score = score
            best = {'c_theta': c_theta, 'B': B, 'phi_theta': phi_theta, 'score': score}
    return best

# ── Main ───────────────────────────────────────────────────────────────────────
def main():
    pa = argparse.ArgumentParser(description='Spiral Q+phase joint fit for RTG block data.')
    pa.add_argument('--input',        required=True)
    pa.add_argument('--p',            type=int, required=True, choices=[5,6])
    pa.add_argument('--m-min',        type=int, default=None)
    pa.add_argument('--m-max',        type=int, default=None)
    pa.add_argument('--tau',          type=float, default=None)
    pa.add_argument('--C',            type=float, default=None)
    pa.add_argument('--kappa-min',    type=float, default=-10.0)
    pa.add_argument('--kappa-max',    type=float, default=10.0)
    pa.add_argument('--kappa-steps',  type=int, default=201)
    pa.add_argument('--phi-steps',    type=int, default=181)
    pa.add_argument('--json-out',     default=None)
    pa.add_argument('--window-check', action='store_true',
                    help='Repeat fit on two sub-windows to check c_theta stability')
    args = pa.parse_args()

    sqrt3 = math.sqrt(3); sqrt5 = math.sqrt(5); s5 = math.sqrt(10+2*sqrt5)
    if args.p == 6:
        tau_default = 2*sqrt3/3
        C_default   = 6.0
    else:
        tau_default = (115-50*sqrt5)*s5/8
        C_default   = (7+3*sqrt5)/5   # [ALG] from DSN

    tau = args.tau if args.tau is not None else tau_default
    C   = args.C   if args.C   is not None else C_default

    ms, qs, ths = read_csv(args.input)
    ths_uw = unwrap_phase(ths)

    # Window filter
    rows = [(ms[i],qs[i],ths_uw[i]) for i in range(len(ms))
            if (args.m_min is None or ms[i]>=args.m_min)
            and (args.m_max is None or ms[i]<=args.m_max)]
    if len(rows) < 50:
        print(f"ERROR: only {len(rows)} rows in window. Use wider m-range or more blocks.")
        sys.exit(1)
    ms   = [r[0] for r in rows]
    qs   = [r[1] for r in rows]
    ths_uw = [r[2] for r in rows]

    print('SPIRAL PHASE-FIT  (OPEN 3 / OPEN 5 / c_theta)')
    print(f'  p={args.p},  N={len(ms)},  m-range=[{ms[0]},{ms[-1]}]')
    print(f'  tau={tau:.10f},  C={C:.10f}')
    print(f'  Q range: [{min(qs):.3e}, {max(qs):.3e}]')
    print()

    # Auto-detect kappa range from data (C/Q_mid - m_mid is a rough estimate)
    q_mid = qs[len(qs)//2]; m_mid = ms[len(ms)//2]
    kappa_center = C/q_mid - m_mid
    kappa_halfwidth = max(abs(args.kappa_max - args.kappa_min)/2, abs(kappa_center)*0.1 + 100)
    kappa_lo = kappa_center - kappa_halfwidth
    kappa_hi = kappa_center + kappa_halfwidth
    print(f'  Auto kappa range: [{kappa_lo:.1f}, {kappa_hi:.1f}]  (center={kappa_center:.1f})')
    # Grids
    kstep = (kappa_hi - kappa_lo)/max(1, args.kappa_steps-1)
    kappa_grid = [kappa_lo + kstep*i for i in range(args.kappa_steps)]
    phi_grid   = [-math.pi + 2*math.pi*i/max(1,args.phi_steps-1) for i in range(args.phi_steps)]

    # ── Q-fit ──────────────────────────────────────────────────────────────────
    print('[1] Fitting Q-skeleton...')
    qfit = fit_q_skeleton(ms, qs, C, tau, kappa_grid, phi_grid)
    print(f'    kappa = {qfit["kappa"]:.6f}')
    print(f'    A     = {qfit["A"]:.6e}')
    print(f'    phi   = {qfit["phi"]:.6f}')
    print(f'    rms   = {qfit["score"]:.3e}')
    print(f'    (smaller rms = better Q-skeleton fit)')

    # Build Q model values
    kappa = qfit['kappa']; A = qfit['A']; phi = qfit['phi']
    q_model_vals = [C/(ms[i]+kappa) + A*ms[i]**(-1.5)*math.cos(tau*math.log(ms[i])+phi)
                    for i in range(len(ms))]

    # ── Phase-fit ──────────────────────────────────────────────────────────────
    print('\n[2] Fitting phase increments...')
    phifit = fit_phase(ms, q_model_vals, ths_uw, tau, phi_grid)
    c_theta = phifit['c_theta']
    print(f'    c_theta    = {c_theta:.8f}')
    print(f'    B          = {phifit["B"]:.6e}')
    print(f'    phi_theta  = {phifit["phi_theta"]:.6f}')
    print(f'    rms        = {phifit["score"]:.3e}')

    # ── Reference values ──────────────────────────────────────────────────────
    print()
    if args.p == 6:
        c_theta_cand = -119*sqrt3/648
        print(f'    Reference c_theta^(6) [ALG candidate] = {c_theta_cand:.8f}')
        print(f'    Discrepancy = {abs(c_theta-c_theta_cand):.2e}')
    else:
        # c_theta^(5) from raw 5-step Im(c32) - tau5/2
        c32_raw5_im = 0.62348454330987151741
        c_theta_cand = c32_raw5_im - tau/2
        print(f'    Reference c_theta^(5) [ALG candidate] = {c_theta_cand:.8f}')
        print(f'    Discrepancy = {abs(c_theta-c_theta_cand):.2e}')

    # ── Window stability check ────────────────────────────────────────────────
    if args.window_check and len(ms) >= 200:
        print('\n[3] Window stability check (split into two halves)...')
        half = len(ms)//2
        for name, sl in [('first half', slice(None,half)), ('second half', slice(half,None))]:
            ms2 = ms[sl]; qs2 = qs[sl]; th2 = ths_uw[sl]
            qf2 = fit_q_skeleton(ms2, qs2, C, tau, kappa_grid, phi_grid)
            qm2 = [C/(ms2[i]+qf2['kappa']) + qf2['A']*ms2[i]**(-1.5)
                   *math.cos(tau*math.log(ms2[i])+qf2['phi']) for i in range(len(ms2))]
            pf2 = fit_phase(ms2, qm2, list(th2), tau, phi_grid)
            print(f'    {name}: c_theta = {pf2["c_theta"]:.8f}  rms={pf2["score"]:.2e}')
        print('    (stable c_theta across windows = reliable result)')

    # ── JSON output ────────────────────────────────────────────────────────────
    if args.json_out:
        out = {
            'p': args.p, 'N': len(ms),
            'm_min': ms[0], 'm_max': ms[-1],
            'tau': tau, 'C': C,
            'Q_fit': {'kappa': qfit['kappa'], 'A': qfit['A'],
                      'phi': qfit['phi'], 'rms': qfit['score']},
            'phase_fit': {'c_theta': c_theta, 'B': phifit['B'],
                          'phi_theta': phifit['phi_theta'], 'rms': phifit['score']},
        }
        with open(args.json_out, 'w', encoding='utf-8') as f:
            json.dump(out, f, indent=2)
        print(f'\nWrote report to {args.json_out}')

    print()
    print('WORKFLOW FOR DSN PROMOTION:')
    print('  1. Run generate_block_csv.py with --blocks 5000000 --dps 120')
    print('  2. Run this script with --m-min [late window] --window-check')
    print('  3. If c_theta is stable across windows: [NUM strong]')
    print('  4. Compare to ALG candidate; discrepancy < 0.001 => confirm')

if __name__ == '__main__':
    main()