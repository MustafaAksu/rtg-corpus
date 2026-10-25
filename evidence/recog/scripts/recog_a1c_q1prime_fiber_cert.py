#!/usr/bin/env python3
"""A1c part 3 -- Q1' (injectivity of the record map): bounded analytic study. Certificate for the constants of Prop. 7
(C^1 regularity of the asymptotic phase in the normalized chart, nonvanishing angular derivative) and [NUM] illustrations.

Chart (DYAD-ALG-NF6 / DYAD-THM-NF-REM row A): z = r e^{i Theta}, q = r^2, lambda = log q;  hat F(z) = z (1 + u),  u = mu q + v,
    v = a32 q^2 + a05 zbar^6/q + rho7,  rho7 = R_7(z)/z,  |R_7| <= C_7 |z|^7,  ||D R_7||_2 <= C_D |z|^6   (C_7 = 100, C_D = 1000).
Polar step:  lambda' = lambda + 2 Re Log(1+u),  Theta' = Theta + Im Log(1+u).   Psi = Theta - tau lambda,   Psi_inf = lim Psi(z_m).
    sigma(z) := Psi(hat F z) - Psi(z) = Im[(1 - 2 i tau) Log(1+u)];   (1 - 2 i tau) mu = -19/6 (real)  =>  sigma = O(q^2)  and
    Psi_inf = Psi(z_0) + sum_m sigma(z_m).
Derivatives (polar; d_lambda f = (1/2) Df[z], d_Theta f = Df[i z]):
    |d_lambda v| <= vl := 2 A5 q^2 + (C_D + C_7) q^3 / 2,     |d_Theta v| <= vt := 6 |a05| q^2 + (C_D + C_7) q^3,
    Jacobian J = I + [[2 Re A, 2 Re B], [Im A, Im B]],  A = d_lambda u/(1+u),  B = d_Theta u/(1+u):
        J11 = 1 - q + e11, |e11| <= 2 eA;  |J12| <= 2 eB;  J21 = -tau q + e21, |e21| <= eA;  |J22 - 1| <= eB,
        eA = (|mu| q ubar + vl)/(1 - ubar),  eB = vt/(1 - ubar);     alpha := 2 eA / q^2,  beta := 2 eB / q^2  (sup over q <= q*).
    |d_lambda sigma| <= (19/6) q (tau q + vbar)/(1 - ubar)^2 + sqrt(1+4 tau^2) vl/(1 - ubar) =: cSL q^2,   |d_Theta sigma| <= sqrt(1+4tau^2) vt/(1-ubar) =: cST q^2.
Propagation of w_m = d_xi (lambda_m, Theta_m) = (p_m, t_m), w_{m+1} = J(z_m) w_m, for xi = Theta_0 (w_0 = (0,1)):
    |p_m| <= beta T e^{alpha S2} sum_{j<m} q_j^2 (b+j+1+epsbar_m)/(b+m)  <= C_p T (1 + Lam(m))/(b+m),   T = sup |t_m| <= 1/(1 - Xi),
    Xi = sum_j [(tau q_j + alpha q_j^2/2) C_p (1+Lam(j))/(b+j) + beta q_j^2/2]  (must be < 1),
    |d_{Theta_0} Psi_inf - 1| <= sum_m (cSL q_m^2 |p_m| + cST q_m^2 |t_m|) <= cPsi q_0   (explicit; evaluated at q_0 = q* = 256/140625, all terms increasing in q_0).
    Inputs for q_m: q_m <= 1/((1-kappa)(b+m)), sum q_m^2 <= 2 q_0 + q_0^2, q_m^{-1} = b + m + eps_m with |eps_m| <= epsbar_m (part 1b Lemma 2).
Gates: G1 exact identities (sympy): (1-2i tau) mu = -19/6; first-order cancellation of sigma; G2 the constants and the final bound cPsi q* < 1
       (interval arithmetic); G3 [NUM] finite-difference d_theta Psi_{W,inf} at fixed Q_0 on 12 starts (illustration, ~ 1 +- O(sqrt Q_0));
       G4 [NUM] level-curve pairs (same Psi_{W,inf} by shooting, Delta a in {0.05, 0.2, 1, 5, -0.2, -1}): the first differing return must equal the
       one predicted by the signed heuristic (o'_j ~ o_j - tau Delta a/(a+M_j): Delta a > 0 flips the first NON-slip return with
       crit_j := |o_j - Delta_j| (a+M_j)/tau < Delta a; Delta a < 0 flips the first SLIP return with crit_j < |Delta a|); slip slack statistics.
Negative controls: NC1 flipped Im mu breaks the -19/6 identity; NC2 a pair NOT on the same level curve (Psi offset 0.01, same Delta a = 0.05)
       separates at an early return while the matched pair does not (within the horizon).
usage: python -I recog_a1c_q1prime_fiber_cert.py [OUT_JSON] [N_STEPS]
"""
import json, math, sys
import numpy as np
import mpmath as mp
from mpmath import iv
import sympy as sp
mp.mp.dps = 40; iv.dps = 40
I = lambda x: iv.mpf(x)
def up(x): return mp.mpf(x._mpi_[1]) if hasattr(x, "_mpi_") else mp.mpf(x)
def lo(x): return mp.mpf(x._mpi_[0]) if hasattr(x, "_mpi_") else mp.mpf(x)
def f(x): return float(up(x))
res = {"gates": {}}
s3 = iv.sqrt(I(3)); tau = 2*s3/3
mu_re, mu_im = I(-1)/2, -2*s3/3
abs_mu = iv.sqrt(mu_re**2 + mu_im**2)
abs_a32 = iv.sqrt((I(97)/432)**2 + (197*s3/324)**2); abs_a05 = iv.sqrt((I(49)/8640)**2 + (307*s3/25920)**2); A5 = abs_a32 + abs_a05
C7, CD = I(100), I(1000)
norm = iv.sqrt(1 + 4*tau**2)
qstar = I(256)/140625
# ---------------- G1 ----------------
X = sp.sqrt(3); tau_s = 2*X/3; mu_s = -sp.Rational(1, 2) - sp.I*2*X/3
g1a = sp.simplify((1 - 2*sp.I*tau_s)*mu_s + sp.Rational(19, 6)) == 0
us = sp.symbols('u'); q_s = sp.symbols('q', positive=True)
# sigma to first order in u: Im[(1-2i tau)(mu q)] = 0
g1b = sp.simplify(sp.im(sp.expand((1 - 2*sp.I*tau_s)*mu_s*q_s))) == 0
res["gates"]["G1_exact"] = bool(g1a and g1b)
# ---------------- G2 constants ----------------
q = qstar
vbar = A5*q**2 + C7*q**3; ubar = abs_mu*q + vbar
vl = 2*A5*q**2 + (CD + C7)*q**3/2; vt = 6*abs_a05*q**2 + (CD + C7)*q**3
eA = (abs_mu*q*ubar + vl)/(1 - ubar); eB = vt/(1 - ubar)
alpha = 2*eA/q**2; beta = 2*eB/q**2
cSL = ((I(19)/6)*q*(tau*q + vbar)/(1 - ubar)**2 + norm*vl/(1 - ubar))/q**2
cST = norm*vt/(1 - ubar)/q**2
# orbit sums at q_0 = q* (b = 1/q*), worst case; kappa and epsbar as in part 1b Lemma 2 (gamma0, gamma1 recomputed here)
g0 = I(29)/216 + 2*abs_a05
delta3 = 2*C7*q**3 + 2*abs_mu*q*vbar + vbar**2; delta2p = abs_mu**2 + 2*(I(-97)/432) + 2*abs_a05; delta_b = delta2p*q**2 + delta3
gamma0 = g0/(1 - q - delta_b); gamma1 = (delta3/q + delta_b)/(q**2*(1 - q - delta_b))
b = 1/q; q0 = q
sigma2 = 2*q0 + q0**2; e_const = gamma0*q0 + gamma1*sigma2
kappa = e_const/b + gamma0/(iv.sqrt(I(2))*b)
S2 = 2*q0 + q0**2                                   # sum q_m^2 (from q_m <= 1/(b + m/2))
# Lam(m) = sum_{j<m} 1/(b+j) <= q0 + log(1 + m/b); epsbar_m <= e_const + 2 gamma0 log(1 + m/(2b)) <= e_const + 2 gamma0 Lam(m)
# closed forms: P_p = sum_{m>=0} (b+m)^{-p} <= b^{-p} + b^{1-p}/(p-1);  LG_p = sum log(1+m/b) (b+m)^{-p} <= b^{-p} + b^{1-p}/(p-1)^2
P = lambda p: b**(-p) + b**(1 - p)/(p - 1)
LG = lambda p: 2*b**(-p) + b**(1 - p)/(p - 1)**2          # 2 sup g + integral, g = log(1+x/b)(b+x)^{-p} <= b^{-p}
ONEPLUSLAM = lambda p: (1 + q0)*P(p) + LG(p)       # sum (1 + Lam(m)) (b+m)^{-p}
# C_p: |p_m| <= beta T e^{alpha S2} (1-kappa)^{-2} [ (1 + 1/b) Lam(m) + (e_const + 2 gamma0 Lam(m) + 1) (1/b^2 + 1/b) ] / (b+m)  <= C_p T (1 + Lam(m))/(b+m)
Cp = beta*iv.exp(alpha*S2)/(1 - kappa)**2*((1 + 1/b) + (e_const + 2*gamma0 + 1)*(1/b**2 + 1/b))
Xi = (tau*Cp/(1 - kappa))*ONEPLUSLAM(I(2)) + (alpha*Cp/(2*(1 - kappa)**2))*ONEPLUSLAM(I(3)) + beta/2*S2
T = 1/(1 - Xi)
cPsi_q0 = T*(cSL*Cp*ONEPLUSLAM(I(3))/(1 - kappa)**2 + cST*S2)      # bound on |d_{Theta_0} Psi_inf - 1| at q_0 = q*
# lambda-direction (w_0 = (1,0)): |p_m| <= e^{alpha S2} (b + 1 + epsbar_m)/(b+m) + (feedback), |t_m| bounded: report the leading bound only
Tl = tau*iv.exp(alpha*S2)/(1 - kappa)*((b + 1)*P(I(2)) + (e_const + 1)*P(I(2)) + 2*gamma0*LG(I(2)))     # sum tau q_j |p_j| (leading)
res["G2_constants"] = {k: f(v) for k, v in {"alpha": alpha, "beta": beta, "cSL": cSL, "cST": cST, "gamma0": gamma0, "gamma1": gamma1, "kappa": kappa, "C_p": Cp, "Xi": Xi, "T": T,
                       "bound_|dTheta Psi_inf - 1|_at_q*": cPsi_q0, "cPsi(=bound/q*)": cPsi_q0/q, "lambda_direction_t_bound": Tl, "q*": q}.items()}
