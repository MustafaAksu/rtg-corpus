> **[SUPERSEDED 2026-09-03] Draft only; the k=0 slot was open and the reporting contract was not layered. Canonical: NG_C7B_DISC2_PREREG_v1.md. Do not cite as current.**

# C7B-DISC-2 — Pre-Registration (DRAFT, one slot open)

**Doc ID:** `NG_C7B_DISC2_PREREG_v1_DRAFT` · **Date:** 2026-09-03 · **Auditor:** Claude
**Status:** DRAFT. **Not frozen.** One design slot (§3.2) requires a PI ruling before freeze.
**Governing definitions:** `NG_N5_DISCRIMINATION_CRITERION_v6_2`, `NG_DISC1_DIAG3_RESULT_v3` (witness relation)

---

## 0. `[COR]` — the seed-phase axis is withdrawn

I proposed `Δ_AC → Δ_AC + h` as the DISC-2 axis. **Withdrawn.** DISC-1 has the structure *`x` fixed, `F_k` varied*; seed translation is *`F` fixed, `x → x_h`*. Those are different realizations, so treating the `h`-family as "the same realization" would silently weaken the same-realization guard — and would do so on exactly the operation Diag3 identified as changing the discriminating information. `Δ_AC → Δ_AC + h` may still serve as a **seed/domain constructor**; it is not an admission axis.

Separately: translating the existing 3456-seed panel would not yield a fresh domain, since that construction already ranges over every `Δ_AC ∈ Z_24` and every `d_AC`.

## 1. Design

```
DISC-2 = fresh owner-registered supplementary seed domain
       + the already-certified same-realization k-axis
       + witness-first reporting
```

No new deformation law is introduced. Further breadth requires a new **pre-registration**, not a new dynamics; the certified `k`-axis may be applied to a previously untouched physical seed family.

## 2. Fresh domain

The owner-registered **supplementary one-pass family**: `|d|_c = 3, 4, 5`, six registered rows, 1728 ICs each, **10368 total**. Excluded: the unregistered extension beyond `|d|_c = 5` (32832 ICs), which is an extrapolation of the generator, not an owner-certified family.

**Freshness attested.** Only the *cardinalities* of this family have been computed (`bind3_repro_v5.py` row A2, a `Counter` over `d`). No trajectory, cycle, event count, or fate of any supplementary seed has been computed or inspected at any point. Verified by source inspection before drafting.

**Pre-data risk, declared:** these are one-pass ICs with empty retrigger overlap, so the base dual-activity rate is unknown and could be low. This is **not** checked in advance — checking would inspect the domain. If few base seeds are dual-active, that outcome is reported under the frozen failure taxonomy (§5) rather than treated as a reason to change the domain.

## 3. Axis and comparison points

### 3.1 Frozen
Same `N = 24`, three-node no-birth sector, canonical CONV-TICK / CONV-P3CYC, unchanged SWAP / active-P3 predicates, `bound_symmetric`. Base `k_0 = 1`. Same-realization guard in force: one frozen seed `x` supplies both witnesses. A comparison point qualifies only if the cycle is dual-active there. Positive-band adjacency `1~2, 2~3`, so `K_stab = {2}`.

### 3.2 **OPEN — requires PI ruling before freeze:** is `k = 0` retained?

- **Omit** (`K_cont = {3}`): DISC-1 produced zero boundary-only passes, and `k = 0` is a singular zero-width stratum. Sharper, and removes a comparison point that contributed nothing.
- **Retain** (`K_cont = {0, 3}`): preserves the `PASS-INT` / `PASS-BDY` subtype distinction and keeps DISC-2 directly comparable to DISC-1.

I have no standing to rule. **It must be decided now, not inherited automatically** — which is why the document is drafted with the slot open rather than defaulted.

### 3.3 Pass rule (given §3.2)
For one frozen seed `x` with base class `r = r_{x,1}`:
- **Stability:** `r_{x,2} = r`, dual-active at `k = 2`.
- **Contingency:** `∃ k_c ∈ K_cont` dual-active with `r_{x,k_c} ≠ r`; equivalently by T4, `|Δ_r^{(k_c)}|` diverges linearly.

## 4. Primary raw object — witness transport table

One row per (seed, deformation point):

```
seed_id, domain_id, k, r_base, r_k, n_swap, n_P3, dual_active,
preperiod, period, blind/exposed, stability, contingency, pass_subtype
```

plus immutable raw seed coordinates and cycle provenance sufficient to recount each witness. The label set is computed **only afterward**, as the projection

```
Q^dyn_established,new = π_r( W_existing ∪ W_DISC2 )
```

**No prevalence threshold.** One valid witness suffices — that is the standing definition of `Q^dyn`, and introducing a threshold now would be a post-data strengthening.

## 5. Frozen failure taxonomy

Report each seed under exactly one: no base dual activity; stability unavailable; stable but no contingency; contingency without stability; both present panel-wide but never on one realization; deformation-blind; valid PASS; and PASS split into **new-label** versus **already-established-label**.

**Declared in advance:** a campaign yielding witnesses only for `2` and `3` is a **successful dynamic campaign with no new label breadth**, not a failed experiment. This preserves the distinction between witness structure and label projection.

## 6. Blindness — reported, never a fence

For each seed, report whether the declared deformation actually changes its trajectory/edge structure. **Do not** add "stability counts only if non-blind." The two-sided criterion already handles blindness: a seed blind across the comparison set cannot supply contingency and so cannot pass. Blindness is a **reporting subtype**, and adding it as a fence would be a post-DISC-1 strengthening of the gate.

## 7. Guards

Nothing here alters DISC-1's verdicts or the ratified `{2,3} ⊆ Q^dyn`. No admission rule, threshold, or witness set is changed. The analysis code is frozen before any fresh-domain trajectory is computed; if the existing harness requires modification for the new domain, that modification is frozen and hashed before use.
