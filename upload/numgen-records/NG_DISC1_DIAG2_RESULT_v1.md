# `[POSTHOC-DIAG]` Within-Spectrum Phase-Geometric Diagnostic — Result

> **`[POSTHOC-DIAG]` Hypothesis-generating only, on already observed DISC-1 data. No admission rule, threshold, deformation axis, or existing DISC-1 verdict is changed. Nothing here is C7B breadth evidence.**

**Memo ID:** `NG_DISC1_DIAG2_RESULT_v1` · **Date:** 2026-09-02
**Pre-registration:** `NG_DISC1_DIAG2_FEATURE_FREEZE_v1` (sha256 `a683639e…3e21`), frozen before any answer was inspected
**Outcome:** the **weak-but-informative** branch of the pre-declared readings — and sharper than either reading anticipated.

---

## 1. Result of the frozen hierarchy

**Test 1 (phase cells) — insufficient.** Every compensator `Δ_AC` cell also contains failures, in all three spectra; the same for `Δ_BC`. Joint `(Δ_AB, Δ_AC)` cells separate cleanly in `{0,1,9}` only, and overlap in the other two (6 of 12, and 2 of 4).

**Test 2 (shell-insertion topology) — insufficient.** Compensator feature vectors are *shared with failures*. In `{0,1,9}` the 12 compensators have a single feature vector, and that vector also occurs among failures. In `{0,1,8}` both compensator vectors occur among failures. Only `{0,1,18}` separates, on 1 vector versus 2.

**Test 3 (matched pairs) — reveals why.** The matched buckets contain compensator/failure pairs agreeing on spectrum, period, contact count, pair identities, edge transitions, word positions and cyclic spacings. Inspecting them:

```
spectrum {0,1,9}:  COMP  k=1 word (..SS.......PSSPSSP)^3
                   FAIL  k=1 word  the same cyclic word, rotated by 13
spectrum {0,1,8}:  COMP and FAIL have LITERALLY IDENTICAL k=1 words
```

## 2. The finding: compensators and failures share the same `k=1` cycle

Verified directly by comparing eventual cycles as reduced-state sets:

| | `{0,1,9}` | `{0,1,8}` |
|---|---|---|
| COMP `k=1` cycle | length 54, preperiod 64 | length 74, preperiod 38 |
| FAIL `k=1` cycle | length 54, preperiod 0 | length 74, preperiod 4 |
| **same `k=1` cycle?** | **True** | **True** |
| `k=2` cycle lengths | 54 vs 180 | 33 vs 162 |
| same `k=2` cycle? | False | False |

**Therefore no function of the `k=1` cycle can separate compensators from failures**, because they *are the same cycle*. Tests 1 and 2 did not fail for want of the right feature; they failed because the entire feature family — indeed any cycle-level observable — is constant across the two classes by construction. The distinguishing datum is the seed's **entry point** into the shared cycle relative to the `k=2` dynamics: the seeds sit at different preperiods, so under the widened band they depart the shared structure from different places and land in different `k=2` cycles.

This also disposes of the pre-registered `12 = 3×4`, `4 = 1×4` phase-cell hypothesis: survival is not a union of `Δ_AC` residue cells, and the counts do not reflect a cell-selection law.

## 3. What this means, stated carefully

`[POSTHOC-HYP]` **H-E.** On this frozen panel, "compensation" is **not a property of the base orbit or of its reduced class**. It is a property of the *(seed, axis)* pair — where the frozen initial state sits relative to the deformed dynamics. Two seeds on one `k=1` cycle, carrying the same conserved spectrum, the same class and the same shell-2 architecture, can differ in `k=2` fate.

This is consistent with everything ratified: DISC-1D's same-realization guard already binds admission to a *realization*, not to a label or an orbit, and this diagnosis shows why that guard was load-bearing rather than merely cautious.

It also revises H-D downward: the conserved advance spectrum organizes the compensators (all 28 lie in 3 of 43 exposed spectra) but cannot be part of a sufficient condition, since compensators and failures share spectra, cycles and words.

## 4. Consequence for C7B-DISC-2 design

The pre-declared weak outcome said explicitly that this would **argue against designing C7B-DISC-2 around a presumed simple shell-selection law**. That is now the position: no small owner-native cycle-level separator exists, and none can, on this panel.

The `Δ_AC → Δ_AC + h` candidate is *not* thereby weakened — it moves the seed, hence the entry point, which is precisely the quantity this diagnosis identifies as decisive. But its rationale changes: it should be motivated as an **entry-point perturbation**, not as a shell-architecture perturbation. Any preregistration should say so, and should still require a fresh data domain, since every `Δ_AC` value in the present panel has now been inspected.

## 5. Guards

Feature family and hierarchy were frozen in advance and neither was extended when Tests 1 and 2 came back insufficient; the shared-cycle finding came from the pre-declared Test 3 matching, not from a new feature. `{2,3} ⊆ Q^dyn` and `Q^dyn ≠ ∅` stand as ratified. Wording corrections from the previous round are carried: bijection holds among the 28 compensators, and H-D's necessity is on this frozen panel only.
