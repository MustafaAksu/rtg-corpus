#!/usr/bin/env python3
"""A1c drift centring -- proof table for the all-m / all-M scope (PR #96 review #5675460082: DRIFT-1, ENV-1).

Companion of recog_a1c_drift_centering_cert.py (imported; its G1-G4 run at import).  Nothing here is a grid in place of a
proof: each table row states an inequality valid for every m >= 0 (Lemma 22) or every M >= 1 (Cor. 24) by the elementary
facts listed, and the gate checks (i) the elementary facts themselves (brute-force sums against their closed-form
majorants, suprema against their claimed values, the Hurwitz-zeta bound on a fine grid, the partial-sum identity), (ii)
that the constants of the table reproduce the certificate's K_eps, and (iii) that the explicit all-M constants c_i(a, r)
dominate every term of E^(5) times (a+M) at a sample of M (small M included) -- a consistency check of the arithmetic,
not the proof.

DRIFT-1 (Lemma 22, sup over m >= 0, every admissible b >= b' = a - Delta_a).  q_m^{-1} - b~_m = -(29/216) S_iso(m) - 2 Re(a05 S_osc(m)) + S_R(m),
  S_iso(m) = sum_{j<m} (q_j - 1/(b+j)),  S_osc(m) = sum_{j<m} q_j e^{-6 i Theta_j},  S_R(m) = sum_{j<m} R_j.  Rows:
  (D1) |q_j - 1/(b+j)| <= epsbar_j/((1-kappa)(b'+j)^2): part 1b's bracket |q_j^{-1} - b - j| <= epsbar_j, q_j^{-1} >= (1-kappa)(b'+j), b >= b'.
  (D2) kappa = e_const/b' + gamma0/(sqrt2 b') >= sup_m epsbar_m/(b'+m): log(1+t) <= sqrt t (G1f) and sup_m sqrt(m)/(b'+m) = 1/(2 sqrt b').
  (D3) sum_{i>=j} (b'+i)^{-2} <= (1+1/b')/(b'+j) (first term + integral; summand decreasing) =: tailP2(j).
  (D4) sum_{i>=j} log(1+i/2b')(b'+i)^{-2} <= [2 log(1+j/2b') + C_L]/(b'+j) =: tailLg2(j), C_L = 1 + 2(log 2 + 1/(8b')):
       j >= b': summand decreasing (G1g), first term <= L/(b'+j), integral = L/(b'+j) + log(1 + b'/(b'+j))/b' <= (L+1)/(b'+j) (G1c);
       j < b': the whole sum <= integral from 0 + sup summand = log2/b' + 1/(8b'^2) <= C_L/(2b') <= C_L/(b'+j).
  (D5) Lam_A1(j) := [e_const tailP2(j) + 2 gamma0 tailLg2(j)]/(1-kappa) >= sum_{i>=j} |q_i - 1/(b+i)|  (D1, D3, D4);  Lam_iso = Lam_A1(0) >= sup_m |S_iso(m)|.
  (D6) Theta_{j+1} - Theta_j = Arg(1+u_j) = -tau q_j + nu_j, |nu_j| <= c_theta q_j^2 (part 1b);  sum_{i<j} q_i = S_iso(j) + H_j(b);
       H_j(b) = log((b+j)/b) + [psi(b+j) - log(b+j)] - [psi(b) - log b],  |psi(x) - log x| <= 1/x.  Hence Theta_j = Theta_0 - tau log((b+j)/b) + eta_j
       with eta_j := -tau S_iso(j) - tau[psi(b+j) - log(b+j)] + tau[psi(b) - log b] + sum_{i<j} nu_i, convergent (D5; sum q_i^2 < inf), limit eta_inf, and
       |eta_j - eta_inf| <= tau Lam_A1(j) + tau/(b+j) + c_theta Sigma_2(j),  Sigma_2(j) := (1+1/b')/((1-kappa)^2 (b'+j)) >= sum_{i>=j} q_i^2.
  (D7) S_osc(m) = e^{-6i(Theta_0+eta_inf)} b^{6 i tau} sum_{j<m} (b+j)^{-s} e^{-6i(eta_j-eta_inf)} + sum_{j<m} (q_j - 1/(b+j)) e^{-6 i Theta_j},  s = 1 - 6 i tau;
       sum_{j<m} (b+j)^{-s} = zeta(s, b) - zeta(s, b+m) (analytic continuation of the partial-sum identity; checked numerically);
       |zeta(s, x)| <= 1/|s-1| + (1+|s|)/(2x) for Re s = 1, x > 0 (first-order Euler-Maclaurin: zeta(s,x) = x^{1-s}/(s-1) + x^{-s}/2 - s int_x^inf B1({t}) t^{-s-1} dt,
       |B1| <= 1/2); |e^{-6i(eta_j - eta_inf)} - 1| <= 6|eta_j - eta_inf|.  Hence for every m:
       |S_osc(m)| <= 2[1/(6 tau) + (1+|s|)/(2b')] + Lam_iso + 6 sum_j |eta_j - eta_inf|/(b'+j) =: Omega,
       sum_j |eta_j - eta_inf|/(b'+j) <= (cA + cC) S_1 + cB S_log + tau S_1 + c_theta (1+1/b')/(1-kappa)^2 S_1,
       S_1 = 1/b'^2 + 1/b' >= sum_j (b'+j)^{-2}, S_log = log2/b' + 1/(8b'^2) >= sum_j log(1+j/2b')(b'+j)^{-2}  (D4 with j = 0),
       Lam_A1(j) <= [cA + cC + cB log(1+j/2b')]/(b'+j),  cA = e_const(1+1/b')/(1-kappa), cB = 4 gamma0/(1-kappa), cC = 2 gamma0 C_L/(1-kappa).
  (D8) |S_R(m)| <= gamma2 sum_j q_j^2 <= gamma2 (2 q_0 + q_0^2): Lemma 21 on (0, q*] (q_j <= q_0 <= q*, one-orbit contraction q_m <= q_0/(1 + q_0 m/2)).
  K_eps = (29/216) Lam_iso + 2|a05| Omega + gamma2 (2 q_0 + q_0^2) at q_0 = 1/b'  (every row is monotone in b, worst at b = b').
ENV-1 (Cor. 24).  Sum form: E^(5) = [xi_max + rho_P + ref_err] + varrho_D + c_J^R Sigma_2 + c_7^R Sigma_3 + tau half(omega S) + tau half Lambda^log
  + tau K_eps P'_2 + ref_d^new -- ten non-negative terms; the difference form of the cell (E^(4) - tau A_1 - ref_d^old + ...) equals it up to the
  interval slack of subtracting equal quantities (E^(4) = E''' - tau A_0 + tau half(omega S), E''' = [in-block] + tau(A_0 + A_1) + varrho_D + ref_d^old
  + c_J^R Sigma_2 + c_7^R Sigma_3), so up(E5_sum) <= up(E5_diff) (PT2).  Covering: |eps'''| <= [in-block] + |tau A_0| + |tau A_1| + |varrho_D| + (sqrt3/8)
  |sqrt q_M - n^{-1/2}| + tails (combined-tail cell); tau A_0 in tau omega S (start offset), tau A_1 = tau Lambda^log(b) + tau A_1' with Lambda^log(b) in
  the enclosure (b in [b-, b+]) and |A_1'| <= K_eps P'_2 (Prop. 23, every M >= 0), q_M in [q-, q+] by Lemma 22 (every M >= 0); the centre subtracts
  tau mid(omega S) + tau mid Lambda^log.  Term-by-term all-M constants c_i(a, r) with n = a + M, n' = b' + M >= rho n, rho = b'/a (table in the record §3a):
  Qd(M) <= G1 QM(M) <= cQd/n (Qd decreasing in M; QM = 1/(nn - c_Q sqrt nn), nn = n' - epsbar_M >= (1-kappa) n'), G1 = (1 + ebar(Qd_1))^10;
  ebar(Qd) <= c_eb n^{-1/2}; (Delta_a + epsbar_M)/sqrt n <= c_De := Delta_a/sqrt a + e_const/sqrt a + 2 gamma0/sqrt(2b');  then
  c1 xi_max, c2 rho_P(r), c3 ref_err(r), c4 varrho_D(r), c5 Sigma_2, c6 Sigma_3, c7 half(omega S) (|omega| <= Delta_a, width <= 2 Delta_a),
  c8 half Lambda^log (b-range width <= 2 Delta_a; Lambda^log decreasing in b; psi-bracket widths; second-order tail), c9 K P'_2, c10 ref_d^new.
Gates: PT1 elementary facts and the Lemma 22 rows (brute force vs majorants; suprema; zeta bound on a fine grid; partial-sum identity; psi bounds;
       K_eps reproduced); PT2 sum form vs difference form; PT3 c_i(a, r) dominate T_i (a+M) at the M sample for a in {625, 1000, 2500}, r = 0..5,
       and C(a, r) = sum c_i bounds E^(5)(a+M); PT4 monotonicity facts (b~_M increasing in b; Lambda^log decreasing in b; Qd decreasing in M) at sample points.
usage: python -I recog_a1c_drift_proof_table_cert.py [OUT_JSON]
"""
import hashlib, json, math, os, sys
import numpy as np
import mpmath as mp
from mpmath import iv
import sympy as sp
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import recog_a1c_drift_centering_cert as d
pct, pib, p1b, pso = d.pct, d.pib, d.p1b, d.pso
I, up, lo, f, tau = d.I, d.up, d.lo, d.f, d.tau
C = d.C_ISO; SQ3_8 = d.SQ3_8
res = {"gates": {}, "imports": {"recog_a1c_drift_centering_cert.py": hashlib.sha256(open(os.path.join(HERE, "recog_a1c_drift_centering_cert.py"), "rb").read()).hexdigest(), **d.res["imports"]}}
gamma0, gamma1, cQ, c_theta = p1b.gamma0, p1b.gamma1, p1b.cQ, p1b.c_theta
def ctx(a):
    a = I(a); env = p1b.envelope_new(a, 1); Delta_a = env["Delta_a"]; bp = a - Delta_a
    q0b = 1/bp; sigma2 = 2*q0b + q0b**2; e_const = gamma0*q0b + gamma1*sigma2; kappa = env["kappa"]
    kappa2 = C*(iv.exp(I(-1)) + 1/bp)/bp
    return dict(a=a, Delta_a=Delta_a, bp=bp, e_const=e_const, kappa=kappa, kappa2=kappa2, rho=bp/a, sigma2=sigma2)
