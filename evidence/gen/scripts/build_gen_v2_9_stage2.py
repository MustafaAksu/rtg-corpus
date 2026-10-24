#!/usr/bin/env python3
"""Genesis v2.9, stage 2: layout-only compaction (Methodology v1.4 §13.6) of the frozen stage-1 intermediate.

Writes the movement map and the candidate; tools/check_compaction.py then re-derives the candidate from the stage-1
intermediate and the map and checks every operation. This script also runs the owner guards G1–G6 (stage-2 scope
requested by the PI on 25 Oct 2026: preserve §6.3a–c, the GA-01/GA-02 text and the nine custody states).

Operations (all declared in the map; nothing else changes):
  S2-H  replace-header   current-only header (Methodology v1.4 §1.1): one predecessor with full hash; Document class
                         with the §1 profile exception; Methodology v1.4; companion editions pointed to §7 (B4 of the
                         atlas row check, carried here so the checker sees it); status summary built only from
                         sentences of the base status summary and the base §1 (profile summary_from).
  S2-A  replace-section  class history-appendix: Appendix A becomes one compact entry per edition; the full records
                         stay in the stage-1 intermediate (archive) and in Appendix A of v2.8.9 (tag gen-v2.8.9).
  S2-F  replace-footer   one footer line (the inherited footer chain is in the archive).
Not done here (no layout operation exists for it, or it is not layout): §1 text (kept under the declared §1 profile
exception); §7 headings (the Imports → Exports → Consumers → Pins order is already the order of the stage-1 file);
live history pointers carrying RIDs or tags; publication status lines (publication transform).

usage: build_gen_v2_9_stage2.py STAGE1 CANDIDATE MAP
"""
import hashlib, json, sys

STAGE1_SHA = "ca431ce90669cfb8bebdf104b52833d05c1147a36ab696fbb4a6160874867845"
ARCHIVE = {"name": "stage1-intermediate", "path": "evidence/gen/v2.9/stage1_intermediate.md", "sha256": STAGE1_SHA}
REL = "`records/gen/GEN_v2_9_RELEASE_RECORD.md`"

SUMMARY = " ".join([
    # a sentence opening with "**" is joined to its predecessor by the checker's sentence split, so the labelled
    # sourced-junction sentence comes first
    "**Local sourced-junction theorem** (§6.9, `GEN-THM-SOURCED-JUNCTION`).",
    r"If $w=0$, $\sigma_f\neq0$ and $\Delta_3>0$: vacuum gluing fails ($S_f = 0$ is impossible), and the constrained birth equation, which at $w=0$ reads $\tau d_\perp+S_f=0$ on $|d_\perp|^2=\Delta_3$, has exactly two antipodal solutions; selection of the physical branch is OPEN (GCL-02, §6.8).",
    "Primitive Genesis algebra through the certified tetrahedral quartic polynomials is retained.",
    "The standalone triad is a **universal chiral pump**: no quartic safe surface exists except $c=0$.",
    r"`GEN-THM-TRANSPORTED-CHIRAL-FACTOR-NOGO` (§6.3c) excludes local \(C^3\) submersive six-step factors for every real \(C^3\) network germ with the stated linear structure, zero quadratic part and chiral cubic invariant \(\mu\neq0\), under \((H_{\rm spec})\); a primitive-clock companion is recorded at the same grade as the §6.3b primitive statement.",
    r"This is a mathematical semiconjugacy exclusion for the stated real \(C^3\) class; no physical model, carrier, closure condition or \(\gamma\) is selected, and existence of an exactly transported realization is not asserted.",
    "The 9B physical lowering bridge, the 9B-tau physical sign/energy selection, and physical realization of the 9C raw-array premise remain open.",
    "Internal typing/model questions therefore remain OPEN alongside OPEN M and OPEN 0-Regge.",
])

