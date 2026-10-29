#!/usr/bin/env python3
"""OFN v0.11 stage 2: layout-only compaction of the frozen stage-1 intermediate.

usage: build_ofn_v0_11_stage2.py STAGE1 OUT MAP
  STAGE1 = evidence/ofn/v0.11/stage1_intermediate.md (SHA-256 cf38b61b...7ce3)
  OUT    = the stage-2 candidate
  MAP    = the movement map read by tools/check_compaction.py

Operations (Methodology v1.4 §13.6; classes as in tools/check_compaction.py):
  S2-H   replace-header      Document status line only (stage-1 -> stage-2 wording)
  S2-E01 history-removal     §0.1 v0.9 revision-boundary paragraph
  S2-E02 history-removal     §0.3 v0.8/v0.9 and v0.10 adoption paragraphs
  S2-E03 history-removal     §6.4 closing history sentence
  S2-E04 history-removal     §9 "*v0.10:*" paragraph (the current count stays in the paragraph above it)
  S2-E05..E07 history-removal " (v0.10)" in the three "Reconciliation input" labels
  S2-E08 history-removal     §12.3 opening sentence on the adopted v0.9 release
  S2-E09 history-removal     §12.3 closing sentence on the resolved RECOG/NUMGEN mismatch
  S2-E10 history-removal     §12.4 sentence on REQ-O08-07's historical fulfilment
  S2-E11 history-removal     §12.4 clause naming the v0.9 reconciliation
  S2-S1  history-section     §12.1: v0.9 register replaced by a pointer; the RECOG row and the evidence rows still cited
                             are kept byte-identical except for the removed "*v0.10:* " labels
  S2-S2  history-section     §12.2: v0.9 adoption narrative replaced by a pointer
  S2-S5  history-section     §12.5: v0.10 decisions/assembly record replaced by a pointer
  S2-T   history-appendix    Appendix C: one entry per edition; footer as one line
Every removed byte is in the archive (the stage-1 intermediate, committed byte-exact). No claim enters stage 2.
"""
import hashlib, json, sys

STAGE1_SHA = "cf38b61b5cd3e268e412dbd10b28a2117f86f1c7423fd2dd33f466a8e5437ce3"
ARCHIVE = "evidence/ofn/v0.11/stage1_intermediate.md"
CTX = 48


def sha(b):
    return hashlib.sha256(b if isinstance(b, bytes) else b.encode("utf-8")).hexdigest()


def one(s, x, what):
    n = s.count(x)
    if n != 1:
        raise SystemExit(f"{what}: {n} occurrences of {x[:70]!r}")
    return s.index(x)


def removal(s, oid, start, end, note):
    """history-removal: delete s[start-marker .. end-marker) with CTX characters of context on both sides."""
    i = one(s, start, oid)
    j = s.index(end, i + len(start)) if end else i + len(start)
    a, b = max(0, i - CTX), min(len(s), j + CTX)
    old = s[a:b]
    new = s[a:i] + s[j:b]
    one(s, old, oid)
    return {"id": oid, "op": "edit", "class": "history-removal", "archive": ["stage1-intermediate"],
            "old": old, "new": new, "note": note}


def apply(s, op):
    if op["op"] == "edit":
        one(s, op["old"], op["id"])
        return s.replace(op["old"], op["new"])
    if op["op"] == "replace-section":
        i = one(s, op["start"], op["id"])
        j = s.find(op["end"], i + len(op["start"])) if op.get("end") else len(s)
        return s[:i] + op["new"] + s[j:]
    if op["op"] == "replace-header":
        k = s.index("\n## ")
        return op["new"] + s[k:]
    raise SystemExit(op["id"])


