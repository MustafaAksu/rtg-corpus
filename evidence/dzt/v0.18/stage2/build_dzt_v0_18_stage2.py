#!/usr/bin/env python3
"""DZT v0.18, stage 2: compacted candidate from the stage-1 intermediate.

    python3 -I evidence/dzt/v0.18/stage2/build_dzt_v0_18_stage2.py [--emit-base PATH]

The base is the stage-1 intermediate of commit 3058bd29 (SHA-256 asserted). It is read with
`git show <commit>:<DSN>`; it is not kept as a second file. The script applies the declared
operations, writes the candidate to the DSN path and the movement map to
evidence/dzt/v0.18/stage2/movement_map.json. With --emit-base it also writes the base bytes to
PATH, which tools/check_compaction.py takes as its first argument; the checker re-derives the
candidate from that base and the map.

Stage 2 is layout only (Methodology v1.4 §13.6): the v1.4 header, five version labels removed
from live headings as history, Appendix A in compact form, and one footer line.
"""
import hashlib
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
BASE_COMMIT = "3058bd29528caf070bb69f2ac09f52cc6e48acbb"
BASE_SHA = "fbfbc00dcb0e7c3e4770ea39e33e80a42324a8cf81dbac8f40fc36f44850716d"
PRED_TAG = "dzt-v0.8"
PRED_SHA = "cad20982d294775d52592c304d743695c6ec2d8cf4975c78de203db3d6a92ff2"
DSN = "dsn/RTG_DYADIC_ARITHMETIC_RESONANCE_TRANSFORM_DSN.md"
BASE = "%s:%s" % (BASE_COMMIT, DSN)


def sha(b):
    return hashlib.sha256(b).hexdigest()


def die(m):
    sys.stderr.write("BUILD STOP: %s\n" % m)
    sys.exit(1)


base_b = subprocess.run(["git", "-C", ROOT, "show", BASE], capture_output=True, check=True).stdout
if sha(base_b) != BASE_SHA:
    die("base is not the stage-1 intermediate")
pred_b = subprocess.run(["git", "-C", ROOT, "show", "%s:%s" % (PRED_TAG, DSN)], capture_output=True, check=True).stdout
if sha(pred_b) != PRED_SHA:
    die("predecessor hash")
s = base_b.decode("utf-8")

HEADER = """# RTG_DYADIC_ARITHMETIC_RESONANCE_TRANSFORM_DSN_v0.18

**Title:** RTG Dyadic Arithmetic-Resonance Transform Study — Founding Charter and Diagnostic Ledger
**Date:** 18 November 2026
**Authors:** Mustafa (PI) · Claude · ChatGPT · Gemini · Grok
**Scope:** Arithmetic transforms (cyclotomic resultants and real-subfield norms) over Dyadic-owned OPEN 9 $p$-resonance observables, and the diagnostics they produce; no Dyadic result is re-owned, no AZ graph-zeta result transfers, and nothing is claimed about the Riemann Hypothesis or prime distribution.
**Document class:** Technical scientific ledger (Methodology v1.4 §0.5), standard layout. Short name: *Dyadic Zeta/Arithmetic Transform (DZT)*.
**Programme tier:** Tier 3 — Continuous Programme, downstream diagnostic of Dyadic. Maturity **Level A** (defined model; exploration begun). All results inherit the OPEN-P0 ceiling (SG-PROG-2 / SG-DZT-6).
**Document status:** DRAFT — stage-2 candidate of v0.18; not adopted. `dzt-v0.8` governs until the PI adopts and tags this edition.
**Supersedes:** `RTG_DYADIC_ARITHMETIC_RESONANCE_TRANSFORM_DSN` v0.8 (tag `dzt-v0.8`, SHA-256 `%s`)
**Companion documents:** Programme Overview v1.4 (`programme-v1.4`) · Dyadic Oscillator v6.4.24 (`dyad-v6.4.24`; source of truth for all OPEN 9 arithmetic) · Arithmetic Resonance and Zeta v0.10 (`az-v0.10`; discrete branch, quarantined, see SG-DZT-1) · Ontological Foundations v0.12 (`ofn-v0.12`)
**DSN Methodology:** v1.4 (`methodology-v1.4`)
**§1 length:** above the 500-word target of Methodology §1, because §1 states the three founding `[DEF]` records of the study (transform, channel state, ambient field) in full.

**Status summary:** This study defines a transform on Dyadic-owned OPEN 9 arithmetic. DZT-OPEN-0A is closed at finite-horizon scope (all three rows: $b=5$ survival, $b\\le4$ structural absence, cascade $(4,(0,3))$). The active frontier is DZT-OPEN-0B-R: prove or reject the anomaly rule for all $p$ from a resultant identity (§2). No Dyadic result is re-owned here; no AZ Thread-C graph-zeta result transfers; no OPEN-M amplitude or RH/prime claim is made.
""" % PRED_SHA

