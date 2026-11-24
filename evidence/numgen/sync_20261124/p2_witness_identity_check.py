#!/usr/bin/env python3
"""NUMGEN co-owner session diagnostic (24 Nov 2026) — [SESSION], read-only, no rule or verdict changed.

Loads the held audit upload/numgen-records/disc2_p2_antipodal_exposure_audit_v1.py (v1.19; its own log is replayed
byte-identically first) and asks two questions of its existing functions:
  Q1  Is the set of P2-exposed DISC-2 witnesses identical to the 40 Census-1 TDR-G records failing F6/R6-P2?
  Q2  Which witnesses change verdict/class under the audit's 'inert' policy, and how?
The audit's 'inert' policy treats S=0, E=N/2 exactly as its E=0 branch (inert tie). TDRG-DEF-ORIENT (tdrg-v2.13 §6.3)
makes S=0, 2E=0 mod N a balanced tie, treated as an inert bound state under bound_path_tie/bound_symmetric. The
identification of the two is a code reading, not a run of the pinned engine with the TDR-G reference orient_path.

usage: p2_witness_identity_check.py AUDIT_PY WITNESS_REPORT_JSON CENSUS1_UTDRG_RESULT_JSON
"""
import sys, json, io, contextlib
from collections import Counter
audit, wrep, cen = sys.argv[1:4]
g = {"__name__": "audit"}; argv = sys.argv; sys.argv = ["audit", wrep]
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    try: exec(compile(open(audit, encoding="utf-8").read(), audit, "exec"), g)
    except SystemExit: pass
sys.argv = argv
W, base, verdict, v18, ine = g["W"], g["base"], g["verdict"], g["v18"], g["ine"]
P = lambda s: tuple(int(z) for z in s.split("_")[1:])
exposed = {s for s in W if verdict(v18, P(s))[2]}
changed = {s for s in W if verdict(ine, P(s))[:2] != base[s]}
r = json.load(open(cen, encoding="utf-8"))
q = {x["record_id"].replace("U-TDRG-D2-", "") for x in r["records"] if x.get("F6", {}).get("result") == "FAIL"}
streams = Counter(x["F3"]["evidence"].split("streams B = ")[1].split(";")[0] for x in r["records"])
print(f"Q1 exposed DISC-2 witnesses: {len(exposed)}; Census-1 F6/R6-P2 failures: {len(q)}; identical sets: {exposed == q}")
print(f"   Census-1 TDR-G records by stream pair: {dict(streams)}")
print(f"Q2 inert-policy verdict/class changes: {len(changed)} (subset of exposed: {changed <= exposed})")
for k, v in sorted(Counter((base[s][0], str(base[s][1]), *map(str, verdict(ine, P(s))[:2])) for s in changed).items()):
    print(f"   {k[0]} {k[1]} -> {k[2]} {k[3]}: {v}")
