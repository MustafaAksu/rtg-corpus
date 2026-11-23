# DYAD OPEN 21 (P5) — Primitive-variable phase remainder: proof record — v0.1.2

**Version:** v0.1.2 (supersedes v0.1.1 `5f82ef6c…a5fe4` and v0.1 `4410ad54…fd64`; changes in §6, §8; `[NUM]` orbit sampling in §7) · **Date:** 19 October 2026 · **Author:** Dyadic DSN owner (Claude)
**Status:** `[SESSION]` proof record with an exact-rational certificate. **Not adopted.** It is a candidate for `[THM — conditional on RECOG-THM-R9-MEMORY]` and needs independent review before any owner adoption. DYAD v6.4.16 is unchanged.
**Authorization:** PI decision of 19 Oct 2026 (`SCOPE REVIEW ACCEPTED — CERTIFICATION READY`). **Review of v0.1:** `REVIEW ACCEPTED WITH ONE CORRECTION — OWNER ADOPTION PENDING` (primary theorem accepted; correction of the secondary single-constant K_A applied in v0.1.1). **Review of v0.1.1:** `PRIMARY THEOREM ACCEPTED — MINOR CERTIFICATE HYGIENE FIX` (G-INV(a) upper-bound gate, applied in v0.1.2; `[NUM]` sampling approved with the corrected M_W estimator). Scope note: `DYAD_OPEN21_P5_PRIMITIVE_PHASE_SCOPE_SESSION_v0_1.md` (`a75994fd…cf07`).
**Statuses unchanged:** OPEN 21 OPEN, OPEN 3 CLOSED (defined scope), OPEN 20 PARTIAL. RECOG R9 is owned by RECOG and is not re-certified here.

## 1. Statement (candidate)

**Setting** (definitions exactly as in DYAD v6.4.16 §6.14):
- Rows j = A (|z| ≤ 1/20, C₇ = 100) and j = B (|z| ≤ 1/40, C₇ = 30). Rows are not mixed.
- Primitive start W₀ with 0 < |W₀| ≤ w_j := (15/16)r_j, that is |W₀| ≤ 3/64 (A) and |W₀| ≤ 3/128 (B). Q₀ = |W₀|².
- The target object is the adopted one:
  𝒫₂(W₀) = −Δ₁(W₀) + Q₀[c_iso + Λ₁(Θ_{W₀})] + P_{W2}(W₀), with P_{W2} = −Δ₂ + DΔ₁[h₂].

**Claim (primary, decomposed).** For every such W₀:

  |M_W − 𝒫₂(W₀)| ≤ K′_j·Q₀^{3/2} + C_{2,j}·(256/225)²·Q₀²

| Row | Primitive domain | K′_{j,exact} (majorant) | K′_j (published ceiling) | C_{2,j} (R9) | C_{2,j}(256/225)² (exact) | K′_j + C_{2,j}(256/225)²w_j (exact) | K_j (published ceiling) |
|---|---|---|---|---|---|---|---|
| A | \|W₀\| ≤ 3/64 (Q₀ ≤ 9/4096) | 3.95020… | **3951/1000** | 517 | 33882112/50625 ≈ 669.28 | 4768649/135000 ≈ 35.32333 | **8831/250 = 35.324** |
| B | \|W₀\| ≤ 3/128 (Q₀ ≤ 9/16384) | 3.88362… | **971/250** | 163 | 10682368/50625 ≈ 211.01 | 297997/33750 ≈ 8.82954 | **883/100** |

**Claim (secondary).** |M_W − 𝒫₂(W₀)| ≤ K_j·Q₀^{3/2}, where K_j is the published rational ceiling of the defining sum K′_j + C_{2,j}(256/225)²·w_j, built from the **published** K′_j. This uses Q₀^{1/2} ≤ w_j at the row's primitive-disk ceiling.

**Naming.** K′_{j,exact} is the exact rational majorant the certificate computes. K′_j is its published ceiling (third decimal, rounded up). Every published constant is checked exactly against its defining expression (gates G-SUM, G-SUM(single)).

**Reading of the constants.**
- K′ is the new P5 error. It is about 3.9, comparable to the P3/P4 constants.
- The C₂ term is inherited from R9's conservative C₂ and dominates the single K_j, especially on row A. Keeping the two parts separate stops them from mixing (reviewer decision, question 1).
- The constants are majorant suprema, not true-error maxima.

