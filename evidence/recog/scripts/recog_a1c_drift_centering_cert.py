#!/usr/bin/env python3
"""A1c -- chart reciprocal drift centring: removing the logarithmic majorant tau A_1 from the known-a envelope.

Setting (recog-v0.3.25 §6.13b, RECOG-THM-A1C-SHARPENED-SCHEDULE; part 1b; combined tail; start offset). In the normalized chart
z = h^{-1}(W), q = |z|^2, with b := q_0^{-1} and q_m at block base points, part 1b bounded the reciprocal law
    q_{m+1}^{-1} - q_m^{-1} - 1 =: delta_m,   |delta_m| <= gamma0 q_m + gamma1 q_m^2   (gamma0 = 0.17715)
and summed it in absolute value:  q_m^{-1} = b + m + eps_m,  |eps_m| <= epsbar_m = e_const + 2 gamma0 log(1 + m/2b').  The tail
    A_1 = sum_{m>=M} (q_m - 1/(b+m))
inherited the logarithm: tau A_1 = O_a(log(a+M)/(a+M)) is the term that made E''' (and E^(4)) grow again at M = 10^7.
This cell (PI decision of 27 Oct 2026, "START RECOG A1c -- CHART RECIPROCAL DRIFT CENTERING"):
  Lemma 21 (exact first order).  delta_m = -(29/216) q_m - 2 Re(a05 e^{-6 i Theta_m}) q_m + R_m,  |R_m| <= gamma2 q_m^2,
      from 1/q' = 1/(q(1+x)), x = 2 Re u + |u|^2, u = mu q + a32 q^2 + a05 zbar^6/q + rho_7 (DYAD-ALG-NF6, DYAD-THM-NF-REM):
      the isotropic coefficient is 1 - |mu|^2 - 2 Re a32 = -29/216 exactly (part 1b G1); the sixth harmonic has zero mean.
  Lemma 22 (centred drift).  With H_m(b) := psi(b+m) - psi(b) = sum_{j<m} 1/(b+j) and  b~_m := b + m - (29/216) H_m(b):
      sup_m |q_m^{-1} - b~_m| <= K_eps(a),  an explicit constant WITHOUT logarithm:
      K_eps = (29/216) Lam_iso + 2|a05| Omega + gamma2 Sigma_{2,0},  where
        Lam_iso   >= sup_m |sum_{j<m} (q_j - 1/(b+j))|           (part 1b closed form at M = 0; converges: epsbar_j/(b+j)^2 summable),
        Omega     >= sup_m |sum_{j<m} q_j e^{-6 i Theta_j}|      (Euler-Maclaurin for sum (b+j)^{-1-6 i tau}: 2[1/(6 tau) + (1+|s|)/(2b')],
                                                                   plus the convergent phase-deviation and amplitude-deviation sums),
        Sigma_{2,0} >= sum_{j>=0} q_j^2                         (one-orbit bound).
      The phase model is Theta_j = Theta_0 + eta_inf - tau log((b+j)/b) + (eta_j - eta_inf), |eta_j - eta_inf| <= (tau Lam_A1(j) + tau/(b'+j)
      + c_theta Sigma_2(j)); the unknown constant phase eta_inf factors out of the magnitude bound.
  Prop. 23 (centring identity, exact).  A_1 = Lambda^log_M(b) + A_1',   Lambda^log_M(b) := sum_{m>=M} (1/b~_m - 1/(b+m))  (explicit in (b, M)),
      |A_1'| <= K_eps(a) P'_2(M),  P'_2 a closed-form majorant of sum_{m>=M} 1/(q_m^{-1} b~_m)  -- no logarithm.
  Cor. 24 (centred schedule).  With b enclosed by the start-offset iteration (b in [b-, b+]):
      c^(5)_k = c^(4)_k - tau mid Lambda^log_{M_k}([b-,b+]),   E^(5)_k = E^(4)_k - tau A_1(a,M_k) + tau half Lambda^log + tau K_eps P'_2(M_k).
      Every remaining term of E^(5) is O_a(1/(a+M)) or O_a(log(a+M)/(a+M)^{3/2}) (the q_M brackets still carry epsbar_M), hence
      E^(5) = O_a(1/(a+M)) -- a statement about this envelope, checked term by term in G3 (the grid values E^(5)(a+M) stop rising).
Gates:  G1 exact identities (sympy: the first-order coefficient of 1/q' - 1/q - 1; the model integrals; H_m = psi difference);
        G2 constants by interval arithmetic (gamma2; the Euler-Maclaurin bound against mpmath's Hurwitz zeta at Re s = 1; K_eps(a) with its
           components for a in {625, 1000, 2500}); G3 the closed-form Lambda^log against direct summation, the envelope table E^(5) vs E^(4)
           on the grid and the (a+M)-scaled values; G4 [NUM-A] jet-model orbits (rho_7 = 0): sup_m |q_m^{-1} - b~_m| <= K_eps while the old
           majorant epsbar_m grows like a logarithm; G5 [NUM-B] the 12 primitive orbits (N steps): |eps^(5)_k| <= E^(5)_k + L_tol at every
           slip and E^(5)_k < E^(4)_k, with the identity-corrected end estimate of L (as in the start-offset cell).
Negative controls: NC1 the isotropic coefficient replaced by -30/216 makes the jet-model drift exceed K_eps (the centre is wrong);
        NC2 the sign of the Lambda^log centre flipped breaks G5 at some slip.
Dependencies: DYAD-ALG-NF6 (mu, a32, a05), DYAD-THM-NF-REM (C_7, one-orbit contraction), part 1b (gamma0, c_theta, closed forms, A_1),
        start offset (b-enclosure; (D5) through Delta_a and the amplitude brackets).  The identity and K_eps need no (D5) constant.
usage: python -I recog_a1c_drift_centering_cert.py [OUT_JSON] [N_STEPS]
"""
import hashlib, json, math, os, sys
import numpy as np
import mpmath as mp
from mpmath import iv
import sympy as sp
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import recog_a1c_start_offset_cert as pso
pct, pib, p2, p1b = pso.pct, pso.pib, pso.p2, pso.p1b
I, up, lo, f, tau = p1b.I, p1b.up, p1b.lo, p1b.f, p1b.tau
fdn, fup = p2.fdn, p2.fup
mp.mp.dps = 40; iv.dps = 40
res = {"gates": {}, "imports": {"recog_a1c_start_offset_cert.py": hashlib.sha256(open(os.path.join(HERE, "recog_a1c_start_offset_cert.py"), "rb").read()).hexdigest(), **pso.res["imports"]}}
C_ISO = I(29)/216
abs_a05, abs_mu, abs_a32, A5, C7, c_theta, gamma0, gamma1 = p1b.abs_a05, p1b.abs_mu, p1b.abs_a32, p1b.A5, p1b.C7, p1b.c_theta, p1b.gamma0, p1b.gamma1
qstar = I(256)/140625
# ---------------- G1: exact identities ----------------
X = sp.sqrt(3); q, Th = sp.symbols('q Theta', positive=True, real=True)
mu = -sp.Rational(1, 2) - sp.I*2*X/3; a32 = -sp.Rational(97, 432) + sp.I*197*X/324; a05 = -sp.Rational(49, 8640) - sp.I*307*X/25920
u = mu*q + a32*q**2 + a05*q**2*(sp.cos(6*Th) - sp.I*sp.sin(6*Th))                       # a05 zbar^6/q = a05 q^2 e^{-6 i Theta}
x = sp.expand(2*sp.re(u) + sp.re(u)**2 + sp.im(u)**2)
inv = sp.series(1/(q*(1 + x)), q, 0, 2).removeO()                                        # 1/q' = 1/(q(1+x)) through order q^1
first = sp.simplify(sp.expand(inv - 1/q - 1).coeff(q, 1))
g1a = sp.simplify(first - (-sp.Rational(29, 216) - 2*sp.re(a05*(sp.cos(6*Th) - sp.I*sp.sin(6*Th))))) == 0
g1a2 = sp.simplify(sp.expand(inv - 1/q - 1).coeff(q, 0)) == 0
xs, bs, Ms = sp.symbols('x b M', positive=True)
g1b = sp.simplify(sp.integrate(sp.log(1 + xs/bs)/(bs + xs)**2, (xs, Ms, sp.oo)) - (sp.log(1 + Ms/bs) + 1)/(bs + Ms)) == 0   # int_M^inf log(1+x/b)/(b+x)^2
g1c = sp.simplify(sp.integrate(sp.log(1 + xs/(2*bs))/(bs + xs)**2, (xs, 0, sp.oo)) - sp.log(2)/bs) == 0                 # int_0^inf log(1+x/2b)/(b+x)^2
g1d = all(sp.simplify(sp.expand_func(sp.digamma(sp.Rational(7, 3) + m)) - sp.expand_func(sp.digamma(sp.Rational(7, 3))) - sum(1/(sp.Rational(7, 3) + j) for j in range(m))) == 0 for m in (1, 2, 5))
res["gates"]["G1_exact"] = bool(g1a and g1a2 and g1b and g1c and g1d)
res["G1"] = {"first_order_coefficient_-29/216_minus_2Re(a05e^-6iTheta)": g1a, "order_q0_vanishes": g1a2, "int_log_over_square_from_M": g1b, "int_log2_over_b": g1c, "H_m_is_digamma_difference": g1d}
# ---------------- G2: constants ----------------
qq = qstar
v = A5*qq**2 + C7*qq**3                                   # |u - mu q|
delta3 = 2*C7*qq**3 + 2*abs_mu*qq*v + v**2                # |x_2 - (2 Re a32 + 2 Re(a05 e^{-6iTheta}) + |mu|^2) q^2|
x2_abs = (2*abs_a32 + 2*abs_a05 + abs_mu**2)*qq**2 + delta3
x_abs = qq + x2_abs
R_abs = delta3/qq + qq*x_abs/(1 - x_abs) + (2*x2_abs + x2_abs**2/qq)/(1 - x_abs)
gamma2 = R_abs/qq**2                                      # every term/q^2 increases with q: the value at q* is the supremum on (0, q*]
s6 = iv.sqrt(I(1) + 36*tau**2)                            # |s|, s = 1 + 6 i tau
def zeta_bound(xv):                                       # |zeta(1 + 6 i tau, x)| <= 1/|s-1| + (1 + |s|)/(2x)   (first-order Euler-Maclaurin, Re s = 1)
    return 1/(6*tau) + (1 + s6)/(2*xv)
