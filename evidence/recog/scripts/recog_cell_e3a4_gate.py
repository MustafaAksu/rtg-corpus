#!/usr/bin/env python3
r"""
recog_cell_e3a4_gate.py — exit-coded gate for RECOG-THM-TWIN-STAGE2-NONUNIVERSAL (CELL-E3A-4).
Usage: python recog_cell_e3a4_gate.py   (in the directory holding the scripts, records and candidate)
PASS only if: the cert record binds the exact E3A-4 script, candidate and 3a/3b records present on disk (sha256); 3a/3b are the
preregistered hashes; the candidate x_c, w, N, L in the record equal the candidate file's; the pieces tile [-1, 1] with exact rational,
ordered, gap-free endpoints; every check in the record passed; the endpoint side tests are RECOMPUTED in Arb from the recorded endpoint
enclosures and the 3b rational separator (one endpoint u < h_-(s), the other u > h_+(s)); the D_s lower-bound list has N positive entries.
"""
import sys, json, hashlib
from fractions import Fraction as Fr
import flint
flint.ctx.prec = 512; arb = flint.arb
EXP_3A = "01ba69c3b5a36afc6ff5baf46eaf14de86876533546f7e6f93c4b187bb642cef"
EXP_3B = "545ecf628d6bdc40fe16530624935380868ae7252d6da23ad10f88421fc4531a"
def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()
errs = []
R = json.load(open("e3a4_cert.json")); C = json.load(open("e3a4_candidate.json")); B = json.load(open("e3a3b_p9_stable_local.json"))
if sha("e3a3a_p9_saddle.json") != EXP_3A or sha("e3a3b_p9_stable_local.json") != EXP_3B: errs.append("upstream 3a/3b hash mismatch")
if R["upstream"] != dict(e3a3a=EXP_3A, e3a3b=EXP_3B): errs.append("record upstream binding mismatch")
if R["script_sha256"] != sha("recog_cell_e3a4_crossing.py"): errs.append("E3A-4 script hash mismatch")
if R["candidate_sha256"] != sha("e3a4_candidate.json"): errs.append("candidate hash mismatch")
if (R["x_c"], R["w"], R["N"], R["L"]) != (C["x_c"], C["w"], C["N"], C["L"]): errs.append("candidate values differ from record")
P = sorted([(Fr(p["t"][0]), Fr(p["t"][1])) for p in R["pieces"]])
if not P or P[0][0] != -1 or P[-1][1] != 1 or any(P[i][1] != P[i + 1][0] for i in range(len(P) - 1)): errs.append("pieces do not tile [-1, 1]")
if not all(c["ok"] for c in R["checks"]) or not R["all_checks_pass"]: errs.append("a recorded check failed")
D = R["D_s_min_lower_by_step"]
if len(D) != R["N"] or min(D) <= 0: errs.append("D_s lower-bound list incomplete or nonpositive")
sep = B["separator"]; g = arb(int(sep["gamma"]))
def A(q): q = Fr(q); return arb(q.numerator)/q.denominator
sides = []
for t in ("-1", "1"):
    s, u = arb(R["endpoints"][t]["s"]), arb(R["endpoints"][t]["u"])
    hm = A(sep["U_LO"]) - (abs(s).upper() + A(sep["S_HI"]))/g; hp = A(sep["U_HI"]) + (abs(s).upper() + A(sep["S_HI"]))/g
    sides.append((bool(u < hm), bool(u > hp)))
if not ((sides[0][0] and sides[1][1]) or (sides[0][1] and sides[1][0])): errs.append("recomputed endpoint side test failed")
print(f"pieces {len(P)}; N {R['N']}; min certified D_s lower bound {min(D):.6f}; endpoint sides (neg,pos) {sides}")
for e in errs: print("  ERROR:", e)
print("E3A-4 GATE PASS" if not errs else "E3A-4 GATE FAIL"); sys.exit(0 if not errs else 1)
