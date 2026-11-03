#!/usr/bin/env python3
"""dyad_bridge_note_v1_1_check.py -- exact replay of the claims of the recovered bridge note
`dyad_triad_antisymmetric_bridge_v1_1.md` (Dyadic DYAD-ART-BRIDGE-NOTE), against the note text and the adopted Dyadic DSN.

Inputs: --note (the uploaded file, unchanged) and --dsn (Dyadic DSN at the governing tag, read with `git show`).
All algebra is exact (sympy); series are truncated polynomials, not floating-point fits.

Gates (exit 0 iff all pass):
  G0  SHA-256 of the note equals 5ddebfe4...f4e875 (the hash of the PI upload, commit 47f807c);
      the DSN text contains the DYAD-ART-BRIDGE-NOTE registry line and the DYAD-DEF-PRIMITIVE-MAP map.
  T   each checked claim is printed in the note as checked here (verbatim LaTeX fragments).
  B1  odd-channel identity: Delta_c T = T(x+cv)-T(x-cv) for general K equals
      (2ca - 2cos(eta)sin(cb), 2cb + 2K e^rho sinh(ca) - 2K cos(eta) sin(cb)); only odd powers of c (series to c^7).
  B1k the note's printed Delta_c T_eta (no K) is the K=1 case: equal at K=1, different at K=2 (finding F1, reported).
  B2  det grad T = 1 + K cos(eta)(e^rho - 1); equal to 1 at the origin; not identically 1 (value at (1,0)).
  B3  p=6, K=1 frame: lambda = 1+omega = e^{i pi/3}, linear part of T in W = rho+omega*eta is lambda*W; inverse map;
      v_perp = d(rho,eta)/dc at fixed s; W = i*sqrt3*Z with the DSN's raw Z frame (u = 1/(1-lambda)).
  B4  section 3 series at P1=(0,0), v = v_perp: both components to O(c^5) and Delta_c W' = 2 lambda i c + (7sqrt3/54 + i/2) c^3.
  B5  one-step Birkhoff normal form of T (K=1) in the W frame: nu_3 = 1/8 - i 7sqrt3/72, computed by removing the
      quadratic terms; equals the DSN closed form nu_3(lambda) (Z frame, DSN section 6, L698 of dyad-v6.4.23) divided by cot^2(pi/6)=3.
  B6  mu_6 = 6 conj(lambda) nu_3 = -1/2 - i 2sqrt3/3 = mu (DYAD-THM-C21); tau = 2sqrt3/3.
  B7  bridge lemma: p-fold composition of W -> lambda W + nu |W|^2 W, truncated at cubic order, has cubic coefficient
      p lambda^{p-1} nu = p conj(lambda) nu, for p = 5, 6, 7 (symbolic nu).
  B8  section 5: F(s+ic) - F(s-ic) = 2ic(1 + mu R^2) and its real form 2ic(1 - R^2/2) + 2 tau c R^2.
  B9  section 6: det P_dyad = 1 - R^2 + 19/12 R^4; |1+mu R^2|^2 equals it; det grad F (W -> W + mu|W|^2 W, exact) =
      1 - 2R^2 + 19/4 R^4; the two differ.
  B10 ratio -Im(mu)/(-Re(mu)) = 2 tau = 4sqrt3/3.
  B11 section 7/10: lift W = beta e^{i chi} w gives w' = w + mu beta^2 |w|^2 w (chi cancels); P_Genesis ratio unchanged.

Controls (each must make the run exit 1):
  TAMPER    the note text with every \tfrac{19}{12} replaced by \tfrac{19}{11} (G0 and T_detP fail)
  KFORM     the printed Delta_c T_eta asserted for K=2 (B1k fails)
  NUSIGN    nu_3 with the imaginary sign flipped (B5, B6 fail)
  ZFRAME    the Z-frame nu_3 used in the W-frame lemma without cot^2 (B6 fails: gives 3 mu)
  DETMIX    det grad F asserted equal to det P_dyad (B9 fails)
Usage: python3 -I -B dyad_bridge_note_v1_1_check.py --note NOTE --dsn DSN --out OUT.json [--control NAME]
"""
import sys, json, argparse, hashlib
sys.dont_write_bytecode = True
import sympy as sp

NOTE_SHA = '5ddebfe46b5572761a5154a05712fbcfe4e675f912430ee7d6bfcf0d93f4e875'
I, sqrt3 = sp.I, sp.sqrt(3)


