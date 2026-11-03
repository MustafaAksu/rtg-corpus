#!/usr/bin/env python3
r"""Triadic v1.7 stage 2: layout-only compaction of the frozen stage-1 intermediate.

usage: build_triad_v1_7_stage2.py STAGE1 OUT MAP
  STAGE1 = evidence/triad/v1.7/stage1_intermediate.md (SHA-256 b47d294d...a66a, round 3; rounds 1 and 2 are in Git history)
  OUT    = the stage-2 candidate
  MAP    = the movement map read by tools/check_compaction.py

Operations (Methodology v1.4 §13.6; classes as in tools/check_compaction.py):
  S2-H   replace-header      v1.4 header (row 17): one field per line, scientific Scope, one predecessor with its hash,
                             status summary drawn only from base header-summary and §1 sentences, no history text
  S2-M   replace-section     history-section (row 18): §6.18 "Per-module dispositions" v1.6 table -> pointer
  S2-E01 edit                history-removal (row 18): §9 ", stage 1" in the edition label
  S2-E02 edit                history-removal (row 18): §9 "History — v1.6.1 release" and "History — v1.6 release" spans
  S2-E03 edit                history-removal: the aliases note "heading grade suffixes are migrated in stage 2" (done in
                             stage-1 round 3)
  S2-B1  replace-section     history-appendix (row 20): Appendix B v1.6 successor table restated in the v1.4 template
  S2-B2  replace-section     history-appendix (row 20): Appendix B v1.6 orientation-chain table restated in the template
  S2-A   replace-section     history-appendix (row 20): Appendix A, one compact entry per edition
  S2-F   replace-footer      single footer (row 22)
Every removed byte is in the stage-1 intermediate (committed byte-exact) and, for v1.6.1 text, in `triad-v1.6.1`.
No claim, grade or RID enters stage 2. Rows 19 (headings), 18 (§7.4 paragraph) and 23 were done in stage 1 round 3,
because the checker has no layout operation for them. Row 29 (history_appendix profile, PR #113) is deferred.
"""
import hashlib, json, re, sys

STAGE1_SHA = "b47d294d9dc82b78f05e02c99e04100177c78480c453438d5d4fca86e14ba66a"
ARCHIVE = "evidence/triad/v1.7/stage1_intermediate.md"
TAG_ARCHIVE = "triad-v1.6.1:dsn/RTG_TRIADIC_BIRTH_LIFT_DSN.md"
TAG_SHA = "95340abe57e999ed48681502152113d8fdb3102f74f45a25aa66c2d0092d451f"
CTX = 48


def sha(b):
    return hashlib.sha256(b if isinstance(b, bytes) else b.encode("utf-8")).hexdigest()


def one(s, x, what):
    n = s.count(x)
    if n != 1:
        raise SystemExit(f"{what}: {n} occurrences of {x[:70]!r}")
    return s.index(x)


def removal(s, oid, start, end, note, archive=("stage1-intermediate",)):
    """history-removal: delete s[start .. end) (end exclusive; end=None: just the start string) with context."""
    i = one(s, start, oid)
    j = s.index(end, i + len(start)) if end else i + len(start)
    a, b = max(0, i - CTX), min(len(s), j + CTX)
    old = s[a:b]
    one(s, old, oid)
    return {"id": oid, "op": "edit", "class": "history-removal", "archive": list(archive),
            "old": old, "new": s[a:i] + s[j:b], "note": note}


def apply(s, op):
    if op["op"] == "edit":
        one(s, op["old"], op["id"])
        return s.replace(op["old"], op["new"])
    if op["op"] == "replace-section":
        i = one(s, op["start"], op["id"])
        j = s.find(op["end"], i + len(op["start"])) if op.get("end") else len(s)
        if j < 0: raise SystemExit(f'{op["id"]}: end not found')
        return s[:i] + op["new"] + s[j:]
    if op["op"] == "replace-header":
        k = s.index("\n## ")
        return op["new"] + s[k:]
    if op["op"] == "replace-footer":
        lines = s.split("\n")
        i = next(n for n, l in enumerate(lines) if l.startswith("*END OF DOCUMENT"))
        return "\n".join(lines[:i]) + "\n" + op["new"]
    raise SystemExit(op["id"])