res["gates"]["G2_constants_and_bound"] = bool(up(Xi) < 1 and up(cPsi_q0) < mp.mpf("0.05"))
# ---------------- [NUM] machinery ----------------
TAU = float(up(tau)); OMEGA = complex(-0.5, math.sqrt(3)/2)
def simulate(Q0s, ths, N, keep_phi=False):
    """vectorised primitive orbits; returns anchors (step indices), lifted phase at anchors, phi history (optional), end Psi"""
    n = len(Q0s)
    rho = np.array([math.sqrt(Q0s[i])*math.cos(ths[i]) for i in range(n)]); eta = np.array([math.sqrt(Q0s[i])*math.sin(ths[i]) for i in range(n)])/OMEGA.imag
    rho = rho - OMEGA.real*eta; W = rho + OMEGA*eta; phi = np.angle(W).copy()
    anchors = [[] for _ in range(n)]
    hist = np.zeros((n, N + 1)) if keep_phi else None
    if keep_phi: hist[:, 0] = phi
    for step in range(1, N + 1):
        rho_n = rho - np.sin(eta); eta_n = eta + np.exp(rho) - 1 - np.sin(eta); Wn = rho_n + OMEGA*eta_n
        phi += np.angle(Wn/W)
        bev = (eta < 0) & (eta_n >= 0) & (rho > 0) & (rho_n > 0)
        for i in np.nonzero(bev)[0]: anchors[i].append(step)
        rho, eta, W = rho_n, eta_n, Wn
        if keep_phi: hist[:, step] = phi
    Mend = N//6; Psi_end = (phi - 2*math.pi*Mend) - TAU*np.log(np.abs(W)**2)
    return anchors, hist, Psi_end
