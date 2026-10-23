#!/usr/bin/env python3
"""RECOG v0.3.23, stage 2: layout-only compaction of the stage-1 intermediate.

Writes the compacted candidate and its movement map. The map is what tools/check_compaction.py
re-derives and checks; this script uses the checker's own apply_ops, so the two cannot disagree.
No claim, grade, qualifier, RID, OPEN status or evidence pointer of the live text is changed.
Passages that carry claim tags (for example the retained v0.3.2 specification of R8, which quotes
`[OPEN]` and `[NUM strong]`, the former R11 text with its `[OPEN]` sub-items, the R9 degree-7 budget
paragraph, the §7.1/§7.2 audit tables) cannot be relocated under the checker's history rules and stay.

Operations (all against the stage-1 intermediate 0b2d5109…bc76):
  M01 replace-header   current-only header (Methodology v1.4 §1.1); the 24 stacked status summaries, the
                       25-edition Supersedes list and the freeze history stay in the archived header
  M04 replace-section  OPEN R10: the v0.3.2 enclosure template (instantiated by Dyadic v6.4.10)
  M05 edit ref-subst   OPEN R10 status line: pointer to the tagged edition
  M06 replace-section  Appendix A: one compact entry per edition; full records at tag recog-v0.3.22
  M07 replace-footer   footer for the candidate

usage (repository root): build_recog_v0_3_23_stage2.py INTERMEDIATE OUT_CANDIDATE OUT_MAP
"""
import hashlib, json, os, sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "tools"))
import check_compaction as cc  # noqa: E402

BASE_SHA = "0b2d5109d75f457ea6168d32f342a6814d8410554808a3b11a596aa467aabc76"
STAGE1_COMMIT = "97b0425d11d701fd02cc02a07351e21df40a4fb8"
PATH = "dsn/RTG_RELATIONAL_RECOGNITION_DSN.md"
ARCHIVES = [
    {"name": "recog-v0.3.22", "git": f"recog-v0.3.22:{PATH}",
     "sha256": "0dcce9e44d48fbedbcd5af083283fce12560cc17a3951a7632ff0e50db44bcd9",
     "role": "adopted predecessor; holds every relocated passage that predates v0.3.23"},
    {"name": "recog-v0.3.23-stage1", "git": f"{STAGE1_COMMIT}:{PATH}", "sha256": BASE_SHA,
     "role": "reviewed stage-1 intermediate (commit 97b0425); holds the stage-1 header lines and the stage-1 Appendix A entry"},
]
PROFILE = {
    "study": "RECOG",
    "ref_words": ["template"],
    "history_words": [],
    "checked_tag_prefixes": ["recog-", "numgen-", "methodology-", "gen-", "ofn-", "rrf-", "rer-"],
    "known_tags": ["dyad-v6.4.19", "dyad-v6.4.20", "dyad-v6.4.21", "dyad-v6.4.22", "numgen-v1.20.8",
                   "methodology-v1.3", "methodology-v1.4", "gen-v2.8.9", "ofn-v0.10", "rrf-v0.8.4", "rer-v0.2"],
    "summary_from": ["header", "section1"],
}

