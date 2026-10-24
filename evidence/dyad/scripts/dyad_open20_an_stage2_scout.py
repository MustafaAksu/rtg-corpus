#!/usr/bin/env python3
"""dyad_open20_an_stage2_scout.py -- OPEN 20 analytic branch, sectorial pilot, stage 2: limited [NUM] scouting.

Authorization: stage-1 J1 closeout review (`J1 CORRECTION VERIFIED — STAGE 1 ACCEPTED`; `STAGE 2 — LIMITED NUM SCOUTING
AUTHORIZED`) and the PI decision of 23 Oct 2026 (continue from commit ae78387, PR #21; stage 3 closed). Everything here
is [NUM]: it is neither a theorem nor a certificate, and it does not establish divergence, convergence, a Stokes
phenomenon, an analytic continuation or a certified radius.

What it computes, for the pilot branch a_pil (Im a > 0) of the smooth formal curve w = phi(z) of F = T^6 tangent to [1:0]:
  1. the coefficients a_2..a_N of phi, solved order by order from the invariance F_w(z, phi(z)) = phi(F_z(z, phi(z))),
     a_k = -R_k / L_k with L_k = ell (k* - k) exact (P1-c; stage-1 gate S2). The six-fold composition of the primitive map
     T(rho, eta) = (rho - sin eta, eta + expm1(rho) - sin eta) is applied to the parametrized curve as one-variable series
     in z, in ball arithmetic (python-flint acb, `--dps` decimal digits). The full map is used (no jet truncation; the
     only truncation is the series length). Balls track rounding only; truncation at N is a separate, non-rigorous choice.
     Ball note: the balls of a_k feed back through W and phi(Z) with cancellation that ball arithmetic cannot see, so the
     recorded radii grow by a factor of about 3.5e3 per order (dependency problem, not a loss of accuracy of the
     midpoints). The working precision therefore has to satisfy roughly dps > 3.6 N + 40; gate C3 enforces that the
     final radii are below 1e-30. A run with too small --dps fails C3 (and, far enough, produces garbage midpoints: the
     signature is coefficients that explode instead of decaying); it is a negative control, not a result.
  2. consistency with stage 1: a_3, a_4 against the exact b_1, b_2 of stage1_prep.json (evaluated at a_pil) [C1, C2]; the
     linear coefficient L_k of a_k in the order-(k+3) residual against ell (k* - k) for k = 3..8 by finite difference [C4];
     F_z = z + O(z^4) on the curve [C0]; the residual of the invariance equation through order N+3 (midpoint and radius
     reported separately; it is small by construction of the recursion and is not an independent check). Beyond a_4 there
     is no exact cross-check in this package.
  3. Borel-scale estimates per residue class r (k = 3n + r), c_n = a_{3n+r}. The design model (D6, level 3 in xi) has two
     singularities of equal modulus at zeta_z = ±(2 pi i/3)/(-ell), so a one-step ratio c_{n+1}/c_n alternates and the
     two-step ratio s_n = c_{n+2}/c_n ~ (n+beta)(n+beta+1)/zeta^2 is fitted instead (quadratic least squares in n on the
     last third of each class): zeta^2 = 1/p2, 2 beta + 1 = p1/p2. Reported: |zeta|, arg zeta mod pi, beta, the raw
     ratios |s_n|/n^2 (which tend to 1/|zeta|^2 under factorial growth and to 0 under geometric growth), and the
     comparison with the model value |zeta_z| = 2 pi/(3 |ell|) and the model direction arg zeta = pi/2 - arg(-ell) mod pi.
     This is a consistency indication, not a proof of Gevrey growth or of the singularity location.
  4. candidate comparison points: xi* on the singular direction arg xi = pi/6 (centre of the overlap S_0 ∩ S_1 of the
     design, D7), |xi*| chosen so that the model jump scale exp(-(2 pi/3)/|xi|^3) equals the target(s); z* = xi*/c. The
     least term of the truncated series at z* is reported beside the model scale. No certified radius exists (E1–E6 not
     done), so none of the points is known to lie in Delta_0 ∩ Delta_1; they are candidates only.
Usage: python -I -B dyad_open20_an_stage2_scout.py --N 72 --dps 330 --stage1 stage1_prep.json --out scout_N72_dps330.json
Runs recorded: (N, dps) = (72, 330), (72, 400), (144, 600), (144, 700), (216, 840); negative control (36, 60) fails C3.
Cross-run comparison and the Borel–Padé singularity scouting: dyad_open20_an_stage2_summary.py.
Exit 0 when the run completes and the gates C0–C4 hold; 1 otherwise; 3 crash. Output JSON is byte-deterministic for
fixed arguments and python-flint version.
"""
import os, sys, json, argparse, math
sys.dont_write_bytecode = True
from flint import acb, acb_poly, arb, ctx