**Grade ceiling and conditions.**
- M_W exists only through T1, which is conditional on R9. The chart-variable memory law that is the starting point here is also conditional on R9. Hence the grade is at most `[THM — conditional on RECOG-THM-R9-MEMORY]`.
- **R9 is used at statement level only.** The source is RECOG v0.3.20 §6.13a–6.14: Λ₁, c_iso, C₂ = 517/163, q_max = 1/400 and 1/1600, and the C_z observable. RECOG's internal Arb certificate (K_Φ) and its proof record are not available in this review and are not used. No claim is made to re-certify R9.
- T1, T2 and the memory law keep their adopted grades.

## 2. Proof

### 2.1 Exact decomposition (gate G-ID, function level)

Define E through the adopted chart-variable memory law:

  M_W = −Δ₁(z₀) − Δ₂(z₀) + q₀[c_iso + Λ₁(Θ_{z₀})] + E, with |E| ≤ C₂q₀² + K₂q₀^{3/2} and z₀ = h⁻¹(W₀).

Subtracting 𝒫₂(W₀) gives the exact identity

  M_W − 𝒫₂ = E + T_{Δ1a} + T_{Δ1b} + T_{Δ2} + T_iso + T_{Λa} + T_{Λb},

where:
- T_{Δ1a} = −[Δ₁(z₀) − Δ₁(W₀) − DΔ₁(W₀)[z₀ − W₀]];
- T_{Δ1b} = −DΔ₁(W₀)[z₀ − W₀ + h₂(W₀)];
- T_{Δ2} = −[Δ₂(z₀) − Δ₂(W₀)];
- T_iso = c_iso(q₀ − Q₀);
- T_{Λa} = (q₀ − Q₀)Λ₁(Θ_{z₀});
- T_{Λb} = Q₀[Λ₁(Θ_{z₀}) − Λ₁(Θ_{W₀})].

**How the identity is checked.** It is verified symbolically on unknown values, using only the linearity of DΔ₁(W₀). This is the function-level check the reviewer required. The finite-order check (§2.6) is separate and does not replace it.

### 2.2 Domain (gate G-D)

Inputs from NF-INV:
- h⁻¹ exists on |W| ≤ 9/100 with values in |z| ≤ 1/10;
- (15/16)|z| ≤ |h(z)|;
- M(1/10)/(1/10) < 1/16.

Hence, with σ := (16/15)|W₀|:
- |z₀| ≤ σ ≤ r_j, so z₀ lies in the row disk. Also q₀ ≤ σ² ≤ r_j² = q_max, so R9's window holds.
- |z₀ − W₀| = |(h − id)(z₀)| ≤ M(σ) < |W₀|/15.
- Every ξ on the segment [W₀, z₀] has (14/15)|W₀| ≤ |ξ| ≤ σ ≤ 1/10.
- |g(z₀)| < 1/16 for g = (h − id)/z, so D_Θ(z₀) = Arg(W₀/z₀) is on the principal branch.

All these inequalities are checked exactly in rationals, per row.

### 2.3 Inverse-map remainder (gates G-INV(a), G-INV(b))

Since z₀ = W₀ − g̃(z₀), with g̃ := h − id = h₂ + g̃_{≥3}:

  z₀ − W₀ + h₂(W₀) = −[h₂(z₀) − h₂(W₀)] − g̃_{≥3}(z₀).

The two pieces are bounded as follows:
- ‖Dh₂(ξ)‖ ≤ 2(|c₂₀| + |c₁₁| + |c₀₂|)|ξ| = (7/6)|ξ|. The degree-2 moduli 1/6, 1/3, 1/12 are exact.
- |g̃_{≥3}(z)| ≤ M(|z|) − (7/12)|z|². This holds because each degree-k modulus sum of h (k = 3..6) is ≤ the M coefficient of degree k. That is checked with the certified rational **upper** bound (sum of `ub_abs`, with ub_abs(c)² ≥ |c|² gated for every coefficient), strictly and without tolerance: 0.07740 ≤ 39/500, 0.11119 ≤ 14/125, 0.04354 ≤ 11/250, 0.04939 ≤ 1/20. Also, h has no terms of degree above 6.

So M(s) − (7/12)s² is a genuine majorant of the degree ≥ 3 part only, as the reviewer required. It follows that

  |z₀ − W₀ + h₂(W₀)| ≤ c_inv(|W₀|)·|W₀|³, where c_inv(w) = [(7/6)σM(σ) + M_{≥3}(σ)]/w³.

c_inv(w) is a polynomial in w with **nonnegative rational coefficients**, which the gate checks exactly. It is therefore nondecreasing, and its supremum is attained at w_j:
- c_inv^A = 0.93347… (stated 467/500);
- c_inv^B = 0.92690… (stated 927/1000).

