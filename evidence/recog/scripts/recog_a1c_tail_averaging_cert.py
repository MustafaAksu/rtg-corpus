#!/usr/bin/env python3
"""A1c part 1b -- primitive-tail averaging: a sharper envelope for S^tail_M (and R^tail_M) in the normalized variable.

Setting (RECOG-THM-A1B-SLIP-SCHEDULE-U, recog-v0.3.24 §6.13b; known a = 1/Q_0):
    |eps_k| <= tau Q* + 1.82 Q*^{3/2} + 5 arcsin(0.705 sqrt Q* + 0.257 Q*) + tau |S^tail_M| + |R^tail_M|,
    S^tail_M = sum_{m>=M} (Q_m - 1/(a+m)),   R^tail_M = sum_{m>=M} r_m   (M = M_k; Q_m = Q_prim at block base points).
Part 1 (RECOG_A1C_KNOWN_A_ENVELOPE_SESSION_v0_1, v0.2) majorised S^tail by Sbar ~ 150/sqrt(a+M) through |e_m| <= 37.5 sqrt(a+m)
summed in absolute value. Here S^tail is written in the NORMALIZED chart z = h^{-1}(W) (q = |z|^2; Q = q + D_Q(z)) and the
oscillating degree-3 bridge term is summed by comparison with the model sum sum (b+m)^{-3/2-ik tau} (one averaging step).
Inputs (Dyadic v6.4.22 §6.2, §6.14; RECOG v0.3.24):
  (D1) DYAD-THM-NF-REM: block base points' chart images lie in row A (|z| < 1/20); hat F(z) = J(z) + R_7, |R_7| <= C_7 |z|^7 (C_7 = 100);
       normalized contraction q' <= q - q^2/2 (q <= 1/400), hence q_m <= q_0/(1 + q_0 m/2).
  (D2) DYAD-ALG-NF6 jet: J(z) = z + mu z^2 zbar + a32 z^3 zbar^2 + a05 zbar^5,  mu = -1/2 - i 2 sqrt3/3.
  (D3) DYAD-THM-NF-INV: q <= (256/225) Q_prim on |z| <= 1/10.
  (D4) h_2 (§6.2, [ALG]): h_2 = c20 z^2 + c11 z zbar + c02 zbar^2; D_3 = 2 Re(zbar h_2) (DYAD-ALG-OPEN3-LEADING), harmonics +-1, +-3.
  (D5) Row-A bridge constants published in the proof of DYAD-THM-LPHASE-ROWA-REMAINDER (certificate DYAD-ART-LPHASE-ROWA):
       |D_Q| <= c_Q q^{3/2} (c_Q = 0.79246),  |D_Q - D_3| <= c'_Q q^2 (c'_Q = 0.36915);
       for R^tail also: r = Lambda_3(z) + rest, |rest| <= (123/125 + taubar c'_Q + c_J) q^2 + c_7 q^3, c_J = 0.50220, c_7 = 157.58,
       Lambda_3 = L_Theta + tau D_3 with the published harmonic coefficients.  [(D5) are proof constants, not theorem rows -> flagged]
Derivation (record §1-§3). b := 1/q_0, |a - b| <= Delta_a := (16/15) c_Q sqrt a. With u = mu q + rho/z, rho = a32 z^3 zbar^2 + a05 zbar^5 + R_7:
  q-law:   |q_{m+1}^{-1} - q_m^{-1} - 1| <= gamma0 q_m + gamma1 q_m^2,  gamma0 ~ |1 - |mu|^2 - 2 Re a32| + 2|a05| = 29/216 + 2|a05| (+ tiny)
           => q_m^{-1} = b + m + eps_m,  |eps_m| <= epsbar_m := gamma0 (q0bar + 2 log(1 + m/(2 b'))) + gamma1 (2 q0bar + q0bar^2),  b' = a - Delta_a
  phase:   e^{i Theta_{m+1}} = e^{i Theta_m} (1+u_m)/|1+u_m|;  |Arg(1+u_m) + tau q_m| <= c_theta q_m^2;
           e^{ik Theta_m} = e^{ik Theta_M} ((b+m)/(b+M))^{-ik tau} e^{ik eta_m},  |eta_m| <= etabar_M  (m >= M)
  S^tail = A0 + A1 + B + C:  A0 = sum (1/(b+m) - 1/(a+m)),  A1 = sum (q_m - 1/(b+m)),  B = sum D_3(z_m),  C = sum (D_Q - D_3)(z_m)
  B = Re(phi1 B_1 + phi3 B_3),  B_k = sum q_m^{3/2} e^{ik Theta_m};  |B_k| <= |Sigma_k| + (3/2) sum epsbar_m (b+m-epsbar_m)^{-5/2} + k etabar_M sum q_m^{3/2}
  Sigma_k = sum_{m>=M} (b+m)^{-s_k}, s_k = 3/2 + ik tau:  |Sigma_k| <= (b+M)^{-1/2}/|s_k - 1| + (1/2 + |s_k|/3)(b+M)^{-3/2}  (Euler-Maclaurin, 1st order)
  All sums majorised by closed forms (integral comparison) in (a, M) only.  Leading constant of Sbar': |phi1|/|s_1-1| + |phi3|/|s_3-1| = 0.7485.
Gates: G1 exact identities (sympy); G2 constants by interval arithmetic; G3 closed forms dominate brute-force sums, |zeta(s_k, b+M)| within the
       Euler-Maclaurin bound; G4 the envelope table, old vs new; G5 [NUM] 12 primitive orbits (N blocks): |S^N_M| <= Sbar'(M) + Sbar'(N),
       |R^N_M| <= Rbar'(M) + Rbar'(N), Q_M <= its bound (illustration, not a proof input; S^N_M = S^tail_M - S^tail_N).
Negative controls: NC1 wrong h_2 coefficient breaks the harmonic identity; NC2 a closed form without its first-term correction fails G3.
usage: python -I recog_a1c_tail_averaging_cert.py [OUT_JSON] [N_STEPS]
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
# ---------------- exact data ----------------
s3 = iv.sqrt(I(3)); tau = 2*s3/3
mu_re, mu_im = I(-1)/2, -2*s3/3
a32_re, a32_im = I(-97)/432, 197*s3/324
a05_re, a05_im = I(-49)/8640, -307*s3/25920
abs_mu = iv.sqrt(mu_re**2 + mu_im**2); abs_a32 = iv.sqrt(a32_re**2 + a32_im**2); abs_a05 = iv.sqrt(a05_re**2 + a05_im**2)
A5 = abs_a32 + abs_a05
C7 = I(100)
cQ, cQp, cJ, c7, K_Theta = I("0.79246"), I("0.36915"), I("0.50220"), I("157.58"), I(123)/125     # (D5) published row-A constants
taubar = I(11548)/10000                                                                            # rational ceiling of tau used by Dyadic (1.1548 > 1.15470)
c_r2 = K_Theta + taubar*cQp + cJ; c_r3 = c7
# harmonic amplitudes
phi1 = (I(-5)/6, -s3/6); phi3 = (I(1)/12, s3/12)
lam1 = (-49*s3/72, I(-1)/24); lam3 = (23*s3/144, I(19)/48)
cabs = lambda c: iv.sqrt(c[0]**2 + c[1]**2)
abs_phi1, abs_phi3, abs_lam1, abs_lam3 = cabs(phi1), cabs(phi3), cabs(lam1), cabs(lam3)
den = lambda k: iv.sqrt(I(1)/4 + k**2*tau**2)          # |s_k - 1|
abs_s = lambda k: iv.sqrt(I(9)/4 + k**2*tau**2)        # |s_k|
# ---------------- G1: exact identities (sympy) ----------------
X = sp.sqrt(3); Th = sp.symbols('Theta', real=True); r = sp.symbols('r', positive=True)
c20 = -sp.Rational(1, 12) - sp.I*X/12; c11 = -sp.Rational(1, 3); c02 = sp.Rational(1, 24) - sp.I*X/24
def harmonics(c20_, c11_, c02_):
    z = r*(sp.cos(Th) + sp.I*sp.sin(Th)); zb = r*(sp.cos(Th) - sp.I*sp.sin(Th))
    h2 = c20_*z**2 + c11_*z*zb + c02_*zb**2
    D3 = sp.expand(2*sp.re(sp.expand(zb*h2)))
    target = r**3*(-sp.Rational(5, 6)*sp.cos(Th) + X/6*sp.sin(Th) + sp.Rational(1, 12)*sp.cos(3*Th) - X/12*sp.sin(3*Th))
    return sp.simplify(sp.expand(sp.expand_trig(D3 - target))) == 0
g1a = harmonics(c20, c11, c02)                                                         # D_3 of DYAD-ALG-OPEN3-LEADING from h_2
g1b = sp.simplify(2*(c20 + sp.conjugate(c11)) - (-sp.Rational(5, 6) - sp.I*X/6)) == 0 and sp.simplify(2*sp.conjugate(c02) - (sp.Rational(1, 12) + sp.I*X/12)) == 0
musq = sp.Rational(1, 4) + sp.Rational(4, 3)
g1c = sp.simplify(1 - musq - 2*(-sp.Rational(97, 432)) + sp.Rational(29, 216)) == 0           # 1 - |mu|^2 - 2 Re a32 = -29/216
# Lambda_3 = L_Theta + tau D_3 (published L_Theta, D_3) matches the published Lambda_3 harmonics
tau_s = 2*X/3
L_Theta = r**3*(-X/8*sp.cos(Th) - sp.Rational(7, 24)*sp.sin(Th) + 5*X/48*sp.cos(3*Th) - sp.Rational(11, 48)*sp.sin(3*Th))
D3_s = r**3*(-sp.Rational(5, 6)*sp.cos(Th) + X/6*sp.sin(Th) + sp.Rational(1, 12)*sp.cos(3*Th) - X/12*sp.sin(3*Th))
Lam3 = r**3*(-49*X/72*sp.cos(Th) + sp.Rational(1, 24)*sp.sin(Th) + 23*X/144*sp.cos(3*Th) - sp.Rational(19, 48)*sp.sin(3*Th))
g1d = sp.simplify(sp.expand(L_Theta + tau_s*D3_s - Lam3)) == 0
# real ray: D_3 = -3/4 q^{3/2}
g1e = sp.simplify(D3_s.subs(Th, 0) + sp.Rational(3, 4)*r**3) == 0
# model integral: int_M^inf (b+x)^{-s} dx = (b+M)^{1-s}/(s-1), Re s > 1
xs, bs = sp.symbols('x b', positive=True); ss = sp.symbols('s')
anti = -(bs + xs)**(1 - ss)/(ss - 1)                       # antiderivative; -> 0 as x -> oo for Re s > 1, value at x = M gives (b+M)^{1-s}/(s-1)
g1f = sp.simplify(sp.diff(anti, xs) - (bs + xs)**(-ss)) == 0
res["gates"]["G1_exact_identities"] = bool(g1a and g1b and g1c and g1d and g1e and g1f)
res["G1"] = {"D3_from_h2": g1a, "phi_from_c": g1b, "q_law_coefficient_-29/216": g1c, "Lambda3_eq_LTheta_plus_tauD3": g1d, "real_ray_-3/4": g1e, "model_integral": g1f}
# ---------------- G2: constants (interval) ----------------
qstar = I(256)/140625                       # q at block base points <= (256/225)/625
def v_bound(q): return A5*q**2 + C7*q**3    # |rho/z|
def u_bound(q): return abs_mu*q + v_bound(q)
q = qstar
g0 = I(29)/216 + 2*abs_a05                                       # |1 - delta_2|
delta3 = 2*C7*q**3 + 2*abs_mu*q*v_bound(q) + v_bound(q)**2       # |delta_3|
delta2p = abs_mu**2 + 2*a32_re + 2*abs_a05                       # delta_2 <= this (and >= 0 anyway); |delta| <= delta2p q^2 + delta3
delta_b = delta2p*q**2 + delta3
denom = 1 - q - delta_b
gamma0 = g0/denom
gamma1 = (delta3/q + delta_b)/(q**2*denom)
c_theta = (v_bound(q) + u_bound(q)**2/(2*(1 - u_bound(q))))/q**2
res["G2_constants"] = {"gamma0": [f(lo(gamma0)), f(up(gamma0))], "gamma1": f(up(gamma1)), "c_theta": f(up(c_theta)), "A5": f(up(A5)), "|mu|": f(up(abs_mu)),
                       "|phi1|": f(up(abs_phi1)), "|phi3|": f(up(abs_phi3)), "|lam1|": f(up(abs_lam1)), "|lam3|": f(up(abs_lam3)),
                       "|s1-1|": f(up(den(1))), "|s3-1|": f(up(den(3))), "lead_S": f(up(abs_phi1/den(1) + abs_phi3/den(3))), "lead_R": f(up(abs_lam1/den(1) + abs_lam3/den(3)))}
# sup_Theta |Phi| <= c_Q and sup |Lambda_3|/r^3 <= 1.4004 (consistency with Dyadic's bridge constant and certified cell bound): grid + Lipschitz
def sup_harm(c1, c3, n=20000):
    L2 = up(cabs(c1) + 9*cabs(c3))                     # |d^2/dTheta^2|: sup <= max node value + L2 h^2/8
    best = mp.mpf(0); h = 2*mp.pi/n
    for j in range(n):
        t = j*h
        v = abs(c1[0]*iv.cos(I(t)) - c1[1]*iv.sin(I(t)) + c3[0]*iv.cos(3*I(t)) - c3[1]*iv.sin(3*I(t)))
        best = max(best, up(v))
    return best + L2*h**2/8
supPhi = sup_harm(phi1, phi3); supLam = sup_harm(lam1, lam3)
res["G2_constants"]["sup|Phi|"] = float(supPhi); res["G2_constants"]["sup|Lambda3|/r^3"] = float(supLam)
res["gates"]["G2_constants"] = bool(up(gamma0) < 0.2 and supPhi <= mp.mpf("0.79246") and supLam <= mp.mpf("1.4004") and up(c_theta) < 3)
# ---------------- closed-form majorants ----------------
def P(p, b_, M_):            # sum_{m>=M} (b'+m)^{-p} <= first term + integral
    n = b_ + M_; return n**(-p) + n**(1 - p)/(p - 1)
def Lg(p, b_, M_):           # sum_{m>=M} log(1+m/2b') (b'+m)^{-p} <= 2 sup g + integral (by parts, 2b'+x >= b'+x)
    n = b_ + M_; return b_**(-p) + n**(1 - p)/(p - 1)*iv.log(1 + M_/(2*b_)) + n**(1 - p)/(p - 1)**2
def envelope_new(a, M, first_term=True):
    a = I(a); M = I(M)
    Delta_a = I(16)/15*cQ*iv.sqrt(a); bp = a - Delta_a; q0b = 1/bp
    sigma2 = 2*q0b + q0b**2
    e_const = gamma0*q0b + gamma1*sigma2                     # epsbar_m = e_const + 2 gamma0 log(1 + m/2b')
    kappa = e_const/bp + gamma0/(iv.sqrt(I(2))*bp)
    Pp = (lambda p: P(p, bp, M)) if first_term else (lambda p: (bp + M)**(1 - p)/(p - 1))
    Lam = lambda p: e_const*Pp(p) + 2*gamma0*Lg(p, bp, M)    # sum epsbar_m (b'+m)^{-p}
    n = bp + M
    A0 = Delta_a/((a + M)*(a + M - Delta_a)) + iv.log((a + M)/(a + M - Delta_a))
    A1 = Lam(I(2))/(1 - kappa)
    etabar = c_theta*Pp(I(2))/(1 - kappa)**2 + tau*(Pp(I(2))/2 + Lam(I(2))/(1 - kappa))
    def Bk(k):
        k = I(k)
        return n**(-I(1)/2)/den(k) + (I(1)/2 + abs_s(k)/3)*n**(-I(3)/2) + I(3)/2*Lam(I(5)/2)/(1 - kappa)**(I(5)/2) + k*etabar*Pp(I(3)/2)/(1 - kappa)**(I(3)/2)
    B1, B3 = Bk(1), Bk(3)
    C = cQp*Pp(I(2))/(1 - kappa)**2
    Sbar = A0 + A1 + abs_phi1*B1 + abs_phi3*B3 + C
    Rbar = abs_lam1*B1 + abs_lam3*B3 + c_r2*Pp(I(2))/(1 - kappa)**2 + c_r3*Pp(I(3))/(1 - kappa)**3
    # block amplitude: Q_M^{-1} >= q_M^{-1} - c_Q q_M^{-1/2} >= nn - c_Q sqrt(nn), nn = b' + M - epsbar_M
    nn = bp + M - (e_const + 2*gamma0*iv.log(1 + M/(2*bp)))
    QM = 1/(nn - cQ*iv.sqrt(nn))
    Qs = QM
    for _ in range(5): Qs = Qs*(1 + I("0.705")*iv.sqrt(Qs) + I("0.257")*Qs)**2
    xarg = I("0.705")*iv.sqrt(Qs) + I("0.257")*Qs
    asin_up = I(mp.asin(up(xarg)))*(1 + I(10)**-30)          # arcsin increasing; mp value at the upper end, widened
    block = tau*Qs + I("1.82")*Qs**(I(3)/2) + 5*asin_up
    E = block + tau*Sbar + Rbar
    return {"Sbar": Sbar, "Rbar": Rbar, "block": block, "E": E, "A0": A0, "A1": A1, "B": abs_phi1*B1 + abs_phi3*B3, "C": C, "kappa": kappa, "QM": QM, "etabar": etabar, "B1": B1, "B3": B3, "Delta_a": Delta_a}
# old envelope (part 1, float; reproduces the part-1 table)
TAU = 2*math.sqrt(3)/3
def old_envelope(a, M):
    def ebar(m): return 0.0 if m == 0 else 7.5*(a**-0.5 + 4*(math.sqrt(a + (m - 1)/2) - math.sqrt(a)))
    def D(m):
        e = ebar(m); c = 1/(a + m); lo_ = 1/(a + m + e); up_ = 1/(a + m/2)
        if a + m > e: up_ = min(up_, 1/(a + m - e))
        return max(c - lo_, up_ - c)
    mc = max(M, int(math.ceil(5625 - a)))
    Sb = sum(D(m) for m in range(M, mc)) + 75*((a + mc)**-1.5 + 2*(a + mc)**-0.5)
    Rb = 403/250*((a + M/2)**-1.5 + 4*(a + M/2)**-0.5)
    Q = 1/(a + M/2)
    for _ in range(5): Q = Q*(1 + 0.705*math.sqrt(Q) + 0.257*Q)**2
    blk = TAU*Q + 1.82*Q**1.5 + 5*math.asin(0.705*math.sqrt(Q) + 0.257*Q)
    return {"Sbar": Sb, "Rbar": Rb, "block": blk, "E": blk + TAU*Sb + Rb}
# ---------------- G3: closed forms dominate brute force ----------------
def brute_checks(first_term=True):
    ok = True; out = {}
    for a, M in ((625, 1000), (2500, 1000), (625, 10000)):
        a_ = I(a); Delta_a = I(16)/15*cQ*iv.sqrt(a_); bp = a_ - Delta_a; bpf = float(lo(bp))     # b' lower end: brute force with the smallest b' (largest sums)
        N = 20_000_000; CH = 2_000_000
        q0b = 1/bpf; e_const = f(gamma0)*q0b + f(gamma1)*(2*q0b + q0b**2)
        sums = {("P", p): 0.0 for p in (1.5, 2, 2.5, 3)}; sums.update({("L", p): 0.0 for p in (2, 2.5)}); 
        for start in range(M, N, CH):
            m = np.arange(start, min(start + CH, N), dtype=np.float64); n = bpf + m; eps = e_const + 2*f(gamma0)*np.log1p(m/(2*bpf))
            for p in (1.5, 2, 2.5, 3): sums[("P", p)] += float(np.sum(n**-p))
            for p in (2, 2.5): sums[("L", p)] += float(np.sum(eps*n**-p))
        Pp = (lambda p: P(p, bp, I(M))) if first_term else (lambda p: (bp + I(M))**(1 - p)/(p - 1))
        checks = {}
        for p in (1.5, 2, 2.5, 3):
            brute = sums[("P", p)] + float(lo(P(I(p), bp, I(N))))                      # tail beyond N by the (valid) closed form at N
            checks[f"P_{p}"] = (float(lo(Pp(I(p)))) * (1 + 1e-12) >= brute, float(lo(Pp(I(p)))), brute)
        for p in (2, 2.5):
            brute = sums[("L", p)] + float(lo(e_const*P(I(p), bp, I(N)) + 2*gamma0*Lg(I(p), bp, I(N))))
            cf = e_const*Pp(I(p)) + 2*gamma0*Lg(I(p), bp, I(M))
            checks[f"Lambda_{p}"] = (float(lo(cf)) * (1 + 1e-12) >= brute, float(lo(cf)), brute)
        # Sigma_k = zeta(s_k, b+M) (Hurwitz zeta, mpmath, 40 digits) vs the Euler-Maclaurin bound, at b = b' and b = a (two ends)
        for k in (1, 3):
            s_k = mp.mpf(3)/2 + 1j*k*mp.mpf(up(tau))
            for bb, lab in ((bp, "b'"), (I(a), "a")):
                exact = abs(mp.zeta(s_k, mp.mpf(lo(bb)) + M))
                bound = float(lo((bb + I(M))**(-I(1)/2)/den(I(k)) + (I(1)/2 + abs_s(I(k))/3)*(bb + I(M))**(-I(3)/2)))
                checks[f"Sigma_{k}@{lab}"] = (bound >= float(exact), bound, float(exact), float(exact)/bound)
        ok &= all(v[0] for v in checks.values()); out[f"a={a},M={M}"] = checks
    return ok, out
g3, g3out = brute_checks()
res["gates"]["G3_closed_forms_dominate"] = bool(g3); res["G3"] = g3out
# ---------------- G4: table ----------------
table = {}; g4 = True
for a in (625, 1000, 2500):
    table[str(a)] = {}
    for M in (1000, 10000, 100000, 1000000, 10000000):
        new = envelope_new(a, M); old = old_envelope(a, M)
        row = {k: f(new[k]) for k in ("Sbar", "Rbar", "block", "E", "A0", "A1", "B", "C", "kappa", "QM")}
        row.update({"old_" + k: old[k] for k in ("Sbar", "Rbar", "block", "E")})
        row["gain_S"] = old["Sbar"]/row["Sbar"]; row["gain_R"] = old["Rbar"]/row["Rbar"]; row["gain_E"] = old["E"]/row["E"]
        row["E_sqrt(a+M)"] = row["E"]*math.sqrt(a + M); row["Sbar_sqrt(a+M)"] = row["Sbar"]*math.sqrt(a + M)
        g4 &= row["E"] < old["E"] and row["Sbar"] < old["Sbar"] and row["Rbar"] < old["Rbar"] and row["block"] <= old["block"]
        table[str(a)][str(M)] = row
lead = 5*I("0.705") + tau*(abs_phi1/den(1) + abs_phi3/den(3)) + abs_lam1/den(1) + abs_lam3/den(3)
res["G4_table"] = table; res["G4_asymptotic_constant_E"] = [f(lo(lead)), f(up(lead))]
res["G4_asymptotic_old"] = TAU*150 + 403/250*4*math.sqrt(2) + 5*0.705*math.sqrt(2)
res["gates"]["G4_table"] = bool(g4)
# ---------------- G5: [NUM] orbit check ----------------
OMEGA = complex(-0.5, math.sqrt(3)/2)
def run_orbits(Nsteps, Ms):
    Q0s = [1/625]*4 + [1/1000]*4 + [1/2500]*4; ths = [0.3, 1.7, 3.9, 5.1]*3; n = len(Q0s)
    rho = np.array([math.sqrt(Q0s[i])*math.cos(ths[i]) for i in range(n)]); eta = np.array([math.sqrt(Q0s[i])*math.sin(ths[i]) for i in range(n)])/OMEGA.imag
    rho = rho - OMEGA.real*eta; W = rho + OMEGA*eta; phi = np.angle(W).copy()
    Nb = Nsteps//6; Qb = np.zeros((n, Nb + 1)); Pb = np.zeros((n, Nb + 1)); Qb[:, 0] = np.abs(W)**2; Pb[:, 0] = phi
    for step in range(1, Nsteps + 1):
        rho_n = rho - np.sin(eta); eta_n = eta + np.exp(rho) - 1 - np.sin(eta); Wn = rho_n + OMEGA*eta_n
        phi += np.angle(Wn/W); rho, eta, W = rho_n, eta_n, Wn
        if step % 6 == 0: Qb[:, step//6] = np.abs(W)**2; Pb[:, step//6] = phi
    out = []; ok = True
    for i in range(n):
        a = 1/Q0s[i]; m = np.arange(0, Nb, dtype=np.float64)
        dev = Qb[i, :Nb] - 1/(a + m)
        rm = (Pb[i, 1:Nb + 1] - Pb[i, :Nb]) - 2*math.pi + TAU*Qb[i, :Nb]
        rows = {}
        for M in Ms:
            SN = float(np.sum(dev[M:])); RN = float(np.sum(rm[M:]))
            eM = envelope_new(a, M); eN = envelope_new(a, Nb)
            SbM, SbN, RbM, RbN = f(eM["Sbar"]), f(eN["Sbar"]), f(eM["Rbar"]), f(eN["Rbar"])
            # S^N_M = S^tail_M - S^tail_N, so the necessary condition is |S^N_M| <= Sbar'(M) + Sbar'(N) (same for R); Q_M <= bound
            okS = abs(SN) <= SbM + SbN; okR = abs(RN) <= RbM + RbN; okQ = Qb[i, M] <= f(eM["QM"])
            ok &= okS and okR and okQ
            rows[str(M)] = {"S_N_M": SN, "Sbar_M": SbM, "Sbar_N": SbN, "ratio_S": abs(SN)/(SbM + SbN), "R_N_M": RN, "Rbar_M": RbM, "Rbar_N": RbN, "ratio_R": abs(RN)/(RbM + RbN),
                            "Q_M": float(Qb[i, M]), "QM_bound": f(eM["QM"]), "ok": bool(okS and okR and okQ)}
        out.append({"Q0": Q0s[i], "theta0": ths[i], "rows": rows})
    return ok, out, Nb
if __name__ == "__main__":
    outp = sys.argv[1] if len(sys.argv) > 1 else "a1c_tail_averaging_cert.json"
    Nsteps = int(sys.argv[2]) if len(sys.argv) > 2 else 1_800_000
    g5, orbits, Nb = run_orbits(Nsteps, tuple(M for M in (1000, 3000, 10000, 30000) if M < Nsteps//12))
    res["gates"]["G5_NUM_orbits"] = bool(g5); res["G5"] = {"N_steps": Nsteps, "N_blocks": Nb, "orbits": orbits,
        "max_ratio_S": max(r["ratio_S"] for o in orbits for r in o["rows"].values()), "max_ratio_R": max(r["ratio_R"] for o in orbits for r in o["rows"].values())}
    # ---------------- negative controls ----------------
    nc1 = not harmonics(c20, -sp.Rational(1, 4), c02)                       # wrong c11 -> harmonic identity fails
    nc2 = not brute_checks(first_term=False)[0]                              # closed forms without the first-term correction fail domination
    res["gates"]["NC1_wrong_h2_caught"] = bool(nc1); res["gates"]["NC2_missing_first_term_caught"] = bool(nc2)
    ok = all(res["gates"].values()); res["ALL_PASS"] = ok
    json.dump(res, open(outp, "w"), indent=1, default=lambda o: bool(o) if isinstance(o, np.bool_) else (float(o) if isinstance(o, (np.floating, np.integer)) else str(o)))
    for k, v in res["gates"].items(): print(k, "PASS" if v else "FAIL")
    print("constants:", {k: v for k, v in res["G2_constants"].items()})
    for a, row in table.items():
        for M, v in row.items():
            print(f"a={a} M={M:>8}: Sbar'={v['Sbar']:.3e} (old {v['old_Sbar']:.3e}, x{v['gain_S']:.1f})  Rbar'={v['Rbar']:.3e} (old {v['old_Rbar']:.3e}, x{v['gain_R']:.1f})  block'={v['block']:.3e} (old {v['old_block']:.3e})  E'={v['E']:.4f} (old {v['old_E']:.4f}, x{v['gain_E']:.1f})  E'sqrt={v['E_sqrt(a+M)']:.2f}  [A0={v['A0']:.1e} A1={v['A1']:.1e} B={v['B']:.1e} C={v['C']:.1e}]")
    print("asymptotic E' sqrt(a+M) ->", res["G4_asymptotic_constant_E"], " old:", res["G4_asymptotic_old"])
    print("NUM orbits: max ratio S", res["G5"]["max_ratio_S"], " max ratio R", res["G5"]["max_ratio_R"])
    for o in orbits:
        print("Q0=%.2e th=%.1f | " % (o["Q0"], o["theta0"]) + " ".join("M=%s S=%+.2e/%.2e R=%+.2e/%.2e" % (M, r["S_N_M"], r["Sbar_M"], r["R_N_M"], r["Rbar_M"]) for M, r in o["rows"].items()))
    print("ALL PASS" if ok else "FAILURES"); sys.exit(0 if ok else 1)
