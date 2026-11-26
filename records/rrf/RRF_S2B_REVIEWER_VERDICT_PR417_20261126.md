# RRF v0.9 S2b — reviewer verdict on PR #417

**Date:** 26 November 2026.
**Status:** [SESSION] / NONCANONICAL. Reviewer lane (Claude, independent reviewer / second co-owner). This is a compaction (Methodology v1.4 §13.6) review of a DRAFT candidate only. It is not adoption, release, tag, BASELINE edit or merge authorization; the PI decides.
**Reviewed:** PR #417 `chatgpt/rrf-v0-9-s2b`, exact head `917f76efd304885bf2eeb92ac6e23967a8ce2b58`.
- Candidate `dsn/RTG_RRF_REPRESENTATION_REGISTRY.md`: 121,071 bytes, SHA-256 `0163284ed22973ff65d5869d62726f4539e481ac0c199bba588d225bdd0c5d24`.
- Input: the S2a freeze `98da97c3` (`390f75e4…9d72`, 131,089 bytes; accepted in `RRF_S2A_REVIEWER_VERDICT_PR404_20261126.md` §5).
- Movement map: `evidence/rrf/v0.9/s2b_movement_map.json`, 76 operations.

## Verdict

**ACCEPT WITH CHANGES.**

S2b is a valid §13.6 compaction of the accepted S2a intermediate:
- every source and destination line is accounted for;
- the exact spans are byte-equal;
- all 18 editorial replacements and 15 navigation insertions are presentational or navigational;
- the 10 archive spans are dated history whose current content survives at a live home;
- no scientific statement, grade, domain, clock, dependency or OPEN state changed.

Two small required changes (C1, C2) and one release-gate condition (G1) remain.

The profile-specific adapter `check_rrf_s2b.py` is accepted as the §13.6 checker **for this RRF edition**, within the limits stated in §3.

## 1. Checks (native, exact head)

| Check | Result |
|---|---|
| `python -I evidence/rrf/scripts/check_rrf_s2b.py` | exit 0. Four negative controls PASS: changed coefficient with rehash, missing exact op, duplicate span, broken archive locator. `RRF_S2B_EXACT_MAP_PASS 691 source lines 654 destination lines 76 operations 0163284e…`, equal to the working-tree SHA-256. |
| `tools/dsn_lint.py --prev` (S2a freeze) | informational: −10,018 bytes (−7.6 %), 0 new RIDs, one footer, 67 RIDs |
| Reviewer checks `evidence/rrf/scripts/rrf_s2b_reviewer_checks.py` (independent of the adapter; output `evidence/rrf/v0.9/s2b_reviewer_checks_pr417_917f76ef.txt`) | **C1 token loss:** 22 tokens lost S2a→candidate; 21 occur only in archived spans; 1 outside (see C1 below). **C2 import coverage:** all 46 live S2a import lines are indexed; the one lost import tag is archived only, and its RID `DYAD-CAND-FLAT-CENTRALIZER` stays live (I-32). **C3 owner-grade readouts:** 26/26 in the import ledger are on the cited owner line with the cited RID. **C4:** the archive base `98da97c3` is an ancestor of HEAD. **C5:** negative control PASS. |
| Archive review (10 spans; read in full) | M010, M021 and M069–M074 are verbatim in `rrf-v0.8.4` and are dated history (old receipts, §9/§10 histories, superseded pins). M003 holds the S2a staging paragraph and the v0.8.2–v0.8.4 publication/OPEN20 overlays; M016 holds the historical §0.2 receipts. Their current content stays live: B-6 ⇔ B-an ∧ B-3 (L211, L219), OPEN 20 B-∞ CLOSED with B-an/B-6 ACTIVE (L58, L164, L202), the class-C/O10-P3 contract (L430), and RF-O09-03/04, SG-15 and the P2-B pointers (L70ff). No current obligation, assumption or result is removed (§13.6 item 3). |
| Editorial review (18) | Header YAML becomes the Markdown field header; stage labels and headings are de-dated; §7 is renamed; Appendix A/B are added. One substantive wording change, M039 ("PI-approved"), is covered by C2 below. |
| Navigation review (15) | The section map, six local-ID attachment lines (each at the S2a-accepted home, marked "registration awaits adoption"), §6.5/§7.4/§7.5 headings, the import ledger M049 (60 rows; grade readouts checked as above; elsewhere the source block controls) and Appendix B. No claim is introduced. |
| Integrity | The 15 unresolved-looking local "§" references are owner-section references inherited unchanged from S2a. Removing §9/§10 broke none of them. |

## 2. Required changes

**C1 — predecessor adoption-record pointer.**
- *Problem:* the S2a header line `predecessor adoption record: records/rrf/RTG_RRF_REPRESENTATION_REGISTRY_v0_8_4_ADOPTION_RECORD.md` was dropped in the YAML→Markdown header rewrite (M001). The path now occurs nowhere in the live file.
- *Fix:* add it to **Supersedes** or **Companion documents**.
- *Acceptance:* `rrf_s2b_reviewer_checks.py` C1 passes (0 lost tokens outside archive).

**C2 — approval citation for the closure criteria (M039).**
- *Problem:* "Closure criteria (PI-approved for the v0.9 candidate, 26 November 2026)" is an approval statement in a live DSN. The build record derives it by interpretation from "S2b kabul / Merge işlemleri yapılabilir". The reviewer neither confirms nor disputes it.
- *Fix:* name the decision record (comment ID or record path) in the line. If the PI has not explicitly approved the narrowed wording, revert to "candidate wording; PI_PENDING".
- *Acceptance:* the line cites a retrievable PI decision record, or PI_PENDING is restored.

## 3. Checker eligibility (profile-specific adapter)

The adapter is accepted for this edition. Its four negative controls are adequate for what it checks.

Stated limits, which the release record must repeat:
1. Archive and editorial *classification* is not mechanically proved. A live span reclassified as archive, with the candidate rehashed, would pass mechanically. This review's §1 archive and editorial readings carry that part.
2. Navigation text is unconstrained beyond its declared bytes. M049's grade readouts are checked here by C3.
3. The adapter should also assert that the base commit is reachable (an ancestor of HEAD), as reviewer check C4 does.

No change to the shared `tools/check_compaction.py` is implied. A general RRF profile extension would need its own review.

## 4. Release-gate condition

**G1 — retrievability of the archived bytes.**
- Eight archive spans are retrievable from the tag `rrf-v0.8.4`.
- Two (M003, M016) exist verbatim only in the S2a commit `98da97c3`, which is neither a tag nor a release record.

At release:
- the release record must name `98da97c3` and `390f75e4…9d72` as the intermediate baseline (§13.6, two-stage build);
- #417 must merge as a merge commit, never squash, so that `98da97c3` stays reachable from `main`;
- optionally, the map can add `rrf-v0.8.4` line locators for the eight tag-retrievable spans.

## 5. Gate

After C1 and C2 are applied and a readback at the corrected head, S2b is accepted for the release review. The candidate cannot be adopted before the PI decision, the release record (carrying G1 and §3's limits) and outbound notices (Programme IF30/31/33). BR-Q2 (#414) remains a separate review; nothing from it enters v0.9.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
