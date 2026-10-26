#!/usr/bin/env python3
"""Number Genesis v1.21, stage 2: Methodology v1.4 compaction (layout only) of the accepted stage-1 intermediate.

Base: stage-1 intermediate, round 2 (PR #74; co-owner review ACCEPTED 26 Oct 2026, "Stage 2 — GO"),
      sha256 ab25c162a727b0826adfb0b8fd5f3898969ed78260fc00e8bbcaa9e1e3b899d2, archived byte-exact as
      evidence/numgen/v1.21/stage1_intermediate.md.
Operations (movement map evidence/numgen/v1.21/movement_map.json, checked by tools/check_compaction.py):
  S2-H  replace-header: current-only header (one field per line; one predecessor with its hash; Methodology v1.4;
        status summary = sentences of the base summary; §1 profile exception declared). The base header's
        pointer-validation note, methodology notes and stacked status prefaces go to the release record.
  S2-T  replace-section (history-appendix) from "## Appendix A. Working Thesis" to the end of the file:
          - new "## Appendix A — Version History": one compact entry each for v1.21, v1.20.8, v1.20.7 and a pointer
            for v0.1–v1.20.6 to the tagged predecessor (its "## Changelog" and the three legacy notes);
          - "## Appendix B. Rejected / Guarded Formulations": body byte-identical;
          - "## Appendix C. Working Thesis": the former Appendix A body byte-identical (heading letter only);
          - one footer.
        The removed bytes (Working Thesis, Appendix B, Changelog, legacy notes) are in the archived intermediate.
No live section (§0–§9) is touched. No claim, RID, grade, OPEN status or scope changes.

usage: build_numgen_v1_21_stage2.py BASE OUT MAP_JSON
"""
import hashlib, json, sys

BASE_SHA = "ab25c162a727b0826adfb0b8fd5f3898969ed78260fc00e8bbcaa9e1e3b899d2"
ARCHIVE = "evidence/numgen/v1.21/stage1_intermediate.md"
PRED_SHA = "835a56f82b2641343a0e2fa116b049a167c62efd4d13fe41236966c117f4817e"
WT, AB, CHG = "## Appendix A. Working Thesis\n", "## Appendix B. Rejected / Guarded Formulations\n", "## Changelog\n"

def sha(b): return hashlib.sha256(b if isinstance(b, bytes) else b.encode("utf-8")).hexdigest()

def summary(base):
    import re
    line = next(l for l in base.split("\n") if l.startswith("**Status summary (scientific state fixed at v1.20;"))
    t = line.split(":**", 1)[1].strip()
    s = [x.strip() for x in re.split(r"(?<=[.;])\s+(?=[A-Z`$(])", t) if x.strip()]
    keep = s[:3]                     # current-state sentences; the version narrative sentences go to the release record
    assert keep[2].startswith("C7B global breadth")
    return " ".join(keep)

def header(base):
    return (
"# RTG_NUMBER_GENESIS_DSN_v1.21\n\n"
"**Title:** RTG Number Genesis — Relational Composition, Repetition, Number Representations, and Recurrence Holonomy  \n"
"**Date:** 26 October 2026  \n"
"**Scope:** Foundational construction of number-like representations and arithmetic compatibility from relational arrows/transitions, composition, repeatable event histories, orientation/inversion, finite multiplicity, phase/character structure, commensurability classification, and recurrence-holonomy diagnostics. Additive, difference, ratio, and multiplicative numerical forms are treated as sector-dependent representations unless a certified mechanism gives them stronger physical status.  \n"
"**Document class:** Foundational/technical bridge ledger (Methodology v1.4 §0.5); it does not modify the ontology, Dyadic, Discrete, Triadic, or Genesis dynamics, and it is not itself an OPEN-P1 physical bridge (Programme v1.3 SG-PROG-4). §1 profile exception: §1 states the imported foundations, the thesis and the three-track counting architecture with their scope guards in full (above the 400-word guide); a pointer-only §1 would drop those qualifications.  \n"
"**Document status:** DRAFT — v1.21 stage-2 candidate, not adopted; v1.20.8 governs until PI adoption. Release record (DRAFT): `records/numgen/NUMGEN_v1_21_RELEASE_RECORD.md`.  \n"
"**Supersedes:** `RTG_NUMBER_GENESIS_DSN_v1.20.8` (SHA-256 `" + PRED_SHA + "`; tag `numgen-v1.20.8`).  \n"
"**Companion documents:** current editions, pins used and consumers in §9.1 (Consumers and pins).  \n"
"**DSN Methodology:** v1.4 (tag `methodology-v1.4`).  \n"
"**Status summary:** " + summary(base) + "  \n"
"**Release record:** `records/numgen/NUMGEN_v1_21_RELEASE_RECORD.md`. Version history: Appendix A.\n")

