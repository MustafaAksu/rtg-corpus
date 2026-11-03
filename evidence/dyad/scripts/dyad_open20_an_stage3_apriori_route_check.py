#!/usr/bin/env python3
"""dyad_open20_an_stage3_apriori_route_check.py -- OPEN 20 analytic branch, sectorial pilot: can the a-priori
constants of LH2012 Theorems 3.1/4.2, written out by LIT (INF-009, INF-010 at rtg-lit 564a1ee), close E3-E5 at a
radius where the sectorial jump is resolvable?

Design: records/dyad/DYAD_OPEN20_AN_SECTORIAL_PILOT_DESIGN.md section 8.  This is a design calculation on recorded
stage-1 data. It evaluates no new map value: the only DYAD inputs are the exact normalized-jet coefficients of
evidence/dyad/open20-an/stage1_prep.json (stage 1, OWNER-RUN, 23 Oct 2026) and the stage-2 Borel-scale range.

Argument.
  INF-010 needs Cauchy constants K1..K4, Psi with |R1| <= K1|x|^4|y| + K2|x|^5, |R2| <= K3|x|^3|y|^2 + K4|x|^4|y|,
  |psi| <= Psi on a polydisc.  Letting y -> 0 and then x -> 0 in these bounds shows that any admissible constant is at
  least the modulus of the corresponding Taylor coefficient: K1 >= |[xi^4 Y]F1|, K2 >= |[xi^5]F1|, K3 >= |[xi^3 Y^2]F2|,
  K4 >= |[xi^4 Y]F2|, Psi >= |psi(0)|.  Every INF-009/INF-010 constant (A, E, C, h, B0, B1) is nondecreasing in each of
  K1..K4, Psi (gate M checks this numerically), so the radius they allow with these lower bounds is the largest radius
  the a-priori route can deliver for this branch, whatever the true constants are.
  The radius admitted for E4 is X = (2 delta)^(1/3) (|xi| < X on the petal).  The expected jump at |xi| is
  exp(-A_xi/|xi|^3), A_xi = |zeta_z| |ell| (stage 2: |zeta_z| in [18.04, 21.344], the upper value being the design model
  2 pi/(3|ell|), i.e. A_xi = 2 pi/3).  Resolving it at |xi| <= X needs at least A_xi/(X^3 ln 10) decimal digits.

Transcription (independent of LIT's illustration scripts; checked against LIT's published values in gate L):
  INF-009: A(rho) = rho^k + K rho^(k+1); E(rho) = K rho + (k+1)/2 rho^k (1+K rho)^2 (1-A)^(-k-2);
           (i) A <= min(1/2, sin(2 eta/k)); (ii) eps0 = E < min(sin eta, cos eta/(cos eta + sin eta));
           delta' = rho^k/2; sigma = sin eta - eps0; C = (3 + 2 eps0)/sigma.
  INF-010: R0 = 2, K = K1 R0 + K2; a_c(R) = 1 + K1 R + K2; rho_alpha = |alpha||alpha+1|/2 2^|Re alpha + 2| e^(|Im alpha| pi/6);
           h(R) = |alpha| R (K1 R + K2) + K3 R^2 + K4 R + Psi + |alpha| a_c (|alpha| R + K3 R^2 + K4 R + Psi)
                  + rho_alpha a_c^2 (R (1 + |alpha| + K3 R + K4) + Psi);
           s = k + m - Re alpha; C_s = C^(s/k) (2 delta + 1/(s-k)); B0(R) = e^(2|Im alpha|(pi - eta)/k) h(R) C_s;
           self-map B0(1)(2 delta)^(1/k) <= 1; contraction L = B0(2)(2 delta)^(1/k) < 1.
           Addendum (claim 6): kappa = 2(3/2)^(k+2)(K1+K2) + 2K1 + K2 + K1 + K2; a_c = 1 + K1 + K2;
           r_k = k(k+1)/2 2^(k+2) a_c^2; e1 = (k+1)kappa + r_k + 2a_c(k+kappa) + (k + k kappa + r_k)(k + kappa + 2a_c(k+kappa));
           h_d = 2(3/2)^(k+m) h(2^(m-1)) + h(2); C_{k+1} = C^((k+1)/k)(2 delta + 1); P = exp(e1 C_{k+1} (2 delta)^(1/k));
           B1 = e^(2|Im alpha|(pi-eta)/k) C_s (|alpha|(1 + P C) h(1) + P C h_d); T(H) in H needs max(B0(1), B1)(2 delta)^(1/k) <= 1.

Gates (exit 0 iff all pass):
  G0  stage1_prep.json SHA-256 = 2c9ae637...4739 and its all_pass is true.
  G1  exact data: [xi^3 Y]F2 = -alpha with alpha = -102/19 - 16 sqrt3/19 i; the pilot root has Im a > 0; c^3 = -ell.
  L   transcription check: with LIT's test germ (K1..K4 = 1/2, Psi = 1, eta = 0.3, DYAD alpha) and LIT's rho rule
      (eps0 at half its bound) the values printed in INF-010 are reproduced: rho, delta', C, B0(1), B0(2) (ChatGPT's
      50-digit replay) and kappa, r_k, e1, h_d (70-digit replay).
  M   monotonicity: doubling any one of K1..K4, Psi never enlarges the best admitted radius (at eta = pi/4).
  V   verdict: for every eta on the grid (0, pi/2) and with the stage-1 lower bounds, the best E4 radius X needs more
      than 10^6 decimal digits to resolve the jump (with the smallest A_xi of the stage-2 range).
  Reported, not gated: the radius bound 1/B0(2) with the orbit constant C set to 1 (no INF-009 loss), at eta = pi/4.
  rho is searched on a logarithmic grid over 12 decades below the INF-009 admissible maximum.
Controls (each must exit 1): --control NOFAC (the factor e^(2|Im alpha|(pi-eta)/k) dropped: L fails),
  --control ROOT (the other root of P: G1 fails), --control TAMPER (one byte of the stage-1 JSON changed: G0 fails).
Usage: python3 -I -B dyad_open20_an_stage3_apriori_route_check.py --stage1 stage1_prep.json --out OUT.json [--control C]
"""
import sys, json, argparse, hashlib, re
sys.dont_write_bytecode = True
import mpmath as mp

