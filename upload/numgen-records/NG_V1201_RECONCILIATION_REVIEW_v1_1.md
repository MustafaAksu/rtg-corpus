# v1.20.1 Manual Reconciliation Review — 24 Pairs

**Memo ID:** `NG_V1201_RECONCILIATION_REVIEW_v1_1` · supersedes `_v1` · **Date:** 2026-09-25 · **Auditor:** Claude
**Base:** frozen v1.20 (`f5ed40f5…3b636`) · **Scope (per ruling):** manual classification only. **No text moved.** Structural rewrite **HOLD**.
**Artifacts:** `NG_V1201_RECONCILIATION_REVIEW_v1_1.json` (per-pair decisions), `ng_state_fingerprint_v2_1.py`

---

## 1. Result in one line

All 9 HIGH and 15 AMBIGUOUS pairs reviewed by reading both blocks in full. **One STOP; no additional STOP was found in the 24-pair manual review.** `[COR v1.1]` v1 said "no other status, scope, or content drift" — too broad: the 37 NONE §6 blocks and the 119 §2 theorem blocks have not been inventoried, so no claim about them is made. STOP-01 is now **resolved in v1.20.1**.

| classification | count | meaning |
|---|---|---|
| SUMMARY-OF-MANY | 13 | the §6 block is a summary over several §2 bodies; not a 1:1 mirror |
| S6-ONLY/FALSE-POSITIVE PAIR | 3 | the automatic pair was a false positive and the §6 block has no confirmed §2 twin in that pair (P01–P03) |
| RELATED/NOT-TWIN | 1 | a real, related §2 guard exists, but it is not a twin (P07: the `Q_true`-witness ownership guard vs the SG-NG-20 guards) |
| PARTIAL-OVERLAP | 2 | shared content, but the §2 side carries something the §6 side lacks |
| MIRROR-CONSISTENT | 2 | genuine 1:1 twins, identical in status and content |
| RELATED-CONSISTENT | 2 | adjacent claims, consistent, not twins |
| **STOP** | **1** | live content drift |

## 2. STOP-01 — a residual stale claim that v1.20 missed

§6 **L2461**, live text: *"T1–T7 discharge the operator half of `RTG-OFN-OPEN-HOLONOMY-RANK-DIAGNOSTIC`; the OFN-side DSN synchronization is a separate governance edit (decision D15)."*

v1.20's S8 declared **D15 SYNC COMPLETE** (§9.1 L2631; changelog L2778). This sentence still presents it as an outstanding separate edit. It survived because the v1.20 acceptance grep searched for `pending (D15)`, and this sentence never uses the word "pending". It has no §2 twin.

Per rule 2 this is out of scope for the migration: it must be corrected in a **v1.20.x scientific/sync patch** before the structural rewrite begins, so the migration starts from a consistent base. The migration may not repair it.

## 3. What the review changes about the migration

**§6 is mostly a summary layer, not a mirror.** Only 2 of 24 pairs are genuine 1:1 twins. Thirteen are §6 summaries sitting over several §2 bodies (N-3D, C1–C4, N5-PHYS-1, DISC-1, DISC-2, P2, C7C-WD/C7C-0, C7C-M, N-6, NG-7A, NG-8A, NG-8B, full NG-8). So the migration is overwhelmingly **"§2 bodies MOVE under their §6 summary"**, not "keep one, discard one". Almost nothing is discarded.

**PARTIAL-OVERLAP is where a naive rule would have lost content.** §2 L998 shares the ORD-2 reflection/P3 content with §6 L2351 and L2377, but it *also* carries a distinct guard — *primitive-step / cross-residue monotonicity is false in general* — that neither §6 block states. A "retain §6, discard the §2 twin" rule would have silently dropped that guard. INV-1 would have caught it after the fact; the review catches it before any patch is written.

**The auto-pairer was wrong in both directions.**
- *False positives:* P01–P03 — and STOP-01 — had no real §2 twin; P07 has a related but non-twin §2 guard. The dominant cause is the §2 queue line L154, which mentions nearly every RID and so matches everything.
- *False negatives:* of 10 NONE blocks spot-checked, 9 genuinely have no twin, but **§6 L2385 (N-3A)** does have a §2 counterpart section. The keyword heuristic undercounts.

So neither the HIGH label nor the NONE label can be trusted without inspection. That confirms the ruling: the **119-block reverse relocation inventory is required**, and it is the containment that catches what forward pairing misses.

## 4. Two non-STOP notes

- **P08 N-3D** carries `[from: MATH/ALG]` on *both* sides. Consistent, so no STOP; but it is a combined grade and a TAG-NORM candidate under Methodology v1.3, recorded as G3 debt.
- **§6 L2377** says "the N-1 tube is existential and may be shrunk". v1.20 does not contradict this — the explicit-tube corollary *adds* a named tube rather than negating the existential one. Not a STOP; an optional clarity note for a later pass.

## 5. Parser cleanup (v2.1)

The literal `RID` from `[import: … | RID unavailable]` placeholders no longer enters the explicit set: the import regex now requires a hyphenated identifier and the literal is filtered. Explicit RIDs: 39 → **38** (the phantom removed). Block count and broad set unchanged.

## 5a. STOP-01 resolution
Resolved in `RTG_NUMBER_GENESIS_DSN_v1.20.1`. A broader live-text scan found no other stale D15 sentence. A fingerprint diff v1.20 → v1.20.1 shows exactly **1** baseline block changed (the STOP-01 sentence) and exactly **2** new blocks (its replacement and the v1.20.1 changelog `[COR]` entry); explicit RID set identical; broad identifier set gained only `STOP-01`. The patch is confined.

## 5b. Bare-status count, reconciled
Two counts are both correct under different definitions: **12** bare `**Status:**` lines lack a *canonical* bracketed status (`[RESULT]`/`[OPEN]`/`[DEF]`/`[CLOSED]`/`[HOLD]`); **9** are not anchored by the fingerprint's block regex, because three of the twelve carry an `[ALG]` in backticks that the regex does anchor. INV-S must cover **all 29** `Status:` lines regardless.

## 6. Gating for the rewrite, restated

Structural rewrite stays **HOLD** until all of the following exist:

1. ~~STOP-01 resolved~~ — **done in v1.20.1**; STOP list empty.
2. **119-block reverse relocation inventory**: each §2 theorem block is exactly one of `MIRROR-RECONCILED`, `MOVE`, `REGISTRY-ONLY`, or `STOP`.
3. **INV-S — registry/status conservation**: all **29** `Status:` lines, anchored or not (9 are invisible to the block fingerprint), with living states ACTIVE/PARTIAL/OPEN/HOLD/BLOCKED/SPLIT unable to change silently.
4. **INV-P — pointer-integrity checker**, working.
