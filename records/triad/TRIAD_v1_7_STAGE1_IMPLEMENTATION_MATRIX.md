# Triadic v1.7 — stage-1 implementation matrix

**Date:** 30 October 2026. **Prepared by:** Claude (Triadic co-owner); for the change-focused review by ChatGPT.
**Status:** working record. Builds nothing beyond the stage-1 intermediate; adopts nothing.
**Round 2 (2 November 2026):** applies R140-F1 of ChatGPT's change-focused review (PR #140 review `5738872551`, ACCEPT WITH CHANGE) to the §7.4 consumer matrix, and R140-F2 (PR comment `6580920857`) to the merge chain. The round-1 intermediate `19af7ee3…6163` (commit `b5f1488`) stays in Git history.
**Round 3 (2 November 2026):** applies the heading part of row 19 (edits G01–G11; Methodology v1.4 §3.5), the §7.4 history-paragraph removal of row 18 (V16) and the repository locator of row 23 (R04). They are moved from stage 2 to stage 1 because `tools/check_compaction.py` has no layout operation that may change tag text (CONVENTIONS §4.2: anything touching tags is stage 1). The round-2 intermediate `a89c5768…1a62` (commit `f39b60f`, accepted in review `5739033005`) stays in Git history. V16 removes a paragraph carrying a status tag and math, and R04's old locator contains digits outside the checker's reference grammar, so neither is expressible as a stage-2 operation either. Needs the co-owner's change-focused check of these thirteen edits only. Round 3 also completes two stale-phrase checks that round 2 meant to add to gate K7 but did not (the insertion missed its anchor); a negative control now covers each.
**Authority:** the confirmed co-owner reconciliation `records/triad/TRIAD_OWNER_DISPOSITION_RECONCILIATION_v1_6_1.md` (PR #139; ChatGPT review `5714190994`, CONFIRMED / ACCEPT SCOPED) and the PI's stage-1 start of 30 October 2026.

## Identities

| Object | Identity |
|---|---|
| Base | `triad-v1.6.1`, `dsn/RTG_TRIADIC_BIRTH_LIFT_DSN.md`, SHA-256 `95340abe57e999ed48681502152113d8fdb3102f74f45a25aa66c2d0092d451f` |
| Builder | `evidence/triad/scripts/build_triad_v1_7_stage1.py` (99 assertion-gated edits; modes `str`, `live`, `line`, `dropline`) |
| Stage-1 intermediate | `dsn/RTG_TRIADIC_BIRTH_LIFT_DSN.md` on this branch = `evidence/triad/v1.7/stage1_intermediate.md`, SHA-256 `b47d294d9dc82b78f05e02c99e04100177c78480c453438d5d4fca86e14ba66a` (round 3; 1,263 lines; also in the edit log and `stage1_check_output.txt`). Stage 2 is checked against this hash |
| Edit log | `evidence/triad/v1.7/stage1_edit_log.json` (old/new text and hash chain for every edit) |
| Checker | `evidence/triad/scripts/check_triad_v1_7_stage1.py`: gates K1–K8, S1, S5, S6 ALL PASS; 16 negative controls ALL CAUGHT (round 2 adds two for R140-F1; round 3 adds three) (`evidence/triad/v1.7/stage1_check_output.txt`) |
| Lint | `tools/dsn_lint.py --prev` (informational, no gate): `evidence/triad/v1.7/dsn_lint_stage1.txt`. Its `new_rids: 1` counts the two new cross-references `DYAD-ALG-KP-FRAME-SCALE` and `RTG-OFN-ALG-REF-CLOSURE-COMPARISON`; the Triadic RID set is unchanged (K3) |

Commands, from the repository root:
```
git show triad-v1.6.1:dsn/RTG_TRIADIC_BIRTH_LIFT_DSN.md > base.md
python -I -B evidence/triad/scripts/build_triad_v1_7_stage1.py base.md cand.md log.json
python -I -B evidence/triad/scripts/check_triad_v1_7_stage1.py base.md cand.md log.json --controls
```

## Rows → edits

| Row | Settled content (reconciliation) | Edits | Where in v1.7 |
|---|---|---|---|
| 1 | f_s, f_c defined for both root-equivalent extensions; domain; ODE clock in six-step block units; D remark (Ḋ = 0 in (b); Ḋ = r q₁ D in (a), with the D ≡ 0 exception); no RID; H₁, H₂ limitation | S02 Q01 X02 X03 X04 | §1; §6.4 T-6d ODE; §6.18 consequences, item 1, new D remark |
| 2 | Gram relation typed as degree-3 first variation of ΔG ≡ 0; weights (1, ½); degree-4 discarded terms; six-step clock; RID kept | Q01 X01 X06 | §6.4; §6.18 new paragraph after "Correct rate"; §6.14 export row |
| 3 | Coercive bound `[ALG]` inside the `TRIAD-ALG-T6L-NORMALIZED-TORSION-SIGN` block; no new RID; no persistence | T01 | §6.9 |
| 4 | C1–C6 current contract with C1 group and C3 off-root extension; interface-constraint sentence; no decisive trajectory campaign before the contract | S04 P01 P04 | §1 queue line; §2 queue item and T-6r record |
| 5 | Sign table (exchange, single, double flip) with σ column; bookkeeping, not a physical action; T-6n unchanged; closure criterion on the complete-state action | P02 P05 | §2 queue item and T-6q record; checked by gate S5 |
| 6 | No change (T-6s/t/u) | — | — |
| 7 | 96:1 OPEN, stated once in §1 with the hypothetical 192 metric caveat; pointers elsewhere | S01 N01 X05 | §1; §6.1; §6.18 |
| 8 | Claim-level repins: Dyadic RIDs → v6.4.23; 11 Genesis imports → v2.9; pointers → Programme v1.3, OFN v0.12, RRF v0.8.4, TDR-G v2.12.14; **held**: radial-polynomial premise (𝒫₄ = 2dᵀBG₃,d not printed at `gen-v2.9`) and the Programme v1.2 §6.3 wording; other point-of-use Genesis pins labelled historical | M01–M28 | header companion line; §6.1, §6.15, §6.17 point-of-use brackets; §7.1; §7.2 |
| 9 | Consumer matrix (10 rows: CN × recipient, receiver tag, **producer claim-level pin** (Triadic RID, or section when no RID is assigned, at v1.6), cited edition, queue, statement accepted, adopted use, gate); Programme CN-05 queue "not recorded" with the v1.3 pass-two fact in the notes; RRF row typed convention-only with no RID-keyed import or physical adopted use; v1.6 receipts distinguished from the v1.6.1 and v1.7 deltas (round 2, R140-F1); stale "pending" lines replaced by pointers | S03 L01 X07 X08 V01–V05 V07–V12 V14 V15 | §1, §4, §6.14, §7.3, §7.4, §8 |
| 10 | Programme v1.3 is the pass-two edition | V05 V13 | §7.4 matrix row and history paragraph |
| 11 | §2 send queue removed; consumer-interface pointer | P03 V11 | §2; §7 export protocol |
| 12 | After the tag | — | notices filed as pipe items after `triad-v1.7` |
| 13 | 46 RIDs stated with the current/historical split; "49" not reproducible; `OPEN-B/E1` | H11 W02 M06 | header change boundary; §9; §7.1 |
| 14 | `[ALG+NUM diagnostic]` unpacked; `[NUM historical]` canonicalized; unused alias dropped; Methodology v1.4 line. The two `[DEF/ALG]` occurrences (§6.15, §7.2) quote the Genesis grade, which `gen-v2.9` still prints (L393); kept as quotations (Methodology v1.4 §8.4) | A01 A02 R03 B01 | aliases; §8; Appendix B |
| 15 | Release labels removed from the seven live qualifiers | C01 C02 V06 (V05 relabels the history paragraph) | §6.1, §6.15, §6.17.2, §7.2, §7.4 |
| 21 (content) | Current classification of the eleven v1.5 negative records: valid current negatives versus records whose reason is withdrawn | B02 | Appendix B, after the v1.5 list |
| 24 | v1.6.1 records placed byte-unchanged under `records/triad/` (separate commit) and cited there | H09 | header adoption records |
| 25 | Repository paths of the two recovered scripts; the T-6l rerun cited (no regrade) | R01 R02 | §8 |
| custody §0(a) | Evidence package stated as held by the PI, not in the repository; recovery list created | H10 | header; `records/triad/TRIAD_SOURCE_RECOVERY_LIST.md` |
| 19 (headings) | Eleven section headings with slash or compound grades rewritten as one primary status plus a prose suffix ("— mixed content", "— PARTIAL module"); anchors unchanged. The qualifier-syntax part of row 19 is **not applied**: Methodology v1.4 §3.2 puts qualifiers in plain brackets, but `tools/check_compaction.py` tracks only backticked qualifiers and the companion DSNs use both forms (Dyadic and Genesis mostly backticks, OFN mostly plain). Converting 67 qualifiers is a corpus-level choice for the Atlas/Methodology owner, not a Triadic edit | G01–G11 (round 3) | §6 headings |
| 18 (part), 23 | §7.4 "v1.6.1 consumer receipt (history …)" paragraph dropped (superseded by the matrix; text in `triad-v1.6.1` §7.4); repository locator `rtg-corpus` | V16 R04 (round 3) | §7.4; §9 |
| header truth | Title, date, DRAFT status, supersedes, base, co-owners, change boundary, §9 edition line and footer made true for a v1.7 draft; their v1.4 layout is stage 2 (row 17) | H01–H08 H11 W01 F01 | header; §9; footer |

Rows 16–18, 20, 22 and the movement part of row 21 are stage 2; rows 18, 19 and 23 are split as above. Row 29 is DEFER: PR #113 is still open (checked 30 Oct 2026).

## Not done in stage 1, and why

- **No Appendix A entry.** The compact v1.7 entry is written with the stage-2 layout and the release record. Gate K6 keeps Appendix A byte-identical in stage 1.
- **Narrative release labels in prose** (for example "accepted r4.2", "v1.6.1 r2 repin" outside the qualifiers and outside the repinned brackets) are row 18 material, moved in stage 2 with a movement map.
- **Status summary, Scope and heading grades** are rows 17 and 19 (stage 2).
- **Queries to the Genesis owner** found by the row-8 re-read: (i) the identity 𝒫₄ = 2dᵀBG₃,d used with Genesis's radial polynomial is not printed at `gen-v2.9` (only the c-mode analogue ΔQ_c^(4) = 2cᵀBG₃,c); (ii) the birth-symmetry theorem is stated as `[THM]` in Genesis §6.6 (L987) but as `[ALG]` in the Genesis §1 summary (L80) and its §8 artifact row `GEN-ART-JQ-PHASEDRIFT` (L1246). Both are proposed as pipe items to `pipes/GEN/` after co-owner review; neither changes a Triadic grade (the import keeps its stated grade and pin).

## Evidence boundary

- `EV-SRC-READ`: the governing tags of the companion studies were re-read on 30 October 2026 for every repinned import and every matrix cell. The per-item line numbers are in the reading notes `evidence/triad/v1.7/row8_repin_reading_notes.md` and `evidence/triad/v1.7/row9_consumer_reading_notes.md`. These notes were prepared in this session by read-only helper passes; the preparer spot-checked the two held items, the Dyadic RID locations, four Genesis values and nine matrix cells against the tags. Every line can be re-derived with `git show <tag>:dsn/<FILE>.md | grep -n`.
- `EV-RUN` (preparer): the stage-1 checker and its gate S1, which reruns the two row-1–3 evidence scripts. No owner certificate, producer campaign or trajectory is rerun; the H₁, H₂ producer bytes remain missing.
- Nothing here is adoption, a merge or a tag.

## Merge chain (R140-F2)

PR #139 cites the ChatGPT disposition of PR #137, so #137 is part of the chain. The reconciliation branch (#139) now contains #137 (merge commit `1e064d6`), and this branch contains both. Merge order for the PI: **#137 and #138 (either order) → #139 → #140.** A merge is not adoption.
