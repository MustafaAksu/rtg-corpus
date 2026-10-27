#!/usr/bin/env python3
"""A1c -- chart reciprocal drift centring: removing the logarithmic majorant tau A_1 from the known-a envelope, and a
correction finding on the asymptotic-order sentences of the adopted envelopes (CORR-1, CORR-2).

Setting (recog-v0.3.25 §6.13b, RECOG-THM-A1C-SHARPENED-SCHEDULE; part 1b; combined tail; start offset). Normalized chart
z = h^{-1}(W), q = |z|^2, b := q_0^{-1}, q_m at block base points. Part 1b bounded the reciprocal law
    delta_m := q_{m+1}^{-1} - q_m^{-1} - 1,   |delta_m| <= gamma0 q_m + gamma1 q_m^2   (gamma0 = 0.17715)
and summed it in absolute value: q_m^{-1} = b + m + eps_m, |eps_m| <= epsbar_m = e_const + 2 gamma0 log(1 + m/2b'); the tail
A_1 = sum_{m>=M} (q_m - 1/(b+m)) inherited the logarithm.  This cell (PI decision of 27 Oct 2026, "START RECOG A1c -- CHART
RECIPROCAL DRIFT CENTERING"):
  Lemma 21 (exact first order).  delta_m = -(29/216) q_m - 2 Re(a05 e^{-6 i Theta_m}) q_m + R_m,  |R_m| <= gamma2 q_m^2,
      from 1/q' = 1/(q(1+x)), x = 2 Re u + |u|^2, u = mu q + a32 q^2 + a05 zbar^6/q + rho_7 (DYAD-ALG-NF6, DYAD-THM-NF-REM);
      the isotropic coefficient 1 - |mu|^2 - 2 Re a32 = -29/216 is exact (part 1b G1); the sixth harmonic has zero mean.
      gamma2 is dominated by the NF-REM tail ceiling: |2 Re(rho_7/z)|/q <= 2 C_7 q^2 (C_7 = 100).
  Lemma 22 (centred drift).  With H_m(b) := psi(b+m) - psi(b) = sum_{j<m} 1/(b+j) and b~_m := b + m - (29/216) H_m(b):
      sup_{m>=0} |q_m^{-1} - b~_m| <= K_eps(a) := (29/216) Lam_iso + 2|a05| Omega + gamma2 Sigma_{2,0}   -- no logarithm --
      Lam_iso >= sum_j |q_j - 1/(b+j)| (convergent: epsbar_j/(b+j)^2 summable), Omega >= sup_m |sum_{j<m} q_j e^{-6 i Theta_j}|
      (Euler-Maclaurin for sum (b+j)^{-1 -+ 6 i tau}: 2[1/(6 tau) + (1+|s|)/(2b')], plus the convergent amplitude- and
      phase-deviation sums; the phase model Theta_j = Theta_0 + eta_inf - tau log((b+j)/b) + (eta_j - eta_inf) with
      |eta_j - eta_inf| <= tau Lam_A1(j) + tau/(b'+j) + c_theta Sigma_2(j); the unknown constant eta_inf factors out),
      Sigma_{2,0} >= sum_j q_j^2 (one-orbit bound).  Numerically K_eps is dominated by gamma2 Sigma_{2,0} (the C_7 ceiling).
  Prop. 23 (centring identity, exact).  A_1 = Lambda^log_M(b) + A_1',  Lambda^log_M(b) := sum_{m>=M} (1/b~_m - 1/(b+m)) =
      sum_{m>=M} (29/216) H_m(b)/((b+m) b~_m)  (explicit in (b, M)),  |A_1'| <= K_eps(a) P'_2(M), P'_2 a closed-form majorant
      of sum_{m>=M} 1/(q_m^{-1} b~_m) -- no logarithm, no constant floor.
  Cor. 24 (centred schedule, log-free envelope).  With b enclosed by the start-offset iteration (b in [b-, b+]):
      c^(5)_k = c^(4)_k - tau mid Lambda^log_{M_k}([b-,b+]);
      E^(5)_k = E^(4)_k - tau A_1 - ref_d^old + tau half Lambda^log + tau K_eps P'_2 + ref_d^new,
      ref_d^new = (sqrt3/8) max(sqrt(q+) - n^{-1/2}, n^{-1/2} - sqrt(q-)) with the log-free bracket q_M^{-1} in [b~_M(b-) - K, b~_M(b+) + K].
      Every term of E^(5) is O_a(1/(a+M)) or o(1/(a+M)) and none has a constant floor (G3c: E^(5)(a+M) is bounded and
      non-increasing on the grid 10^4 .. 10^13).
CORRECTION FINDING (not a change of any inequality; the theorems' bounds remain valid; the asymptotic-order SENTENCES are wrong):
  CORR-1  the closed-form majorant Lg(p, b', M) of part 1b (sum_{m>=M} log(1+m/2b')(b'+m)^{-p}) carries the M-independent term
          b'^{-p} ("2 sup g" slack).  Hence A_1(a, M) >= 2 gamma0 b'^{-2}/(1-kappa) for every M: the adopted E''' (and E^(4))
          has a constant floor ~ 1.1e-6 at a = 625 (6.8e-8 at a = 2500), and  E''' = O_a((1+log(a+M))/(a+M)),
          E''' = o((a+M)^{-1/2})  [recog-v0.3.25 §1, §6.13b]  and  E''' sqrt(a+M) -> 0,  Sbar' sqrt(a+M) -> 0.74850,
          Rbar' sqrt(a+M) -> 1.0753  [part 1b record, RECOG-ALG-A1C-TAIL-HARMONICS (i)]  are false for the majorants as defined
          (Sbar', Rbar' also carry b'^{-5/2}, b'^{-3} floors through Lg(5/2), Lg(3)).  On the certified grid M <= 10^7 the floor is
          at most ~20 % of E''' (a = 625) and the displayed values are unaffected.
  CORR-2  the reference term ref_d of the combined-tail envelope uses q+_M = ((1-kappa)(b'+M))^{-1} with the UNIFORM slack
          kappa = sup_m epsbar_m/(b'+m) ~ 1.3e-3; its contribution is (sqrt3/8)(kappa/2)(a+M)^{-1/2} -- order (a+M)^{-1/2}, not
          o((a+M)^{-1/2}) (1.45e-4 (a+M)^{-1/2}: 1 % of E''' at M = 10^7, dominant beyond ~10^9).
  Both are repaired by sharper, still valid, closed forms: Lg_corr (first term + integral in the decreasing regime M >= b',
  explicit finite sum below) and the M-dependent slack q+_M = (b'+M-epsbar_M)^{-1} (or the log-free drift bracket of Lemma 22).
  With Lg_corr the part-1b limits hold (G3c: Sbar'_corr sqrt(a+M) -> 0.7485, Rbar'_corr sqrt(a+M) -> 1.0753 at M = 10^13).
Gates:  G1 exact identities (sympy: the first-order coefficient of 1/q' - 1/q - 1; the antiderivatives of the log integrals;
           H_m = psi difference); G2 constants (gamma2; the Euler-Maclaurin bound against mpmath's Hurwitz zeta at Re s = 1;
           K_eps(a) and its components); G3a Lambda^log closed form against direct summation; G3b Lg_corr dominates brute-force
           sums (incl. M < b') and is below Lg; G3c asymptotic table: old floors (A_1 n, E''' sqrt n grow) vs corrected
           (Sbar'_corr sqrt n, Rbar'_corr sqrt n converge; E^(5) (a+M) bounded, non-increasing from 10^4); G4 [NUM-A] jet-model
           orbits (rho_7 = 0): sup_m |q_m^{-1} - b~_m| <= K_eps and A_1^model within Lambda^log +- K P'_2; G5 [NUM-B] the 12 primitive
           orbits (N steps): |eps^(5)_k| <= E^(5)_k + L_tol at every slip (identity-corrected end estimate of L, as before).
Negative controls: NC1 the drift without the centre (coefficient 0) exceeds K_eps in the jet model; NC2 the centre with the wrong
           sign (+29/216) exceeds K_eps; NC3 the old Lg without its constant is NOT a majorant for M < b' (the two-regime form is needed).
Dependencies: DYAD-ALG-NF6, DYAD-THM-NF-REM (C_7, one-orbit contraction), part 1b (gamma0, c_theta, closed forms), combined tail
           and start offset (E^(4), the b-enclosure; (D5) through Delta_a and the amplitude brackets). Lemma 21-22 and Prop. 23
           need no (D5) constant.
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
abs_a05, abs_mu, abs_a32, A5, C7, c_theta, gamma0, gamma1, cQ = p1b.abs_a05, p1b.abs_mu, p1b.abs_a32, p1b.A5, p1b.C7, p1b.c_theta, p1b.gamma0, p1b.gamma1, p1b.cQ
qstar = I(256)/140625
SQ3_8 = pct.SQ3_8
# ---------------- G1: exact identities ----------------
X = sp.sqrt(3); q, Th = sp.symbols('q Theta', positive=True, real=True)
mu = -sp.Rational(1, 2) - sp.I*2*X/3; a32 = -sp.Rational(97, 432) + sp.I*197*X/324; a05 = -sp.Rational(49, 8640) - sp.I*307*X/25920
u = mu*q + a32*q**2 + a05*q**2*(sp.cos(6*Th) - sp.I*sp.sin(6*Th))                       # a05 zbar^6/q = a05 q^2 e^{-6 i Theta}
x = sp.expand(2*sp.re(u) + sp.re(u)**2 + sp.im(u)**2)
inv = sp.series(1/(q*(1 + x)), q, 0, 2).removeO()
first = sp.simplify(sp.expand(inv - 1/q - 1).coeff(q, 1))
g1a = sp.simplify(first - (-sp.Rational(29, 216) - 2*sp.re(a05*(sp.cos(6*Th) - sp.I*sp.sin(6*Th))))) == 0
g1a2 = sp.simplify(sp.expand(inv - 1/q - 1).coeff(q, 0)) == 0
xs, bs, ps = sp.symbols('x b p', positive=True)
F1 = -(sp.log(1 + xs/bs) + 1)/(bs + xs)                                                  # antiderivative of log(1+x/b)/(b+x)^2; -> 0
g1b = sp.simplify(sp.diff(F1, xs) - sp.log(1 + xs/bs)/(bs + xs)**2) == 0 and sp.limit(F1, xs, sp.oo) == 0
F2 = -sp.log(1 + xs/(2*bs))/(bs + xs) + sp.log((bs + xs)/(2*bs + xs))/bs                  # antiderivative of log(1+x/2b)/(b+x)^2; -> 0; F2(0) = -log2/b
g1c = sp.simplify(sp.diff(F2, xs) - sp.log(1 + xs/(2*bs))/(bs + xs)**2) == 0 and sp.limit(F2, xs, sp.oo) == 0 and sp.simplify(F2.subs(xs, 0) + sp.log(2)/bs) == 0
Fp = -sp.log(1 + xs/(2*bs))*(bs + xs)**(1 - ps)/(ps - 1)                                 # by parts: d/dx Fp = log(.)(b+x)^{-p} - (b+x)^{1-p}/((p-1)(2b+x))
g1p = sp.simplify(sp.diff(Fp, xs) - (sp.log(1 + xs/(2*bs))*(bs + xs)**(-ps) - (bs + xs)**(1 - ps)/((ps - 1)*(2*bs + xs)))) == 0
g1d = all(sp.simplify(sp.expand_func(sp.digamma(sp.Rational(7, 3) + m)) - sp.expand_func(sp.digamma(sp.Rational(7, 3))) - sum(1/(sp.Rational(7, 3) + j) for j in range(m))) == 0 for m in (1, 2, 5))
res["gates"]["G1_exact"] = bool(g1a and g1a2 and g1b and g1c and g1p and g1d)
res["G1"] = {"first_order_coefficient": g1a, "order_q0_vanishes": g1a2, "antiderivative_log_b": g1b, "antiderivative_log_2b_and_log2_over_b": g1c, "by_parts_general_p": g1p, "H_m_is_digamma_difference": g1d}
# ---------------- G2: constants ----------------
qq = qstar
v = A5*qq**2 + C7*qq**3                                   # |u - mu q|
delta3 = 2*C7*qq**3 + 2*abs_mu*qq*v + v**2                # |x_2 - (2 Re a32 + 2 Re(a05 e^{-6iTheta}) + |mu|^2) q^2|   (the rho_7 part is 2 C_7 q^3)
x2_abs = (2*abs_a32 + 2*abs_a05 + abs_mu**2)*qq**2 + delta3
x_abs = qq + x2_abs
R_abs = delta3/qq + qq*x_abs/(1 - x_abs) + (2*x2_abs + x2_abs**2/qq)/(1 - x_abs)
gamma2 = R_abs/qq**2                                      # every term/q^2 increases with q: the value at q* is the supremum on (0, q*]
gamma2_C7_share = 2*C7
s6 = iv.sqrt(I(1) + 36*tau**2)                            # |s|, s = 1 +- 6 i tau
def zeta_bound(xv):                                       # |zeta(s, x)| <= 1/|s-1| + (1 + |s|)/(2x)  for Re s = 1
    return 1/(6*tau) + (1 + s6)/(2*xv)
zeta_check = {}
for sgn in (+1, -1):
    s_c = mp.mpc(1, sgn*6*mp.mpf(up(tau)))
    for xv in (600, 625, 1000, 2500, 10**4, 10**6):
        ex = abs(mp.zeta(s_c, mp.mpf(xv))); bd = float(lo(zeta_bound(I(xv)))); zeta_check[f"{'+' if sgn > 0 else '-'}{xv}"] = (float(ex), bd, float(ex) <= bd)
g2z = all(v_[2] for v_ in zeta_check.values())
def P(p, b_, M_): return p1b.P(p, b_, M_)                 # sum_{m>=M} (b'+m)^{-p} <= n^{-p} + n^{1-p}/(p-1)
def Lg_corr(p, b_, M_):
    """sum_{m>=M} log(1+m/2b')(b'+m)^{-p} without the constant slack: for M >= b' the summand is decreasing (p >= 2), so
       first term + integral (G1p; 1/(2b+x) <= 1/(b+x)); for M < b' the terms up to ceil(b') are summed explicitly (intervals)"""
    p = I(p); b_ = I(b_) if not hasattr(b_, "_mpi_") else b_
    Mb = int(math.ceil(float(up(b_))))
    Mi = int(M_) if not hasattr(M_, "_mpi_") else int(up(M_))
    tot = I(0)
    if Mi < Mb:
        for m in range(Mi, Mb): tot += iv.log(1 + I(m)/(2*b_))*(b_ + m)**(-p)
        Mi = Mb
    n = b_ + Mi; L_ = iv.log(1 + I(Mi)/(2*b_))
    return tot + L_*n**(-p) + L_*n**(1 - p)/(p - 1) + n**(1 - p)/(p - 1)**2
def tailP2(bp, j): return (1 + 1/bp)/(bp + j)                 # sum_{i>=j} (b'+i)^{-2} <= (1 + 1/b')/(b'+j)
C_L = lambda bp: 1 + 2*(iv.log(I(2)) + 1/(8*bp))               # uniform constant for the log tail
def tailLg2(bp, j): return (2*iv.log(1 + j/(2*bp)) + C_L(bp))/(bp + j)   # sum_{i>=j} log(1+i/2b')(b'+i)^{-2} <= [2 log(1+j/2b') + C_L]/(b'+j)
def K_eps(a):
    """Lemma 22 constant: sup_m |q_m^{-1} - b~_m|, closed forms in a only (b' = a - Delta_a the smallest admissible b)"""
    a = I(a); env0 = p1b.envelope_new(a, 1)
    Delta_a = env0["Delta_a"]; bp = a - Delta_a; q0b = 1/bp
    sigma2 = 2*q0b + q0b**2                                               # sum_{j>=0} q_j^2 <= q_0^2 + 2 q_0 (one-orbit bound)
    kappa = env0["kappa"]
    e_const = gamma0*q0b + gamma1*sigma2
    Lam_A1 = lambda M_: (e_const*tailP2(bp, M_) + 2*gamma0*tailLg2(bp, M_))/(1 - kappa)   # >= sum_{j>=M} |q_j - 1/(b+j)|
    Lam_iso = Lam_A1(I(0))
    cA = e_const*(1 + 1/bp)/(1 - kappa); cB = 4*gamma0/(1 - kappa); cC = 2*gamma0*C_L(bp)/(1 - kappa)   # Lam_A1(j) <= [cA + cC + cB log(1+j/2b')]/(b'+j)
    S_1 = 1/bp**2 + 1/bp                                                 # sum_j (b'+j)^{-2}
    S_log = iv.log(I(2))/bp + 1/(8*bp**2)                                # sum_j log(1+j/2b')/(b'+j)^2  (G1c + sup-summand slack <= 1/(8b'^2))
    phase_sum = 6*(tau*((cA + cC)*S_1 + cB*S_log) + tau*S_1 + c_theta*(1 + 1/bp)/(1 - kappa)**2*S_1)
    Omega = 2*zeta_bound(bp) + Lam_iso + phase_sum
    K = C_ISO*Lam_iso + 2*abs_a05*Omega + gamma2*sigma2
    return {"K": K, "Lam_iso": Lam_iso, "Omega": Omega, "zeta_part": 2*zeta_bound(bp), "phase_sum": phase_sum, "Sigma20": sigma2, "gamma2_part": gamma2*sigma2,
            "osc_part": 2*abs_a05*Omega, "iso_part": C_ISO*Lam_iso, "bp": bp, "kappa": kappa, "Delta_a": Delta_a}
Ktab = {str(a): {k: f(v_) for k, v_ in K_eps(a).items()} for a in (625, 1000, 2500)}
res["G2_constants"] = {"gamma2": f(gamma2), "gamma2_C7_share": f(gamma2_C7_share), "|s|": f(s6), "zeta_bound_vs_mpmath": zeta_check, "K_eps": Ktab, "gamma0_old": f(gamma0), "2|a05|": f(2*abs_a05), "29/216": f(C_ISO)}
res["gates"]["G2_constants"] = bool(g2z and up(gamma2) < 250 and all(Ktab[a]["K"] < 1 for a in Ktab))
# ---------------- Lambda^log (interval in b), the drift bracket, P'_2, the corrected ref_d ----------------
def H_bracket(b_, m):
    """H_m(b) = psi(b+m) - psi(b), enclosed by log x - 1/x < psi(x) < log x - 1/(2x)"""
    if m == 0: return I(0)
    n = b_ + m
    return iv.mpf([lo(iv.log(n/b_) - 1/n + 1/(2*b_)), up(iv.log(n/b_) - 1/(2*n) + 1/b_)])
def Lambda_log(b_, M, J=None):
    """sum_{m>=M} (1/b~_m - 1/(b+m)) = sum C H_m/(n b~_m): explicit terms for m < M+J (dependency-free form), two-sided closed-form tail"""
    b_ = I(b_) if not hasattr(b_, "_mpi_") else b_
    J = J or max(2000, 2*int(up(b_)) + 2)
    assert M + J >= 2*up(b_), "tail start must be beyond 2b for the monotone tail bounds"
    tot = I(0)
    for m in range(M, M + J):
        n = b_ + m; H = H_bracket(b_, m)
        tot += C_ISO*H/(n*(n - C_ISO*H))
    Mt = M + J; n0 = b_ + Mt
    Hup = iv.log(n0/b_) + 1/b_; kappa2 = C_ISO*(iv.exp(I(-1)) + 1/b_)/b_               # sup_m C(log(n/b)+1/b)/n <= C(1/e + 1/b)/b
    tail_up = C_ISO/(1 - kappa2)*(Hup/n0**2 + (iv.log(n0/b_) + 1 + 1/b_)/n0)            # first term + int (G1b); summand decreasing for n > e^{1/2} b
    tail_lo = C_ISO*((iv.log(n0/b_) + 1)/n0 - 1/(2*n0**2))                             # int_{Mt}^inf (log(x/b) - 1/x)/x^2 (G1b); summand decreasing for n >= 2b
    return iv.mpf([lo(tot + tail_lo), up(tot + tail_up)])
def q_bracket(a, bw, M):
    """log-free bracket of q_M^{-1} from Lemma 22: b~_M(b) - K <= q_M^{-1} <= b~_M(b) + K over b in [b-, b+]"""
    K = K_eps(a)["K"]; b_ = iv.mpf([bw[0], bw[1]]); n = b_ + M
    bt = n - C_ISO*H_bracket(b_, M)
    return lo(bt) - up(K), up(bt) + up(K)
def P2prime(a, M):
    """closed-form majorant of sum_{m>=M} 1/(q_m^{-1} b~_m): q_m^{-1} >= b'+m-epsbar_m (part 1b), b~_m >= b'+m - C(log(1+m/b')+1/b')"""
    a = I(a); env = p1b.envelope_new(a, M); bp = a - env["Delta_a"]
    kappa = env["kappa"]; kap2 = C_ISO*(iv.exp(I(-1)) + 1/bp)/bp
    return P(I(2), bp, I(M))/((1 - kappa)*(1 - kap2))
def ref_d_new(a, bw, M):
    inv_lo, inv_hi = q_bracket(a, bw, M); n = I(a) + M
    qp = 1/I(inv_lo); qm = 1/I(inv_hi)
    return SQ3_8*I(max(up(iv.sqrt(qp) - n**(-I(1)/2)), up(n**(-I(1)/2) - iv.sqrt(qm))))
def E5_terms(a, M, r, bw, E4_iv, Ka):
    """E^(5) = E^(4) - tau A_1 - ref_d^old + tau half(Lambda^log) + tau K P'_2 + ref_d^new; returns (E5, mid Lambda, pieces)"""
    c3 = pct.combined(a, M, r); tA1 = tau*p1b.envelope_new(a, M)["A1"]
    Lam = Lambda_log(iv.mpf([bw[0], bw[1]]), M)
    mid = (lo(Lam) + up(Lam))/2; half = (up(Lam) - lo(Lam))/2
    rdn = ref_d_new(a, bw, M); kp = tau*Ka*P2prime(a, M)
    E5 = E4_iv - tA1 - c3["ref_d"] + tau*half + kp + rdn
    return E5, mid, {"tauA1_old": f(tA1), "ref_d_old": f(c3["ref_d"]), "tau_halfLam": f(tau*half), "tau_K_P2": f(kp), "ref_d_new": f(rdn), "Lam_mid": float(mid)}
# ---------------- G3a: Lambda^log closed form vs direct summation (fixed b) ----------------
def Lambda_log_direct(bf, M, N=3_000_000):
    m = np.arange(M, N, dtype=np.float64); n = bf + m
    psi_b = float(mp.digamma(bf)); psi_n = np.log(n) - 1/(2*n) - 1/(12*n**2) + 1/(120*n**4)   # |error| < 1/(252 n^6) for n >= 600
    Hm = psi_n - psi_b; bt = n - (29/216)*Hm
    return float(np.sum(1/bt - 1/n))
g3a = True; lam_checks = {}
for a, M in ((625, 1000), (2500, 1000), (625, 100000)):
    cf = Lambda_log(I(a), M); direct = Lambda_log_direct(float(a), M)
    ok = lo(cf) - 1e-6 <= direct and direct <= up(cf) + 1e-6 and up(cf) <= 1.2*lo(cf) + 1e-9
    g3a &= ok; lam_checks[f"a={a},M={M}"] = {"closed": [f(lo(cf)), f(up(cf))], "direct": direct, "ok": bool(ok)}
res["G3a_Lambda_log"] = lam_checks
# ---------------- G3b: Lg_corr dominates brute force, is below Lg, and the old Lg without its constant fails for M < b' (NC3) ----------------
g3b = True; nc3 = False; lg_checks = {}
for a in (625, 2500):
    bp = I(a) - p1b.envelope_new(a, 1)["Delta_a"]; bpf = float(lo(bp))
    for M in (0, 100, 1000, 10000, 1000000):
        for p in (2, 2.5, 3):
            N = 5_000_000; m = np.arange(M, N, dtype=np.float64); n = bpf + m
            brute = float(np.sum(np.log1p(m/(2*bpf))*n**(-p))) + float(lo(Lg_corr(p, bp, N)))      # tail beyond N by the (valid, decreasing-regime) closed form
            cf = Lg_corr(p, bp, M); old = p1b.Lg(I(p), bp, I(M))
            ok = float(lo(cf))*(1 + 1e-12) >= brute and up(cf) <= up(old)
            g3b &= ok; lg_checks[f"a={a},M={M},p={p}"] = {"Lg_corr": [f(lo(cf)), f(up(cf))], "brute": brute, "Lg_old": f(old), "ok": bool(ok)}
            if M < bpf and up(old - bp**(-I(p))) < brute: nc3 = True
res["G3b_Lg_corr"] = lg_checks; res["NC3"] = {"old_Lg_without_constant_fails_below_bprime": bool(nc3)}
# ---------------- G3c: asymptotic table (old floors vs corrected / centred) ----------------
def with_Lg_corr(fun, *args):
    old = p1b.Lg
    try:
        p1b.Lg = lambda p, b_, M_: Lg_corr(p, b_, M_)
        return fun(*args)
    finally:
        p1b.Lg = old
asym = {}; g3c = True; rising = {}
for a in (625, 2500):
    asym[str(a)] = {}; Ka = K_eps(a)["K"]; prev = None; rise = False
    bpf = float(lo(I(a) - p1b.envelope_new(a, 1)["Delta_a"]))
    for M in (10**3, 10**4, 10**5, 10**6, 10**7, 10**9, 10**11, 10**13):
        n = a + M; e_old = p1b.envelope_new(a, M); e_cor = with_Lg_corr(p1b.envelope_new, a, M)
        c3 = pct.combined(a, M, 5)
        om = iv.mpf([-1, 1]); bw = (mp.mpf(a) - 1, mp.mpf(a) + 1)                       # illustrative b-range [a-1, a+1]
        prod = om*pso.S_bracket(a, M, bw); half0 = (up(prod) - lo(prod))/2
        E4 = c3["E3"] - c3["tauA0"] + tau*half0
        E5, mid, pieces = E5_terms(a, M, 5, bw, E4, Ka)
        row = {"A1_old*n": f(e_old["A1"])*n, "A1_corr*n": f(e_cor["A1"])*n, "A1_corr*n/log(1+M/b')": f(e_cor["A1"])*n/math.log(1 + M/bpf),
               "Sbar_old*sqrt": f(e_old["Sbar"])*math.sqrt(n), "Sbar_corr*sqrt": f(e_cor["Sbar"])*math.sqrt(n), "Rbar_old*sqrt": f(e_old["Rbar"])*math.sqrt(n), "Rbar_corr*sqrt": f(e_cor["Rbar"])*math.sqrt(n),
               "E3*sqrt": f(c3["E3"])*math.sqrt(n), "E3*n": f(c3["E3"])*n, "ref_d_old*sqrt": f(c3["ref_d"])*math.sqrt(n), "E4*n": f(E4)*n, "E5*n": f(E5)*n,
               **{k: v_*n for k, v_ in pieces.items() if k != "Lam_mid"}, "Lam_mid*n": pieces["Lam_mid"]*n}
        if M >= 10**4:
            if prev is not None and row["E5*n"] > prev*(1 + 1e-6): rise = True
            prev = row["E5*n"]
        asym[str(a)][str(M)] = row
    rising[str(a)] = rise
    last = asym[str(a)]["10000000000000"]
    g3c &= (not rise) and abs(last["Sbar_corr*sqrt"] - 0.74850) < 0.01 and abs(last["Rbar_corr*sqrt"] - 1.0753) < 0.01 and last["E5*n"] < 60
    g3c &= last["A1_old*n"] > 1000 and last["E3*sqrt"] > 1                                   # the old floors are real
res["G3c_asymptotics"] = asym; res["G3c_E5n_rises_from_1e4"] = rising
res["gates"]["G3_closed_forms_and_asymptotics"] = bool(g3a and g3b and g3c)
# ---------------- G4 [NUM-A]: jet-model orbits ----------------
MU = complex(-0.5, -2*math.sqrt(3)/3); A32 = complex(-97/432, 197*math.sqrt(3)/324); A05 = complex(-49/8640, -307*math.sqrt(3)/25920)
def jet_orbit(b, th0, N, c_iso=29/216, M_A1=1000):
    z = complex(math.sqrt(1/b)*math.cos(th0), math.sqrt(1/b)*math.sin(th0)); drift_max = 0.0; drifts = []; A1 = 0.0
    Hm = 0.0
    for m in range(N + 1):
        qm = abs(z)**2
        d = 1/qm - (b + m - c_iso*Hm)
        drift_max = max(drift_max, abs(d))
        if m % 10000 == 0: drifts.append((m, float(d)))
        if m >= M_A1: A1 += qm - 1/(b + m)
        Hm += 1/(b + m)
        uu = MU*qm + A32*qm*qm + A05*(z.conjugate()**6)/qm
        z = z*(1 + uu)
    return drift_max, drifts, A1
g4 = True; jet = {}; NJ = 300_000
for b in (625, 1000, 2500):
    Kb = Ktab[str(b)]["K"]
    Lam = Lambda_log(I(b), 1000); P2p = f(P2prime(b, 1000)); tailN = f(Lambda_log(I(b), NJ))   # A1^model is truncated at N: compare with Lambda^log_M - Lambda^log_N +- K P'_2
    for th0 in (0.3, 1.7, 3.9, 5.1):
        dm, dr, A1m = jet_orbit(b, th0, NJ)
        eps_old = f(gamma0)*(1/b) + f(gamma1)*(2/b + 1/b**2) + 2*f(gamma0)*math.log(1 + NJ/(2*b))
        okd = dm <= Kb; okA = (f(lo(Lam)) - tailN - Kb*P2p <= A1m <= f(up(Lam)) + Kb*P2p); g4 &= okd and okA
        jet[f"b={b},th={th0}"] = {"sup_drift": dm, "K_eps": Kb, "ratio": dm/Kb, "old_epsbar_at_N": eps_old, "A1_model_M1000_to_N": A1m, "Lambda_log_M1000": [f(lo(Lam)), f(up(Lam))], "Lambda_log_N": tailN, "K_P2prime": Kb*P2p, "ok": bool(okd and okA), "samples": dr[::6]}
res["G4_jet_model"] = jet; res["gates"]["G4_NUM_jet_drift_within_K_and_A1_within_identity"] = bool(g4)
nc1 = True; nc2 = True
for b in (625, 2500):
    nc1 &= jet_orbit(b, 0.3, NJ, c_iso=0.0)[0] > Ktab[str(b)]["K"]
    nc2 &= jet_orbit(b, 0.3, NJ, c_iso=-29/216)[0] > Ktab[str(b)]["K"]
res["NC1"] = {"uncentred_drift_exceeds_K": bool(nc1)}; res["NC2"] = {"wrong_sign_drift_exceeds_K": bool(nc2)}
# ---------------- G5 [NUM-B]: primitive orbits ----------------
TAU = float(up(tau))
def centred5(a, n0, slips):
    hist, cfun, Efun, arcW, arcT, D0, Delta_a, omega, Tarc = pso.centred(a, n0, slips)
    bw = (mp.mpf(a) - omega[1], mp.mpf(a) - omega[0]); Ka = K_eps(a)["K"]
    sh5 = {}; en5 = {}; pieces = {}
    for (k, M, r) in slips:
        E5, mid, pc = E5_terms(a, M, r, bw, Efun(a, M, r), Ka)
        sh5[M] = -tau*I(mid); en5[M] = iv.mpf([0, up(E5)]); pieces[M] = pc
    cfun5 = lambda a_, M, r, c=cfun, s=sh5: c(a_, M, r) + s[M]
    Efun5 = lambda a_, M, r, e=en5: e[M]
    return cfun, Efun, cfun5, Efun5, bw, Ka, pieces
if __name__ == "__main__":
    outp = sys.argv[1] if len(sys.argv) > 1 else "a1c_drift_centering_cert.json"
    N = int(sys.argv[2]) if len(sys.argv) > 2 else 1_800_000
    Q0s = [1/625]*4 + [1/1000]*4 + [1/2500]*4; ths = [0.3, 1.7, 3.9, 5.1]*3
    anc, hist_phi, Qh, Psi = pib.simulate(Q0s, ths, N); Nb = N//6
    g5 = True; orbits = []
    for i in range(12):
        a = 1/Q0s[i]; an = anc[i]; n0 = an[0]
        slips = []; k = 0
        for j in range(1, len(an)):
            if an[j] - an[j - 1] == 7:
                k += 1; nA = an[j - 1]; M = nA//6; r = nA % 6
                if M >= 1: slips.append((k, M, r))
        cfun, Efun, cfun5, Efun5, bw, Ka, pieces = centred5(a, n0, slips)
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
            ok = abs(eps5) <= E5 + Ltol; g5 &= ok
            rows.append({"k": k, "M": M, "r": r, "eps4": eps4, "E4": E4, "eps5": eps5, "E5": E5, "ratio5_with_tol": abs(eps5)/(E5 + Ltol), "ratio5": abs(eps5)/E5, "gain_E5_vs_E4": E4/E5, "ok": bool(ok), **pieces[M]})
        orbits.append({"a": a, "theta0": ths[i], "n0": int(n0), "b_range": [fdn(bw[0]), fup(bw[1])], "K_eps": f(Ka), "L_est": L, "L_tol": Ltol, "slips": rows})
    res["gates"].update({"G5_NUM_eps5_within_E5": bool(g5), "NC1_uncentred_caught": bool(nc1), "NC2_wrong_sign_caught": bool(nc2), "NC3_old_Lg_without_constant_fails": bool(nc3)})
    gains = [s["gain_E5_vs_E4"] for o in orbits for s in o["slips"]]
    res["G5"] = {"N_steps": N, "orbits": orbits, "max_ratio5": max(s["ratio5"] for o in orbits for s in o["slips"]), "max_ratio5_with_tol": max(s["ratio5_with_tol"] for o in orbits for s in o["slips"]),
                 "min_gain": min(gains), "max_gain": max(gains), "slips_with_gain_gt_1": sum(1 for g in gains if g > 1), "n_slips": len(gains)}
    ok = all(res["gates"].values()); res["ALL_PASS"] = ok
    json.dump(res, open(outp, "w"), indent=1, default=lambda o: bool(o) if isinstance(o, np.bool_) else (float(o) if isinstance(o, (np.floating, np.integer)) else str(o)))
    for k_, v_ in res["gates"].items(): print(k_, "PASS" if v_ else "FAIL")
    print("gamma2 =", round(res["G2_constants"]["gamma2"], 3), "(C_7 share", round(res["G2_constants"]["gamma2_C7_share"], 1), ")  K_eps:", {a: round(Ktab[a]["K"], 4) for a in Ktab})
    for a in asym:
        print("a=%s:" % a)
        for M, r_ in asym[a].items():
            print("   M=%-14s A1_old*n=%9.2f A1_corr*n=%7.3f  Sbar_old*sqrt=%.4f Sbar_corr*sqrt=%.4f  Rbar_corr*sqrt=%.4f  E3*sqrt=%.2e  E4*n=%.2f  E5*n=%.2f  (K P2*n=%.2f, refd_new*n=%.3f, refd_old*n=%.3f)" % (M, r_["A1_old*n"], r_["A1_corr*n"], r_["Sbar_old*sqrt"], r_["Sbar_corr*sqrt"], r_["Rbar_corr*sqrt"], r_["E3*sqrt"], r_["E4*n"], r_["E5*n"], r_["tau_K_P2"], r_["ref_d_new"], r_["ref_d_old"]))
    for o in orbits:
        print("a=%4d th=%.1f n0=%d: b in [%.2f, %.2f] K=%.4f | " % (o["a"], o["theta0"], o["n0"], o["b_range"][0], o["b_range"][1], o["K_eps"]) + " ".join("k%d(M=%d,r=%d) e5=%+.1e/E5=%.1e (E4=%.1e x%.2f)" % (s["k"], s["M"], s["r"], s["eps5"], s["E5"], s["E4"], s["gain_E5_vs_E4"]) for s in o["slips"]))
    print("gains E4/E5: min %.2f max %.2f; slips with gain > 1: %d/%d" % (res["G5"]["min_gain"], res["G5"]["max_gain"], res["G5"]["slips_with_gain_gt_1"], res["G5"]["n_slips"]))
    print("ALL PASS" if ok else "FAILURES"); sys.exit(0 if ok else 1)