HEADER = """# RTG_TRIADIC_BIRTH_LIFT_DSN_v1.7

**Title:** RTG Triadic Birth-Lift Study — Scientific Ledger
**Date:** 2 November 2026
**Scope:** The continuous $2\\to3$ birth family, the scoped $K_3/K_4$ return models and the typed diagnostic phase and orientation models (root-closed model, historical executed models, corrected coefficient extensions), with their consumer exports. No complete physical birth law, independent-orientation physical carrier or discrete TDR-G bridge is selected.
**Document class:** Technical scientific ledger
**Document status:** DRAFT — v1.7 stage-2 candidate (layout only, over the stage-1 intermediate `b47d294d…a66a`); adoption pending. `triad-v1.6.1` governs until adoption and tag. Consumer acceptance is not implied.
**Supersedes:** `RTG_TRIADIC_BIRTH_LIFT_DSN_v1.6.1` (tag `triad-v1.6.1`, SHA-256 `95340abe57e999ed48681502152113d8fdb3102f74f45a25aa66c2d0092d451f`), on adoption.
**Companion documents:** governing editions read for v1.7 — Programme Overview v1.3 (`programme-v1.3`); DSN Methodology v1.4 (`methodology-v1.4`); OFN v0.12 (`ofn-v0.12`); Dyadic Oscillator v6.4.23 (`dyad-v6.4.23`); Genesis Geometry v2.9 (`gen-v2.9`); OPEN-M v0.7.1 (`uvm-v0.7.1`); RRF v0.8.4 (`rrf-v0.8.4`); TDR-G v2.12.14 (`tdrg-v2.12.14`). Proof imports keep claim-level pins (§7.1–§7.2).
**DSN Methodology:** v1.4 (tag `methodology-v1.4`).
**Status summary:** This release does not select a complete physical birth law, an independent-orientation physical carrier, or a discrete TDR-G bridge. The recovered T-6c2/T-6e producers establish an orientation-output normalization correction: T-6d's root variable is retained, T-6e's raw-determinant extraction is retained, and downstream uses that treated the raw increment as the normalized orientation rate are narrowed to historical executed-model records. The former safety-wedge/no-basin/phase-steering obstruction chain is not a current corrected-model result. T-6j2 is PARTIAL with only its historical root-closed torsional excursion retained; T-6m retains its exact reference quarter-turn and producer-frame forcing polynomial, not the wedge obstruction. The 96:1 coefficient comparison is bookkeeping until source/model correspondence is proved. No corrected-field trajectory campaign is treated as scientifically decisive before the T-6r acceptance contract (§2) is met.
**Programme tier:** Tier 3 — Continuous Programme, conditional on the selected generator; no maturity regrade.
**Co-owners:** Claude and ChatGPT (PI designation, 18 Oct 2026); v1.7 prepared by Claude, change-focused review by ChatGPT.
**Records:** v1.7 release record `records/triad/TRIAD_v1_7_RELEASE_RECORD.md` (written at adoption); stage-1 build `evidence/triad/scripts/build_triad_v1_7_stage1.py` with `records/triad/TRIAD_v1_7_STAGE1_IMPLEMENTATION_MATRIX.md`; stage-2 movement map `evidence/triad/v1.7/movement_map.json`; v1.6.1 adoption and release records `records/triad/OWNER_ADOPTION_v1_6_1.json` and `records/triad/RELEASE_RECORD_v1_6_1.md`.
**Evidence location:** the v1.6 accepted evidence package `evidence/accepted_r4_2/` is held by the PI and is **not in the repository**. Relative script, input and evidence paths in §8 refer to that package root unless a repository path is given; the hashes printed there remain the identities. Repository holdings and missing items: `records/triad/TRIAD_SOURCE_RECOVERY_LIST.md`.
**Repository:** `rtg-corpus`
"""

