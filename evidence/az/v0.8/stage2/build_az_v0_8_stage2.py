#!/usr/bin/env python3
"""AZ v0.8, stage 2: compacted candidate from the reviewed stage-1 intermediate.

    python3 -I evidence/az/v0.8/stage2/build_az_v0_8_stage2.py [--emit-base PATH]

The base is the stage-1 intermediate accepted in review 5874483729. It is not kept as a
second file: it is read from the reviewed commit with
`git show 873b277a8c62b9a8536207e68fe153257fdb9454:dsn/RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN.md`
and its SHA-256 is asserted. The script applies the declared operations, writes the candidate
to dsn/RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN.md and the movement map to
evidence/az/v0.8/stage2/movement_map.json. With --emit-base it also writes the base bytes to
PATH (a temporary file), which tools/check_compaction.py needs as its first argument; the
checker re-derives the candidate from that base and the map.

Stage 2 is layout only: header, Appendix A, footer, and three reference substitutions.
"""
import hashlib
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
BASE_COMMIT = "873b277a8c62b9a8536207e68fe153257fdb9454"
BASE_SHA = "19a1faf01e44a74d2bffc8dbf14fddae798f21e75f3c5e166f290d6f11fd0426"
PRED_TAG = "az-v0.7"
PRED_SHA = "2294d2a3287651802824a77ea22fb8f3896f6837cca1162fd8479ff02839fc94"
DSN = "dsn/RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN.md"
BASE = "%s:%s" % (BASE_COMMIT, DSN)


def sha(b):
    return hashlib.sha256(b).hexdigest()


def die(m):
    sys.stderr.write("BUILD STOP: %s\n" % m)
    sys.exit(1)


base_b = subprocess.run(["git", "-C", ROOT, "show", BASE], capture_output=True, check=True).stdout
if sha(base_b) != BASE_SHA:
    die("base is not the reviewed stage-1 intermediate")
pred_b = subprocess.run(["git", "-C", ROOT, "show", "%s:%s" % (PRED_TAG, DSN)], capture_output=True, check=True).stdout
if sha(pred_b) != PRED_SHA:
    die("predecessor hash")
s = base_b.decode("utf-8")

HEADER = """# RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN_v0.8

**Title:** RTG Arithmetic Resonance and Zeta Study — Infrastructure and Diagnostic Ledger  
**Date:** 12 November 2026  
**Authors:** Mustafa (PI) · Claude · ChatGPT · Gemini · Grok  
**Scope:** A reference-only index of the arithmetic-resonance results of the Dyadic DSN; the TDR-G $\\mathbb{Z}_N$ arithmetic structure as a bridge-candidate observable family; and the graph/transfer-zeta diagnostic infrastructure with the diagnostics it has produced. No cross-branch import is made and nothing is claimed about the Riemann Hypothesis.  
**Document class:** Infrastructure / diagnostic ledger (Methodology v1.4 §0.5) with a declared section map (§0.3); not a scientific result ledger  
**Programme tier:** Tier 5 — Arithmetic-diagnostic infrastructure; serves both continuous and discrete branches without belonging to either  
**Maturity:** Level A — retained. Defined scope, internal consistency established, exploration begun. Thread C engineering is certified; the one Phase-2 scientific result is a negative-clarifying diagnostic, not a Level-B-promoting bridge result.  
**Document status:** DRAFT — stage-2 candidate of v0.8; not adopted. `az-v0.7` governs until the PI adopts and tags this edition.  
**Supersedes:** `RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN` v0.7 (tag `az-v0.7`, SHA-256 `%s`)  
**Companion documents:** Programme Overview v1.4 (`programme-v1.4`) · Dyadic Oscillator v6.4.24 (`dyad-v6.4.24`) · Discrete Genesis v2.12.14 (`tdrg-v2.12.14`) · Genesis Geometry v2.10 (`gen-v2.10`) · OPEN-M v0.7.1 (`uvm-v0.7.1`)  
**DSN Methodology:** v1.4 (`methodology-v1.4`)  

**Status summary:** This document remains an infrastructure ledger, not an active scientific study, and Maturity remains **Level A**. Milestone AZ-2 is recorded as **attempted, negative-clarifying**: the most tempting angular observable was tested and **disqualified** as a bridge-candidate. **No Level B promotion. No OPEN-P1 / Dyadic bridge-candidate is promoted.**

---
""" % PRED_SHA

a0 = s.index("## Appendix A — Version History")
a1 = s.index("## Appendix B — Retired and Rejected Claims")
old_app = s[a0:a1]
k5 = old_app.index("### v0.5 — June 2026")
APPA = """## Appendix A — Version History

### v0.8 — November 2026
Methodology v1.4 migration with a declared section map (§0.3), the reduction asked for in Programme §6.7, and availability corrections. Each owner result is cited once, in §8; restated Dyadic and TDR-G text is removed from §1.2, §4.1, §4.2 and §6. PROP-AZ-CORE-EQUIV is `[THM]` on a written proof (§4.3.2), replacing the bare `[THM-ALG]`; a finite check is registered (`AZ-ART-CORE-EQUIV-CHECK`). The static-geometry reading of the `4|q` rule (`TDRG-AZ-STATIC-ZN-4Q`) is stated at the scope of its numerical evidence (SG-AZ-7, §4.3.5). §9 gives per-artifact availability after the partial recovery of 11 November 2026. Dyadic pin: `dyad-v6.4.24`. No new scientific result; Level A retained. Corrections: Appendix B. Record: `records/az/AZ_v0_8_RELEASE_RECORD.md`.

### v0.7 — November 2026
Corrections-only edition. Owner pins, identifiers and imported statements synchronized with the adopted owner editions (Dyadic v6.4.23, TDR-G v2.12.14, Genesis v2.10, Programme v1.4, OPEN-M v0.7.1); the withdrawn OPEN-M "legal ×2" reading removed; the Thread C evidence files recorded as not available in the repository. No grade of an AZ-owned result changed. Full entry: Appendix A of `az-v0.7`; record: `records/az/AZ_v0_7_RELEASE_RECORD.md`.

### v0.6 — June 2026
Ledger-state update. AZ-1 closed (AZ-1A, AZ-1B, AZ-1C `[ENG PASS]`); AZ-OPEN-EDGE resolved (directed, both orientations); PROP-AZ-CORE-EQUIV and the antipodal-band low-order obstruction registered; the first Phase-2 diagnostic (the Core(G_T) `4|q` rule) registered and reclassified as static $\\mathbb{Z}_N$ geometry; retraction block added (§4.3.4, Appendix B); SG-AZ-5 repurposed as a provenance guard; AZ-2 attempted, negative-clarifying; Level A retained. Full entry: Appendix A of `az-v0.7`.

""" + old_app[k5:]

