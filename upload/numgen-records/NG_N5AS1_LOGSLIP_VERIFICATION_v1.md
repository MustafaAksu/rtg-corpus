# N-5A-S1 LOGSLIP — Independent Verification and Quantitative Law

**Memo ID:** `NG_N5AS1_LOGSLIP_VERIFICATION_v1` · **RID:** `NUMGEN-CAND-N5AS1-LOGSLIP`
**Date:** 2026-08-28 · **Auditor:** Claude
**Verifies:** `NG_N5AS1_LONG_HORIZON_CORRECTION_v1` / DSN v1.7.1
**Artifacts:** `ng_n5as1_logslip_verification_v1.py` / `.log`
**Verdict:** correction **CONFIRMED independently**; my v1.7 obstruction was wrong; the LOGSLIP mechanism is now **quantitatively confirmed** and supports an ALG argument for infinitude.

---

## 1. Independent confirmation of the correction

Reimplemented with a **different crossing detector** (lap counting via `floor(φ/2π)` transitions rather than floor-arithmetic on the interval endpoints), independent unwrapping, mpmath dps=60. Result: gap histogram over 40 000 steps is `{6: 6664, 7: 1}`, first non-6 return at primitive step **33229**, with `Q_true = 5.34427576108541615961×10⁻⁵ < Q₀ = 7.6×10⁻⁵`. Identical to the correction memo. The PI's script also reproduces on rerun (Stage A and Stage B assertions pass).

**My v1.7 error stands corrected.** The claim "exactly rational *limiting* rotation number ⟹ every transverse section has constant gap" is invalid: a limiting rational rotation is not a rigid rational rotation, and the residual nonlinear shear is not summable. I inferred asymptotic structure from a 240-step horizon — three orders of magnitude short of the first slip. The `[FAIL]` verdict and `NUMGEN-ART-ROTNUM-OBSTRUCTION` are correctly retracted. Recorded as `[COR]` against my own entry.

## 2. The LOGSLIP mechanism is quantitatively predictive

The owner mechanism gives per-block defect `ΔΘ = −τQ_m + O(Q_m²)`, `τ = 2√3/3`, with `Q_m ~ 1/(m+κ)`. A section crossing is delayed by one primitive step each time the accumulated defect advances by the per-step angle `π/3`. Since

```
Σ_{m≤M} τ Q_m ≈ τ ln((M+κ)/κ),
```

slips must occur at **geometrically spaced** times: with `M_k` the k-th slip in block units,

```
(M_k + κ) / (M_{k−1} + κ)  →  ρ := exp(π/(3τ)) = 2.4766…
```

**Pre-registered before the run, then tested** over 4×10⁶ primitive steps (float64, validated against the dps=60 first slip):

| k | primitive step | gap | `M+κ` (blocks) | observed ratio | `1/Q` at slip |
|---|---|---|---|---|---|
| 1 | 33 229 | 7 | 18 696 | — | 18 643 |
| 2 | 198 242 | 7 | 46 198 | 2.4710 | 46 165 |
| 3 | 606 981 | 7 | 114 321 | 2.4746 | 114 319 |
| 4 | 1 619 416 | 7 | 283 061 | 2.4760 | 283 106 |

Observed ratios converge monotonically to the predicted **2.4766**. The `1/Q` column independently confirms `Q_m ≈ 1/(m+κ)` at each slip.

**Second, independent confirmation from the section sweep.** The twelve sections split into two clusters (even sections ≈ 33.2k, odd ≈ 97.5k) because the per-step angle is `π/3 = 60°` while the sections are spaced `30°` — the odd sections sit exactly half a step in phase, so they should slip at **half a log-period**, i.e. ratio `√ρ = 1.5737`. Observed: **1.5729**. This structure was not designed into the sweep; it falls out of the mechanism.

The mechanism is therefore no longer merely plausible — it is a **falsifiable quantitative law that passed two independent tests**.

## 3. Gate 2 (repeatability): an ALG argument is now available

The PI's requested theorem follows from the same estimate. Since `Σ τ Q_m ~ τ ln M → ∞` diverges while `Σ O(Q_m²)` converges, the accumulated angular defect is **unbounded**. Every threshold `kπ/3` is therefore crossed at some finite time, giving **infinitely many non-6 returns**. Two lemmas are needed for theorem grade: (i) the owner asymptotic `Q_m = 1/(m+κ) + o(1/m)` with uniform control, and (ii) a bridge from the six-step block-phase law to the primitive section-return word (the PI's step-5 bridge). Both are stated, neither is hand-waved here. Status remains `[CAND]`; promotion to `[ALG]` is one focused module away, and I'd propose registering it as **N-5A-S1-INF**.

## 4. A caution the survival of gate 5 does not remove

Gate 5 asks whether `B = T^m` for a **fixed** `m`. It does not, and the candidate passes. But the density of slips is `O(log M)` against `M` blocks, so the asymptotic stream ratio is

```
steps per crossing  =  6 + O(log M / M)  →  6 exactly.
```

Numerically: 6.0000623 at `10⁴` blocks, 6.0000048 at `10⁶`, 6.000000012 at `10⁹`. So `B` is **not a fixed relabeling of `T⁶`**, yet its limiting ratio to the primitive stream is still the rational number 6. This is a genuine new distinction that N-5 must respect:

> `[GUARD proposal]` **Non-relabeling ≠ incommensurability.** Passing gate 5 shows a stream is not a fixed block of another. It does **not** establish that the pair carries a non-trivial commensurability class: a density/limit-based Q-like classification of this pair returns 6, and the entire physical content of the second stream lives in the *logarithmic correction*, not in the limit.

This is programme-relevant in two directions. Negatively, it warns that N-5 could close vacuously on this pair with the label 6 while the interesting structure is discarded. Positively, it suggests the right invariant for this pair may not be a ratio at all but the **slip-rate constant** `π/(3τ)` — equivalently the geometric ratio `ρ` — which is an irrational, generator-derived number that a commensurability classification would throw away. Whether `ρ` is an admissible RTG-native comparison invariant is a genuine question for N-5, and an interpretive one, so I register rather than answer it.

## 5. Verdict and consequences

- Correction **confirmed**; my v1.7 obstruction retracted; v1.7.1 accepted as canonical base.
- `NUMGEN-CAND-N5AS1-LOGSLIP` strengthened from qualitative candidate to **quantitatively confirmed law** (geometric slip spacing `ρ = 2.4766`, half-period section offset `√ρ`, `1/Q` tracking).
- Gate 2 has an ALG route via divergence of `Σ τQ_m`; proposed module **N-5A-S1-INF**.
- New `[GUARD proposal]`: non-relabeling ≠ incommensurability, with the slip-rate constant flagged as the candidate carrier of the physical content.
- N-4 is **not** a prerequisite for escaping `T⁶` re-blocking, as the correction states. Gates 1, 3, 4 remain open.
