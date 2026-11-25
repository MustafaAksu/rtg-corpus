# DYAD OPEN 21 (P5) — Primitive-variable phase remainder: scope note

**Version:** v0.1 · **Date:** 19 October 2026 · **Author:** Dyadic DSN owner (Claude)
**Status:** `[SESSION]` scope note. **Scope preparation only.** No certificate is computed, no constant K is declared, no `[THM]` is proposed, and adopted DYAD v6.4.16 is not changed.
**Authorization:** PI decision of 19 Oct 2026 (scope note approved). The Λ₁ dependency must be settled before any certificate work.
**Statuses unchanged:** OPEN 3 CLOSED (within its defined scope); OPEN 21 OPEN; OPEN 20 PARTIAL. N12 has not been sent; N10/N11 receipts are pending.

## 1. Source manifest

| Source | Identity | Used for |
|---|---|---|
| `RTG_DYADIC_OSCILLATOR_DSN_v6.4.16` (adopted) | `33c14c5cc27625c17a2b78be74e070ae61b5c7399ded49a1538098735ab559e0` | Definitions §6.14 (Δ₀, Δ₁, Δ₂, P_{W2}, the chart memory law); OPEN 21 text; NF-INV, NF-REM |
| DYAD-ALG-NF6 jet (h, J) | P2B v2 `certificate.json` `d59b0ff6…c6ce` (exact coefficient equality, v6.4.16) | h₂, M(s), μ, a₃₂, a₀₅ |
| DYAD-ART-OPEN3-P3 | `dyad_open3_p3_remainder_cert.py` `b7df79b0…258d` + engine `e45286fa…50f6` | Exact h coefficients; coefficient-modulus data for D_Q, D_Θ |
| DYAD-ART-OPEN3-P4 | `dyad_open3_p4_exact.py` `199a15ba…0703`; `dyad_open3_p4_offset_cert.py` `4058dfc9…7b7a` | Δ₁, Δ₂ (exact); K₁, K₂; majorants of D_Q, D_Θ |
| `RTG_RELATIONAL_RECOGNITION_DSN_v0.3.20` §6.13, §6.13a, §6.14 | project document, read 19 Oct 2026 via the project tool (byte hash not measured) | Statement of RECOG-THM-R9-MEMORY: Λ₁, c_iso, C₂, rows, observable |
| `dyad_open21_p5_lambda1_check.py` (this note) | `aca13bf62a6034a11e30190178e3e7a7fad932f26b4114cceb941e530e06e8ae` | Gate G-L (§3) |

## 2. Exact definitions (unchanged from v6.4.16 §6.14)

- **Frame and chart.** W = 𝓛(ρ,η), Q = |W|²; W = h(z), q = |z|²; z₀ = h⁻¹(W₀). Θ_W = Arg W, Θ_z = Arg z, z = re^{iΘ}.
- **Memories.** M = Ψ_∞ − Ψ_z(0), on the C_z track of R9. M_W = Ψ_{W,∞} − Ψ_W(0), the primitive asymptotic-phase memory with the P4 lift tie.
- **Chart-variable memory law** (adopted, `[THM — conditional on RECOG-THM-R9-MEMORY]`):
  M_W(z₀) = −Δ₁(z₀) − Δ₂(z₀) + q₀[c_iso + Λ₁(Θ_{z₀})] + E, with |E| ≤ C₂q₀² + K₂q₀^{3/2}.
- **Target object 𝒫₂.** This is the adopted primitive-variable second-order form of DYAD-ALG-OPEN3-PHASE-OFFSET, verbatim. No new normalization and no new phase definition:
  𝒫₂(W₀) := −Δ₁(W₀) + Q₀[c_iso + Λ₁(Θ_{W₀})] + P_{W2}(W₀), with P_{W2} = −Δ₂ + DΔ₁[h₂].
  Equivalently, 𝒫₂(W₀) = −Δ₁(W₀) − Δ₂(W₀) + DΔ₁(W₀)[h₂(W₀)] + Q₀[c_iso + Λ₁(Θ_{W₀})].
