#!/usr/bin/env python3
"""A1c -- combined tail tau S^tail - R^tail: the leading harmonics cancel to a single boundary term (telescoping), and the known-a
envelope loses its M^{-1/2} order.

Exact identity (Prop. 13). With the Dyadic decomposition of the block remainder under branch (B),
    r_m = S_Theta(z_m) + tau D_Q(z_m) + [Arg(J(z_m)/z_m) + tau q_m] + Arg(hat F(z_m)/J(z_m)),      S_Theta(z) = D_Theta(hat F z) - D_Theta(z),
and Q_m = q_m + D_Q(z_m), the D_Q terms cancel in tau (Q_m - 1/(a+m)) - r_m, and sum_{m>=M} S_Theta(z_m) = -D_Theta(z_M) (telescoping, D_Theta -> 0):
    tau S^tail_M - R^tail_M = tau A_M + D_Theta(z_M) - Sigma^J_M - Sigma^7_M,
    A_M = sum_{m>=M} (q_m - 1/(a+m))  (part 1b: |A_M| <= A0 + A1 = O(1/M)),   |Sigma^J_M| <= c_J^R sum q_m^2,   |Sigma^7_M| <= c_7^R sum q_m^3.
Leading harmonics: separately, tau S and R carry tau phi_k and lambda_k; combined, lambda_k - tau phi_k = ell_k (the harmonics of L_Theta),
    |ell_1|/|s_1 - 1| + |ell_3|/|s_3 - 1| = 1/sqrt12 + 1/12 = 0.3720 (vs 1.9396 separately) -- and these are exactly the harmonic amplitudes of
    d(Theta) := D_{Theta,1}/r = Im(h_2/z)/r, because L_Theta = D D_{Theta,1}[mu q z] is the spiral derivative of D_{Theta,1}: the whole oscillatory
    tail collapses to the single term D_Theta(z_M) = sqrt(q_M) d(Theta_M) + O(q_M), |D_Theta - D_{Theta,1}| <= c_1 q (DYAD-THM-OPEN3-SPIRAL-REM, c_1 = 0.261).
Known phase (Cor. 14). At a slip block, the block base point has primitive angle -r pi/3 + O(sqrt Q) (in-block cell), and d(-r pi/3) = -sqrt3/8 for
    r = 0,1,2 and +sqrt3/8 for r = 3,4,5. Combined with kappa(r) = (0,0,0,sqrt3/4,sqrt3/4,sqrt3/4): kappa(r) - d(-r pi/3) = sqrt3/8 for EVERY r.
    Sharpened schedule:  tau psi(a+M_k) - (k-1) pi/3 + (sqrt3/8)(a+M_k)^{-1/2} + (tau/2)(a+M_k)^{-1} = L + eps'''_k,   |eps'''_k| <= E'''(a, M_k, r_k),
    E''' = xi_max + rho_P + kappa ref_kappa + tau (A0 + A1) + varrho_D + (sqrt3/8) ref_d + c_J^R Sigma_2 + c_7^R Sigma_3 = O((a+M)^{-1})
    (dominant term tau A0 <= tau Delta_a/(a+M) ~ 0.98 sqrt(a)/(a+M): the unknown start offset a - b).
Gates: G1 exact identities (sympy): d from h_2 equals the published D_{Theta,1}; ell_k = lambda_k - tau phi_k equals the published L_Theta harmonics;
    the six values d(-s pi/3); kappa - d = sqrt3/8 for all r; the harmonic-amplitude identities |ell_1|/|s_1-1| = 1/sqrt12, |ell_3|/|s_3-1| = 1/12.
    G2 constants (interval): sup|d|, sup|d'|, c_J^R, c_7^R; the leading constants 0.3720 vs 1.9396. G3 E''' < E'' on the tested grid.
    G4 [NUM] 12 orbits: |eps'''_k| <= E''' (+ L tolerance) at every slip, L from the run's end corrected by the identity (tolerance
    tau Delta_a/(a+N) + 3/(a+N)); G4b the same against the naive end estimate of L (tolerance adds sup|d| sqrt(q_N) + c_1 q_N); the measured
    combined tail at slip blocks vs the predicted d(-r pi/3)/sqrt(a+M) within the tau A0 range. G5 part-2 enclosures with (c''', E'''): narrower than with E''; true a inside.
    NC1 sign of the D_Theta centre flipped -> G4 fails at large M; NC2 the separate-tails constant (1.94) used as a would-be combined constant is
    contradicted by the exact harmonic identity (G1).
usage: python -I recog_a1c_combined_tail_cert.py [OUT_JSON] [N_STEPS]
"""
import json, math, sys, os, hashlib, importlib.util
import numpy as np
import mpmath as mp
from mpmath import iv
import sympy as sp
HERE = os.path.dirname(os.path.abspath(__file__))
def load(name):
    pth = os.path.join(HERE, name); spec = importlib.util.spec_from_file_location(name[:-3], pth); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m, hashlib.sha256(open(pth, "rb").read()).hexdigest()
