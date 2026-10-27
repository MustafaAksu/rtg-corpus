> **[SUPERSEDED 2026-09-02] This file is retained for lineage only. It contains the withdrawn causal phrase "basin/transient memory" and the unproved `class < spectrum < orbit < entry` hierarchy. The canonical record is `NG_DISC1_DIAG3_RESULT_v2.md`. Do not cite this file as current.**

# `[POSTHOC-DIAG]` Marked-Entry / Entry-Sufficiency / Transient-Necessity

> **`[POSTHOC-DIAG]` Hypothesis-generating only, on already observed DISC-1 data. No admission rule, threshold, deformation axis, or existing DISC-1 verdict is changed. Nothing here is C7B breadth evidence.**

**Memo ID:** `NG_DISC1_DIAG3_RESULT_v1` · **Date:** 2026-09-02
**Supersedes the causal claim in** `NG_DISC1_DIAG2_RESULT_v1` §2
**Outcome:** the **stronger** of the two pre-declared branches — even the *marked* entry state is insufficient. Deformation fate retains basin/transient memory.

---

## 1. `[COR]` — the entry-point claim was unsupported

Diag2 v1 said "the distinguishing datum is the seed's entry point into the shared cycle." That was not established: the frozen experiment runs `F₂` from the **original seed**, not from the cycle-entry state, so differing preperiods showed realization dependence without identifying which discarded datum is causal. Likewise "no function of the `k=1` cycle" is corrected to **"no function of the *unmarked* eventual `k=1` cycle."** Both corrections adopted; the tests below were run precisely to settle what was asserted prematurely.

## 2. Results, in the ruled order (288 exposed seeds in the three admitted spectra; 28 COMP, 260 FAIL)

**Test 1 — marked entry: FAILS.** 212 distinct entry states; **4 carry both fates**. The marked first-entry state does *not* determine compensation.

**Test 2 — entry-state sufficiency: FAILS.** Running the same `F₂` from `e_x` itself reproduces the seed's fate in only **270/288** cases (93.8%). Every one of the 18 disagreements is a COMP seed whose entry state yields FAIL — e.g. `s_11_0_1_16` (COMP, preperiod 64) versus FAIL from its own entry state.

**Test 3 — transient necessity: CONFIRMED.** The 4 mixed-fate entry states separate cleanly by transient length:

```
entry (13, 0,16, 1):  COMP pre = 64, 62, 63   |  FAIL pre = 25, 23, 24
entry (11,11, 8, 7):  COMP pre = 38, 36       |  FAIL pre =  4,  2,  3, 1
entry (11,11, 8, 9):  COMP pre = 63, 64       |  FAIL pre = 24, 25, 23
```

Same entry state, same shared cycle, same conserved spectrum, same class — different `F₁` transients, different `F₂` fates.

## 3. The conclusion, stated at the supported strength

```
C₁(x) = C₁(y)  ⇏  C₂(x) = C₂(y)          (Diag2, confirmed)
e_x   = e_y    ⇏  fate(x) = fate(y)      (Test 1, new)
F₂ from e_x    ⇏  fate(x)                (Test 2, new)
```

So the missing datum is **not** a marked-cycle coordinate. It lies earlier, in the `F₁` transient or the basin position of the frozen seed. This is the branch you flagged as the stronger and more interesting one, and it makes the same-realization guard more load-bearing still: DISC-1D's insistence that admission attach to a *realization* is not conservatism about labels or orbits — it is tracking information that provably survives no coarser quotient tested here.

**H-E `[POSTHOC-HYP]`, revised as ruled and now sharpened:** compensation is not a function of the reduced class, the conserved spectrum, the unmarked eventual `k=1` orbit, **or the marked first-entry state**. It depends on realization information discarded by all of these.

## 4. One observation, reported and explicitly not promoted

Within Test 3's declared scope (transient information), longer `k=1` preperiods associate with compensation: COMP median preperiod 37.5 against FAIL median 0. Per spectrum, `{0,1,9}` separates perfectly — COMP preperiods `{59…64}`, FAIL range `[0,40]`, no shared value — while `{0,1,8}` shares 4 values and `{0,1,18}` has all preperiods 0 with both fates present.

**This is not a separator and must not be used as one.** It fails outright in `{0,1,18}`, where every seed has preperiod 0 and fates still differ. It is reported because it indicates *where* the missing information lives — in the transient — not what it is. Preperiod length is a coarse summary of the transient, and the `{0,1,18}` counterexample shows the relevant content is the transient's structure rather than its length.

## 5. Consequences for C7B-DISC-2

- The candidate `Δ_AC → Δ_AC + h` stays named a **seed-phase perturbation candidate**, per your ruling. Calling it an "entry-point perturbation" is now positively wrong: entry point is proved insufficient.
- The revised hierarchy: `class < spectrum < unmarked eventual orbit < marked entry < ` **still-unidentified realization information**. Four levels of quotient are now excluded.
- A design implication worth weighing before any freeze: if fate depends on transient/basin information, then any axis will produce results that are seed-specific in a way no orbit-level or entry-level summary can predict. That argues for reporting full per-seed transport on future campaigns rather than any aggregated orbit statistic — and it raises the question of whether `Q^dyn` breadth is a well-posed *structural* target at all, or only ever a statement about realizations. That is interpretive and PI-blocked.

## 6. Guards

No feature outside the frozen family and the ruled Test 1–3 hierarchy was introduced; preperiod falls inside Test 3's declared transient scope and is reported, not used. Ratified results untouched.
