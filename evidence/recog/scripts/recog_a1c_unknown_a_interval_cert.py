#!/usr/bin/env python3
"""A1c part 2 -- certified unknown-a parameter interval from the slip record (outer enclosures by interval boxes).

Setting (RECOG-THM-A1B-SLIP-SCHEDULE-U, recog-v0.3.24 §6.13b, with the part-1b envelope E'(a,M) of
recog_a1c_tail_averaging_cert.py, imported unchanged): for x0 in U, a = 1/Q_0 >= 625 UNKNOWN, slip record {(k, M_k)}, M_k >= 1,
    c_k(a) := tau psi(a + M_k) - (k-1) pi/3 = L + eps_k,   |eps_k| <= E'(a, M_k)      (E' conditional on the Dyadic (D5) constants).
Unknowns (a, L). Admissible region and its a-projection:
    R_K = {(a, L): a >= 625, |c_k(a) - L| <= E'(a, M_k) for all k <= K},
    A_K = {a >= 625: max_j (c_j - E'_j)(a) <= min_j (c_j + E'_j)(a)}   (1-D Helly: all pairwise conditions).
(a_true, L_true) in R_K, a_true in A_K -- immediate from the theorem.  Nothing here uses monotonicity of E' in a.
Lemma 7 (digamma bracket, x > 0):  ln x - 1/(2x) - 1/(12x^2) <= psi(x) <= ln x - 1/(2x) - 1/(12x^2) + 1/(120 x^4)   (Stirling, alternating remainder).
Lemma 8 (first finite interval, two slips k1 < k2): h(a) := tau [psi(a+M_2) - psi(a+M_1)] is strictly decreasing in a (trigamma decreasing),
    and |h(a) - (k2-k1) pi/3| <= E'(a,M_1) + E'(a,M_2) <= 0.62 (part-1b Lemma 6); since (k2-k1) pi/3 - 0.62 >= 0.427 > 0 the set is a finite
    interval [a^-, a^+] = h^{-1}([D pi/3 - 0.62, D pi/3 + 0.62]) cap [625, inf), computed by bisection with the interval digamma.
Prop. 4 (outer enclosure): bisection of [a^-, a^+] into boxes; a box is EXCLUDED iff for some pair (j,k)  inf_box(c_j - E'_j) > sup_box(c_k + E'_k)
    (interval enclosures, outward rounding); boxes neither excluded nor wider than w_min are kept. The union of kept boxes contains A_K;
    the L-hull over kept boxes, [max_k inf(c_k - E'_k), min_k sup(c_k + E'_k)] per box, contains the L-projection of R_K.
Gates: G1 digamma bracket contains mp.digamma at 2000 points, h decreasing (trigamma sign); G2 Lemma-8 intervals contain a_true (12 orbits);
       G3 the all-slip enclosure contains a_true and its L-hull contains the [NUM] L estimate (tolerance = tail scale of the estimate);
       G4 nesting: enclosure(K slips) subset Lemma-8 interval, widths non-increasing in K.
Negative controls: NC1 a digamma bracket without the 1/(12x^2) term fails containment; NC2 a corrupted record (one slip index k shifted by +1)
       yields an EMPTY enclosure for at least one orbit (the exclusion logic detects the inconsistency).
[NUM] orbits: 12 starts in U, N_STEPS primitive steps; slips by the F2(b) predicate; L estimated at the end of the run (tail scale sqrt(Q_end)).
usage: python -I recog_a1c_unknown_a_interval_cert.py [OUT_JSON] [N_STEPS]
"""
import json, math, sys, os, hashlib, importlib.util
import numpy as np
import mpmath as mp
from mpmath import iv
HERE = os.path.dirname(os.path.abspath(__file__))
P1B = os.path.join(HERE, "recog_a1c_tail_averaging_cert.py")
spec = importlib.util.spec_from_file_location("p1b", P1B); p1b = importlib.util.module_from_spec(spec); spec.loader.exec_module(p1b)   # runs its G1-G4, G6 at import
I, up, lo, f, tau, envelope_new = p1b.I, p1b.up, p1b.lo, p1b.f, p1b.tau, p1b.envelope_new
assert all(p1b.res["gates"].values()), "part-1b gates must pass"
PI3 = iv.pi/3
def fdn(x):
    """float rounded DOWN (never above x); x an mp.mpf"""
    v = float(x)
    return math.nextafter(v, -math.inf) if mp.mpf(v) > x else v