- **Target inequality (OPEN 21).** |M_W − 𝒫₂(W₀)| ≤ K·Q₀^{3/2}, per row, with rows not mixed (§4). The R9 remainder is kept as a separate term (§6).

## 3. Λ₁ dependency (check 3) — RESOLVED at statement level

**Source.** RECOG v0.3.20 §6.13a (RECOG-THM-R9-MEMORY) and §6.13 (RECOG-ALG-LATTICE-MEMORY).

**Coefficients.**
- Λ₁(Θ) = (43 sin6Θ − 5611√3 cos6Θ)/1270080 = Im(G e^{−6iΘ}).
- G = (1−2iτ)a₀₅/(1−6iτ) = −(43 + 5611√3 i)/1270080.
- c_iso = Im[(1−2iτ)(a₃₂ − μ²/2)] = −4√3/27.

**Representation frame.** NF chart z of DYAD-ALG-NF6 on the C_z track. Θ is the continuous lift of arg z; Λ₁ is a function of the **chart** angle Θ_z. In 𝒫₂ it is evaluated at the **primitive** angle Θ_W. That change of argument is a term to be bounded (T_Λ, §6); it is not an identity.

**Exact sup-norms.**
- ‖Λ₁‖_∞ = |G| = √481897/90720 ≈ 0.00765198.
- ‖∂_ΘΛ₁‖_∞ = 6|G| = √481897/15120 ≈ 0.0459119.
- Exact: |G|² = 481897/8230118400.

**Gate G-L** (`dyad_open21_p5_lambda1_check.py`, sympy, exit-gated). From the adopted DYAD μ, a₃₂, a₀₅ it reproduces exactly:
- G;
- Λ₁, as RECOG states it;
- c_iso;
- R9's cohomological identity g + τg′ = c_iso + Im((1−2iτ)a₀₅e^{−6iΘ}), with g = c_iso + Λ₁;
- |G|².

Result: 5/5 PASS. The negative control substitutes the archival raw six-step c₀₅ (an SG-19 violation); it exits 1 with 4 checks failing.

**Not inspected: the R9 proof record.** The underlying proof material is not in the project: the Arb enclosure of K_Φ ≤ 258.49 / 81.44 and RECOG's certificate script. P5 uses **only the R9 statement**: the form of M, Λ₁, c_iso, C₂ = 517 / 163, q_max = 1/400 / 1/1600, and the C_z observable. It does not use any R9 internal constant. So no BLOCKED status is needed. P5's result inherits R9's condition. If RECOG changes R9's statement or rows, P5 must be re-checked; N11 already asks RECOG to flag such changes.

## 4. Domains (check 1)

**Inputs** (DYAD-THM-NF-INV):
- h is injective on |z| ≤ 1/10;
- h⁻¹ exists on |W| ≤ 9/100, with values in |z| ≤ 1/10;
- on |z| ≤ 1/10: (15/16)|z| ≤ |h(z)| ≤ (17/16)|z| and M(|z|)/|z| < 1/16.

**Primitive-start domain per row.** Set |W₀| ≤ (15/16)·r. Then |z₀| ≤ (16/15)|W₀| ≤ r, so z₀ lies in the certified row disk. R9's window q₀ ≤ q_max = r² then holds automatically, because q_max = (1/20)² and (1/40)².

| Row | Chart disk | R9 window | Primitive domain | Q₀ range |
|---|---|---|---|---|
| A | \|z\| ≤ 1/20 (C₇ = 100) | q₀ ≤ 1/400, C₂ = 517 | \|W₀\| ≤ 3/64 | Q₀ ≤ 9/4096 |
| B | \|z\| ≤ 1/40 (C₇ = 30) | q₀ ≤ 1/1600, C₂ = 163 | \|W₀\| ≤ 3/128 | Q₀ ≤ 9/16384 |

