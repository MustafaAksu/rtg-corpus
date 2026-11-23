# DYAD OPEN 3 — P3 certified remainders for the spiral residual: SESSION proof record (v0.1)

**Date:** 19 October 2026 · **Author:** Claude (Dyadic DSN owner/editor)

**Status:** `[SESSION]`. The main result is a **`[THM]` candidate**, with proof by analytic estimates plus an exact-rational certificate. It is not owner-adopted. Independent review is requested.
- DYAD v6.4.13 is unchanged.
- OPEN 3 stays OPEN until review and an owner/PI decision.
- OPEN 20 stays PARTIAL.

**Authorization:** reviewer/PI decision of 19 Oct, "SCIENTIFIC REVIEW ACCEPTED — P3 READY". Rows are kept separate. Derivatives of D_Θ and the Q ↔ q bridge are tracked explicitly.

**Base documents:**
- scope note v0.1.1 (`4526546a…6c1ab`);
- P1/P2 record v0.1 (`83248235…1b53`), externally accepted;
- adopted DYAD v6.4.13 (`5958f7fe…b968542`).

**Artifacts** (Python 3.13, standard-library `fractions`; mpmath 1.3.0 only for the `[NUM]` script):

| File | SHA-256 | Role |
|---|---|---|
| `dyad_open3_p3_remainder_cert.py` | `b7df79b0f820f8431e6c2af54a03ef8fd93f869fb06470ed037cdca1126d258d` | exit-gated exact-rational certificate (<1 s). Argument `neg_K`, `neg_h2` or `neg_mu` runs a negative control, which must exit 1 |
| `p3_certificate.json` | `bd533725b8c562fae708becdfa6b58ab3601ac5698b1ab00da6afd6493ddfcde` | output of the main run |
| `dyad_return_qchi_exact.py` | `e45286fa100b2b31c4d547e8513e23f926b2bda36d31938577fa9f312ca350f6` | exact ℚ(i√3) engine; the same file as the DYAD-ART-RE-REFEREE engine cited in DYAD §6.14 (`e45286fa…50f6`) |
| `dyad_open3_p3_numeric_check.py` | `7e91c6b5648b9756cd83de7f4a1222890537c33b273203f4bb679e4b8d8737e3` | `[NUM]` illustration only; not a proof input |
| `p3_numeric.json` | `2e7ee33640c894e3371e26aabc833b2ffd01df2be5072e494a41faead9f414cd` | its output |

**Gate results:** main run exit 0 (PASS). Each negative control exits 1: `neg_K` (stated K_Θ below the exact value), `neg_h2` (perturbed c₀₂), `neg_mu` (μ ↔ μ̄).

## 1. Statement `[THM — SESSION candidate]` (T-OPEN3)

**Setting** (definitions as fixed in P1):
- the normalized chart W = h(z) of DYAD-ALG-NF6;
- one block z′ = F̂(z), with F̂ = h⁻¹∘F_W∘h;
- q = |z|²;
- S_Θ = D_Θ∘F̂ − D_Θ and S_Q = D_Q∘F̂ − D_Q;
- L_Θ and [S_Q]₅ as in P2 (M-1c, M-1b).

For each NF-REM row r (rows not mixed) and every 0 < |z| ≤ r:

  |S_Θ(z) − L_Θ(z)| ≤ K_Θ(r) q²,   |S_Q(z) − [S_Q]₅(z)| ≤ K_Q(r) q³,

| Row | C₇ (NF-REM) used | K_Θ | K_Q | c₁ | c₂ |
|---|---|---|---|---|---|
| \|z\| ≤ 1/20 | 100 | **123/125** (0.9837…) | **2353/1000** (2.3525…) | 261/1000 | 393/500 |
| \|z\| ≤ 1/40 | 30 | **909/1000** (0.9086…) | **258/125** (2.0636…) | 51/200 | 96/125 |

The value in parentheses is the exact rational bound produced by the certificate. The stated constant is its ceiling at three decimals.

**Static chart constants**, on the same row:
- |D_Θ(z) − D_{Θ,1}(z)| ≤ c₁ q;
- ‖D D_Θ(z)‖ ≤ c₂;
- ‖D² D_{Θ,1}(w)‖ ≤ c₃/|w| with c₃ = 2/3, for all w ≠ 0.

Here D_{Θ,1} = Im(h₂(z)/z) (P2, M-1a).

**Orbit scope.** For q ≤ 1/400 the normalized one-orbit contraction of NF-REM gives |F̂z|² ≤ q − ½q². So both disks are forward-invariant, and the per-block bounds hold at every block of every orbit that starts in the row's disk.

