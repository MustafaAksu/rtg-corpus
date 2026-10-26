#!/usr/bin/env python3
"""A1c -- joint unknown-a / start-offset transfer: an outer enclosure of the admissible (a, L, b, Theta_0) region from the record alone.

Inputs: the record (n_0; slips (k, M_k, r_k)) and x_0 in U (a >= 625). NOTHING else: the true a is never given to the algorithm (it is used
only afterwards, to test containment). Per a-box A = [a1, a2] all of a, L, b (= a - omega), Theta_0 and omega = a - b are interval variables:
  (C1) schedule (combined-tail centres c''' and envelopes E''' evaluated on the interval A):   L in I_K(A) = [max_k inf(c'''_k - E'''_k), min_k sup(c'''_k + E'''_k)]
  (C2) Lemma 16 sector for Theta_0 (n_0, A);   (C3) Prop. 18 arc  Theta_0 = L - pi n_0/3 - tau log b - M(z_0)  (L in I, b in its range);
  (C4) Lemma 17  omega in [-max_T Phi sqrt(A) - beta(A), -min_T Phi sqrt(A) + beta(A)];   (C5) b = A - omega;
  (C6) centred schedule: c4_k = c'''_k(A) - tau mid(omega S_{M_k}), E4_k = E'''_k(A) - tau A0(A, M_k) + tau half(omega S_{M_k}) -> new I_K.
Contractor per box: start omega = [-Delta_A, Delta_A] (Delta_A = (16/15) c_Q sqrt(a2)); I from (C1); then 3 rounds of (C2)-(C6), each step
intersecting with the previous enclosure (monotone). A box is EXCLUDED when any window/arc becomes empty; otherwise it is bisected down to
w_min and kept (UNDECIDED). The union of kept boxes is an OUTER enclosure of the admissible a-set; the hulls of their final I, omega and Theta_0
arcs enclose the admissible L, start offset and start angle. Invariant: the true (a, L, b, Theta_0, omega) satisfies every enclosure at every
step (all maps are enclosure-valid), hence the true a is never excluded.
Start region: the Lemma-8 interval of part 2 (first two slips, |h - D pi/3| <= 0.62), record-only.
Gates: G1 [NUM] 12 records: true a in the outer enclosure, reference L in the L-hull (tolerance), true theta_W0 in the Theta_0-hull (+ D0+);
    G2 the a-hull narrower than the combined-tail cell's (PR #64) on every record; G3 omega-hull width < 2 Delta_a; NC1 a corrupted record
    (last slip index + 1) gives an empty enclosure; NC2 the sector with n_0 + 1 excludes the true a or empties for some record.
usage: python -I recog_a1c_joint_transfer_cert.py [OUT_JSON] [N_STEPS]
"""
import json, math, sys, os, hashlib, importlib.util
import numpy as np
import mpmath as mp
from mpmath import iv
HERE = os.path.dirname(os.path.abspath(__file__))
def load(name):
    pth = os.path.join(HERE, name); spec = importlib.util.spec_from_file_location(name[:-3], pth); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m, hashlib.sha256(open(pth, "rb").read()).hexdigest()
pso, hso = load("recog_a1c_start_offset_cert.py")        # loads combined-tail, in-block, part 2, part 1b
pct, pib, p2, p1b = pso.pct, pso.pib, pso.p2, pso.p1b
I, up, lo, tau, f = p1b.I, p1b.up, p1b.lo, p1b.tau, pib.f
fup, fdn, asin_iv = p2.fup, p2.fdn, pib.asin_iv
res = {"gates": {}, "imports": {"recog_a1c_start_offset_cert.py": hso, **pso.res["imports"]}}
s3 = iv.sqrt(I(3)); PI = iv.pi; TWOPI = 2*mp.pi
cQ, cQp = p1b.cQ, p1b.cQp
C1 = I("0.261"); C_ISO = -4*s3/27; ABS_G = I("0.0076520"); C2_R9 = I(517); SUP_D = I(pct.SUP_D)
Phi_iv, LIP_PHI, SUP_PHI, circ_intersect, Q_UT, N0_MAX = pso.Phi_iv, pso.LIP_PHI, pso.SUP_PHI, pso.circ_intersect, pso.Q_UT, pso.N0_MAX
def Phi_range(t_lo, t_hi, n=400):
    t_lo = mp.mpf(t_lo); t_hi = mp.mpf(t_hi); h = (t_hi - t_lo)/n
    vals = [Phi_iv(I(t_lo + j*h)) for j in range(n + 1)]
    return mp.mpf(min(lo(v) for v in vals)) - LIP_PHI*h/2, mp.mpf(max(up(v) for v in vals)) + LIP_PHI*h/2