pib, hib = load("recog_a1c_inblock_angular_cert.py")       # also loads part 1b and part 2
p1b, p2 = pib.p1b, pib.p2
I, up, lo, tau, f = p1b.I, p1b.up, p1b.lo, p1b.tau, pib.f
fup, fdn, asin_iv = p2.fup, p2.fdn, pib.asin_iv
res = {"gates": {}, "imports": {"recog_a1c_inblock_angular_cert.py": hib, **pib.res["imports"]}}
s3 = iv.sqrt(I(3)); PI = iv.pi
# ---------------- G1 exact ----------------
X = sp.sqrt(3); th = sp.symbols('Theta', real=True); r_ = sp.symbols('r', positive=True)
c20 = -sp.Rational(1, 12) - sp.I*X/12; c11 = -sp.Rational(1, 3); c02 = sp.Rational(1, 24) - sp.I*X/24
z = r_*(sp.cos(th) + sp.I*sp.sin(th)); zb = r_*(sp.cos(th) - sp.I*sp.sin(th))
h2 = c20*z**2 + c11*z*zb + c02*zb**2
d_from_h2 = sp.simplify(sp.expand(sp.im(sp.expand(h2/z)))/r_)
d_pub = -X/12*sp.cos(th) + sp.Rational(1, 4)*sp.sin(th) - X/24*sp.cos(3*th) - sp.Rational(1, 24)*sp.sin(3*th)
g1a = sp.simplify(sp.expand(sp.expand_trig(d_from_h2 - d_pub))) == 0
dvals = [sp.nsimplify(sp.simplify(d_pub.subs(th, -s*sp.pi/3))) for s in range(6)]
g1b = dvals == [-X/8, -X/8, -X/8, X/8, X/8, X/8]
kap = [0, 0, 0, X/4, X/4, X/4]
g1c = all(sp.simplify(kap[s] - dvals[s] - X/8) == 0 for s in range(6))
tau_s = 2*X/3
phi1 = -sp.Rational(5, 6) - sp.I*X/6; phi3 = sp.Rational(1, 12) + sp.I*X/12
lam1 = -49*X/72 - sp.I/24; lam3 = 23*X/144 + sp.I*sp.Rational(19, 48)
ell1 = -X/8 + sp.I*sp.Rational(7, 24); ell3 = 5*X/48 + sp.I*sp.Rational(11, 48)          # harmonics of L_Theta (published), convention Re((alpha+i beta)e^{ik Theta})
g1d = sp.simplify(lam1 - tau_s*phi1 - ell1) == 0 and sp.simplify(lam3 - tau_s*phi3 - ell3) == 0
s1 = sp.sqrt(sp.Rational(1, 4) + tau_s**2); s3_ = sp.sqrt(sp.Rational(1, 4) + 9*tau_s**2)
g1e = sp.simplify(sp.Abs(ell1)/s1 - 1/sp.sqrt(12)) == 0 and sp.simplify(sp.Abs(ell3)/s3_ - sp.Rational(1, 12)) == 0
# d's harmonic amplitudes: |(-sqrt3/12) + i(-1/4)| = 1/sqrt12,  |(-sqrt3/24) + i(1/24)| = 1/12
g1f = sp.simplify(sp.sqrt(sp.Rational(3, 144) + sp.Rational(1, 16)) - 1/sp.sqrt(12)) == 0 and sp.simplify(sp.sqrt(sp.Rational(3, 576) + sp.Rational(1, 576)) - sp.Rational(1, 12)) == 0
res["gates"]["G1_exact"] = bool(g1a and g1b and g1c and g1d and g1e and g1f)
res["G1"] = {"d_from_h2_eq_published": g1a, "d_at_phases": [str(v) for v in dvals], "kappa_minus_d_eq_sqrt3_over_8": g1c, "ell_eq_lambda_minus_tau_phi": g1d, "amplitude_identities": g1e and g1f}
# ---------------- G2 constants ----------------
d_iv = lambda t: -s3/12*iv.cos(t) + I(1)/4*iv.sin(t) - s3/24*iv.cos(3*t) - I(1)/24*iv.sin(3*t)
dp_iv = lambda t: s3/12*iv.sin(t) + I(1)/4*iv.cos(t) + s3/8*iv.sin(3*t) - I(1)/8*iv.cos(3*t)
def sup_grid(fun, L2, n=20000):
    h = 2*mp.pi/n; best = mp.mpf(0)
    for j in range(n): best = max(best, up(abs(fun(iv.mpf(j*h)))))
    return best + L2*h**2/8
