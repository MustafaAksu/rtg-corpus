# DYAD OPEN 3 — P1 definitions and P2 exact symbolic gate: SESSION record (v0.1)

**Date:** 19 October 2026 · **Author:** Claude (Dyadic DSN owner/editor) · **Status:** `[SESSION]`. All results below are `[ALG — SESSION]`. Owner adoption is a separate review step. DYAD v6.4.13 is unchanged. OPEN 3 stays OPEN: there is no `[THM]` promotion, and the `[ALG structure]` origin is not promoted. OPEN 20 stays PARTIAL.

**Authorization:** PI / reviewer decision of 19 Oct, "SESSION REVIEW PASSED", approving P1 and P2.

**Base documents:**
- `DYAD_OPEN3_OBSERVABLE_TRANSPORT_SCOPE_SESSION_v0_1_1.md` (SHA-256 `4526546ad6a99835a9fe2cddd8a6b63d2134ce89d0e9a405e2b601ccf8e6c1ab`);
- adopted `RTG_DYADIC_OSCILLATOR_DSN_v6.4.13` (`5958f7fe…b968542`).

**Artifacts:**

| File | SHA-256 | Role |
|---|---|---|
| `dyad_open3_p2_exact_gate.py` | `89939581d553483de0793b17c6e4b65748291e158e6db218bf1a0c2883b10c50` | exit-gated exact script (sympy, ~35 s); exit 0 iff all main checks hold and all negative controls fail |
| `p2_coefficients.json` | `c24389c94f5d77a674374aabc8cef75f7f5781e821a81d65700e1c2f8151f3dc` | the script's output: check table and exact coefficients |

## 1. P1 — fixed definitions `[DEF]`

These replace §2 of the scope note as the working definitions. The content is the same; the conventions are made explicit.

**P1-1. Block counter.**
- m counts six-step blocks F = T⁶ (SG-2). One block in the normalized chart is z ↦ F̂(z) = h⁻¹∘F_W∘h(z).
- W_m = h(z_m) holds exactly for every m while the orbit stays in the certified domains (NF-INV |z| ≤ 1/10, |W| ≤ 9/100; NF-REM rows).

**P1-2. Frames and amplitudes.**
- Primitive frame: W = ρ + ωη with ω = e^{2πi/3}, so Q := Q_prim = |W|² = ρ² − ρη + η².
- Normalized coordinate: z, with q := |z|².
- Q and q are different functions. They are related only through D_Q (NUMGEN F1; RRF pullback rule).

**P1-3. Per-block angle increments are principal, not wound.**
- Over the six intermediate steps of a block, arg W turns through about 2π, since the linear part of T has eigenvalue λ = e^{iπ/3}. That winding is excluded by definition. The increments are:

  ΔΘ_W := Arg(W_{m+1}/W_m),  ΔΘ_z := Arg(z_{m+1}/z_m),  principal values in (−π, π).

- In the certified domains both are O(q), and the intermediate steps play no role.
- The ISP angle of DYAD §6.4 differs from arg W by a fixed rotation, so it has the same increment.

**P1-4. Static offsets.**
- D_Q(z) := |h(z)|² − |z|².
- D_Θ(z) := Arg(h(z)/z). It is well defined because |h(z)/z − 1| < 1/16 on |z| ≤ 1/10 (NF-INV), which gives |D_Θ| < arcsin(1/16).

**P1-5. Spiral residuals: the two primary objects.**

  S_Q(z) := ΔQ − Δq = [Q(W_{m+1}) − Q(W_m)] − [q_{m+1} − q_m] = D_Q(F̂z) − D_Q(z),
  S_Θ(z) := ΔΘ_W − ΔΘ_z = D_Θ(F̂z) − D_Θ(z).

- **S_Q** is the difference of **absolute** per-block radial increments. It is not a relative or logarithmic difference.
- **S_Θ** is the difference of **per-block angle increments**.
- The second equality in S_Θ holds as real numbers, not only mod 2π. All four angles involved are below π/2 in modulus on the certified domains.

**P1-6. Status of fit residuals.**
- S_Q and S_Θ are not identified with any numerical fit residual (scope note C2).
- P0, the comparison with the historical `spiral_phase_fit.py`, stays `BLOCKED — historical artifact unavailable`.

## 2. P2 — exact results `[ALG — SESSION]`

All four objects below depend only on h₂ (DYAD-ALG-NF6) and μ = −½ − i·2√3/3:
- the degree-3 part of D_Q;
- the degree-1 part of D_Θ;
- [S_Q]₅ = D(D₃)[μqz];
- [S_Θ]₃ = L_Θ.

The reason is that h_k with k ≥ 3 and F̂ − z − μqz = O(|z|⁵) enter only at higher degree. Formulas are in normalized polar form z = r e^{iΘ_z}, q = r², per F-block. Harmonics are in Θ_z.

