# DYAD → NUMGEN — L-PHASE angular remainder: exact-rational certificate on row A (SESSION v0.1)

**Version:** v0.1 · **Date:** 20 October 2026 · **Author:** Dyadic DSN owner (Claude)

**Basis.** Scope note `DYAD_NUMGEN_LPHASE_ANGULAR_ENCLOSURE_SCOPE_v0_1.md` (`1eae1d1a…1f74`), reviewed as `L-PHASE SCOPE ACCEPTED — ROW A CERTIFICATION AUTHORIZED`.
- Scope of the authorization: P-Λ, P-a1, P-a2, P-b, P-c, P-7 and the final C_*.
- All six negative controls are kept.
- Order: P-c and P-Λ first.
- Every irrational factor (τ, the bridge factor, π/2) enters through a proved rational ceiling.

**Status.**
- `[SESSION]` record, pending review.
- No constant is adopted, and no NUMGEN coefficient is corrected.
- DYAD v6.4.18 is unchanged; OPEN 20 PARTIAL; B-an and B-6 OPEN.

**Certificate.** `dyad_numgen_lphase_rowA_cert.py`, with helpers `qw.py` and `tzw.py` (the six-step helper of the O20-an work, generalized to n steps).
- It writes `lphase_rowA_certificate.json` (byte-deterministic; verified by rerun) and `lphase_rowA_perf.json` (timings only).
- 10 gates and 6 negative controls; exit-gated. Runs in about 2 s.
- Arithmetic is exact in ℚ(ω), ω = i√3, and in Fractions. √3 is enclosed by 15-digit rational bounds; π by [3.14159265, 3.14159266]; e^x by Taylor sums with a proved tail. Moduli use rational square-root ceilings.

## 1. Result

`[THM — SESSION, pending review]`; conditional on the selected T (SG-14).

Let x ∈ U = {0 < Q ≤ 1/625}, let x_m = T^{6m}x and Q_m = |W(x_m)|², the **primitive** observable. Let φ̂ be the increasing primitive lift whose one-step increments are the principal angles δ_T(y) = Arg(W(Ty)/W(y)). Then, for every m ≥ 0,

φ̂_{6(m+1)} − φ̂_{6m} = 2π − τQ_m + r_m,  **|r_m| ≤ (403/250)·Q_m^{3/2}** (C_* = 1.612).

**Branch statement (P-c).** On the whole six-phase tube U_T:
- |W(Ty)/(λW(y)) − 1| ≤ ε with ε ≤ 0.04654;
- hence |δ_T − π/3| ≤ arcsin ε < π/6, and W never vanishes;
- the six-step lifted increment equals 2π + Arg(F_W(W)/W), with a margin of 2.86 rad to the (π, 3π) window edges.

**Domain.** Block base points stay in U, because F(U) ⊂ U (DYAD-THM-PRIM-CTR). Their chart images lie in the row-A disk |z| < 1/20 (DYAD-THM-NF-REM). So the bound holds at **every block of every orbit started in U**, including the canonical NUMGEN seed (1/100, 1/250).

## 2. Proof chain

1. **Identity D.** Under the branch conditions B1 and B2 (P-c):

   r = Λ₃(z) + [S_Θ − L_Θ] + τ[D_Q − D₃] + [Arg(J/z) + τq] + Arg(F̂/J),  Λ₃ = L_Θ + τD₃.

   This is the scope note §2, reviewed. Gate **G-D** checks its leading order **exactly against the primitive map**: Im(F₄(W)·W̄) = Λ₃(W)|W|², where F₄ is the quartic part of the six-step return in W and F₃ = μ|W|²W. This upgrades the scope check S1, which tested only Θ = 0, to a full polynomial identity.
2. **Bounds on row A** (q ≤ 1/400, √q ≤ 1/20):

   | Term | Bound | Source |
   |---|---|---|
   | \|Λ₃(z)\| | ≤ Λ̄ q^{3/2}, Λ̄ = 1401/1000 | **P-L** |
   | \|S_Θ − L_Θ\| | ≤ K_Θ q², K_Θ = 123/125 | DYAD-THM-OPEN3-SPIRAL-REM, row A (imported; pin gate **S-T**) |
   | τ\|D_Q − D₃\| | ≤ τ̄ c′_Q q², c′_Q = 0.3692 | **P-a2** |
   | \|Arg(J/z) + τq\| | ≤ c_J q², c_J = 0.5022 | **P-b** |
   | \|Arg(F̂/J)\| | ≤ c₇ q³, c₇ = (π̄/2)·100/(1 − U) = 157.58 | **P-7**; C₇ = 100 imported from DYAD-THM-NF-REM |

