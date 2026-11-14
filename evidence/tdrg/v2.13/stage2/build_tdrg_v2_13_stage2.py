#!/usr/bin/env python3
"""TDR-G v2.13, stage 2: compacted candidate from the stage-1 intermediate.

    python3 -I evidence/tdrg/v2.13/stage2/build_tdrg_v2_13_stage2.py [--emit-base PATH]

The base is the stage-1 intermediate. It is not kept as a second file: it is read from the stage-1
commit with `git show <BASE_COMMIT>:dsn/RTG_DISCRETE_GENESIS_DSN.md` and its SHA-256 is asserted.
The script declares the operations, applies them with the semantics of tools/check_compaction.py
(apply_ops), and writes the candidate to dsn/RTG_DISCRETE_GENESIS_DSN.md and the movement map to
evidence/tdrg/v2.13/stage2/movement_map.json. With --emit-base it also writes the base bytes to PATH,
which tools/check_compaction.py takes as its first argument; that checker re-derives the candidate
from base + map and checks each operation against its class rules.

Stage 2 is layout only: the header (its status summary is the stage-1 one, unchanged), version labels
without content (history-removal edits), Appendix A (including the §A.sim copy, which stage 1 placed
verbatim in §8), and the footer.
"""
import hashlib, json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
DSN = "dsn/RTG_DISCRETE_GENESIS_DSN.md"
BASE_COMMIT = "fd96f8a0b33a1236989b9e941b1c1c0e2381f2db"
BASE_SHA = "472e26e99a1da054447b57c4755adf50cacfc9dbe56ea7b8d5eaa2beb17856ff"
PRED_TAG = "tdrg-v2.12.15"
PRED_SHA = "1e35be54a37bb227cd75e34fc1cd6732ae95782bdc147a76e736f16760c92e64"
sha = lambda b: hashlib.sha256(b).hexdigest()


def die(m):
    sys.stderr.write("BUILD STOP: %s\n" % m)
    sys.exit(1)


def git(ref):
    return subprocess.run(["git", "-C", ROOT, "show", ref], capture_output=True, check=True).stdout


base_b = git("%s:%s" % (BASE_COMMIT, DSN))
if sha(base_b) != BASE_SHA:
    die("base is not the stage-1 intermediate")
if sha(git("%s:%s" % (PRED_TAG, DSN))) != PRED_SHA:
    die("predecessor hash")
s = base_b.decode("utf-8")
summary = [l for l in s.split("\n") if l.startswith("**Status summary:**")]
if len(summary) != 1:
    die("status summary")

HEADER = """# RTG_DISCRETE_GENESIS_DSN_v2.13

**Title:** RTG Discrete Relational Genesis — Canonical Study Ledger
**Date:** 13 November 2026
**Scope:** Fully discrete pre-metric relational universe on $\\mathbb{Z}_N$. Interaction from relational distinguishability; no continuous coordinates; no imported continuous coefficients.
**Document class:** Technical scientific ledger (Methodology v1.4 §0.5): standard §0–§9 with Appendices A and B and the scientific Appendix C (TDR-T requirements).
**Document status:** DRAFT — stage-2 candidate of v2.13; not adopted. `tdrg-v2.12.15` governs until the PI adopts and tags this edition.
**Supersedes:** `RTG_DISCRETE_GENESIS_DSN` v2.12.15 (tag `tdrg-v2.12.15`, SHA-256 `%s`)
**Companion documents:** Programme Overview v1.4 (`programme-v1.4`) · Ontological Foundations v0.12 (`ofn-v0.12`) · DSN Methodology v1.4 (`methodology-v1.4`)
**DSN Methodology:** DSN_METHODOLOGY_v1.4 (`methodology-v1.4`)
%s
**Programme tier:** Tier 4 — Discrete Programme (see Programme Overview §6)
""" % (PRED_SHA, summary[0])

FOOTER = "*END OF DOCUMENT — RTG_DISCRETE_GENESIS_DSN_v2.13*\n"

