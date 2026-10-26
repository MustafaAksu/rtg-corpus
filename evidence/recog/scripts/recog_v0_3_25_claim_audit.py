#!/usr/bin/env python3
"""recog_v0_3_25_claim_audit.py -- presence of the owner statements the v0.3.25 stage-1 blocks rely on, in the current
owner sources at their adopted tags (Dyadic dyad-v6.4.22; RECOG recog-v0.3.24 for the rows the new blocks extend).

Presence at the cited RID in the current source only; not a comparison with earlier editions, not a proof check.
usage (repository root): python evidence/recog/scripts/recog_v0_3_25_claim_audit.py OUT_JSON
"""
import hashlib, json, subprocess, sys

def show(tag, path):
    b = subprocess.run(["git", "show", f"{tag}:{path}"], capture_output=True, check=True).stdout
    return b.decode("utf-8"), hashlib.sha256(b).hexdigest()

CHECKS = [
 # (source, tag, path, label, list of strings that must all be present)
 ("Dyadic", "dyad-v6.4.22", "dsn/RTG_DYADIC_OSCILLATOR_DSN.md", "DYAD-THM-NF-REM: rows, one-orbit contraction and the published certificate values used as [assuming:] ceilings (B1 L2)",
  ["[RID: DYAD-THM-NF-REM]", "85.07", "27.60", "q_0/(1+\\tfrac12q_0m)"]),
 ("Dyadic", "dyad-v6.4.22", "dsn/RTG_DYADIC_OSCILLATOR_DSN.md", "(D5) row-A bridge proof constants c_Q, c'_Q in the LPHASE row-A proof, certified by DYAD-ART-LPHASE-ROWA (A1c, [assuming:])",
  ["[RID: DYAD-THM-LPHASE-ROWA-REMAINDER]", "0.79246", "0.36915", "[RID: DYAD-ART-LPHASE-ROWA]"]),
 ("Dyadic", "dyad-v6.4.22", "dsn/RTG_DYADIC_OSCILLATOR_DSN.md", "branch (B) of LPHASE row A and the block law (A1c in-block, combined tail, start offset)",
  ["0.04654", "\\tfrac{403}{250}"]),
 ("Dyadic", "dyad-v6.4.22", "dsn/RTG_DYADIC_OSCILLATOR_DSN.md", "PRIM-CTR tube bound used to cap the first-anchor amplitude majorant (A1c start offset)",
  ["[RID: DYAD-THM-PRIM-CTR]", "2209"]),
 ("Dyadic", "dyad-v6.4.22", "dsn/RTG_DYADIC_OSCILLATOR_DSN.md", "NF-INV row bound and NF6 chart (A1c-Q fiber result)",
  ["[RID: DYAD-THM-NF-INV]", "\\tfrac{256}{225}", "[RID: DYAD-ALG-NF6]"]),
 ("RECOG", "recog-v0.3.24", "dsn/RTG_RELATIONAL_RECOGNITION_DSN.md", "R9 rows extended by B1 (adopted rows stay in force)",
  ["[RID: RECOG-THM-R9-MEMORY]", "$(C_2,q_{\\max})=(517,\\tfrac1{400})$", "$(163,\\tfrac1{1600})$", "K_\\Phi\\le258.49", "81.44"]),
 ("RECOG", "recog-v0.3.24", "dsn/RTG_RELATIONAL_RECOGNITION_DSN.md", "A1b slip schedule extended by A1c-E (statement unchanged)",
  ["[RID: RECOG-THM-A1B-SLIP-SCHEDULE-U]", "\\tau\\,\\psi(a+M_k)-(k-1)\\tfrac\\pi3=L+\\varepsilon_k", "5\\arcsin\\bigl(0.705\\sqrt Q+0.257\\,Q\\bigr)"]),
 ("RECOG", "recog-v0.3.24", "dsn/RTG_RELATIONAL_RECOGNITION_DSN.md", "A1c record readout and the two OPEN R6 sub-items answered/reworded by A1c-D and A1c-Q",
  ["[RID: RECOG-RESULT-A1C-RECORD-PHASE-READOUT]", "- A1c-Q1′:", "- A1c-decoder:"]),
]

def main():
    out = sys.argv[1] if len(sys.argv) > 1 else "claim_audit.json"
    res = {"sources": {}, "checks": []}; allok = True
    cache = {}
    for src, tag, path, label, needles in CHECKS:
        if (tag, path) not in cache: cache[(tag, path)] = show(tag, path)
        txt, h = cache[(tag, path)]; res["sources"][f"{tag}:{path}"] = h
        missing = [n for n in needles if n not in txt]
        ok = not missing; allok &= ok
        res["checks"].append({"source": src, "tag": tag, "label": label, "present": ok, "missing": missing})
        print(f"{'PRESENT' if ok else 'MISSING'}  {src} {tag}: {label}" + (f"  -- missing {missing}" if missing else ""))
    res["ALL_PRESENT"] = allok
    json.dump(res, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("ALL PRESENT" if allok else "SOME MISSING"); sys.exit(0 if allok else 1)

if __name__ == "__main__":
    main()