c_inv is not the OPEN 3 constant c₃ = 2/3.

### 2.4 Δ₁, Δ₂ derivative constants (gate G-D2)

**Δ₁.** In complex form, Δ₁(w) = Re(Aw) + Re(B w²/w̄), with A = 17√3/36 + i/12 and B = −7√3/72 − i/8; equality with the adopted harmonic form is checked exactly. |A|² = 73/108 and |B|² = 19/432. This gives:
- ‖DΔ₁‖ ≤ d₁ = |A| + 3|B|;
- ‖D²Δ₁(ξ)‖ ≤ d₂/|ξ| with d₂ = 8|B|, since the second derivative of w²/w̄ has norm at most 8/|w|.

**Δ₂.** In complex form, Δ₂ = k₀|w|² + Re(B₂w²) + Re(B₄w³/w̄) + Re(B₆w⁴/w̄²), again checked exactly against the adopted form. This gives ‖DΔ₂(ξ)‖ ≤ e₁|ξ| with e₁ = 2k₀ + 2|B₂| + 4|B₄| + 6|B₆|.

**Target object.** The gate checks that the implemented −Δ₂ + DΔ₁[h₂] equals the adopted P_{W2} (6 rational points, 50 digits). So 𝒫₂ is exactly the adopted object.

All irrational moduli are replaced by rational ceilings of exact squares.

### 2.5 Term bounds (per row, divided by |W₀|³; each nondecreasing in |W₀|, gate G-MON)

Notation: m(σ) := M(σ)/σ²; B_d are the P3 degree-d modulus sums of D_Q, so |D_Q(z)| ≤ Σ_{d=3}^{12} B_d|z|^d; G_σ := |g| ceiling at σ.

| Term | Bound / \|W₀\|³ | Row A | Row B |
|---|---|---|---|
| E, K₂ part | K₂(16/15)³ (since q₀ ≤ σ²) | 1.6056 | 1.5559 |
| T_{Δ1a} | ½·d₂·(15/14)·(16/15)⁴·m(σ)² (Taylor along the segment, \|ξ\| ≥ (14/15)\|W₀\|) | 0.4016 | 0.3987 |
| T_{Δ1b} | d₁·c_inv | 1.3547 | 1.3452 |
| T_{Δ2} | e₁·(16/15)³·m(σ) | 0.2164 | 0.2156 |
| T_iso | \|c_iso\|·Σ B_dσ^d / \|W₀\|³ | 0.3323 | 0.3294 |
| T_{Λa} | \|G\|·Σ B_dσ^d / \|W₀\|³ (with ‖Λ₁‖ = \|G\|) | 0.0099 | 0.0098 |
| T_{Λb} | 6\|G\|·[G_σ/(1−G_σ)] / \|W₀\| (with ‖Λ₁′‖ = 6\|G\|, \|Θ_W − Θ_z\| = \|D_Θ\| ≤ \|g\|/(1−\|g\|)) | 0.0296 | 0.0291 |
| **K′_{j,exact}** → published **K′_j** | sum | **3.9502 → 3951/1000** | **3.8836 → 971/250** |
| E, C₂ part | C₂q₀² ≤ C₂(256/225)²Q₀², kept separate | 669.28·Q₀² | 211.01·Q₀² |

**Why the suprema are at w_j** (gate G-MON(struct); this structural argument is the proof). Each part is a nondecreasing function of |W₀|:
- polynomials with nonnegative coefficients (c_inv, m(σ), Σ B_d σ^{d−3});
- or such a polynomial divided by (1 − G_σ).

So the value at w_j is the supremum. The 16-point exact grid check (G-MON(grid)) is supporting only and is not a proof over the whole interval.

**Inputs reused unchanged:**
- K₂ from P4 (1323/1000 and 641/500);
- B_d from P3;
- c_iso and |G| from gate G-L (`dyad_open21_p5_lambda1_check.py`, 5/5 PASS, reviewer-replayed).

### 2.6 Finite-order consistency (gate G-JET; not a proof input, not orbit sampling)

This is a check at 60 digits on the exact h, with h⁻¹ computed by fixed-point iteration. It evaluates (chart main part at z₀) − 𝒫₂(W₀), which equals the sum of the T terms, at 13 angles and at |W₀| = 10⁻², 10⁻³, 10⁻⁴, 10⁻⁵.

The maximum of |ΣT|/|W₀|³ is 0.3962, 0.3989, 0.3992 and 0.3992 respectively. So:
- the remainder is of order Q₀^{3/2} and the ratio is stable;
- the ratio stays far below the T-majorant sum of 2.345 (row A).