# history-removal edits: (label to remove, text that must follow it, text that must precede it).
# Each label is a version marker without claim content; the qualifications next to it stay.
LABELS = [
    ("new in v2.12; ", "does not block TDR-T)*", "frontier** *("),
    (" *(v2.12.15)*", "  \nQuestion: Identify a purely relational invariant", "Status: ACTIVE — PARTIAL"),
    (" *(v2.12.15)*", " — TDRG-ALG-TOKEN-CENSUS-LAW and TDRG-ALG-BIRTH-SPECTRUM-INJECTION", "**predictable-change law** `[ALG]`"),
    (" *(v2.12.15)*", " — TDRG-ALG-TOKEN-CENSUS-LAW (iii)", "**exactly invariant** `[ALG]`"),
    (" (revised v2.12.1)", ": derive the clean-star-count collapse", "Question"),
    (" (v2.12.14)", ":** the derivation target is the clean-star-count collapse", "**Current status"),
    (" (v2.12.1)", " $\\chi$ re-fit on v17 corpus", "**`[COR]`"),
    (", v2.12.4", "]` Field count is not resolvable", "`[SCOPE — decidability"),
    ("v2.12 note: ", "the \"failed null-return\" component", "*("),
    ("(v2.12) ", "LEM-REACH / LEM-NOANNIHIL / LEM-RETRIG / LEM-SPECCONS closed**", "- **"),
    ("(v2.12) ", "BIND3-CYCLE-N24K1 certified**", "- **"),
    (" (v2.12.15)", ":** the birth update is exact", "**Current status"),
    (" *(v2.12)*", " **Pairwise bound-state scope.**", "**[SG-11]**"),
    (" *(v2.12)*", " **Spectrum-conservation star firewall.**", "**[SG-12]**"),
    ("*(v2.12.15)* ", "Its $n$-node birth-free form", "under canonical swap and $P_3$ events. "),
    (" *(v2.12)*", " **Spectral-gate scope.**", "**[SG-13]**"),
    (" *(v2.12.14)*", " **Relabelling covariance.**", "**[SG-14]**"),
    ("v2.12.14, ", "cross-citation; AZ-owned)*", "star-supported structures. *("),
    ("**(v2.12)** ", "This convention is named **CONV-TICK**", ""),
    ("v2.12, ", "`[script-certified v18]`)**", "oriented 3-cycle along the path direction. **("),
    (" *(v2.12.14: previously used here but defined only in the engine, function `signed_centered`.)*", "", "orientation rule below."),
    ("(v2.12) ", "LEM-REACH — band-form reachability.**", "[RID: TDRG-ALG-LEM-REACH] **"),
    ("(v2.12) ", "LEM-NOANNIHIL — no free annihilation.**", "[RID: TDRG-ALG-LEM-NOANNIHIL] **"),
    ("(v2.12) ", "LEM-RETRIG — two-node retrigger / binding threshold.**", "[RID: TDRG-ALG-LEM-RETRIG] **"),
    ("v2.12; ", "period dividing 2) |", "| Retrigger bound state ("),
    ("**(v2.12.14)** ", "All motif-log results of §§6.6–6.10", "Policy results are branch-specific. "),
    (" *(v2.12.14, owner finding N1)*", " **`largest_center` breaks equal-degree ties", "pinned v17/v18 engines]`"),
    (" (v2.12.1)", "; $\\texttt{cs}/\\text{row}\\sim N^{-0.73}$", "composite ratio — not a power law"),
    (" *(v2.12.14)*", " The former companion check", "`[COR]`"),
    (" *(new in v2.12)*", "", "{#sec-6-12-threenode}"),
    ("**(v2.12.14)** ", "The enumerations and suites", "unless stated otherwise. "),
    (" (v2.12.14)", " th", "Under TDRG-DEF-ORIENT"),
    (" *(v2.12.14)*", "", "#### Orientation covariance at the antipodal-endpoint stratum"),
    (" *(new in v2.12.15)*", "", "{#sec-6-13-tokens}"),
    (" *(v2.12.14: four-way register — imports, consumers, pins, exports — with the states received / statement accepted / adopted use read from records, not from queue states.)*", "", "with the one scoped import below."),
    ("v2.12.15: repinned from `ofn-v0.10` to `ofn-v0.12`; the statement text is byte-identical at both tags, only OFN's scope tag changed. ",
     "Also cited by TDRG-ALG-BIRTH-SPECTRUM-NOT-CLOSED.)*", "this entry. *("),
    (" *(v2.12.15)*", ": the token laws of §6.13", "Contributions registered as TDR-G results, not imports"),
    (" (v2.12.14; rows for v2.12.15 added at the end)", ". RID names carry", "**Owner RID map**"),
    (" (v2.12.14)", " | §6.3 | `TDRG-ORIENT`", "path orientation rule"),
    ("v2.12.14 register; ", "hash check `records/tdrg/TDRG_UPLOAD_HASH_CHECK_20261027.md`", "*("),
]


