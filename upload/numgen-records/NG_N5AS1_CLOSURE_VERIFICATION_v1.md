# N-5A-S1 Closure — Independent Verification, Slip-Count Corollary, and Riemann-Lens Merge

**Memo ID:** `NG_N5AS1_CLOSURE_VERIFICATION_v1` · **RID:** `NUMGEN-OPEN-N5AS1-INF` (verification), `NUMGEN-CAND-N5AS1-LOGSLIP` (upgrade)
**Canonical base:** `RTG_NUMBER_GENESIS_DSN_v1.11` (sha256 `3782244f…cb421`, **verified**)
**Date:** 2026-08-28 · **Auditor:** Claude
**Artifacts:** `ng_n5as1_closure_verification_v1.py` / `.log`
**Verdict:** closure **CONFIRMED independently**, with one cross-check the original certificate did not make. Two consequences follow that the closure implies but does not state.

---

## 1. Independent verification

The uploaded certificate reruns clean, and I re-derived every exact assertion from scratch with an independent expansion routine:

| Claim | Verified |
|---|---|
| `F = T⁶` has no quadratic term in primitive coordinates | ✓ |
| cubic jet `Δρ₃ = (8η − 7ρ)Q/6` | ✓ |
| cubic jet `Δη₃ = (η − 8ρ)Q/6` | ✓ |
| `W(Fx) = W + (−½ − iτ)W|W|² + O(|W|⁴)`, `τ = 2√3/3` | ✓ |
| quartic angular ray coefficient `= −25√3/48 ≠ 0` | ✓ |
| one-step primitive linearization is `+π/3` rotation in `W` | ✓ |

**Additional cross-check, not present in the original certificate.** The claimed cubic jet, contracted against `∇Q`, induces at degree 4

```
ΔQ = (2ρ−η)·Δρ₃ + (2η−ρ)·Δη₃ = (Q/6)·(−6Q) = −Q²
```

**exactly** — independently reproducing the certified L1 radial law from an expansion computed for an entirely different purpose. This is the strongest single validation available: two independently derived objects (the L1 contraction law and the six-step angular jet) agree with no free parameters. Relatedly, `Re(c₂₁) = −½` is *forced*, since `Δ|W|² = 2Re(c₂₁)|W|⁴` must equal `−Q²`. The `c₂₁` real part is therefore not an independent measurement but a consistency requirement — worth recording, as it means only `Im(c₂₁) = −τ` carries new information.

**The `O(Q²)` rejection is now theorem-grade and I concur.** The nonvanishing quartic ray coefficient makes a uniform `O(Q²)` post-leading remainder false by exact Taylor algebra, not merely unsupported numerically. My earlier numerical rejection is superseded by the algebraic one. I also computed the supremum over directions of `|Im(ΔW₄/W)|/Q^{3/2}`, obtaining **1.4003**, against my measured orbit values 1.3565 → 1.3449 (decreasing as `Q → 0`). Measured sits below the directional supremum, as it must, since an orbit samples directions non-uniformly. Consistent.

## 2. One audit note on L-MONO — sufficient, but with zero margin

The six-step lift determination needs the total increment to select the correct `2π` branch. With the stated bracket `π/6 < Δφ_T < π/2`, six steps give a total in `(π, 3π)` — an open interval of length **exactly** `2π`, which does contain exactly one representative of each residue class. So the argument is **valid as stated**. But it is valid with no margin at all: the whole determination rests on an interval whose width is precisely the period.

The sharper estimate is already in hand in §3 of the closure memo — from `W(Tx)/W = λ + O(|W|)` one gets

```
Δφ_T = π/3 + O(Q^{1/2}).
```

I verified the exponent: `max|Δφ_T − π/3|` divided by `√Q` is stable at ≈ 0.393 across a 64-fold range of `Q`, while divided by `Q` it diverges (22.8 → 45.3 → 90.3 → 180.2). So the deviation is genuinely half-power, and six steps give `2π + O(√Q)` — comfortably inside `(π, 3π)` with room to spare.

**Recommendation:** promote `Δφ_T = π/3 + O(Q^{1/2})` into the statement of L-MONO, retaining `(π/6, π/2)` as its corollary. No result changes; the branch determination stops depending on an exactly-critical interval width.

## 3. New corollary — the slip-count law, and the exponential rate becomes theorem-grade