HEADER = r"""# RTG_RELATIONAL_RECOGNITION_DSN_v0.3.23

**Title:** RTG Relational Recognition Study — Comparators, Return Defect, and Event Strata on the Dyadic Substrate
**Date:** 23 October 2026
**Scope:** Substrate-level mathematics of *recognition* — how a relational distinction is compared with its transported self or with another distinction, what residue a closed history leaves, and which loci of the comparator/transport geometry qualify as candidate recognition events — worked on the postulated continuous dyad generator $T$ and its diagnostic shear twins. Ontological readings are carried as `[HYP]` only.
**Document class:** Technical scientific ledger (Methodology v1.4 §0.5). §1 profile exception: §1 gives RID-level readouts of the certified results with their load-bearing qualifications (about 1,300 words); a pointer-only list would drop those qualifications (Methodology v1.4 §1.1 item 3).
**Document status:** DRAFT — v0.3.23 candidate (atlas-advisory corrections and FC-21, stage 1, reviewed; Methodology v1.4 compaction, stage 2); not adopted.
**Supersedes:** `RTG_RELATIONAL_RECOGNITION_DSN_v0.3.22` (SHA-256 `0dcce9e44d48fbedbcd5af083283fce12560cc17a3951a7632ff0e50db44bcd9`; tag `recog-v0.3.22`).
**Companion documents:** current owner editions and every import pin: §7 (synchronization note) and §7.3 — Dyadic `dyad-v6.4.22`, Number Genesis `numgen-v1.20.8`, Genesis v2.8.9, OFN v0.10, RRF v0.8.4 (convention and registry reference); Discrete Genesis v2.12.13 (reference only, no import).
**DSN Methodology:** v1.4 (tag `methodology-v1.4`); `RECOG | RTG Relational Recognition` is in its namespace registry.
**Programme tier:** Tier 3 — Continuous Programme, downstream of Dyadic and Genesis (Programme Overview §6). The study prefix `RECOG` is registered in DSN Methodology v1.4 and in Programme Overview v1.2 Tier 3; the Programme entry's selected RECOG edition is updated by programme synchronization.
**Status summary:** On the explicit start set $U=\{0<Q_0\le\tfrac1{625}\}$, A1a's local extension $D_M^U$ of the Number Genesis defect formula aligns exactly with Dyadic's block phase, and $MQ_M\to1$; on the intersection with NUMGEN's existential tube $U_{\rm NUMGEN}$, $D_M^U$ equals NUMGEN's $D_M$. Hence: the limit $C_D^{\rm ext}=\lim_M(D_M^U-\tau\log M)$ exists and equals $\tau\log Q_0-M_W$ (`[THM]`, using RECOG's own R9 through Dyadic T1/T2); on $U\cap U_{\rm NUMGEN}$ it equals NUMGEN's $C_D$, and the asymptotic phase exists **without R9** (existence only, `[RESULT] [from: ALG]`, no explicit radius); quantitatively $C_D^{\rm ext}=\tau\log Q_0-\mathcal P_2(W_0)+E$ per Dyadic OPEN 21 row (`[THM]`). `[THM]` [RID: RECOG-THM-A1A-PHASE-EXISTENCE-U] (v0.3.23) On all of $U$, without R9 and without NUMGEN INF-1, $C_D^{\rm ext}$ exists and equals an explicit absolutely convergent series in the block amplitudes and the Dyadic row-A block remainders (existence and that series only). $C_D$ depends on the start state. R6 stays ACTIVE.
**Release record:** `records/recog/RECOG_v0_3_23_RELEASE_RECORD.md`. Version history: Appendix A. The earlier header — status summaries v0.2.1–v0.3.22, the full supersedes list and the freeze history — is in v0.3.22 (tag `recog-v0.3.22`).
"""