def main(stage1, out, mpath):
    s1 = open(stage1, encoding="utf-8").read()
    if sha(s1.encode("utf-8")) != STAGE1_SHA:
        raise SystemExit("stage-1 input is not cf38b61b...7ce3")
    s = s1
    ops = []

    def add(op):
        nonlocal s
        s = apply(s, op)
        ops.append(op)

    # ---- S2-H header: Document status only
    head = s[:s.index("\n## ")]
    old_st = ("**Document status:** DRAFT — stage-1 intermediate of v0.11; adoption pending "
              "(`records/ofn/OFN_v0_11_RELEASE_RECORD.md`). `ofn-v0.10` remains the governing edition until adoption and tag.  ")
    new_st = ("**Document status:** DRAFT — v0.11 candidate: layout-only compaction (stage 2) of the frozen stage-1 intermediate; "
              "adoption pending (`records/ofn/OFN_v0_11_RELEASE_RECORD.md`). `ofn-v0.10` remains the governing edition until adoption and tag.  ")
    one(head, old_st, "S2-H")
    add({"id": "S2-H", "op": "replace-header", "archive": ["stage1-intermediate"], "new": head.replace(old_st, new_st),
         "note": "Document status line only; the status summary and all other fields are unchanged"})

    # ---- history removals
    add(removal(s, "S2-E01", "\n\n**Revision boundary:** v0.9 is reconciliation", "\n\n**v0.11 revision boundary:**",
                "§0.1: v0.9 revision boundary (history of v0.9; recorded in Appendix C at ofn-v0.10)"))
    add(removal(s, "S2-E02", "OFN v0.8 was adopted on September 21, 2026", "*v0.11 (adoption pending):*",
                "§0.3: v0.8/v0.9 and v0.10 adoption paragraphs (now in the Appendix C entries; the Draft-2 hash moves there)"))
    add(removal(s, "S2-E03", " Existing OFN08-C17/C22 history remains unchanged; the v0.9 source update is recorded separately.",
                None, "§6.4: history sentence"))
    add(removal(s, "S2-E04", "*v0.10:* the twenty identities and statuses above are unchanged.",
                "All twenty-one entries belong to OFN",
                "§9: v0.10 change paragraph; the current count (twenty-one, twenty ACTIVE / one PARTIAL) stays in the paragraph above"))
    for k, follow in (("05", " class C (§5.5.4) has exact invariant lock surfaces"),
                      ("06", " §5.5.2 Q4 requires the genuine-triad class"),
                      ("07", " Q5 (§5.5.2) requires complete-state relabeling covariance")):
        lab = "Reconciliation input (v0.10):" + follow
        i = one(s, lab, "S2-E" + k)
        start = "Reconciliation input"
        op = {"id": "S2-E" + k, "op": "edit", "class": "history-removal", "archive": ["stage1-intermediate"],
              "old": s[i:i + len(lab)], "new": s[i:i + len(lab)].replace(" (v0.10):", ":", 1),
              "note": "edition label removed from a reconciliation-input label"}
        add(op)
    add(removal(s, "S2-E08", "The twenty inherited OPEN identities/statuses, nine definition identities",
                "IMP/RF/CUST/REQ labels are administrative records",
                "§12.3: sentence describing the adopted v0.9 release (current counts are in the header and §9)"))
    add(removal(s, "S2-E09", " The earlier RECOG v0.3.1→NUMGEN threshold-RID mismatch", "\n\n### 12.4",
                "§12.3: resolved historical request"))
    add(removal(s, "S2-E10", " REQ-O08-07's historical fulfillment for v1.19 receipt is not reopened.", None,
                "§12.4: historical fulfilment"))
    add(removal(s, "S2-E11", "; neither stopping FMS nor this v0.9 reconciliation automatically authorizes it", None,
                "§12.4: clause naming the v0.9 reconciliation; the requirement before it is unchanged"))

    # ---- §12.1 register
    h121, h122 = "### 12.1 Evidence and Release-State Register\n", "### 12.2 Contributions and Adoption Boundary\n"
    i = one(s, h121, "S2-S1"); j = s.index(h122, i)
    sec = s[i:j]
    rows = [l for l in sec.split("\n") if l.startswith("| RECOG v0.3.20 |") or l.startswith("| *v0.10:* ")]
    if len(rows) != 5:
        raise SystemExit(f"S2-S1: expected 5 kept rows, found {len(rows)}")
    rows = [r.replace("| *v0.10:* ", "| ", 1) for r in rows]
    new121 = (h121 + "\n"
              "Evidence of earlier editions is listed in their release records and Appendix C entries; the v0.9 register "
              "(the adopted v0.8 baseline, the v0.9 source editions and release checks) is preserved in §12.1 at tag `ofn-v0.10`. "
              "The rows below are the evidence this edition still cites.\n\n"
              "| Source/record | Evidence access and stage | Consequence |\n|---|---|---|\n" + "\n".join(rows) + "\n\n")
    add({"id": "S2-S1", "op": "replace-section", "class": "history-section", "archive": ["stage1-intermediate"],
         "start": h121, "end": h122, "new": new121,
         "note": "v0.9 register replaced by a pointer; RECOG row and the four evidence rows kept (labels removed)"})

    # ---- §12.2
    h123 = "### 12.3 Local Identities, Actual Consumers and Handoffs\n"
    new122 = (h122 + "\n"
              "Each edition's adoption act, approved object and finalization boundary are recorded in its Appendix C entry and "
              "release record; the v0.9 adoption boundary is preserved in §12.2 at tag `ofn-v0.10`. Contributions follow the header "
              "attribution; no separate reviewer-account authentication or approval by every inherited author is inferred.\n\n")
    add({"id": "S2-S2", "op": "replace-section", "class": "history-section", "archive": ["stage1-intermediate"],
         "start": h122, "end": h123, "new": new122, "note": "v0.9 adoption narrative replaced by a pointer"})

    # ---- §12.5
    h125 = "### 12.5 v0.10 Decisions and Assembly Record\n"
    end125 = "---\n\n<a id=\"ofn-historical-scenarios\"></a>"
    new125 = ("### 12.5 Edition Decisions\n\n"
              "Decisions O10-P1–P7 (adopted 19 October 2026) are summarized in the Appendix C v0.10 entry; the decision table and the "
              "v0.10 assembly record are preserved in §12.5 at tag `ofn-v0.10`. The v0.11 dispositions, by row of the joint owner "
              "reconciliation, are in `records/ofn/OFN_v0_11_RELEASE_RECORD.md`.\n\n")
    add({"id": "S2-S5", "op": "replace-section", "class": "history-section", "archive": ["stage1-intermediate"],
         "start": h125, "end": end125, "new": new125, "note": "v0.10 decisions/assembly record replaced by a pointer"})

    # ---- Appendix C
    hC = "## Appendix C — Version History\n"
    i = one(s, hC, "S2-T")
    c = s[i:]
    v11h = "### v0.11 — 29 October 2026 — DRAFT (stage-1 intermediate; adoption pending)\n"
    a = one(c, v11h, "S2-T v0.11"); b = c.index("\n\n### v0.10 — 19 October 2026 — ADOPTED", a)
    v11_bullets = c[a + len(v11h):b]
    newC = (
        "## Appendix C — Compact Version History {#appendix-c}\n\n"
        "One entry per edition (Methodology v1.4). The full entries for v0.10 and earlier, with their draft-stage entries, are "
        "preserved verbatim in Appendix C at tag `ofn-v0.10`; the v0.1–v0.6 entries are in `ARCHIVED_OFN_HISTORY_v0_7.md`, "
        "which is not supplied to the corpus.\n\n"
        "### v0.11 — 29 October 2026 — DRAFT (adoption pending)\n"
        + v11_bullets + "\n"
        "- **Layout (stage 2):** current-only compaction of §§0.1, 0.3, 6.4, 9 and 12 and of this appendix; no claim, RID, "
        "status or OPEN change (`evidence/ofn/v0.11/movement_map.json`).\n\n"
        "### v0.10 — 19 October 2026 — ADOPTED / FMS model-selection interface release\n\n"
        "- **Authority:** adopted by Mustafa (PI), approving O10-P1–P7 in full on Draft 2 (`58e2dec5…3610`) after both OFN "
        "co-owners accepted it; v0.10 superseded v0.9.\n"
        "- **Assembly:** Draft 1 (`d94e1e39…8c36`) built by `build_ofn_v0_10_draft1.py` from the adopted v0.9 bytes "
        "(`5ae8fdab…9795`) and the co-owner-accepted handoff v0.8.2 (`6e4fc3c3…564b1d`); Draft 2 added the editorial "
        "corrections C2-A and C2-B; finalization by `release_ofn_v0_10.py` changed metadata, proposed→registered wording, the "
        "history entry and the footer only.\n"
        "- **Decisions:** O10-P1 source synchronization (Genesis v2.8.9, DYAD v6.4.13–v6.4.16, RRF v0.8.3); O10-P2 the "
        "triad model contract and Standard C definitions; O10-P3 class C declared a different conditional model under RRF v0.8.3 "
        "§0.3, with the model-contract-row request; O10-P4 the two §5.5.3 local results; O10-P5 the scoped FMS disposition, "
        "RF-O10-02 reference-only; O10-P6 OPEN-OFN-TRIAD-CLASS and the reconciliation inputs to OPEN-OFN-3B, FRUSTRATION and "
        "OPA without status change; O10-P7 notices N-O10-1–4.\n"
        "- **Registered:** `RTG-OFN-DEF-TRIAD-MODEL-CONTRACT`, `RTG-OFN-DEF-STANDARD-C`, `RTG-OFN-ALG-RAW-STANDARD-C-NOGO`, "
        "`RTG-OFN-ALG-NARROW-Q6-PLANAR-PRODUCT`, `RTG-OFN-OPEN-TRIAD-CLASS`. No scientific OPEN closed.\n\n"
        "### v0.9 — 13 October 2026 — ADOPTED / second-pass reconciliation release\n\n"
        "- **Authority:** finalized at the PI's release instruction on consolidated Draft 2 (SHA-256 "
        "`770d533feb26beb5a1e4d11ccb8544d0625414fec0b3037d110024177d66090a`) after the supplied final review recommended "
        "adoption; decisions O09-P1–P4; v0.9 superseded v0.8.\n"
        "- **Assembly:** 34 reviewed amendments applied to the adopted v0.8 baseline (SHA-256 "
        "`56bc991d28c4a6f3e841eec5ac8c4550528fbaac91bcfc23ab0dc2540bd2a514`, matching its release record); REQ-O09-01 "
        "fulfilled.\n"
        "- **Scope:** reconciliation and sharpening of existing OPEN questions; no new definition, axiom, physical model, grade, "
        "research closure or custody transfer; the twenty OPEN statuses (nineteen ACTIVE, one PARTIAL) unchanged; OFN-side "
        "ACCEPT SCOPED for the FMS handoff (O09-P3), pilot closeout not adopted.\n"
        "- **Record:** `RTG_ONTOLOGICAL_FOUNDATIONS_v0_9_RELEASE_RECORD.md` and its validation records; not supplied to the corpus.\n\n"
        "### v0.8 — 21 September 2026 — ADOPTED / final definition and model-selection release\n\n"
        "- **Authority:** Mustafa (PI) accepted Review Draft 3 as canonical, with O08-P1–P6 as amended; v0.8 superseded v0.7.\n"
        "- **Registered:** nine definition IDs; `RTG-OFN-HYP-FSP-U` as a hypothesis, not a physical axiom; "
        "`RTG-OFN-ALG-STAR-TOKEN-SHIFT` and `RTG-OFN-ALG-FREE-ANTIPODAL-CONTINUATION` under OFN custody; XFER-O08-01 offered "
        "to TDR-G. Twenty research OPENs (nineteen ACTIVE, one PARTIAL).\n"
        "- **Record:** `RTG_ONTOLOGICAL_FOUNDATIONS_v0_8_RELEASE_RECORD.md` and the v0.8 release package; neither is in the corpus.\n\n"
        "### v0.7 — June 2026\n\n"
        "- Genesis axiom-base revision and proto-geometry distinction: the trap/obstruction-to-annihilation axiom deleted as an "
        "axiom and replaced by the imported theorem LEM-NOANNIHIL; A8, IQP-E and FSP surfaced, with OPA as an OPEN; OPEN-OFN-IQP, "
        "-OPA, -FSP and -SECTOR added; the OFN-DIST-ZN three-level distinction installed (§4.6).\n\n"
        "### v0.1–v0.6\n\n"
        "- Earlier foundation-ledger editions, including rank typing and the interpretive build sequence (v0.4).\n\n"
        "---\n\n"
        "*END OF DOCUMENT — RTG_ONTOLOGICAL_FOUNDATIONS_v0.11 — DRAFT, adoption pending; `ofn-v0.10` governs until adoption and tag.*\n"
    )
    add({"id": "S2-T", "op": "replace-section", "class": "history-appendix", "archive": ["stage1-intermediate"],
         "start": hC, "end": None, "new": newC,
         "note": "base history region (profile base_history_from) relocated; one entry per edition; one footer line"})

    open(out, "w", encoding="utf-8", newline="\n").write(s)
    mp = {
        "study": "OFN", "target": "v0.11", "stage": 2,
        "base": ARCHIVE, "base_sha256": STAGE1_SHA, "candidate_sha256": sha(s.encode("utf-8")),
        "archives": [{"name": "stage1-intermediate", "path": ARCHIVE, "sha256": STAGE1_SHA}],
        "archives_note": "the stage-1 intermediate, committed byte-exact; every removed byte is in it. The predecessor tag "
                         "ofn-v0.10 holds the v0.10 and earlier history verbatim.",
        "profile": {
            "study": "OFN", "ref_words": [],
            "history_words": ["v0.8", "v0.9", "v0.10", "the adopted release"],
            "checked_tag_prefixes": ["ofn-", "gen-", "rrf-", "tdrg-", "numgen-", "recog-", "triad-", "programme-",
                                     "methodology-", "er2b-"],
            "known_tags": ["ofn-v0.10", "dyad-v6.4.22", "gen-v2.9", "rrf-v0.8.4", "tdrg-v2.12.14", "numgen-v1.21",
                           "recog-v0.3.26", "triad-v1.6.1", "programme-v1.3", "methodology-v1.4", "er2b-v0.3"],
            "summary_from": ["header"],
            "base_history_from": "## Appendix C — Version History",
        },
        "operations": ops,
    }
    json.dump(mp, open(mpath, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
    open(mpath, "a", encoding="utf-8").write("\n")
    print(f"candidate {mp['candidate_sha256']}  ({len(ops)} operations)")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        raise SystemExit(__doc__)
    main(*sys.argv[1:])