APP_A = (
"## Appendix A — Version History {#appendix-a}\n\n"
"One compact entry per recent edition (Methodology v1.4 §1). The full changelog of v0.1–v1.20.8 and the three legacy notes "
"(v0.3 Change Note, v1.0 Result Note, v0.9 Result Note) are in the predecessor edition (tag `numgen-v1.20.8`, sections "
"\"Changelog\" and the notes after it); the held release records and packages of v1.20.x are on the branch "
"`upload/numgen-records` (hash check `records/numgen/NUMGEN_UPLOAD_HASH_CHECK_20261026.md`).\n\n"
"### v1.21 — 26 October 2026 — DRAFT (stage-2 candidate; not adopted)\n\n"
"- **Basis:** the reconciled v1.20.8 advisory (`records/numgen/ATLAS_ADVISORY_NUMGEN_v1_20_8_RECONCILIATION.md`), the two owner disposition records and their reconciliation (`records/numgen/NUMGEN_OWNER_DISPOSITION_RECONCILIATION_v1_20_8.md`); PI \"başla\" of 26 October 2026; co-owner review of stage 1 (PR #74, ACCEPTED after round 2).\n"
"- **Interfaces [science/scope] (stage 1):** `DYAD-THM-LPHASE-ROWA-REMAINDER` imported at §6.6 (pin `dyad-v6.4.22`, producer v6.4.19; the explicit-constant OPEN sub-item closed by the import; NUMGEN-RESULT-N5AS1-L-PHASE unchanged); RECOG v0.3.24 explicit-domain theorems recorded as consumer-side confirmations with the §9.1 acceptance matrix (nothing imported); domain labels (§6.2); consumers and pins (§9.1); pins Programme v1.3, Genesis v2.9, §7 Q403 v6.4.18; C7C-M4 hold with the TDR-G request.\n"
"- **RIDs and evidence (stage 1):** NUMGEN-RESULT-N5AS1-GAPLOCK-ALPHABET, NUMGEN-RESULT-N5AS1-GAPLOCK-COUNT, NUMGEN-RESULT-N5AS1-GAPLOCK-SLIP-RATIO, NUMGEN-RESULT-N5AS1-INF2, NUMGEN-RESULT-N3CP-CYCLIC-AVERAGE at their statements; evidence-state clause (§9.2); owner alias `DYAD-ALG-P5-RADIAL` (exact gate A1); sampled L-PHASE range live as `[NUM]`.\n"
"- **Compaction [layout] (stage 2):** current-only header with the §1 profile exception; this Appendix A; Working Thesis moved to Appendix C (heading letter only); one footer. Movement map `evidence/numgen/v1.21/movement_map.json`, checked by `tools/check_compaction.py`.\n"
"- **Unchanged:** every statement, proof, domain and grade of v1.20.8 outside the declared stage-1 edits; every OPEN status except the L-PHASE explicit-constant sub-item; Census-1 INCONCLUSIVE / INCONCLUSIVE; C7C-M4 HOLD.\n"
"- **Records:** release record `records/numgen/NUMGEN_v1_21_RELEASE_RECORD.md`; stage-1 intermediate SHA-256 `ab25c162…99d2` (round 1 `702e3917…3880` superseded); predecessor tag `numgen-v1.20.8`.\n\n"
"### v1.20.8 — 21 October 2026 — Adopted\n\n"
"- **Content:** maintenance: consumer synchronization (OFN v0.10, Dyadic v6.4.18, Genesis v2.8.9); OFN §1.1 imports narrowed to three DEF imports; six N-5A-S1 RIDs allocated (NUMGEN-DEF-N5AS1-PRIMITIVE-LIFT, NUMGEN-DEF-N5AS1-DEFECT, NUMGEN-RESULT-N5AS1-L-BACKBONE, NUMGEN-RESULT-N5AS1-L-MONO, NUMGEN-RESULT-N5AS1-L-PHASE, NUMGEN-RESULT-N5AS1-INF1); no result, proof, domain or grade changed.\n"
"- **Records:** release record `upload/numgen-records/NUMGEN_v1_20_8_RELEASE_RECORD.md` on the branch `upload/numgen-records` (SHA-256 `fb699967…1f97`); adopted from DRAFT r3 (`9d59cfa1…e7b3`); full entry: tag `numgen-v1.20.8`.\n\n"
"### v1.20.7 — 1 October 2026 — Adopted\n\n"
"- **Content:** M2-1 transported chain identity adopted at ALG grade; C7C-M2 Census-1 recorded INCONCLUSIVE / INCONCLUSIVE; grade-normalization inventory completed.\n"
"- **Records:** full entry: tag `numgen-v1.20.8`, section \"Changelog\" (no `numgen-v1.20.7` tag; the edition bytes `c4637e7a…ab28` are on the branch `upload/numgen-records`).\n\n")