# Markdown line breaks: every header field line except the last ends with two spaces.
_h = HEADER.split("\n")
_f = [n for n, l in enumerate(_h) if l.startswith("**")]
HEADER = "\n".join(l.rstrip() + "  " if n in _f[:-1] else l for n, l in enumerate(_h))

FOOTER = "*END OF DOCUMENT — RTG_TRIADIC_BIRTH_LIFT_DSN_v1.7 — DRAFT, stage-2 candidate; adoption pending; `triad-v1.6.1` governs until adoption and tag.*\n"

MODULE_POINTER = """### Per-module dispositions

The v1.6 per-module disposition table (accepted r4.2 scope) is history and is not repeated here; see §6.18 of `triad-v1.6.1`. Current module status is stated at each point of use (§§6.4–6.14) and in the §2 module records.

"""

APPENDIX_A = """## Appendix A — Version History {#appendix-a}

### v1.7 — 2 November 2026 — DRAFT (adoption pending)
- **§6.18, §6.4, §1 [COR, scope]:** the off-root extension of the §6.4 coefficients is not unique; $f_s$, $f_c$ are stated for both root-equivalent extensions; $D=\\mathcal G/Q_s$ is a first integral in the $Q_c$-free extension and has $\\dot D=r\\,q_1D$ in the literal one (ODE-scope remark, no RID); domain and the six-step-block ODE clock stated. Reason: the displayed $\\Delta Q_c^{(1)}$ carries $Q_c$.
- **§6.18 [scope]:** `TRIAD-ALG-T6E-ORIENTATION-NORMALIZATION` typed as the first-variation (degree-3) coefficient of $\\Delta\\mathcal G\\equiv0$; RID kept.
- **§6.9 [corollary, no RID]:** coercive bound $6(\\sqrt3-1)K\\le A_\\theta^{\\rm corr}\\le6(\\sqrt3+1)K$ inside `TRIAD-ALG-T6L-NORMALIZED-TORSION-SIGN`.
- **§2 [scope]:** `TRIAD-OPEN-T6R` acceptance contract C1–C6; `TRIAD-OPEN-T6Q` coordinate sign table, labelled bookkeeping.
- **§1 [scope]:** the 96:1 status stated once, with the metric-dictionary caveat.
- **§7 [currency]:** claim-level repins (Dyadic v6.4.23, Genesis v2.9, Programme v1.3, OFN v0.12, RRF v0.8.4, TDR-G v2.12.14; two pins held); per-recipient consumer matrix; stale handoff queue and receipt paragraph removed.
- **§9, §6 headings, Appendix B [form, scope]:** identifier set stated (46 RIDs); compound tags unpacked; release labels removed from qualifiers; heading grades normalized; current classification of the v1.5 negative records; two Appendix B tables restated in the v1.4 template.
- **Header, Appendix A, footer [layout]:** Methodology v1.4 header; one entry per edition; single footer; the v1.6 per-module disposition table relocated.
- Release record: `records/triad/TRIAD_v1_7_RELEASE_RECORD.md` (at adoption). Predecessor: `triad-v1.6.1`.

### v1.6.1 — 19 October 2026 — ADOPTED
- Birth-remainder scope correction (D3, D3-R1), receiving-review corrections (H-R1, H-R2), source sync (E1), consumer synchronization notices. Release record: `records/triad/RELEASE_RECORD_v1_6_1.md`. Full entry and draft rounds: Appendix A of `triad-v1.6.1`.

### v1.6 — 5 October 2026 — ADOPTED
- T-6s/t/u successor identities; recovered-producer orientation-normalization correction and model-contract separation; historical phase chain narrowed. Drafts r1–r4.2: Appendix A of `triad-v1.6.1`.

### v1.5 — June 2026
- T-6u apex source ratio added; isometric apex-lift model rejected as a physical source estimate.

### v1.4 — June 2026
- T-6s and T-6t certificates added.

### v1.3 — June 2026
- T-6j2 and T-6p closed; SG-14 added.

### v1.2 — June 2026
- T-6m convention annotation; exact torsion-turn root.

### v1.1 — June 2026
- T-6m birth-policy phase-angle audit incorporated.

### v1.0 — June 2026
- Safety-wedge renaming and sufficiency caveat.

### v0.15 — May 2026
- T-6d through T-6l incorporated.

### v0.14 and earlier
- T-6a through T-6k incorporated progressively; the global $K_3$ explosiveness overclaim introduced and revoked.

The full text of every entry above is in Appendix A of `triad-v1.6.1`.

"""