APPA = r"""
## Appendix A — Version History

One compact entry per edition (Methodology v1.4 §1). Full records of earlier editions — adoption metadata, draft-round records, review verdicts, the stacked status summaries and the freeze history — are in Appendix A and the header of v0.3.22 (tag `recog-v0.3.22`, SHA-256 `0dcce9e4…bcd9`). Scientific corrections and retired claims: Appendix B.

### v0.3.23 — 23 October 2026 — DRAFT candidate

- **Basis:** the atlas advisory `records/recog/ATLAS_ADVISORY_RECOG_v0_3_22.md` as disposed by the PI on 23 Oct 2026 (`records/recog/ATLAS_ADVISORY_RECOG_v0_3_22_DISPOSITION_RECONCILIATION.md` §5), erratum E-0322-1, Methodology v1.4.
- **New RIDs (statements unchanged):** RECOG-THM-R9-COMPARATOR-INCOMPLETENESS (§6.13a corollary), RECOG-ALG-SWAP-ODD-RHO (§6.4 lemma). Named sub-statements: the radial identity under RECOG-ALG-NU3-CLOSED-FORM; the $C_0$-avoidance corollary under RECOG-THM-P2-HET.
- **New science (separately reviewed):** RECOG-THM-A1A-PHASE-EXISTENCE-U (§6.13b) — R9-free existence of $C_D^{\rm ext}$ on all of $U$ with an explicit series, from DYAD-THM-LPHASE-ROWA-REMAINDER; RECOG-ART-A1A-EXISTENCE-U (§8).
- **Imports:** NUMGEN $D_M$ and INF-1 by RID (`NUMGEN-DEF-N5AS1-DEFECT`, `NUMGEN-RESULT-N5AS1-INF1`, v1.20.8; A1a-G1 closed); Dyadic A1a imports by RID and section at v6.4.22 with the current owner tag forms (line pins removed); §7 rows gain the Dyadic RIDs registered in v6.4.20; claim audit: quoted statements present at the cited RIDs in the current source.
- **Status and wording:** R10 status "CLOSED (v0.3.2) — delivered and accepted"; §1 RECOG-OPEN-INTERSECTION carries the `[HYP]` tag of its §6.5 entry; frame labels and rounded equalities; R9 finite-$q_0$ pointer and partial budget; $j^6S_h=j^6R_0$, with $S_h$ an exact involution whose commutation with $F$ is certified only through degree 6; `[RESULT]` blocks paired or split per block; stale F2 pointers; §7.2/§7.3 current state (RF-1 fulfilled; no notice state changed); §8 repository locations.
- **Compaction [layout]:** current-only header with the §1 profile exception; this compact Appendix A; the v0.3.2 template of the closed OPEN R10 left in v0.3.22 (tag `recog-v0.3.22`); one footer.
- **Unchanged:** every existing RID's statement and grade; every OPEN status (R1, R3 PARTIAL; R4, R5, R6 ACTIVE; R2, R7–R11 CLOSED).
- **Records:** release record `records/recog/RECOG_v0_3_23_RELEASE_RECORD.md`; stage-1 intermediate SHA-256 `0b2d5109…bc76`; predecessor tag `recog-v0.3.22`.

### v0.3.22 — 20 October 2026 — Adopted

- **Content:** A1a scientific cell §6.13b (asymptotic phase and the Number Genesis constant $C_D$): RECOG-DEF-A1A-PHASE-INTERFACE, RECOG-THM-A1A-LIFT-ALIGNMENT, RECOG-THM-A1A-RECIPROCAL-AMPLITUDE, RECOG-THM-A1A-PHASE-EXISTENCE-ALT, RECOG-RESULT-A1A-PHASE-EXISTENCE-NG, RECOG-THM-A1A-CD-IDENTIFICATION, RECOG-RESULT-A1A-CD-AGREEMENT, RECOG-THM-A1A-CD-PRIMITIVE-EXPANSION; four artifact IDs (§8). No existing RID, grade or OPEN status changed.
- **Records:** `records/recog/RECOG_v0_3_22_RELEASE_RECORD.md`; post-release note `records/recog/RECOG_v0_3_22_POST_RELEASE_MAINTENANCE_NOTE.md`; adoption, draft rounds r1–r3 and review verdicts: Appendix A of v0.3.22 (tag `recog-v0.3.22`).

### Earlier editions

Identities as printed in the v0.3.22 header; full entries in Appendix A of v0.3.22 (tag `recog-v0.3.22`).

| Edition | State or date | SHA-256 | Content |
|---|---|---|---|
| v0.3.21 | adopted 20 Oct 2026 | `a3459522…0ae3` | owner synchronization (G2 audits, §7.2, §7.3) |
| v0.3.20 | frozen 19 Oct 2026 | `fdb8c9a7…b8df` | orientation conjugacy |
| v0.3.19 | frozen | `2b006b9f…2b36` | R6 identification and inheritance ledger (CELL-F4) |
| v0.3.18 | frozen | `9a4c7184…904e` | owner synchronization |
| v0.3.17 | frozen | `e04452b9…8f2` | R5 CELL-G1 |
| v0.3.16 | frozen | `6e010221…4152d` | R7 closed |
| v0.3.15 | candidate | `e97fa520…25d5cd` | R7 rank-locus accessibility |
| v0.3.14 | frozen | `d10c2a98…4b43` | R7 Stage 2 refuted |
| v0.3.13 | frozen | `acbdeffc…aacb7` | F3 coupling audit |
| v0.3.12 | candidate | `fca3f986…3129` | F2(d) retention classification |
| v0.3.11 | candidate | `686e3fff…0fa1` | F2(c1) registered retention |
| v0.3.10 | candidate | `077e8fe7…0ba` | F2(c0) Whitney fold |
| v0.3.9 | candidate | `d1112cee…eb9a` | F2(a) closure |
| v0.3.8 | candidate | `4b7347d4…240d` | F2(b) token shadow |
| v0.3.7 | candidate | `b77a549a…4648` | R6 identifiability audit |
| v0.3.6 | frozen | `fc790fad…16eb` | twin radial-access theorem |
| v0.3.5 | frozen | `3ba74002…abd6` | positive-branch theorem (frozen bytes not in the repository; recovery list §3) |
| v0.3.4 | frozen | `39665f89…80df` | R9 theorem |
| v0.3.3 | frozen 26 Sep 2026 | `701d56ac…decb` | theorem promotion |
| v0.3.2 | frozen 25 Sep 2026 | — | scope patch: Dyadic v6.4.10 consumer acceptance; R11 ledger |
| v0.3.1 | frozen 19 Sep 2026 | — | external audit rounds 1–2 |
| v0.3 | 18 Sep 2026 | — | — |
| v0.2.1 | September 2026 | — | pre-freeze patch, critique round 2 |
| v0.2 | September 2026 | — | — |
| v0.1 | September 2026 | — | — |
"""

