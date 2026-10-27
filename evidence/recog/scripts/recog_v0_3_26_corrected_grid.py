#!/usr/bin/env python3
"""recog_v0_3_26_corrected_grid.py -- the A1c envelope grids with the corrected closed forms (CORR-1, CORR-2; Appendix B, v0.3.26).

CORR-1: part 1b's log-majorant Lg(p, b', M) is replaced by Lg_corr (drift-centering cell, G3b): the same sums without the
        M-independent slack b'^{-p}.  Affects A1-bar, Sbar', Rbar', E', E''' (through tau A1-bar) and E^(4).
CORR-2: the combined-tail reference term ref_d uses the M-dependent bracket q_M^{-1} in [b'+M-epsbar_M, a+Delta_a+M+epsbar_M]
        (part 1b Lemma 2) instead of the uniform slack kappa in q+_M.
Writes the corrected values of the displayed grid quantities (recog-v0.3.25 §6.13b) next to the v0.3.25 ones, and the
asymptotic check (scaled values at M up to 10^13).  No long orbit is rerun; the inequalities are unchanged (the corrected
majorants are below the adopted ones at every grid point: checked here).
usage (repository root): python evidence/recog/scripts/recog_v0_3_26_corrected_grid.py OUT_JSON
"""
import json, math, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import recog_a1c_drift_centering_cert as pdc           # imports the stack; defines Lg_corr
pct, p1b, pso = pdc.pct, pdc.p1b, pdc.pso
I, up, lo, f, tau, iv = p1b.I, p1b.up, p1b.lo, p1b.f, p1b.tau, pdc.iv
SQ3_8 = pct.SQ3_8

def ref_d_corr(a, M):
    """CORR-2: (sqrt3/8) max(sqrt(q+) - n^{-1/2}, n^{-1/2} - sqrt(q-)) with the M-dependent bracket of part 1b Lemma 2"""
    a = I(a); M = I(M); e = p1b.envelope_new(a, M); Delta_a = e["Delta_a"]; bp = a - Delta_a
    q0b = 1/bp; sigma2 = 2*q0b + q0b**2; e_const = p1b.gamma0*q0b + p1b.gamma1*sigma2
    epsM = e_const + 2*p1b.gamma0*iv.log(1 + M/(2*bp))
    qp = 1/(bp + M - epsM); qm = 1/(a + Delta_a + M + epsM); n = a + M
    return SQ3_8*I(max(up(iv.sqrt(qp) - n**(-I(1)/2)), up(n**(-I(1)/2) - iv.sqrt(qm))))
def corrected(a, M, r):
    """E''' with Lg_corr (through envelope_new inside combined) and ref_d_corr"""
    old = pct.combined(a, M, r); e_old = p1b.envelope_new(a, M)
    c3 = pdc.with_Lg_corr(pct.combined, a, M, r); e_c = pdc.with_Lg_corr(p1b.envelope_new, a, M)
    E3c = c3["E3"] - c3["ref_d"] + ref_d_corr(a, M)
    return {"E3_old": f(old["E3"]), "E3_corr": f(E3c), "tauA1_old": f(old["tauA1"]), "tauA1_corr": f(c3["tauA1"]), "ref_d_old": f(old["ref_d"]), "ref_d_corr": f(ref_d_corr(a, M)),
            "Eprime_old": f(e_old["E"]), "Eprime_corr": f(e_c["E"]), "Sbar_old": f(e_old["Sbar"]), "Sbar_corr": f(e_c["Sbar"]), "Rbar_old": f(e_old["Rbar"]), "Rbar_corr": f(e_c["Rbar"]),
            "ok_below": bool(up(E3c) <= up(old["E3"]) and up(e_c["E"]) <= up(e_old["E"]) and up(e_c["Sbar"]) <= up(e_old["Sbar"]) and up(e_c["Rbar"]) <= up(e_old["Rbar"]))}
def main():
    out = sys.argv[1] if len(sys.argv) > 1 else "corrected_grid.json"
    res = {"grid": {}, "asymptotic": {}, "all_below": True}
    for a in (625, 1000, 2500):
        res["grid"][str(a)] = {}
        for M in (1000, 10000, 100000, 1000000, 10000000):
            rows = {str(r): corrected(a, M, r) for r in range(6)}
            worst = max(rows.values(), key=lambda x: x["E3_corr"])
            res["grid"][str(a)][str(M)] = {"rows": rows, "E3_corr_worst_r": worst["E3_corr"], "E3_old_worst_r": max(x["E3_old"] for x in rows.values()),
                                           "E3_corr_scaled": worst["E3_corr"]*(a + M), "Eprime_corr": worst["Eprime_corr"], "Eprime_old": worst["Eprime_old"]}
            res["all_below"] &= all(x["ok_below"] for x in rows.values())
        res["asymptotic"][str(a)] = {}
        for M in (10**9, 10**11, 10**13):
            c = corrected(a, M, 5); n = a + M
            res["asymptotic"][str(a)][str(M)] = {"E3_corr_sqrt": c["E3_corr"]*math.sqrt(n), "E3_old_sqrt": c["E3_old"]*math.sqrt(n), "E3_corr_scaled_over_log": c["E3_corr"]*n/(1 + math.log(n)),
                                                 "Sbar_corr_sqrt": c["Sbar_corr"]*math.sqrt(n), "Rbar_corr_sqrt": c["Rbar_corr"]*math.sqrt(n), "Eprime_corr_sqrt": c["Eprime_corr"]*math.sqrt(n), "Sbar_old_sqrt": c["Sbar_old"]*math.sqrt(n)}
    json.dump(res, open(out, "w"), indent=1)
    for a in res["grid"]:
        print("a=%s: " % a + "  ".join("M=%s E'''=%.3e (old %.3e) scaled %.1f | E'=%.4f (old %.4f)" % (M, g["E3_corr_worst_r"], g["E3_old_worst_r"], g["E3_corr_scaled"], g["Eprime_corr"], g["Eprime_old"]) for M, g in res["grid"][a].items()))
        print("   asymptotic: " + "  ".join("M=%s E'''sqrt=%.2e (old %.2e) E'''n/(1+log)=%.2f Sbar'sqrt=%.4f Rbar'sqrt=%.4f E'sqrt=%.4f" % (M, g["E3_corr_sqrt"], g["E3_old_sqrt"], g["E3_corr_scaled_over_log"], g["Sbar_corr_sqrt"], g["Rbar_corr_sqrt"], g["Eprime_corr_sqrt"]) for M, g in res["asymptotic"][a].items()))
    print("corrected majorants below the adopted ones at every grid point:", res["all_below"])
if __name__ == "__main__":
    main()