def exp_series(s, n):
    """exp of a series with s[0] = 0, length n (list of acb)"""
    e = [acb(1)] + [acb(0)] * (n - 1)
    for m in range(1, n):
        tot = acb(0)
        for k in range(1, m + 1):
            if k < len(s) and not s[k].is_zero(): tot += s[k] * k * e[m - k]
        e[m] = tot / m
    return e


def sincos_series(s, n):
    I = acb(0, 1)
    ep = exp_series([t * I for t in s], n); em = exp_series([-(t * I) for t in s], n)
    sin = [(ep[k] - em[k]) / (2 * I) for k in range(n)]
    return sin


def expm1_series(s, n):
    e = exp_series(s, n); e[0] = acb(0); return e


def mul(a, b, n):
    pa, pb = acb_poly(a), acb_poly(b)
    c = (pa * pb).coeffs()
    c = list(c) + [acb(0)] * n
    return c[:n]


def T_step(rho, eta, n):
    s = sincos_series(eta, n); x = expm1_series(rho, n)
    return [rho[k] - s[k] for k in range(n)], [eta[k] + x[k] - s[k] for k in range(n)]


def compose_phi(phi, Z, n):
    """phi(Z) with Z = z + z^4 g: sum_m phi^(m)(z)/m! (z^4 g)^m, truncated at length n (coefficient lists).
    Requires Z[0] = Z[2] = Z[3] = 0 and Z[1] = 1 (checked by the caller once)."""
    g = Z[4:] + [acb(0)] * 4          # z^4 g = Z - z
    pert = [acb(0)] * 4 + g[:n - 4]
    pert = pert[:n]
    out = [acb(0)] * n
    dphi = list(phi) + [acb(0)] * n; dphi = dphi[:n]
    pw = [acb(1)] + [acb(0)] * (n - 1)
    fact = acb(1); m = 0
    while True:
        term = mul(dphi, pw, n)
        for k in range(n): out[k] += term[k] / fact
        m += 1
        if 4 * m >= n: break
        fact *= m
        pw = mul(pw, pert, n)
        dphi = [dphi[k + 1] * (k + 1) for k in range(n - 1)] + [acb(0)]
    return out


def fmt(x, d=40):
    """midpoint string with d digits (deterministic), no radius"""
    if isinstance(x, acb):
        return [x.real.mid().str(d, radius=False), x.imag.mid().str(d, radius=False)]
    return x.mid().str(d, radius=False)