s_c = mp.mpc(1, 6*mp.mpf(up(tau)))
zeta_check = {}
for xv in (600, 625, 1000, 2500, 10**4, 10**6):
    ex = abs(mp.zeta(s_c, mp.mpf(xv))); bd = float(lo(zeta_bound(I(xv)))); zeta_check[str(xv)] = (float(ex), bd, float(ex) <= bd)
g2z = all(v_[2] for v_ in zeta_check.values())
def P(p, b_, M_): return p1b.P(p, b_, M_)
def tailP2(bp, j):                                        # sum_{i>=j} (b'+i)^{-2} <= (1 + 1/b')/(b'+j)   (first term + integral)
    return (1 + 1/bp)/(bp + j)
C_L = lambda bp: 1 + 2*(iv.log(I(2)) + 1/(8*bp))           # uniform constant of the log tail (see tailLg2)
def tailLg2(bp, j):                                       # sum_{i>=j} log(1+i/2b')(b'+i)^{-2} <= [2 log(1+j/2b') + C_L]/(b'+j):
    # j >= b': summand decreasing, first term + integral (G1: int = log(1+j/2b)/(b+j) + (1/b) log((2b+j)/(b+j)) <= [log(1+j/2b) + 1]/(b+j));
    # j < b': the whole sum from 0 <= log2/b' + sup summand (<= 1/(8b'^2)) <= 2(log2 + 1/(8b'))/(b'+j) since b'+j <= 2b'
    return (2*iv.log(1 + j/(2*bp)) + C_L(bp))/(bp + j)