def label_ops(text):
    ops = []
    for n, (lab, after, before) in enumerate(LABELS, 1):
        key = before + lab + after
        cnt = text.count(key)
        if cnt != 1:
            die("label %d %r: context occurs %d times" % (n, lab, cnt))
        ops.append({"id": "S2-L%02d" % n, "op": "edit", "class": "history-removal", "archive": ["stage1-intermediate"],
                    "old": key, "new": before + after,
                    "note": "version label without claim content; the text around it stays"})
        text = text.replace(key, before + after)
    return ops, text


ops = [{"id": "S2-H", "op": "replace-header", "class": "presentation", "archive": ["stage1-intermediate"], "new": HEADER,
        "note": "v1.4 header: field order with Document class and Document status; Supersedes names the immediate "
                "predecessor and its hash only; companions current; the status summary is the stage-1 sentence set, unchanged"}]
lops, _ = label_ops(s)
ops += lops
ops.append({"id": "S2-A", "op": "replace-section", "class": "history-appendix", "archive": ["stage1-intermediate", PRED_TAG],
            "start": "## Appendix A — Version History {#appendix-a}", "end": "## Appendix B — Retired and Rejected Claims {#appendix-b}",
            "new": open(os.path.join(HERE, "blocks", "appendix_a.md"), encoding="utf-8").read(),
            "note": "one compact entry for v2.13, v2.12.15, v2.12.14; one line for each earlier edition, full text at the tag; "
                    "§A.sim removed (stage 1 placed its table verbatim in §8; its closing [RESULT] stays at the tag)"})
ops.append({"id": "S2-F", "op": "replace-footer", "class": "presentation", "archive": ["stage1-intermediate"], "new": FOOTER,
            "note": "single footer line; the predecessor lineage is in the header (immediate predecessor) and the tags"})

# apply (the semantics of tools/check_compaction.py apply_ops)
t = s
for op in ops:
    if op["op"] == "edit":
        if t.count(op["old"]) != 1:
            die("%s: old text not unique" % op["id"])
        t = t.replace(op["old"], op["new"])
    elif op["op"] == "replace-header":
        r = t.index("\n## ")
        t = op["new"] + t[r:]
    elif op["op"] == "replace-section":
        i = t.find(op["start"]); j = t.find(op["end"], i + len(op["start"]))
        if i < 0 or j < 0 or t.count(op["start"]) != 1:
            die("%s: bounds" % op["id"])
        t = t[:i] + op["new"] + t[j:]
    elif op["op"] == "replace-footer":
        L = t.split("\n")
        i = [k for k, l in enumerate(L) if l.startswith("*END OF DOCUMENT")][0]
        t = "\n".join(L[:i]) + "\n" + op["new"]

cand = t.encode("utf-8")
mp = {"study": "TDRG", "target": "v2.13", "stage": 2,
      "base": "%s:%s" % (BASE_COMMIT, DSN), "base_sha256": BASE_SHA, "candidate_sha256": sha(cand),
      "archives": [{"name": "stage1-intermediate", "git": "%s:%s" % (BASE_COMMIT, DSN), "sha256": BASE_SHA},
                   {"name": PRED_TAG, "git": "%s:%s" % (PRED_TAG, DSN), "sha256": PRED_SHA}],
      "archives_note": "the stage-1 intermediate, read from its commit, holds every removed byte; the predecessor tag "
                       "holds the v2.12.15 header, Appendix A and footer verbatim.",
      "profile": {"study": "TDRG", "ref_words": [], "history_words": ["v2.12"],
                  "checked_tag_prefixes": ["tdrg-", "az-", "ofn-", "programme-", "methodology-", "numgen-"],
                  "known_tags": ["tdrg-v2.12.13", "tdrg-v2.12.14", "tdrg-v2.12.15", "az-v0.6", "az-v0.7", "az-v0.8",
                                 "ofn-v0.10", "ofn-v0.12", "programme-v1.4", "methodology-v1.4", "numgen-v1.21"],
                  "summary_from": ["header"]},
      "operations": ops}
open(os.path.join(ROOT, DSN), "wb").write(cand)
with open(os.path.join(HERE, "movement_map.json"), "w", encoding="utf-8") as f:
    json.dump(mp, f, indent=1, ensure_ascii=False)
    f.write("\n")
if "--emit-base" in sys.argv:
    open(sys.argv[sys.argv.index("--emit-base") + 1], "wb").write(base_b)
print("candidate", sha(cand), len(cand), "bytes;", len(ops), "operations")
