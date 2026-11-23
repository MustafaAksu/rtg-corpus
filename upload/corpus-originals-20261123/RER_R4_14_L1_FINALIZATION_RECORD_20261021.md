# RER v0.2 DRAFT r4.14 — L1 finalization record (21 Oct 2026, preparer)

**Role.** PREPARER_ROLE. Implements the five L1 items of the receiving co-owner's batch review of 21 Oct 2026 (`inputs/BATCH_RECEIVING_REVIEW_20261021.md`, SHA-256 `bd80f89d…`; `inputs/L1_FINALIZATION_DELTA_20261021.json`, items BATCH-L1-01…05) **on the same r4.14 target** with the distinct revision identity **r4.14-L1**. No r4.15. The submitted candidate is kept unchanged as history. Nothing scientific changes.

| Object | Identity |
|---|---|
| r4.13 base | `e92991bd90d24599248410a20845a14588f4ae75e6582681aaa300de370f368c` |
| r4.14 candidate (submitted; history) | `92f983e64bd54e208898954c45c4ac6482928b794d08b3d1660f0db9d00ff044` |
| **r4.14-L1** (`RTG_RELATIONAL_EMERGENCE_REGISTRY_v0_2_DRAFT_r4_14_L1.md`) | `032f2211229ab55d6f5f2477f19b75bb29c55a32d7574682be514b18ae0070d3` |
| edit list `r4_14_to_r4_14_L1_edits.json` (8 exact-once edits) | `840be5f8744a1fab2d64b4dd250921d0c9bfd1e682d73fa65eb748bf71c38858` |

## Items

| Item | Where | Change |
|---|---|---|
| BATCH-L1-01 title/date | line 1, line 4 | title "DRAFT r4.13" → "DRAFT r4.14"; date list gains "r4.14 — L1 finalization of the r4.14 candidate; r4.14" (r4.13 history kept) |
| BATCH-L1-02 aggregate count | status line, §8 P0 (r4.14) row, §9 R4.14 entry | "10 lines" → "12 lines: 10 in the gap entries, 2 record imports" / "12 current RRF v0.8.4 references (10 gap references + 2 record imports)" / "12 lines — 10 gap references and 2 record imports"; no reference line added or removed to fit the prose |
| BATCH-L1-03 table attribution | batch package `dispositions/` (not the RER text) | FORMAL-INVOLUTION row no longer carries "(d) conditional" — it is on BIRTH-GRAPH-INVOLUTION; FORMAL-AGE row: the r2 contributor review is preparer-authored and distinct from the FORMAL structural note, no author identity newly authenticated; decision column relabelled "summary", not a quotation |
| BATCH-L1-04 K3 packet typing | batch package `k3_econjugacy/` | E₀: R² → R³ (3×2), P₀ (2×3), Ē = E₀⊗I₂: R⁴ → C_raw, P̄ = P₀⊗I₂, E_W = (I₃⊗L)Ē: R⁴ → C_W; identities P̄Ē = I₄, ĒP̄ = Π_C; no formula change in the RER record |
| BATCH-L1-05 receipt integration | RER-GEN-K3-MODAL Review receipt (append-only); status line; §8 row ("DONE"); §9 entry (one sentence); batch table 18 + 2; Phase A regenerated once with the receiver sidecar attached | the receiver's decisions are recorded as receipts; the submitted candidate, the r21 image and their pending/proposed fields are kept as history; no adoption inferred |

## What does not change

All 20 records' grades, exactness, tasks, adoption text, contract tables, claim lines, OPEN items, imports and pins; the 4 gap entries and their 23 Reference lines (13 historical + 10 current); the source table; the legacy entries; line-initial tag counts. The only record-level change is the append-only Review receipt of RER-GEN-K3-MODAL (receipt integration), checked by gate D2.

## Focused L1 identity check (`check_r4_14_L1_draft.py`)

8/8 gates: M1–M3 (candidate hash, deterministic rebuild, reversibility), **M4 chain** (r4.13 + the 17 r4.14 edits = the candidate), **D1** allowed diff only (title, date, status, K3-MODAL receipt, §8 row, §9 entry — line-for-line replacements, same line count), **D2** parser identity except the append-only receipt, **D3** identity/count wording (no stale "10" aggregate), **D4** tag counts unchanged and the receiver review hash in the text equals the pinned file. 7 controls (scientific line edited, Reference line dropped, receipt rewritten, title left r4.13, count left at 10, review hash altered, stray §7 edit) each fail their gate. Output `check_r4_14_L1_output.txt`.

```
python -I -B build_r4_14_L1_draft.py          # 032f2211…70d3
python -I -B check_r4_14_L1_draft.py --controls
```

## Package

`RER_r4_14_L1/` = the submitted `RER_r4_14` package (unchanged files, incl. the candidate and its build/check) + the L1 files (`make_/build_/check_r4_14_L1_*.py`, edit list, L1 text, `r4_14_to_r4_14_L1_DRAFT.diff`, `check_r4_14_L1_output.txt`, this record) + `inputs/` receiver batch files (review, decision, reference dispositions, coverage, K3 proof, L1 delta). The manifest excludes only its own root path.

**Status after this step.** RER r4.14-L1 is the publication/adoption **object candidate**: scientific/source delta ACCEPT SCOPED (receiver), L1 finalization applied, Phase A regenerated once (r21-L1). Adoption, freeze or publication are not performed here; the PI's adoption-scope decision is separate (receiver §6 proposed scope: 18 scoped reviewed payloads + 2 blocked records outside acceptance + enumerated OPENs and source limits).