def K_eps(a):
    """Lemma 22 constant: sup_m |q_m^{-1} - b~_m|, closed forms in a only (b' = a - Delta_a the smallest admissible b)"""
    a = I(a); env0 = p1b.envelope_new(a, 1)
    Delta_a = env0["Delta_a"]; bp = a - Delta_a; q0b = 1/bp
    sigma2 = 2*q0b + q0b**2                                               # sum_{j>=0} q_j^2 <= q_0^2 + 2 q_0 (one-orbit bound)
    kappa = env0["kappa"]
    e_const = gamma0*q0b + gamma1*sigma2
    Lam_A1 = lambda M_: (e_const*tailP2(bp, M_) + 2*gamma0*tailLg2(bp, M_))/(1 - kappa)           # >= sum_{j>=M} |q_j - 1/(b+j)|  (part 1b bracket, sharper tails)
    Lam_iso = Lam_A1(I(0))                                                                          # sup_m |sum_{j<m}(q_j - 1/(b+j))| <= sum_j |...|
    # phase deviation: |eta_j - eta_inf| <= tau Lam_A1(j) + tau/(b'+j) + c_theta Sigma_2(j),  Sigma_2(j) = sum_{i>=j} q_i^2 <= P(2,b',j)/(1-kappa)^2
    # sum_{j>=0} 6 |eta_j - eta_inf| /(b+j): each piece is a sum of (const + log)/(b'+j)^2 type terms, majorised by first term + integral (G1b, G1c)
    #   Lam_A1(j) <= [e_const (1 + 1/b') + 2 gamma0 (log(1+j/2b')(1 + 1/b') + 1)] /((1-kappa)(b'+j))   (P(2) <= (1+1/b')/(b'+j) -- first term + integral; Lg(2) likewise)
    # Lam_A1(j) <= [e_const tailP2(j) + 2 gamma0 tailLg2(j)]/(1-kappa) = [cA + cC + cB log(1+j/2b')]/(b'+j)
    cA = e_const*(1 + 1/bp)/(1 - kappa); cB = 4*gamma0/(1 - kappa); cC = 2*gamma0*C_L(bp)/(1 - kappa)
    S_1 = 1/bp**2 + 1/bp                                                 # sum_j (b'+j)^{-2}
    S_log = iv.log(I(2))/bp + 1/(8*bp**2)                                # sum_j log(1+j/2b')/(b'+j)^2  (G1c + the sup-summand slack)
    phase_sum = 6*(tau*((cA + cC)*S_1 + cB*S_log) + tau*S_1 + c_theta*(1 + 1/bp)/(1 - kappa)**2*S_1)
    amp_sum = Lam_iso
    Omega = 2*zeta_bound(bp) + amp_sum + phase_sum
    K = C_ISO*Lam_iso + 2*abs_a05*Omega + gamma2*sigma2
    return {"K": K, "Lam_iso": Lam_iso, "Omega": Omega, "zeta_part": 2*zeta_bound(bp), "phase_sum": phase_sum, "Sigma20": sigma2, "gamma2_part": gamma2*sigma2,
            "osc_part": 2*abs_a05*Omega, "iso_part": C_ISO*Lam_iso, "bp": bp, "kappa": kappa, "Delta_a": Delta_a}