**Corollaries `[ALG]`** (from the statement together with adopted results):
- **(a) Certified SG-9 at chart level.** Combine with P2's exact ceiling |L_Θ| ≤ ((7+2√19)/24) q^{3/2} < (131/200) q^{3/2}. This gives:
  - |S_Θ| ≤ (131/200 + K_Θ r) q^{3/2}, i.e. ≤ 0.705 q^{3/2} on row 1/20 and ≤ 0.678 q^{3/2} on row 1/40;
  - relative to the leading normalized phase step τq, this is ≤ 0.611 √q (row 1/20) and ≤ 0.587 √q (row 1/40).
- **(b) Primitive-amplitude form.** NF-INV gives q ≤ (256/225) Q_prim at the same state. Then:
  - |S_Θ − L_Θ| ≤ (637/500) Q² on row 1/20 and ≤ (1177/1000) Q² on row 1/40;
  - |S_Q − [S_Q]₅| ≤ (1733/500) Q³ on row 1/20 and ≤ (3041/1000) Q³ on row 1/40.

  L_Θ and [S_Q]₅ are still evaluated at z = h⁻¹(W). Q and q are not identified; only the comparison inequality is used.
- **(c) Telescoping.** Along an orbit, Σ_{m<M} S_Θ(z_m) = D_Θ(z_M) − D_Θ(z₀), and this tends to −D_Θ(z₀). The per-block bounds are not needed for the cumulative offset. They matter for windowed or per-block observables, which is SG-9's setting.

## 2. Inputs

All analytic inputs are adopted. h and J are regenerated exactly from T and cross-checked against the adopted data.

| Input | Source | Use |
|---|---|---|
| h (degree 6, resonant coefficients zero) | DYAD-ALG-NF6 | regenerated exactly by the one-step homological recursion (as in `dyad_open19_R0_identity_cert.py`) |
| J through degree 6: J = z + μz²z̄ + a₃₂z³z̄² + a₀₅z̄⁵ | DYAD-ALG-NF6, NF-REM | J = 𝒥_{≤6}(n^{∘6}), with n the one-step normal-form jet |
| \|F̂ − J\| ≤ C₇\|z\|⁷ on \|z\| ≤ r | DYAD-THM-NF-REM | displacement remainder (Lemma 0) |
| \|h(z)/z − 1\| < 1/16, inverse chart on \|z\| ≤ 1/10 | DYAD-THM-NF-INV | Log branch and domain; q ↔ Q comparison |
| one-orbit contraction for q ≤ 1/400 | DYAD-THM-NF-REM | orbit scope |

**Cross-checks of the regenerated h and J** (all PASS in the certificate):
- h₂ equals the NF6 h₂;
- h has 23 nonzero coefficients including the linear one;
- every resonant coefficient (a − b − 1 ≡ 0 mod 6) is zero;
- the degree-k coefficient-modulus sums of h are ≤ the M(s) coefficients for k = 3,…,6, and the degree-2 moduli are exactly 1/6, 1/3, 1/12;
- μ = −½ − i·2√3/3;
- J has exactly the monomials (1,0), (2,1), (3,2), (0,5) through degree 6;
- the chart-law identities 245/216 = |μ|² + 2Re a₃₂ and 89√3/324 = Im(a₃₂ − μ²/2) (DYAD §6.14 / RECOG-ALG-CHART-LAWS);
- the regenerated values are a₃₂ = −97/432 + (197/324) i√3 and a₀₅ = −49/8640 − (307/25920) i√3.

`certificate.json` (`jets.h_degree6`, `jets.J_through6`) was not available in this session. Comparing the regenerated h with it is a review request (§6).

## 3. Proof

Fix a row r and 0 < s := |z| ≤ r. Write z′ = F̂(z) and δ := z′ − z.

**Notation for the bounds:**
- **Moduli.** For c ∈ ℚ(i√3), |c| is replaced by an exact rational when |c|² is a rational square. Otherwise it is replaced by a rational ceiling of √(|c|²) at 10⁻¹² resolution.
- **Coefficient sums.** A₅ := |a₃₂| + |a₀₅| (ceiling 1.0981) and |μ| (ceiling 1.2583).

**Lemma 0 (block displacement).** δ = μqz + ρ with

  |ρ| ≤ A₅ s⁵ + C₇ s⁷,  |δ| ≤ s·β(s),  β(s) := |μ|s² + A₅s⁴ + C₇s⁶.

*Proof.* F̂z − z = (J(z) − z) + (F̂ − J)(z). Here J(z) − z − μqz = a₃₂z³z̄² + a₀₅z̄⁵, and NF-REM bounds the second term. ∎