SUP_D = sup_grid(d_iv, mp.mpf(1)/mp.sqrt(12) + 9*mp.mpf(1)/12); SUP_DP = sup_grid(dp_iv, mp.mpf(1)/mp.sqrt(12) + 27*mp.mpf(1)/12)
C1 = I("0.261")                                       # DYAD-THM-OPEN3-SPIRAL-REM, row A static constant |D_Theta - D_{Theta,1}| <= c_1 q
qstar = I(256)/140625
mu_re, mu_im = I(-1)/2, -2*s3/3; abs_mu = p1b.abs_mu; A5 = p1b.A5; abs_a05 = p1b.abs_a05; a32_im = 197*s3/324; C7 = I(100)
def cJ_R(q):   # |Arg(J/z) + tau q| <= cJ_R q^2 ; J/z = 1 + u_J, u_J = mu q + v5, |v5| <= A5 q^2
    uJ = abs_mu*q + A5*q**2
    main = abs(a32_im - tau/2) + abs_a05                          # Im a32 - Im(mu^2)/2 = Im a32 - tau/2, plus the 6th harmonic of a05
    return main + abs_mu*A5*q + A5**2*q**2/2 + uJ**3/(3*(1 - uJ))/q**2
def c7_R(q):   # |Arg(hat F/J)| <= c7_R q^3 ; |R_7/J| <= C7 q^3/(1 - |u_J|), |Arg(1+w)| <= |w|/(1-|w|)
    uJ = abs_mu*q + A5*q**2; w = C7*q**3/(1 - uJ)
    return C7/(1 - uJ)/(1 - w)