Dropping DΔ₁[h₂] makes the ratio diverge like 1/|W₀|, and the gate fails.

## 3. Certificate

**Files.**
- Script `dyad_open21_p5_remainder_cert.py` v0.1.2 (`80452d8a…787c`); output `p5_certificate.json` (`2902ba44…bc10`). Superseded: v0.1.1 `ac549ba0…cef8`, v0.1 `0d260838…bb50`; diffs `cert_v0_1_to_v0_1_1.diff`, `cert_v0_1_1_to_v0_1_2.diff`.
- Pinned inputs, checked by hash in G-0:
  - P3 certificate script `b7df79b0…258d` and engine `e45286fa…50f6`;
  - P4 `p4_offset_certificate.json` `9b0e0c80…57b4` and `p4_exact.json` `945db486…38d8`;
  - Λ₁ gate `aca13bf6…e8ae`.

**Result.** 28/28 gates PASS:
- G-0 (×3), G-L;
- G-INV(a) (×5, incl. the v0.1.2 upper-bound validity gate), G-INV(b);
- G-D2 (×4), G-ID (×2);
- G-D (×2), G-SUM (×4), G-SUM(single) (×2);
- G-MON(struct), G-MON(grid, supporting);
- G-JET (×2, supporting).

Exit 0.

**Negative controls** (`neg_output.txt`, 7/7 rerun by the owner for v0.1.2). Each exits 1, for the reason shown:

| Control | Failing gates |
|---|---|
| `neg_dropDh2` (𝒫₂ without DΔ₁[h₂]) | G-D2 P_{W2}, G-ID, both G-JET |
| `neg_noTL` (T_Λ terms omitted) | G-ID, G-SUM completeness (both rows) |
| `neg_noC2` (C₂q₀² term omitted) | G-ID E parts, G-SUM (both rows) |
| `neg_mix` (row-A primitive domain with the row-B disk) | G-D row A |
| `neg_Mdeg3` (M degree-3 coefficient 39/600 < the true sum 0.0774) | G-INV(a) |
| `neg_raw` (archival raw c₀₅ in G-L, an SG-19 violation) | G-L |
| `neg_Kround` (row-A single K stated 0.001 lower, i.e. the v0.1 value 35323/1000) | G-SUM(single) row A |

## 4. Not established / out of scope

- Re-certification of R9 or of its C₂ (RECOG-owned). A sharper C₂ would shrink the dominant term; that is RECOG's work.
- Any change to T1, T2, the memory law, v6.4.16 or OPEN 21's status (still OPEN until review and adoption).
- The comparator C_W^{(h)}.
- NUMGEN L1 / ISP-angle transfer (SG-19); C_est/κ_est (SG-7).
- True-error maxima: K′ is a majorant supremum. The G-JET ratio, about 0.40 for the T part, suggests K′ is conservative by a factor of about 6 there.

## 5. Next steps (reviewer's order)

1. Independent review of this certificate (gates, negative controls, the decomposition and the monotonicity argument).
2. `[NUM]` orbit sampling — done after the review (§7); PI-machine replication via `run_p5_orbit_num.ps1`.
3. Then, if the PI decides: a v6.4.17 DRAFT r1 with the result proposed at `[THM — conditional on RECOG-THM-R9-MEMORY]`, OPEN 21 → CLOSED (proposed), and a notice to RECOG and NUMGEN.

## 6. Changes v0.1 → v0.1.1 (review of 19 Oct 2026)

1. **Correction (secondary constant).** v0.1 stated K_A = 35323/1000. The certificate computed it from the exact majorant K′_{A,exact} ≈ 3.95020, whereas the record defined K_j from the published K′_A = 3951/1000; with the published value the defining sum is 4768649/135000 ≈ 35.32333 > 35.323. K_A is now **8831/250 = 35.324**, computed from the published K′_A. K_B = 883/100 is unchanged (valid under both readings).
2. **Naming.** K′_{j,exact} (exact majorant) and K′_j (published ceiling) are named separately.
3. **New gate G-SUM(single)** per row checks exactly that the published K_j ≥ published K′_j + C_{2,j}(256/225)²w_j; new negative control `neg_Kround` (the v0.1 value) fails it.
4. **G-MON split** into G-MON(struct), the structural proof of monotonicity, and G-MON(grid), a supporting 16-point check (reviewer note).
5. **Unchanged:** the primary decomposed inequality, both K′_j, both C₂ terms, the domains, every bound part, the scientific scope, the R9 statement-level dependency and the grade ceiling. OPEN 21 stays OPEN; v6.4.16 unchanged.