Ktab = {str(a): {k: f(v_) for k, v_ in K_eps(a).items()} for a in (625, 1000, 2500)}
res["G2_constants"] = {"gamma2": f(gamma2), "|s|": f(s6), "zeta_bound_vs_mpmath": zeta_check, "K_eps": Ktab, "gamma0_old": f(gamma0), "2|a05|": f(2*abs_a05), "29/216": f(C_ISO)}
res["gates"]["G2_constants"] = bool(g2z and up(gamma2) < 10 and all(Ktab[a]["K"] < 0.1 for a in Ktab))
# ---------------- Lambda^log closed form (interval in b) and the centred envelope ----------------
def H_bracket(b_, m):
    """H_m(b) = psi(b+m) - psi(b) enclosed by log x - 1/x < psi(x) < log x - 1/(2x)"""
    n = b_ + m
    return iv.mpf([lo(iv.log(n/b_) - 1/n + 1/(2*b_)), up(iv.log(n/b_) - 1/(2*n) + 1/b_)]) if m > 0 else I(0)
def Lambda_log(b_, M, J=None):
    """sum_{m>=M} (1/b~_m - 1/(b+m)), b~_m = b + m - (29/216) H_m(b): explicit terms for m < M+J, closed-form tail (summand <= C_ISO H/(n (n - C_ISO H)))"""
    b_ = I(b_) if not hasattr(b_, "_mpi_") else b_
    J = J or max(2000, int(up(b_)) + 1)
    assert M + J > up(b_), "tail start must be beyond b for the monotone tail bound"
    tot = I(0)
    for m in range(M, M + J):
        n = b_ + m; H = H_bracket(b_, m); bt = n - C_ISO*H
        tot += 1/bt - 1/n
    # tail m >= M+J (M+J > b, so the summand bound (log(n/b)+1/b)/n^2 is decreasing): t_m <= C H_m/(n b~_m) <= C/(1-kappa2) (log(n/b)+1/b)/n^2,
    # sum <= first term + integral (G1b):  kappa2 = sup_m C(log(n/b)+1/b)/n <= C(1/e + 1/b)/b
    Mt = M + J; n0 = b_ + Mt; Hup = iv.log(n0/b_) + 1/b_
    kappa2 = C_ISO*(iv.exp(I(-1)) + 1/b_)/b_
    tail_up = C_ISO/(1 - kappa2)*(Hup/n0**2 + (iv.log(n0/b_) + 1 + 1/b_)/n0)
    return iv.mpf([lo(tot), up(tot + tail_up)])
