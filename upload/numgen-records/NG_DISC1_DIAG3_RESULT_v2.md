> **[SUPERSEDED 2026-09-03] Retained for lineage only. Contains the withdrawn causal phrase "transient necessity" and asserts four mixed-fate entry states while displaying three. Canonical record: `NG_DISC1_DIAG3_RESULT_v3.md`. Do not cite as current.**

# `[POSTHOC-DIAG]` Marked-Entry / Entry-Sufficiency / Transient-Necessity

> **`[POSTHOC-DIAG]` Hypothesis-generating only, on already observed DISC-1 data. No admission rule, threshold, deformation axis, or existing DISC-1 verdict is changed. Nothing here is C7B breadth evidence.**

**Memo ID:** `NG_DISC1_DIAG3_RESULT_v2` · supersedes `_v1` · **Date:** 2026-09-02
**Supersedes the causal claim in** `NG_DISC1_DIAG2_RESULT_v1` §2
**Outcome:** the **stronger** of the two pre-declared branches — even the *marked* entry state is insufficient.

**`[COR]` v2, two precision corrections.** (i) v1 said deformation fate "retains basin/transient memory." That imputes a causal channel that does not exist: `F₁` and `F₂` both start independently from the original seed `x`, so `F₂` neither remembers nor traverses the `F₁` transient. The transient is *evidence about where `x` sits in the `F₁` basin*, not history supplied to `F₂`. Replaced throughout by **pre-entry realization information** / seed-basin information not retained by the tested summaries. (ii) v1's `class < spectrum < orbit < entry` notation asserted a nested refinement chain that was never proved; replaced by a flat list of tested-insufficient summaries.

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

The strongest supported formulation:

```
fate₂(x) depends on original-realization information
not recoverable from C₁(x) or e(x).
```

**Tested insufficient summaries** (a flat list, not a chain — no refinement order is claimed): reduced class; conserved advance spectrum; unmarked eventual `k=1` orbit; marked first-entry state.

This makes the same-realization guard more load-bearing still: DISC-1D's insistence that admission attach to a *realization* is not conservatism about labels or orbits — it tracks information that survives none of the coarser summaries tested here.

**H-E `[POSTHOC-HYP]`, revised:** compensation is not a function of the reduced class, the conserved spectrum, the unmarked eventual `k=1` orbit, **or the marked first-entry state**. It depends on pre-entry realization information discarded by all of these.

## 4. One observation, reported and explicitly not promoted

Within Test 3's declared scope (transient information), longer `k=1` preperiods associate with compensation: COMP median preperiod 37.5 against FAIL median 0. Per spectrum, `{0,1,9}` separates perfectly — COMP preperiods `{59…64}`, FAIL range `[0,40]`, no shared value — while `{0,1,8}` shares 4 values and `{0,1,18}` has all preperiods 0 with both fates present.

**This is not a separator and must not be used as one.** It fails outright in `{0,1,18}`, where every seed has preperiod 0 and fates still differ. It is reported as a further *indication* that the discriminating information is pre-entry — preperiod being one coarse read-out of basin position — not as a claim that transient length is the operative variable.

## 5. Consequences for C7B-DISC-2

- The candidate `Δ_AC → Δ_AC + h` stays named a **seed-phase perturbation candidate**, per your ruling. Calling it an "entry-point perturbation" is now positively wrong: entry point is proved insufficient.
- **Tested insufficient summaries** (flat list; no refinement order is claimed among them): reduced class; conserved advance spectrum; unmarked eventual `k=1` orbit; marked first-entry state. Each is excluded by an explicit counterexample above.
- **Witness-relation clarification (PI ruling, registered here as documentation).** `Q^dyn` is **not** redefined and C7B breadth remains well-posed exactly as written. Membership was always existential *through a realization*, never universal over a label, spectrum, orbit or basin. The object underneath is a witness relation

```
W_dyn = { (r, x, A) : x is a certified realization carrying r that passes
                      the preregistered dynamic gate on axis A }
Q^dyn = π_r(W_dyn)
```

so the spectrum is the label projection of the witness records. Two questions previously conflated verbally are now separated: **label breadth** — which `r` have at least one certified dynamic witness (this is C7B, fully meaningful) — and **realization robustness** — how large or structured the witness fibre `W_dyn(r)` is. No canonical measure, equivalence or basin notion exists for the second, so **no `Q^dyn_rob` is invented here**; doing so post-data would make "robust" an adjustable threshold. This also answers my v1 §5 question: `Q^dyn` never claimed to be a universal structural property of a numeral, and Diag3 is the dynamical analogue of the C7A caution against confusing equal rational labels with physically identical pairs.
- **Provenance requirement for future campaigns.** Every C7B campaign must retain witness-level provenance: frozen seed ID, base class, axis and deformation points, dual-activity status, base/stability/contingency counts and periods, pass subtype, and enough trajectory provenance to reconstruct each witness. The label set is a projection of those records, not the primary datum. This does **not** require predicting pass/fail from a structural classifier — DISC-1 never demanded predictability, only a preregistered same-realization stability-plus-contingency test, and realization-sensitivity makes that guard more appropriate, not less.

## 6. Central methodological result

> `[POSTHOC-DIAG]` The DISC-1 dynamic-pass predicate is genuinely realization-sensitive on the frozen panel. It does not factor through reduced class, conserved advance spectrum, unmarked `k=1` eventual cycle, or marked first-entry state. Therefore future C7B campaigns must preserve witness-level provenance; label breadth remains the existential projection prescribed by the existing definition.

## 7. Guards

No feature outside the frozen family and the ruled Test 1–3 hierarchy was introduced; preperiod falls inside Test 3's declared transient scope and is reported, not used. Ratified results untouched.
