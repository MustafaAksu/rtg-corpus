#!/usr/bin/env python3
"""dyad_open20_an_stage2_twosing_fit.py -- two-singularity model fit of the stage-2 coefficients (OPEN 20 analytic branch).

Co-owner review check 3 (24 Oct 2026): replace the single-beta quadratic ratio fit by a two-singularity model and test the
stability of the fitted scale across windows. Everything here is [NUM]; the model is a heuristic ansatz for the large-n
behaviour of c_n = a_{3n+r} (one residue class r at a time):

    one-singularity:  c_n ~ K1 Gamma(n + b1) z1^(-n)
    two-singularity:  c_n ~ K1 Gamma(n + b1) z1^(-n) + K2 Gamma(n + b2) z2^(-n)

with complex z1, z2 (Borel singularity positions in the z-variable Borel plane of the class), complex Gamma shifts b1, b2
and complex amplitudes K1, K2. For given (z, b) the amplitudes are linear: variable projection (complex linear least
squares on the relative residuals r_n = (c_n - model_n)/|c_n|), outer nonlinear least squares (scipy, double precision;
the stored 80-digit coefficients are rounded to double, which is harmless for a fit with relative residuals ~1e-3).
Starting points: z from the design model (±(2 pi i/3)/(-ell)) and from the Borel–Padé strings (17 e^{±...}); b = 0.
For each class and each window [n_lo, n_hi] the script reports the fitted z1, z2 (modulus, arg/pi), b1, b2, |K2/K1|,
the RMS relative residual of the one- and two-singularity models, and the spread of |z1| across windows.
Determinism: fixed starting points and tolerances; results are reproducible to the optimizer's tolerance (~1e-8
relative), not byte-identical across platforms; the JSON rounds to 8 significant digits.
Usage: python -I -B dyad_open20_an_stage2_twosing_fit.py --scout scout_N216_dps840.json --out twosing_fit.json
Exit 0 when every fit converges; 1 otherwise; 3 crash. No gate asserts a scientific outcome.
"""
import os, sys, json, argparse, math, cmath
sys.dont_write_bytecode = True
import numpy as np
from scipy.optimize import least_squares
from scipy.special import loggamma


def model_cols(n, zs, bs):
    cols = []
    n0 = float(np.mean(n))
    for z, b in zip(zs, bs):
        lg = np.array([loggamma(complex(k) + b) - loggamma(complex(n0) + b) for k in n])
        cols.append(np.exp(lg - (n - n0) * np.log(z)))     # normalized at n0 to avoid overflow; K absorbs the constant
    return np.array(cols).T   # shape (len(n), m)


def fit(n, c, z0s, b0s):
    m = len(z0s)
    w = 1.0 / np.abs(c)
    def unpack(p):
        zs = [complex(p[4 * i], p[4 * i + 1]) for i in range(m)]
        bs = [complex(p[4 * i + 2], p[4 * i + 3]) for i in range(m)]
        return zs, bs
    def resid(p):
        zs, bs = unpack(p)
        if any(abs(z) < 1e-3 or abs(z) > 1e3 for z in zs) or any(abs(b) > 200 for b in bs): return np.full(2 * len(n), 1e3)
        A = model_cols(n, zs, bs) * w[:, None]
        rhs = c * w
        if not np.all(np.isfinite(A)): return np.full(2 * len(n), 1e3)
        K, *_ = np.linalg.lstsq(A, rhs, rcond=None)
        r = A @ K - rhs
        return np.concatenate([r.real, r.imag])
    p0 = []
    for z, b in zip(z0s, b0s): p0 += [z.real, z.imag, b.real, b.imag]
    sol = least_squares(resid, p0, method='lm', xtol=1e-12, ftol=1e-12, gtol=1e-12, max_nfev=20000)
    zs, bs = unpack(sol.x)
    A = model_cols(n, zs, bs) * w[:, None]; K, *_ = np.linalg.lstsq(A, c * w, rcond=None)
    r = A @ K - c * w
    rms = float(np.sqrt(np.mean(np.abs(r) ** 2)))
    return zs, bs, K, rms, bool(sol.success), int(sol.nfev)