HEADER = (
    "# RTG_GENESIS_GEOMETRY_DSN_v2.9\n\n"
    "**Title:** RTG Genesis Geometry Study — Canonical Scientific Ledger  \n"
    "**Date:** 25 October 2026  \n"
    "**Document status:** STAGE-2 CANDIDATE — not adopted (corrections of the reconciled v2.8.9 advisory and Methodology v1.4 compaction). "
    f"Release record: {REL}.  \n"
    "**Scope:** Primitive dyadic/triadic/tetrahedral Genesis algebra, quaternionic metric lift, UV completion, foam network structure, and Regge bridge. "
    "Imports settled continuous-branch results from Dyadic and Triadic with inherited scope; routes TDR-G dependencies through explicit bridge requirements only.  \n"
    "**Document class:** Technical scientific ledger (Methodology v1.4 §0.5). §1 profile exception: §1 gives statement-level readouts of the "
    "theorem-grade results with their hypotheses and scope qualifications (about 1,000 words); a pointer-only list would drop those qualifications.  \n"
    "**Supersedes:** `RTG_GENESIS_GEOMETRY_DSN_v2.8.9` (SHA-256 `d143673e9596abc900f54f269582299c87c9146504d6c9e1fd08ac294ba8c6fc`; tag `gen-v2.8.9`).  \n"
    "**Companion documents:** current editions, producer pins and companion references in §7 (Pins; Programme-context references).  \n"
    "**DSN Methodology:** v1.4 (tag `methodology-v1.4`).  \n"
    "**Programme tier:** Tier 3 — integrating study (placement recorded in Programme v1.3 §6.1); imports scoped continuous-branch results from Dyadic and Triadic; "
    "routes Discrete/TDR-G dependencies through explicit bridge requirements only.  \n"
    f"**Status summary:** {SUMMARY}  \n"
    f"**Release record:** {REL}. Version history: Appendix A.\n"
)