def fup(x):
    """float rounded UP (never below x)"""
    v = float(x)
    return math.nextafter(v, math.inf) if mp.mpf(v) < x else v
res = {"gates": {}, "imports": {"recog_a1c_tail_averaging_cert.py_sha256": hashlib.sha256(open(P1B, "rb").read()).hexdigest()}}
# ---------------- Lemma 7: interval digamma ----------------
def psi_iv(x, full=True):
    x = iv.mpf(x)
    base = iv.log(x) - 1/(2*x) - (1/(12*x**2) if full else 0)
    return iv.mpf([lo(base), up(base + 1/(120*x**4)) if full else up(base)])
def c_k(a, k, M): return tau*psi_iv(a + M) - (k - 1)*PI3
def E_k(a, M): return envelope_new(a, M)["E"]
# G1
g1 = True
for t in np.linspace(625, 5e6, 2000):
    with mp.workdps(70): v = mp.digamma(mp.mpf(t))        # reference value well beyond the 40-digit interval arithmetic
    b = psi_iv(I(t))
    g1 &= lo(b) <= v <= up(b)
g1 &= all(mp.polygamma(1, mp.mpf(x)) > mp.polygamma(1, mp.mpf(x) + 1) for x in (625, 1e3, 1e4, 1e6))     # trigamma decreasing (sanity; analytic)
res["gates"]["G1_digamma_bracket"] = bool(g1)
# ---------------- Lemma 8 ----------------
def h_iv(a, M1, M2): return tau*(psi_iv(a + M2) - psi_iv(a + M1))
def lemma8_interval(k1, M1, k2, M2, ceiling=mp.mpf("0.62"), tol=mp.mpf("1e-6")):
    D = k2 - k1; t_hi = up(D*PI3) + ceiling; t_lo = lo(D*PI3) - ceiling
    assert t_lo > 0
    # a^-: smallest a >= 625 with h(a) <= t_hi (h decreasing). If sup h(625) <= t_hi then 625.
    if up(h_iv(I(625), M1, M2)) <= t_hi: a_minus = mp.mpf(625)
    else:
        L_, R_ = mp.mpf(625), mp.mpf(625)
        while lo(h_iv(I(R_), M1, M2)) > t_hi: R_ *= 2
        while R_ - L_ > tol:                       # invariant: h(L_) > t_hi possible (excluded), h(R_) <= t_hi possibly admissible
            m_ = (L_ + R_)/2
            if lo(h_iv(I(m_), M1, M2)) > t_hi: L_ = m_
            else: R_ = m_
        a_minus = L_                               # outer: a^- >= L_
    # a^+: largest a with h(a) >= t_lo
    L_, R_ = mp.mpf(625), mp.mpf(625)
    while up(h_iv(I(R_), M1, M2)) >= t_lo: R_ *= 2
    while R_ - L_ > tol:
        m_ = (L_ + R_)/2
        if up(h_iv(I(m_), M1, M2)) < t_lo: R_ = m_
        else: L_ = m_
    a_plus = R_                                    # outer: a^+ <= R_
    return fdn(a_minus), fup(a_plus)                 # outward float rounding of the interval ends
# ---------------- Prop. 4: box enclosure ----------------
def classify(a_box, slips):
    """EXCLUDED: some pair has inf(c_j - E_j) > sup(c_k + E_k) on the box (no a in the box is admissible).
       SURE: max_j sup(c_j - E_j) <= min_k inf(c_k + E_k) on the box (every a in the box is admissible). Otherwise UNDECIDED."""
    vals = [(c_k(a_box, k, M), E_k(a_box, M)) for k, M in slips]
    lo_lo = max(lo(c - E) for c, E in vals); hi_hi = min(up(c + E) for c, E in vals)
    lo_hi = max(up(c - E) for c, E in vals); hi_lo = min(lo(c + E) for c, E in vals)
    status = "EXCLUDED" if lo_lo > hi_hi else ("SURE" if lo_hi <= hi_lo else "UNDECIDED")
    return status, (lo_lo, hi_hi)
