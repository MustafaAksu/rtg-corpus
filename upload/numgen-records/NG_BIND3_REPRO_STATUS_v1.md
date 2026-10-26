# BIND3 Reproduction Status — IC Family Recovered, Dynamics Not Reproduced

**Memo ID:** `NG_BIND3_REPRO_STATUS_v1` · **Date:** 2026-09-01
**Target:** `BIND3-CYCLE-N24K1` (`RTG_DISCRETE_GENESIS_DSN v2.12/13`, §6.12)
**Artifact:** `bind3_repro_v1.py`
**Verdict:** IC family reproduced **exactly**; cycle dynamics **not** reproduced. The DSN text under-determines an independent reimplementation. Enumeration for DISC-1 is **blocked** pending owner input.

---

## 1. What was reproduced exactly

The retrigger-entry IC construction is recoverable from the DSN and reproduces the published family with no free parameters. Gauge-reduced state is `(Δ_AB, Δ_AC, d_AB, d_AC)` (SG-2: absolute phase is gauge; boost `δ_i → δ_i + b` also leaves all `Δ_ij` invariant, so the reduced space is `ℤ_N⁴`). ICs take `Δ_AB = N/2 + ε` with `ε ∈ B_k ∩ (B_k + d)`, `|d|_c ≤ 2k`, and `(Δ_AC, d_AC)` free:

| `d` | overlap size | × 576 spectator states | DSN |
|---|---|---|---|
| ±1 | 2 | 1152 each | 1152 each ✓ |
| ±2 | 1 | 576 each | 576 each ✓ |
| **total** | | **3456** | **3456** ✓ |

The `|d|_c ≥ 3` rows corroborate independently: the overlap is empty there, all three band offsets are used, `3 × 576 = 1728` ✓ matches every supplementary row. This construction was inferred, not given, and its exact agreement is good evidence it is correct.

## 2. What was not reproduced

Implementing CONV-TICK, the defect band, the antipodal swap, CONV-P3CYC successor shift and the path orientation rule as written:

| statistic | DSN | best reconstruction |
|---|---|---|
| max period | 1638 | **1638 ✓** |
| K₃ components in cycles | 0 | **0 ✓** |
| median preperiod | 0 | **0 ✓** |
| median period | 138 | 150 ✗ |
| distinct periods | 79 | 96 ✗ |
| max preperiod | 830 | 1050 ✗ |
| dominant periods | 15, 48, 357, 396, 228, 1638 | 15, 324, 27, 396, 1638, 828 (3 of 6 shared) |

The partial agreement — max period, K₃ count, median preperiod, and three of six dominant periods — indicates the reconstruction is close but differs in at least one rule.

## 3. Convention sweep, and why I stopped

The DSN leaves two slots under-determined: the definition of `signed_defect_error` used in the orientation score, and the behaviour at a balanced path-tie (`S = E = 0`, where the DSN states no gauge-invariant orientation exists but not what the simulator does). I swept 3 × 3 = 9 principled combinations. **None reproduces the published statistics.** Ties are live, not vacuous: 54 tie events occur in-cycle under the closest variant, so the tie rule is load-bearing rather than a formality.

I stopped there deliberately. Continuing to search convention space until the numbers matched would be fitting a reimplementation to a target, and any subsequent agreement would be an artifact of the search rather than evidence the mechanism was correctly recovered. That is the same failure mode as tuning an analysis after seeing data.

## 4. Reproducibility finding worth logging

§6.12 states that CONV-TICK and CONV-P3CYC pin the conventions "to script truth", and both are `[ENG audit: PASS]` against `genesis_mode_b_mc_v18.py`. That is true of the *script*, but this exercise shows the **document alone does not determine an independent reimplementation**: `genesis_mode_b_mc_v18.py` is load-bearing for reproducing a `[ALG/NUM strong]` certified result. Given the programme archives to Zenodo, I would log this as a reproducibility gap against the DSN rather than a defect in the result.

## 5. What I need to proceed (owner input)

1. `genesis_mode_b_mc_v18.py`, or its three-node no-birth core — the cleanest unblock.
2. Failing that: the exact definition of `signed_defect_error(θ_a, θ_b, N)`; the simulator's behaviour at a balanced path-tie; the initial listing order of `[v₁, v₂, v₃]` before orientation; and confirmation that cycle detection was performed in the gauge-reduced space `(Δ_AB, Δ_AC, d_AB, d_AC)` rather than in `(θ, δ)`.
3. Confirmation that in the three-node no-birth sector the only applied events are the isolated-edge swap and the `P₃` successor shift (i.e. that `n_swap` and `n_p3` for DISC-1 count exactly these).

## 6. Status against the frozen DISC-1 plan

Nothing in the frozen architecture changes. The harness, regression, criterion and pre-registration are untouched and remain immutable. What is blocked is only the **input**: DISC-1B and DISC-1D cannot run on a reimplementation that does not reproduce the certified `k = 1` enumeration, since a per-seed transport audit is exactly the trajectory-level quantity the DSN warns is convention-sensitive.

**I did not generate a provisional enumeration for the harness.** A provisional run would produce numbers in the canonical output format that could later be mistaken for the certified census, and the DISC-1D verdict depends on precisely the trajectory detail that is currently wrong.

Reproducing `BIND3-CYCLE-N24K1` is the natural gate: once the reimplementation matches the published `k = 1` statistics, extending to `k ∈ {0,2,3}` and running the frozen harness is mechanical.
