# Note to the Discrete Genesis co-owners — current state, the advisory, and what is asked of you

**Date:** 27 October 2026. **From:** the atlas owner (Claude), with the PI. **To:** the Discrete Genesis (TDRG) DSN co-owner sessions. **Status:** working note; PI decisions of 27 Oct 2026 (reconciliation §5): *staged update — v2.12.14 corrections-only first (Methodology v1.2 kept as declared), the v1.4 migration later as v2.13; the TDR-G co-owners build; no reruns inside v2.12.14 (EV-NOT-RERUN with the census bound); the held motif logs and scripts go to `upload/tdrg-records` unchanged.*

**Purpose.** TDR-G has not had an owner pass since v2.12 (June 2026; Programme v1.3 §6.4 records it). Since then the corpus moved into a git repository with tags, Methodology moved to v1.4, Programme to v1.3, OFN to v0.10, and NUMGEN v1.21 (26 Oct 2026) filed a scientific request in your inbox that blocks its C7C-M4 campaign. Two independent advisories were written against your edition and reconciled; this note brings you to the current state and hands you the merged list. The edition is yours to build.

## 1. How we work now

Full rules: `CONVENTIONS.md` (repository root) and Methodology v1.4 (`dsn/DSN_METHODOLOGY.md`). Read `CONVENTIONS.md` before any edit. In short: the repository is the source (`dsn/RTG_DISCRETE_GENESIS_DSN.md`; governing edition = latest `tdrg-v…` tag with its release record; no versioned copies); current-only live file (v1.4 §1.1; one compact Appendix A entry per edition; history at the tags); releases through a branch → change-focused review by the other co-owner and the atlas owner → release record → PI adoption → merge commit (never squash) and annotated tag by the PI; two stages when layout changes (stage 1 corrections with an assertion-gated script, exact-once edits logged with hashes, checker with negative controls, frozen intermediate hash; stage 2 layout-only compaction checked by `tools/check_compaction.py` with a movement map); evidence in `evidence/tdrg/`; every session pushes its own branch and opens a PR; never invent hashes, RIDs or approvals. **Cross-stream items** are files in `pipes/<STREAM>/` (`pipes/README.md`; validator `python3 -I tools/pipes_index.py --check`): a request, offer, finding, question or notice with no scientific authority; you read `pipes/TDRG/` at the start of your pass, before freezing stage 1 / finalising the release record, and when blocked, and you decide autonomously; you set the item's `state` and `disposition` (`YYYY-MM-DD · accept | accept with change | reject | defer | no action · <pointer>`). Nothing goes through the PI. Precedents to copy: NUMGEN v1.21 (`records/numgen/NUMGEN_v1_21_RELEASE_RECORD.md`, `evidence/numgen/scripts/`), Genesis v2.9 (`records/gen/GEN_v2_9_RELEASE_RECORD.md`).

## 2. Your edition in the repository

| Item | Value |
|---|---|
| File | `dsn/RTG_DISCRETE_GENESIS_DSN.md` |
| Governing edition | v2.12.13, tag `tdrg-v2.12.13`, SHA-256 `aa232643f6f631694b0eda1532be213e5a517ef109cd66794f8e638e24fc053f` (1,288 lines; `BASELINE.md` row TDRG) |
| Declared methodology | v1.2 (v1.4 lets a document keep its edition until migrated) |
| Records on `main` | none yet for TDR-G; the two advisories and the reconciliation arrive with PRs #82 and #84 |
| Not in the repository | the session-certified scripts and data your §8 says to "consolidate" (`TDRG-ART-KINEMATIC-CERTS`, `-SPECCONS`, `-BIND3-N24K1`, `-BIND3-SUITE`, the v16/v17 motif logs, `genesis_mode_b_mc.py` v17). If your sessions hold them, place them unchanged on an `upload/tdrg-records` branch; the atlas owner hash-checks them. `genesis_mode_b_mc_v18.py` is already on `upload/numgen-records` (SHA-256 `9d787b43…`). Nothing is reconstructed. |
| Consumers (Programme v1.3 §7.2) | OFN v0.10 (IF03; twelve "RID unavailable" imports IMP-O08-*; Finding A `RTG-OFN-ALG-STAR-TOKEN-SHIFT` offered for custody, XFER-O08-01; REQ-O09-05 open), NUMGEN v1.21 (IF13; DISC-1/DISC-2 on your v18 conventions; `*NUMGEN:imp-DISC` "RID unavailable"), AZ v0.6 Threads B/C (IF21), Genesis (IF25, blocked interface) |
| Your pins | Programme v1.1 (governing v1.3), OFN v0.6 (governing v0.10), Methodology v1.2 (governing v1.4) |
| Inbox `pipes/TDRG/` | `20261026-NUMGEN-orientation-policy-s0-e-half-n.md` (request, `blocks: NUMGEN C7C-M4`), `20261026-NUMGEN-v1-21-adopted.md` (notice) — both `state: open` |

## 3. The list you work from

`records/tdrg/ATLAS_ADVISORY_TDRG_v2_12_13_RECONCILIATION.md` §3 (merged from `ATLAS_ADVISORY_TDRG_v2_12_13.md`, TA/TB/TC, and `…_INDEPENDENT_CHATGPT.md`, TG13-I01…I12; the two passes agree everywhere). The items that need a **scientific decision** from you:

- **TA-01 / I01 (P0), with TC-14 / I03.** Your path orientation rule (§6.3 line 572) has no node-relabelling-covariant output on the stratum S=0 ∧ δ_{v_n}−δ_{v_1} ≡ N/2: `signed_centered` returns +N/2 under both listings and v18 then orients by node-ID order — the "arbitrary path label fallback" your Appendix B retires. The atlas check (`evidence/atlas/tdrg/atlas_tdrg_orientation_covariance_check.py`; exhaustive at N=24, three nodes, k∈{0..3}) gives: 1,152 degenerate (state,k) path cases; on all of them a covariant selector exists for P_3 (G = sc(δ_{v_1}−δ_c) − sc(δ_{v_3}−δ_c) is reversal-odd and never 0); the 136 ratified DISC-2 witnesses change in 10 / 20 / 12 records under reverse / inert / G, with the ten-label set unchanged and the 96 unexposed witnesses unchanged by construction; at k=1, 77 of 9,800 eventual cycles (4.9 % of states) contain a listing-dependent event under v18. **Choose** a covariant rule — (a) the G-rule for P_3 with a palindromic tie for even n, or (b) the balanced tie extended to E≡N/2 — name the covariance group (new guard SG-14), define `signed_centered`/`signed_defect_error` (TA-02), qualify the §6.12 "relabeling-covariance check" (TA-08/I02), record what the change touches (BIND3-CYCLE-N24K1 and the §6.6–6.8 policy results ran on v18: `EV-NOT-RERUN` with the census bound — the PI deferred any rerun to a later campaign), and disposition NUMGEN's request with the witness-effect table. Node identity as physical (keep v18) is not a live option in either advisory.
- **TA-05 / I04, TA-06 / I05 (P1).** Two one-sentence mathematical corrections: LEM-RETRIG at d=0 is a fixed point (least period 1), so "period divides two"; LEM-SPECCONS "equivalently" → "therefore, in particular".
- **TA-04 / I06, I07 (P1).** Headline exponent −0.869 range-tagged (480–1440 ≈ −0.730), the χ=0.836 consistency sentence retired, one grade in §1 and §5, §1/§2/§5 aligned on TDR-24 D/F closed vs analytic residuals vs A/B/C.
- **TA-03 / I11, TC-15 (P1).** Two separate dispositions: the global token shift (OFN Finding A, XFER-O08-01) and the endpoint selector (REQ-O09-05).

Everything else is bounded: claim RIDs (TB-09/I08; definitions consumed by OFN/NUMGEN first), evidence custody (TB-11), Methodology v1.4 migration and pins (TB-10/I09/I10), compound grades (TB-12), internal stale (TB-13), cross-branch residues (TA-07), AZ cross-citation and scoping (TC-16, I12), the dropped Programme owner-review tasks (TC-17).

## 4. What is asked of you, in order

1. Read `CONVENTIONS.md`, `pipes/README.md`, Methodology v1.4 §§1.1, 3.4, 4, 12, 13.6–13.9, the three records in §3, and your inbox.
2. **Disposition records**, one per co-owner session (`records/tdrg/TDRG_OWNER_DISPOSITION_ADVISORY_v2_12_13_<session>_<date>.md`): accept / accept with change / reject with reason / defer for every row of the reconciliation §3; your orientation decision (a)/(b) with its covariance group. The PI has fixed the edition (v2.12.14, corrections only), the builder (you), the rerun scope (none now) and the upload route. Where the two of you differ, say so; the atlas owner reconciles, the PI decides.
3. **Build v2.12.14** after the PI fixes the dispositions: one corrections stage on a branch from `main` (script under `evidence/tdrg/scripts/`, exact-once edits logged with hashes, checker with negative controls including the antipodal permutation fixture and a covariant-rule control, candidate hash); no layout compaction in this edition (the Methodology v1.4 migration is v2.13, later); release record `records/tdrg/TDRG_v2_12_14_RELEASE_RECORD.md` (DRAFT) with dispositions, hashes, the live-file exceptions you keep on purpose, the disposition of every `pipes/TDRG/` item, and the affected consumers (NUMGEN, OFN, AZ).
4. **Review**: the other co-owner reviews stage 1 and stage 2 change-focused; the atlas owner runs its row checks and reruns your scripts. Then PI adoption, merge commit, tag; the atlas owner verifies the tag and refreshes the atlas (D5, H4, H9, D5.X1).
5. After the tag: one `kind: notice` item per affected consumer in its inbox; close the dispositioned inbox items. NUMGEN then re-annotates its DISC witnesses under your rule and releases C7C-M4.

## 5. What is not asked

No rerun of the N-scaling scans, the NKSCAN suite or the BIND3 enumeration in this edition (PI decision; a scoped sensitivity audit is a later campaign); no change to `bound_symmetric` as canonical (SG-8) or to any policy branch; no bridge to the continuous branch (SG-10); no choice between (a) and (b) by the atlas. The advisories do not grade your claims; where they say a statement is inconsistent they quote the owner lines and leave the choice to you.

## 6. Pointers

Atlas `atlas-v0.6` (noncanonical): D5.L2 TDRG nodes, D5.L5 TDRG.G1–G9 and D5.X1, H4, H9. NUMGEN v1.21 §2 item 1 (C7C-M4 HOLD), §6.6 P2 exposure, Appendix B "implementation agreement ⟹ presentation covariance `[REJECTED]`". OFN v0.10 §4.1 Finding A, §11 REQ-O09-05. Programme v1.3 §6.4, §7.2 IF03/IF13/IF21/IF25. Questions to the atlas owner as PR comments, as a record in `records/tdrg/`, or as a `kind: question` item in `pipes/ATLAS/`.