FOOTER = "*END OF DOCUMENT — RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN_v0.8 — DRAFT, stage-2 candidate; adoption pending; `az-v0.7` governs until adoption and tag.*\n"

ARCH = ["stage1-intermediate"]
ops = [
    {"id": "S2-H", "op": "replace-header", "class": "presentation", "archive": ARCH, "new": HEADER,
     "note": "v1.4 header: field order with Scope and Document status; one predecessor with its hash; companions with dyad-v6.4.24; "
             "status summary of three sentences taken from the base summary; the v0.6 'Major update' list and the v0.6/v0.7 "
             "edition narrative are history (in the stage-1 intermediate and at az-v0.7)"},
    {"id": "S2-R1", "op": "edit", "class": "ref-subst", "archive": ARCH,
     "old": "is not yet established (Dyadic Appendix E).", "new": "is not yet established (Dyadic Appendix E, `dyad-v6.4.24`).",
     "note": "the owner appendix is named with its edition tag, so that the reference resolves"},
    {"id": "S2-R2", "op": "edit", "class": "ref-subst", "archive": ARCH,
     "old": "Owner evidence boundary (Dyadic Appendix D):", "new": "Owner evidence boundary (Dyadic Appendix D, `dyad-v6.4.24`):",
     "note": "as S2-R1"},
    {"id": "S2-R3", "op": "edit", "class": "ref-subst", "archive": ARCH,
     "old": "its statement is not recovered, Dyadic Appendix D).", "new": "its statement is not recovered, Dyadic Appendix D, `dyad-v6.4.24`).",
     "note": "as S2-R1"},
    {"id": "S2-A", "op": "replace-section", "class": "history-appendix", "archive": ["stage1-intermediate", PRED_TAG],
     "start": "## Appendix A — Version History", "end": "## Appendix B — Retired and Rejected Claims", "new": APPA,
     "note": "one compact entry per edition; new v0.8 entry; the v0.7 and v0.6 entries shortened, their full text in Appendix A of "
             "az-v0.7; the v0.5-v0.1 entries byte-identical"},
    {"id": "S2-F", "op": "replace-footer", "class": "presentation", "archive": ARCH, "new": FOOTER, "note": "single footer line"},
]

# apply (the checker re-derives the same result independently)
c = s
for op in ops:
    if op["op"] == "replace-header":
        c = op["new"] + c[c.index("\n## "):]
    elif op["op"] == "edit":
        if c.count(op["old"]) != 1:
            die("%s: old text occurs %d times" % (op["id"], c.count(op["old"])))
        c = c.replace(op["old"], op["new"])
    elif op["op"] == "replace-section":
        if c.count(op["start"]) != 1:
            die("%s: start not unique" % op["id"])
        i = c.index(op["start"]); j = c.index(op["end"], i + len(op["start"]))
        c = c[:i] + op["new"] + c[j:]
    elif op["op"] == "replace-footer":
        lines = c.split("\n")
        i = next(n for n, l in enumerate(lines) if l.startswith("*END OF DOCUMENT"))
        c = "\n".join(lines[:i]) + "\n" + op["new"]
cand_b = c.encode("utf-8")
open(os.path.join(ROOT, DSN), "wb").write(cand_b)

mp = {
    "study": "AZ", "target": "v0.8", "stage": 2,
    "base": BASE, "base_sha256": BASE_SHA, "candidate_sha256": sha(cand_b),
    "archives": [{"name": "stage1-intermediate", "git": BASE, "sha256": BASE_SHA},
                 {"name": PRED_TAG, "git": "%s:%s" % (PRED_TAG, DSN), "sha256": PRED_SHA}],
    "archives_note": "the stage-1 intermediate, read from the reviewed commit, holds every removed byte; the predecessor tag holds the "
                     "v0.7 header, Appendix A and footer verbatim.",
    "profile": {"study": "AZ", "ref_words": [], "history_words": [],
                "checked_tag_prefixes": ["az-", "tdrg-", "gen-", "uvm-", "programme-", "methodology-", "dzt-"],
                "known_tags": ["az-v0.6", "az-v0.7", "dyad-v6.4.23", "dyad-v6.4.24", "tdrg-v2.12.14", "gen-v2.10", "uvm-v0.7.1",
                               "programme-v1.4", "methodology-v1.4"],
                "summary_from": ["header"]},
    "operations": ops,
}
json.dump(mp, open(os.path.join(HERE, "movement_map.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
if "--emit-base" in sys.argv:
    out = sys.argv[sys.argv.index("--emit-base") + 1]
    open(out, "wb").write(base_b)
print("base      %s  (git show %s)" % (BASE_SHA, BASE))
print("candidate %s  %d bytes  (%d operations)" % (sha(cand_b), len(cand_b), len(ops)))
