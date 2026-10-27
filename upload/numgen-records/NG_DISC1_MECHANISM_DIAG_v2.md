# `[POSTHOC-DIAG]` 2:1 / 3:1 Stability-Mechanism Diagnosis v2

> **`[POSTHOC-DIAG]` Mechanism diagnosis on already observed DISC-1 data. Hypothesis-generating only. No admission rule, threshold, deformation axis, or existing DISC-1 verdict may be changed from this analysis.**

**Memo ID:** `NG_DISC1_MECHANISM_DIAG_v2` · supersedes `_v1` · **Date:** 2026-09-02
**Base:** `RTG_NUMBER_GENESIS_DSN_v1.16` (sha256 `c86eacb2…002f`) · enumeration `dab769a0…fc83d`

---

## 1. `[COR]` — v1 used the wrong observable

v1 measured the **minimum** pair shell per step. That is not the physically relevant quantity: a state can carry a shell-1 pair *and* a shell-2 pair simultaneously, so the minimum hides precisely the newly admitted edge the diagnosis is about. The correct observable is any-pair exposure `X_s(t) = 1{∃ i<j : |sde_ij(t)| = s}`. All §2 figures are replaced. v1's non-eligible comparison was also a 400-seed sample described as "across the census"; the full census is used here.

Corrected, with every PI figure reproduced exactly:

| | zero shell-2 exposure | mean shell-2 exposure |
|---|---|---|
| eligible (64) | **36 / 64 = 56.25%** | 0.0651 |
| non-eligible (3189) | **0 / 3189 = 0%** | 0.2220 |

So on this panel **every zero-shell-2 base orbit survives `1→2`** — and the converse fails: 28 eligible realizations have genuine exposure and compensate anyway (mean 0.1489, median 0.1622, against 0.2220 and 0.2128 for the 3189 failures). Archetype exposures: `P=9 → (0, 0)`, `P=36 → (0.2222, 0.1667)`, `P=54 → (0.1111, 0.2222)`, `P=74 → (0.1622, 0.2432)`.

**The partition the corrected metric exposes:**

```
64 stable = 36 deformation-blind + 28 genuinely compensating
22 DISC-1D passes ⊂ 28 genuinely compensating
```

This is the scientifically important consequence: v1's single "64 eligible" count mixed two mechanisms that the corrected observable separates.

## 2. A second `[COR]`, self-caught — my spectrum canonicalization

The advance spectrum is conserved because swap and the `P₃` successor shift only **permute** the `δ` tokens. My first normalization subtracted the minimum and applied `sc()`, which wraps and splits classes that are equal under common shift: `(0,1,8)` and `(−1,0,7)` are the same multiset. That inflated 3 spectra into 6 and would have made the result look weaker than it is. Canonical form is now the lexicographic minimum over all common shifts mod `N`.

## 3. The 28 exposed compensators versus the 3189 exposed failures

**The conserved advance spectrum is strongly organizing, and it is in exact bijection with the archetypes:**

| spectrum | compensators | exposed seeds with it | survival | archetype |
|---|---|---|---|---|
| `{0, 1, 9}` | 12 | 96 | 12.5% | `2:1`, P=54 |
| `{0, 1, 8}` | 12 | 96 | 12.5% | `3:1`, P=74 |
| `{0, 1, 18}` | 4 | 96 | 4.2% | `2:1`, P=36 |

The 28 compensators occupy **only 3 of the 43** exposed spectra, and each spectrum maps to exactly one archetype — so among exposed orbits, the conserved spectrum determines the archetype. This is a genuine organizing structure, matching the owner's treatment of the advance spectrum as a primary BIND3 invariant, and it is not feature mining: the quantity was selected because it is conserved by the dynamics.

**It is necessary but not sufficient.** Within each admitted spectrum only 12.5% (or 4.2%) of exposed seeds compensate, so a second condition — presumably phase-geometric, since the spectrum fixes the advance tokens but not `Δ_AC` — separates survivors within a spectrum class. That is the remaining open half of the question.

For contrast the 36 blind seeds carry spectra `{0,1,21}`, `{0,1,5}`, `{0,2,21}` — disjoint from all three compensator spectra.

## 4. Q3 stands unchanged

The `2:1` internal control is unaffected by the metric correction. Within the single label `2:1`: `P=9` blind, `P=36` perturbed and compensating through `k=3`, `P=54` compensating at shell 2 and destroyed at shell 3 (`(18,9) → (16,8)` preserves `2:1`; `(16,8) → (84,120)` becomes `7:10`). Class label alone cannot determine the outcome; orbit architecture does.

## 5. Hypotheses, narrowed as ruled

- **H-A′ `[POSTHOC-HYP]`** — shell exposure partitions stability into a blind component and a genuinely compensating component. Zero shell-2 exposure explains 36/64 exactly; exposure magnitude may modulate compensating survival but does not explain it.
- **H-B′ `[POSTHOC-HYP]`** — blindness should be reported separately from compensation on future campaigns. **Blindness is relative to the chosen deformation interval**, not an intrinsic property: a cycle blind to `k = 1→3` could respond to a different axis. v1's claim that "blind seeds cannot contribute contingency by construction" is accordingly rescoped to the specific axis and range on which their edge/state evolution is unchanged.
- **H-C `[POSTHOC-HYP]`** — an axis perturbing shell architecture while preserving the sector is worth considering. **Design motivation only, never C7B evidence.**
- **H-D `[POSTHOC-HYP]` (new)** — the conserved advance spectrum is a necessary organizing filter for compensation: only 3 of 43 exposed spectra admit compensators, and spectrum determines archetype. The sufficient condition is phase-geometric and unidentified.

## 6. Design firewall, recorded

The `Δ_AC → Δ_AC + h` phase-translation axis is an attractive **candidate** — same state space, AB retrigger relation preserved, advance spectrum untouched, and it perturbs exactly the shell geometry isolated here. It must **not** be applied to the existing `N=24` enumeration and scored as C7B evidence: every `Δ_AC` value is already represented in the frozen panel and its outcomes have been inspected extensively, so scoring that panel after choosing the axis would be post-hoc. Any C7B-DISC-2 requires a frozen axis definition **and a fresh data domain** on which no candidate-axis trajectory has been inspected.

## 7. Guards

Exploratory throughout; no admission rule, threshold, axis, or verdict changed. `{2,3} ⊆ Q^dyn` and `Q^dyn ≠ ∅` stand exactly as ratified. Nothing here touches SG-NG-19/23/24, C7C, or the continuous branch.
