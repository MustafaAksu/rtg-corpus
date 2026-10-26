# GAP-LOCK Lemma 3 — CLOSED by the Event-Time Defect Identity

**Memo ID:** `NG_GAPLOCK_LEMMA3_CLOSURE_v2` · supersedes `_v1` · **Date:** 2026-09-01
**Ruling:** PI, 2026-09-01 — **GAP-LOCK Lemma 3 CLOSED `[ALG]`**, by identity (2)–(6), **not** by the v1 bootstrap.
**Artifacts:** `ng_gaplock_lemma3_cert_v2.py` / `.log` (7 rows, finite facts only, exit 0)

---

## 1. `[COR]` — the v1 bootstrap is retracted as a proof

v1's Step 1 inferred boundedness of the **accumulated** offset `α_k` from a **per-slip** bound `|δ_j − π/3| = O(√q_j)`. That does not follow: a bounded per-slip error can accumulate over infinitely many slips, and excluding that needs `Σ_k √q_{M_k} < ∞` — precisely what Step 2–3 were meant to supply. **Circular at the first arrow.** The overshoot mechanism was right; the closing argument was not, and I presented a circular chain as a bootstrap.

Three further `[COR]`s against the v1 certificate, all accepted:

- **L3-1** tested the surrogate `o_j < τq_j` while the theorem uses the actual `Δ_j = 2π − Λ₆(x_j)`. Zero mismatches on a finite horizon does not promote a surrogate to an identity. v2 tests the true `Δ_j` (C2) and retains the surrogate as an explicitly labelled regression (C2b).
- **L3-3** reused the symbol `D` for `Σ τq_j` over laps, a different object from the owner's `D_M = 2πM − (φ̂_{6M} − φ̂_0)`. v2 uses `G_n` and states the block-boundary reduction explicitly (C3).
- **L3-4/L3-5** asserted geometric decay, summability and convergence from four finite ratios, and reported `(n+κ)`-shifted ratios as the observed physical ones. The **raw** physical ratios are `5.967, 3.062, 2.668, 2.549, 2.505`; the shifted sequence is a **backbone-shifted diagnostic**. Both are now reported, neither asserted to converge (C6).

## 2. The closure — exact, local, nothing accumulates

With `n_j` the B-event steps, `o_j` the overshoot, `s_j` the count of 7-gaps among the first `j` returns, and

```
G_n := (π/3)·n − (φ̂_n − φ̂_0),        G_{6M} = D_M
```

Lemma 1's `{6,7}` alphabet gives the exact `n_j = n_0 + 6j + s_j`, hence the **exact local identity**

```
G(n_j) = C + (π/3)·s_j − o_j.                                (2)
```

Because the alphabet is exactly `{6,7}`, the gap criterion is likewise exact: if the overshoot covers the six-step deficit the crossing has already occurred by step 6 (steps 1–5 excluded by Lemma 1), otherwise it is forced to step 7 —

```
g_{j+1} = 7  ⟺  o_j < Δ_j,     Δ_j := 2π − Λ₆(x_j) → 0.      (3)
```

So at the start of the `k`-th 7-gap, `0 ≤ o < Δ → 0` and `s = k−1`, giving `G = C + (k−1)π/3 + o(1)`. Returning to block time with `n = 6M_k + r_k`, `r_k ≤ 5`, and the promoted one-step estimate `Δφ_T = π/3 + O(Q^{1/2})`, the bracket is `O(√q_{M_k}) = o(1)`, so

```
D_{M_k} = C + (k−1)π/3 + o(1).                               (6)
```

With INF-1 (`D_M = τ log M + C_D + o(1)`, theorem-grade): `log M_k = (π/3τ)k + C* + o(1)`, hence

```
M_{k+1}/M_k → exp(π/(3τ)) = exp(√3π/6) = 2.476632271…
```

and since `n_k = 6M_k + O(1)`, the same limit holds in primitive steps. **No accumulated error appears anywhere** — (2) is an identity and (4) is a local bracket at each slip. That is exactly why the circularity disappears.

## 3. Certificate v2 — finite facts only

| row | content |
|---|---|
| C1 | identity (2) holds with a **single** constant `C = 0.4086378551` across all 3 333 330 events; spread `4.39e−9` against the float64 noise floor `4.65e−9` (ratio 0.94) |
| C2 | criterion (3) with the **true** `Δ_j`: 0 mismatches |
| C2b | v1 surrogate agrees on this horizon — labelled regression, not identity |
| C3 | `G_{6M} = D_M` by construction |
| C4 | at each of the 6 slips, `0 ≤ o_j < Δ_j` (values listed) |
| C5 | block remainders at slips are `[0,1,2,3,4,5]`, all `≤ 5` |
| C6 | raw and shifted ratio sequences, both reported, neither asserted to converge |

No row asserts convergence, summability, or any infinite implication; the closure argument lives entirely in §2.

`[COR]` on my own test design: C1 initially reported a spurious failure because I compared at 9 decimals a quantity of magnitude `~10⁷`, past float64 resolution. The tolerance is now tied to the ulp of the accumulated lift, and the row says so.

## 4. Consequences

**GAP-LOCK Lemmas 1–3 complete.** The physical consecutive 7-gap ratio is theorem-grade, closing the v1.12.1 distinction between the proved defect-threshold ratio and the then-open physical ratio — they now agree.

## 5. Guards

1. Local, selected-chart, continuous-branch theorem under the OPEN-P0 ceiling. `exp(√3π/6)` remains a chart-derived constant behind SG-NG-19 and is **not** a genesis-grade `ℝ` premise.
2. SG-NG-23 and SG-NG-24 untouched; no new `Q^dyn` element, no commensurability arithmetic, no bearing on the discrete branch.
3. The `√3/4` coefficient observed in v1 is **not used** and is withdrawn from the argument; nor is convergence of `α_k`.
4. The Fatou/`C_D` identification remains an optional refinement, never a GAP-LOCK blocker.
