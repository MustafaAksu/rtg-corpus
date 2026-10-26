# DISC-1D Audit Item 3 — Is the Stability Fence Selecting Short Cycles or Robust Dynamics?

**Memo ID:** `NG_DISC1_AUDIT_ITEM3_v1` · **Date:** 2026-09-01
**Audits:** `NG_DISC1_RESULT_v1` §4 item 3 · **Input:** `bind3_disc1_enumeration_k0123.json`
**Verdict:** the confound is **real but does not explain the result.** Class simplicity predicts survival *independently* of cycle length, and all 22 passes exhibit non-trivial ratio-persistence.

---

## 1. The worry, restated

Reduced-class complexity `a + b` is loosely bounded by cycle period, so if the `1→2` stability fence merely selected short cycles it would automatically select simple classes, and the admissions `2:1`, `3:1` would be an artifact rather than a fact about the dynamics.

## 2. The confound is real

Eligibility is strongly length-dependent. Eligible seeds have median `k=1` cycle length **9** (range 9–74); non-eligible, median **162** (range 14–1638). Eligibility rate by band:

| `k=1` cycle length | eligible / base |
|---|---|
| [0, 20) | 36 / 226 = **15.9%** |
| [20, 60) | 16 / 713 = 2.2% |
| [60, 150) | 12 / 618 = 1.9% |
| [150, 400) | 0 / 1020 = **0.0%** |
| [400, 2000) | 0 / 676 = **0.0%** |

Nothing above period 150 survives. So the fence does strongly favour short cycles, and the worry was well-placed.

## 3. But length and complexity are not collinear, so the test separates

Complex classes occur abundantly at short cycle length: in the `< 150` band there are **1289** seeds with `a+b > 4` alongside 268 with `a+b ≤ 4`. Restricting to that band — the only region where anything survives at all — removes length as an explanation:

| within `k=1` period < 150 | eligible |
|---|---|
| simple classes `a+b ≤ 4` | 64 / 268 = **23.9%** |
| complex classes `a+b > 4` | **0 / 1289 = 0.0%** |

Zero of 1289 short-cycle complex-class seeds survive the elementary move, against 24% of comparable simple-class seeds. Class simplicity therefore predicts survival **independently of cycle length**. The hypothesis "the fence is just picking short cycles" is falsified: short cycles are necessary but nowhere near sufficient.

## 4. Persistence is not trivial cycle-identity

The second degenerate reading — that `r_{x,2} = r_{x,1}` because the deformation left the orbit untouched — is also falsified. **0 of 22** passing seeds have identical `(n_swap, n_p3)` at `k=1` and `k=2`; all 22 preserve the *ratio* while the *counts change*:

```
s_11_7_1_16 : (18,9) len 54  →  (16,8) len 54  →  (84,120) len 360
s_11_3_1_17 : (18,6) len 74  →  (12,4) len 33  →  (120,72) len 339
```

The `k=2` cycle is a genuinely different cycle — different event counts, and in the second case a different period — that nonetheless carries the same reduced class, before `k=3` destroys it. That is precisely the "locally robust yet dynamically contingent" shape `Q^dyn` was defined to capture, rather than an orbit that simply failed to notice the deformation.

Across all 64 eligible seeds, 28 achieve the same ratio via different counts and 12 have a different period at `k=2`, so non-trivial persistence is not confined to the passing subset.

## 5. Residual reading, offered honestly

What survives is a real dependence on class simplicity that is *not* reducible to period. Two interpretations remain open and this test does not separate them: simple classes may be genuinely more robust under band widening, or the `n:1` family may occupy a structurally distinguished position (a single P₃ event per `n` swaps) that makes it special for reasons other than robustness. The second would still be a fact about the dynamics rather than about predicate multiplicity, so neither reading reinstates the artifact worry — but they differ in what `2, 3 ∈ Q^dyn` would *mean*, and that is interpretive and PI-blocked.

Audit item 4 — proving the absence of a common-source multiplicity factorization for SWAP versus active-P₃, which is SG-NG-26's actual discharge condition — remains untested.