# ---------------- PT1: elementary facts and the Lemma 22 rows ----------------
def log(*a_): print(*a_, file=sys.stderr, flush=True)
pt1 = {}; g = True
for a in (625, 2500):
    log("PT1", a)
    c = ctx(a); bp = c["bp"]; bpf = float(lo(bp)); N = 4_000_000
    i_ = np.arange(0, N, dtype=np.float64); n = bpf + i_
    S2_all = np.cumsum((n**-2)[::-1])[::-1]                                        # sum_{i>=j} (b'+i)^{-2} up to N (tail beyond N added below)
    Slog_all = np.cumsum((np.log1p(i_/(2*bpf))*n**-2)[::-1])[::-1]
    rows = {}
    for j in (0, 1, 10, int(bpf//2), int(math.ceil(bpf)), 2*int(math.ceil(bpf)), 10**4, 10**5):
        tP = float(lo(d.tailP2(bp, I(j)))); tL = float(lo(d.tailLg2(bp, I(j))))
        s2 = float(S2_all[j]) + float(lo(p1b.P(I(2), bp, I(N)))); sl = float(Slog_all[j]) + float(lo(d.Lg_corr(2, bp, N)))
        ok = s2 <= tP*(1 + 1e-12) and sl <= tL*(1 + 1e-12); g &= ok
        rows[str(j)] = {"sumP2": s2, "tailP2": tP, "sumLg2": sl, "tailLg2": tL, "ok": bool(ok)}
    log("PT1 tails done")
    # (D2) kappa >= sup_m epsbar_m/(b'+m); (D7) S_1, S_log; kappa2 >= sup_n C(log(n/b)+1/b)/n
    m = np.arange(0, 10**7, dtype=np.float64); eps_m = f(c["e_const"]) + 2*f(gamma0)*np.log1p(m/(2*bpf))
    supk = float(np.max(eps_m/(bpf + m))); okk = supk <= f(c["kappa"])
    S1 = float(lo(1/bp**2 + 1/bp)); Slog = float(lo(iv.log(I(2))/bp + 1/(8*bp**2)))
    oks = float(S2_all[0]) + float(lo(p1b.P(I(2), bp, I(N)))) <= S1 and float(Slog_all[0]) + float(lo(d.Lg_corr(2, bp, N))) <= Slog
    x = np.concatenate([np.linspace(bpf, 50*bpf, 200001), np.geomspace(50*bpf, 1e12, 100001)])
    supk2 = float(np.max(f(C)*(np.log(x/bpf) + 1/bpf)/x)); okk2 = supk2 <= f(c["kappa2"])
    # (D8) one-orbit bound: sum_j q_j^2 <= q0^2 + 2 q0 for q_j <= q0/(1 + q0 j/2)
    q0 = 1/bpf; jj = np.arange(0, 10**7, dtype=np.float64); sq = float(np.sum((q0/(1 + q0*jj/2))**2)) + 2*q0/(1 + q0*1e7/2)
    ok8 = sq <= q0**2 + 2*q0
    log("PT1 suprema done")
    # (D7) zeta bound on a fine grid (both signs), the partial-sum identity, |psi(x) - log x| <= 1/x
    okz = True; worst = 0.0
    for sgn in (+1, -1):
        s_c = mp.mpc(1, sgn*6*mp.mpf(up(tau)))
        for xv in np.concatenate([np.linspace(bpf, 20*bpf, 400), np.geomspace(20*bpf, 2e5, 100)]) + 0.37:    # non-integer x (mpmath's integer path sieves primes up to x)
            ex = abs(mp.zeta(s_c, mp.mpf(float(xv)))); bd = float(lo(d.zeta_bound(I(float(xv))))); okz &= ex <= bd; worst = max(worst, float(ex/bd))
    log("PT1 zeta grid done")
    s_c = mp.mpc(1, -6*mp.mpf(up(tau))); bb = mp.mpf(bpf); mm = 1000
    part = mp.fsum((bb + j)**(-s_c) for j in range(mm)); ident = abs(part - (mp.zeta(s_c, bb) - mp.zeta(s_c, bb + mm))); oki = ident < 1e-25
    xs_ = np.geomspace(1, 1e9, 2000); okpsi = all(abs(float(mp.digamma(float(xv))) - math.log(float(xv))) <= 1/float(xv) for xv in xs_)
    # K_eps reproduced from the rows
    K = d.K_eps(a); Lam_iso = (c["e_const"]*d.tailP2(bp, I(0)) + 2*gamma0*d.tailLg2(bp, I(0)))/(1 - c["kappa"])
    cA = c["e_const"]*(1 + 1/bp)/(1 - c["kappa"]); cB = 4*gamma0/(1 - c["kappa"]); cC = 2*gamma0*d.C_L(bp)/(1 - c["kappa"])
    S_1 = 1/bp**2 + 1/bp; S_log = iv.log(I(2))/bp + 1/(8*bp**2)
    phase = 6*(tau*((cA + cC)*S_1 + cB*S_log) + tau*S_1 + c_theta*(1 + 1/bp)/(1 - c["kappa"])**2*S_1)
    Omega = 2*d.zeta_bound(bp) + Lam_iso + phase
    K_rows = C*Lam_iso + 2*d.abs_a05*Omega + d.gamma2*c["sigma2"]
    okK = abs(f(K_rows) - f(K["K"])) <= 1e-12*f(K["K"])
    ok_a = okk and oks and okk2 and ok8 and okz and oki and okpsi and okK; g &= ok_a
    pt1[str(a)] = {"tails": rows, "sup_epsbar_over_n": supk, "kappa": f(c["kappa"]), "S_1_ok_and_S_log_ok": bool(oks), "sup_CL_over_n": supk2, "kappa2": f(c["kappa2"]),
                   "sum_q2_majorant": sq, "one_orbit_bound": q0**2 + 2*q0, "zeta_bound_worst_ratio": worst, "zeta_ok": bool(okz), "partial_sum_identity_err": float(ident),
                   "psi_log_ok": bool(okpsi), "K_from_rows": f(K_rows), "K_cert": f(K["K"]), "ok": bool(ok_a)}
res["gates"]["PT1_lemma22_rows"] = bool(g); res["PT1"] = pt1
# ---------------- PT2: sum form vs difference form ----------------
def common(a, M, bw):
    """r-independent pieces of E^(5) at (a, M) over the b-range bw"""
    om = iv.mpf([float(a - bw[1]), float(a - bw[0])])                               # omega = a - b
    prod = om*pso.S_bracket(a, M, bw); half0 = (up(prod) - lo(prod))/2
    Lam = d.Lambda_log(iv.mpf([bw[0], bw[1]]), M); halfL = (up(Lam) - lo(Lam))/2
    Ka = d.K_eps(a)["K"]; kp = tau*Ka*d.P2prime(a, M); rdn = d.ref_d_new(a, bw, M)
    return {"half0": half0, "halfL": halfL, "kp": kp, "rdn": rdn, "Ka": Ka}
def terms(a, M, r, bw, cm=None):
    """the ten non-negative terms of E^(5) (sum form) and the difference form of the cell"""
    cm = cm or common(a, M, bw)
    a_ = I(a); n = a_ + M; c3 = pct.combined(a, M, r); ib = pib.inblock(a_, I(M), r)
    T = {"xi_max": ib["xi_max"], "rho_P": ib["rho_P"], "ref_err": ib["ref_err"], "varrho_D": c3["varrho_D"], "SigmaJ": c3["SigmaJ"], "Sigma7": c3["Sigma7"],
         "tau_half_omegaS": tau*I(cm["half0"]), "tau_half_Lam": tau*I(cm["halfL"]), "tau_K_P2": cm["kp"], "ref_d_new": cm["rdn"]}
    E5_sum = sum(T.values(), I(0))
    E4 = c3["E3"] - c3["tauA0"] + tau*cm["half0"]
    E5_diff, _, _ = d.E5_terms(a, M, r, bw, E4, cm["Ka"])
    return T, E5_sum, E5_diff, n
pt2 = {}; g = True
for a in (625, 2500):
    bw = (mp.mpf(a) - 1, mp.mpf(a) + 1)
    for M in (1, 10, 10**3, 10**5, 10**7, 10**10, 10**13):
        log("PT2", a, M)
        T, Es, Ed, n = terms(a, M, 5, bw)
        ok = up(Es) <= up(Ed)*(1 + mp.mpf(10)**-25) and all(lo(v) >= 0 for v in T.values()) and abs(f(Es) - f(Ed)) <= 1e-6*f(Ed); g &= ok
        pt2[f"a={a},M={M}"] = {"E5_sum*n": f(Es)*(a + M), "E5_diff*n": f(Ed)*(a + M), "ok": bool(ok)}
res["gates"]["PT2_sum_form"] = bool(g); res["PT2"] = pt2
# ---------------- PT3: all-M constants c_i(a, r) ----------------
def constants(a, r):
    c = ctx(a); a_ = c["a"]; bp = c["bp"]; kappa = c["kappa"]; kappa2 = c["kappa2"]; rho = c["rho"]; Delta_a = c["Delta_a"]; e_const = c["e_const"]
    K = d.K_eps(a)["K"]
    Qd1 = pib.inblock(a_, I(1), r)["Qd"]; eb1 = pib.ebar(Qd1); G1 = (1 + eb1)**10
    cQp = (1 - kappa)*(1 - cQ/iv.sqrt((1 - kappa)*bp))                               # QM <= 1/(cQp n')
    cQd = G1/(cQp*rho)                                                                # Qd <= cQd/n
    c_eb = (pib.e_sqrt + pib.e_lin*iv.sqrt(Qd1))*iv.sqrt(cQd)                        # ebar(Qd) <= c_eb n^{-1/2}
    c_De = Delta_a/iv.sqrt(a_) + e_const/iv.sqrt(a_) + 2*gamma0/iv.sqrt(2*bp)        # (Delta_a + epsbar_M)/sqrt n <= c_De
    cDelta = tau*cQd + I("1.82")*cQd**(I(3)/2)/iv.sqrt(a_)                            # Deltabar <= cDelta/n
    c1 = iv.mpf([0, max(up(tau/2), up(cDelta))])
    c2 = I(0); s1e = iv.sqrt(1 - eb1**2)
    for s_ in range(1, int(r) + 1):
        c2 += pib.c_delta(Qd1)*cQd + I(pib.SUP_GP)*(iv.sqrt(Qd1)*cDelta + s_*c_eb*iv.sqrt(cQd)/s1e) + pib.GABS[s_]*s_*c_eb*iv.sqrt(cQd)/(1 - eb1)**(s_ + 1)
    c_up = G1*(c_De + cQ)/(cQp*rho) + 10*(1 + eb1)**9*c_eb
    c_lo = c_De + cQ/iv.sqrt((1 - kappa)*rho) + 10*c_eb
    c3 = pib.KAPPA[int(r)]*I(max(up(c_up), up(c_lo)))
    qp_s = 1/iv.sqrt((1 - kappa)*bp)                                                   # sqrt q+ <= this, and <= 1/sqrt((1-kappa) rho n)
    c4 = I(pct.SUP_DP)*(cDelta*qp_s + int(r)*c_eb/(s1e*iv.sqrt((1 - kappa)*rho)) + I(pct.SUP_D)/((1 - kappa)*rho) + pct.C1*qp_s/((1 - kappa)*rho)) + pct.C1/((1 - kappa)*rho)
    c5 = pct.CJ*(1 + 1/bp)/((1 - kappa)**2*rho)
    c6 = pct.C7R*(1/bp + I(1)/2)/((1 - kappa)**3*bp*rho)
    c7 = tau/2*(Delta_a*(1 + 2*Delta_a)/(bp*rho) + 2*Delta_a*(1 + 1/bp)/rho)
    one = 1 + 1/bp
    var_b = 2*Delta_a*C/(1 - kappa2)**2*(one/bp + 2*one**2/bp)/rho                   # Lambda(b-) - Lambda(b+) <= w_b sum sup|d_b f_m|, w_b <= 2 Delta_a
    w_expl = C*(1/(2*bp) + 1/(2*bp))*one/rho*(1/(1 - kappa2) + C*one/(bp*(1 - kappa2)**2))   # psi-bracket widths of the explicit sum (delta_m <= 1/(2b) + 1/(2n_M) <= 1/b')
    L2 = 8/(iv.exp(I(2))*bp) + 2/bp**2                                               # L0^2/n0^2 <= L2/n_M (log^2 y <= (4/e^2) y)
    w_tail = (C*(one/bp + 1/bp + 1/(2*bp)) + C**2/(1 - kappa2)*(L2/(3*bp) + L2/2 + one/(2*bp) + 1/(4*bp)))/rho
    c8 = tau/2*(var_b + 2*(w_expl + w_tail))
    c9 = tau*K*(1 + 1/bp)/((1 - kappa)*(1 - kappa2)*rho)
    cD = (1 - kappa2) - K/bp; assert lo(cD) > 0
    c10 = SQ3_8*I(max(up(((Delta_a + K + C/bp)/iv.sqrt(a_) + C/iv.sqrt(bp))/(cD*rho)), up((Delta_a + K)/((1 - kappa2)*rho*iv.sqrt(a_)))))
    cs = {"xi_max": c1, "rho_P": c2, "ref_err": c3, "varrho_D": c4, "SigmaJ": c5, "Sigma7": c6, "tau_half_omegaS": c7, "tau_half_Lam": c8, "tau_K_P2": c9, "ref_d_new": c10}
    aux = {"G1": f(G1), "cQp": f(cQp), "cQd": f(cQd), "c_eb": f(c_eb), "c_De": f(c_De), "cDelta": f(cDelta), "Qd1": f(Qd1), "rho": f(rho), "cD": f(cD)}
    return cs, aux
Ms = [1, 2, 3, 4, 5, 7, 10, 15, 20, 30, 50, 70, 100, 200, 500, 10**3, 3*10**3, 10**4, 3*10**4, 10**5, 10**6, 10**7, 10**8, 10**9, 10**10, 10**11, 10**12, 10**13]
pt3 = {}; g = True
for a in (625, 1000, 2500):
    c = ctx(a); Delta_a = f(c["Delta_a"]); bw = (mp.mpf(a) - Delta_a, mp.mpf(a) + Delta_a)       # the widest admissible b-range (omega in [-Delta_a, Delta_a])
    cms = {}
    for M in Ms:
        log("PT3", a, M); cms[M] = common(a, M, bw)
    for r in range(6):
        cs, aux = constants(a, r); Ctot = sum(cs.values(), I(0)); worst = {k: 0.0 for k in cs}; worstE = 0.0
        for M in Ms:
            T, Es, Ed, n = terms(a, M, r, bw, cms[M])
            for k in cs:
                ratio = f(T[k])*f(n)/f(cs[k]) if f(cs[k]) > 0 else (0.0 if f(T[k]) == 0 else float("inf"))
                worst[k] = max(worst[k], ratio); g &= up(T[k]*n) <= up(cs[k])*(1 + mp.mpf(10)**-25)
            worstE = max(worstE, f(Es)*f(n)/f(Ctot)); g &= up(Es*n) <= up(Ctot)
        pt3[f"a={a},r={r}"] = {"c": {k: f(v) for k, v in cs.items()}, "C_total": f(Ctot), "worst_ratio_T_n_over_c": worst, "worst_E5n_over_C": worstE, "aux": aux}
res["gates"]["PT3_all_M_constants"] = bool(g); res["PT3"] = pt3; res["PT3_M_sample"] = Ms
# ---------------- PT4: monotonicity facts ----------------
bs_, Ms_ = sp.symbols('b M', positive=True)
bt = bs_ + Ms_ - sp.Rational(29, 216)*(sp.polygamma(0, bs_ + Ms_) - sp.polygamma(0, bs_))
dbt = sp.simplify(sp.diff(bt, bs_) - (1 - sp.Rational(29, 216)*(sp.polygamma(1, bs_ + Ms_) - sp.polygamma(1, bs_))))
ok4 = dbt == 0                                                                        # d b~_M/db = 1 + C (psi'(b) - psi'(b+M)) >= 1 since psi' is decreasing
g = ok4; pt4 = {"d_btilde_db_identity": bool(ok4)}
for a in (625, 2500):
    for M in (1, 100, 10**4, 10**7):
        lam = [f(d.Lambda_log(I(b), M)) for b in (a - 20, a, a + 20)]; ok = lam[0] > lam[1] > lam[2]; g &= ok
        qd = [f(pib.inblock(I(a), I(mm), 5)["Qd"]) for mm in (1, 2, max(M, 3), 10*max(M, 3))]; okq = qd[0] > qd[1] > qd[2] > qd[3]; g &= okq
        pt4[f"a={a},M={M}"] = {"Lambda_log_at_b_minus_20_a_plus_20": lam, "decreasing_in_b": bool(ok), "Qd_decreasing_in_M": bool(okq)}
res["gates"]["PT4_monotonicity"] = bool(g); res["PT4"] = pt4
ok = all(res["gates"].values()); res["ALL_PASS"] = ok
if __name__ == "__main__":
    outp = sys.argv[1] if len(sys.argv) > 1 else "a1c_drift_proof_table_cert.json"
    json.dump(res, open(outp, "w"), indent=1, default=lambda o: bool(o) if isinstance(o, np.bool_) else (float(o) if isinstance(o, (np.floating, np.integer)) else str(o)))
    for k_, v_ in res["gates"].items(): print(k_, "PASS" if v_ else "FAIL")
    for a in pt1: print("a=%s: K from rows %.6f (cert %.6f); zeta worst ratio %.3f; sup epsbar/n %.3e <= kappa %.3e; sup C L/n %.3e <= kappa2 %.3e" % (a, pt1[a]["K_from_rows"], pt1[a]["K_cert"], pt1[a]["zeta_bound_worst_ratio"], pt1[a]["sup_epsbar_over_n"], pt1[a]["kappa"], pt1[a]["sup_CL_over_n"], pt1[a]["kappa2"]))
    for k_, v_ in pt3.items():
        print("%s: C(a,r)=%.1f  c=" % (k_, v_["C_total"]) + " ".join("%s=%.3g(%.2f)" % (kk, v_["c"][kk], v_["worst_ratio_T_n_over_c"][kk]) for kk in v_["c"]) + "  worst E5 n/C=%.3f" % v_["worst_E5n_over_C"])
    print("ALL PASS" if ok else "FAILURES"); sys.exit(0 if ok else 1)