APPA = """## Appendix A — Version History

### v0.18 — 18 November 2026 — DRAFT (stage-2 candidate)
Corrections and synchronization edition after the reactivation triage (`records/dzt/DZT_REACTIVATION_TRIAGE.md`), with the Methodology v1.4 migration as a second build stage; no new scientific claim and no grade raised. The tabulated amplitude norms are stated as $\\lvert N_+(M_p)\\rvert$, and $M_p$ is defined as $Q_p/(i\\zeta_p^3)$ with its sign not asserted; the validation table and the anomaly set are scoped together; the Import Ledger is repinned to `dyad-v6.4.24` per its Appendix F; compound grade tokens are unpacked; §8 cites the recovered script files by path and hash with their evidence states; §1 keeps readouts and pointers. Companion pins: `programme-v1.4`, `dyad-v6.4.24`, `az-v0.10`, `ofn-v0.12`, `methodology-v1.4`. Corrections: Appendix B. Record: `records/dzt/DZT_v0_18_RELEASE_RECORD.md`.

### v0.9–v0.17 — not part of this lineage
DZT editions v0.9–v0.17 (June 2026) have no adoption record. Their files were received on 16 November 2026 and are listed with hashes in the v0.18 release record; their content enters v0.18 only through the corrections above.

### v0.1–v0.8 — June 2026
From the founding charter (v0.1) to the integration of the Dyadic all-$p$ phase law (v0.8). Full entries: Appendix A of `dzt-v0.8`.

"""

FOOTER = ("*END OF DOCUMENT — RTG_DYADIC_ARITHMETIC_RESONANCE_TRANSFORM_DSN_v0.18 — DRAFT, stage-2 candidate; adoption pending; "
          "`dzt-v0.8` governs until adoption and tag.*\n")

ARCH = ["stage1-intermediate"]


def hist(i, old, new, why):
    return {"id": "S2-L%d" % i, "op": "edit", "class": "history-removal", "archive": ARCH, "old": old, "new": new, "note": why}


ops = [
    {"id": "S2-H", "op": "replace-header", "class": "presentation", "archive": ARCH, "new": HEADER,
     "note": "v1.4 header: field order with Scope and Document status; one predecessor with its hash; the Methodology pin "
             "(triage row 9, stage 2); companion pins as set in stage 1; the §1 length exception declared in the header (Methodology §1); status summary "
             "of four sentences taken from the base summary and the base §1; the version-by-version narrative of the old "
             "summary is history (stage-1 intermediate and dzt-v0.8)"},
    hist(1, "**Two-layer channel state (v0.2).**", "**Two-layer channel state.**", "version label in a live heading"),
    hist(2, "**Ambient field (v0.2).**", "**Ambient field.**", "version label in a live heading"),
    hist(3, "**Cascade correction (v0.4):**", "**Cascade correction:**", "version label in a live heading"),
    hist(4, "- Cascade $(q,D)=(4,(0,3))$ (v0.4, finite horizon):", "- Cascade $(q,D)=(4,(0,3))$ (finite horizon):",
         "version label in a closed sub-item"),
    hist(5, "**Case V cascade channel (v0.4):**", "**Case V cascade channel:**", "version label in a live heading"),
    {"id": "S2-A", "op": "replace-section", "class": "history-appendix", "archive": ["stage1-intermediate", PRED_TAG],
     "start": "## Appendix A — Version History", "end": "## Appendix B — Retired and Rejected Claims", "new": APPA,
     "note": "one compact entry for v0.18, one line on the unadopted v0.9-v0.17, one pointer for v0.1-v0.8; the v0.1-v0.8 "
             "entries are byte-identical in Appendix A of dzt-v0.8"},
    {"id": "S2-F", "op": "replace-footer", "class": "presentation", "archive": ARCH, "new": FOOTER,
     "note": "single footer line (the descriptive second line of the base footer restates §3 and is dropped)"},
]

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
        i = c.index(op["start"])
        j = c.index(op["end"], i + len(op["start"]))
        c = c[:i] + op["new"] + c[j:]
    elif op["op"] == "replace-footer":
        lines = c.split("\n")
        i = next(n for n, l in enumerate(lines) if l.startswith("*END OF DOCUMENT"))
        c = "\n".join(lines[:i]) + "\n" + op["new"]

cand_b = c.encode("utf-8")
open(os.path.join(ROOT, DSN), "wb").write(cand_b)
mp = {
    "study": "DZT", "target": "v0.18", "stage": 2,
    "base": BASE, "base_sha256": BASE_SHA, "candidate_sha256": sha(cand_b),
    "archives": [{"name": "stage1-intermediate", "git": BASE, "sha256": BASE_SHA},
                 {"name": PRED_TAG, "git": "%s:%s" % (PRED_TAG, DSN), "sha256": PRED_SHA}],
    "archives_note": "the stage-1 intermediate, read from its commit, holds every removed byte; the predecessor tag holds the "
                     "v0.8 header, Appendix A and footer verbatim.",
    "profile": {"study": "DZT", "ref_words": [], "history_words": ["v0."],
                "checked_tag_prefixes": ["dzt-", "dyad-", "az-", "ofn-", "programme-", "methodology-"],
                "known_tags": ["dzt-v0.8", "dyad-v6.4.24", "az-v0.10", "ofn-v0.12", "programme-v1.4", "methodology-v1.4"],
                "summary_from": ["header", "section1"]},
    "operations": ops,
}
with open(os.path.join(HERE, "movement_map.json"), "w", encoding="utf-8", newline="\n") as f:
    json.dump(mp, f, ensure_ascii=False, indent=1)
    f.write("\n")
if "--emit-base" in sys.argv:
    out = sys.argv[sys.argv.index("--emit-base") + 1]
    open(out, "wb").write(base_b)
print("base      %s  (git show %s)" % (BASE_SHA, BASE))
print("candidate %s  %d bytes  (%d operations)" % (sha(cand_b), len(cand_b), len(ops)))