**Segment condition.** The Taylor steps of §6 run along the segment [W₀, z₀]. From |z₀ − W₀| = |(h−id)(z₀)| ≤ M(|z₀|) < |z₀|/16 ≤ |W₀|/15, every point ξ on the segment satisfies:
- |ξ| ≥ (14/15)|W₀|, so the segment avoids the singular point 0 of Δ₁;
- |ξ| ≤ (16/15)|W₀| ≤ r.

The certificate gate G-D (§7) checks these rational inequalities exactly. Rows A and B are evaluated separately throughout; no constant from one row is used in the other.

## 5. Inverse-map remainder (check 2)

**Target:**

  |h⁻¹(W) − W + h₂(W)| ≤ c_inv·|W|³ on the row domains of §4.

The constant is named **c_inv** (per row: c_inv^A, c_inv^B). It is **not** the OPEN 3 constant c₃ = 2/3, which bounds the angular second derivative ‖D²D_{Θ,1}‖ (v6.4.14).

**Route.** Use exact rational ceilings only. Let g = h − id = h₂ + g_{≥3} and z = h⁻¹(W). Then

  z − W + h₂(W) = −[h₂(z) − h₂(W)] − g_{≥3}(z).

The two pieces are bounded as follows:
- |h₂(z) − h₂(W)| ≤ (7/6)·max(|z|,|W|)·|z − W|. Here 7/12 = |c₂₀| + |c₁₁| + |c₀₂| exactly, so ‖Dh₂(w)‖ ≤ (7/6)|w|.
- |z − W| = |g(z)| ≤ M(|z|).
- |g_{≥3}(z)| ≤ M(|z|) − (7/12)|z|², since the degree-2 part of M is exact.

With |z| ≤ (16/15)|W|, each term is a polynomial in |W| of order ≥ 3. c_inv is its exact rational supremum after division by |W|³; the quotient is nondecreasing, so it is evaluated at the row endpoint.

`[HEUR]` Expected size: about 0.9 on row A. **Not certified, not declared.**

## 6. Remainder decomposition (check 4)

Subtract §2's 𝒫₂ from the chart law. This gives an exact identity:

  M_W − 𝒫₂(W₀) = E + T_{Δ1} + T_{Δ2} + T_iso + T_Λ,

| Term | Definition | Majorant plan (per row) | Order |
|---|---|---|---|
| E | chart-law remainder | \|E\| ≤ C₂q₀² + K₂q₀^{3/2}, with q₀ ≤ (256/225)Q₀. **C₂q₀² is kept as its own term**, with R9's C₂ and window. | Q₀² + Q₀^{3/2} |
| T_{Δ1} | −[Δ₁(z₀) − Δ₁(W₀) − DΔ₁(W₀)[z₀ − W₀]] − DΔ₁(W₀)[z₀ − W₀ + h₂(W₀)] | ½·sup_ξ‖D²Δ₁(ξ)‖·\|z₀−W₀\|² + ‖DΔ₁‖·c_inv\|W₀\|³. Δ₁ is homogeneous of degree 1: ‖DΔ₁‖ ≤ d₁ and ‖D²Δ₁(ξ)‖ ≤ d₂/\|ξ\|, with \|ξ\| ≥ (14/15)\|W₀\| (§4). d₁ and d₂ are exact sums over the harmonic coefficients of Δ₁ (k = ±1, ±3). | Q₀^{3/2} |
| T_{Δ2} | −[Δ₂(z₀) − Δ₂(W₀)] | sup‖DΔ₂‖·\|z₀ − W₀\|; Δ₂ is homogeneous of degree 2, so ‖DΔ₂(w)‖ ≤ e₁\|w\|, with e₁ exact from its harmonics k = 0, ±2, ±4, ±6. | Q₀^{3/2} |
| T_iso | c_iso(q₀ − Q₀) = −c_iso·D_Q(z₀) | \|c_iso\|·\|D_Q(z₀)\|; \|D_Q\| ≤ c_DQ\|z\|³ from the P3/P4 coefficient-modulus data | Q₀^{3/2} |
| T_Λ | q₀Λ₁(Θ_{z₀}) − Q₀Λ₁(Θ_{W₀}) | \|q₀ − Q₀\|·\|G\| + Q₀·6\|G\|·\|Θ_{W₀} − Θ_{z₀}\|. The angle difference is \|D_Θ(z₀)\| ≤ c_DΘ\|z₀\|, the principal branch certified in P4 (\|g\| < 1/16). Needs the §3 sup-norms. | Q₀^{3/2} |