FOOTER = "*END OF DOCUMENT — RTG_NUMBER_GENESIS_DSN_v1.21 (DRAFT stage-2 candidate; not adopted).*\n"

def build(base):
    assert sha(base) == BASE_SHA, "base is not the accepted stage-1 intermediate (round 2)"
    for m in (WT, AB, CHG):
        assert base.count(m) == 1, m
    i_wt, i_ab, i_chg = base.index(WT), base.index(AB), base.index(CHG)
    assert i_wt < i_ab < i_chg
    wt_body = base[i_wt + len(WT):i_ab]
    ab_part = base[i_ab:i_chg]
    assert ab_part.endswith("\n\n---\n\n") and wt_body.endswith("\n\n---\n\n")
    # both bodies are carried byte-identical, each with its own closing rule; only the heading letter of the
    # Working Thesis changes (A -> C) and the new Appendix A is placed first
    tail_new = APP_A + ab_part + "## Appendix C. Working Thesis\n" + wt_body + FOOTER
    i_head = base.index("\n## ")
    head_new = header(base)
    cand = head_new + base[i_head:i_wt] + tail_new
    ops = [
        {"id": "S2-H", "op": "replace-header", "archive": ["stage1-intermediate"], "new": head_new},
        {"id": "S2-T", "op": "replace-section", "class": "history-appendix", "archive": ["stage1-intermediate"],
         "start": WT, "end": None, "new": tail_new},
    ]
    return cand, ops

def main(argv):
    base_p, out, mp = argv[1:4]
    base = open(base_p, "rb").read().decode("utf-8")
    cand, ops = build(base)
    data = cand.encode("utf-8")
    open(out, "wb").write(data)
    m = {"study": "NUMGEN", "target": "v1.21", "stage": 2, "base": ARCHIVE, "base_sha256": BASE_SHA,
         "candidate_sha256": sha(data),
         "archives": [{"name": "stage1-intermediate", "path": ARCHIVE, "sha256": BASE_SHA}],
         "archives_note": "the stage-1 intermediate (round 2) archived byte-exact; every removed byte is in it; the predecessor tag numgen-v1.20.8 holds the same changelog and legacy notes",
         "profile": {"study": "NUMGEN", "ref_words": [], "history_words": [],
                     "checked_tag_prefixes": ["numgen-", "recog-", "gen-", "programme-", "ofn-", "methodology-", "rrf-", "tdrg-"],
                     "known_tags": ["numgen-v1.20.8", "dyad-v6.4.22", "recog-v0.3.24", "gen-v2.9", "programme-v1.3", "ofn-v0.10",
                                    "methodology-v1.4", "rrf-v0.8.4", "tdrg-v2.12.13", "dzt-v0.8", "dyad-v6.4.19"],
                     "summary_from": ["header"], "base_history_from": "## Changelog"},
         "operations": ops}
    json.dump(m, open(mp, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(sha(data))

if __name__ == "__main__":
    main(sys.argv)