CJ = cJ_R(qstar); C7R = c7_R(qstar)
lead_comb = 1/iv.sqrt(I(12)) + I(1)/12; lead_sep = tau*(p1b.abs_phi1/p1b.den(1) + p1b.abs_phi3/p1b.den(3)) + p1b.abs_lam1/p1b.den(1) + p1b.abs_lam3/p1b.den(3)
res["G2_constants"] = {"sup|d|": float(SUP_D), "sup|d'|": float(SUP_DP), "c_1": f(C1), "c_J^R": f(CJ), "c_7^R": f(C7R), "lead_combined": f(lead_comb), "lead_separate": f(lead_sep), "ratio": f(lead_sep)/f(lead_comb)}
res["gates"]["G2_constants"] = bool(up(CJ) < 0.55 and up(C7R) < 102 and SUP_D < 0.38 and SUP_DP < 0.6)
SQ3_8 = s3/8
# ---------------- the envelope E''' ----------------
def combined(a, M, r):
    a = I(a); M = I(M); n = a + M
    e = p1b.envelope_new(a, M); ib = pib.inblock(a, M, r)
    Delta_a = e["Delta_a"]; bp = a - Delta_a; kap_ = e["kappa"]
    q0b = 1/bp; sigma2 = 2*q0b + q0b**2; e_const = p1b.gamma0*q0b + p1b.gamma1*sigma2; epsM = e_const + 2*p1b.gamma0*iv.log(1 + M/(2*bp))
    q_plus = 1/((1 - kap_)*(bp + M)); q_minus = 1/(a + Delta_a + M + epsM)
    Sigma2 = p1b.P(I(2), bp, M)/(1 - kap_)**2; Sigma3 = p1b.P(I(3), bp, M)/(1 - kap_)**3
    Qd = ib["Qd"]; eb = pib.ebar(Qd); alphabar = asin_iv(eb); Deltabar = tau*Qd + I("1.82")*Qd**(I(3)/2)
    Dplus = I(SUP_D)*iv.sqrt(q_plus) + C1*q_plus                                   # |D_Theta(z_M)|
    ang_err = Deltabar + int(r)*alphabar + Dplus                                    # |Theta_M - (-r pi/3)|
    varrho_D = iv.sqrt(q_plus)*I(SUP_DP)*ang_err + C1*q_plus
    ref_d = I(max(up(iv.sqrt(q_plus) - n**(-I(1)/2)), up(n**(-I(1)/2) - iv.sqrt(q_minus))))
    E3 = ib["xi_max"] + ib["rho_P"] + ib["ref_err"] + tau*(e["A0"] + e["A1"]) + varrho_D + SQ3_8*ref_d + CJ*Sigma2 + C7R*Sigma3
    return {"E3": E3, "E2": ib["E2"], "E1": ib["E1"], "tauA0": tau*e["A0"], "tauA1": tau*e["A1"], "varrho_D": varrho_D, "ref_d": SQ3_8*ref_d, "inblock": ib["xi_max"] + ib["rho_P"] + ib["ref_err"],
            "SigmaJ": CJ*Sigma2, "Sigma7": C7R*Sigma3, "q_plus": q_plus, "q_minus": q_minus}
DVAL = [-SQ3_8, -SQ3_8, -SQ3_8, SQ3_8, SQ3_8, SQ3_8]
def centre_shift(a, M, r, sign_D=+1):
    """+ (tau/2)(a+M)^{-1} + [kappa(r) - sign_D d(-r pi/3)] (a+M)^{-1/2};  sign_D = +1 is the identity, -1 the negative control"""
    a = I(a); M = I(M); n = a + M
    return tau/(2*n) + (pib.KAPPA[int(r)] - sign_D*DVAL[int(r)])*n**(-I(1)/2)
# ---------------- G3 table ----------------
table = {}; g3 = True
for a in (625, 1000, 2500):
    table[str(a)] = {}
    for M in (1000, 10000, 100000, 1000000, 10000000):
        row = {}
        for r in range(6):
            c = combined(a, M, r)
            row[str(r)] = {k: f(c[k]) for k in ("E3", "E2", "E1", "tauA0", "tauA1", "varrho_D", "ref_d", "inblock", "SigmaJ", "Sigma7")}
            row[str(r)]["gain_vs_E2"] = row[str(r)]["E2"]/row[str(r)]["E3"]; row[str(r)]["E3_times_(a+M)"] = row[str(r)]["E3"]*(a + M)
            g3 &= row[str(r)]["E3"] < row[str(r)]["E2"]
        table[str(a)][str(M)] = row