**M-1a. Leading static offsets.**

  D₃ := [D_Q]₃ = 2Re(z̄ h₂(z)) = r³ [ −(5/6) cos Θ + (√3/6) sin Θ + (1/12) cos 3Θ − (√3/12) sin 3Θ ],
  D_{Θ,1} := [D_Θ]₁ = Im(h₂(z)/z) = r [ −(√3/12) cos Θ + (1/4) sin Θ − (√3/24) cos 3Θ − (1/24) sin 3Θ ].

**Checks:**
- D₃ was obtained by series expansion of |h|² − q with h truncated after h₂.
- The Arg → Im step was checked at linear order.
- The harmonic form was reconstructed back to the polynomial form.

**M-1b. Radial identity (I-5), reproduced.**

  P₅(𝓛⁻¹z) = D(D₃)(z)[μ q z] + 2q·D₃(z),
  [S_Q]₅ = D(D₃)[μqz] = r⁵ [ (11/12) cos Θ − (29√3/36) sin Θ + (3/8) cos 3Θ + (7√3/24) sin 3Θ ].

[S_Q]₅ was computed two ways: as a directional derivative and by series in t. The two agree.

**M-1c. Angular leading term.**

  L_Θ(z) := D(D_{Θ,1})(z)[μ q z] = Im( μ c₂₀ q z + μ̄ c₁₁ q z̄ + (2μ̄ − μ) c₀₂ z̄³ ),

with h₂ = c₂₀z² + c₁₁zz̄ + c₀₂z̄². Explicitly:

  L_Θ = −(√3/48) X³ − (47/48) X²Y − (7√3/16) XY² − (1/16) Y³   (z = X + iY)
      = r³ [ −(√3/8) cos Θ − (7/24) sin Θ + (5√3/48) cos 3Θ − (11/48) sin 3Θ ].

- **Checks.** L_Θ was computed three ways, which agree: the real directional derivative, the monomial formula (a μ + b μ̄ for z^a z̄^b), and series in t. [S_Θ]₃ = L_Θ.
- **Harmonic content.** All four objects contain only the harmonics k = ±1, ±3, as predicted in scope §2. This was checked by Fourier reconstruction.

**Exact ceiling** (by the triangle inequality on the harmonic coefficients):

  |L_Θ| ≤ ((7 + 2√19)/24) q^{3/2} ≈ 0.6549 q^{3/2}.

**Consequence for SG-9** (leading order only):

  |L_Θ| / (τq) ≤ ((7 + 2√19)/(16√3)) √q ≈ 0.567 √q.

This is the quantitative leading form of SG-9's "O(√Q) spiral contribution" in the normalized chart. It is not a certified statement about the full S_Θ; that needs the remainder K_Θ (P3). A sampled supremum of |L_Θ|/r³ ≈ 0.6494 (200 001 points) is `[NUM]` illustration only.

**Negative controls** (all fail, as required):

| Control | Result |
|---|---|
| N1: ω = e^{−2πi/3} in (I-5) | fails |
| N2: (I-5) without +2qD₃ | fails |
| N3: (I-5) with −2qD₃ | fails |
| N4: L_Θ with the direction sign flipped (−μqz) | fails |
| N5: L_Θ with μ ↔ μ̄ swapped | fails |

**Independence note.** The script uses one CAS (sympy). Each object is computed by two or three internally different methods. The script is not an independent replay by a second engine or author. Before owner adoption, an independent replay is requested, for example from the reviewer or in a different CAS.

## 3. Not claimed

- No remainder bound: K_Θ, K_Q, c₁–c₃ belong to P3 (M-2, M-3, M-3r). The target inequality |S_Θ − L_Θ| ≤ K_Θ q² remains `[OPEN]`.
- No promotion of the `[ALG structure]` origin. The exact leading terms are `[ALG — SESSION]` until reviewed.
- The harmonic coefficients above are in **normalized z coordinates and the F-block counter**. They are not the primitive phase coefficients (for example NUMGEN L1 A(φ)), the ISP-angle coefficients, or the fit quantities C_est and κ_est. No comparison or transfer is made (SG-7, SG-19).
- No effect on OPEN 20, G2, RRF or any physical reading.

## 4. Next steps (unchanged order)

1. External review of this record, with an independent replay of `dyad_open3_p2_exact_gate.py` or an independent re-derivation.
2. P3: exact-rational constants per NF-REM row (1/20 and 1/40, not mixed):
   - c₁, c₂, c₃ from M(s), M′, M″;
   - K_Θ;
   - the radial K_Q, from PRIM-CTR with NF-REM and the Q ↔ q bridge.

   Heavier parts can run on the PI machine.
3. P4: asymptotic-phase transfer (scope §4a).
4. Proof record, then review, then a DYAD successor proposal.