FOOTER = "*END OF DOCUMENT — RTG_RELATIONAL_RECOGNITION_DSN_v0.3.23 (DRAFT candidate, 23 October 2026).*\n"

OPS = [
    {"id": "M01", "op": "replace-header", "class": "presentation", "new": HEADER, "archive": ["recog-v0.3.23-stage1"],
     "note": "current-only header; status-summary sentences taken verbatim from the base header summary and base §1"},
    {"id": "M04", "op": "replace-section", "class": "history-section",
     "start": "\nTemplate (to be posed only after R11 fixes the chart):", "end": "\n---\n\n---\n**OPEN R7",
     "new": "", "archive": ["recog-v0.3.22"], "note": "OPEN R10 v0.3.2 template, instantiated by DYAD-THM-NF-REM and DYAD-THM-PRIM-CTR"},
    {"id": "M05", "op": "edit", "class": "ref-subst",
     "old": "The template below is now instantiated",
     "new": "The v0.3.2 template (tag `recog-v0.3.22`) is now instantiated", "archive": ["recog-v0.3.22"]},
    {"id": "M06", "op": "replace-section", "class": "history-appendix",
     "start": "\n## Appendix A — Version History", "end": "\n## Appendix B —", "new": APPA,
     "archive": ["recog-v0.3.23-stage1"], "note": "compact Appendix A; full records at tag recog-v0.3.22 and in the stage-1 intermediate"},
    {"id": "M07", "op": "replace-footer", "class": "presentation", "new": FOOTER, "archive": ["recog-v0.3.22"]},
]


def main(base_path, out_path, map_path):
    raw = open(base_path, "rb").read()
    assert hashlib.sha256(raw).hexdigest() == BASE_SHA, "base is not the stage-1 intermediate"
    base = raw.decode("utf-8")
    mp = {"study": "RECOG", "target": "v0.3.23", "stage": "compaction",
          "base": "corrected intermediate (stage 1, round 2; commit 97b0425)", "base_sha256": BASE_SHA,
          "archives": ARCHIVES, "profile": PROFILE, "operations": [dict(o) for o in OPS]}
    cand, _ = cc.apply_ops(base, json.loads(json.dumps(mp)))
    data = cand.encode("utf-8")
    open(out_path, "wb").write(data)
    mp["candidate_sha256"] = hashlib.sha256(data).hexdigest()
    json.dump(mp, open(map_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(mp["candidate_sha256"], len(raw), "->", len(data), "bytes")


if __name__ == "__main__":
    main(*sys.argv[1:4])