def trunc(expr, vars_, deg):
    """Drop monomials of total degree > deg in vars_."""
    p = sp.Poly(sp.expand(expr), *vars_)
    return sp.expand(sum(c * sp.prod([v ** e for v, e in zip(vars_, m)]) for m, c in p.terms() if sum(m) <= deg))


def series_c(expr, c, n):
    return sp.expand(sp.series(expr, c, 0, n).removeO())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--note', required=True); ap.add_argument('--dsn', required=True)
    ap.add_argument('--out', required=True)
    ap.add_argument('--control', choices=['TAMPER', 'KFORM', 'NUSIGN', 'ZFRAME', 'DETMIX'])
    o = ap.parse_args()
    raw = open(o.note, 'rb').read()
    if o.control == 'TAMPER':
        raw = raw.replace(b'\\tfrac{19}{12}', b'\\tfrac{19}{11}')
    note = raw.decode('utf-8'); dsn = open(o.dsn, encoding='utf-8').read()
    g, info = {}, {}

    # G0
    sha = hashlib.sha256(raw).hexdigest(); info['note_sha256'] = sha
    g['G0_note_hash'] = sha == NOTE_SHA
    g['G0_dsn_registry_line'] = ('[RID: DYAD-ART-BRIDGE-NOTE] :: `dyad_triad_antisymmetric_bridge_v1_1.md`' in dsn)
    g['G0_dsn_primitive_map'] = ('\\rho\' = \\rho - \\sin\\eta, \\qquad \\eta\' = \\eta + (e^\\rho - 1) - \\sin\\eta' in dsn)

    # T: printed claims
    frag = {
        'map': 'T(\\rho,\\eta) = \\bigl(\\rho - \\sin\\eta,\\; \\eta + K(e^\\rho - 1) - K\\sin\\eta\\bigr)',
        'dTrho': '\\Delta_c T_\\rho = 2ca - 2\\cos\\eta\\cdot\\sin(cb)',
        'dTeta': '\\Delta_c T_\\eta = 2cb + 2e^\\rho\\sinh(ca) - 2\\cos\\eta\\cdot\\sin(cb)',
        'jac': '\\det \\nabla T = 1 + K\\cos\\eta\\,(e^\\rho - 1)',
        'vperp': 'v_\\perp = \\left(\\frac{1}{\\sqrt{3}},\\, \\frac{2}{\\sqrt{3}}\\right)',
        's3rho': '\\Delta_c T_\\rho = -\\frac{2}{\\sqrt{3}}c + \\frac{8}{9\\sqrt{3}}c^3 + O(c^5)',
        's3eta': '\\Delta_c T_\\eta = \\frac{2}{\\sqrt{3}}c + \\frac{\\sqrt{3}}{3}c^3 + O(c^5)',
        's3W': '\\Delta_c W\' = 2\\lambda\\,ic + \\left(\\frac{7\\sqrt{3}}{54} + \\frac{i}{2}\\right)c^3 + O(c^5)',
        'nu3': '\\left(\\tfrac{1}{8} - i\\tfrac{7\\sqrt{3}}{72}\\right) = -\\tfrac{1}{2} - i\\tfrac{2\\sqrt{3}}{3}',
        'lemma': '\\mu_p = p\\,\\bar\\lambda\\,\\nu_3^{(1,p)}',
        'detP': '1 - R^2 + \\tfrac{19}{12}R^4',
        'detF': '1 - 2R^2 + \\tfrac{19}{4}R^4',
        'ratio': '\\frac{\\tau}{1/2} = 2\\tau = \\frac{4\\sqrt{3}}{3}',
        'lift': 'w\' = w + \\mu\\beta^2|w|^2 w + O(|w|^5)',
        'frame': 'W = W_\\mathrm{DSN}^{(p=6)} = i\\sqrt{3}\\,Z_\\mathrm{eng}',
        'grade_area': '| Primitive dyad not globally area-preserving | `[ALG]`',
    }
    for k, f in frag.items():
        g['T_' + k] = f in note

    # B1, B1k, B2
    rho, eta, a, b, c, K = sp.symbols('rho eta a b c K', real=True)
    T = lambda r, e, KK: (r - sp.sin(e), e + KK * (sp.exp(r) - 1) - KK * sp.sin(e))
    Tp, Tm = T(rho + c * a, eta + c * b, K), T(rho - c * a, eta - c * b, K)
    d_rho = sp.expand(Tp[0] - Tm[0]); d_eta = sp.expand(Tp[1] - Tm[1])
    gen_rho = 2 * c * a - 2 * sp.cos(eta) * sp.sin(c * b)
    gen_eta = 2 * c * b + 2 * K * sp.exp(rho) * sp.sinh(c * a) - 2 * K * sp.cos(eta) * sp.sin(c * b)
    g['B1_rho'] = sp.simplify(sp.expand_trig(d_rho - gen_rho)) == 0
    g['B1_eta_generalK'] = sp.simplify((d_eta - gen_eta).rewrite(sp.exp).expand()) == 0
    ser = series_c(d_eta, c, 8) + series_c(d_rho, c, 8)
    g['B1_odd_only'] = all(sp.Poly(ser, c).coeff_monomial(c ** k) == 0 for k in (0, 2, 4, 6))
    printed_eta = 2 * c * b + 2 * sp.exp(rho) * sp.sinh(c * a) - 2 * sp.cos(eta) * sp.sin(c * b)
    Kcheck = 2 if o.control == 'KFORM' else 1
    g['B1k_printed_eta_is_K1_form'] = sp.simplify((gen_eta.subs(K, Kcheck) - printed_eta).rewrite(sp.exp).expand()) == 0
    info['F1_printed_eta_differs_at_K2'] = bool(sp.simplify((gen_eta.subs(K, 2) - printed_eta).rewrite(sp.exp).expand()) != 0)
    J = sp.Matrix([[sp.diff(e, v) for v in (rho, eta)] for e in T(rho, eta, K)])
    detJ = sp.simplify(J.det())
    g['B2_det'] = sp.simplify(detJ - (1 + K * sp.cos(eta) * (sp.exp(rho) - 1))) == 0
    g['B2_det_origin_1'] = sp.simplify(detJ.subs({rho: 0, eta: 0})) == 1
    info['det_at_(1,0)'] = str(sp.simplify(detJ.subs({rho: 1, eta: 0})))
    g['B2_not_identically_1'] = sp.simplify(detJ.subs({rho: 1, eta: 0}) - 1) != 0

    # B3 frame (p=6, K=1)
    om = sp.Rational(-1, 2) + I * sqrt3 / 2
    lam = sp.Rational(1, 2) + I * sqrt3 / 2
    g['B3_lambda'] = sp.simplify(1 + om - lam) == 0 and sp.simplify(lam ** 6 - 1) == 0 and sp.simplify(lam ** 3 + 1) == 0
    J1 = J.subs({K: 1, rho: 0, eta: 0})
    lin_W = (J1[0, 0] * rho + J1[0, 1] * eta) + om * (J1[1, 0] * rho + J1[1, 1] * eta)
    g['B3_linear_is_lambdaW'] = sp.simplify(sp.expand(lin_W - lam * (rho + om * eta))) == 0
    s, cc = sp.symbols('s cc', real=True)
    r_inv, e_inv = s + cc / sqrt3, 2 * cc / sqrt3
    Winv = sp.expand(r_inv + om * e_inv)
    g['B3_inverse'] = sp.simplify(sp.re(Winv) - s) == 0 and sp.simplify(sp.im(Winv) - cc) == 0
    vperp = (sp.diff(r_inv, cc), sp.diff(e_inv, cc))
    g['B3_vperp'] = sp.simplify(vperp[0] - 1 / sqrt3) == 0 and sp.simplify(vperp[1] - 2 / sqrt3) == 0
    u = sp.simplify(1 / (1 - lam)); ub = sp.conjugate(u)
    g['B3_frame_bridge_iSqrt3Z'] = sp.simplify(ub + om) == 0 and sp.simplify(u + om - I * sqrt3) == 0
    info['u'] = str(u)

    # B4 section 3
    T1p, T1m = T(c * vperp[0], c * vperp[1], 1), T(-c * vperp[0], -c * vperp[1], 1)
    s3r = series_c(T1p[0] - T1m[0], c, 5); s3e = series_c(T1p[1] - T1m[1], c, 5)
    g['B4_rho'] = sp.simplify(s3r - (-2 / sqrt3 * c + sp.Rational(8, 9) / sqrt3 * c ** 3)) == 0
    g['B4_eta'] = sp.simplify(s3e - (2 / sqrt3 * c + sqrt3 / 3 * c ** 3)) == 0
    s3W = sp.expand(s3r + om * s3e)
    g['B4_W'] = sp.simplify(s3W - (2 * lam * I * c + (7 * sqrt3 / 54 + I / 2) * c ** 3)) == 0

    # B5 one-step BNF in the W frame
    z, zb = sp.symbols('z zb')
    # eta = 2c/sqrt3 with c = (z - zb)/(2i); rho = s + c/sqrt3 with s = (z + zb)/2
    cz = (z - zb) / (2 * I); sz = (z + zb) / 2
    R0, E0 = sz + cz / sqrt3, 2 * cz / sqrt3
    t = sp.symbols('t')
    def taylor3(f):  # Taylor to degree 3 in (z, zb) via scaling
        return sp.expand(sp.series(f.subs({z: t * z, zb: t * zb}), t, 0, 4).removeO().subs(t, 1))
    Tr, Te = T(R0, E0, 1)
    Wp = taylor3(Tr + om * Te)
    P = sp.Poly(Wp, z, zb)
    coef = {m: sp.nsimplify(sp.simplify(cf)) for m, cf in P.terms()}
    g['B5_linear'] = sp.simplify(coef.get((1, 0), 0) - lam) == 0 and sp.simplify(coef.get((0, 1), 0)) == 0
    lamb = sp.conjugate(lam)
    h = {}
    for (j, k) in [(2, 0), (1, 1), (0, 2)]:
        h[(j, k)] = sp.simplify(coef.get((j, k), 0) / (lam ** j * lamb ** k - lam))
    w, wb = sp.symbols('w wb')
    hz = sum(h[m] * w ** m[0] * wb ** m[1] for m in h)
    hzb = sum(sp.conjugate(h[m]) * wb ** m[0] * w ** m[1] for m in h)
    zsub = {z: w + hz, zb: wb + hzb}
    Wp_w = trunc(Wp.subs(zsub, simultaneous=True), (w, wb), 3)
    # w' = z' - h(w', wb'), to cubic order by fixed-point iteration
    zp = Wp_w
    zbp = trunc(sp.conjugate(Wp_w.subs({w: sp.Symbol('W_'), wb: sp.Symbol('Wb_')})).subs(
        {sp.conjugate(sp.Symbol('W_')): wb, sp.conjugate(sp.Symbol('Wb_')): w}), (w, wb), 3)
    wp, wbp = zp, zbp
    for _ in range(3):
        wp_new = trunc(zp - hz.subs({w: wp, wb: wbp}, simultaneous=True), (w, wb), 3)
        wbp_new = trunc(zbp - hzb.subs({w: wp, wb: wbp}, simultaneous=True), (w, wb), 3)
        wp, wbp = wp_new, wbp_new
    PW = sp.Poly(wp, w, wb)
    nu3 = sp.nsimplify(sp.simplify(PW.coeff_monomial(w ** 2 * wb)))
    quad_left = [sp.simplify(PW.coeff_monomial(w ** j * wb ** k)) for (j, k) in [(2, 0), (1, 1), (0, 2)]]
    g['B5_quadratic_removed'] = all(q == 0 for q in quad_left)
    nu3_note = sp.Rational(1, 8) - I * 7 * sqrt3 / 72
    info['nu3_W_computed'] = str(sp.simplify(nu3))
    g['B5_nu3_W'] = sp.simplify(nu3 - nu3_note) == 0
    L = sp.Symbol('L')
    nu3_Z_dsn_expr = -(L ** 5 - L ** 4 - L ** 3 - 2 * L ** 2 + 1) / (2 * (L - 1) * (L + 1) * (L ** 2 + L + 1))
    g['G0_dsn_nu3_closed_form'] = ('\\nu_3(\\lambda)=-\\frac{\\lambda^5-\\lambda^4-\\lambda^3-2\\lambda^2+1}{2(\\lambda-1)(\\lambda+1)(\\lambda^2+\\lambda+1)}' in dsn)
    nu3_Z = sp.simplify(sp.expand_complex(nu3_Z_dsn_expr.subs(L, lam)))
    info['nu3_Z_dsn_at_zeta6'] = str(nu3_Z)
    g['B5_dsn_Z_over_cot2'] = sp.simplify(nu3_Z / 3 - nu3) == 0
    nu_used = nu3_note
    if o.control == 'NUSIGN':
        nu_used = sp.Rational(1, 8) + I * 7 * sqrt3 / 72
        g['B5_nu3_W'] = sp.simplify(nu3 - nu_used) == 0
    if o.control == 'ZFRAME':
        nu_used = nu3_Z

    # B6
    tau = 2 * sqrt3 / 3
    mu = sp.Rational(-1, 2) - I * tau
    mu6 = sp.simplify(sp.expand(6 * lamb * nu_used))
    info['mu6'] = str(mu6)
    g['B6_mu6_equals_mu'] = sp.simplify(sp.expand_complex(mu6 - mu)) == 0
    g['B6_dsn_tau'] = '\\tau=2\\sqrt3/3' in dsn or '\\tau=\\tfrac{2\\sqrt3}{3}' in dsn or '2\\sqrt3/3' in dsn

    # B7 bridge lemma, p = 5, 6, 7 (symbolic nu, lambda a primitive p-th root)
    nu, nub = sp.symbols('nu nub')
    ok7 = True
    for p in (5, 6, 7):
        lp = sp.exp(2 * sp.pi * I / p); lpb = sp.exp(-2 * sp.pi * I / p)
        x, xb = w, wb
        for _ in range(p):
            x, xb = (trunc(lp * x + nu * x ** 2 * xb, (w, wb), 3), trunc(lpb * xb + nub * xb ** 2 * x, (w, wb), 3))
        Px = sp.Poly(x, w, wb)
        lin_ok = sp.simplify(Px.coeff_monomial(w) - 1) == 0
        cub = sp.simplify(Px.coeff_monomial(w ** 2 * wb) - p * lpb * nu)
        others = [sp.simplify(Px.coeff_monomial(w ** j * wb ** k)) for (j, k) in [(3, 0), (1, 2), (0, 3), (0, 1)]]
        ok7 = ok7 and lin_ok and cub == 0 and all(q == 0 for q in others)
    g['B7_bridge_lemma_p567'] = bool(ok7)

    # B8
    R2 = sp.Symbol('R2', positive=True)
    Fpm = lambda W: (1 + mu * R2) * W  # |W_+|^2 = |W_-|^2 = R^2, cubic order
    dF = sp.expand(Fpm(s + I * cc) - Fpm(s - I * cc))
    g['B8_channel'] = sp.simplify(dF - 2 * I * cc * (1 + mu * R2)) == 0
    g['B8_real_form'] = sp.simplify(dF - (2 * I * cc * (1 - R2 / 2) + 2 * tau * cc * R2)) == 0

    # B9
    Pd = sp.Matrix([[1 - R2 / 2, tau * R2], [-tau * R2, 1 - R2 / 2]])
    detP = sp.expand(Pd.det())
    g['B9_detP'] = sp.simplify(detP - (1 - R2 + sp.Rational(19, 12) * R2 ** 2)) == 0
    g['B9_modulus'] = sp.simplify(sp.expand(sp.Abs(1 + mu * R2) ** 2) - detP) == 0
    X, Y = sp.symbols('X Y', real=True)
    Wc = X + I * Y
    FW = sp.expand(Wc + mu * (X ** 2 + Y ** 2) * Wc)
    JF = sp.Matrix([[sp.diff(sp.re(FW), v) for v in (X, Y)], [sp.diff(sp.im(FW), v) for v in (X, Y)]])
    detF = sp.expand(sp.simplify(JF.det()).subs(Y, 0).subs(X, sp.sqrt(R2)))
    detF_full = sp.simplify(JF.det() - (1 - 2 * (X ** 2 + Y ** 2) + sp.Rational(19, 4) * (X ** 2 + Y ** 2) ** 2))
    g['B9_detF_exact'] = detF_full == 0
    if o.control == 'DETMIX':
        g['B9_detF_exact'] = sp.simplify(detF - detP) == 0
    g['B9_differ'] = sp.simplify(detF - detP) != 0
    info['detF'] = str(detF)

    # B10, B11
    g['B10_ratio'] = sp.simplify((-sp.im(mu)) / (-sp.re(mu)) - 4 * sqrt3 / 3) == 0
    beta, chi = sp.symbols('beta chi', positive=True)
    wr, wi = sp.symbols('wr wi', real=True)
    wv = wr + I * wi; gam = beta * sp.exp(I * chi)
    lhs = sp.expand((gam * wv + mu * sp.Abs(gam * wv) ** 2 * gam * wv) / gam)
    g['B11_chi_cancels'] = sp.simplify(lhs - (wv + mu * beta ** 2 * (wr ** 2 + wi ** 2) * wv)) == 0
    PG = Pd.subs(R2, beta ** 2 * R2)
    g['B11_ratio_preserved'] = sp.simplify(PG[0, 1] / (1 - PG[0, 0]) - 2 * tau) == 0

    g = {k: bool(v) for k, v in g.items()}
    ok = all(g.values())
    for k in sorted(g):
        print(k, 'PASS' if g[k] else 'FAIL')
    print('RESULT', 'PASS' if ok else 'FAIL', '(control %s)' % o.control if o.control else '')
    with open(o.out, 'w', encoding='utf-8', newline='\n') as f:
        json.dump({'gates': g, 'info': info, 'all_pass': ok, 'control': o.control,
                   'script': 'dyad_bridge_note_v1_1_check.py', 'sympy': sp.__version__}, f, indent=1, sort_keys=True)
        f.write('\n')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