mp.mp.dps = 50
STAGE1_SHA = '2c9ae6376e0c482f2ba520a7ea8e2b38606a6821f7ac3bfa259d4d6020d04739'
k, m = 3, 2
S3 = mp.sqrt(3)
ALPHA = mp.mpc(mp.mpf(-102) / 19, -16 * S3 / 19)
ZETA_RANGE = (mp.mpf('18.04'), None)   # lower end of the stage-2 two-singularity fits; upper end = design model


def frac(t):
    n, _, dd = t.partition('/')
    return mp.mpf(int(n)) / (int(dd) if dd else 1)


def qs(p, q):
    return mp.mpc(frac(p), frac(q) * S3)


def parse_elem(sv, a, c):
    """Parse '((p + q*i*sqrt3) + (p2 + q2*i*sqrt3)*a)*c^j' (as written by stage 1) into a complex number."""
    pat = r'\(([-0-9/]+) \+ ([-0-9/]+)\*i\*sqrt3\)'
    parts = re.findall(pat, sv)
    val = qs(*parts[0])
    if len(parts) > 1:
        val += qs(*parts[1]) * a
    mc = re.search(r'\*c(\^(\d+))?$', sv)
    if mc:
        val *= c ** (int(mc.group(2)) if mc.group(2) else 1)
    if len(parts) not in (1, 2):
        raise ValueError(sv)
    return val


def exact_branch(root):
    mu = mp.mpc(mp.mpf(-1) / 2, mp.mpf(-2) / 3 * S3)
    c40 = mp.mpc(mp.mpf(-1) / 16, mp.mpf(7) / 144 * S3)
    d31 = mp.mpc(mp.mpf(1) / 3, mp.mpf(-1) / 9 * S3)
    cc = mp.mpc(mp.mpf(-61) / 2160, mp.mpf(43) / 6480 * S3)
    A = mp.conj(mu) - 2 * mu; B = d31 - 2 * c40
    disc = B * B - 4 * A * cc
    sq = mp.sqrt(disc)
    a = (-B - sq) / (2 * A) if root == 'pil' else (-B + sq) / (2 * A)
    ell = c40 + mu * a
    c = mp.exp(mp.log(-ell) / 3)   # principal cube root (D4)
    return a, ell, c, A * a * a + B * a + cc


def lf(K, rho, eta):
    A = rho ** k + K * rho ** (k + 1)
    E = K * rho + mp.mpf(k + 1) / 2 * rho ** k * (1 + K * rho) ** 2 * (1 - A) ** (-k - 2)
    bnd = min(mp.sin(eta), mp.cos(eta) / (mp.cos(eta) + mp.sin(eta)))
    ok = A <= min(mp.mpf(1) / 2, mp.sin(2 * eta / k)) and E < bnd
    sigma = mp.sin(eta) - E
    C = (3 + 2 * E) / sigma if sigma > 0 else mp.inf
    return ok, A, E, bnd, C


