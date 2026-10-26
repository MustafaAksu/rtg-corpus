# `[POSTHOC-DIAG]` 2:1 / 3:1 Stability-Mechanism Diagnosis

> **`[POSTHOC-DIAG]` Mechanism diagnosis on already observed DISC-1 data. Hypothesis-generating only. No admission rule, threshold, deformation axis, or existing DISC-1 verdict may be changed from this analysis.**

**Memo ID:** `NG_DISC1_MECHANISM_DIAG_v1` · **Date:** 2026-09-02
**Base:** `RTG_NUMBER_GENESIS_DSN_v1.16` (sha256 `c86eacb2…002f`, verified) · enumeration `dab769a0…fc83d`
**Scope:** answers Q1–Q3 as posed. Renamed from "`n:1` specialness" per the PI correction.

---

## 0. The reframing was necessary and is confirmed

`n:1` was the wrong target. Reproduced exactly: eligible by class is `2:1 → 52`, `3:1 → 12`, everything else `0`, while other `n:1` classes are present in quantity and all fail:

| class | base | eligible | `k=1` period range |
|---|---|---|---|
| 4:1 | 134 | **0** | 15–39 |
| 5:1 | 96 | **0** | 108–846 |
| 6:1 | 82 | **0** | 21–72 |
| 7:1 | 64 | **0** | 32–300 |
| 8:1 | 80 | **0** | 27–78 |
| 9:1 | 20 | **0** | 50–114 |
| 10:1 | 8 | **0** | 45 |
| 14:1 | 48 | **0** | 30–378 |

Denominator 1 and short period are both insufficient. The four stability archetypes reproduce exactly as tabulated, including the `k=3` outcomes and the two `3:1` seeds that lose dual activity.

## 1. Q1 — the orbit words

```
2:1  P= 9  n=36 : SSPSSPSSP                       (pure (SSP)^3, fully saturated)
2:1  P=36  n= 4 : P...S...S...P.S..S..S.P...S...S...PS
2:1  P=54  n=12 : (..SS.......PSSPSSP)^3          (inert stretch + saturated block)
3:1  P=74  n=12 : SSP..S.S.....S.....S.S..P......S.S..P  (×2, with a shift)
```

Event-count ratios were indeed hiding structure: the `P=9` archetype is a fully saturated period-3 repeat with no inert steps, while the others interleave long inert stretches with saturated blocks.

## 2. Q2 — what widening `k` adds, and the decisive finding

The `1→2` move admits the shell-2 edges (defect-error magnitude exactly 2); `2→3` admits shell 3. Measuring, on each **base** `k=1` cycle, the fraction of steps whose minimal shell is 2 or 3:

| archetype | mean shell-2 | mean shell-3 | reading |
|---|---|---|---|
| `2:1` P=9 (n=36) | **0.0000** | **0.0000** | **BLIND** |
| `2:1` P=36 (n=4) | 0.2222 | 0.0556 | perturbed, locked at both |
| `2:1` P=54 (n=12) | 0.0556 | 0.1667 | perturbed, breaks at `k=3` |
| `3:1` P=74 (n=12) | 0.1351 | 0.1892 | perturbed, breaks at `k=3` |

**The `P=9` archetype never visits shells 2 or 3 at all.** Its minimal-shell histogram is `{0: 6, 1: 3}` — the orbit lives entirely inside the `k=1` band. Widening the band therefore admits *no new edge*, and Q3 confirms the consequence: its word is byte-identical at `k = 1, 2, 3` (`SSPSSPSSP` throughout). This archetype is not robust under the deformation; it is **invisible to it**.

Across the census the exposure hypothesis holds directionally: 56.2% of eligible seeds have zero shell-2 exposure versus 16.5% of a 400-seed non-eligible sample (mean shell-2 exposure 0.050 vs 0.127). Low shell-2 exposure strongly predicts surviving `1→2` — but it is not necessary, since three of the four archetypes are perturbed and survive anyway.

## 3. Q3 — the internal control, class held fixed

| | `k=1` | `k=2` | `k=3` |
|---|---|---|---|
| `2:1` P=9 | `SSPSSPSSP` | **identical** | **identical** |
| `2:1` P=36 | `P...S...S...P.S..S..S.P…` | **word changes**, class `2:1` | **word changes**, class `2:1` |
| `2:1` P=54 | `(..SS.......PSSPSSP)^3` | **word changes**, class `2:1` | period `54 → 360`, class → `7:10` |

This separates class identity from orbit architecture cleanly. Three distinct regimes sit inside the single label `2:1`:

1. **Blind** (P=9) — the deformation does nothing; persistence is vacuous.
2. **Compensating** (P=36) — the word genuinely changes at both `k=2` and `k=3`, yet the reduced class is invariant. Real robustness, and the only one of the three that is a candidate for *structural* stability of the label.
3. **Compensating then destructive** (P=54) — absorbs the shell-2 perturbation, but the shell-3 perturbation restructures the orbit entirely (period ×6.7) and the class breaks. This is the DISC-1D pass.

So the shell-2/shell-3 asymmetry the PI proposed is confirmed in the passing archetypes: **shell-2 perturbation compensated, shell-3 perturbation destructive.**

## 4. Retrospective validation of the frozen criterion

**36 of the 64 stability-fence survivors — more than half — are the blind archetype.** They pass stability trivially because the deformation never touches their orbit. The frozen contingency requirement is the only thing that removed them, and had DISC-1D required stability alone, these 36 would have been admitted on the strength of an orbit that does not respond to the deformation at all.

This is the two-sided criterion doing exactly the work it was designed for, and it is worth recording as an empirical vindication of the round in which contingency was added.

## 5. Hypotheses generated (for a future pre-registered campaign, not for use here)

- **H-A.** Survival of `1→2` is governed by *shell-2 exposure of the base orbit*, not by class arithmetic. `2:1` and `3:1` dominate because their orbit architectures happen to be low-exposure, not because those numerals are special.
- **H-B.** Blindness is a checkable structural property (orbit confined to shells `≤ k`), so a future axis should report blind-versus-compensating separately, since blind seeds cannot contribute contingency by construction.
- **H-C.** A deformation axis that raises shell exposure without changing the sector — rather than one that widens the band — might admit classes beyond `{2,3}`. This is a suggestion for axis design and is explicitly **not** a proposal to test several axes and select one.

## 6. Guards

Exploratory throughout. No admission rule, threshold, axis, or verdict is changed. `{2,3} ⊆ Q^dyn` and `Q^dyn ≠ ∅` stand exactly as ratified; no exhaustiveness is implied or approached. Nothing here touches SG-NG-19/23/24, C7C, or the continuous branch.
