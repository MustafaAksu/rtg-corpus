# BIND3 Reproduction Status v3 — Provenance Corrected; Discrepancy Localized

**Memo ID:** `NG_BIND3_REPRO_STATUS_v3` · supersedes `_v2` · **Date:** 2026-09-01
**Target:** `BIND3-CYCLE-N24K1` (`RTG_DISCRETE_GENESIS_DSN v2.12/13`, §6.12)
**Artifacts:** `bind3_repro_v3.py` / `.log` (4 rows, every clause decided by its expression, exit 0)
**Status:** correct blocked-state artifact for BIND3 reproduction.
**Verdict:** published IC **cardinalities and `d`-resolved multiplicities** reproduced exactly; IC **pairing** strongly supported but not owner-verified; cycle statistics close but **not exact**. DISC-1 remains blocked.

---

## 1. `[COR]` restated correctly — v1 used the wrong IC-stage sign pairing

I over-reached in v2 by writing that "the owner's `d` is `δ_B − δ_A`". The owner defines `d_AB = δ_A − δ_B` (LEM-SPECCONS), and a swap sends `d ↦ −d`, so `ε' = ε − d` is consistent with `d` being the **pre-swap** relative advance. v3's pairing `d_AB^IC = −d` is therefore correct **if** the exported retrigger-entry state is the *post-swap* member of the dyad cycle. The DSN calls these only "post-advance BIND3 ICs" and does not document that stage conversion.

So the corrected claim is: **v1 used the wrong IC-stage sign pairing**, and the dramatic improvement under the corrected pairing is strong *evidence* for the post-swap reading — not an owner-text identity. I have not redefined the owner's `d`.

Correspondingly the v2 headline "IC families reproduced exactly" is weakened to: **published cardinalities and `d`-resolved multiplicities reproduced exactly; reconstructed pairing strongly supported but not compared against an owner seed export.** v1 is the reason this distinction is not pedantic — it showed counts can be exact while the pairing is wrong.

## 2. A3 provenance split

The expression checks all `24⁴ = 331776` reduced states under **three declared lifts** `(c,b) = (0,0), (5,7), (17,3)`, and the row now says exactly that. The all-lift statement is the memo `[ALG]` theorem and is not asserted by the certificate:

> A common shift `θ_i → θ_i + c`, `δ_i → δ_i + b` moves every advanced phase by the same `c + b`, so all `Δ_ij` and hence the defect graph are unchanged; swap and the `P₃` successor shift permute the `δ` values and carry the common `b` along. Every pairwise difference after the event is therefore identical, for every `(c,b)`.

The quotient is a derived no-birth dynamical symmetry, not the SG-2 global-phase gauge. This still does not settle which key the *published* enumeration used.

## 3. A4 Boolean widened to its own PASS string

The v2 Boolean tested median period, max period and dominant-period overlap, while its PASS string also claimed median preperiod 0 and K₃-freeness — neither tested, and `stats()` did not even count K₃ events. `stats()` now counts them, and the Boolean covers all five clauses. The two residual mismatches are printed as an explicit `[REPORT, not asserted]` line, outside any assertion.

## 4. A2 wording

The six published supplementary rows reproduce exactly at 1728 ICs each, totalling the owner's 10368. Extending the same generator past the owner-tabulated range to all `|d|_c > 2k` yields 32832 ICs — an **unregistered extrapolation** of the generation rule, used in no owner comparison. I should not have called it "the full one-pass family."

## 5. Where this leaves the science

| statistic | DSN | reconstruction |
|---|---|---|
| median period | 138 | **138 ✓** |
| max period | 1638 | **1638 ✓** |
| median preperiod | 0 | **0 ✓** |
| K₃ events in cycles | 0 | **0 ✓** |
| dominant periods | 15, 48, 357, 396, 228, 1638 | 5 of 6 shared |
| distinct lengths | 79 | 80 ✗ |
| max preperiod | 830 | 629 ✗ |

The informative reading is the one the review states: v1's cardinality agreement gave a false sense of construction validation, while v3's corrected stage-sign pairing recovers the two strongest period statistics and five of six dominant lengths. The remaining gap is therefore **more** informative, not less — this is no longer a broadly wrong reconstruction but a locally wrong one, most plausibly a small or localized convention or state-definition discrepancy. The data justify localized rather than broad mismatch; they do not establish that exactly one detail is responsible.

The tie coincidence (forcing the double-zero orientation yields 79 lengths) is reported and **not acted on**, since the owner specifies balanced ties as identity.

## 6. Gate unchanged

`k = 1` exact reproduction → `k ∈ {0,2,3}` enumeration → frozen DISC-1B/DISC-1D. The `629` vs `830` max-preperiod mismatch is decisive: aggregate closeness cannot certify the per-seed transport map DISC-1D consumes, and a preperiod discrepancy is direct evidence that individual orbits still differ. No provisional DISC-1 export.

**Unblock request, unchanged:** (1) `genesis_mode_b_mc_v18.py` or its three-node no-birth core; failing that (2) the exact `signed_defect_error(θ_a, θ_b, N)` **and** the cycle-key/canonicalization used for the published enumeration; optionally (3) the original `bind3_cycle_n24k1.py`.