The certificate checks β(r) < 1/2 (β(1/20) ≈ 0.00315, β(1/40) ≈ 0.00079). Hence every point w of the segment [z, z′] satisfies s(1 − β) ≤ |w| ≤ s⁺ := s(1 + β).

**Lemma 1 (chart majorants).** Put g(w) := (h(w) − w)/w = Σ_{k=2}^{6} h_k(w)/w. Each monomial c w^a w̄^b of h_k gives c w^{a−1} w̄^b in g. Let:
- G(t) := Σ |c| t^{k−1};
- G₁(t) := Σ |c| (|a − 1| + b) t^{k−2};
- G₁^{≥2}(t) := the same sum as G₁, restricted to k ≥ 3.

Then |g(w)| ≤ G(|w|) and ‖Dg(w)‖ ≤ G₁(|w|), since ‖Df‖ ≤ |f_w| + |f_w̄| for the real derivative.

Write g₁ := h₂/w = c₂₀w + c₁₁w̄ + c₀₂ φ(w) with φ := w̄²/w. Then:
- ‖Dg₁‖ ≤ L₁ := |c₂₀| + |c₁₁| + 3|c₀₂| = 3/4;
- ‖D²φ(w)‖ ≤ 8/|w|, from |φ_ww| = |φ_ww̄| = |φ_w̄w̄| = 2/|w| and D²φ[v,v] = φ_ww v² + 2φ_ww̄ |v|² + φ_w̄w̄ v̄².

**Domain check** (certificate): s⁺ ≤ 1/10 and G(s⁺) < 1/16. So D_Θ = Im Log(1 + g) uses the principal Log, holomorphic in g, along the whole segment. This agrees with P1-4.

**Lemma 2 (angular decomposition).** Let E := Im[Log(1 + g) − g] and g_{≥2} := g − g₁. Then

  S_Θ − L_Θ = A₁ + A₂ + B + C,

where:
- A₁ = Im[g₁(z′) − g₁(z) − Dg₁(z)[δ]];
- A₂ = Im Dg₁(z)[ρ];
- B = Im[g_{≥2}(z′) − g_{≥2}(z)];
- C = E(z′) − E(z).

This uses L_Θ = Im Dg₁(z)[μqz] (P2) and δ = μqz + ρ.

The four bounds:
- **A₁.** Only the c₀₂φ part has a second derivative. Taylor's formula with the ‖D²φ‖ bound on the segment gives |A₁| ≤ ½·8|c₀₂|·|δ|²/(s(1−β)) ≤ 4|c₀₂| s β²/(1 − β).
- **A₂.** |A₂| ≤ L₁ (A₅s⁵ + C₇s⁷).
- **B.** By the mean value inequality, |B| ≤ G₁^{≥2}(s⁺)·sβ.
- **C.** C = Im ∫₀¹ ψ′(g(w_t)) Dg(w_t)[δ] dt, with ψ(u) = Log(1+u) − u and |ψ′(u)| = |u|/|1+u| ≤ |u|/(1−|u|). Hence |C| ≤ [G(s⁺)/(1 − G(s⁺))]·G₁(s⁺)·sβ.

**Monotonicity.** Each bound divided by s⁴ is a product of nonnegative, nondecreasing functions of s:
- β/s² = |μ| + A₅s² + C₇s⁴ is nondecreasing;
- G(s⁺)/s and G₁^{≥2}(s⁺)/s are polynomials in s and (1+β) with nonnegative coefficients;
- 1/(1−β) and 1/(1−G) are nondecreasing.

So the supremum over 0 < s ≤ r is attained at s = r. K_Θ(r) is the exact rational sum at s = r. The parts (A₁, A₂, B, C) are:
- row 1/20: 0.0266, 0.0506, 0.3221, 0.5844;
- row 1/40: 0.0132, 0.0209, 0.3085, 0.5660. ∎

**Static constants.**
- c₁ q bounds |Im g_{≥2}| + |Log(1+g) − g| ≤ G^{≥3}(s) + G(s)²/(2(1 − G(s))), where G^{≥3} is G restricted to k ≥ 3 and |Log(1+u) − u| ≤ |u|²/(2(1−|u|)).
- c₂ bounds ‖D Im Log(1+g)‖ ≤ G₁(s)/(1 − G(s)).
- c₃ = 8|c₀₂| = 2/3.

All are evaluated at s = r by the same monotonicity.

