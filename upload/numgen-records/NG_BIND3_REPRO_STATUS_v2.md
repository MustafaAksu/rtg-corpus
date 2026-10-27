# BIND3 Reproduction Status v2 — Sign Error Corrected; Reproduction Now Close but Not Exact

**Memo ID:** `NG_BIND3_REPRO_STATUS_v2` · supersedes `_v1` · **Date:** 2026-09-01
**Target:** `BIND3-CYCLE-N24K1` (`RTG_DISCRETE_GENESIS_DSN v2.12/13`, §6.12)
**Artifacts:** `bind3_repro_v2.py` / `.log` (4 assertion rows + executable convention sweep, exit 0)
**Verdict:** IC families reproduced exactly; cycle statistics now match on median period, max period, median preperiod, K₃-freeness and 5 of 6 dominant periods, but **not** on distinct-length count or max preperiod. Still **not usable as DISC-1 input.**

---

## 1. `[COR]` — v1 carried a sign error, and it was mine

v1 paired the retrigger offset `ε` with `d_AB = +d`. The owner's retrigger relation is `ε' = ε − d`, while `Δ_AB = θ_A − θ_B` evolves as `Δ' = Δ + d_AB`. Hence the owner's `d` is `δ_B − δ_A = −d_AB`. Because the overlap `B_k ∩ (B_k + d)` is *not* symmetric in `d`, pairing `ε` with the wrong sign yields the right IC **cardinality** with the wrong IC **set** — which is exactly why v1's totals matched while its dynamics did not.

Correcting it moves the median period from 150 to the published **138**, the distinct-length count from 96 to 80, and recovers **5 of the 6** published dominant periods. This is a caution worth recording: v1's exact 3456/1152/576 agreement looked like strong validation of the construction, and it validated only the counting, not the pairing.

## 2. Three review corrections, applied as artifacts rather than relabelling

**(a) Balanced path-tie is not under-determined.** The owner specifies ties inert under `bound_symmetric` (LEM-SPECCONS). Removed from the gap list; retained as the canonical behaviour, with tie variants kept in the sweep only as a sensitivity probe.

**(b) Supplementary family now reproduced, not claimed algebraically.** `ics()` generates it: per-`d` counts are **1728** at each of `d = ±3, ±4, ±5`, matching every published row. One clarification the reproduction exposes — the DSN table lists only `|d|_c ≤ 5`, whereas the full `|d|_c > 2k` family extends to `|d|_c = 12` (32832 ICs). The published 10368 therefore covers the tabulated rows, not the whole one-pass family.

**(c) The convention sweep is now executable code** in `bind3_repro_v2.py`, not a memo-level execution report.

**(d) The quotient is a derived symmetry, not SG-2 gauge** — reworded and, more usefully, *verified*: the induced map on `(Δ_AB, Δ_AC, d_AB, d_AC)` is well defined across all **331776** reduced states under three independent lifts, 0 mismatches. Proof sketch: a common shift `δ_i → δ_i + b` advances every `θ_i` equally, leaving all `Δ_ij` fixed, and commutes with both the swap and the `P₃` successor shift. This does not settle whether the published *periods* used the same key.

## 3. Where the reproduction now stands

| statistic | DSN | `sde=offset`, ties inert |
|---|---|---|
| median period | 138 | **138 ✓** |
| max period | 1638 | **1638 ✓** |
| median preperiod | 0 | **0 ✓** |
| K₃ in cycles | 0 | **0 ✓** |
| dominant periods | 15, 48, 357, 396, 228, 1638 | 15, **30**, 48, 357, 396, 228 — 5 of 6 shared |
| distinct lengths | 79 | 80 ✗ |
| max preperiod | 830 | 629 ✗ |

The alternative `sde` definitions (`neg`, `raw`) are far off on every statistic, so `sc((θ_a − θ_b) − N/2)` is very likely the right family — but "very likely" is not the standard here.

**One suggestive detail, offered as a question rather than a conclusion.** Ties inert gives 80 distinct lengths; forcing an orientation at the tie gives **79**, matching the DSN, with identical median/max/dominant. Since the owner documents ties as inert, either the extra length has another source or v18's tie path differs from the documented behaviour. I am not adopting the orientation-forcing variant — that would be tuning to the target, and the review's point about `bound_symmetric` stands. I flag it as a coincidence the owner may be able to explain or dismiss.

## 4. Narrowed unblock request

1. **Best:** `genesis_mode_b_mc_v18.py`, or the three-node no-birth transition/cycle core.
2. **Minimal substitute:** the exact source of `signed_defect_error(θ_a, θ_b, N)`, **and** the cycle-key/canonicalization function used for the published enumeration.
3. Optionally the original `bind3_cycle_n24k1.py` consolidation artifact.

Per the review, I am no longer asking for confirmation of CONV-TICK, the swap, the `P₃` successor shift, tie semantics, or the SWAP/`P₃` event meanings — the owner documents all of these sufficiently for DISC-1.

## 5. Gate unchanged

No `k ∈ {0,2,3}` enumeration and no DISC-1 export until the independent implementation reproduces the `k = 1` certification exactly. Getting closer is not the criterion: the per-seed transport map DISC-1D consumes is precisely the trajectory-level quantity the DSN warns is convention-sensitive, and a 629-vs-830 preperiod discrepancy is direct evidence that individual orbits still differ. The frozen DISC-1 architecture is untouched.