def P2prime(a, M):
    """closed-form majorant of sum_{m>=M} 1/(q_m^{-1} b~_m): q_m^{-1} >= b'+m-epsbar_m (part 1b), b~_m >= b'+m - C_ISO(log(1+m/b')+1/b')"""
    a = I(a); env = p1b.envelope_new(a, M); bp = a - env["Delta_a"]
    kappa = env["kappa"]; kap2 = C_ISO*(iv.exp(I(-1)) + 1/bp)/bp                       # sup_m (log(1+m/b')+1/b')/(b'+m) <= (1/e + 1/b')/b'
    return P(I(2), bp, I(M))/((1 - kappa)*(1 - kap2))
# G3: Lambda^log closed form against direct high-precision summation (fixed b), and the envelope table
def Lambda_log_direct(bf, M, N=3_000_000):
    m = np.arange(M, N, dtype=np.float64); n = bf + m
    psi_b = float(mp.digamma(bf)); psi_n = np.log(n) - 1/(2*n) - 1/(12*n**2) + 1/(120*n**4)       # |error| < 1/(252 n^6) for n >= 600
    Hm = psi_n - psi_b
    bt = n - (29/216)*Hm
    return float(np.sum(1/bt - 1/n))
g3 = True; lam_checks = {}
for a, M in ((625, 1000), (2500, 1000), (625, 100000)):
    cf = Lambda_log(I(a), M); direct = Lambda_log_direct(float(a), M)
    ok = lo(cf) - 1e-6 <= direct and direct <= up(cf) + 1e-6 and up(cf) <= 2*direct     # enclosure contains the direct sum (its tail beyond N = 3e6 is below 1e-6) and is not loose by more than 2x
    g3 &= ok; lam_checks[f"a={a},M={M}"] = {"closed": [f(lo(cf)), f(up(cf))], "direct": direct, "ok": bool(ok)}
