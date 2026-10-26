# DISC-1B / DISC-1D — Frozen Pre-Registration and Analysis Harness

**Memo ID:** `NG_DISC1_FROZEN_PREREGISTRATION_v1` · consolidates the PI ruling of 2026-08-31
**Base:** `RTG_NUMBER_GENESIS_DSN_v1.15` (sha256 `d56440c6…3375`, verified) + `NG_N5_DISCRIMINATION_CRITERION_v5`
**Artifacts:** `disc1_analysis_harness_v1.py` / `.log` (frozen analysis code, synthetic self-test exit 0)
**Status:** architecture **FROZEN**. No further criterion design. Next operation is data acquisition.

---

## 1. The ruling, recorded

`k = 0` is admissible but is **not** an elementary stability neighbour of `k = 1`: at `k = 0` the retrigger condition collapses to `|d|_c ≤ 2k = 0`, so only the zero-advance case supports the two-node retrigger mechanism feeding BIND3, making it a zero-width boundary stratum for exactly the structure under test. Adjacency is therefore taken inside the positive-band stratum (`1~2`, `2~3`), with `k = 0` retained as a named boundary comparison control.

```
𝒦_DISC = {0,1,2,3}      base k₀ = 1
𝒦_stab = {2}            elementary positive-band neighbour
𝒦_cont = {0,3}          0 = boundary control, 3 = interior
```

**Pass rule (same-realization).** For a frozen seed `x` with dual-active base cycle of reduced class `r = r_{x,1}`: require `r_{x,2} = r` with the `k=2` cycle dual-active (**local stability**), and `∃ k_c ∈ {0,3}` with dual-active cycle and `r_{x,k_c} ≠ r` (**contingency**) — equivalently, by T4, `|Δ_r^{(k_c)}| = |b a_{x,k_c} − a b_{x,k_c}|·m + O(1) → ∞`. Subtypes reported separately: `DISC-1D-PASS-INT` (destruction at `k=3`) and `DISC-1D-PASS-BDY` (destruction only at `k=0`), the former being stronger evidence of dependence on dynamics within the same positive-band regime. Neither is mandatory.

**Null taxonomy, observational.** "No stability anywhere" now means specifically: *no base candidate survives the positive-band elementary move `1→2`*.

## 2. Analysis code frozen before data

`disc1_analysis_harness_v1.py` implements the above with the witness sets and pass conditions as module constants, so no threshold or witness set can be adjusted after ratios are seen. Synthetic self-test passes (exit 0): it correctly classifies a `PASS-INT` seed, a `PASS-BDY` seed, a seed failing the stability fence, a `1:1`-everywhere seed with no contingency, and a seed not dual-active at base.

**The harness deliberately does not simulate TDR-G.** It implements no swap/P3 kinematics, no CONV-TICK, no CONV-P3CYC — those are owner mechanisms, and reimplementing them from a description would fabricate an owner result rather than audit one. It consumes an enumeration in a declared contract:

```json
{"seed_id": str, "k": 0|1|2|3, "dual_active": bool,
 "n_swap": int, "n_p3": int, "cycle_len": int}
```

with records present for non-dual-active cases as explicit null markers. Emitted report covers every frozen reporting requirement: base dual-active count, dual-active count per `k`, count eligible after the stability fence, interior vs boundary-only pass counts, admitted class multiset, and full transport tuples `x ↦ (r_{x,0}, r_{x,1}, r_{x,2}, r_{x,3})`.

## 3. One interaction the frozen spec leaves ambiguous — for ruling before data

DISC-1B fails iff no dual-active base cycle carries a non-`1` class. DISC-1D is a separate gate on a base class `r`. Nothing currently states whether DISC-1D may be run on `r = 1:1` candidates, and the two readings give materially different outcomes:

- **(a) DISC-1B failure halts the branch.** No `Q^dyn` admission from this axis if the census is all-`1:1`.
- **(b) DISC-1D runs independently.** A `1:1` base class that is stable at `k=2` and destroyed at `k∈{0,3}` would put **`1 ∈ Q^dyn`** even though the non-`1` search failed.

Reading (b) is not incoherent: `Q^bd` and `Q^dyn` are sets of *labels*, admission is per-label-via-some-realization, and N5-PHYS-1 established `1 ∈ Q^bd` only as a control. A dynamically contingent realization of the label `1` would be a genuinely different object from that control — the numeral would coincide while the epistemic status would not. But it would also mean the branch delivers a `Q^dyn` element while failing its own non-triviality census, which reads oddly and should not be discovered after the fact.

This is a definitional/interpretive call and therefore PI-blocked. I flag only that the current frozen text does not decide it, and that discovering the ambiguity *after* seeing an all-`1:1` census would make either answer look post-hoc.

## 4. State

DISC-1B and DISC-1D are frozen; the analysis code is frozen; the remaining dependency is the per-cycle BIND3 enumeration at `N = 24` for `k ∈ {0,1,2,3}` over the frozen raw seed panel. Order of operations: reproduce/obtain the enumeration → run DISC-1B → run the `k`-transport audit for DISC-1D. The original v1.15 SWAP/P3 falsifier is intact at the DISC-1B layer.