def enclosure(slips, a_lo, a_hi, w_min=0.25):
    """returns (outer components, inner components, n_eval, undecided_length): outer = SURE + small UNDECIDED boxes (contains A_K);
       inner = SURE boxes only (contained in A_K). All float ends rounded outward for the outer set and inward for the inner set."""
    kept = []; sure = []; n_eval = 0; undecided_len = mp.mpf(0)
    stack = [(mp.mpf(a_lo), mp.mpf(a_hi))]
    while stack:
        x1, x2 = stack.pop(); n_eval += 1
        status, (Llo, Lhi) = classify(iv.mpf([x1, x2]), slips)
        if status == "EXCLUDED": continue
        if status == "UNDECIDED" and x2 - x1 > w_min:
            m_ = (x1 + x2)/2; stack.append((x1, m_)); stack.append((m_, x2))
        else:
            kept.append((fdn(x1), fup(x2), fdn(Llo), fup(Lhi)))
            if status == "SURE": sure.append((fup(x1), fdn(x2)))
            else: undecided_len += x2 - x1
    def merge(boxes, with_L):
        boxes.sort(); comps = []
        for b in boxes:
            if comps and abs(comps[-1][1] - b[0]) < 1e-9:
                comps[-1] = (comps[-1][0], b[1], min(comps[-1][2], b[2]), max(comps[-1][3], b[3])) if with_L else (comps[-1][0], b[1])
            else: comps.append(b)
        return comps
    return merge(kept, True), merge(sure, False), n_eval, float(undecided_len)
# ---------------- orbits ----------------
TAU = float(up(tau)); OMEGA = complex(-0.5, math.sqrt(3)/2)
def run_orbits(N):
    Q0s = [1/625]*4 + [1/1000]*4 + [1/2500]*4; ths = [0.3, 1.7, 3.9, 5.1]*3; n = len(Q0s)
    rho = np.array([math.sqrt(Q0s[i])*math.cos(ths[i]) for i in range(n)]); eta = np.array([math.sqrt(Q0s[i])*math.sin(ths[i]) for i in range(n)])/OMEGA.imag
    rho = rho - OMEGA.real*eta; W = rho + OMEGA*eta; phi = np.angle(W).copy()
    anchors = [[] for _ in range(n)]; Theta_end = None; Q_end = None
    for step in range(1, N + 1):
        rho_n = rho - np.sin(eta); eta_n = eta + np.exp(rho) - 1 - np.sin(eta); Wn = rho_n + OMEGA*eta_n
        phi += np.angle(Wn/W)
        bev = (eta < 0) & (eta_n >= 0) & (rho > 0) & (rho_n > 0)
        for i in np.nonzero(bev)[0]: anchors[i].append((step, phi[i]))
        rho, eta, W = rho_n, eta_n, Wn
    Mend = N//6; Theta_end = phi - 2*math.pi*Mend; Q_end = np.abs(W)**2
    out = []
    for i in range(n):
        a = 1/Q0s[i]; an = anchors[i]; n0, phi0 = an[0]; ell0 = math.floor(phi0/(2*math.pi))
        Psi = Theta_end[i] - TAU*math.log(Q_end[i]); L = math.pi/3*n0 - 2*math.pi*ell0 + Psi
        slips = []; k = 0; bad = 0
        for j in range(1, len(an)):
            gap = an[j][0] - an[j-1][0]
            if gap == 7:
                k += 1; Mk = an[j-1][0]//6
                if Mk >= 1: slips.append((k, int(Mk)))
            elif gap != 6: bad += 1
        out.append({"Q0": Q0s[i], "a": a, "theta0": ths[i], "slips": slips, "L_est": L, "L_tol": float(TAU*math.sqrt(Q_end[i])), "bad_gaps": bad})
    return out