res["G3_table"] = table; res["gates"]["G3_table_E3_below_E2_on_grid"] = bool(g3)
# ---------------- [NUM] ----------------
TAU = float(up(tau)); OMEGA = complex(-0.5, math.sqrt(3)/2); SQ38 = math.sqrt(3)/8
if __name__ == "__main__":
    outp = sys.argv[1] if len(sys.argv) > 1 else "a1c_combined_tail_cert.json"
    N = int(sys.argv[2]) if len(sys.argv) > 2 else 1_800_000
    Q0s = [1/625]*4 + [1/1000]*4 + [1/2500]*4; ths = [0.3, 1.7, 3.9, 5.1]*3
    anc, hist, Qh, Psi = pib.simulate(Q0s, ths, N)
    Nb = N//6
    g4 = True; g4b = True; orbits = []; worst = 0.0; worst_nc = 0.0; worst_naive = 0.0
    for i in range(12):
        a = 1/Q0s[i]; an = anc[i]; n0 = an[0]; ell0 = math.floor(hist[i, n0]/(2*math.pi))
        # L estimate from the run's end, corrected with the identity of Prop. 13:  phi_{6N} - 2 pi N = Psi_inf - tau psi(a+N) + tau A_N + D_Theta(z_N) + O(1/N)
        # -> Psi_inf ~ phi_{6N} - 2 pi N + tau psi(a+N) - d(theta_W(N)) (a+N)^{-1/2};  residual |tau A_N| + O(1/N) <= tau Delta_a/(a+N) + 3/(a+N)  (tolerance)
        thN = hist[i, 6*Nb] % (2*math.pi)
        dN = -math.sqrt(3)/12*math.cos(thN) + 0.25*math.sin(thN) - math.sqrt(3)/24*math.cos(3*thN) - math.sin(3*thN)/24
        Psi_corr = (hist[i, 6*Nb] - 2*math.pi*Nb) + TAU*float(mp.digamma(a + Nb)) - dN/math.sqrt(a + Nb)
        L = math.pi/3*n0 - 2*math.pi*ell0 + Psi_corr
        Delta_a_f = f(p1b.envelope_new(a, 1)["Delta_a"]); Ltol = TAU*Delta_a_f/(a + Nb) + 3/(a + Nb)
        L_naive = math.pi/3*n0 - 2*math.pi*ell0 + Psi[i]
        # naive estimate Psi_W(N) = Theta_W(N) - tau log Q_N: its error carries, besides tau A_N + D_Theta(z_N), the primitive/chart amplitude ratio
        # tau log(Q_N/q_N) (|D_Q| <= c_Q q^{3/2}) and tau log(q_N (a+N)) (<= tau (Delta_a + epsbar_N)/(b'+N)); all O(N^{-1/2}) or smaller
        eN = p1b.envelope_new(a, Nb); kapN = f(eN["kappa"]); bpN = a - Delta_a_f
        qN_plus = 1/((1 - kapN)*(bpN + Nb)); sq = math.sqrt(qN_plus); cQf = f(p1b.cQ)
        epsN = f(p1b.gamma0)/bpN + f(p1b.gamma1)*(2/bpN + 1/bpN**2) + 2*f(p1b.gamma0)*math.log(1 + Nb/(2*bpN))
        Ltol_naive = float(SUP_D)*sq + 0.261*qN_plus + TAU*cQf*sq/(1 - cQf*sq) + TAU*(Delta_a_f + epsN)/(bpN + Nb) + Ltol
        # block data for the measured combined tail
        Mi = np.arange(0, Nb, dtype=np.float64); Qb = Qh[i, 0:6*Nb:6]; phib = hist[i, 0:6*Nb + 1:6]
        rm = np.diff(phib) - 2*math.pi + TAU*Qb; dev = Qb - 1/(a + Mi)
        slips = []; k = 0
        for j in range(1, len(an)):
            if an[j] - an[j - 1] == 7:
                k += 1; n_anchor = an[j - 1]; M = n_anchor//6; r = n_anchor % 6
                if M < 1: continue
                c = combined(a, M, r)
                ck = TAU*float(mp.digamma(a + M)) - (k - 1)*math.pi/3 + f(centre_shift(a, M, r)); eps3 = ck - L; E3 = f(c["E3"])
                ck_nc = TAU*float(mp.digamma(a + M)) - (k - 1)*math.pi/3 + f(centre_shift(a, M, r, sign_D=-1)); eps_nc = ck_nc - L
                ok = abs(eps3) <= E3 + Ltol; g4 &= ok
                worst = max(worst, abs(eps3)/E3); worst_nc = max(worst_nc, abs(eps_nc)/E3)
                # G4b: the same test against the NAIVE end estimate of L (no use of the identity), with the naive tolerance
                # |D_Theta(z_N)| + |tau A_N| + O(1/N) <= sup|d| sqrt(q_N^+) + c_1 q_N^+ + tau Delta_a/(a+N) + 3/(a+N)
                eps3n = ck - L_naive
                g4b_ok = abs(eps3n) <= E3 + Ltol_naive; g4b = g4b and g4b_ok
                worst_naive = max(worst_naive, abs(eps3n)/(E3 + Ltol_naive))
                comb_meas = TAU*float(np.sum(dev[M:])) - float(np.sum(rm[M:]))       # tau S^N_M - R^N_M (truncated at N; tail O(1/sqrt N) boundary term)
                pred = (-SQ38 if r <= 2 else SQ38)/math.sqrt(a + M)                      # D_Theta(z_M) ~ d(-r pi/3) sqrt(q_M); tau A0 unknown within +- tau Delta_a/(a+M)
                slips.append({"k": k, "M": M, "r": r, "eps3": eps3, "E3": E3, "ratio": abs(eps3)/E3, "E2": f(c["E2"]), "E1": f(c["E1"]), "eps_negctrl": eps_nc,
                              "combined_tail_measured": comb_meas, "D_Theta_pred": pred, "tauA0_bound": f(c["tauA0"]), "comb_minus_pred_over_tauA0bound": (comb_meas - pred)/f(c["tauA0"])})
        orbits.append({"a": a, "theta0": ths[i], "L_est_corrected": L, "L_est_naive_end": L_naive, "L_tol": Ltol, "slips": slips})
    res["gates"]["G4_NUM_eps_within_E3"] = bool(g4); res["gates"]["G4b_NUM_naive_L"] = bool(g4b)
    res["G4"] = {"orbits": orbits, "max_ratio": worst, "max_ratio_negative_control": worst_nc, "max_ratio_naive_L_incl_tol": worst_naive}
    # the measured combined tail minus the predicted D_Theta term must lie within the tau A0 bound (plus the truncation and L-free quantities): report fraction
    frac_ok = np.mean([abs(s["comb_minus_pred_over_tauA0bound"]) <= 1.5 for o in orbits for s in o["slips"]])
    res["G4"]["fraction_comb_tail_explained"] = float(frac_ok)
    res["gates"]["NC1_wrong_D_sign_fails"] = bool(worst_nc > 1.0)
    res["gates"]["NC2_separate_constant_not_combined"] = bool(up(lead_sep) > 5*up(lead_comb))     # 1.94 vs 0.372: the separate constant is not the combined one
    # ---------------- G5 part-2 enclosures with (c''', E''') ----------------
    def classify_new(a_box, slips):
        vals = [(p2.c_k(a_box, k, M) + centre_shift(a_box, M, r), combined(a_box, M, r)["E3"]) for k, M, r in slips]
        lo_lo = max(lo(c - E) for c, E in vals); hi_hi = min(up(c + E) for c, E in vals)
        lo_hi = max(up(c - E) for c, E in vals); hi_lo = min(lo(c + E) for c, E in vals)
        return ("EXCLUDED" if lo_lo > hi_hi else ("SURE" if lo_hi <= hi_lo else "UNDECIDED")), (lo_lo, hi_hi)
    p2.classify = classify_new
    old = {}
    try:
        rib = json.load(open(os.path.join(HERE, "..", "a1c_inblock", "a1c_inblock_angular_cert.json")))
        for p in rib["G5"]: old[(p["a"], p["theta0"])] = (p["width_new"], p["L_hull_new"])
    except Exception: pass
    g5 = True; part2 = []
    for i in range(12):
        a = 1/Q0s[i]; an = anc[i]; sl3 = []; sl2 = []; k = 0
        for j in range(1, len(an)):
            if an[j] - an[j - 1] == 7:
                k += 1; n_anchor = an[j - 1]; M = n_anchor//6; r = n_anchor % 6
                if M >= 1: sl3.append((k, M, r)); sl2.append((k, M))
        if len(sl2) < 2: continue
        (k1, M1), (k2, M2) = sl2[0], sl2[1]
        am, ap = p2.lemma8_interval(k1, M1, k2, M2)
        comps, inner, n_eval, und = p2.enclosure(sl3, am, ap)
        hull = [comps[0][0], comps[-1][1]] if comps else None
        Lh = [min(c[2] for c in comps), max(c[3] for c in comps)] if comps else None
        contains = any(c[0] <= a <= c[1] for c in comps)
        ow = old.get((a, ths[i]), (None, None))
        g5 &= contains and (ow[0] is None or (hull[1] - hull[0]) < ow[0])
        part2.append({"a": a, "theta0": ths[i], "slips": sl3, "a_hull": hull, "width": hull[1] - hull[0] if hull else None, "width_inblock_cell": ow[0], "L_hull": Lh, "L_hull_inblock_cell": ow[1], "inner": inner, "undecided": und, "contains_a": contains})
    res["gates"]["G5_part2_narrower"] = bool(g5); res["G5"] = part2
    res["N_steps"] = N
    ok = all(res["gates"].values()); res["ALL_PASS"] = ok
    json.dump(res, open(outp, "w"), indent=1, default=lambda o: bool(o) if isinstance(o, np.bool_) else (float(o) if isinstance(o, (np.floating, np.integer)) else str(o)))
    for k, v in res["gates"].items(): print(k, "PASS" if v else "FAIL")
    print("constants:", res["G2_constants"])
    for a, rows in table.items():
        for M, row in rows.items():
            v = row["5"]; print(f"a={a} M={M:>8}: E'''={v['E3']:.3e} (E'' {v['E2']:.3e}, x{v['gain_vs_E2']:.1f}; E' {v['E1']:.3e})  E'''(a+M)={v['E3_times_(a+M)']:.1f}  [tauA0 {v['tauA0']:.1e} tauA1 {v['tauA1']:.1e} inblock {v['inblock']:.1e} varrhoD {v['varrho_D']:.1e} refd {v['ref_d']:.1e} SigJ {v['SigmaJ']:.1e}]")
    print("NUM: max |eps'''|/E''' =", worst, " negative control (D sign flipped):", worst_nc, " naive-L ratio incl. tol:", worst_naive, " fraction of combined tails explained:", frac_ok)
    for o in orbits: print("a=%4d th=%.1f: " % (o["a"], o["theta0"]) + " ".join("k%d(M=%d,r=%d) eps=%+.1e/E=%.1e [nc %+.1e] comb=%+.2e pred=%+.2e" % (s["k"], s["M"], s["r"], s["eps3"], s["E3"], s["eps_negctrl"], s["combined_tail_measured"], s["D_Theta_pred"]) for s in o["slips"]))
    for p in part2: print("a=%4d th=%.1f: a-hull %s (w=%.1f; in-block cell %.1f)  L-hull %s (in-block cell %s)" % (p["a"], p["theta0"], [round(x, 1) for x in p["a_hull"]] if p["a_hull"] else None, p["width"] or 0, p["width_inblock_cell"] or 0, [round(x, 4) for x in p["L_hull"]] if p["L_hull"] else None, [round(x, 4) for x in p["L_hull_inblock_cell"]] if p["L_hull_inblock_cell"] else None))
    print("ALL PASS" if ok else "FAILURES"); sys.exit(0 if ok else 1)
