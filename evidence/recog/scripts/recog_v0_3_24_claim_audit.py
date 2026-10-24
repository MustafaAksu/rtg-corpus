#!/usr/bin/env python3
"""recog_v0_3_24_claim_audit.py -- the owner statements quoted by the v0.3.24 science groups are present in the
current owner source at its tag (quoted-statement presence, as the v0.3.23 audit; not a comparison with earlier editions).
usage: python -I evidence/recog/scripts/recog_v0_3_24_claim_audit.py [OUT_JSON]   (from the repository root)
"""
import json, subprocess, sys, hashlib
def show(tag, path):
    return subprocess.run(["git", "show", f"{tag}:{path}"], capture_output=True, check=True).stdout.decode("utf-8")
CHECKS = [
 ("dyad-v6.4.22", "dsn/RTG_DYADIC_OSCILLATOR_DSN.md", "DYAD-THM-LPHASE-ROWA-REMAINDER", [
    "[RID: DYAD-THM-LPHASE-ROWA-REMAINDER]", r"$|W(Ty)/(\lambda W(y))-1|\le\varepsilon$ with $\varepsilon\le0.04654$", r"\tfrac{403}{250}"]),
 ("dyad-v6.4.22", "dsn/RTG_DYADIC_OSCILLATOR_DSN.md", "DYAD-THM-NF-REM ingredients", [
    "`[RID: DYAD-THM-NF-REM]`", r"vector ceilings $|F_7|\le\tfrac{2079}{1000}|W|^7$, $|F_8|\le\tfrac{577}{500}|W|^8$, $|F_9|\le\tfrac{1763}{1000}|W|^9$",
    r"tail $|R^{\rm prim}_{\ge10,\rm vec}|\le332000|W|^{10}$ on $|W|\le\tfrac1{16}$"]),
 ("dyad-v6.4.22", "dsn/RTG_DYADIC_OSCILLATOR_DSN.md", "DYAD-THM-PRIM-CTR", ["DYAD-THM-PRIM-CTR", r"\tfrac1{625}", r"\tfrac{47}{1000}"]),
 ("dyad-v6.4.22", "dsn/RTG_DYADIC_OSCILLATOR_DSN.md", "DYAD-THM-C21", ["DYAD-THM-C21", r"-\tfrac12-i\tfrac{2\sqrt3}{3}"]),
 ("dyad-v6.4.22", "dsn/RTG_DYADIC_OSCILLATOR_DSN.md", "Dyadic §1 fixed-point scope (winding fixed points)", [r"$(\log(1+2\pi k),0)$ and $(\log(1+2\pi k),\pi)$"]),
 ("recog-v0.3.23", "dsn/RTG_RELATIONAL_RECOGNITION_DSN.md", "RECOG A1a inputs", [
    "[RID: RECOG-THM-A1A-PHASE-EXISTENCE-U]", "[RID: RECOG-THM-A1A-LIFT-ALIGNMENT]", "[RID: RECOG-THM-A1A-RECIPROCAL-AMPLITUDE]",
    "[RID: RECOG-THM-A1A-PHASE-EXISTENCE-ALT]", "[RID: RECOG-DEF-EVENT-TOKEN-SCHEMA]", "[RID: RECOG-DEF-POLE-COMPARATOR]"]),
 ("rrf-v0.8.4", "dsn/RTG_RRF_REPRESENTATION_REGISTRY.md", "RRF wrapped native ratio (for the declared form Omega)", ["RRF-DYAD-WRAPPED"]),
]
out = {"checks": []}; ok = True
for tag, path, label, strings in CHECKS:
    try:
        txt = show(tag, path)
    except subprocess.CalledProcessError:
        out["checks"].append({"tag": tag, "path": path, "label": label, "status": "source not available"}); ok = False; continue
    res = {s: txt.count(s) for s in strings}
    good = all(v >= 1 for v in res.values())
    out["checks"].append({"tag": tag, "path": path, "sha256": hashlib.sha256(txt.encode()).hexdigest(), "label": label, "present": res, "status": "present" if good else "MISSING"})
    ok &= good
out["ALL_PRESENT"] = ok
json.dump(out, open(sys.argv[1] if len(sys.argv) > 1 else "claim_audit.json", "w"), indent=1)
for c in out["checks"]: print(c["tag"], c["label"], c["status"], c.get("present", ""))
print("ALL PRESENT" if ok else "MISSING ITEMS"); sys.exit(0 if ok else 1)