APPA_START = "## Appendix A — Version History {#appendix-a}\n"
APPA_END = "## Appendix B —"
APPA_NEW = (
    "## Appendix A — Version History {#appendix-a}\n\n"
    "One compact entry per edition (Methodology v1.4 §1). Full records of earlier editions — adoption metadata, draft-round records, review verdicts, "
    "the stacked status summaries and the inherited footer chain — are in Appendix A, the header and the footer of v2.8.9 (tag `gen-v2.8.9`, "
    "SHA-256 `d143673e…c6fc`), and in the release records named below.\n\n"
    "### v2.9 — 25 October 2026 — stage-2 candidate (not adopted)\n\n"
    "- **Basis:** the reconciled v2.8.9 advisory (`records/gen/ATLAS_ADVISORY_GEN_v2_8_9_RECONCILIATION.md`) and the two owner disposition records; "
    "PI authorization of 24 October 2026 (21 dispositions; F-1); atlas row check `records/gen/ATLAS_ROW_CHECK_GEN_v2_9_STAGE1.md` with B1–B3 applied in stage 1.\n"
    "- **Corrections [science/scope] (stage 1):** local sourced-junction theorem rescoped to its algebraic content with $\\Delta_3>0$; the minimizer clause "
    "is recorded in Appendix B (GA-01). Face-lift magnitude renamed $\\kappa\\to\\kappa_f$ (notation only), sign-explicit 9A pole–projector map, $B_*$ declared "
    "undefined (GA-02, GA-03, F-1). Scope words (GA-04, GA-05, GA-08, GA-09); one record per `GEN-OPEN-WPHASE` (GA-06); closed items out of active lists (GA-07).\n"
    "- **RIDs and evidence (stage 1):** `GEN-THM-QH-NOGO`, `GEN-THM-SINGLE-FACE-METRIC`, `GEN-THM-SOURCED-JUNCTION` (statements as in §6.7/§6.9; GB-10); "
    "custody states of the nine proof-source artifacts and the independent-contribution clause, defined once in §8 (GB-11); $c_\\theta^{(6)}$ archival status (GB-12); "
    "GSPLIT/DELTA-QC specialization with its $\\omega_{sc}$ convention (GB-13); T-6u case label (GB-14); tier wording (GB-16).\n"
    "- **Interfaces (stage 1):** Dyadic v6.4.22 import and the G-20 existence note for §6.3c (C2), the only change in §6.3a–§6.3c (GC-17); §7 Consumers and Pins, "
    "companion references at Programme v1.3 and OFN v0.10 (GC-18, GC-19). The OFN Q6 notice erratum (`records/gen/GENESIS_V2_8_9_NOTICE_ERRATUM_OFN_Q6_v0_1.md`) "
    "is a `[SESSION]` record accepted by the owner on 19 October 2026; it corrects notice wording only (GC-21).\n"
    "- **Compaction [layout] (stage 2):** current-only header with the §1 profile exception; this compact Appendix A; one footer. Movement map "
    "`evidence/gen/v2.9/movement_map.json`, checked by `tools/check_compaction.py`.\n"
    "- **Unchanged:** §6.3a–§6.3c apart from the G-20 note; every other RID's statement and grade; every OPEN status.\n"
    f"- **Records:** release record {REL}; stage-1 intermediate SHA-256 `ca431ce9…7845`; predecessor tag `gen-v2.8.9`.\n\n"
    "### v2.8.9 — 19 October 2026 — Adopted\n\n"
    "- **Content:** `GEN-THM-TRANSPORTED-CHIRAL-FACTOR-NOGO` (§6.3c) with the primitive-clock companion at `[ALG]` grade without RID (D-4).\n"
    "- **Records:** release record `upload/gen-records/GENESIS_V2_8_9_RELEASE_RECORD.md` (SHA-256 `f6df5d11…4181`); adoption, draft record and the "
    "negative-control replay note: Appendix A of v2.8.9 (tag `gen-v2.8.9`).\n\n"
    "### v2.8.8 — 19 October 2026 — Adopted\n\n"
    "- **Content:** maintenance: live Dyadic pins to v6.4.13; $\\nu_5^{(5)}$ attributed to `DYAD-ALG-NU5-P5` with its convention; no scientific claim changed.\n"
    "- **Records:** `upload/gen-records/GENESIS_V2_8_8_RELEASE_RECORD.md` (SHA-256 `03deb7cb…c049`).\n\n"
    "### v2.8.7 — 18 October 2026 — Adopted\n\n"
    "- **Content:** `GEN-THM-CHIRAL-CUBIC-FACTOR-LEMMA`, `GEN-THM-K3-SIXSTEP-FACTOR-NOGO`, `GEN-DEF-MEANFEEDBACK-FAMILY`, `GEN-THM-MEANFEEDBACK-SIXSTEP-NOGO`, SG-16.\n"
    "- **Records:** `upload/gen-records/GENESIS_V2_8_7_RELEASE_RECORD.md` (SHA-256 `d3fcc38e…9223`).\n\n"
    "### v2.8.6 — 16 October 2026 — Adopted\n\n"
    "- **Content:** `GEN-THM-K3-PLANAR-FACTOR-NOGO` (§6.3a); Dyadic v6.4.11 / OFN v0.9 source synchronization.\n"
    "- **Records:** `upload/gen-records/GENESIS_V2_8_6_RELEASE_RECORD.md` (SHA-256 `b6137587…3fec`).\n\n"
    "### v2.8.5 — 5 October 2026 — Adopted\n\n"
    "- **Content:** correction/reconciliation release: GCL-01–11 dispositions; adopted Triadic v1.6 reconciliation (CN-01–CN-05).\n"
    "- **Records:** release record not in the repository; adoption and draft records: Appendix A of v2.8.9 (tag `gen-v2.8.9`).\n\n"
    "### Earlier editions\n\n"
    "- v2.8.4, v2.8.3, v2.8.2, v2.8.1, v2.8.0, v2.7.7, v2.7.6, v2.7.5, v2.7.4, v2.7.3, v2.7.2, v2.7.1, v2.7, v2.6, v2.5, v2.4, v2.3, v2.2, v2.1, v2.0 — June 2026; "
    "the v1.1 update summary. Entries: Appendix A of v2.8.9 (tag `gen-v2.8.9`). Editions before v2.8.6 are not in the repository.\n\n"
    "---\n\n"
)
FOOTER_NEW = "*END OF DOCUMENT — RTG_GENESIS_GEOMETRY_DSN_v2.9 (stage-2 candidate; not adopted).*\n"