def beta_A(A):
    xp = cQ*(I(256)/225)**(I(3)/2)/iv.sqrt(A)
    return I(SUP_PHI)*iv.sqrt(A)*xp/(2*iv.sqrt(1 - xp)) + cQp*I(256)/225
def sector_A(n0, A):
    """Lemma 16 on an a-interval: arcs for theta_W0 and Theta_0 valid for every a in A"""
    assert 1 <= int(n0) <= N0_MAX
    Q = 1/A
    for _ in range(int(n0)): Q = iv.mpf([lo(Q), min(up(Q*(1 + pib.ebar(Q))**2), up(Q_UT))])
    alpha0 = asin_iv(pib.ebar(Q))
    lo_ = -n0*PI/3 - n0*alpha0; hi_ = -(n0 - 1)*PI/3 + (n0 + 1)*alpha0
    q0p = I(256)/(225*A); D0 = SUP_D*iv.sqrt(q0p) + C1*q0p
    return (lo(lo_ - D0), up(hi_ + D0)), up(D0)
def theta0_arc(n0, Lw, bw):
    Lint = iv.mpf([Lw[0], Lw[1]]); bint = iv.mpf([bw[0], bw[1]]); q0 = 1/bint
    Mmem = C_ISO*q0 + iv.mpf([-1, 1])*(ABS_G*q0 + C2_R9*q0**2)
    T = Lint - PI/3*n0 - tau*iv.log(bint) - Mmem
    return (lo(T), up(T))
def S_bracket_A(A, M, bw):
    cp = iv.mpf(max(up(A), mp.mpf(bw[1]))); cm = iv.mpf(min(lo(A), mp.mpf(bw[0]))); M = I(M)
    return iv.mpf([lo(1/(cp + M)), up(1/(cm + M)**2 + 1/(cm + M))])
def window(A, slips, extra, envs):
    los = []; his = []
    for (k, M, r) in slips:
        c = p2.c_k(A, k, M) + pct.centre_shift(A, M, r) + extra[M]; E = envs[M]
        los.append(lo(c - E)); his.append(up(c + E))
    L1, L2 = max(los), min(his)
    return (L1, L2) if L1 <= L2 else None
def contract(A, n0, slips, rounds=3):
    """returns None (EXCLUDED) or the final (I, omega, Theta0 arc, b-range)"""
    DeltaA = up(I(16)/15*cQ*iv.sqrt(A)); om = (-DeltaA, DeltaA); bw = (lo(A) - DeltaA, up(A) + DeltaA)
    base = {}
    for (k, M, r) in slips:
        c = pct.combined(A, M, r); e = p1b.envelope_new(A, M); base[M] = (c["E3"], tau*e["A0"])
    extra = {M: I(0) for M in base}; envs = {M: base[M][0] for M in base}
    Lw = window(A, slips, extra, envs)
    if Lw is None: return None
    secA, D0 = sector_A(n0, A); Tarc = None
    for it in range(rounds):
        T18 = theta0_arc(n0, Lw, bw)
        Tnew = secA if T18[1] - T18[0] >= TWOPI else circ_intersect(secA, T18)      # an arc of width >= 2 pi carries no information (wide boxes)
        if Tnew is None: return None
        Tarc = Tnew if Tarc is None else circ_intersect(Tarc, Tnew)
        if Tarc is None: return None
        pmin, pmax = Phi_range(Tarc[0], Tarc[1]); b_ = beta_A(A); sA = iv.sqrt(A)
        om_new = (lo(-I(pmax)*sA - b_), up(-I(pmin)*sA + b_))
        om = (max(om[0], om_new[0]), min(om[1], om_new[1]))
        if om[0] > om[1]: return None
        om_iv = iv.mpf([om[0], om[1]]); bw = (lo(A) - om[1], up(A) - om[0])
        for M in base:
            prod = om_iv*S_bracket_A(A, M, bw)
            mid = (lo(prod) + up(prod))/2; half = (up(prod) - lo(prod))/2
            E3, tA0 = base[M]
            extra[M] = -tau*I(mid); envs[M] = iv.mpf([0, up(E3 - tA0 + tau*half)])
        Lw_new = window(A, slips, extra, envs)
        if Lw_new is None: return None
        Lw = (max(Lw[0], Lw_new[0]), min(Lw[1], Lw_new[1]))
        if Lw[0] > Lw[1]: return None
    return {"L": Lw, "omega": om, "Theta0": Tarc, "b": bw, "D0": D0}
