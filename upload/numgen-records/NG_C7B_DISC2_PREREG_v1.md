# C7B-DISC-2 — Pre-Registration (FROZEN)

**Doc ID:** `NG_C7B_DISC2_PREREG_v1` · **Date:** 2026-09-03 · **Auditor:** Claude
**Status:** **FROZEN.** No fresh-domain trajectory has been computed. PI ruling of 2026-09-03 incorporated.
**Governing:** `NG_N5_DISCRIMINATION_CRITERION_v6_2`, `NG_DISC1_DIAG3_RESULT_v3`, `NG_DISC1_FREEZE_MANIFEST_v1`

---

## 0. `[COR]` — the seed-phase axis is withdrawn

I proposed `Δ_AC → Δ_AC + h` as the DISC-2 axis. **Withdrawn.** DISC-1 is *`x` fixed, `F_k` varied*; seed translation is *`F` fixed, `x → x_h`* — a different realization. Treating the `h`-family as "the same realization" would weaken the same-realization guard on precisely the operation Diag3 showed changes the discriminating information. It may serve as a seed/domain constructor; it is not an admission axis. Translating the existing panel would also not give a fresh domain, since that construction already ranges over every `Δ_AC ∈ Z_24` and every `d_AC`.

## 1. Design

```
DISC-2 = fresh owner-registered supplementary seed domain
       + the already-certified same-realization k-axis (unchanged)
       + witness-first reporting
```

No new deformation law. Further breadth requires a new **pre-registration**, not a new dynamics.

## 2. Fresh domain

Owner-registered **supplementary one-pass family**: `|d|_c = 3, 4, 5`, six registered rows, 1728 ICs each, **10368 total**. Excluded: the unregistered extension beyond `|d|_c = 5` (32832 ICs).

**Freshness attested by source inspection.** Only *cardinalities* of this family have ever been computed (`bind3_repro_v5.py` row A2 — a `Counter` over `d`). No trajectory, cycle, event count, or fate of any supplementary seed has been computed or inspected.

**Pre-data risk, declared and deliberately unchecked:** these are one-pass ICs with empty retrigger overlap, so base dual-activity rate is unknown and may be low. Checking in advance would inspect the domain. A low rate reports as `NO_BASE_DUAL` under §5, never as grounds to change the domain.

## 3. Axis — identical to the certified DISC-1 family

```
K_DISC = {0, 1, 2, 3}     k_0 = 1     K_stab = {2}     K_cont = {0, 3}
```

**PI ruling (2026-09-03): `k = 0` retained.** Architectural, not empirical: DISC-2 reuses the certified axis, which includes `k = 0` as the admissible singular boundary control. Dropping it because DISC-1 produced zero boundary-only passes would be a data-informed alteration of the gate, and would reject a DISC-2 transport pattern that DISC-1 would have admitted. DISC-1's zero `PASS-BDY` is a historical observation making no prediction about the untouched panel.

Same `N = 24`, three-node no-birth sector, canonical CONV-TICK / CONV-P3CYC, unchanged SWAP / active-P3 predicates, `bound_symmetric`, positive-band adjacency `1~2, 2~3`. Same-realization guard in force. A comparison point qualifies only if dual-active there.

**Pass rule (unchanged from DISC-1).** For frozen seed `x` with base class `r = r_{x,1}`: stability iff `r_{x,2} = r` with `k=2` dual-active; contingency iff `∃ k_c ∈ {0,3}` dual-active with `r_{x,k_c} ≠ r` — equivalently by T4, `|Δ_r^{(k_c)}|` diverges linearly.

## 4. Analysis engine — sealed, unmodified

The frozen `disc1_analysis_harness_v1.py` (`57a15421b352f8fbe58d7642d78a6ebb936b78aae90d91b9e39034b738510d9d`) already implements `K_DISC = (0,1,2,3)`, `K_BASE = 1`, `K_STAB = (2,)`, `K_CONT = (0,3)` and the subtype precedence. **It is used unchanged.** The supplementary-domain enumerator emits the existing schema; any additional witness/provenance fields live in a companion transport artifact the harness does not read. The decision engine is not reopened.

## 5. Reporting contract — three frozen layers

`[COR]` The draft's single flat list conflated per-seed verdicts, panel diagnoses and orthogonal annotations, and was not mutually exclusive.

**(a) Per-seed gate verdict — mutually exclusive, exhaustive**

1. `NO_BASE_DUAL`
2. `STABILITY_UNAVAILABLE` — `k=2` not dual-active
3. `UNSTABLE` — `k=2` dual-active but `r_2 ≠ r_1`
4. `STABLE_NO_CONTINGENCY`
5. `PASS_INT` — whenever `k=3` supplies contingency, even if `k=0` does too
6. `PASS_BDY_ONLY` — no interior pass, but `k=0` supplies one

**(b) Orthogonal per-seed annotations** — blind/exposed flags; base class; new-label vs already-established-label for passes; qualifying status at each `k`.

**(c) Panel-level diagnoses** — stability somewhere but contingency nowhere; contingency somewhere but stability nowhere; both on the panel but never on one realization; no new label breadth; new label breadth.

**Declared in advance:** witnesses only for `2` and `3` constitute a **successful dynamic campaign with no new label breadth**, not a failed experiment.

## 6. Trajectory blindness — operational definition, reporting only

`[COR]` Blindness is **not** defined by eventual-cycle equality: Diag3 showed two realizations can share an eventual cycle and differ in deformation fate.

For seed `x`, comparison `k` is **trajectory-blind relative to base** iff

```
F_k^t(x) = F_1^t(x)   for all t ≥ 0
```

in the canonical reduced representation. Finitely decidable in this deterministic finite sector: evolve the paired trajectory `(F_1^t(x), F_k^t(x))` until the pair-state repeats; blind iff it never leaves the diagonal before pair-cycle closure.

Report `blind_k0`, `blind_k2`, `blind_k3`, and `axis_blind = blind_k0 ∧ blind_k2 ∧ blind_k3`. **Reporting only, never an admission fence** — the two-sided criterion already handles blindness, since a seed blind across the comparison set cannot supply contingency. Adding it as a fence would be a post-DISC-1 strengthening.

## 7. Label projection

Computed only after the transport table exists:

```
Q^dyn_established,new = π_r( W_existing ∪ W_DISC2 )
```

**No prevalence threshold.** One valid witness suffices — the standing definition. A threshold introduced now would be a post-data strengthening.

## 8. Guards

Nothing alters DISC-1's verdicts or the ratified `{2,3} ⊆ Q^dyn`. No admission rule, threshold, witness set or comparison point is changed from the certified family. The analysis engine is sealed and unmodified. No fresh-domain trajectory is computed before this document is frozen and hashed.