class Germ:
    def __init__(self, K1, K2, K3, K4, Psi, alpha=ALPHA, nofac=False):
        self.K1, self.K2, self.K3, self.K4, self.Psi, self.al, self.nofac = K1, K2, K3, K4, Psi, alpha, nofac

    def h(self, R):
        al = abs(self.al); ac = 1 + self.K1 * R + self.K2
        ra = al * abs(self.al + 1) / 2 * mp.power(2, abs(self.al.real + 2)) * mp.exp(abs(self.al.imag) * mp.pi / 6)
        K3, K4, Psi = self.K3, self.K4, self.Psi
        return (al * R * (self.K1 * R + self.K2) + K3 * R * R + K4 * R + Psi + al * ac * (al * R + K3 * R * R + K4 * R + Psi)
                + ra * ac * ac * (R * (1 + al + K3 * R + K4) + Psi))

    def fac(self, eta):
        return mp.mpf(1) if self.nofac else mp.exp(2 * abs(self.al.imag) * (mp.pi - eta) / k)

    def B0(self, R, C, delta, eta):
        s = k + m - self.al.real
        Cs = C ** (s / k) * (2 * delta + 1 / (s - k))
        return self.fac(eta) * self.h(R) * Cs

    def B1(self, C, delta, eta):
        K1, K2 = self.K1, self.K2
        kap = 2 * mp.mpf(1.5) ** (k + 2) * (K1 + K2) + 2 * K1 + K2 + K1 + K2
        ac = 1 + K1 + K2
        rk = mp.mpf(k * (k + 1)) / 2 * 2 ** (k + 2) * ac ** 2
        e1 = (k + 1) * kap + rk + 2 * ac * (k + kap) + (k + k * kap + rk) * (k + kap + 2 * ac * (k + kap))
        hd = 2 * mp.mpf(1.5) ** (k + m) * self.h(2 ** (m - 1)) + self.h(2)
        Ck1 = C ** (mp.mpf(k + 1) / k) * (2 * delta + 1)
        P = mp.exp(e1 * Ck1 * (2 * delta) ** (mp.mpf(1) / k))
        s = k + m - self.al.real
        Cs = C ** (s / k) * (2 * delta + 1 / (s - k))
        return self.fac(eta) * Cs * (abs(self.al) * (1 + P * C) * self.h(1) + P * C * hd), dict(kappa=kap, r_k=rk, e1=e1, h_d=hd, P=P)

    def radius(self, eta, rho, which='E4'):
        """Largest X = (2 delta)^(1/3), delta <= rho^3/2, admitted at this rho (0 if INF-009 fails)."""
        K = self.K1 * 2 + self.K2
        ok, A, E, bnd, C = lf(K, rho, eta)
        if not ok:
            return mp.mpf(0), None
        dprime = rho ** k / 2
        def good(d):
            X = (2 * d) ** (mp.mpf(1) / k)
            if which == 'E4':
                return self.B0(2, C, d, eta) * X < 1 and self.B0(1, C, d, eta) * X <= 1
            b1, _ = self.B1(C, d, eta)
            return max(self.B0(1, C, d, eta), b1) * X <= 1 and self.B0(2, C, d, eta) * X < 1
        if good(dprime):
            return (2 * dprime) ** (mp.mpf(1) / k), C
        lo, hi = mp.mpf(0), dprime          # good is monotone in delta on (0, delta']
        for _ in range(200):
            mid = (lo + hi) / 2
            if mid == lo or mid == hi:
                break
            lo, hi = (mid, hi) if good(mid) else (lo, mid)
        return (2 * lo) ** (mp.mpf(1) / k), C

    def best(self, eta, which='E4', n=240):
        """Maximize the admitted radius over rho on a logarithmic grid inside the INF-009 admissible range."""
        K = self.K1 * 2 + self.K2
        lo, hi = mp.mpf(0), mp.mpf(1)
        for _ in range(120):
            mid = (lo + hi) / 2
            lo, hi = (mid, hi) if lf(K, mid, eta)[0] else (lo, mid)
        rmax = lo
        bestX, bestrho = mp.mpf(0), None
        for i in range(n):
            rho = rmax * mp.power(10, -mp.mpf(12) * i / n)
            X, _ = self.radius(eta, rho, which)
            if X > bestX:
                bestX, bestrho = X, rho
        return bestX, bestrho, rmax