res["G3_Lambda_log"] = lam_checks
# envelope table: E^(5) vs E^(4) on the grid, with b-range of width 2 around a (illustrative; the record-specific ranges come from the start-offset iteration)
table = {}; rising_old = {}; rising_new = {}
for a in (625, 1000, 2500):
    table[str(a)] = {}; Ka = K_eps(a)["K"]
    prev_old = prev_new = None; ro = rn = False
    for M in (1000, 10000, 100000, 1000000, 10000000):
        tbl = {}
        for r in range(6):
            c3 = pct.combined(a, M, r); e1b = p1b.envelope_new(a, M)
            E3, tA0, tA1 = c3["E3"], c3["tauA0"], tau*e1b["A1"]
            om = iv.mpf([-1, 1]); bw = (mp.mpf(a) - 1, mp.mpf(a) + 1)
            prod = om*pso.S_bracket(a, M, bw); half0 = (up(prod) - lo(prod))/2
            E4 = E3 - tA0 + tau*half0
            Lam = Lambda_log(iv.mpf([bw[0], bw[1]]), M, J=2000) if M < 10**6 else Lambda_log(iv.mpf([bw[0], bw[1]]), M, J=200)
            halfL = (up(Lam) - lo(Lam))/2
            E5 = E4 - tA1 + tau*halfL + tau*Ka*P2prime(a, M)
            tbl[str(r)] = {"E3": f(E3), "E4": f(E4), "E5": f(E5), "tauA1_old": f(tA1), "tau_halfLam": f(tau*halfL), "tau_K_P2": f(tau*Ka*P2prime(a, M)), "Lam_mid": f((lo(Lam) + up(Lam))/2),
                           "E4(a+M)": f(E4)*(a + M), "E5(a+M)": f(E5)*(a + M)}
            g3 &= up(E5) < up(E4)
        worst4 = max(tbl[r]["E4(a+M)"] for r in tbl); worst5 = max(tbl[r]["E5(a+M)"] for r in tbl)
        if prev_old is not None: ro |= worst4 > prev_old*1.001; rn |= worst5 > prev_new*1.001
        prev_old, prev_new = worst4, worst5
        table[str(a)][str(M)] = tbl
    rising_old[str(a)] = ro; rising_new[str(a)] = rn
res["G3_table"] = table; res["G3_scaled_rising"] = {"E4(a+M)_rises_on_grid": rising_old, "E5(a+M)_rises_on_grid": rising_new}
res["gates"]["G3_Lambda_log_and_table"] = bool(g3 and not any(rising_new.values()))
# ---------------- G4 [NUM-A]: jet-model orbits ----------------
MU = complex(-0.5, -2*math.sqrt(3)/3); A32 = complex(-97/432, 197*math.sqrt(3)/324); A05 = complex(-49/8640, -307*math.sqrt(3)/25920)
def jet_orbit(b, th0, N, c_iso=29/216):
    z = complex(math.sqrt(1/b)*math.cos(th0), math.sqrt(1/b)*math.sin(th0)); drift_max = 0.0; drifts = []
    Hm = 0.0  # H_m(b) accumulated exactly as sum 1/(b+j)
    for m in range(N + 1):
        qm = abs(z)**2
        d = 1/qm - (b + m - c_iso*Hm)
        drift_max = max(drift_max, abs(d))
        if m % 10000 == 0: drifts.append((m, float(d)))
        Hm += 1/(b + m)
        uu = MU*qm + A32*qm*qm + A05*(z.conjugate()**6)/qm
        z = z*(1 + uu)
    return drift_max, drifts