def cells(row):
    return [c.strip() for c in row.strip().strip("|").split("|")]


def restate_table1(sec):
    """v1.6 successor lifecycle: | Historical RID | Original | Successor and status | Reason |"""
    rows = [l for l in sec.split("\n") if l.startswith("| [RID:")]
    out = []
    for r in rows:
        rid, orig, succ, reason = cells(r)
        out.append(f"`[SUPERSEDED]` {rid} Original: {orig}.  \nReason: {reason} Replacement: {succ}. Recorded in: v1.6.")
    return "\n\n".join(out) + "\n\n", rows


def restate_table2(sec):
    """v1.6 orientation chain: | Historical/current-use RID | Successor / disposition | Reason |"""
    rows = [l for l in sec.split("\n") if l.startswith("| ") and not l.startswith("| Historical/current-use RID") and not l.startswith("|---")]
    out = []
    for r in rows:
        rid, succ, reason = cells(r)
        if rid.startswith("[RID:"):
            head, orig = rid, "current use of the historical proposition under this RID (proposition text in the v1.5 file, not in the repository)"
        else:
            head, orig = "[RID: none]", rid
        out.append(f"`[SUPERSEDED]` {head} Original: {orig}.  \nReason: {reason} Replacement: {succ}. Recorded in: v1.6.")
    return "\n\n".join(out) + "\n\n", rows