def record_data(anc, hist_i, a):
    """gaps, overshoots o_j, thresholds Delta_j = 2 pi - Lambda_6(x_{n_j}), slips, normalized slacks, critical Delta a per return"""
    anc = np.array(anc); gaps = np.diff(anc)
    phi_anc = hist_i[anc]; ell = np.floor(phi_anc/(2*math.pi)); o = phi_anc - 2*math.pi*ell
    valid = anc + 6 <= hist_i.shape[0] - 1
    Lam6 = np.full(len(anc), np.nan); Lam6[valid] = hist_i[anc[valid] + 6] - phi_anc[valid]
    Delta = 2*math.pi - Lam6
    M = anc//6
    crit = np.abs(o - Delta)*(a + M)/TAU                    # heuristic critical |Delta a| for a level-curve partner to flip this return
    return gaps, o, Delta, M, crit
if __name__ == "__main__":
    outp = sys.argv[1] if len(sys.argv) > 1 else "a1c_q1prime_fiber_cert.json"
    N = int(sys.argv[2]) if len(sys.argv) > 2 else 1_800_000
    # ---- G3: finite differences of Psi_{W,inf} in theta at fixed Q_0 (12 starts) ----
    Q0s = [1/625]*4 + [1/1000]*4 + [1/2500]*4; ths = [0.3, 1.7, 3.9, 5.1]*3; h = 1e-4
    anc, _, Psi = simulate(Q0s + Q0s, ths + [t + h for t in ths], N)
    fd = [(Psi[12 + i] - Psi[i])/h for i in range(12)]
    res["G3_finite_difference_dPsi_dtheta"] = {"values": [float(v) for v in fd], "h": h, "expected": "1 + O(sqrt Q_0) (primitive angle; chart statement is exact 1 + O(q_0))"}
    res["gates"]["G3_NUM_dPsi_dtheta_near_1"] = bool(all(0.8 < v < 1.2 for v in fd))
    # ---- G4: level-curve pairs by shooting ----
    base_a, base_th = 625.0, 0.3
    das = [0.05, 0.2, 1.0, 5.0, -0.2, -1.0]
    partners_a = [base_a + d for d in das]
    th = [base_th + TAU*math.log(base_a/pa) for pa in partners_a]            # start on the level curve of Psi(z_0) ~ Theta - tau log Q
    offs = None
    for it in range(4):
        anc, hist, Psi = simulate([1/base_a] + [1/pa for pa in partners_a], [base_th] + th, N, keep_phi=(it == 3))
        mism = [Psi[1 + i] - Psi[0] for i in range(len(das))]
        if it < 3: th = [th[i] - mism[i] for i in range(len(das))]
    gb, ob, Db, Mb, critb = record_data(anc[0], hist[0], base_a)
    pairs = []
    g4 = True
    for i, d in enumerate(das):
        gp, op, Dp, Mp, critp = record_data(anc[1 + i], hist[1 + i], partners_a[i])
        L = min(len(gb), len(gp)); diff = np.nonzero(gb[:L] != gp[:L])[0]
        first = int(diff[0]) if len(diff) else None
        # signed prediction: the partner's overshoot is o'_j ~ o_j - tau Delta a/(a+M_j); for Delta a > 0 a flip needs a NON-slip return (gap 6 after j)
        # with margin o_j - Delta_j < tau Delta a/(a+M_j), i.e. crit_j < Delta a; for Delta a < 0 a SLIP return (gap 7) with Delta_j - o_j < tau |Delta a|/(a+M_j)
        side = (gb[:L] == 6) if d > 0 else (gb[:L] == 7)
        pred = np.nonzero(side & (critb[:L] < abs(d)))[0]; pred_first = int(pred[0]) if len(pred) else None
        pairs.append({"Delta_a": d, "theta_partner": th[i], "Psi_mismatch_end": float(mism[i]), "n_returns_compared": int(L), "first_differing_return": first,
                      "M_at_first_difference": int(Mb[first]) if first is not None else None, "crit_at_first_difference": float(critb[first]) if first is not None else None,
                      "predicted_first_return(signed rule)": pred_first, "prediction_exact": first == pred_first, "min_crit_over_horizon": float(np.nanmin(critb[:L]))})
        g4 &= (first == pred_first)                                   # the signed heuristic must predict the first differing return exactly
    # slip slack statistics (base orbit and the 12 starts of G3 are different runs; use base + partners)
    slips_b = np.nonzero(gb == 7)[0]
    slacks = [(int(j), int(Mb[j]), float((Db[j] - ob[j])/Db[j]), float(critb[j])) for j in slips_b if not np.isnan(Db[j])]
    res["G4_level_curve_pairs"] = {"base": {"a": base_a, "theta": base_th, "slips_(j,M,normalized_slack,crit)": slacks}, "pairs": pairs,
                                   "note": "crit_j = |o_j - Delta_j| (a+M_j)/tau; a level-curve partner flips return j iff crit_j < |Delta a| on the matching side (gap 6 for Delta a > 0, gap 7 for Delta a < 0)"}
    res["gates"]["G4_NUM_separation_consistent"] = bool(g4)
    # ---- NC ----
    nc1 = not (sp.simplify((1 - 2*sp.I*tau_s)*sp.conjugate(mu_s) + sp.Rational(19, 6)) == 0)
    anc2, hist2, Psi2 = simulate([1/base_a, 1/partners_a[0], 1/partners_a[0]], [base_th, th[0], th[0] + 0.01], N, keep_phi=True)
    gb2 = np.diff(np.array(anc2[0])); gm = np.diff(np.array(anc2[1])); go = np.diff(np.array(anc2[2]))
    L = min(len(gb2), len(gm), len(go)); dm = np.nonzero(gb2[:L] != gm[:L])[0]; do = np.nonzero(gb2[:L] != go[:L])[0]
    fm = int(dm[0]) if len(dm) else None; fo = int(do[0]) if len(do) else None
    nc2 = fo is not None and (fm is None or fo < fm)
    res["NC2"] = {"matched_pair_first_difference": fm, "offset_pair_first_difference": fo, "returns_compared": int(L)}
    res["gates"]["NC1_wrong_mu_caught"] = bool(nc1); res["gates"]["NC2_unmatched_pair_separates_earlier"] = bool(nc2)
    res["N_steps"] = N
    ok = all(res["gates"].values()); res["ALL_PASS"] = ok
    json.dump(res, open(outp, "w"), indent=1, default=lambda o: bool(o) if isinstance(o, np.bool_) else (float(o) if isinstance(o, (np.floating, np.integer)) else str(o)))
    for k, v in res["gates"].items(): print(k, "PASS" if v else "FAIL")
    print("constants:", res["G2_constants"])
    print("finite differences dPsi/dtheta:", [round(v, 4) for v in fd])
    print("base slips (j, M, slack, crit):", slacks)
    for p in pairs: print(p)
    print("NC2:", res["NC2"])
    print("ALL PASS" if ok else "FAILURES"); sys.exit(0 if ok else 1)