3. **Combination.**
   - With q² ≤ q^{3/2}/20 and q³ ≤ q^{3/2}/8000:

     |r| ≤ [Λ̄ + (K_Θ + τ̄c′_Q + c_J)/20 + c₇/8000] q^{3/2} = 1.51632 q^{3/2}.
   - **Correction to the scope note.** The scope note wrote c₇/400. That is valid but loose; q^{3/2} ≤ (1/400)^{3/2} = 1/8000 is used here.
4. **Bridge (P-a1).** |D_Q| ≤ c_Q q^{3/2} with c_Q = 0.79246. On row A this gives Q = q + D_Q ≥ q(1 − c_Q/20), so q^{3/2} ≤ (1 − c_Q/20)^{−3/2} Q^{3/2}. The factor is enclosed as y·√y with y = 1/(1 − c_Q/20): 1.06252.
5. **Conclusion.** C_* ≤ 1.06252 × 1.51632 = 1.61112, published as the ceiling 403/250. ∎

## 3. Gates

| Gate | Content | Result |
|---|---|---|
| **G-H** | Provenance of the chart. h and the one-step normal form n are regenerated exactly from T: one-step homological equation, resonant coefficients of h set to zero. The adopted h is defined as the unique solution in this convention (DYAD-ALG-NF6), so the regeneration is that h. Checked against the adopted data: h₂; n₂₁, n₃₂, n₀₅; 23 nonzero coefficients; J = n^{∘6} gives μ, a₃₂, a₀₅; per-degree modulus sums 7/12 (exact), 0.07740, 0.11119, 0.04354, 0.04939 lie below the adopted M(s) ceilings 39/500, 14/125, 11/250, 1/20 | PASS |
| **G-L** | L_Θ recomputed as D(Im(h₂/z))[μqz] equals the adopted Cartesian L_Θ. D₃ = 2Re(z̄h₂) equals the adopted trigonometric D₃ | PASS |
| **G-D** | Im(F₄W̄) = Λ₃\|W\|² exactly; F₃ = μ\|W\|²W | PASS |
| **P-c** | ε = e₂\|W\| + e₃\|W\|² at \|W\| = 47/1000 (U_T ⊂ {Q < 2209/10⁶}, PRIM-CTR). e₂, e₃ come from \|η − sin η\| ≤ \|η\|³/6, \|e^ρ − 1 − ρ\| ≤ e^{\|ρ\|}ρ²/2 and \|ρ\|, \|η\| ≤ (2/√3)\|W\|. Gates: ε < 1/2, and 36ε² < π_lo²(1 − ε²) (the six-step window). B2 on row A: \|J/z − 1\| ≤ U = 0.00315 and \|F̂/J − 1\| < 1/2, so the arguments add and nothing vanishes | PASS |
| **P-L** | sup_Θ\|Λ₃\|/r³ ≤ 1401/1000, by 401 rational points of the unit circle (t = 2 arctan s, s ∈ [−1, 1]; odd harmonics give \|g(t + π)\| = \|g(t)\|) and cells bounded with \|g″\| ≤ L₂. Certified cell bound 1.400397; largest point value 1.400306 (a lower estimate of Λ*) | PASS |
| **P-a** | D̄₃ = 387/500 by the same method (cell bound 0.773457). Moduli of the exact polynomial D_Q in degrees 3–12, evaluated at s = 1/20: c′_Q = Σ_{d≥4} m_d s^{d−4}, c_Q = D̄₃ + Σ_{d≥4} m_d s^{d−3}. The degree-3 part of D_Q equals z̄h₂ + z·conj(h₂) | PASS |
| **P-b** | Im Log(1 + u), u = μq + a₃₂q² + a₀₅q²e^{−6iΘ}. The exact q² coefficient 89√3/324 + Im(a₀₅e^{−6iΘ}) is bounded by 89√3/324 + \|a₀₅\|. The cross term \|u² − μ²q²\|/2 and the Log remainder \|u\|³/(3(1 − \|u\|)) are evaluated at q = 1/400 (all monotone) | PASS |
| **P-7** | arcsin x ≤ (π/2)x; \|J\| ≥ \|z\|(1 − U) | PASS |
| **S-T** | Imported pins: radius 1/20, C₇ = 100, K_Θ = 123/125 | PASS |
| **FIN** | C_* ceiling and all gates | PASS |