The closure proves `N_B(M) = M − (τ/2π)·log M + O(1)`. It does not draw out what this says about the *slips themselves*. Counting primitive steps two ways: in `6M` primitive steps with `N_B` events of which `s` are 7-gaps and the rest 6-gaps,

```
6M = 6·N_B(M) + s(M)   ⟹   s(M) = 6(M − N_B(M)) = 3·D_M/π.
```

Hence, using `D_M = τ log M + C_D + o(1)`:

```
s(M) = (3τ/π)·log M + O(1).
```

**Numerical confirmation** against the observed slips (with `κ = 1/Q₀`):

| primitive steps | predicted `s` | observed |
|---|---|---|
| 33 229 | 0.387 | 1 |
| 198 242 | 1.385 | 2 |
| 606 981 | 2.384 | 3 |
| 1 619 416 | 3.384 | 4 |
| 4 000 000 | 4.350 | 4 |

The successive predicted differences are 0.998, 0.999, 1.000 — the law tracks each individual slip to three digits, with a constant offset ≈ 0.615.

**Consequence for the geometric spacing law.** Solving `s(M_k) = k` gives `log M_k = (π/3τ)·k + O(1)`, hence

```
(1/k)·log M_k  →  π/(3τ) = √3π/6.
```

So the **exponential slip rate `exp(√3π/6) = 2.476632271…` is now theorem-grade**, upgraded from `[CAND]/[NUM]` — it is a corollary of the closed INF-1/INF-2, not an independent conjecture. What is *not* yet proved is that the consecutive ratios `M_{k+1}/M_k` converge to that value; that requires the `O(1)` term to converge rather than merely stay bounded. Numerically it appears to converge (differences 0.998 → 1.000), and the observed ratios 2.4710 → 2.4746 → 2.4760 do approach 2.4766, but this remains open.

**Suggested registration:** `NUMGEN-CAND-N5AS1-LOGSLIP` splits into (a) `[RESULT][from: ALG]` slip-count law and exponential rate, and (b) `[OPEN]` convergence of the `O(1)` offset, which is the remaining content of the consecutive-ratio claim.

## 4. Riemann-lens merge

The lens findings (relayed separately to the Dyadic owner) now interlock with the closure:

- `Q_true` is the **unique** `J`-invariant quadratic form up to scale — the Eisenstein/hexagonal norm form of `λ = exp(±iπ/3)`. `Q_euclid` is not invariant (defect `ρ(ρ−2η)`), so the Dyadic SG-1 primacy policy is forced rather than conventional.
- With Gram matrix `g = [[1,−½],[−½,1]]`, `det g = 3/4`, and **`τ = 1/√(det g)`** exactly. The shear constant is the volume normalisation of that invariant form — which now, via §3, is *the* constant setting the slip rate.
- `F = T⁶` is tangent to the identity with cubic leading term — independently confirmed by the closure's own jet (no quadratic term, cubic nonzero). This is the classical **cubic parabolic germ** class, in which `|z_n| ~ n^{-1/2}`, matching `q_m ~ 1/m`.

**The Fatou-coordinate question is sharpened, not retired.** L-PHASE no longer needs it — the direct exact-jet proof is cleaner. But the parabolic Fatou coordinate carries a logarithmic term whose coefficient is the *iterative residue*, and our `D_M = τ log M + C_D + o(1)` is exactly such a term with `C_D` the constant in question. So the remaining open item in §3 — does the `O(1)` offset converge, and to what — is precisely the question of whether `C_D` is the Fatou-coordinate constant of `F`. That is now a well-posed, narrowly scoped target rather than a general appeal to the literature.

## 5. Guards, unchanged

1. SG-NG-23 remains fully active. This is a second certified stream, not a nontrivial commensurability class; the leading average is still 6 and the content is the unbounded logarithmic discrepancy.
2. `exp(√3π/6)` is now proved as a *rate*, which makes it more tempting and no more admissible as a genesis-grade `ℝ` premise: it is constructed inside the continuous chart and stays behind SG-NG-19 / OPEN-P0.
3. `Q_true`, `τ`, `c₂₁`, and the phase law remain Dyadic-owned; the §4 identifications are relayed upstream, not claimed here.
4. All closure arguments remain local/existential on a sufficiently small tube under the OPEN-P0 generator ceiling; no explicit radius is claimed and the long seed orbits stay `[NUM]` witnesses.