g4 = True; jet = {}
for b in (625, 1000, 2500):
    Kb = Ktab[str(b)]["K"]
    for th0 in (0.3, 1.7, 3.9, 5.1):
        dm, dr = jet_orbit(b, th0, 300_000)
        eps_old = f(gamma0)*(1/b) + f(gamma1)*(2/b + 1/b**2) + 2*f(gamma0)*math.log(1 + 300_000/(2*b))     # old majorant at m = 3e5
        ok = dm <= Kb; g4 &= ok
        jet[f"b={b},th={th0}"] = {"sup_drift": dm, "K_eps": Kb, "ratio": dm/Kb, "old_epsbar_at_3e5": eps_old, "samples": dr[::6], "ok": bool(ok)}
res["G4_jet_model"] = jet; res["gates"]["G4_NUM_jet_drift_within_K"] = bool(g4)
# NC1: wrong isotropic coefficient
nc1 = True
for b in (625, 2500):
    dm, _ = jet_orbit(b, 0.3, 300_000, c_iso=30/216)
    nc1 &= dm > Ktab[str(b)]["K"]
res["NC1"] = {"wrong_coefficient_30/216_exceeds_K": bool(nc1)}
# ---------------- G5 [NUM-B]: primitive orbits ----------------
TAU = float(up(tau))
def centred5(a, n0, slips, sign=+1):
    hist, cfun, Efun, arcW, arcT, D0, Delta_a, omega, Tarc = pso.centred(a, n0, slips)
    bw = (mp.mpf(a) - omega[1], mp.mpf(a) - omega[0]); Ka = K_eps(a)["K"]
    sh5 = {}; en5 = {}
    for (k, M, r) in slips:
        Lam = Lambda_log(iv.mpf([bw[0], bw[1]]), M)
        mid = (lo(Lam) + up(Lam))/2; half = (up(Lam) - lo(Lam))/2
        tA1 = tau*p1b.envelope_new(a, M)["A1"]
        sh5[M] = -sign*tau*I(mid)
        en5[M] = iv.mpf([0, up(Efun(a, M, r) - tA1 + tau*half + tau*Ka*P2prime(a, M))])
    cfun5 = lambda a_, M, r, c=cfun, s=sh5: c(a_, M, r) + s[M]
    Efun5 = lambda a_, M, r, e=en5: e[M]
    return cfun, Efun, cfun5, Efun5, bw, Ka