def main(argv):
    if len(argv) != 4:
        raise SystemExit(__doc__)
    base_b = open(argv[1], "rb").read()
    if sha(base_b) != STAGE1_SHA:
        raise SystemExit("input is not the frozen stage-1 intermediate")
    base = base_b.decode("utf-8")
    s = base
    ops = []

    def add(op):
        nonlocal s
        ops.append(op)
        s = apply(s, op)

    k = s.index("\n## ")
    add({"id": "S2-H", "op": "replace-header", "class": "presentation", "archive": ["stage1-intermediate"], "new": HEADER,
         "note": "row 17: v1.4 header; removed header text (stage-1 status lines, v1.6.1/v1.6 history, draft hashes) is in the stage-1 intermediate and in triad-v1.6.1"})
    add({"id": "S2-M", "op": "replace-section", "class": "history-section", "archive": ["stage1-intermediate", "triad-v1.6.1"],
         "start": "### Per-module dispositions (summary; point-of-use text in §§6.4–6.14)", "end": "---\n\n## §7. Import Ledger",
         "new": MODULE_POINTER, "note": "row 18: v1.6 per-module disposition table (history) relocated; identical bytes in triad-v1.6.1 §6.18"})
    add(removal(s, "S2-E01", ", stage 1", None, "row 18: stage label in the §9 edition line"))
    add(removal(s, "S2-E02", " **History — v1.6.1 release:**", "  \n**Source custody:**",
                "row 18: §9 v1.6.1 and v1.6 release-history spans (in triad-v1.6.1 §9)", ("stage1-intermediate", "triad-v1.6.1")))

    add(removal(s, "S2-E03", " Section-heading grade suffixes are migrated in stage 2.", None,
                "row 19 follow-up: process note made obsolete by stage-1 round 3 (headings done there)"))

    i1 = one(s, "| Historical RID | Original recorded verdict / proposition | Adopted successor and status | Reason |", "S2-B1")
    j1 = s.index("`[COR]` **Thread-4 evidence count:**", i1)
    new1, rows1 = restate_table1(s[i1:j1])
    add({"id": "S2-B1", "op": "replace-section", "class": "history-appendix", "archive": ["stage1-intermediate", "triad-v1.6.1"],
         "start": "| Historical RID | Original recorded verdict / proposition | Adopted successor and status | Reason |",
         "end": "`[COR]` **Thread-4 evidence count:**", "new": new1,
         "note": "row 20: v1.6 successor table restated as [SUPERSEDED] template entries; every cell kept verbatim"})
    i2 = one(s, "| Historical/current-use RID | Adopted successor / disposition | Reason |", "S2-B2")
    j2 = s.index("`[DEF]` **Historical r3 identities retained for traceability.**", i2)
    new2, rows2 = restate_table2(s[i2:j2])
    add({"id": "S2-B2", "op": "replace-section", "class": "history-appendix", "archive": ["stage1-intermediate", "triad-v1.6.1"],
         "start": "| Historical/current-use RID | Adopted successor / disposition | Reason |",
         "end": "`[DEF]` **Historical r3 identities retained for traceability.**", "new": new2,
         "note": "row 20: v1.6 orientation-chain table restated as [SUPERSEDED] template entries; every cell kept verbatim"})
    add({"id": "S2-A", "op": "replace-section", "class": "history-appendix", "archive": ["stage1-intermediate", "triad-v1.6.1"],
         "start": "## Appendix A — Version History {#appendix-a}", "end": "## Appendix B — Retired and Rejected Claims {#appendix-b}",
         "new": APPENDIX_A, "note": "row 20: one compact entry per edition; full v1.6.1-and-earlier text in triad-v1.6.1 Appendix A"})
    add({"id": "S2-F", "op": "replace-footer", "class": "presentation", "archive": ["stage1-intermediate"], "new": FOOTER,
         "note": "row 22: single footer"})

    open(argv[2], "w", encoding="utf-8", newline="\n").write(s)
    mp = {
        "study": "TRIAD", "target": "v1.7", "stage": 2,
        "base": ARCHIVE, "base_sha256": STAGE1_SHA, "candidate_sha256": sha(s),
        "archives": [{"name": "stage1-intermediate", "path": ARCHIVE, "sha256": STAGE1_SHA},
                     {"name": "triad-v1.6.1", "git": TAG_ARCHIVE, "sha256": TAG_SHA}],
        "archives_note": "the stage-1 intermediate, committed byte-exact, holds every removed byte; the predecessor tag holds the v1.6.1 and earlier history verbatim.",
        "profile": {"study": "TRIAD", "ref_words": [], "history_words": ["History —", "stage 1", "stage 2"],
                    "checked_tag_prefixes": ["triad-", "gen-", "rrf-", "ofn-", "programme-", "methodology-", "uvm-", "tdrg-", "dyad-"],
                    "known_tags": ["triad-v1.6.1", "gen-v2.9", "rrf-v0.8.4", "ofn-v0.12", "programme-v1.3", "methodology-v1.4",
                                   "uvm-v0.7.1", "tdrg-v2.12.14", "dyad-v6.4.23"],
                    "summary_from": ["header", "section1"]},
        "verbatim_cells": {"S2-B1": [c for r in rows1 for c in cells(r)], "S2-B2": [c for r in rows2 for c in cells(r)]},
        "operations": ops,
    }
    json.dump(mp, open(argv[3], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"operations: {len(ops)}; candidate sha256: {sha(s)}; lines: {s.count(chr(10))}")


if __name__ == "__main__":
    main(sys.argv)
