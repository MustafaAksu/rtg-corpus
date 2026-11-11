#!/usr/bin/env python3
"""dyad_open20_an_stage3c_w1_check.py -- stage 3c-a, work package W1: development check of the series engine.

DEVELOPMENT RUN.  Not a certificate; no statement about the jump or about divergence is drawn from it.

Gates (exit 0 iff all pass), python-flint balls at --dps digits:
  G0  stage-2 file hash; its all_pass.
  W1a the balls a_2..a_40 from the recursion agree with the 80-digit values recorded by stage 2 to 1e-78
      relative, and every ball radius is below 1e-150.
  W1b Z(x) = F_z(x, phi_40(x)) = x + ell x^4 + ...: the coefficients of x^0, x^2, x^3 contain 0 with radius below
      1e-150, the coefficient of x is 1 and that of x^4 is ell, to the same accuracy.
  W1c the raw defect W - phi_40(Z) has coefficients of x^0..x^43 that contain 0 with radius below 1e-150, and a
      coefficient of x^44 that does not contain 0 (the lifted defect vanishes to order 42 = N + 2 exactly).
  W1d the coefficients of Z and W decay: |Z_k|, |W_k| <= 0.82^k for 100 <= k <= D (reported: the observed roots).
Reported, not gated: sum of |defect_k| X^k for X = 0.9, 1.0, 1.02 (an absolute-value bound; it overestimates the
defect by orders of magnitude near |x| = 1, so the certificate will evaluate the defect by a Taylor shift on boxes).
Control (must exit 1): --control SHIFTCOEF (a_5 changed by 1e-30 relative before the series are formed: W1c fails).
Usage: python3 -I -B dyad_open20_an_stage3c_w1_check.py --stage2 scout_N216_dps840.json --out OUT.json [--D 200] [--dps 400]
"""
import os, sys, json, argparse, hashlib
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from flint import acb, arb, ctx
import dyad_open20_an_stage3c_lib as L

STAGE2_SHA = '6ca8c663061ce2fa9e062938a1e6046c932da4cbddccc6e3e2c3de4df68c477e'
N = 40


def up(v):
    return float(abs(v).upper())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--stage2', required=True); ap.add_argument('--out', required=True)
    ap.add_argument('--D', type=int, default=200); ap.add_argument('--dps', type=int, default=400)
    ap.add_argument('--control', choices=['SHIFTCOEF'])
    o = ap.parse_args()
    ctx.dps = o.dps
    raw = open(o.stage2, 'rb').read(); d2 = json.loads(raw.decode('utf-8'))
    g, info = {}, {}
    g['G0_stage2_input'] = hashlib.sha256(raw).hexdigest() == STAGE2_SHA and d2.get('all_pass') is True
    K = L.Consts(); a = L.coefficients(K, N)
    tiny = 1e-150
    rel = 0.0; rad = 0.0
    for k in range(2, N + 1):
        re, im = d2['info']['coefficients'][str(k)]
        ref = acb(arb(re), arb(im))
        rel = max(rel, up(a[k] - ref) / up(ref)); rad = max(rad, float(a[k].rad()))
    g['W1a_coefficient_balls'] = rel < 1e-78 and rad < tiny
    info['W1a'] = dict(max_relative_difference_to_stage2=rel, max_ball_radius=rad)
    if o.control == 'SHIFTCOEF':
        a[5] = a[5] * (1 + acb(10) ** (-30))
    nn = o.D + 1
    Z, W = L.curve_image(K, a, nn)
    zero = lambda v: bool(v.contains(acb(0))) and float(v.rad()) < tiny
    g['W1b_identity_plus_order_four'] = (zero(Z[0]) and zero(Z[2]) and zero(Z[3]) and up(Z[1] - 1) < tiny and up(Z[4] - K.ell) < tiny)
    res = L.residual(K, a, nn)
    g['W1c_defect_vanishes_to_order_43_raw'] = all(zero(res[k]) for k in range(44)) and not res[44].contains(acb(0))
    info['W1c'] = dict(max_radius_below_44=max(float(res[k].rad()) for k in range(44)), abs_coefficient_44=up(res[44]))
    roots = {k: (round(up(Z[k]) ** (1.0 / k), 4), round(up(W[k]) ** (1.0 / k), 4)) for k in (100, 150, o.D) if k <= o.D}
    g['W1d_coefficients_decay'] = all(up(Z[k]) <= 0.82 ** k and up(W[k]) <= 0.82 ** k for k in range(100, o.D + 1))
    info['W1d_roots_Z_W'] = {str(k): list(v) for k, v in roots.items()}
    info['defect_abs_sums'] = {str(X): float('%.4g' % sum(up(res[k]) * X ** k for k in range(44, nn))) for X in (0.9, 1.0, 1.02)}
    info['parameters'] = dict(N=N, D=o.D, dps=o.dps)
    g = {k: bool(v) for k, v in g.items()}; ok = all(g.values())
    for k in sorted(g):
        print(k, 'PASS' if g[k] else 'FAIL')
    print('RESULT', 'PASS' if ok else 'FAIL', '(control %s)' % o.control if o.control else '', '| development run; not a certificate')
    with open(o.out, 'w', encoding='utf-8', newline='\n') as f:
        json.dump({'gates': g, 'info': info, 'all_pass': ok, 'control': o.control,
                   'status': 'stage 3c-a development run; not a certificate', 'script': 'dyad_open20_an_stage3c_w1_check.py'},
                  f, indent=1, sort_keys=True)
        f.write('\n')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