if __name__ == "__main__":
    outp = sys.argv[1] if len(sys.argv) > 1 else "a1c_drift_centering_cert.json"
    N = int(sys.argv[2]) if len(sys.argv) > 2 else 1_800_000
    Q0s = [1/625]*4 + [1/1000]*4 + [1/2500]*4; ths = [0.3, 1.7, 3.9, 5.1]*3
    anc, hist_phi, Qh, Psi = pib.simulate(Q0s, ths, N); Nb = N//6
    g5 = True; nc2 = False; orbits = []
    for i in range(12):
        a = 1/Q0s[i]; an = anc[i]; n0 = an[0]
        slips = []; k = 0
        for j in range(1, len(an)):
            if an[j] - an[j - 1] == 7:
                k += 1; nA = an[j - 1]; M = nA//6; r = nA % 6
                if M >= 1: slips.append((k, M, r))
        cfun, Efun, cfun5, Efun5, bw, Ka = centred5(a, n0, slips)
        Delta_a = f(p1b.envelope_new(a, 1)["Delta_a"])
        ell0 = math.floor(hist_phi[i, n0]/(2*math.pi)); thN = hist_phi[i, 6*Nb] % (2*math.pi)
        dN = -math.sqrt(3)/12*math.cos(thN) + 0.25*math.sin(thN) - math.sqrt(3)/24*math.cos(3*thN) - math.sin(3*thN)/24
        L = math.pi/3*n0 - 2*math.pi*ell0 + (hist_phi[i, 6*Nb] - 2*math.pi*Nb) + TAU*float(mp.digamma(a + Nb)) - dN/math.sqrt(a + Nb)
        Ltol = TAU*Delta_a/(a + Nb) + 3/(a + Nb)
        rows = []
        for (k, M, r) in slips:
            c4 = TAU*float(mp.digamma(a + M)) - (k - 1)*math.pi/3 + f(cfun(a, M, r)); E4 = f(Efun(a, M, r))
            c5 = TAU*float(mp.digamma(a + M)) - (k - 1)*math.pi/3 + f(cfun5(a, M, r)); E5 = f(Efun5(a, M, r))
            eps4 = c4 - L; eps5 = c5 - L
            ok = abs(eps5) <= E5 + Ltol and E5 < E4; g5 &= ok
            rows.append({"k": k, "M": M, "r": r, "eps4": eps4, "E4": E4, "eps5": eps5, "E5": E5, "ratio5_with_tol": abs(eps5)/(E5 + Ltol), "ratio5": abs(eps5)/E5, "gain_E5_vs_E4": E4/E5, "ok": bool(ok)})
        # NC2: centre sign flipped
        _, _, cf_nc, Ef_nc, _, _ = centred5(a, n0, slips, sign=-1)
        for (k, M, r) in slips:
            c5n = TAU*float(mp.digamma(a + M)) - (k - 1)*math.pi/3 + f(cf_nc(a, M, r))
            if abs(c5n - L) > f(Ef_nc(a, M, r)) + Ltol: nc2 = True
        orbits.append({"a": a, "theta0": ths[i], "n0": int(n0), "b_range": [fdn(bw[0]), fup(bw[1])], "K_eps": f(Ka), "L_est": L, "L_tol": Ltol, "slips": rows})
    res["gates"].update({"G5_NUM_eps5_within_E5_and_E5_below_E4": bool(g5), "NC1_wrong_coefficient_caught": bool(nc1), "NC2_flipped_centre_breaks_G5": bool(nc2)})
    res["G5"] = {"N_steps": N, "orbits": orbits, "max_ratio5": max(s["ratio5"] for o in orbits for s in o["slips"]), "max_ratio5_with_tol": max(s["ratio5_with_tol"] for o in orbits for s in o["slips"]),
                 "min_gain": min(s["gain_E5_vs_E4"] for o in orbits for s in o["slips"]), "max_gain": max(s["gain_E5_vs_E4"] for o in orbits for s in o["slips"])}
    ok = all(res["gates"].values()); res["ALL_PASS"] = ok
    json.dump(res, open(outp, "w"), indent=1, default=lambda o: bool(o) if isinstance(o, np.bool_) else (float(o) if isinstance(o, (np.floating, np.integer)) else str(o)))
    for k_, v_ in res["gates"].items(): print(k_, "PASS" if v_ else "FAIL")
    print("gamma2 =", res["G2_constants"]["gamma2"], " K_eps:", {a: round(Ktab[a]["K"], 5) for a in Ktab}, " (old epsbar at M=1e5, a=625:", round(f(gamma0)*(1/625) + f(gamma1)*(2/625) + 2*f(gamma0)*math.log(1 + 1e5/1250), 3), ")")
    for a in table:
        print("a=%s: " % a + "  ".join("M=%s E4=%.2e E5=%.2e (E5(a+M)=%.1f, E4(a+M)=%.1f)" % (M, max(t["E4"] for t in table[a][M].values()), max(t["E5"] for t in table[a][M].values()), max(t["E5(a+M)"] for t in table[a][M].values()), max(t["E4(a+M)"] for t in table[a][M].values())) for M in table[a]))
    for o in orbits:
        print("a=%4d th=%.1f n0=%d: b in [%.2f, %.2f] K=%.4f | " % (o["a"], o["theta0"], o["n0"], o["b_range"][0], o["b_range"][1], o["K_eps"]) + " ".join("k%d(M=%d) e5=%+.1e/E5=%.1e (E4=%.1e x%.1f)" % (s["k"], s["M"], s["eps5"], s["E5"], s["E4"], s["gain_E5_vs_E4"]) for s in o["slips"]))
    print("ALL PASS" if ok else "FAILURES"); sys.exit(0 if ok else 1)