def enclosure(n0, slips, a_lo, a_hi, w_min=0.25):
    kept = []; n_eval = 0; stack = [(mp.mpf(a_lo), mp.mpf(a_hi))]
    while stack:
        x1, x2 = stack.pop(); n_eval += 1
        out = contract(iv.mpf([x1, x2]), n0, slips)
        if out is None: continue
        if x2 - x1 > w_min: m_ = (x1 + x2)/2; stack.append((x1, m_)); stack.append((m_, x2))
        else: kept.append((x1, x2, out))
    kept.sort(key=lambda t: t[0])
    return kept, n_eval
def hulls(kept):
    if not kept: return None
    a_h = (fdn(kept[0][0]), fup(kept[-1][1]))
    L_h = (fdn(min(t[2]["L"][0] for t in kept)), fup(max(t[2]["L"][1] for t in kept)))
    om_h = (fdn(min(t[2]["omega"][0] for t in kept)), fup(max(t[2]["omega"][1] for t in kept)))
    th_h = (fdn(min(t[2]["Theta0"][0] for t in kept)), fup(max(t[2]["Theta0"][1] for t in kept)))
    D0 = max(t[2]["D0"] for t in kept)
    # components of the a-union (exact adjacency only)
    comps = []
    for x1, x2, _ in kept:
        if comps and x1 <= comps[-1][1]: comps[-1] = (comps[-1][0], max(comps[-1][1], x2))
        else: comps.append((x1, x2))
    return {"a_hull": a_h, "a_width": fup(kept[-1][1] - kept[0][0]), "L_hull": L_h, "L_width": fup(L_h[1] - L_h[0]), "omega_hull": om_h, "omega_width": fup(om_h[1] - om_h[0]),
            "Theta0_hull": th_h, "Theta0_width": fup(th_h[1] - th_h[0]), "D0_plus": float(D0), "components": [(fdn(c[0]), fup(c[1])) for c in comps], "n_boxes_kept": len(kept)}
