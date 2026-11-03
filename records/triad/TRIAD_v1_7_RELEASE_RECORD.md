# Triadic Birth-Lift v1.7 — Release Record

**Status:** ADOPTED by the PI on 3 November 2026 (§1). The published file `506f3403…e64a` equals the accepted candidate `2573961a…5c0d` plus the adoption-state lines only (§8). The edition governs once the PI has merged PR #140 and created the tag `triad-v1.7`; until then `triad-v1.6.1` is the tagged edition.
**Date:** 3 November 2026.
**Prepared by:** Claude, Triadic co-owner (builder), on branch `claude/triad-v1-7-stage1`.
**Edition:** v1.7, one successor built in two stages under DSN Methodology v1.4. Stage 1 carries the content, scope and form edits; stage 2 is layout only, checked by `tools/check_compaction.py` against the stage-1 hash.
**Predecessor:** `RTG_TRIADIC_BIRTH_LIFT_DSN_v1.6.1`, tag `triad-v1.6.1`, SHA-256 `95340abe57e999ed48681502152113d8fdb3102f74f45a25aa66c2d0092d451f`.

Fields marked *(to be filled)* depend on steps that have not happened yet. This record invents no hash, approval or review identifier. Every hash below was computed on the branch files.

## 1. Authorization and reviews

