#!/usr/bin/env python3
"""A1c -- in-block angular envelope sharpening: the partial-block angular sum is a KNOWN multiple of sqrt(Q) plus O(Q).

Setting (RECOG-THM-A1B-SLIP-SCHEDULE-U; A1b cell §2): at the k-th 7-gap anchor n_{j_k} = 6 M_k + r_k (0 <= r_k <= 5),
    tau psi(a+M_k) - (k-1) pi/3 = L - o_{j_k} - P_{r_k} + tau S^tail_{M_k} - R^tail_{M_k}     (exact),
    P_r := sum_{i<r} (pi/3 - delta_T(x_{6M+i}))  (partial block),  0 <= o_{j_k} < Delta_{j_k} <= tau Q + 1.82 Q^{3/2}.
The theorem bounds |P_r| <= 5 arcsin(0.705 sqrt Q + 0.257 Q) ~ 3.5 sqrt Q (worst case per step). Here:
Lemma 12 (one-step angle law). W(Tx) = lambda W + lambda (eta - sin eta) + omega (e^rho - 1 - rho) (exact), eps := W(Tx)/(lambda W) - 1,
    eps_1 := lambda rho^2/(2W) = (2/3) sqrt Q cos^2(theta - pi/6) e^{i(pi/3 - theta)}   (W = sqrt Q e^{i theta}, rho = (2/sqrt3) Re(W e^{-i pi/6})),
    delta_T - pi/3 = sqrt Q g(theta) + varrho,  g(theta) = (2/3) cos^2(theta - pi/6) sin(pi/3 - theta),  |varrho| <= c_delta Q on U_T,
    with |eps| <= ebar(Q) = 0.7039 sqrt Q + 0.2566 Q, |eps - eps_1| <= c_2 Q, c_delta = c_2 + ebar^2/(2(1-ebar))/Q.
    KEY VALUES: g(-s pi/3) = 0 for s = 1,2,4,5 and g(-3 pi/3) = -sqrt3/4, g(0) = +sqrt3/4: four of the six phases have no first-order
    angular deviation, and the two nonzero ones cancel over a block (consistent with Delta = tau Q + O(Q^{3/2}), no sqrt Q term).
Prop. 10 (partial block). The anchor has theta = o_{j_k} in [0, Delta); the point s steps before it has theta = -s pi/3 + O(sqrt Q). Hence
    P_r = kappa(r) sqrt(Q_star) + varrho_P,  kappa(r) = -sum_{s=1}^r g(-s pi/3) = (0, 0, 0, sqrt3/4, sqrt3/4, sqrt3/4)[r],  Q_star = Q(anchor),
    |varrho_P| <= sum_{s=1}^r [ c_delta Qd + sqrt(Qd) ||g'|| (Deltabar + s alphabar) + |g(-s pi/3)| sqrt(Qd) ((1-ebar_d)^{-s} - 1) ],
    Qd = in-block amplitude ceiling (part 1b Cor. 3: f^5(Qbar_M)), Deltabar = tau Qd + 1.82 Qd^{3/2}, alphabar = arcsin(ebar(Qd)), ebar_d = ebar(Qd).
Cor. 11 (sharpened schedule, known a, r_k from the record). With the reference (a+M)^{-1/2} and the centred overshoot:
    tau psi(a+M_k) - (k-1) pi/3 + kappa(r_k) (a+M_k)^{-1/2} + (tau/2)(a+M_k)^{-1} = L + eps''_k,
    |eps''_k| <= E''(a, M_k, r_k) := xi_max + c_P(r_k) + kappa(r_k) |sqrt(Q_star) - (a+M)^{-1/2}|_max + tau Sbar'(a,M) + Rbar'(a,M),
    where xi_max bounds |(tau/2)(a+M)^{-1} - o| and the reference error uses the two-sided in-block amplitude bracket [Qd_lo, Qd].
    Asymptotically E'' sqrt(a+M) -> tau 0.7485 + 1.0753 = 1.94 (E': 5.46; E: 187.3): the in-block term is now O(1/(a+M)).
Gates: G1 exact identities (sympy); G2 constants (interval); G3 E'' < E' on the tested (a, M, r) grid only (no universal claim; IB-1),
    asymptotic constant; G4 [NUM] 12 orbits:
    |P_{r_k} - kappa sqrt(Q_star)| <= c_P bound and |eps''_k| <= E'' (+ L-estimate tolerance) at every slip; G5 part-2 enclosures recomputed with
    the new centres/envelope: narrower than with E' on every orbit, true a inside. NC1 wrong phase direction (kappa from g(+s pi/3)) and
    NC2 r shifted by one both break G4.
usage: python -I recog_a1c_inblock_angular_cert.py [OUT_JSON] [N_STEPS]
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
p1b, h1b = load("recog_a1c_tail_averaging_cert.py")
p2, h2 = load("recog_a1c_unknown_a_interval_cert.py")
I, up, lo, tau = p1b.I, p1b.up, p1b.lo, p1b.tau
fup, fdn = p2.fup, p2.fdn                              # directed float rounding (part 2)
def f(x): return fup(up(x))                            # every reported upper bound is rounded UP to a float (IB-2)
def asin_iv(x):
    """rigorous interval enclosure of arcsin on 0 <= x < 1: arcsin x = sum c_n x^{2n+1}, c_n = (2n)!/(4^n n!^2 (2n+1)) decreasing;
       truncation after n = 2 with tail 0 <= R <= c_3 x^7/(1 - x^2), c_3 = 5/112 (IB-2)"""
    x = iv.mpf(x)
    base = x + x**3/6 + 3*x**5/40
    tail = (I(5)/112)*x**7/(1 - x**2)
    return iv.mpf([lo(base), up(base + tail)])
envelope_new, old_envelope, cQ, cQp = p1b.envelope_new, p1b.old_envelope, p1b.cQ, p1b.cQp
res = {"gates": {}, "imports": {"recog_a1c_tail_averaging_cert.py": h1b, "recog_a1c_unknown_a_interval_cert.py": h2}}
s3 = iv.sqrt(I(3)); PI = iv.pi
# ---------------- G1: exact identities ----------------
X = sp.sqrt(3); rho_s, eta_s, th = sp.symbols('rho eta theta', real=True); Qs = sp.symbols('Q', positive=True)
lam = sp.Rational(1, 2) + sp.I*X/2; om = -sp.Rational(1, 2) + sp.I*X/2          # e^{i pi/3}, e^{2 i pi/3} in algebraic form
W = rho_s + om*eta_s; Wp = (rho_s - sp.sin(eta_s)) + om*(eta_s + sp.exp(rho_s) - 1 - sp.sin(eta_s))
g1a = sp.simplify(sp.expand(Wp - lam*W - lam*(eta_s - sp.sin(eta_s)) - om*(sp.exp(rho_s) - 1 - rho_s))) == 0
Wc = sp.sqrt(Qs)*sp.exp(sp.I*th)
rho_from_W = 2/X*sp.re(sp.expand(Wc*sp.exp(-sp.I*sp.pi/6)))                                   # (2/sqrt3) Re(W e^{-i pi/6})
g1b = sp.simplify(rho_from_W - 2/X*sp.sqrt(Qs)*sp.cos(th - sp.pi/6)) == 0
# rho = Re W + Im W / sqrt3 identity from W = rho + omega eta
g1b &= sp.simplify(sp.re(W) + sp.im(W)/X - rho_s) == 0
eps1 = lam*rho_from_W**2/(2*Wc)
g_expr = sp.Rational(2, 3)*sp.cos(th - sp.pi/6)**2*sp.sin(sp.pi/3 - th)
g1c = sp.simplify(sp.im(sp.expand_complex(eps1))/sp.sqrt(Qs) - g_expr) == 0
gvals = [sp.nsimplify(sp.simplify(g_expr.subs(th, -s*sp.pi/3))) for s in range(0, 7)]
g1d = gvals == [X/4, 0, 0, -X/4, 0, 0, X/4]
kappa_exact = [-sum(gvals[1:r + 1]) for r in range(0, 6)]                                     # kappa(r) = -sum_{s=1}^r g(-s pi/3)
g1e = kappa_exact == [0, 0, 0, X/4, X/4, X/4]
res["gates"]["G1_exact"] = bool(g1a and g1b and g1c and g1d and g1e)
res["G1"] = {"one_step_identity": g1a, "rho_from_W": g1b, "g_formula": g1c, "g_at_phases": [str(v) for v in gvals], "kappa": [str(v) for v in kappa_exact]}
KAPPA = [I(0), I(0), I(0), s3/4, s3/4, s3/4]
GABS = [I(0), I(0), I(0), s3/4, I(0), I(0)]      # |g(-s pi/3)| for s = 0..5 (index s)
# ---------------- G2: constants ----------------
rmax = 2*I("0.047")/s3                             # |rho|, |eta| <= (2/sqrt3) sqrt Q, sqrt Q < 0.047 on U_T
e_sqrt = I(2)/3*iv.exp(rmax); e_lin = (2/s3)**3/6  # ebar(Q) = e_sqrt sqrt Q + e_lin Q
c2 = (2/s3)**3/6*(1 + iv.exp(rmax))              # |eps - eps_1| <= c2 Q
def ebar(Q): return e_sqrt*iv.sqrt(Q) + e_lin*Q
def c_delta(Q):                                    # |delta_T - pi/3 - sqrt Q g(theta)| <= c_delta(Q) Q, increasing in Q
    e = ebar(Q); return c2 + e**2/(2*(1 - e))/Q
QUT = I("0.002209")                                # U_T subset {Q < 2209e-6}
res["G2_constants"] = {"e_sqrt": f(e_sqrt), "e_lin": f(e_lin), "c2": f(c2), "c_delta_on_U_T": f(c_delta(QUT))}
# sup |g|, sup |g'| by grid with second-derivative correction (|g''| <= 2/3 * (2^2 + ... ) crude: |g''| <= 6)
def sup_grid(fun, L2, n=20000):
    h = 2*mp.pi/n; best = mp.mpf(0)
    for j in range(n):
        v = abs(fun(iv.mpf(j*h))); best = max(best, up(v))
    return best + L2*h**2/8
g_iv = lambda t: I(2)/3*iv.cos(t - PI/6)**2*iv.sin(PI/3 - t)
gp_iv = lambda t: I(2)/3*(-2*iv.cos(t - PI/6)*iv.sin(t - PI/6)*iv.sin(PI/3 - t) - iv.cos(t - PI/6)**2*iv.cos(PI/3 - t))
# crude second-derivative ceilings: g is a trig polynomial of degree 3 with coefficients summing (in modulus) to <= 2/3*(1/2+1/2)*... use |g''| <= 9*sup|g| <= 9*(2/3) = 6, |g'''| <= 27*(2/3) = 18
SUP_G = sup_grid(g_iv, mp.mpf(6)); SUP_GP = sup_grid(gp_iv, mp.mpf(18))
res["G2_constants"].update({"sup|g|": float(SUP_G), "sup|g'|": float(SUP_GP)})
asin_ok = all(lo(asin_iv(I(x))) <= mp.asin(mp.mpf(x)) <= up(asin_iv(I(x))) for x in ("0.001", "0.01", "0.0331", "0.05"))
res["G2_constants"]["asin_enclosure_contains_mp_asin"] = bool(asin_ok)
res["gates"]["G2_constants"] = bool(asin_ok and up(e_sqrt) <= mp.mpf("0.705") and up(e_lin) <= mp.mpf("0.257") and SUP_G < 0.46 and SUP_GP < 0.70 and up(c_delta(QUT)) < 0.8)
# ---------------- the sharpened envelope ----------------
def inblock(a, M, r):
    """returns dict with Qd (in-block ceiling), Qd_lo (floor), xi_max, c_P (absolute, already multiplied), ref_err, and the pieces"""
    a = I(a); M = I(M)
    e = envelope_new(a, M)                           # part 1b: Sbar', Rbar', QM (block-base ceiling), Delta_a, kappa
    QM = e["QM"]
    Qd = QM
    for _ in range(5): Qd = Qd*(1 + ebar(Qd))**2     # in-block ceiling (any point of the block)
    # floor: Q_M^{-1} <= q_M^{-1} (1 + c_Q sqrt q_M/(1 - c_Q sqrt q_M)),  q_M^{-1} <= a + Delta_a + M + epsbar_M,  sqrt q_M <= ((1-kappa)(b'+M))^{-1/2}
    Delta_a = e["Delta_a"]; bp = a - Delta_a; kap = e["kappa"]
    q0b = 1/bp; sigma2 = 2*q0b + q0b**2; e_const = p1b.gamma0*q0b + p1b.gamma1*sigma2
    epsM = e_const + 2*p1b.gamma0*iv.log(1 + M/(2*bp))
    sq = 1/iv.sqrt((1 - kap)*(bp + M))
    QM_lo = 1/((a + Delta_a + M + epsM)*(1 + cQ*sq/(1 - cQ*sq)))
    Qd_lo = QM_lo*(1 - ebar(Qd))**10
    eb = ebar(Qd); alphabar = asin_iv(eb)
    Deltabar = tau*Qd + I("1.82")*Qd**(I(3)/2)
    cd = c_delta(Qd)
    rho_P = I(0)
    for s_ in range(1, int(r) + 1):
        rho_P += cd*Qd + iv.sqrt(Qd)*I(SUP_GP)*(Deltabar + s_*alphabar) + GABS[s_]*iv.sqrt(Qd)*((1 - eb)**(-s_) - 1)
    n = a + M
    ref_err = KAPPA[int(r)]*I(max(up(iv.sqrt(Qd) - n**(-I(1)/2)), up(n**(-I(1)/2) - iv.sqrt(Qd_lo))))
    xi_max = I(max(up(tau/(2*n)), up(Deltabar - tau/(2*n))))
    E2 = xi_max + rho_P + ref_err + tau*e["Sbar"] + e["Rbar"]
    return {"E2": E2, "xi_max": xi_max, "rho_P": rho_P, "ref_err": ref_err, "Qd": Qd, "Qd_lo": Qd_lo, "E1": e["E"], "block_old": e["block"], "Sbar": e["Sbar"], "Rbar": e["Rbar"], "QM": QM}
def centre_shift(a, M, r):                           # + kappa(r) (a+M)^{-1/2} + (tau/2) (a+M)^{-1}
    a = I(a); M = I(M); n = a + M
    return KAPPA[int(r)]*n**(-I(1)/2) + tau/(2*n)
# ---------------- G3: table ----------------
table = {}; g3 = True
for a in (625, 1000, 2500):
    table[str(a)] = {}
    for M in (1000, 10000, 100000, 1000000, 10000000):
        row = {}
        for r in range(6):
            ib = inblock(a, M, r)
            row[str(r)] = {"E2": f(ib["E2"]), "E1": f(ib["E1"]), "gain": f(ib["E1"])/f(ib["E2"]), "inblock_new": f(ib["xi_max"] + ib["rho_P"] + ib["ref_err"]), "inblock_old": f(ib["block_old"]),
                           "xi_max": f(ib["xi_max"]), "rho_P": f(ib["rho_P"]), "ref_err": f(ib["ref_err"]), "E2_sqrt": f(ib["E2"])*math.sqrt(a + M)}
            g3 &= row[str(r)]["E2"] < row[str(r)]["E1"]
        table[str(a)][str(M)] = row
lead = tau*(p1b.abs_phi1/p1b.den(1) + p1b.abs_phi3/p1b.den(3)) + p1b.abs_lam1/p1b.den(1) + p1b.abs_lam3/p1b.den(3)
res["G3_table"] = table; res["G3_asymptotic_constant"] = [f(lo(lead)), f(up(lead))]
res["gates"]["G3_table"] = bool(g3)
# ---------------- [NUM] ----------------
TAU = float(up(tau)); OMEGA = complex(-0.5, math.sqrt(3)/2)
def simulate(Q0s, ths, N):
    n = len(Q0s)
    rho = np.array([math.sqrt(Q0s[i])*math.cos(ths[i]) for i in range(n)]); eta = np.array([math.sqrt(Q0s[i])*math.sin(ths[i]) for i in range(n)])/OMEGA.imag
    rho = rho - OMEGA.real*eta; Wv = rho + OMEGA*eta; phi = np.angle(Wv).copy()
    hist = np.zeros((n, N + 1)); Qh = np.zeros((n, N + 1)); hist[:, 0] = phi; Qh[:, 0] = np.abs(Wv)**2
    anchors = [[] for _ in range(n)]
    for step in range(1, N + 1):
        rho_n = rho - np.sin(eta); eta_n = eta + np.exp(rho) - 1 - np.sin(eta); Wn = rho_n + OMEGA*eta_n
        phi += np.angle(Wn/Wv)
        bev = (eta < 0) & (eta_n >= 0) & (rho > 0) & (rho_n > 0)
        for i in np.nonzero(bev)[0]: anchors[i].append(step)
        rho, eta, Wv = rho_n, eta_n, Wn
        hist[:, step] = phi; Qh[:, step] = np.abs(Wv)**2
    Mend = N//6; Psi_end = (phi - 2*math.pi*Mend) - TAU*np.log(np.abs(Wv)**2)
    return anchors, hist, Qh, Psi_end
if __name__ == "__main__":
    outp = sys.argv[1] if len(sys.argv) > 1 else "a1c_inblock_angular_cert.json"
    N = int(sys.argv[2]) if len(sys.argv) > 2 else 1_800_000
    Q0s = [1/625]*4 + [1/1000]*4 + [1/2500]*4; ths = [0.3, 1.7, 3.9, 5.1]*3
    anc, hist, Qh, Psi = simulate(Q0s, ths, N)
    KAP = [0.0, 0.0, 0.0, math.sqrt(3)/4, math.sqrt(3)/4, math.sqrt(3)/4]
    g4 = True; orbits = []; worst_P = 0.0; worst_E = 0.0
    nc1_hit = False; nc2_hit = False
    for i in range(12):
        a = 1/Q0s[i]; an = anc[i]; n0 = an[0]; ell0 = math.floor(hist[i, n0]/(2*math.pi)); L = math.pi/3*n0 - 2*math.pi*ell0 + Psi[i]
        Ltol = TAU*math.sqrt(Qh[i, -1])
        slips = []; k = 0
        for j in range(1, len(an)):
            if an[j] - an[j - 1] == 7:
                k += 1; n_anchor = an[j - 1]; M = n_anchor//6; r = n_anchor % 6
                if M < 1: continue
                # exact partial block and anchor amplitude from the simulation
                P_r = sum(math.pi/3 - (hist[i, 6*M + t + 1] - hist[i, 6*M + t]) for t in range(r))
                Qstar = Qh[i, n_anchor]
                ib = inblock(a, M, r)
                resid = P_r - KAP[r]*math.sqrt(Qstar); bound = f(ib["rho_P"])
                okP = abs(resid) <= bound if r > 0 else abs(resid) <= 1e-12
                ck = TAU*float(mp.digamma(a + M)) - (k - 1)*math.pi/3 + f(centre_shift(a, M, r))
                eps2 = ck - L; E2 = f(ib["E2"]); okE = abs(eps2) <= E2 + Ltol
                g4 &= okP and okE
                worst_P = max(worst_P, abs(resid)/bound if r > 0 else 0.0); worst_E = max(worst_E, abs(eps2)/E2)
                # negative controls on the same data: wrong direction (kappa from g(+s pi/3): sum_{s<=r} g(s pi/3) = -(0,0,0,sqrt3/4,...)?) -> use -KAP; r shifted by one
                if r >= 3 and abs(P_r + KAP[r]*math.sqrt(Qstar)) > bound: nc1_hit = True
                r2 = (r + 1) % 6
                if KAP[r2] != KAP[r] and abs(P_r - KAP[r2]*math.sqrt(Qstar)) > bound: nc2_hit = True
                slips.append({"k": k, "M": M, "r": r, "P_r": P_r, "kappa_sqrtQstar": KAP[r]*math.sqrt(Qstar), "resid": resid, "resid_bound": bound, "eps2": eps2, "E2": E2, "E1": f(ib["E1"]),
                              "old_inblock_bound": f(ib["block_old"]), "ratio_P": (abs(resid)/bound if r > 0 else 0.0), "ratio_E": abs(eps2)/E2})
        orbits.append({"a": a, "theta0": ths[i], "L_est": L, "L_tol": Ltol, "slips": slips})
    res["gates"]["G4_NUM_residuals_within_bounds"] = bool(g4)
    res["G4"] = {"orbits": orbits, "max_ratio_P": worst_P, "max_ratio_E": worst_E}
    res["gates"]["NC1_wrong_direction_caught"] = bool(nc1_hit); res["gates"]["NC2_wrong_r_caught"] = bool(nc2_hit)
    # ---------------- G5: part-2 enclosures with the sharpened centres/envelope ----------------
    def c_k_new(a_iv, k, M, r): return p2.c_k(a_iv, k, M) + centre_shift(a_iv, M, r)
    def E_k_new(a_iv, M, r): return inblock(a_iv, M, r)["E2"]
    # monkeypatch part 2: slips carry (k, M, r); classify unpacks (k, M) -> wrap
    def classify_new(a_box, slips):
        vals = [(c_k_new(a_box, k, M, r), E_k_new(a_box, M, r)) for k, M, r in slips]
        lo_lo = max(lo(c - E) for c, E in vals); hi_hi = min(up(c + E) for c, E in vals)
        lo_hi = max(up(c - E) for c, E in vals); hi_lo = min(lo(c + E) for c, E in vals)
        return ("EXCLUDED" if lo_lo > hi_hi else ("SURE" if lo_hi <= hi_lo else "UNDECIDED")), (lo_lo, hi_hi)
    p2.classify = classify_new
    g5 = True; part2 = []
    for i in range(12):
        a = 1/Q0s[i]; an = anc[i]
        sl3 = []; sl2 = []; k = 0
        for j in range(1, len(an)):
            if an[j] - an[j - 1] == 7:
                k += 1; n_anchor = an[j - 1]; M = n_anchor//6; r = n_anchor % 6
                if M >= 1: sl3.append((k, M, r)); sl2.append((k, M))
        if len(sl2) < 2: continue
        (k1, M1), (k2, M2) = sl2[0], sl2[1]
        am, ap = p2.lemma8_interval(k1, M1, k2, M2)
        comps, inner, n_eval, und = p2.enclosure(sl3, am, ap)
        hull = [comps[0][0], comps[-1][1]] if comps else None
        # the part-2 widths (envelope E', uncorrected centres) are read from the part-2 JSON for comparison
        old_w = None
        try:
            r2 = json.load(open(os.path.join(HERE, "..", "a1c_2", "a1c_unknown_a_interval_cert.json")))
            for o in r2["orbits"]:
                if abs(o["a"] - a) < 1e-9 and abs(o["theta0"] - ths[i]) < 1e-9: old_w = o["final"]["width"]; old_L = o["final"]["L_hull"]
        except Exception: pass
        Lh = [min(c[2] for c in comps), max(c[3] for c in comps)] if comps else None
        contains = any(c[0] <= a <= c[1] for c in comps)
        g5 &= contains and (old_w is None or (hull[1] - hull[0]) < old_w)
        part2.append({"a": a, "theta0": ths[i], "slips": sl3, "a_hull_new": hull, "width_new": hull[1] - hull[0] if hull else None, "width_old_E1": old_w, "L_hull_new": Lh, "L_hull_old": old_L if old_w is not None else None,
                      "inner": inner, "undecided": und, "contains_a": contains, "n_boxes": n_eval})
    res["gates"]["G5_part2_narrower"] = bool(g5); res["G5"] = part2
    res["N_steps"] = N
    ok = all(res["gates"].values()); res["ALL_PASS"] = ok
    json.dump(res, open(outp, "w"), indent=1, default=lambda o: bool(o) if isinstance(o, np.bool_) else (float(o) if isinstance(o, (np.floating, np.integer)) else str(o)))
    for k, v in res["gates"].items(): print(k, "PASS" if v else "FAIL")
    print("constants:", res["G2_constants"])
    for a, rows in table.items():
        for M, row in rows.items():
            print(f"a={a} M={M:>8}: " + "  ".join(f"r={r}: E''={v['E2']:.4g} (E' {v['E1']:.4g}, x{v['gain']:.1f}; inblock {v['inblock_new']:.2e} vs {v['inblock_old']:.2e})" for r, v in row.items() if r in ('0', '3', '5')) + f"  E''sqrt(r=5)={row['5']['E2_sqrt']:.2f}")
    print("asymptotic E'' sqrt(a+M) ->", res["G3_asymptotic_constant"])
    print("NUM: max ratio P", worst_P, " max ratio E", worst_E)
    for o in orbits: print("a=%4d th=%.1f: " % (o["a"], o["theta0"]) + " ".join("k%d(M=%d,r=%d) P=%+.2e kap=%.2e res=%+.1e/%.1e eps''=%+.2e/E''=%.2e(E'=%.2e)" % (s["k"], s["M"], s["r"], s["P_r"], s["kappa_sqrtQstar"], s["resid"], s["resid_bound"], s["eps2"], s["E2"], s["E1"]) for s in o["slips"]))
    for p in part2: print("a=%4d th=%.1f: new a-hull %s (w=%.1f; old %.1f)  L-hull %s (old %s)" % (p["a"], p["theta0"], [round(x, 1) for x in p["a_hull_new"]] if p["a_hull_new"] else None, p["width_new"] or 0, p["width_old_E1"] or 0, [round(x, 4) for x in p["L_hull_new"]] if p["L_hull_new"] else None, [round(x, 4) for x in p["L_hull_old"]] if p["L_hull_old"] else None))
    print("ALL PASS" if ok else "FAILURES"); sys.exit(0 if ok else 1)
