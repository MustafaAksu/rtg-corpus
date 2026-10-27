# DISC-1B / DISC-1D Result — First Run on the Frozen Panel

**Memo ID:** `NG_DISC1_RESULT_v1` · **Date:** 2026-09-01
**Inputs:** `bind3_disc1_enumeration_k0123.json` (13824 records) via the frozen `disc1_analysis_harness_v1.py`
**Artifacts:** `bind3_enumerate_k0123_v1.py`, enumeration JSON, `disc1_result.json`
**Verdict:** **DISC-1B PASS · DISC-1D PASS.** Candidate admissions: `2 ∈ Q^dyn`, `3 ∈ Q^dyn`. **Not yet PI-ratified** — audit items in §4.

---

## 1. Prerequisites discharged before any data was generated

- `BIND3-CYCLE-N24K1` reproduced **exactly** (`bind3_repro_v5.py`, exit 0): median 138, max 1638, 79 distinct, preperiod 0/830, K₃ 0, all six dominant periods, taxonomy 124/3332.
- The reproduced core is **one-step identical to `genesis_mode_b_mc_v18.py` across all 331776 reduced states for every `k ∈ {0,1,2,3}`** — 0 mismatches. This was run *before* the enumeration, per the PI's provenance safeguard, and removes the residual risk that exact `k=1` aggregates could coexist with divergence at other `k`.
- Frozen engineering constraints honoured: one panel of 3456 raw `k=1` seeds reused at every `k`; cycle-only counts after the preperiod; `dual_active` records retained when false; `seed_id` tied to the raw reduced state; **no bond-transfer classification computed or exported**.

## 2. DISC-1B — PASS

Base `k=1` dual-active seeds: **3253 / 3456**. Non-`1` classes: **3253** (every dual-active base cycle carries a non-`1` reduced class). Most frequent: `3:1` (178), `2:1` (144), `35:3` (142), `4:1` (134), `78:17` (112). The original v1.15 falsifier — all dual-active cycles reduce to `1:1` — does not fire.

## 3. DISC-1D — PASS

| | |
|---|---|
| dual-active by `k` | 0 → 156, 1 → 3253, 2 → 3141, 3 → 2857 |
| eligible after the `1→2` stability fence | **64** |
| passing by interior contingency (`k=3`) | **22** |
| passing by boundary contingency only (`k=0`) | **0** |
| admitted classes | `2:1` × 12, `3:1` × 10 |

All 22 passes are `DISC-1D-PASS-INT`, the stronger subtype: contingency occurs within the positive-band regime, not through the zero-width boundary control. Representative transport tuples `(k=0,1,2,3)`:

```
s_11_0_1_16 : [None, (2,1), (2,1), (7,10)]
s_11_11_1_17: [None, (3,1), (3,1), (5,3)]
```

**Independent recount.** All 22 passing seeds were recounted at all four `k` by driving `v18.step_universe` directly and reading v18's own `single_edge_swaps` / `path_interactions` counters: **0 mismatches** against my enumeration. The result therefore does not depend on my counting logic, only on the frozen pass rule.

## 4. Audit items before ratification — I do not recommend accepting this yet

A positive result on the first run is the case this architecture was built to distrust, so I flag rather than conclude:

1. **The `k=0` column is degenerate.** Only 156/3456 seeds are dual-active at `k=0`, and **no** passing seed is dual-active there (`None` in every transport tuple). The boundary control contributed nothing, exactly as the zero-width-stratum ruling anticipated. Worth recording as a confirmed prediction, but it also means contingency rests entirely on `k=3`.
2. **The eligibility funnel is very narrow** — 64 of 3253, about 2%. Nearly every base class is destroyed by the elementary `1→2` move. That is a fact about the deformation family and should be reported alongside the pass: the stability half of the criterion is close to failing globally.
3. **Only two classes are admitted, both of form `n:1`.** With `78:17`, `35:3`, `39:11` present in the base census, the survivors are conspicuously the simplest ratios. This may be real — simple classes plausibly have larger basins and more robust cycles — or it may indicate the stability fence selects for short cycles rather than for dynamical robustness. I have not tested which.
4. **SG-NG-26 does not obviously apply** — SWAP and active-P₃ are distinct native mechanisms, not ray families of one monotone lift — but I have not *proved* the absence of a common-source multiplicity factorization, which is the guard's actual discharge condition.

## 5. Recommendation

Record as **candidate** `2, 3 ∈ Q^dyn` pending PI ruling on §4, in particular items 3 and 4. The frozen rules were followed exactly and nothing was tuned; what is unclear is whether the pass carries the physical content `Q^dyn` was defined to capture, which is an interpretive call and PI-blocked.

Note this is the outcome the architecture treats as strongest: `PASS/PASS` with interior contingency, arrived at through a pre-registered rule with frozen analysis code, an exhaustively verified transition core, and an independent recount through the owner's own counters.