**Lemma 3 (radial decomposition; explicit Q ↔ q bridge).** D_Q = |h|² − |z|² is an exact polynomial in (z, z̄) of degrees 3 to 12. The certificate computes it and checks that [D_Q]₃ = D₃ = 2Re(z̄h₂). Let B_k be the coefficient-modulus sum of its degree-k part (B₃ ≈ 1.0486, B₄ ≈ 0.3628, …). Then [S_Q]₅ = DD₃(z)[μqz] (P2), and

  S_Q − [S_Q]₅ = [D₃(z′) − D₃(z) − DD₃(z)[δ]] + DD₃(z)[ρ] + [D_{≥4}(z′) − D_{≥4}(z)],

with bounds:
- first bracket: ½·6B₃ s⁺·(sβ)²;
- second term: 3B₃ s²·(A₅s⁵ + C₇s⁷);
- third bracket: Σ_{k≥4} k B_k (s⁺)^{k−1}·sβ.

These use ‖D^j of a degree-k homogeneous part‖ ≤ k(k−1)⋯(k−j+1)·B_k |w|^{k−j}. Divided by s⁶, each term is nondecreasing, so K_Q(r) is the value at s = r. The parts are 0.2512, 0.2120, 1.8893 (row 1/20) and 0.1248, 0.0878, 1.8510 (row 1/40). ∎

**Route note** (difference from scope v0.1.1 M-3r):
- The radial bound uses the exact chart identity S_Q = D_Q∘F̂ − D_Q. D_Q *is* the Q ↔ q bridge, written explicitly.
- `DYAD-THM-PRIM-CTR` is therefore **not** an input. The scope note's PRIM-CTR + normalized-law route would also need a certified normalized radial O(q³) remainder, and that is not adopted.
- PRIM-CTR stays consistent with the result through the P2 identity (I-5).

## 4. Numerical illustration `[NUM]` (not a proof input)

The `[NUM]` script uses:
- 60-digit evaluation of the exact primitive T, six steps;
- the exact polynomial h;
- h⁻¹ by the NF-INV contraction;
- 4 radii (r, r/2, r/4, r/8) × 72 angles per row.

| Row | max \|F̂ − J\|/\|z\|⁷ | max \|S_Θ − L_Θ\|/q² (bound) | max \|S_Q − [S_Q]₅\|/q³ (bound) |
|---|---|---|---|
| 1/20 | 0.971 (C₇ = 100) | 0.196 (0.984) | 0.949 (2.353) |
| 1/40 | 0.971 (C₇ = 30) | 0.189 (0.909) | 0.909 (2.064) |

Reading:
- The O(|z|⁷) behaviour of F̂ − J at every radius confirms that the regenerated h, J and the primitive map agree through degree 6.
- The adopted C₇ values are conservative ceilings, about 30–100 times the sampled ratio. The certified bounds use the adopted C₇ unchanged.
- The certified bounds lie within a factor of about 5 (angular) and about 2.5 (radial) of the sampled maxima.

## 5. What this does and does not establish

- **Establishes (candidate).** It supplies the "theorem-grade Taylor remainder bounds" that DYAD OPEN 3 names as open, for the **per-block spiral residual at chart level** (S_Θ, S_Q) on both NF-REM rows. With P2 this makes the 2Re(W̄h₂) / Im(h₂/z) origin exact (leading terms) and certified (remainders).
- **Proposed handling after review** (owner/PI decision):
  - promote T-OPEN3 to `[THM]`;
  - promote the P2 identities to `[ALG]`;
  - record OPEN 3 as CLOSED at per-block chart scope.

  The scope-note items P4 (asymptotic-phase transfer, §4a) and P0 (historical fit, BLOCKED) would be listed as separate residual items. No DYAD text is changed here.
- **Not established:**
  - any statement about the historical fit, C_est or κ_est (SG-7);
  - any transfer to NUMGEN L1 primitive phase coefficients or to ISP-angle coefficients (SG-19);
  - a certified bound on ΔΘ_z itself beyond the adopted chart laws;
  - anything about OPEN 20, G2, RRF or physical readings.
- `[ALG structure]` in DYAD §2 OPEN 3 is not changed by this record. Any change is a successor-text decision.

## 6. Review requests

1. Lemma 2: the A₁/A₂/B/C split and the Log-branch argument (P1-4 domain).
2. Lemma 3: the coefficient-modulus derivative bounds for the degree-3…12 polynomial D_Q.
3. The monotonicity argument that places the supremum at s = r.
4. If `certificate.json` is accessible, compare the regenerated h (23 coefficients) with `jets.h_degree6` and J with `jets.J_through6`.
5. An independent replay of `dyad_open3_p3_remainder_cert.py`. It is pure-Python exact arithmetic and finishes in under 1 s, so the earlier timeout should not recur. Include its three negative controls.