def rad_str(x):
    r = x.rad() if isinstance(x, acb) else x.rad()
    return r.str(5, radius=False)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--N', type=int, default=72); ap.add_argument('--dps', type=int, default=330)
    ap.add_argument('--stage1', default='stage1_prep.json'); ap.add_argument('--out', default='scout.json')
    ap.add_argument('--targets', default='1e-10,1e-15,1e-20,1e-30')
    a_ = ap.parse_args()
    ctx.dps = a_.dps
    N = a_.N; n = N + 4
    s3 = arb(3).sqrt(); I = acb(0, 1)
    from fractions import Fraction as Fr
    def Q(p, qq):
        return acb(arb(p.numerator) / p.denominator, (arb(qq.numerator) / qq.denominator) * s3)
    MU = Q(Fr(-1, 2), Fr(-2, 3)); C40 = Q(Fr(-1, 16), Fr(7, 144)); D31 = Q(Fr(1, 3), Fr(-1, 9)); CC = Q(Fr(-61, 2160), Fr(43, 6480))
    A_ = MU.conjugate() - 2 * MU; B_ = D31 - 2 * C40
    KSTAR = Q(Fr(-64, 19), Fr(-16, 19)); ALPHA = Q(Fr(-102, 19), Fr(-16, 19))
    OM = Q(Fr(-1, 2), Fr(1, 2)); OMB = OM.conjugate()
    disc = B_ * B_ - 4 * A_ * CC
    a_pil = (-B_ - disc.sqrt()) / (2 * A_)       # stage-1 S1: this is the root with Im a > 0
    assert a_pil.imag > 0
    ell = C40 + MU * a_pil
    cpil = (-ell).root(3) if hasattr(acb, 'root') else (-ell) ** (acb(1) / 3)   # principal cube root
    assert cpil.real > 0 and cpil.imag > 0
    info = {'N': N, 'dps': a_.dps, 'a_pil': fmt(a_pil), 'ell': fmt(ell), 'c_pil': fmt(cpil), 'abs_ell': fmt(abs(ell)),
            'alpha': fmt(ALPHA), 'k_star': fmt(KSTAR)}
    # ---- stage-1 exact values at a_pil ----
    st1 = json.load(open(a_.stage1))
    def parse_E(sr):  # "(p + q*i*sqrt3) + (p + q*i*sqrt3)*a"  or "(p + q*i*sqrt3)"  or "p"
        import re
        def q3(tok):
            tok = tok.strip().strip('()')
            m = re.match(r'^(-?\d+(?:/\d+)?) \+ (-?\d+(?:/\d+)?)\*i\*sqrt3$', tok)
            if m: return Q(Fr(m.group(1)), Fr(m.group(2)))
            return Q(Fr(tok), Fr(0))
        parts = sr.split(' + (')
        if len(parts) == 1 or '*a' not in sr: return q3(sr)
        e0 = q3(parts[0]); e1 = q3('(' + parts[1].replace('*a', ''))
        return e0 + e1 * a_pil
    b1x = parse_E(st1['info']['S2']['b1=a3']); b2x = parse_E(st1['info']['S2']['b2=a4'])
    # ---- coefficients of phi, order by order ----
    phi = [acb(0), acb(0), a_pil] + [acb(0)] * (n - 3)
    def curve_image(ph, nn):
        # curve (rho, eta)(z) from (z, w) = (z, ph(z)):  z = rho + om eta, w = rho + omb eta
        zser = [acb(0), acb(1)] + [acb(0)] * (nn - 2); wser = ph[:nn] + [acb(0)] * (nn - len(ph))
        den = OM - OMB
        eta = [(zser[k] - wser[k]) / den for k in range(nn)]; rho = [zser[k] - OM * eta[k] for k in range(nn)]
        for _ in range(6): rho, eta = T_step(rho, eta, nn)
        Z = [rho[k] + OM * eta[k] for k in range(nn)]; W = [rho[k] + OMB * eta[k] for k in range(nn)]
        return Z, W
    def residual(ph, nn):
        Z, W = curve_image(ph, nn)
        return [W[k] - t for k, t in enumerate(compose_phi(ph, Z, nn))]      # P1-c convention: F_w(z,phi) - phi(F_z(z,phi))
    # structural check of the composition hypothesis: Z = z + O(z^4) on the curve
    Z0, W0 = curve_image(phi, 8)
    G = {}
    G['C0_Fz_is_z_plus_O_z4'] = bool(Z0[0].contains(acb(0)) and (Z0[1] - 1).contains(acb(0)) and Z0[2].contains(acb(0)) and Z0[3].contains(acb(0))
                                     and abs(Z0[0]).upper() < 1e-20 and abs(Z0[1] - 1).upper() < 1e-20 and abs(Z0[2]).upper() < 1e-20 and abs(Z0[3]).upper() < 1e-20)
    info['Fz_on_curve_z4_coefficient_vs_ell'] = fmt(abs(Z0[4] - ell))
    c4 = []
    for k in range(3, N + 1):
        nn = k + 4
        Lk = ell * (KSTAR - k)
        Rk = residual(phi, nn)[k + 3]
        if k <= 8:   # gate C4: the coefficient of a_k in the order-(k+3) residual equals L_k = ell (k* - k) (P1-c, stage-1 S2), checked by finite difference
            p1 = list(phi); p1[k] = acb(1)
            dev = abs(residual(p1, nn)[k + 3] - Rk - Lk) / abs(Lk)
            c4.append(dev.upper() < 1e-20)
        phi[k] = -Rk / Lk
    G['C4_linear_coefficient_is_L_k_for_k_3_to_8'] = all(c4)
    res_final = residual(phi, n)
    info['residual_through_N+3'] = {'sup_abs_midpoint': fmt(max(abs(acb(t.real.mid(), t.imag.mid())) for t in res_final[:N + 4]), 8),
                                    'sup_radius': rad_str(max(res_final[:N + 4], key=lambda t: t.rad()))}
    # ---- gates ----
    d3 = abs(phi[3] - b1x); d4 = abs(phi[4] - b2x)
    G['C1_a3_matches_stage1'] = bool(d3.upper() < 1e-20); G['C2_a4_matches_stage1'] = bool(d4.upper() < 1e-20)
    maxrad = max(phi[k].rad() for k in range(2, N + 1))
    G['C3_ball_radii_below_1e-30'] = bool(maxrad < 1e-30)
    info['a3_vs_b1_exact'] = fmt(d3, 8); info['a4_vs_b2_exact'] = fmt(d4, 8)
    info['max_ball_radius_a_k'] = maxrad.str(5, radius=False)
    info['coefficients'] = {str(k): fmt(phi[k], 80) for k in range(2, N + 1)}   # 80 digits: enough for the Borel–Padé analysis of the summary script
    info['abs_coefficients'] = {str(k): fmt(abs(phi[k]), 12) for k in range(2, N + 1)}
    info['ball_radius_a_k'] = {str(k): rad_str(phi[k]) for k in range(2, N + 1)}
    # ---- Borel-scale estimates per residue class ----
    classes = {}
    model_abs = (2 * arb.pi() / 3) / abs(ell)
    model_dir = (arb.pi() / 2 - (-ell).arg())
    def mod_pi_over_pi(theta):   # theta/pi reduced to (-1/2, 1/2]
        v = theta / arb.pi(); f = v.mid()
        while f > 0.5: f -= 1
        while f <= -0.5: f += 1
        return f.str(12, radius=False)
    for r in (0, 1, 2):
        ks = [k for k in range(2, N + 1) if k % 3 == r]
        cs = [phi[k] for k in ks]; ns = [(k - r) // 3 for k in ks]
        s2 = [(ns[i], cs[i + 2] / cs[i]) for i in range(len(cs) - 2) if not cs[i].is_zero()]
        one = [(ns[i], cs[i + 1] / cs[i]) for i in range(len(cs) - 1) if not cs[i].is_zero()]
        h = (2 * len(s2)) // 3
        fit = s2[h:]
        m = len(fit)
        # quadratic least squares s_n = p2 n^2 + p1 n + p0 (normal equations, exact integer moments)
        S0 = m; S1 = sum(x for x, _ in fit); S2 = sum(x * x for x, _ in fit); S3 = sum(x ** 3 for x, _ in fit); S4 = sum(x ** 4 for x, _ in fit)
        T0 = sum((y for _, y in fit), acb(0)); T1 = sum((acb(x) * y for x, y in fit), acb(0)); T2 = sum((acb(x * x) * y for x, y in fit), acb(0))
        Mx = [[S4, S3, S2], [S3, S2, S1], [S2, S1, S0]]
        from fractions import Fraction as Fr
        # solve 3x3 by Cramer with exact rational determinant
        def det3(M):
            return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1]) - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
                    + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))
        D = det3(Mx)
        if m >= 3 and D != 0:
            rhs = [T2, T1, T0]
            sol = []
            for col in range(3):
                # replace column col by rhs: expand along that column
                Mc = [[acb(Mx[i][j]) if j != col else rhs[i] for j in range(3)] for i in range(3)]
                def det3c(M):
                    return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1]) - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
                            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))
                sol.append(det3c(Mc) / D)
            p2, p1, p0 = sol
            zeta2 = 1 / p2; zeta = zeta2.sqrt()    # principal root; direction defined mod pi
            beta = (p1 / p2 - 1) / 2
            est = {'n_points_fit': m, 'fit_n_range': [fit[0][0], fit[-1][0]], 'zeta_squared': fmt(zeta2, 20), 'abs_zeta': fmt(abs(zeta), 20),
                   'arg_zeta_over_pi_mod_1': mod_pi_over_pi(zeta.arg()), 'beta_estimate': fmt(beta, 20),
                   'abs_zeta_over_model': fmt(abs(zeta) / model_abs, 12),
                   'arg_minus_model_over_pi_mod_1': mod_pi_over_pi(zeta.arg() - model_dir)}
        else:
            est = {'n_points_fit': m, 'note': 'too few points'}
        est['two_step_ratio_abs_over_n2_last'] = [[x, fmt(abs(y) / (x * x), 10)] for x, y in s2[-6:] if x > 0]
        est['one_step_ratio_last'] = [[x, fmt(y, 12)] for x, y in one[-6:]]
        classes[str(r)] = est
    info['borel'] = {'classes': classes, 'model_abs_zeta_z': fmt(model_abs, 20),
                     'model_formula': 'zeta_z = ±(2 pi i/3)/(-ell): level-3 Borel singularities of the model xi - xi^4 transported to z = xi/c',
                     'model_arg_zeta_over_pi_mod_1': mod_pi_over_pi(model_dir),
                     'reading': 'two-step ratio fit; |zeta| and arg zeta mod pi only; beta is the fitted Gamma shift; indication only'}
    # ---- candidate points ----
    zeta_xi = 2 * arb.pi() / 3                 # model, in xi^3
    cands = []
    for tstr in a_.targets.split(','):
        target = arb(tstr)
        r_xi = (zeta_xi / (-target.log())) ** (arb(1) / 3)     # exp(-zeta_xi / r^3) = target
        xi_star = acb(r_xi * (arb.pi() / 6).cos(), r_xi * (arb.pi() / 6).sin())
        z_star = xi_star / cpil
        terms = [abs(phi[k] * z_star ** k).mid() for k in range(2, N + 1)]
        kmin = min(range(len(terms)), key=lambda i: terms[i]) + 2
        cands.append({'target_model_jump_scale': tstr, 'abs_xi_star': fmt(r_xi, 15), 'xi_star': fmt(xi_star, 15), 'z_star': fmt(z_star, 15),
                      'abs_z_star': fmt(abs(z_star), 15), 'arg_z_star_over_pi': fmt(z_star.arg() / arb.pi(), 15),
                      'least_term_index': kmin, 'least_term_abs': terms[kmin - 2].str(6, radius=False),
                      'least_term_inside_range': bool(kmin < N), 'first_term_abs': terms[0].str(6, radius=False),
                      'model_least_term_index_3n_with_n=|zeta_xi|/|xi|^3': int(round(3 * float((zeta_xi / r_xi ** 3).mid())))})
    info['candidates'] = {'points': cands, 'direction': 'arg xi = pi/6 (centre of the overlap S_0 ∩ S_1, design D7); arg z = pi/6 - arg c',
                          'note': 'candidates only: no certified radius (E1–E6 not done), no membership in Delta_0 ∩ Delta_1 shown, no sum evaluated'}
    ok = all(G.values())
    for k in sorted(G): print(k, 'PASS' if G[k] else 'FAIL')
    print('RESULT', 'COMPLETED' if ok else 'FAIL')
    with open(a_.out, 'w', encoding='utf-8', newline='\n') as f:
        json.dump({'gates': G, 'info': info, 'all_pass': ok, 'script': 'dyad_open20_an_stage2_scout.py', 'args': vars(a_),
                   'status': 'NUM scouting; not a certificate; not theorem evidence'},
                  f, indent=1, sort_keys=True, ensure_ascii=False); f.write('\n')
    return 0 if ok else 1


if __name__ == '__main__':
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except Exception as ex:
        import traceback; traceback.print_exc(); print('CRASH', type(ex).__name__, ex); sys.exit(3)