def lit_rho(K, eta):
    """LIT's illustration rule: rho at the boundary of A <= min(1/2, sin(2 eta/k)) and E <= half the (ii) bound, times 0.999."""
    lo, hi = mp.mpf(0), mp.mpf(1)
    for _ in range(200):
        mid = (lo + hi) / 2
        ok, A, E, bnd, C = lf(K, mid, eta)
        ok2 = A <= min(mp.mpf(1) / 2, mp.sin(2 * eta / k)) and E <= bnd / 2
        lo, hi = (mid, hi) if ok2 else (lo, mid)
    return lo * mp.mpf('0.999')


def rel(x, y, tol):
    return abs(x - y) <= tol * abs(y)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--stage1', required=True); ap.add_argument('--out', required=True)
    ap.add_argument('--control', choices=['NOFAC', 'ROOT', 'TAMPER'])
    o = ap.parse_args()
    raw = open(o.stage1, 'rb').read()
    if o.control == 'TAMPER':
        raw = raw.replace(b'"all_pass"', b'"all_pasS"', 1)
    g, info = {}, {}
    g['G0_stage1_hash'] = hashlib.sha256(raw).hexdigest() == STAGE1_SHA
    d = json.loads(raw.decode('utf-8'))
    g['G0_stage1_all_pass'] = d.get('all_pass') is True

    a, ell, c, Pa = exact_branch('other' if o.control == 'ROOT' else 'pil')
    g['G1_pilot_root_Im_a_positive'] = a.imag > 0
    g['G1_P_a_zero'] = abs(Pa) < mp.mpf(10) ** (-40)
    g['G1_c_cubed_minus_ell'] = abs(c ** 3 + ell) < mp.mpf(10) ** (-40)
    S4 = d['info']['S4']
    g['G1_alpha_from_stage1'] = S4['F2_xi3Y'] == '((102/19 + 16/19*i*sqrt3))'
    co = {key: parse_elem(S4[key], a, c) for key in ('F1_xi4Y', 'F1_xi5', 'F2_xi3Y2', 'F2_xi4Y', 'psi0=F2_xi5')}
    g['G1_parse_alpha'] = abs(parse_elem(S4['F2_xi3Y'], a, c) + ALPHA) < mp.mpf(10) ** (-40)
    lb = dict(K1=abs(co['F1_xi4Y']), K2=abs(co['F1_xi5']), K3=abs(co['F2_xi3Y2']), K4=abs(co['F2_xi4Y']), Psi=abs(co['psi0=F2_xi5']))
    info['a_pil'] = mp.nstr(a, 15); info['ell'] = mp.nstr(ell, 15); info['c'] = mp.nstr(c, 15)
    info['lower_bounds_from_stage1_jets'] = {kk: mp.nstr(v, 12) for kk, v in lb.items()}

    nofac = o.control == 'NOFAC'
    # L: LIT test germ, LIT rho rule; values printed in INF-010 (ChatGPT replays, PR #29 and #30 comments)
    toy = Germ(*(mp.mpf(1) / 2,) * 4, mp.mpf(1), nofac=nofac)
    eta_t = mp.mpf('0.3'); Kt = toy.K1 * 2 + toy.K2
    rho_t = lit_rho(Kt, eta_t)
    ok_t, A_t, E_t, bnd_t, C_t = lf(Kt, rho_t, eta_t)
    dp_t = rho_t ** k / 2
    b01, b02 = toy.B0(1, C_t, dp_t, eta_t), toy.B0(2, C_t, dp_t, eta_t)
    _, aux = toy.B1(C_t, dp_t, eta_t)
    g['L_rho'] = rel(rho_t, mp.mpf('0.09680972646'), mp.mpf('1e-9'))
    g['L_delta_prime'] = rel(dp_t, mp.mpf('0.00045365634'), mp.mpf('1e-8'))
    g['L_C'] = rel(C_t, mp.mpf('22.278'), mp.mpf('5e-5'))
    g['L_B0_1'] = rel(b01, mp.mpf('9.6819e8'), mp.mpf('1e-4'))
    g['L_B0_2'] = rel(b02, mp.mpf('3.0201e9'), mp.mpf('1e-4'))
    g['L_kappa'] = aux['kappa'] == mp.mpf('17.6875')
    g['L_r_k'] = aux['r_k'] == 768
    g['L_e1'] = aux['e1'] == mp.mpf('86160.46484375')
    g['L_h_d'] = rel(aux['h_d'], mp.mpf('495716.08'), mp.mpf('1e-7'))
    info['L_reproduced'] = dict(rho=mp.nstr(rho_t, 12), delta_prime=mp.nstr(dp_t, 12), C=mp.nstr(C_t, 8),
                                B0_1=mp.nstr(b01, 8), B0_2=mp.nstr(b02, 8), kappa=mp.nstr(aux['kappa'], 10),
                                r_k=mp.nstr(aux['r_k'], 10), e1=mp.nstr(aux['e1'], 14), h_d=mp.nstr(aux['h_d'], 10))

    # DYAD best case
    dy = Germ(lb['K1'], lb['K2'], lb['K3'], lb['K4'], lb['Psi'], nofac=nofac)
    eta_d = mp.pi / 4
    X_d, rho_d, rmax_d = dy.best(eta_d)
    XH_d, rhoH_d, _ = dy.best(eta_d, which='H')
    info['design_eta_pi_over_4'] = dict(best_radius_E4=mp.nstr(X_d, 6), at_rho=mp.nstr(rho_d, 6), rho_admissible_max=mp.nstr(rmax_d, 6),
                                        best_radius_with_claim6=mp.nstr(XH_d, 6))
    # ideal orbit constant C = 1 (no INF-009 loss at all), design eta: X must satisfy B0(2) X < 1 with delta -> 0
    X_ideal = 1 / dy.B0(2, mp.mpf(1), mp.mpf(0), eta_d)
    info['design_eta_ideal_C1_radius_bound'] = mp.nstr(X_ideal, 6)
    # M: monotonicity
    mono = True
    for key in ('K1', 'K2', 'K3', 'K4', 'Psi'):
        lb2 = dict(lb); lb2[key] = 2 * lb2[key]
        X2, _, _ = Germ(lb2['K1'], lb2['K2'], lb2['K3'], lb2['K4'], lb2['Psi'], nofac=nofac).best(eta_d, n=120)
        X1, _, _ = dy.best(eta_d, n=120)
        info.setdefault('monotonicity', {})[key] = '%s -> %s' % (mp.nstr(X1, 6), mp.nstr(X2, 6))
        mono = mono and X2 <= X1 * (1 + mp.mpf('1e-6'))
    g['M_monotone_in_each_constant'] = mono

    # V: verdict over an eta grid
    A_lo = ZETA_RANGE[0] * abs(ell); A_model = 2 * mp.pi / 3
    info['A_xi_range'] = [mp.nstr(A_lo, 6), mp.nstr(A_model, 6)]
    worst_digits = None; grid = {}
    for i in range(1, 16):
        eta = mp.pi / 2 * i / 16
        X, rho, _ = dy.best(eta, n=120)
        digits = A_lo / (X ** 3 * mp.log(10)) if X > 0 else mp.inf
        grid['%.4f' % float(eta)] = dict(radius=mp.nstr(X, 5), digits_needed=mp.nstr(digits, 4))
        worst_digits = digits if worst_digits is None else min(worst_digits, digits)
    info['eta_grid'] = grid
    info['min_digits_needed_over_grid'] = mp.nstr(worst_digits, 5)
    g['V_apriori_route_needs_more_than_1e6_digits'] = worst_digits > mp.mpf(10) ** 6
    # reference: radius at which the jump is ~1e-100 and ~1e-1000 (model A_xi)
    info['radius_for_jump_1e-100_model'] = mp.nstr(mp.cbrt(A_model / (100 * mp.log(10))), 6)
    info['radius_for_jump_1e-1000_model'] = mp.nstr(mp.cbrt(A_model / (1000 * mp.log(10))), 6)

    g = {kk: bool(v) for kk, v in g.items()}
    ok = all(g.values())
    for kk in sorted(g):
        print(kk, 'PASS' if g[kk] else 'FAIL')
    print('design eta=pi/4: best E4 radius', info['design_eta_pi_over_4']['best_radius_E4'],
          '| with claim 6', info['design_eta_pi_over_4']['best_radius_with_claim6'],
          '| min digits needed over eta grid', info['min_digits_needed_over_grid'])
    print('RESULT', 'PASS' if ok else 'FAIL', '(control %s)' % o.control if o.control else '')
    with open(o.out, 'w', encoding='utf-8', newline='\n') as f:
        json.dump({'gates': g, 'info': info, 'all_pass': ok, 'control': o.control, 'mpmath_dps': mp.mp.dps,
                   'script': 'dyad_open20_an_stage3_apriori_route_check.py',
                   'lit_sources': 'rtg-lit 564a1ee: inferences/INF-009, inferences/INF-010 (incl. Addendum)'},
                  f, indent=1, sort_keys=True)
        f.write('\n')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