| Step | Source | State |
|---|---|---|
| Advisories | `records/triad/ATLAS_ADVISORY_TRIAD_v1_6_1.md` (pass 1), `…_INDEPENDENT_CHATGPT.md` (pass 2), `…_RECONCILIATION.md` (§4: the 29-row list) | on `main` (#131, #133) |
| Custody entry | `records/triad/TRIAD_UPLOAD_HASH_CHECK_20261030.md`, `records/triad/TRIAD_COOWNER_ENTRY_NOTE_20261030.md` | on `main` (#136) |
| Co-owner dispositions | Claude: `records/triad/TRIAD_COOWNER_DISPOSITIONS_CLAUDE_20261030.md` (PR #138, `f35f52e6…87e8`). ChatGPT: `records/triad/TRIAD_OWNER_DISPOSITION_ADVISORY_v1_6_1_chatgpt_20261030.md` (PR #137, `5fffb199…cbd`) | open PRs; merge before #140 (§9) |
| Joint reconciliation | `records/triad/TRIAD_OWNER_DISPOSITION_RECONCILIATION_v1_6_1.md` (PR #139, `3c551769…021a`); ChatGPT confirmation in review `5714190994` on `5275223`: CONFIRMED / ACCEPT SCOPED, 29 rows | confirmed |
| PI start of stage 1 | "Stage 1'i hazırlayalım" (30 Oct 2026, Triadic owner session) | given |
| Change-focused review, stage 1 round 1 | PR #140 review `5738872551` on `b5f1488`: ACCEPT WITH CHANGE (R140-F1 consumer matrix); comment `6580920857` (R140-F2 merge chain) | answered in round 2 |
| Round-2 receiving review | PR #140 review `5739033005` on `f39b60f`: ACCEPT SCOPED; R140-F1 and R140-F2 CLOSED | given |
| Round 3 and stage 2 review | PR #140 review `5739393136` on `1f89cb9`: ACCEPT SCOPED; 99 stage-1 edits and 9 stage-2 operations reproduced byte-for-byte by the receiver; open format notes F-1, F-2, F-3 | given; F-3 done; F-1, F-2 open (§7) |
| Atlas row check | Request `pipes/ATLAS/20261102-TRIAD-v1-7-row-check.md`. ChatGPT: `records/atlas/ATLAS_TRIAD_v1_7_29_ROW_CHECK_CHATGPT.md` (PR #141, head `7c2c31d`, `b070418b…d943`), PASS SCOPED / no Atlas-row blocker. Atlas owner: `records/atlas/ATLAS_TRIAD_v1_7_29_ROW_CHECK_OWNER.md` (PR #143, head `40c8440`, `32782fb4…f2b3`), PASS SCOPED; reran both stages and the row-1–3 scripts; concurs on all 29 rows; notes A-1 to A-4 | given |
| **Adoption** | PI, Triadic owner session, 3 November 2026, 08:01 +03:00: "Triadic kayıtlarını bu haliyle benimdiyorum." (quoted as written), on candidate `2573961a…5c0d` as presented with the co-owner and Atlas acceptances. "Bu haliyle" (as is) is read as: F-1 and F-2 stay open (§7) | **adopted** |
| Publication finalization | `evidence/triad/scripts/release_triad_v1_7.py`, adoption-state lines only; gates P1–P6 PASS, controls X1–X6 caught | done; published SHA-256 `506f3403628ca01d5a904f885df055d9bfbdf1ef5e474e24e83d4797c122e64a` |
| Merges and tag `triad-v1.7` | PI (§9) | *(to be filled)* |

## 2. Identities

| Object | Path | SHA-256 |
|---|---|---|
| Base (adopted v1.6.1) | `git show triad-v1.6.1:dsn/RTG_TRIADIC_BIRTH_LIFT_DSN.md` | `95340abe57e999ed48681502152113d8fdb3102f74f45a25aa66c2d0092d451f` |
| Stage-1 intermediate, round 1 (superseded; in Git history) | `dsn/RTG_TRIADIC_BIRTH_LIFT_DSN.md` at `b5f1488` | `19af7ee3b87ef8ff228c76c90632b9cf1ee15f2d09995d82cf9a30019ef46163` |
| Stage-1 intermediate, round 2 (superseded; in Git history) | same path at `f39b60f` | `a89c5768aeecf7c3e32667a04ab7aa2290f2a8830c22560bf5f66e791fdd1a62` |
| **Stage-1 intermediate, round 3 (frozen; the stage-2 base)** | `evidence/triad/v1.7/stage1_intermediate.md` | `b47d294d9dc82b78f05e02c99e04100177c78480c453438d5d4fca86e14ba66a` |
| Stage-1 builder (99 edits) | `evidence/triad/scripts/build_triad_v1_7_stage1.py` | `ae4d9cd5836a7bf99e4a8671c64097dc7d4ad19441f119235104e5aea0b9014f` |
| Stage-1 checker | `evidence/triad/scripts/check_triad_v1_7_stage1.py` | `077d5d85b917a25eb9ad5903d61b0b0712df8ebd637cf2038b6c9569ec6b14cb` |
| Stage-1 edit log | `evidence/triad/v1.7/stage1_edit_log.json` | `e0db55a4c98e26fd862b92cc794247310d666acf05530997162eb889f0b1a7c6` |
| Stage-1 check output (gates ALL PASS; 16 controls caught) | `evidence/triad/v1.7/stage1_check_output.txt` | `2ef68086c6c714bd80349f0c03273f2c28384fe060a6d0b0b3e2467ec495c844` |
| Row 1–3 evidence | `evidence/triad/scripts/triad_coowner_row1_row3_check.py`; `evidence/triad/scripts/triad_reconciliation_row1_extension_check.py` (outputs in `evidence/triad/v1.7/`) | `ab3482b7…cea5`; `b6c02ae5…589f` |
| Stage-2 builder (9 operations) | `evidence/triad/scripts/build_triad_v1_7_stage2.py` | `53e43e3aec9d0bdc57fa636179a1eeb0ad9166740ef5b1aefad6815574c90ece` |
| Stage-2 owner guards and fixtures | `evidence/triad/scripts/check_triad_v1_7_stage2.py` | `4f902688226df8455e9b31bd323587507735e1b6858a0d7bfdab575353e5c411` |
| Movement map | `evidence/triad/v1.7/movement_map.json` | `44e0e6b6cf03afc5e589b7d467cb20625a0c7ad5f7d0f6e5f1d67971c9595ebb` |
| `tools/check_compaction.py` output and report (PASS) | `evidence/triad/v1.7/check_compaction_output.txt`, `…/check_compaction_report.json` | `3e41317c…3b83`, `1d3c21bc…c909` |
| Stage-2 guard and fixture output (G0–G9 PASS; 11 fixtures caught) | `evidence/triad/v1.7/stage2_check_output.txt` | `b8d21ca93afe26dec3b01b46f7fbba07b7509897057035cbd55c181e3d549103` |
| **Stage-2 candidate (accepted and adopted object)** | builder output; `dsn/RTG_TRIADIC_BIRTH_LIFT_DSN.md` at `27ddc2f` | `2573961a82ce10a348f76f10feece6fefb3831f3c4dd60de5dcae78acb745c0d` |
| Publication transform and checker | `evidence/triad/scripts/release_triad_v1_7.py` | `d56e139253cb5d4ca837add9e19d067564e09c8386bfdb47d8cbca207a9db9d9` |
| Publication check output (P1–P6, X1–X6) | `evidence/triad/v1.7/release_check_output.txt` | `ce91be13b05e0d9fddc37b90b58cee5f07e1e2e95bad79de3aef47f2818d3e4b` |
| **Published v1.7 (adopted; final)** | `dsn/RTG_TRIADIC_BIRTH_LIFT_DSN.md` | `506f3403628ca01d5a904f885df055d9bfbdf1ef5e474e24e83d4797c122e64a` |

## 3. Content (stage 1)

Row-by-row edits, with edit identifiers: `records/triad/TRIAD_v1_7_STAGE1_IMPLEMENTATION_MATRIX.md`. In summary:
- **Row 1.** The §6.18 off-root extension is not unique. $f_s$ and $f_c$ are stated for both root-equivalent extensions. $D=\mathcal G/Q_s$ is a first integral in the $Q_c$-free extension and satisfies $\dot D=r\,q_1D$ in the literal one. It is recorded as an ODE-scope remark with no RID.
- **Row 2.** `TRIAD-ALG-T6E-ORIENTATION-NORMALIZATION` is typed as a first-variation identity, with the bookkeeping weights and the clock.
- **Row 3.** A coercive bound is added inside `TRIAD-ALG-T6L-NORMALIZED-TORSION-SIGN`.
- **Rows 4–5.** T-6r gets the acceptance contract C1–C6; T-6q gets a coordinate sign table.
- **Row 7.** 96:1 is stated once, with the metric caveat.
- **Row 8.** Claim-level repins, with two held pins.
- **Rows 9–11.** A per-recipient consumer matrix with producer pins; stale queue and receipts removed.
- **Rows 13–15.** The 46 RIDs are stated; compound tags and release labels removed.
- **Row 19 (headings).** Heading grades normalized.
- **Row 21 (classification).** The v1.5 negative records are classified.
- **Custody.** Evidence package held by the PI; recovery list added.

No live claim's grade changed. No RID was added, removed or renamed (46 before and after). No OPEN status line changed.

The edits were applied in three rounds: round 1 on `b5f1488`; round 2 on `f39b60f` (R140-F1); round 3 on `ce98e23`. Round 3 carries the items the compaction checker cannot express as layout: heading grades (row 19), the §7.4 history paragraph (row 18) and the repository locator (row 23).

## 4. Stage 2 (layout only)

There are 9 declared operations, against the round-3 intermediate. They cover rows 17, 18, 20 and 22, and S2-E03 removes an obsolete process note. Details are in the "Stage 2" section of the implementation matrix and in `movement_map.json`.

`tools/check_compaction.py` returns PASS:
- 256 claim blocks: 241 byte-identical, 15 changed by declared operations, 0 unexplained.
- RIDs, anchors, source hashes and qualifiers preserved.

The generic harness `tools/test_check_compaction.py` reports 11 of its 16 controls as NOT APPLICABLE, because it is written against Dyadic patterns. The study fixtures replace it, as in OFN v0.11. Its output is kept in `tool_harness_generic_output.txt`.

## 5. Custody (rows 24–28)

- `records/triad/OWNER_ADOPTION_v1_6_1.json` (`33bcd3ce…37cd5dd`) and `records/triad/RELEASE_RECORD_v1_6_1.md` (`aa3d8d77…7eb45d`) are placed byte-unchanged from `upload/triad-records` (`2a1a4a8`).
- The v1.6 evidence package `evidence/accepted_r4_2/`, the nine other v1.6.1 package files and the v1.6 records are held by the PI and are not in the repository. They are listed in `records/triad/TRIAD_SOURCE_RECOVERY_LIST.md`, which uses five states.
- Nothing was reconstructed.
- The T-3a scaffold is classified as a scaffold, not a certificate.
- The T-6e producer bytes that carry $H_1,H_2$ remain missing.

## 6. Inbox, and what would be notified after the tag (row 12)

- **Inbox.** `pipes/TRIAD/20261030-OFN-v0-12-adopted.md` is dispositioned "no action" (reconciliation §5). The OFN result enters T-6r C1 as an interface constraint, not as an import.
- **Atlas request.** `pipes/ATLAS/20261102-TRIAD-v1-7-row-check.md` has been answered by #141 and #143. Its state is set by the Atlas after the merge (A-3).
- **After `triad-v1.7`**, one claim-specific pipe item per receiver:
  - **GEN.** The v1.6 pin and the `[CAND]` import of T-6s/t/u. Two queries from the row-8 re-read: the 𝒫₄ = 2dᵀBG₃,d identity is not printed at `gen-v2.9`, and birth symmetry is graded `[THM]` in §6.6 but `[ALG]` in §1 and §8.
  - **UVM (OPEN-M).** The v1.6 pin, and the v1.6.1 and v1.7 deltas.
  - **PROG.** No CN-05 disposition is recorded in v1.3.
  - **OFN.** Reference rows at v1.6.1; the v1.7 delta.
  - **RRF.** The §3.1 convention-only entry and the v1.6 pin.
- Filing a notice is a queue event, not acceptance.

## 7. Open notes carried past this release

None of these is a scientific defect. v1.7 does not claim full Methodology v1.4 form compliance.
- **F-1, qualifier syntax.** Methodology v1.4 §3.2 puts qualifiers in plain brackets; 67 backticked qualifiers remain. This is a corpus-level conversion and should go together with a checker change.
- **F-2, status summary.** It has six sentences; the target is 2–4.
- **A-1.** The §2 T-6u record keeps v1.6-era wording ("Exact-candidate review and owner publication are complete", "registered by this owner release"). It can be misread in a v1.7 file and goes with F-1 and F-2 to the next edition.
- **A-4.** The next Atlas edition refreshes the Triadic rows after the tag.
- **Row 29.** DEFER: PR #113 is open.
- **The v1.6 phrase "all 49 RIDs"** (Appendix A of `triad-v1.6.1`) cannot be reproduced from the repository, because the v1.5 and v1.6 files are not in it. v1.7 states the 46 RIDs it declares.

## 8. Publication transform

`release_triad_v1_7.py` changes exactly seven lines of the candidate:
- the header Date, Document status, Supersedes (", on adoption" dropped) and Records ("(written at adoption)" dropped) lines;
- the §9 edition line;
- the Appendix A v1.7 heading;
- the footer.

Gate results:
- P2: the output equals the transform.
- P3: exactly the 7 declared lines differ.
- P4: the reverse transform recovers the candidate byte-exactly.
- P5: no draft or adoption-pending marker is left.
- P6: every other line is byte-identical, and the claim-tag, RID and math census is unchanged.
- Controls X1–X6 are caught.

The release record keeps both identities (A-2): reviewed candidate `2573961a…5c0d`, published file `506f3403…e64a`.

## 9. For the PI — merges and tag

1. **Merge, with merge commits (not squash), in this order:**
   - #137 and #138, in either order;
   - #139;
   - #140, which carries this record, the published file and the pipe items;
   - then the Atlas records #141 and #143.

   #139 already contains #137, and #140 contains #137–#139, so later merges show only their own files.
2. **Check the file on `main`.** `dsn/RTG_TRIADIC_BIRTH_LIFT_DSN.md` must have SHA-256 `506f3403628ca01d5a904f885df055d9bfbdf1ef5e474e24e83d4797c122e64a`.
3. **Tag.** Create the annotated tag on the #140 merge commit, then push it:
   `git tag -a triad-v1.7 <merge-commit> -m "Triadic v1.7 — dsn/RTG_TRIADIC_BIRTH_LIFT_DSN.md SHA-256 506f3403628ca01d5a904f885df055d9bfbdf1ef5e474e24e83d4797c122e64a"`
   then `git push origin triad-v1.7`
4. **Afterwards.** Update `BASELINE.md` (TRIAD row → v1.7, `triad-v1.7`), file the §6 notices, and run "Sync now" in the Claude project.

Merge and tag identities: *(to be filled after the PI's steps)*.

## 10. Not claimed

- No physical $K<1$ carrier, birth or source law, basin, safe wedge, finite-amplitude torsion sign or physical 96:1 correspondence.
- $D$ is not a conserved physical mode.
- The Gram relation is not an exact discrete law.
- No owner certificate, producer campaign or trajectory was rerun beyond the stated scripts. The $H_1,H_2$ producer bytes are unavailable.
- Consumer acceptance of any v1.6.1 or v1.7 delta is not implied.
