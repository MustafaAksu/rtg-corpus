# GAP-LOCK Lemma 3 — Proposed Closure via the Overshoot Recursion

**Memo ID:** `NG_GAPLOCK_LEMMA3_CLOSURE_v1` · **RID:** `NUMGEN-OPEN-N5AS1-GAPLOCK` item 3
**Base:** `RTG_NUMBER_GENESIS_DSN v1.15` · **Date:** 2026-09-01 · **Auditor:** Claude
**Artifacts:** `ng_gaplock_lemma3_cert_v1.py` / `.log` (5 rows, exit 0, 2×10⁷ primitive steps, 6 slips)
**Status:** proposed closure, **PI ruling required**. The `[ALG]` argument is §2–§4; the certificate decides only the stated facts.

---

## 1. The mechanism — the right object is the per-lap overshoot

Let `n_j` be the B-event steps and `o_j = φ(n_j) − 2πj` the overshoot. Six steps from an event supply `Λ₆ = 2π − Δ_j` with `Δ_j = τ q_j + O(q_j^{3/2})` (L-PHASE in its every-basepoint form, already certified for GAP-LOCK Lemma 1). Therefore the next lap completes in six steps iff the overshoot covers the deficit:

```
gap_{j+1} = 7   ⟺   o_j < Δ_j.
```

**This is exact, not asymptotic.** The criterion reproduces the realized gap at every one of 3 333 330 laps — 0 mismatches. Since `Δ ≈ 10⁻⁴` while `o` ranges over a cell of width `≈ π/3`, 7-gaps occur at rate `≈ 3τq/π` per lap, which integrates to exactly the certified `s(M) = (3τ/π) log M + O(1)`. The rate law and the locking mechanism are the same fact seen at two resolutions.

The overshoot recursion is then

```
gap 6:  o_{j+1} = o_j − Δ_j
gap 7:  o_{j+1} = o_j − Δ_j + δ_j ,    δ_j = π/3 + O(√q_j).
```

So `o_j` is a rotation-like sequence on a cell of width `≈ π/3` whose decrements tend to zero, and **7-gaps are in exact bijection with its crossings of 0**. This is precisely the "within-cell locking" the earlier framing left as an obstruction — the fractional part does not need to converge, because the *crossings* are what matter and their overshoot is squeezed into `[0, Δ_j)` with `Δ_j → 0`.

Measured: `sup|ε|/q^{3/2} = 1.726` on gap-6 laps (same half-power as L-PHASE), and on gap-7 laps `δ = π/3 + c√q` with `c ∈ [0.4330, 0.4332]` — apparently tending to `√3/4 = 0.43301`, offered as an observation, not claimed.

## 2. The bootstrap — why this is not circular

Set `α_k := D(M_k) − kπ/3`. The tempting argument uses `M_k ~ ρ^k` to make `Σ√q` summable, but that is the conclusion. The fix is a bootstrap:

1. `|δ_j − π/3| ≤ c√q_j ≤ c√q_1` and the overshoot at a slip lies in `[0, Δ)`, so **`α_k` is bounded**.
2. With `D_M = τ log M + C_D + o(1)` (INF-1, closed at v1.11), bounded `α` gives `log M_k = (π/3τ)k + O(1)`, hence **`M_k ≥ c ρ^k`**.
3. Therefore `q_{M_k} = O(ρ^{−k})` and `Σ_k √q_{M_k}` converges **geometrically**, so **`α_k` converges**.
4. Hence `log M_k = (π/3τ)k + const + o(1)`, and

```
M_{k+1} / M_k  →  exp(π/(3τ)) = exp(√3π/6) = 2.476632271…
```

Bounded → geometric growth → summable corrections → convergent offset. Each step uses only the previous one.

## 3. Numerical confirmation of every link

`α_k = −0.641961, −0.645207, −0.647303, −0.648622, −0.649464, −0.649997` — bounded and monotone, with increments decaying at rates `0.646, 0.629, 0.639, 0.633` against the predicted `ρ^{−1/2} = exp(−√3π/12) = 0.6354`. Partial sum of `|increments|` = 0.008. Consecutive physical slip ratios: `2.471014, 2.474584, 2.476007, 2.476487, 2.476651` against `2.476632271`.

Slips at primitive steps 33229, 198242, 606981, 1619416, **4127027**, **10337784** — the last two are new, beyond the previously audited horizon.

## 4. What this closes

If ratified: **GAP-LOCK Lemma 3 CLOSED**, hence GAP-LOCK complete, hence the **physical consecutive-slip ratio limit** promoted from `[NUM]` to theorem-grade. The v1.12.1 split between the defect-threshold ratio theorem and the physical ratio then collapses — they agree, and the physical statement no longer trails the threshold one.

## 5. Guards

1. The argument consumes L-PHASE (every-basepoint), L-BACKBONE, and INF-1, all closed. It adds the overshoot recursion and the bootstrap. I have not re-derived the inputs.
2. `[NUM]` in the above: the exactness of L3-1 over the sampled horizon, the constants 1.726 and `√3/4`, and the observed ratios. The `[ALG]` content is §2, which needs only *boundedness* of `δ − π/3` in `O(√q)` — a consequence of the certified per-step expansion `Δφ_T = π/3 + O(Q^{1/2})` promoted at v1.12.1.
3. Scope unchanged: local tube, selected generator, OPEN-P0 ceiling. `exp(√3π/6)` remains a chart-derived constant behind SG-NG-19 and does **not** become a genesis-grade `ℝ` premise; SG-NG-23 and SG-NG-24 are untouched.
4. Nothing here bears on `Q^dyn` or the discrete branch.

## 6. Open

Whether `C_D` — and now also `α_∞ ≈ −0.6509` — admit closed forms, and whether they are the canonically normalised Fatou/iterative-residue constants of `F = T⁶`. That was the original framing of Lemma 3; the present argument closes the lemma **without** needing it, which leaves the Fatou question as a genuine but now optional refinement.
