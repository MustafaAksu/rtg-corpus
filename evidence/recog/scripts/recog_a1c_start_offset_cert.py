#!/usr/bin/env python3
"""A1c -- start-offset centring (bounded feasibility): the start angle from the record, the signed start offset a - b via h_2, and the
known-a envelope with the start offset centred.

Objects (known a = 1/Q_0; record (n_0; g), slips (k, M_k, r_k)). Chart start z_0 = h^{-1}(W_0), q_0 = |z_0|^2, b = 1/q_0, Theta_0 = chart angle;
primitive start angle theta_W0 = Arg W_0 in (-pi, pi]; Theta_0 = theta_W0 - D_Theta(z_0), |D_Theta(z_0)| <= sup|d| sqrt(q_0) + c_1 q_0 =: D0+.
Lemma 16 (first-anchor sector). phi_{n_0} = theta_W0 + sum_{i<n_0} delta_T(x_i) in [2 pi l_0, 2 pi l_0 + delta_T(x_{n_0-1}))  (Lemma A) and
    |delta_T - pi/3| <= alphabar_0 := arcsin(ebar(Q^dd)), Q^dd = amplitude ceiling on the first n_0 steps (f^{n_0}(1/a)). Hence, mod 2 pi,
    theta_W0 in [ -n_0 pi/3 - n_0 alphabar_0,  -(n_0-1) pi/3 + (n_0+1) alphabar_0 ]  -- a sector of width pi/3 + (2 n_0 + 1) alphabar_0;
    Theta_0 lies in the sector widened by D0+ on each side.  (All n_0 >= 1; l_0 drops out mod 2 pi.)
Lemma 17 (signed start offset). a - b = -D_Q(z_0)/(q_0 Q_0) exactly; with D_Q = q_0^{3/2} Phi(Theta_0) + delta, |delta| <= c'_Q q_0^2 (D5):
    a - b = -Phi(Theta_0) sqrt(a) + eps_b,   |eps_b| <= beta(a) := sup|Phi| sqrt(a) * x+/(2 sqrt(1 - x+)) + c'_Q (256/225),
    x+ = c_Q (256/225)^{3/2} a^{-1/2}  (so beta is O(1), ~0.80 for a >= 625).  Given Theta_0 in an interval T:
    a - b in [ -max_T Phi sqrt(a) - beta,  -min_T Phi sqrt(a) + beta ]   (signed; max/min of the trig polynomial Phi on T by grid + Lipschitz).
Prop. 18 (start angle from (a, L)). Psi_{z,inf} = Theta_0 - tau log q_0 + M(z_0) (RECOG-DEF, M = retained memory; RECOG-THM-R9-MEMORY:
    M = q_0 [c_iso + Lambda_1(Theta_0)] + R, |R| <= 517 q_0^2, c_iso = -4 sqrt3/27, |Lambda_1| <= |G| = 0.0076520) and Psi_{z,inf} = Psi_{W,inf} =
    L - (pi/3) n_0 + 2 pi l_0 (RECOG-THM-A1A-PHASE-EXISTENCE-ALT; RESULT). Hence, mod 2 pi,
    Theta_0 = L - (pi/3) n_0 - tau log b - c_iso q_0 - Lambda_1 q_0 - R,   with L in the decoder window, b in its current range.
Cor. 19 (centred offset, iterated). Start: b in [a - Delta_a, a + Delta_a], L-window I_K from (c''', E''') (combined-tail cell). Repeat:
    Theta_0-interval = (Lemma 16 sector) cap (Prop. 18 interval) on the circle -> Phi range -> omega := a - b in [omega-, omega+] (Lemma 17)
    -> centred A_0: A_0 = omega S_M(b), S_M(b) = sum_{m>=M} 1/((a+m)(b+m)) in [1/(c+ + M), 1/(c- + M)^2 + 1/(c- + M)], c+ = max(a, b+), c- = min(a, b-)
    -> schedule centre c4_k = c'''_k - tau mid(omega S) (eps''' carries + tau A_M), envelope E4_k = E'''_k - tau A0_k(part 1b) + tau halfwidth(omega S)
    -> new L-window I_K from (c4, E4); new b-range [a - omega+, a - omega-].  Each step maps valid enclosures to valid enclosures; 4 rounds.
Invariant (Cor. 19): at every round the true (a, L, b, Theta_0, omega) satisfies all current enclosures (b-range, Theta_0 arc, omega interval, L window);
    each round only applies enclosure-valid maps, so the invariant propagates. SO-1: n_0 <= 7 from hat phi_0 in (-pi, pi] and delta_T >= pi/3 - arcsin 0.04654
    on U_T (adopted); the amplitude majorant f^{n_0}(Q_0) is capped by the U_T bound 2209e-6 since the orbit stays in U_T. SO-2: circle arcs are intersected
    over every 2 pi branch that can meet; all reported arc/interval ends are rounded outward.
Gates: G1 constants (beta(a), sup|Phi|, sup|Phi'|, sup|d|) and the exact identities (sympy: Phi from h_2; a - b = -D_Q/(q_0 Q_0));
    G2 [NUM] the Lemma-16 sector contains the true theta_W0 for all 12 orbits (all n_0 classes that occur); G3 [NUM] the final Theta_0 interval
    contains theta_W0 within the D0+ allowance; G4 [NUM] |eps4_k| <= E4_k at every slip (L from the run's end, corrected as in the combined-tail
    cell) and E4 < E''' at every slip; G5 the omega-interval width < 2 Delta_a for every orbit (improvement over the uncentred offset).
    NC1 the sector built with n_0 + 1 excludes the true angle for some orbit; NC2 Phi with the wrong sign breaks G4.
usage: python -I recog_a1c_start_offset_cert.py [OUT_JSON] [N_STEPS]
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
pct, hct = load("recog_a1c_combined_tail_cert.py")        # loads in-block, part 2, part 1b
pib, p2, p1b = pct.pib, pct.p2, pct.p1b
I, up, lo, tau, f = p1b.I, p1b.up, p1b.lo, p1b.tau, pib.f
fup, fdn, asin_iv = p2.fup, p2.fdn, pib.asin_iv
res = {"gates": {}, "imports": {"recog_a1c_combined_tail_cert.py": hct, **pct.res["imports"]}}
s3 = iv.sqrt(I(3)); PI = iv.pi; TWOPI = 2*mp.pi
cQ, cQp = p1b.cQ, p1b.cQp
C1 = I("0.261"); C_ISO = -4*s3/27; ABS_G = I("0.0076520"); C2_R9 = I(517)
SUP_D = I(pct.SUP_D)
# ---------------- G1: constants and identities ----------------
X = sp.sqrt(3); th = sp.symbols('Theta', real=True); r_ = sp.symbols('r', positive=True); q0s, Q0s = sp.symbols('q0 Q0', positive=True)
c20 = -sp.Rational(1, 12) - sp.I*X/12; c11 = -sp.Rational(1, 3); c02 = sp.Rational(1, 24) - sp.I*X/24
z = r_*(sp.cos(th) + sp.I*sp.sin(th)); zb = r_*(sp.cos(th) - sp.I*sp.sin(th))
Phi_from_h2 = sp.simplify(sp.expand(2*sp.re(sp.expand(zb*(c20*z**2 + c11*z*zb + c02*zb**2))))/r_**3)
Phi_pub = -sp.Rational(5, 6)*sp.cos(th) + X/6*sp.sin(th) + sp.Rational(1, 12)*sp.cos(3*th) - X/12*sp.sin(3*th)
g1a = sp.simplify(sp.expand(sp.expand_trig(Phi_from_h2 - Phi_pub))) == 0
DQ = sp.symbols('D_Q', real=True)
g1b = sp.simplify((1/(q0s + DQ) - 1/q0s) - (-DQ/(q0s*(q0s + DQ)))) == 0           # a - b = Q0^{-1} - q0^{-1} = -D_Q/(q0 Q0), Q0 = q0 + D_Q
Phi_iv = lambda t: -I(5)/6*iv.cos(t) + s3/6*iv.sin(t) + I(1)/12*iv.cos(3*t) - s3/12*iv.sin(3*t)
LIP_PHI = up(iv.sqrt((I(5)/6)**2 + (s3/6)**2) + 3*iv.sqrt((I(1)/12)**2 + (s3/12)**2))     # |Phi'| <= |phi1| + 3|phi3| = 1.3819
SUP_PHI = pct.sup_grid(Phi_iv, mp.mpf(1)*(mp.sqrt(28)/6 + 9/mp.mpf(6)))                   # second-derivative ceiling |phi1| + 9|phi3|
def beta_of(a):
    a = I(a); xp = cQ*(I(256)/225)**(I(3)/2)/iv.sqrt(a)
    return I(SUP_PHI)*iv.sqrt(a)*xp/(2*iv.sqrt(1 - xp)) + cQp*I(256)/225
res["G1"] = {"Phi_from_h2_eq_published": g1a, "offset_identity": g1b, "sup|Phi|": float(SUP_PHI), "Lip_Phi": float(LIP_PHI), "beta(625)": f(beta_of(625)), "beta(2500)": f(beta_of(2500)), "beta(1e6)": f(beta_of(10**6))}
res["gates"]["G1_constants_identities"] = bool(g1a and g1b and up(beta_of(625)) < 0.85)
# ---------------- angle intervals on the circle ----------------
def Phi_range(t_lo, t_hi, n=4000):
    """rigorous [min, max] of Phi on [t_lo, t_hi] (mp floats): grid values +- Lip * h/2"""
    t_lo = mp.mpf(t_lo); t_hi = mp.mpf(t_hi); h = (t_hi - t_lo)/n
    vals = [Phi_iv(I(t_lo + j*h)) for j in range(n + 1)]
    return mp.mpf(min(lo(v) for v in vals)) - LIP_PHI*h/2, mp.mpf(max(up(v) for v in vals)) + LIP_PHI*h/2
def circ_intersect(A, B):
    """intersection of two arcs [lo, hi] (widths < 2 pi) on the circle; returns the hull of the overlapping pieces or None.
       The shift range covers every k with [B + 2 pi k] possibly meeting A (SO-2): k from floor((A_lo - B_hi)/2pi) - 1 to ceil((A_hi - B_lo)/2pi) + 1"""
    assert A[1] - A[0] < TWOPI and B[1] - B[0] < TWOPI
    pieces = []
    kmin = int(mp.floor((A[0] - B[1])/TWOPI)) - 1; kmax = int(mp.ceil((A[1] - B[0])/TWOPI)) + 1
    for k in range(kmin, kmax + 1):
        lo_ = max(A[0], B[0] + k*TWOPI); hi_ = min(A[1], B[1] + k*TWOPI)
        if lo_ <= hi_: pieces.append((lo_, hi_))
    if not pieces: return None
    return (min(p[0] for p in pieces), max(p[1] for p in pieces))
N0_MAX = 7                                   # Lemma 16 (SO-1): hat phi_0 in (-pi, pi], delta_T >= pi/3 - arcsin(0.04654) on U_T (branch (B), adopted) => n_0 <= 7
Q_UT = I("0.002209")                         # U_T subset {Q < 2209e-6} (DYAD-THM-PRIM-CTR): every point of the orbit stays in U_T, so the amplitude ceiling is capped there
ALPHA_T = asin_iv(I("0.04654"))
assert up(2*PI/(PI/3 - ALPHA_T)) < N0_MAX   # 2 pi / (pi/3 - alpha_T) = 6.28.. < 7: the first crossing of the next multiple of 2 pi happens within 7 steps
def sector(n0, a):
    """Lemma 16: arc for theta_W0 (mod 2 pi) and the widened arc for Theta_0; requires 1 <= n0 <= N0_MAX (SO-1)"""
    assert 1 <= int(n0) <= N0_MAX, "first anchor outside the certified range"
    a = I(a); Q = 1/a
    for _ in range(int(n0)): Q = iv.mpf([lo(Q), min(up(Q*(1 + pib.ebar(Q))**2), up(Q_UT))])    # f^{n0}(Q_0) capped by the tube bound (SO-1)
    alpha0 = asin_iv(pib.ebar(Q))
    lo_ = -n0*PI/3 - n0*alpha0; hi_ = -(n0 - 1)*PI/3 + (n0 + 1)*alpha0
    q0p = I(256)/(225*a); D0 = SUP_D*iv.sqrt(q0p) + C1*q0p
    return (lo(lo_), up(hi_)), (lo(lo_ - D0), up(hi_ + D0)), f(D0)
def theta0_from_L(a, n0, Lw, bw):
    """Prop. 18: arc for Theta_0 (mod 2 pi) from L in Lw = [L-, L+] and b in bw = [b-, b+]"""
    a = I(a); Lint = iv.mpf([Lw[0], Lw[1]]); bint = iv.mpf([bw[0], bw[1]]); q0 = 1/bint
    Mmem = C_ISO*q0 + iv.mpf([-1, 1])*(ABS_G*q0 + C2_R9*q0**2)
    T = Lint - PI/3*n0 - tau*iv.log(bint) - Mmem
    return (lo(T), up(T))
def omega_interval(a, Tarc):
    pmin, pmax = Phi_range(Tarc[0], Tarc[1]); b = beta_of(a); sa = iv.sqrt(I(a))
    return (lo(-I(pmax)*sa - b), up(-I(pmin)*sa + b))
def S_bracket(a, M, bw):
    a = I(a); M = I(M); cp = iv.mpf(max(lo(a), mp.mpf(bw[1]))); cm = iv.mpf(min(lo(a), mp.mpf(bw[0])))
    return iv.mpf([lo(1/(cp + M)), up(1/(cm + M)**2 + 1/(cm + M))])
def window(a, slips, centre_fn, E_fn):
    """known-a decoder window I_K = [max_k (c_k - E_k), min_k (c_k + E_k)] (outer: interval c_k, upper E_k)"""
    los = []; his = []
    for k, M, r in slips:
        c = p2.c_k(I(a), k, M) + centre_fn(a, M, r); E = E_fn(a, M, r)
        los.append(lo(c - E)); his.append(up(c + E))
    if max(los) > min(his): raise RuntimeError("empty L window (inconsistent centres/envelopes)")
    return (max(los), min(his))
def centred(a, n0, slips, rounds=4, phi_sign=+1):
    """Cor. 19 iteration; returns the history and the final (centre, envelope) functions"""
    a_ = I(a); Delta_a = f(p1b.envelope_new(a, 1)["Delta_a"])
    bw = (mp.mpf(a) - Delta_a, mp.mpf(a) + Delta_a)
    arcW, arcT, D0 = sector(n0, a)
    base = {}
    for k, M, r in slips:
        c = pct.combined(a, M, r); base[(k, M, r)] = (c["E3"], c["tauA0"])
    cfun = lambda a_, M, r: pct.centre_shift(a_, M, r); Efun = lambda a_, M, r: base[next(key for key in base if key[1] == M)][0]
    Lw = window(a, slips, cfun, Efun)
    hist = [{"round": 0, "L_window": [fdn(Lw[0]), fup(Lw[1])], "L_width": fup(Lw[1] - Lw[0]), "b_range": [fdn(bw[0]), fup(bw[1])]}]
    omega = None; Tarc = None
    for it in range(1, rounds + 1):
        T18 = theta0_from_L(a, n0, Lw, bw)
        Tarc = circ_intersect(arcT, T18)
        if Tarc is None: raise RuntimeError("empty Theta_0 interval (inconsistent record)")
        om = omega_interval(a, Tarc)
        if phi_sign < 0: om = (-om[1], -om[0])                                  # negative control: Phi with the wrong sign
        omega = om; om_iv = iv.mpf([om[0], om[1]])
        bw_new = (mp.mpf(a) - om[1], mp.mpf(a) - om[0])                       # b = a - omega
        shifts = {}; envs = {}
        for key in base:
            k, M, r = key
            prod = om_iv*S_bracket(a, M, bw_new)
            mid = (lo(prod) + up(prod))/2; half = (up(prod) - lo(prod))/2
            E3, tauA0 = base[key]
            shifts[key] = -tau*I(mid); envs[key] = iv.mpf([0, up(E3 - tauA0 + tau*half)])     # eps''' contains + tau A_M ~ + tau omega S: subtract its centre
        cfun2 = lambda a_, M, r, sh=shifts: pct.centre_shift(a_, M, r) + sh[next(key for key in sh if key[1] == M)]
        Efun2 = lambda a_, M, r, en=envs: en[next(key for key in en if key[1] == M)]
        Lw = window(a, slips, cfun2, Efun2); bw = bw_new
        hist.append({"round": it, "Theta0_arc": [fdn(Tarc[0]), fup(Tarc[1])], "Theta0_width": fup(Tarc[1] - Tarc[0]), "omega": [fdn(om[0]), fup(om[1])], "omega_width": fup(om[1] - om[0]),
                     "L_window": [fdn(Lw[0]), fup(Lw[1])], "L_width": fup(Lw[1] - Lw[0]), "b_range": [fdn(bw[0]), fup(bw[1])]})     # outward float rounding (SO-2)
        cfun, Efun = cfun2, Efun2
    return hist, cfun, Efun, arcW, arcT, D0, Delta_a, omega, Tarc
# ---------------- [NUM] ----------------
TAU = float(up(tau))
if __name__ == "__main__":
    outp = sys.argv[1] if len(sys.argv) > 1 else "a1c_start_offset_cert.json"
    N = int(sys.argv[2]) if len(sys.argv) > 2 else 1_800_000
    Q0s = [1/625]*4 + [1/1000]*4 + [1/2500]*4; ths = [0.3, 1.7, 3.9, 5.1]*3
    anc, hist_phi, Qh, Psi = pib.simulate(Q0s, ths, N); Nb = N//6
    g2 = g3 = g4 = g5 = True; nc1 = False; nc2 = False; orbits = []
    for i in range(12):
        a = 1/Q0s[i]; an = anc[i]; n0 = an[0]; theta_W0 = (ths[i] + math.pi) % (2*math.pi) - math.pi      # principal start angle
        slips = []; k = 0
        for j in range(1, len(an)):
            if an[j] - an[j - 1] == 7:
                k += 1; nA = an[j - 1]; M = nA//6; r = nA % 6
                if M >= 1: slips.append((k, M, r))
        hist, cfun, Efun, arcW, arcT, D0, Delta_a, omega, Tarc = centred(a, n0, slips)
        # G2: sector contains theta_W0 (mod 2 pi)
        in_sec = circ_intersect(arcW, (theta_W0, theta_W0)) is not None; g2 &= in_sec
        in_sec_wrong = circ_intersect(sector(n0 + 1, a)[0], (theta_W0, theta_W0)) is not None
        if not in_sec_wrong: nc1 = True
        # G3: final Theta_0 arc contains theta_W0 within D0 allowance
        in_T = circ_intersect((Tarc[0] - D0, Tarc[1] + D0), (theta_W0, theta_W0)) is not None; g3 &= in_T
        # G4: envelope test with the corrected L estimate (as in the combined-tail cell)
        ell0 = math.floor(hist_phi[i, n0]/(2*math.pi)); thN = hist_phi[i, 6*Nb] % (2*math.pi)
        dN = -math.sqrt(3)/12*math.cos(thN) + 0.25*math.sin(thN) - math.sqrt(3)/24*math.cos(3*thN) - math.sin(3*thN)/24
        L = math.pi/3*n0 - 2*math.pi*ell0 + (hist_phi[i, 6*Nb] - 2*math.pi*Nb) + TAU*float(mp.digamma(a + Nb)) - dN/math.sqrt(a + Nb)
        Ltol = TAU*Delta_a/(a + Nb) + 3/(a + Nb)
        inv_ok = all(h["L_window"][0] - Ltol <= L <= h["L_window"][1] + Ltol for h in hist); g4 &= inv_ok      # invariant: the true L stays in every round's window
        rows = []
        for (k, M, r) in slips:
            ck = TAU*float(mp.digamma(a + M)) - (k - 1)*math.pi/3 + f(cfun(a, M, r)); E4 = f(Efun(a, M, r))
            E3 = f(pct.combined(a, M, r)["E3"]); eps4 = ck - L
            ok = abs(eps4) <= E4 + Ltol and E4 < E3; g4 &= ok
            rows.append({"k": k, "M": M, "r": r, "eps4": eps4, "E4": E4, "E3": E3, "ratio": abs(eps4)/E4, "gain_vs_E3": E3/E4})
        g5 &= omega[1] - omega[0] < 2*Delta_a
        # NC2: wrong sign of Phi
        try:
            h_nc, cf_nc, Ef_nc, *_ = centred(a, n0, slips, phi_sign=-1)
            for (k, M, r) in slips:
                ck = TAU*float(mp.digamma(a + M)) - (k - 1)*math.pi/3 + f(cf_nc(a, M, r)); E4n = f(Ef_nc(a, M, r))
                if abs(ck - L) > E4n + Ltol: nc2 = True
        except RuntimeError: nc2 = True                                   # an empty window / empty Theta_0 arc counts as detection
        orbits.append({"a": a, "theta0": ths[i], "theta_W0_principal": theta_W0, "n0": int(n0), "sector_thetaW": [fdn(arcW[0]), fup(arcW[1])], "sector_in": in_sec, "D0_plus": D0,
                       "history": hist, "final_Theta0_arc": [fdn(Tarc[0]), fup(Tarc[1])], "Theta0_arc_contains": in_T, "omega_final": [fdn(omega[0]), fup(omega[1])], "omega_width": fup(omega[1] - omega[0]),
                       "two_Delta_a": 2*Delta_a, "slips": rows, "L_est": L, "L_tol": Ltol})
    res["gates"].update({"G2_sector_contains_thetaW0": bool(g2), "G3_Theta0_arc_contains": bool(g3), "G4_eps4_within_E4_and_E4_below_E3": bool(g4), "G5_omega_narrower_than_2Delta_a": bool(g5),
                         "NC1_wrong_n0_sector_excludes": bool(nc1), "NC2_wrong_Phi_sign_breaks_G4": bool(nc2)})
    res["orbits"] = orbits; res["N_steps"] = N
    ok = all(res["gates"].values()); res["ALL_PASS"] = ok
    json.dump(res, open(outp, "w"), indent=1, default=lambda o: bool(o) if isinstance(o, np.bool_) else (float(o) if isinstance(o, (np.floating, np.integer)) else str(o)))
    for k, v in res["gates"].items(): print(k, "PASS" if v else "FAIL")
    print("G1:", res["G1"])
    for o in orbits:
        print("a=%4d th=%.1f n0=%d: sector theta_W [%.3f, %.3f] (true %.3f) | final Theta0 arc width %.4f | omega=[%.2f, %.2f] (w=%.2f; 2 Delta_a=%.1f) | L width: %s"
              % (o["a"], o["theta0"], o["n0"], o["sector_thetaW"][0], o["sector_thetaW"][1], o["theta_W0_principal"], o["final_Theta0_arc"][1] - o["final_Theta0_arc"][0], o["omega_final"][0], o["omega_final"][1], o["omega_width"], o["two_Delta_a"],
                 [round(h["L_width"], 6) for h in o["history"]]))
        print("      " + " ".join("k%d(M=%d,r=%d) eps=%+.1e/E4=%.1e (E'''=%.1e, x%.1f)" % (s["k"], s["M"], s["r"], s["eps4"], s["E4"], s["E3"], s["gain_vs_E3"]) for s in o["slips"]))
    print("ALL PASS" if ok else "FAILURES"); sys.exit(0 if ok else 1)