**Final form, per row:**

  |M_W − 𝒫₂(W₀)| ≤ K′·Q₀^{3/2} + C₂·(256/225)²·Q₀²

K′ collects T_{Δ1}, T_{Δ2}, T_iso, T_Λ and the K₂ part of E. The R9 term stays visible. A single-K version K = K′ + C₂(256/225)²·Q_max^{1/2} may be stated *in addition*, and only per row.

`[HEUR]` On row A, the R9 term probably dominates: C₂(256/225)²·(3/64) is roughly 31. That is a property of R9's conservative C₂ (RECOG notes it is about 170–550× pessimistic). It is not a P5 defect. K and K′ are **not declared** in this note.

**Grade ceiling.** The best possible grade is `[THM — conditional on RECOG-THM-R9-MEMORY]`:
- M_W exists only through T1, which is conditional on R9;
- the chart law is conditional on R9.

T1, T2 and their grades are not touched.

## 7. Planned certificate (not executed)

Script `dyad_open21_p5_remainder_cert.py`. It uses exact rationals and the P3/P4 inputs pinned by hash, and is exit-gated per row.

| Gate | Content |
|---|---|
| G-0 | Input hashes: P3 and P4 certificates, engine, P2B certificate; h and J reproduced exactly |
| G-L | Λ₁, G, c_iso, \|G\|², 6\|G\| (§3; already passing) |
| G-D | Domain inclusions of §4, per row, exact |
| G-INV | c_inv per row (§5); nondecreasing quotient check |
| G-Δ1 | d₁, d₂ from the exact Δ₁ harmonics; the derivative identities checked symbolically |
| G-Δ2 | e₁ from the exact Δ₂ harmonics |
| G-DQΘ | c_DQ, c_DΘ reused from the P3/P4 majorants (no new derivation) |
| G-SUM | K′ per row (rational ceiling); single-K version reported separately |
| G-ID | The identity M_W − 𝒫₂ = E + ΣT, checked symbolically through degree 3 in W, so that no term is missing |

**Negative controls** (each must exit 1):
- drop DΔ₁[h₂] from 𝒫₂;
- evaluate Λ₁ at Θ_z inside 𝒫₂ while omitting T_Λ;
- use the raw c₀₅ (G-L negative);
- mix rows (row-A domain with row-B C₂);
- omit the C₂q₀² term.

**Illustration `[NUM]`, not a proof input.** On the PI machine (PowerShell), sample orbits in both row domains. Compute M_W − 𝒫₂(W₀) in high precision, with Ψ_{W,∞} extrapolated using the R9-controlled tail. Report |M_W − 𝒫₂|/Q₀^{3/2} against K′. This is the same pattern as P3/P4: the majorant suprema are not the true-error maxima.

## 8. Out of scope

- Any change to v6.4.16, to R9, or to the grades of T1/T2.
- The comparator C_W^{(h)}.
- Transfer to NUMGEN L1 or to ISP-angle coefficients (SG-19).
- C_est/κ_est (SG-7).
- Sharpening R9's C₂ (that is RECOG's).
- The combined ±6 coefficient of Λ₁ and P_{W2} (an optional `[ALG]` remark; not needed for OPEN 21).

## 9. Questions for the reviewer

1. Final form: should it be K′Q₀^{3/2} + C₂(256/225)²Q₀² (recommended, keeps R9 visible), or the single K, or both?
2. Is the statement-level R9 dependency (§3) acceptable, or must the R9 proof record be obtained from RECOG before P5 certification?
3. Should the `[NUM]` illustration (§7) run before or after the exact certificate?