TAU = float(up(tau))
if __name__ == "__main__":
    outp = sys.argv[1] if len(sys.argv) > 1 else "a1c_joint_transfer_cert.json"
    N = int(sys.argv[2]) if len(sys.argv) > 2 else 1_800_000
    Q0s = [1/625]*4 + [1/1000]*4 + [1/2500]*4; ths = [0.3, 1.7, 3.9, 5.1]*3
    anc, hist_phi, Qh, Psi = pib.simulate(Q0s, ths, N); Nb = N//6
    old = {}
    try:
        rct = json.load(open(os.path.join(HERE, "..", "a1c_comb", "a1c_combined_tail_cert.json")))
        for p in rct["G5"]: old[(p["a"], p["theta0"])] = p["width"]
    except Exception: pass
    g1 = g2 = g3 = True; nc1 = False; nc2 = False; records = []
    for i in range(12):
        a_true = 1/Q0s[i]; an = anc[i]; n0 = int(an[0]); theta_W0 = (ths[i] + math.pi) % (2*math.pi) - math.pi
        slips = []; k = 0
        for j in range(1, len(an)):
            if an[j] - an[j - 1] == 7:
                k += 1; nA = an[j - 1]; M = nA//6; r = nA % 6
                if M >= 1: slips.append((k, M, r))
        (k1, M1, _), (k2, M2, _) = slips[0], slips[1]
        am, ap = p2.lemma8_interval(k1, M1, k2, M2)                               # record-only start region
        kept, n_eval = enclosure(n0, slips, am, ap)
        H = hulls(kept)
        # reference L (simulation; identity-corrected end estimate, as in the previous cells) -- used ONLY for the containment test
        ell0 = math.floor(hist_phi[i, n0]/(2*math.pi)); thN = hist_phi[i, 6*Nb] % (2*math.pi)
        dN = -math.sqrt(3)/12*math.cos(thN) + 0.25*math.sin(thN) - math.sqrt(3)/24*math.cos(3*thN) - math.sin(3*thN)/24
        L_ref = math.pi/3*n0 - 2*math.pi*ell0 + (hist_phi[i, 6*Nb] - 2*math.pi*Nb) + TAU*float(mp.digamma(a_true + Nb)) - dN/math.sqrt(a_true + Nb)
        Delta_a = f(p1b.envelope_new(a_true, 1)["Delta_a"]); Ltol = TAU*Delta_a/(a_true + Nb) + 3/(a_true + Nb)
        ok_a = H is not None and any(c[0] <= a_true <= c[1] for c in H["components"])
        ok_L = H is not None and H["L_hull"][0] - Ltol <= L_ref <= H["L_hull"][1] + Ltol
        ok_T = H is not None and circ_intersect((mp.mpf(H["Theta0_hull"][0]) - H["D0_plus"], mp.mpf(H["Theta0_hull"][1]) + H["D0_plus"]), (theta_W0, theta_W0)) is not None
        g1 &= ok_a and ok_L and ok_T
        ow = old.get((a_true, ths[i]))
        g2 &= H is not None and (ow is None or H["a_width"] < ow)
        g3 &= H is not None and H["omega_width"] < 2*Delta_a
        # NC1: corrupted record (last slip index + 1)
        bad = slips[:-1] + [(slips[-1][0] + 1, slips[-1][1], slips[-1][2])]
        kb, _ = enclosure(n0, bad, am, ap)
        if not kb: nc1 = True
        # NC2: wrong first anchor (n0 + 1, if within range)
        if n0 + 1 <= N0_MAX:
            kw, _ = enclosure(n0 + 1, slips, am, ap)
            Hw = hulls(kw)
            if Hw is None or not any(c[0] <= a_true <= c[1] for c in Hw["components"]): nc2 = True
        records.append({"a_true": a_true, "theta0": ths[i], "n0": n0, "slips": slips, "lemma8": [am, ap], "n_boxes_evaluated": n_eval, "hulls": H, "a_width_combined_tail_cell": ow,
                        "two_Delta_a": 2*Delta_a, "contains_a": ok_a, "L_ref": L_ref, "L_tol": Ltol, "contains_L": ok_L, "theta_W0": theta_W0, "contains_theta": ok_T})
    res["gates"].update({"G1_containment_a_L_theta": bool(g1), "G2_narrower_than_combined_tail_cell": bool(g2), "G3_omega_narrower_than_2Delta_a": bool(g3), "NC1_corrupt_record_empty": bool(nc1), "NC2_wrong_n0_excludes": bool(nc2)})
    res["records"] = records; res["N_steps"] = N
    ok = all(res["gates"].values()); res["ALL_PASS"] = ok
    json.dump(res, open(outp, "w"), indent=1, default=lambda o: bool(o) if isinstance(o, np.bool_) else (float(o) if isinstance(o, (np.floating, np.integer)) else str(o)))
    for k, v in res["gates"].items(): print(k, "PASS" if v else "FAIL")
    for rr in records:
        H = rr["hulls"]
        print("a=%4d th=%.1f n0=%d K=%d: a-hull [%.2f, %.2f] (w=%.2f; #64 cell %.1f; comps=%d, boxes %d) | L-hull width %.2e | omega [%.2f, %.2f] (w=%.2f; 2Da=%.1f) | Theta0 width %.4f | contains a/L/theta: %s/%s/%s"
              % (rr["a_true"], rr["theta0"], rr["n0"], len(rr["slips"]), H["a_hull"][0], H["a_hull"][1], H["a_width"], rr["a_width_combined_tail_cell"] or 0, len(H["components"]), rr["n_boxes_evaluated"], H["L_width"], H["omega_hull"][0], H["omega_hull"][1], H["omega_width"], rr["two_Delta_a"], H["Theta0_width"], rr["contains_a"], rr["contains_L"], rr["contains_theta"]) if H else "a=%4d: EMPTY" % rr["a_true"])
    print("ALL PASS" if ok else "FAILURES"); sys.exit(0 if ok else 1)