if __name__ == "__main__":
    outp = sys.argv[1] if len(sys.argv) > 1 else "a1c_unknown_a_interval_cert.json"
    N = int(sys.argv[2]) if len(sys.argv) > 2 else 1_800_000
    orbits = run_orbits(N)
    g2 = g3 = g4 = True
    for o in orbits:
        a = o["a"]; sl = o["slips"]
        if len(sl) < 2: o["note"] = "fewer than two slips"; continue
        (k1, M1), (k2, M2) = sl[0], sl[1]
        am, ap = lemma8_interval(k1, M1, k2, M2)
        o["lemma8"] = {"pair": [sl[0], sl[1]], "interval": [am, ap], "width": ap - am, "contains_a": am <= a <= ap}
        g2 &= am <= a <= ap
        prog = []
        prev_w = None
        for K in range(2, len(sl) + 1):
            comps, inner, n_eval, und = enclosure(sl[:K], am, ap)
            hull = [comps[0][0], comps[-1][1]] if comps else None
            inner_hull = [inner[0][0], inner[-1][1]] if inner else None
            Lh = [min(c[2] for c in comps), max(c[3] for c in comps)] if comps else None
            w = (hull[1] - hull[0]) if hull else 0.0
            contains = any(c[0] <= a <= c[1] for c in comps)
            prog.append({"K": K, "components": comps, "a_hull": hull, "width": w, "L_hull": Lh, "inner_components": inner, "inner_hull": inner_hull,
                         "inner_width": (inner_hull[1] - inner_hull[0]) if inner_hull else 0.0, "undecided_length": und, "n_boxes_evaluated": n_eval, "contains_a": contains})
            if prev_w is not None: g4 &= w <= prev_w + 1e-9
            prev_w = w
            g4 &= hull is not None and hull[0] >= am - 1e-9 and hull[1] <= ap + 1e-9
        o["enclosures"] = prog
        last = prog[-1]
        g3 &= last["contains_a"] and last["L_hull"] is not None and (last["L_hull"][0] - o["L_tol"] <= o["L_est"] <= last["L_hull"][1] + o["L_tol"])
        o["final"] = {"K": last["K"], "a_hull": last["a_hull"], "width": last["width"], "relative_width": last["width"]/a, "L_hull": last["L_hull"], "L_est": o["L_est"],
                      "inner_hull": last["inner_hull"], "inner_width": last["inner_width"], "undecided_length": last["undecided_length"]}
    res["gates"]["G2_lemma8_contains_a"] = bool(g2); res["gates"]["G3_enclosure_contains_a_and_L"] = bool(g3); res["gates"]["G4_nesting"] = bool(g4)
    # ---- negative controls ----
    nc1 = False
    for t in np.linspace(625, 5e6, 200):
        b = psi_iv(I(t), full=False)
        with mp.workdps(70): v = mp.digamma(mp.mpf(t))
        if not (lo(b) <= v <= up(b)): nc1 = True; break
    nc2 = False
    for o in orbits[:4]:
        sl = list(o["slips"])
        if len(sl) < 3: continue
        bad = sl[:-1] + [(sl[-1][0] + 1, sl[-1][1])]                 # last slip index shifted by +1 (a phantom 7-gap)
        am, ap = o["lemma8"]["interval"]
        comps, _, _, _ = enclosure(bad, am, ap)
        if not comps: nc2 = True; break
    res["gates"]["NC1_bad_bracket_caught"] = bool(nc1); res["gates"]["NC2_corrupt_record_empty"] = bool(nc2)
    res["N_steps"] = N; res["orbits"] = orbits
    ok = all(res["gates"].values()); res["ALL_PASS"] = ok
    json.dump(res, open(outp, "w"), indent=1, default=lambda o: bool(o) if isinstance(o, np.bool_) else (float(o) if isinstance(o, (np.floating, np.integer)) else str(o)))
    for k, v in res["gates"].items(): print(k, "PASS" if v else "FAIL")
    for o in orbits:
        if "final" not in o: print("orbit a=%d th=%.1f: %s" % (o["a"], o["theta0"], o.get("note"))); continue
        l8 = o["lemma8"]; fi = o["final"]
        print("a=%4d th=%.1f slips=%s | Lemma8 pair %s: [%.1f, %.1f] (w=%.1f) | all %d slips: a in [%.1f, %.1f] (w=%.1f, %.1f%%) comps=%d | L in [%.4f, %.4f] (L_est %.4f +- %.4f)"
              % (o["a"], o["theta0"], [(k, M) for k, M in o["slips"]], l8["pair"], l8["interval"][0], l8["interval"][1], l8["width"], fi["K"], fi["a_hull"][0], fi["a_hull"][1], fi["width"], 100*fi["relative_width"], len(o["enclosures"][-1]["components"]), fi["L_hull"][0], fi["L_hull"][1], fi["L_est"], o["L_tol"]))
        print("      widths by K (outer / inner / undecided length):", [(p["K"], round(p["width"], 1), round(p["inner_width"], 1), round(p["undecided_length"], 2)) for p in o["enclosures"]])
    print("ALL PASS" if ok else "FAILURES"); sys.exit(0 if ok else 1)