def c8(x):
    if isinstance(x, complex) or isinstance(x, np.complexfloating): return [float('%.8g' % x.real), float('%.8g' % x.imag)]
    return float('%.8g' % x)


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--scout', default='scout_N216_dps840.json'); ap.add_argument('--out', default='twosing_fit.json')
    o = ap.parse_args()
    S = json.load(open(o.scout, encoding='utf-8'))['info']
    N = S['N']
    C = {int(k): complex(float(v[0]), float(v[1])) for k, v in S['coefficients'].items()}
    ell = complex(float(S['ell'][0]), float(S['ell'][1]))
    z_model = (2j * math.pi / 3) / (-ell)          # design model; the pair is ±z_model
    pade = 17.1 * cmath.exp(1j * math.pi * 0.59), 17.1 * cmath.exp(-1j * math.pi * 0.47)   # Borel–Padé strings, N=216 [34/34]
    windows = [(20, 70), (30, 70), (40, 70), (50, 70), (30, 60), (40, 65)]
    out = {'N': N, 'model_z': c8(z_model), 'abs_model_z': c8(abs(z_model)), 'windows': windows, 'classes': {}}
    allok = True
    for r in (0, 1, 2):
        ks = [k for k in range(2, N + 1) if k % 3 == r]
        ns = np.array([(k - r) // 3 for k in ks], dtype=float); cs = np.array([C[k] for k in ks])
        res_r = {}
        for lo, hi in windows:
            sel = (ns >= lo) & (ns <= hi)
            n, c = ns[sel], cs[sel]
            if len(n) < 12: continue
            entry = {}
            # one singularity, two starts
            best1 = None
            for z0 in (z_model, -z_model, pade[0], pade[1]):
                zs, bs, K, rms, okk, nfev = fit(n, c, [z0], [0j])
                allok &= okk
                if best1 is None or rms < best1[3]: best1 = (zs, bs, K, rms, nfev)
            zs, bs, K, rms, nfev = best1
            entry['one'] = {'abs_z': c8(abs(zs[0])), 'arg_z_over_pi': c8(cmath.phase(zs[0]) / math.pi), 'b': c8(bs[0]), 'rms_rel_residual': c8(rms), 'nfev': nfev}
            # two singularities, several starts
            best2 = None
            for z0s in ((z_model, -z_model), (pade[0], pade[1]), (z_model, pade[1]), (pade[0], -z_model)):
                zs, bs, K, rms, okk, nfev = fit(n, c, list(z0s), [0j, 0j])
                allok &= okk
                if best2 is None or rms < best2[3]: best2 = (zs, bs, K, rms, nfev)
            zs, bs, K, rms, nfev = best2
            order = sorted(range(2), key=lambda i: -abs(K[i]))      # dominant amplitude first (at the window's normalization point n0)
            zs = [zs[i] for i in order]; bs = [bs[i] for i in order]; K = [K[i] for i in order]
            entry['two'] = {'ordering': 'index 1 = larger amplitude at the window centre', 'abs_z1': c8(abs(zs[0])), 'arg_z1_over_pi': c8(cmath.phase(zs[0]) / math.pi), 'b1': c8(bs[0]),
                            'abs_z2': c8(abs(zs[1])), 'arg_z2_over_pi': c8(cmath.phase(zs[1]) / math.pi), 'b2': c8(bs[1]),
                            'abs_K2_over_K1': c8(abs(K[1]) / abs(K[0])) if abs(K[0]) > 0 else None,
                            'arg_z2_minus_arg_z1_over_pi': c8((cmath.phase(zs[1]) - cmath.phase(zs[0])) / math.pi),
                            'rms_rel_residual': c8(rms), 'nfev': nfev}
            res_r['%d-%d' % (lo, hi)] = entry
        vals1 = [e['one']['abs_z'] for e in res_r.values()]; vals2 = [e['two']['abs_z1'] for e in res_r.values()]
        res_r['spread'] = {'one_abs_z_min_max': [min(vals1), max(vals1)], 'two_abs_z1_min_max': [min(vals2), max(vals2)],
                           'two_abs_z2_min_max': [min(e['two']['abs_z2'] for e in res_r.values() if 'two' in e), max(e['two']['abs_z2'] for e in res_r.values() if 'two' in e)]}
        out['classes'][str(r)] = res_r
    out['reading'] = ('heuristic fits; a window-stable |z| with a small residual indicates the scale, a window-dependent one does not; '
                      'no theorem, no certificate; the model form itself is an assumption')
    print('RESULT', 'COMPLETED' if allok else 'FIT NOT CONVERGED')
    for r in ('0', '1', '2'):
        R = out['classes'][r]
        for w, e in R.items():
            if w == 'spread': continue
            print(f"r={r} n={w}: one |z|={e['one']['abs_z']:.4f} arg/pi={e['one']['arg_z_over_pi']:+.4f} b={e['one']['b']} rms={e['one']['rms_rel_residual']:.2e} | "
                  f"two |z1|={e['two']['abs_z1']:.4f} arg/pi={e['two']['arg_z1_over_pi']:+.4f} b1={e['two']['b1']} |z2|={e['two']['abs_z2']:.4f} arg/pi={e['two']['arg_z2_over_pi']:+.4f} "
                  f"b2={e['two']['b2']} |K2/K1|={e['two']['abs_K2_over_K1']} rms={e['two']['rms_rel_residual']:.2e}")
        print(f"r={r} spread: {R['spread']}")
    with open(o.out, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(out, f, indent=1, sort_keys=True, ensure_ascii=False); f.write('\n')
    return 0 if allok else 1


if __name__ == '__main__':
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except Exception as ex:
        import traceback; traceback.print_exc(); print('CRASH', type(ex).__name__, ex); sys.exit(3)