PROFILE = {
    "study": "GEN",
    "ref_words": [],
    "history_words": [],
    "checked_tag_prefixes": ["gen-", "triad-", "programme-", "ofn-", "methodology-", "rrf-", "recog-"],
    "known_tags": ["gen-v2.8.9", "dyad-v6.4.22", "triad-v1.6.1", "programme-v1.3", "ofn-v0.10", "methodology-v1.4", "rrf-v0.8.4"],
    "summary_from": ["header", "section1"],
}

def sha(b): return hashlib.sha256(b if isinstance(b, bytes) else b.encode("utf-8")).hexdigest()

def build(s1):
    assert sha(s1) == STAGE1_SHA, "input is not the frozen stage-1 intermediate"
    h_end = s1.index("\n## ")
    old_header = s1[:h_end]
    assert old_header.endswith("\n"), "header region must end at a line break"
    # the tool's header region is s[0:first "\n## "]; HEADER ends with one line break, so the blank line before
    # "## Local Tag Aliases" is kept from the base
    t = HEADER + s1[h_end:]
    i = t.index(APPA_START); j = t.index(APPA_END, i)
    assert t.count(APPA_START) == 1
    removed_a = t[i:j]
    assert removed_a.endswith("---\n\n")
    t = t[:i] + APPA_NEW + t[j:]
    lines = t.split("\n")
    k = next(n for n, l in enumerate(lines) if l.startswith("*END OF DOCUMENT"))
    t = "\n".join(lines[:k]) + "\n" + FOOTER_NEW
    mp = {
        "study": "GEN", "target": "v2.9", "stage": "compaction",
        "base": "frozen stage-1 intermediate (round 2; commit e3dfee9)",
        "base_sha256": STAGE1_SHA, "candidate_sha256": sha(t),
        "archives": [ARCHIVE],
        "archives_note": "The stage-1 intermediate holds every removed byte (old header, Appendix A, footer chain). The tag gen-v2.8.9 is "
                         "listed in known_tags but not named as an archive, so the checker does not read version strings in live sentences that "
                         "point to it (e.g. 'OFN v0.9') as Appendix A entries of that tag (same reason as RECOG v0.3.24 stage 2).",
        "profile": PROFILE,
        "operations": [
            {"id": "S2-H", "op": "replace-header", "archive": ["stage1-intermediate"], "new": HEADER,
             "what": "current-only header; Document class with the §1 profile exception; one predecessor with full hash; Methodology v1.4; "
                     "companion editions pointed to §7; status summary from base summary and base §1 sentences only (B4 of the atlas row check)",
             "why": "Methodology v1.4 §1.1 current-only header; atlas row check B4 (header companion/methodology/status lines as declared operations)"},
            {"id": "S2-A", "op": "replace-section", "class": "history-appendix", "archive": ["stage1-intermediate"],
             "start": APPA_START, "end": APPA_END, "new": APPA_NEW,
             "what": "Appendix A compacted to one entry per edition; full records in the archive and at tag gen-v2.8.9",
             "why": "Methodology v1.4 §1.1: one compact Appendix A entry per edition; draft rounds and review verdicts in release records"},
            {"id": "S2-F", "op": "replace-footer", "archive": ["stage1-intermediate"], "new": FOOTER_NEW,
             "what": "one footer line; the inherited footer chain is in the archive", "why": "Methodology v1.4 §1.1: one footer"},
        ],
    }
    return t, mp

def main(argv):
    s1p, outp, mapp = argv[1:4]
    s1 = open(s1p, encoding="utf-8").read()
    t, mp = build(s1)
    open(outp, "w", encoding="utf-8").write(t)
    mp["candidate_sha256"] = sha(open(outp, "rb").read())
    json.dump(mp, open(mapp, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(mp["candidate_sha256"], len(mp["operations"]), "operations")

if __name__ == "__main__":
    main(sys.argv)
