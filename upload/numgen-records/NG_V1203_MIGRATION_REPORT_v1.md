# v1.20.3 Structural Migration (Option B) — Candidate Report

**Report ID:** `NG_V1203_MIGRATION_REPORT_v1` · **Date:** 2026-09-25 · **Auditor:** Claude
**Base:** frozen v1.20.2 (`35fe1a65…dd1053`) · **Rulings:** v1.20.3 GO; option B (module-level).
**Status:** **CANDIDATE, metadata-finalized.** Co-owner ruling 2026-09-25: scientific migration APPROVED; NG-9/N-4/N-6 placement APPROVED; L1 cap APPROVED as a documented rendering exception; canonical freeze HOLD pending the metadata-finalization patch recorded in §8. v1.20.2 remains the frozen owner until freeze.

## 1. Result
All **11** batches clean, final composite gate **all PASS**:

| gate | result |
|---|---|
| FP-v2.3 INV-0 no open STOP | PASS |
| INV-1 no loss / INV-1b twin present | PASS (0 lost) |
| INV-2 no invention | PASS (0) |
| INV-3 no theorem blocks in §2 | PASS (0; queue exempted by name) |
| INV-4a/4b identifier conservation | PASS |
| INV-S final — all 29 statuses at correct location | PASS (0 errors) |
| INV-P post-write — 114 MOVE placed, mirror removed, twin kept, §6.9a present | PASS |
| INV-LIVE | PASS (0 live hits) |
| §2 queue and §8 byte-identical to v1.20.2 | PASS |

§2: **1973 → 59 lines** (heading, unchanged queue, module registry). §6: 246 → 2186 lines. Theorem-grade blocks left in §2 per batch: 85 → 79 → 76 → 58 → 12 → 3 → 1 → **0** (reached at §6.9a).

## 2. The point of option B — verified
- **`D_chain` [DEF] is now 2 lines before M-1B**, both in §6.6.
- **NG-7 set-up (`R_ij`, `a_ij = log R_ij`, node potentials) sits with NG-7A** in §6.8.

## 3. Method
**Hierarchical inventory v1** (`NG_V1203_HIER_INVENTORY_v1.json`): 19 level-3 §2 modules; 18 relocate, the queue stays. **Module destinations agree with all 115 approved per-block destinations: 0 mismatches** — option B changes no approved disposition.

**Engine** (`ng_migration_engine_v1.py`): builds the document from inventories. **Self-test: K=0 reproduces v1.20.2 byte-for-byte.** Modules appended after existing §6 content (summary first, then bodies), original order, headings demoted one level (one level-6 heading capped).

**Approved dispositions applied unchanged:** 114 MOVE; 4 REGISTRY-ONLY (queue in place; 3 bare statuses verbatim onto `<!-- REGISTRY -->` rows, each under a sub-module label); 1 MIRROR-RECONCILED (§2 ORD-4 removed, §6.3a twin kept).

## 4. Two tooling findings during execution — both surfaced by the gate
**(a) Registry conversions and the in-place queue** were unrepresentable in `compare`: converted statuses read as "lost", the `[ALG]`-tagged queue as a theorem left in §2. **v2.2** adds two explicit ledger keys; self-test: INV-3 count 119 → 118, the queue only.

**(b) HEADING-DEMOTION.** Batch 5 failed INV-1/INV-2 on one block. Cause: the N-5A-S1 heading carries `[COR: v1.7 verdict]`, so the heading line *is* a claim-block anchor, and demoting it changes the block hash. Exactly **one** such block exists in the document. **v2.3** adds a `heading_demotion` class whose entries are **derived, not observed**: base block, first line's `#` count increased, re-hashed with the fingerprint's own normalization — admitted **only if** that hash is an actual block of the new file. Any real content change breaks the equality and surfaces as INV-2. All batches then PASS.

## 5. Decisions recorded for your review
1. **NG-9 → §6.10 External benefit boundary** — **APPROVED** by the co-owner (§6.10 already bounds external mathematics/physics consequences).
2. **N-4 → §6.5, N-6 → §6.7** — **APPROVED**; OPEN bodies collected under their existing target headings, not new scientific assignments.
3. **`###### L1` capped at level 6** — **APPROVED as a rendering exception.** The H6 cap on L1 is a Markdown rendering exception only; semantic parentage remains N-1C-DYAD → L1 (depth-cap only; no semantic re-parenting). Blocks unaffected.

## 6. Self-caught during this pass
The engine's changelog first said relocated `§2 …` pointers were "listed in the migration report". The scan found **none**, so the sentence implied a list that does not exist; corrected to state none were found, then all gates re-run.

## 7. Artifacts
Candidate owner, diff, fingerprint (generator **v2.3**), migration ledger, hierarchical inventory, engine, batch runner, fingerprint v2.2/v2.3. Hashes in the reply.

## 8. Metadata-finalization patch (pre-freeze, same version v1.20.3)
Per the co-owner ruling, four release-metadata corrections; **no scientific state and no relocated body touched**, applied in the engine so the candidate stays reproducible:
1. Header line 6 no longer says the structural migration is "deferred"; it now reads: *§2/§6 structural migration completed in this methodology-only release; scientific state unchanged from v1.20.2.*
2. Changelog gate name `FP-v2.2` → **`FP-v2.3`** (the migration uses v2.3's derived HEADING-DEMOTION).
3. Changelog `NG-9 -> §6.10 proposed and reviewable` → *co-owner approved structural mappings N-4 → §6.5, N-6 → §6.7, NG-9 → §6.10*.
4. The L1 cap is described in the changelog, this report, and the hierarchical inventory as a Markdown rendering exception with semantic parent N-1C-DYAD unchanged — confirmed against v1.20.2, where `##### N-1C-DYAD` directly parents `###### L1`.
All four composite gates re-run after the patch (see reply).