| Negative control | Must fail | Result |
|---|---|---|
| N1 | sign of S_Θ flipped (Λ₃ := −L_Θ + τD₃) breaks G-D | fails |
| N2 | τD_Q omitted (Λ₃ := L_Θ) breaks G-D | fails |
| N3 | bridge removed: "q ≤ Q on row A" is false (D₃ < 0 on the positive real axis) | fails |
| N4 | row-B pins (K_Θ = 909/1000, C₇ = 30) in row A | fails |
| N5 | Λ̄ = 1400/1000 (below the true maximum) | fails |
| N6 | one-step bound × 12 leaves the (π, 3π) window | fails |

## 4. Illustration

`[NUM]`; not a proof input. Script `lphase_rowA_numeric.py`, output `lphase_rowA_numeric.json`.

| Sample | sup \|r\|/Q^{3/2} |
|---|---|
| Circle Q = 1/625 (top of U), 2400 angles | 1.42849 |
| Circle Q = 10⁻⁴ | 1.40747 |
| Circle Q = 10⁻⁵ | 1.40259 |
| NUMGEN seed orbit, 20 000 blocks | **1.35035** |

All values are below C_* = 1.612; the slack is about 13% at the top of U.

The seed-orbit value 1.35035 falls inside NUMGEN's measured range [1.3449, 1.3565]. This confirms the explanation of the scope note: NUMGEN's figure is orbit-sampled, while the sup over all angles tends to Λ* ≈ 1.4003. Following the review, this is **not** recorded as a NUMGEN coefficient correction.

## 5. Scope and guards

- **Imports**, at their adopted grades:
  - DYAD-THM-PRIM-CTR: tube, F(U) ⊂ U, U_T ⊂ {Q < 2209/10⁶};
  - DYAD-THM-NF-INV and DYAD-THM-NF-REM: chart, tube → |z| < 1/20, C₇ = 100;
  - DYAD-THM-OPEN3-SPIRAL-REM: K_Θ, row A;
  - the OPEN 3 definitions: S_Θ as real numbers, |h/z − 1| < 1/16;
  - DYAD-ALG-NF6: h and J, regenerated (G-H).
- **Provenance limit.** The regenerated h is identified with the adopted one through the uniqueness of the convention and the G-H checks. A coefficient-by-coefficient comparison with `jets.h_degree6` of the P2B v2 `certificate.json` was not repeated in this session (the file is not in this workspace). It is a cheap gate to add when the certificate is replayed on the owner/PI machine.
- **Lift convention.** φ̂ is taken as the sum of principal one-step angles. This is NUMGEN's L-MONO lift (δ_T ∈ (π/6, π/2)); NUMGEN should confirm.
- **SG-19.** Satisfied: the target is primitive Q; q is used only inside the computation; the final statement goes through the explicit P-a1 bridge; no coefficient is transferred to NUMGEN L1 or to the ISP angle.
- **Ownership.** L-PHASE and L1 stay NUMGEN-owned. C_* is a DYAD-certified constant offered as a separate import.
- **Not claimed:**
  - optimality;
  - row B (separate, later);
  - any statement beyond the first-order block law;
  - any change to NUMGEN's grades;
  - any φ* statement;
  - any effect on OPEN 20.

**Status unchanged:** DYAD v6.4.18 adopted; OPEN 20 PARTIAL; B-an and B-6 OPEN.

## 6. Files

| File | SHA-256 |
|---|---|
| `dyad_numgen_lphase_rowA_cert.py` | `117484ae1a2509b6f6065d395840bfdfe2b0c977af0505f9fe6de68c13959cdb` |
| `tzw.py` | `f007d42cde36d2a70115b9db25f47b107c446735fa31c66664f620c3247a5609` |
| `qw.py` | `3a913062c1cdc6d151a2fb5b2f76d5354a367d1fa55df43f1f31d06e1b94cce8` |
| `lphase_rowA_certificate.json` | `8697c6970bd908327c66ef2ce3b2d38386947899033ef7f720bc096c4c3ad4fa` |
| `lphase_rowA_numeric.py` | `95b891f8f62b42342c0307e77b0f8c13e68cc7f5a3b9d368b18a1a3e4c3a4647` |
| `lphase_rowA_numeric.json` | `2291db4e1404654427b567bdba338ea1ce0ddd0b7f4e8bad1bd8b03b16d1b9c4` |

**Command:** `python3 dyad_numgen_lphase_rowA_cert.py`. Expected output: exit 0 and `RESULT: PASS`.
