> **[SUPERSEDED 2026-09-03] Retained for lineage only. §1 wrongly stated that the CONV-TICK / CONV-P3CYC pinning is "not true of the document", contradicting its own §2; and item (f) was mislabelled as under-determination rather than ambiguous labelling. Canonical record: `NG_TO_TDRG_REPRODUCIBILITY_GAP_v2.md`. Do not cite as current.**

# Governance Note to the Discrete Genesis Owner — Reproducibility Gap in the BIND3 Certification

**Note ID:** `NG_TO_TDRG_REPRODUCIBILITY_GAP_v1` · **Date:** 2026-09-03
**From:** Number Genesis (auditor) · **To:** `RTG_DISCRETE_GENESIS_DSN` owner
**Concerns:** `BIND3-CYCLE-N24K1` `[ALG/NUM strong]` (§6.12), CONV-TICK (§6.3), CONV-P3CYC (§6.3), artifact `TDRG-ART-BIND3-N24K1`
**Status:** governance/provenance only. **No scientific claim is disputed.** The certification reproduces exactly once the missing conventions are supplied.

---

## 1. Summary

`BIND3-CYCLE-N24K1` is certified `[ALG/NUM strong]` and CONV-TICK / CONV-P3CYC are stated as *pinned to script truth* against `genesis_mode_b_mc_v18.py`. Both statements are true **of the script**. They are not true of the **document**: an independent party working from `RTG_DISCRETE_GENESIS_DSN_v2.12/13` alone cannot reproduce the certified enumeration.

This was established empirically, not asserted. Working only from the DSN, an independent reimplementation reproduced the IC family exactly (3456 ICs; 1152 at `d = ±1`, 576 at `d = ±2`; supplementary rows 1728 each) but produced **median period 150 vs 138, 96 vs 79 distinct lengths, max preperiod 1050 vs 830**. After `genesis_mode_b_mc_v18.py` was supplied, every published statistic reproduced exactly, including the full dominant-period list and the 124 / 3332 taxonomy.

Given the Zenodo archiving, this is worth recording as a defect in the *reproduction contract*, distinct from the correctness of the result.

## 2. What the DSN specifies sufficiently

No gap in: CONV-TICK ordering (advance → snapshot → classify on snapshot → apply against snapshot, no same-tick re-advance); the defect band `D_k`; the isolated-edge antipodal swap; CONV-P3CYC as the successor shift with the orientation rule; balanced path-ties inert under `bound_symmetric` (LEM-SPECCONS); `K₃` exclusion under narrow band. These were implemented correctly from the text on first attempt.

## 3. What the document under-determines

**(a) `signed_centered` boundary convention — the decisive item.** v18 returns the representative in `(−N/2, N/2]`; the natural alternative is `[−N/2, N/2)`. They differ at **exactly one argument**, `x = N/2 = 12` — the antipode, i.e. the centre of the defect band, which is therefore hit constantly. This single unstated convention accounted for the entire residual discrepancy in §1. It is not derivable from the DSN.

**(b) `signed_defect_error` is invoked but never reduced to a formula.** The orientation rule cites it; the text gives no expression. (The natural reading `signed_centered((θ_a − θ_b) mod N − N/2, N)` does match v18 — but that was luck, not derivation.)

**(c) IC-stage sign pairing.** §6.12 calls the family "post-advance BIND3 ICs". LEM-RETRIG defines `d_AB = δ_A − δ_B` with `ε' = ε − d`, consistent with `d` being the *pre-swap* relative advance. Whether the exported retrigger-entry state is the pre- or post-swap member of the dyad cycle is not stated. Getting this wrong yields the **exactly correct IC cardinality and `d`-resolved multiplicities with the wrong IC set** — a failure mode that looks like successful validation.

**(d) Cycle-key / canonicalization.** The key used for the published cycle detection is not stated. The gauge-reduced 4-tuple `(Δ_AB, Δ_AC, d_AB, d_AC)` agrees, but note this quotient relies on a *derived* no-birth dynamical symmetry (common token shift), not on SG-2's global-phase gauge, so it is not immediate from the stated gauge.

**(e) Bond-transfer classifier.** The 81.8% figure has no operational definition. Two principled readings give 83.3% ("a non-AB pair becomes bonded") and 81.8% ("the bonded pair identity changes"). The second matches — but selecting it *because* it matches would be fitting, so this remains undetermined from the document.

**(f) Supplementary-family scope.** The `d`-resolved table lists `|d|_c ≤ 5` totalling 10368, while the same generation rule extends to `|d|_c = 12` (32832 ICs). The document does not state that 10368 covers the tabulated rows rather than the full one-pass family.

## 4. Root cause

`TDRG-ART-BIND3-N24K1` is recorded as *"session-certified; consolidate into `bind3_cycle_n24k1.py`"*. That consolidation appears never to have happened, so the only executable witness for an `[ALG/NUM strong]` result is `genesis_mode_b_mc_v18.py` plus an unarchived session script. Items (a)–(f) are the predictable consequence: conventions that live in code and not in text, with nothing in between.

## 5. Recommended remedies (owner's call)

1. **Record the script hash beside the claim.** `genesis_mode_b_mc_v18.py` = `9d787b435c42fd2024c81e614e3c6e3e076dc2bd30ad1e7e286ada8e6dfe675e`. An `[ALG/NUM strong]` result whose reproduction depends on a specific script should name that script by hash, not by filename.
2. **Add a short reproduction contract to §6.12** covering (a)–(d) explicitly — four lines would suffice — and state (e) as `[OPEN]` or supply the classifier.
3. **Complete the `bind3_cycle_n24k1.py` consolidation.** A candidate is available: `bind3_repro_v5.py` reproduces every published statistic and taxonomy figure exactly, and its transition core is **one-step identical to v18 across all 331776 reduced states for every `k ∈ {0,1,2,3}`** (0 mismatches, `disc1_safeguards_v2.py` row S1). Offered for owner adoption or rejection; it is not claimed as canonical.
4. **Scope-correct (f)** so the 10368 figure is attached to the tabulated rows.

## 6. What is *not* claimed

No result is disputed. The taxonomy, period spectrum, `K₃ = 0`, and `d`-resolved anatomy all reproduce exactly. §6.12's own note that the coarse taxonomy is convention-robust while trajectory-level outcomes are convention-sensitive is confirmed and is precisely why (a)–(d) matter: any downstream use requiring **per-realization** trajectories — as the Number Genesis DISC-1 campaign did — depends on conventions the document does not fix.

## 7. Cross-reference

The DISC-1 campaign proceeded only after `k=1` reproduced exactly and the one-step differential passed; artifacts and hashes are in `NG_DISC1_RESULT_v4.md` §7 and `NG_BIND3_REPRO_STATUS_v3.md`. The reproduction history there doubles as the evidence base for this note.
