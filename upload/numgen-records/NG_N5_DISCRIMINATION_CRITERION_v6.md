# N-5 Discrimination v6 — State Freeze (`k=0` Boundary Ruling)

**Memo ID:** `NG_N5_DISCRIMINATION_CRITERION_v6` · **supersedes** `_v5` (memo only)
**Certificate:** `ng_n5_discrimination_identity_cert_v5.py` / `.log` — **unchanged and final** (8 literal `*-ID` rows, exit 0). No edit was made to it.
**Base:** `RTG_NUMBER_GENESIS_DSN_v1.15` (sha256 `d56440c6…3375`, verified)
**Date:** 2026-08-31 · **Auditor:** Claude
**Purpose:** incorporate the `k = 0` boundary ruling and freeze. This is a state-freeze update, not new design.

---

## 1. What changed from v5

Only the stability neighbourhood. v5 froze `K_stab = {0,2}` and left the `k = 0` status open. The owner ruling resolves it conservatively:

> `k = 0` is admissible but is a **singular boundary control**, not an elementary stability move.

Grounds: the retrigger condition becomes `|d|_c ≤ 2k = 0` at `k = 0`, so only the zero-advance case supports the two-node retrigger mechanism feeding BIND3 — a zero-width boundary stratum for precisely the structure under test. Elementary adjacency is therefore taken inside the positive-band stratum.

## 2. Frozen deformation structure

```
𝒦_DISC = {0, 1, 2, 3}          fixed N = 24, three-node no-birth sector
k₀     = 1                     base (DISC-1B preregistration point)
positive-band elementary graph: 1 ~ 2,  2 ~ 3
K_stab = {2}
K_cont = {0, 3}                0 = zero-width boundary control, 3 = interior
```

Also frozen: canonical CONV-TICK and CONV-P3CYC, unchanged SWAP/P3 predicates, frozen raw seed panel, same-realization guard, and the requirement that a comparison point qualifies only if its cycle is dual-active.

## 3. Frozen admission rule

For a base dual-active seed `x` with reduced class `r = r_{x,1}`:

- **Local stability:** `r_{x,2} = r`, with `x` dual-active at `k = 2`.
- **Contingency:** `∃ k_c ∈ {0,3}` with `x` dual-active there and `r_{x,k_c} ≠ r`.

By T4 the contingency condition is equivalently the strong fixed-class falsifier

```
|Δ_r^{(k_c)}| = |b a_{x,k_c} − a b_{x,k_c}|·m + O(1) → ∞.
```

**Pass subtypes (reported, admission unchanged):** `DISC-1D-PASS-INT` — persists at `k=2`, destroyed at `k=3`; contingency inside the positive-band regime, the stronger evidence. `DISC-1D-PASS-BDY` — persists at `k=2`, destroyed only at `k=0`; valid contingency through the boundary control.

## 4. Frozen observational failure taxonomy

- **No stability:** no qualifying base seed preserves its class under `1 → 2`.
- **No contingency:** stable seeds preserve the fixed class at every qualifying `k ∈ {0,3}`.
- **Panel-level both, never same realization:** the same-realization guard blocks admission.

All three are failures of DISC-1D on the `k` axis; they differ in diagnostic value, not in verdict.

## 5. Frozen reporting table

Base dual-active count; dual-active counts at `k = 0, 2, 3`; number surviving the `k = 2` stability fence; `PASS-INT` count; `PASS-BDY`-only count; passing-class multiset; and the complete transport map `x ↦ (r_{x,0}, r_{x,1}, r_{x,2}, r_{x,3})` with an explicit null marker where a cycle is not dual-active.

## 6. Implementation status

`disc1_analysis_harness_v1.py` already implements this ruling: its frozen constants are `K_BASE = 1`, `K_STAB = (2,)`, `K_CONT = (0, 3)`, with subtype separation and the full reporting table. No harness change is required by v6. The harness simulates no TDR-G kinematics by design and consumes an owner-produced enumeration under a declared contract.

## 7. Single remaining pre-data item (PI-blocked)

Whether DISC-1D may run on `r = 1:1` base candidates when DISC-1B fails. Reading (a): DISC-1B failure halts the branch. Reading (b): a `1:1` class stable at `k=2` and destroyed at `k ∈ {0,3}` admits `1 ∈ Q^dyn` despite the non-`1` census failing — coherent, since admission is per-label-via-some-realization and N5-PHYS-1 established `1 ∈ Q^bd` only as a control, but it would deliver a `Q^dyn` element from a branch that failed its own non-triviality test. Flagged only because deciding it after seeing an all-`1:1` census would make either answer look post-hoc.

## 8. State

**Criterion design is closed.** No further criterion work before BIND3 cycle data. Next operations, in order: obtain/reproduce the per-cycle enumeration at `N = 24` for `k ∈ {0,1,2,3}` over the frozen panel → run DISC-1B (original v1.15 falsifier intact) → run the frozen DISC-1D transport audit.

**Ledger:** C1–C4 CLOSED; C5-SYN-13 mathematical periodic control; T2 periodicity triviality; T3 corrected (closed finite invariant sector); T4 class-change ⟺ loss of boundedness of the fixed class; C6 unchanged and discriminating; N5-PHYS-1 first physical positive control, `1 ∈ Q^bd`; C7A unchanged; **`Q^dyn` = ∅ until a same-realization DISC-1D pass**; DISC-1B falsifiable non-`1` census; DISC-1D frozen as above; C7C downstream.