## 7. `[NUM]` orbit sampling (illustration only; not a proof input)

Run after the certificate review, so the majorants were fixed before any orbit data existed.

**Estimator (reviewer form, v0.1.1 review §3).**

  M̂_W(m) = Ψ_W(m) − Δ₀(z_m) + q_m[c_iso + Λ₁(Θ_z(m))] − Ψ_W(0),

- Θ_W(m) is the continuous lift: Θ_W(0) = Arg W₀ plus the principal per-block increments Arg(W_{k+1}/W_k);
- Θ_z(m) = Θ_W(m) − D_Θ(z_m), the P4 lift tie;
- z_m = h⁻¹(W_m) at 50 digits;
- Ψ_W(m) − Δ₀(z_m) = Ψ_z(m) is the adopted P4-0 identity, and q_m(c_iso + Λ₁) is R9's averaging correction.

Under the R9 statement, |M̂_W(m) − M_W| ≤ C_{2,j}q_m². The owner's first proposal omitted −Ψ_W(0); that form estimates Ψ_∞, not M_W. It is kept as the negative control `--neg noPsi0`, which fails with ratios of order 10⁵–10⁶.

**Finite-time check per sample:**

  |M̂_W − 𝒫₂(W₀)|/Q₀^{3/2} ≤ K′_j + C_{2,j}(256/225)²√Q₀ + C_{2,j}q_m²/Q₀^{3/2}.

**Run.**
- Script `dyad_open21_p5_orbit_num.py` (`e9af1ee1…c7f5`); primitive map in float64, 10⁶ blocks per orbit.
- Per row: 4 radii (w_j, w_j/2, w_j/4, w_j/8) × 8 angles, i.e. 64 orbits; runtime 77 s.
- Output `p5_orbit_num.json` (`94c0933c…8297`; it contains a runtime field, so it is not byte-reproducible).

| Row | \|W₀\| | max ratio | smallest finite-time bound | max truncation term |
|---|---|---|---|---|
| A | 3/64 | 0.3457 | 35.32 | 5.0·10⁻⁶ |
| A | 3/128 | 0.3394 | 19.64 | 4.0·10⁻⁵ |
| A | 3/256 | 0.3363 | 11.79 | 3.2·10⁻⁴ |
| A | 3/512 | 0.3348 | 7.88 | 2.4·10⁻³ |
| B | 3/128 | 0.3394 | 8.83 | 1.3·10⁻⁵ |
| B | 3/256 | 0.3363 | 6.36 | 1.0·10⁻⁴ |
| B | 3/512 | 0.3348 | 5.12 | 7.7·10⁻⁴ |
| B | 3/1024 | 0.3341 | 4.51 | 5.2·10⁻³ |

**Findings.**
- All 64 samples are within the bound.
- The ratio is nearly constant, about 0.33–0.35, across an 8× range of |W₀|. The true remainder therefore behaves like ≈ 0.35·Q₀^{3/2}, with no visible Q₀² (R9) component. K′_j is about 11× conservative; R9's C₂ is pessimistic, as RECOG itself notes.
- **Truncation check.** The same 64 orbits at 2·10⁵ blocks differ from 10⁶ blocks by at most 4.6·10⁻⁵·Q₀^{3/2}.
- **Negative control.** `--neg noPsi0` exits 1.

**Replication on the PI machine.** `run_p5_orbit_num.ps1` reruns, in order: the certificate, the 10⁶-block sampling, the 2·10⁵ truncation run, the negative control, and the hashes.

## 8. Changes v0.1.1 → v0.1.2 (review of 19 Oct 2026)

1. **G-INV(a) hygiene fix.** v0.1.1 compared a rational *lower* bound of each modulus sum with the M coefficients, which does not prove the inequality. The gate now uses the certified upper bound (ub_abs sums), strictly and without tolerance. A new gate checks ub_abs(c)² ≥ |c|² for every coefficient. Result unchanged; 28/28 PASS; `neg_Mdeg3` fails the corrected gate.
2. `[NUM]` orbit sampling added (§7), with the reviewer's corrected M_W estimator and finite-time bound.
3. **Unchanged:** the primary and secondary results (K′_A = 3951/1000, K′_B = 971/250, K_A = 8831/250, K_B = 883/100), the domains, the decomposition, the R9 statement-level dependency and the grade ceiling. OPEN 21 stays OPEN; v6.4.16 unchanged.
