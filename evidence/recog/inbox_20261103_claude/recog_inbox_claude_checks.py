#!/usr/bin/env python3
"""recog_inbox_claude_checks.py -- RECOG co-owner (Claude) checks for the inbox round of 3 Nov 2026 (dispositions R1-R6).

NONCANONICAL session evidence. It changes no RECOG text, certificate, output or pipe state.

  c7cj     standalone interval recomputation of the two remainder constants that RECOG-ALG-A1C-COMBINED-TAIL derives
           RECOG-side (recog-v0.3.26 §6.13b: c_J^R = 0.5008, c_7^R = 100.23, "RECOG-derived from the explicit jet and C_7"):
             c_J^R(q) >= |Arg(J/z) + tau q| / q^2,  c_7^R(q) >= |Arg(hat F/J)| / q^3   (formulas of recog_a1c_combined_tail_cert.py
             L78-84, jet coefficients of DYAD-ALG-NF6, C_7 of DYAD-THM-NF-REM), at q* = 256/140625 (block base points of starts
             in U) and at q = 1/400 (Dyadic's row-A disk), monotonicity on a q-grid, and the margins against the two constants
             of the DYAD-THM-LPHASE-ROWA-REMAINDER proof sketch that part 1b uses (c_J = 0.50220, c_7 = 157.58; dyad-v6.4.23 L906).
  (The own patched rerun of the A1c chain is summarised in rerun_summary.json beside this script; it was produced by a
  plain shell loop, recorded in RUN_NOTE.md.)
usage (repository root): python -I evidence/recog/inbox_20261103_claude/recog_inbox_claude_checks.py c7cj OUT_JSON
"""
import json, sys
from mpmath import iv, mp
iv.dps = 40
I = iv.mpf
s3 = iv.sqrt(I(3)); tau = 2*s3/3
mu = (I(-1)/2, -2*s3/3); a32 = (I(-97)/432, 197*s3/324); a05 = (I(-49)/8640, -307*s3/25920)   # DYAD-ALG-NF6 (dyad-v6.4.23)
absv = lambda z: iv.sqrt(z[0]**2 + z[1]**2)
abs_mu, abs_a32, abs_a05 = absv(mu), absv(a32), absv(a05); A5 = abs_a32 + abs_a05; a32_im = a32[1]
def cJ(q):
    uJ = abs_mu*q + A5*q**2
    return abs(a32_im - tau/2) + abs_a05 + abs_mu*A5*q + A5**2*q**2/2 + uJ**3/(3*(1 - uJ))/q**2
def c7(q, C7=I(100)):
    uJ = abs_mu*q + A5*q**2; w = C7*q**3/(1 - uJ)
    return C7/(1 - uJ)/(1 - w)
up = lambda x: float(x.b)
def c7cj(out):
    qs = I(256)/140625; grid = [I(10)**(-k) for k in range(9, 2, -1)] + [qs, I(1)/400]
    gJ = [up(cJ(q)) for q in grid]; g7 = [up(c7(q)) for q in grid]
    res = {"q_star": "256/140625", "cJ_R(q*)_upper": up(cJ(qs)), "c7_R(q*)_upper": up(c7(qs)),
           "cJ_R(1/400)_upper": up(cJ(I(1)/400)), "c7_R(1/400)_upper": up(c7(I(1)/400)),
           "c7_R(q*)_upper_with_C7_85.1": up(c7(qs, I("85.1"))),
           "monotone_cJ_on_grid": all(gJ[i] <= gJ[i + 1] for i in range(len(gJ) - 1)),
           "monotone_c7_on_grid": all(g7[i] <= g7[i + 1] for i in range(len(g7) - 1)),
           "dyad_proof_sketch_cJ": 0.50220, "dyad_proof_sketch_c7": 157.58}
    res["cJ_R(q*) <= 0.50220"] = res["cJ_R(q*)_upper"] <= 0.50220
    res["c7_R(q*) <= 157.58"] = res["c7_R(q*)_upper"] <= 157.58
    res["ALL_PASS"] = all(res[k] for k in ("monotone_cJ_on_grid", "monotone_c7_on_grid", "cJ_R(q*) <= 0.50220", "c7_R(q*) <= 157.58"))
    json.dump(res, open(out, "w"), indent=1); print(json.dumps(res, indent=1)); sys.exit(0 if res["ALL_PASS"] else 1)
if __name__ == "__main__":
    if len(sys.argv) >= 3 and sys.argv[1] == "c7cj": c7cj(sys.argv[2])
    else: print(__doc__); sys.exit(2)
