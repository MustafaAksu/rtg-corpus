# OFN source review — ER-2B v0.3.1, Genesis v2.8.8, DYAD OPEN 3 (P1–P3), FMS ψ test (v0.1.1)

**v0.1.1 (19 Oct 2026):** corrections from the second co-owner's review (co-owner-accepted as v0.10 input, subject to these corrections). Two changes: (1) one chiral-coordinate convention fixed throughout (§0a); this repairs §1, §2, §4.1 and D5; (2) Genesis provenance guard: I-1 covers the raw family only, (H_prim) is not used to reach κ = 2, and the v2.8.8 byte-identity claim is labelled as release-checker reported (§3). Nothing else changed. v0.1 is superseded.

**Date:** 19 October 2026 · **Author:** Claude (OFN co-owner) · **Status:** `[SESSION]` single independent OFN-side source review. Input to OFN v0.10. No owner file is modified and no OFN decision is changed by this note: every "decision change" below is a proposal for joint co-owner agreement and PI adoption.

**Baseline OFN text:** `claude/OFN_REPLY_TO_FMS_MODEL_SELECTION_v0_7_2.md` (author's working copy SHA-256 `6044f43e78b267c08daf054c0b85c4b370a0f1ba317ed0d09774860a2a1c5b4c`; byte identity with the project copy to be confirmed by the second co-owner).

**Protocol.** Three layers are kept apart in every row: **[OWNER]** owner-adopted results; **[SESSION]** session inferences (including this review's own checks); **[PHYS-OPEN]** open physical interpretations. Single-dyad results are never transferred as network basin theorems.

## 0. Sources read

| Source | Status | Read |
|---|---|---|
| `RTG_ER2B_CONSOLIDATED_STUDY_v0_3_NONCANONICAL.md` (v0.3.1, frozen) | noncanonical reference record | full |
| `GENESIS_V2_8_8_RELEASE_RECORD.md`, adopted Genesis v2.8.8 `9abd3616…0f37` | [OWNER], maintenance release | release record (scientific payload byte-identical to v2.8.7 for §6.3a–b, SG-15/16) |
| `GENESIS_FMS_OFN_G2_MODEL_SELECTION_SCOPE_v0_1.md` | Genesis [SESSION] | full |
| `DYAD_OPEN3_OBSERVABLE_TRANSPORT_SCOPE_SESSION_v0_1_1.md`, `DYAD_OPEN3_P1_P2_SESSION_RECORD_v0_1.md`, `dyad_open3_p2_exact_gate.py`, `DYAD_OPEN3_P3_REMAINDER_PROOF_RECORD_v0_1.md`, `DYAD_OPEN3_P3_REVIEW_DISPOSITION_v0_1.md` | DYAD [SESSION]; P1–P3 externally accepted; owner adoption pending (proposed v6.4.14) | full |
| `FMS_PSI_QUINTIC_CONJUGACY_TEST_v0_1.py` | FMS [SESSION] | full; rerun |
| Not read: Genesis v2.8.8 occurrence disposition, `GENESIS_DYADIC_v6_4_13_CONSUMER_IMPACT_v0_1.md`, RRF v0.8.3 (the DYAD scope note reports it adopted 19 Oct) | — | — |

## 0a. Chiral-coordinate convention (v0.1.1)

v0.1 printed S in one mode convention while the surrounding OFN/Genesis text uses another, and left N implicit. Both conventions are internally consistent; they must not be mixed.

| Convention | Modes | N = Σ\|w_e\|² | S = Im(w₁w̄₂) | Pure chiral \|ρ\| = \|S\|/N |
|---|---|---|---|---|
| **OFN/Genesis (adopted here)**, Genesis §6.3a(d) | u = w₁ + λw₂, v = w₁ + λ̄w₂ | \|u\|² + \|v\|² | (\|u\|² − \|v\|²)/√12 | 1/√12 |
| Fourier (used in v0.1 checks) | w_e = uω^e + vω^{−e} | 3(\|u\|² + \|v\|²) | −(√3/2)(\|u\|² − \|v\|²) | √3/6 = 1/√12 |

Both rows checked numerically (random states on Σw = 0). The limit |ρ| → 1/√12 is therefore correct in either convention and agrees with the ER-2B bound S² ≤ N²/12; the three-fold mismatch noted by the second co-owner came from reading the Fourier S against the Genesis N. The sign attached to "u-axis" differs between conventions, so any chirality-sign statement must name its convention.

## 1. Checks run by this review

| Check | Result | Grade |
|---|---|---|
| FMS ψ test rerun from the project text | ALL PASS (6/6), exit 0 | replay, same code |
| **New:** `OFN_PSI_KAPPA_EXTENSION_v0_1.py` (SHA-256 `6566009c6ae8a9ca57a8e4a13bf42025cbd98f589f4f908fc477bc3fe1a25f88`) | ALL PASS (28/28), exit 0, ~20 s | `[ALG — SESSION]` |
| P2 core identities (M-1a, (I-5), L_Θ two ways, closed form of L_Θ, ceiling) with N1–N5 | PASS; all controls fail as required; sampled max \|L_Θ\|/r³ = 0.64938 < (7+2√19)/24 | own transcription, same CAS (sympy) |
| ER-2B A.4: ΔN = −½N² + 2S², ΔS = −⅓NS for f_e = μ(w_e\|w_e\|² − ⅓Σw_j\|w_j\|²) on Σw = 0 | PASS | `[ALG]` |
| **New:** relative chirality ρ = S/N: Δρ = S(1/6 − 2ρ²) + O(5) (convention-free: only S, N enter); in OFN/Genesis modes S = (\|u\|² − \|v\|²)/√12, N = \|u\|² + \|v\|² (§0a) | PASS | `[ALG — SESSION]` |

### 1.1 Content of the κ-extension

The FMS test works at κ = 1 on the closure plane 𝒞, which lies **outside** the OFN class-C range κ ∉ {0, 1, 2}. The extension reduces to the formal centre manifold of the closure mode, which is hyperbolic for |1 − κ| ≠ 1:

- ψ₃(c) = (1 − κ)/(κλ) · (n₂₁/3) Σ_e c_e² c̄_e, verified by direct three-edge construction (κ = 1/2, 3).
- The reduced cubic is κ-independent (corroborates OFN §3.4 "ψ₃ enters only through the linear part").
- The reduced quintic is the κ = 1 quintic plus a correction E_κ that is **independent of the chart parameter a**.
- **a ∈ ℝμ:** the single-dyad map N_a = g_a⁻¹ N g_a equals N **identically through degree 5**. The FMS "conjugate" verdict for a = μ, μ/6 is therefore trivial: the models coincide at this order (g_a agrees with an element of Cent(N) through degree 5).
- **a ∈ iℝμ:** formal conjugacy is obstructed on the reduced map for every sampled κ ∈ {1, 1/2, 3/2, 7/5, 3, −1}, with exactly one real obstruction direction. The obstruction is a non-vanishing minor that is rational in κ, so it holds for **all but finitely many κ**; the exceptional set is not computed.
- A conjugacy of the full maps maps the (unique) formal centre manifold to itself, so the reduced obstruction is an obstruction for the full transported models.

**Reading.** The transported class C is not a single model up to formal conjugacy: λ-equivariant cubic chart changes carry at least one genuine real modulus (the iℝμ direction), visible at quintic order. Scope: one-step formal conjugacy through degree 5, linearized stabilizer, sampled κ.

## 2. Focus 1 — ER-2B v0.3.1: does it change Q1–Q6?

**Verdict: no Q1–Q6 verdict changes.** ER-2B is noncanonical. Its only canonical content (C10) entered Genesis by independent rederivation.

| ER-2B item | Relation to OFN | Disposition |
|---|---|---|
| C17A "closure typing" (identity in an additive node carrier vs. modelling constraint); C15A/B, C19 (additivity is chart-relative) | Same position as Q1 (exact closure not universal), model declaration 3 and the RRF §0.3 passive-vs-model rule | Reference; supports Q1/Q2 |
| C09 collinear locus S = 0 is **not invariant** in the raw projected model (Ω⁺ = (5√3/24)t³ + O(t⁵)) | On the closure plane S = 0 ⇔ \|u\| = \|v\|, i.e. the OFN cubic separator. C09 is an exact raw (κ = 1) witness that this set is not invariant | Reference; consistent with "cubic-order separator only". It proves nothing for the transported class |
| A.4 / C20 σ = 1 endpoint = transported cubic (ν → μ, χ → 0) | Independent cubic-order cross-derivation of OFN §3.4 via a quadratic-chart route; reproduced here | Corroboration; cite as noncanonical in v0.10 §3.4 |
| C11/C20 "chirality attenuating" for σ > σ_in | Refers to **absolute** \|S\|. OFN's relative attraction concerns ρ = S/N: Δρ = S(1/6 − 2ρ²), so \|ρ\| grows towards 1/√12, the pure chiral axes, in either convention of §0a. No conflict | v0.10 must name the observable (§5, D5) |
| C13 local instability of the raw projected κ = 1 model | A1 is excluded on Q4 and Standard C, not on stability | Reference |
| C19 six-parameter quadratic carrier freedom | Sharpens the "other carriers" loophole of OFN §3.2 (§2.1) | New OPEN |

### 2.1 Session inference: the §3.2 argument over the C19 family `[ALG — SESSION; hand derivation, not script-checked]`

In a C19 chart with residual quadratic q̃ = ũw² + ṽww̄ + t̃w̄² and linear closure re-imposed, the §3.2 dimension-1 step becomes

  [Σ_e G_e]₂ = h̃₂ applied as c̃₂₀ Σc_e² w² + c̃₁₁ Σ|c_e|² |w|² + c̃₀₂ Σc̄_e² w̄², with c̃₁₁ = −ṽ/(λ − 1).

The dimension-2 step requires Σ_e q̃(u_e) ≡ 0 on 𝒞, which forces q̃ = 0.

- **Along the ER-2B σ-slice** (q̃ = (1 − σ)q_G): c̃₁₁ = −(1 − σ)/3 ≠ 0 for σ < 1. The §3.2 no-go extends to every σ < 1, so Standard C at cubic order selects σ = 1 within that slice.
- **In the full C19 family**, the quadratic-order necessary condition on equilateral lock lines (Σc_e² = 0) is only ṽ = 0. That is a codimension-2 (real) subfamily which §3.2 does not exclude. Its cubic-order (I = O(4)) and exact-invariance conditions are unchecked.

This is registered as OPEN-C19-L (§6). It does not alter the A1/A2 dispositions, which concern the raw carrier.

## 3. Focus 2 — Genesis v2.8.8

**[OWNER] facts.**
- This is a maintenance release.
- `GEN-THM-K3-PLANAR-FACTOR-NOGO`, `GEN-THM-K3-SIXSTEP-FACTOR-NOGO`, `GEN-THM-MEANFEEDBACK-SIXSTEP-NOGO` (γ ∈ ℝ∖{0,2}, under (H_spec); primitive-clock statement for the same γ-range under (H_prim)), `GEN-THM-CHIRAL-CUBIC-FACTOR-LEMMA`, SG-15 and SG-16.
- **Provenance (v0.1.1).** This review read the theorem statements and proofs of §6.3a, §6.3a.1, §6.3b and SG-15/16 directly in the project copy of v2.8.8. Byte identity of these blocks with v2.8.7, and the adopted hash `9abd3616…0f37`, are **reported by the Genesis release checker**; they were not independently re-hashed here.
- M2c is closed (`DYAD-ALG-NU5-P5`; not needed by OFN).
- J, Lemma F and F1–F3 are **not** imported by Genesis.
- Edgewise J^{×3} and R₀^{×3} do not preserve 𝒞 beyond linear order in the raw carrier.

| Question | Effect |
|---|---|
| FMS model classification | **None on verdicts.** OFN agrees with the Genesis scope note: Genesis is not on the exclusion path of OFN §4. Every exclusion rests on Standard C (PI), OFN §3.2, Q4, or κ = 0. Genesis enters only positively, as a Q6 certificate |
| OFN §3.1 grade | For the **raw family only**, the condition "conditional on 6S" is discharged at owner level. **Import:** cite the Genesis RIDs with exactly their owner scope: κ ∈ ℝ∖{0,2}, C³, with (H_spec) for the six-step family theorem and (H_prim) for the primitive-clock statement. (H_prim) is a hypothesis inside that range; it does **not** extend any statement to κ = 2. The transported class C is **not** covered by this import: its Q6 entry stays on the separate D-4 argument |
| Standard C | No effect; Genesis makes no Standard C statement |
| Physical carrier | No selection. The raw-carrier non-preservation result is consistent with OFN §3.2/§3.5: the lock symmetries live in the transported chart, not edgewise in raw coordinates. Not an argument for or against class C |
| D-4 (transferring the factor no-go to the transported family) | The only selection-relevant Genesis item. The Q6 entry of class C rests on it. This review's reduced-map check corroborates one link (κ-independent reduced cubic of chiral form) at formal level. The chain stays OFN `[ALG — formal; leading order]`. **OFN supports opening D-4 as a scoped Genesis item** |

**OFN co-owner answers proposed to the Genesis scope note §9** (for joint agreement):
- **(i) Regularity in Q6.** State Q6 at local C³, the class of every theorem used (§3.1, Lemma S, carrier independence). Passive decouplings below C³ are recorded as OPEN (D-2): "unproved, not refuted".
- **(ii) Why κ = 2 is excluded.** The closure-mode multiplier (1 − κ)λ = −λ lies on the unit circle. The closure direction is then non-hyperbolic, the §3.4 centre-manifold reduction (stated for κ ∉ {0, 2}) does not apply, and the raw family is resonant there. It is not a Q6 failure. In addition, for κ < 0 or κ > 2 the closure mode is **repelling** (|1 − κ| > 1). The formal class-C properties hold there, but the FMS stability statements apply only to 0 < κ < 2, κ ≠ 1 (D2).
- **(iii) Dynamical independence of the cycle defect.** Neither required nor prohibited. It is a diagnostic property; Q4 asks only for capacity.
- **(iv) Authoritative copy.** The project copy of v0.7.2 is the agreed handoff. Its SHA pin is to be fixed in v0.10.

## 4. Focus 3 — DYAD OPEN 3: transferability to FMS parabolic stability

**[OWNER] status.**
- DYAD v6.4.13 still lists OPEN 3 as OPEN.
- P1, P2 and P3 are externally accepted but **not owner-adopted**; promotion is proposed for v6.4.14.
- OFN can therefore cite them only as DYAD SESSION results until then.

| OPEN 3 result | Transferable to FMS? | Why |
|---|---|---|
| Static leading offsets D₃ = 2Re(z̄h₂), D_{Θ,1} = Im(h₂/z) | **Yes, edgewise, class-wide at leading order** (after v6.4.14) | They are functions of a single edge state. Class members differ by h′ = h∘g with g − id = O(3), which changes D_Q only from degree 4 and D_Θ only from degree 2 |
| Static constants c₁, c₂, c₃ | Only for the NF6 member chart | Member-dependent beyond leading order |
| Per-block T-OPEN3 bounds (K_Θ, K_Q, L_Θ, [S_Q]₅) | **On the exact lock surfaces only**, edgewise, conditional on the real surfaces (J) or within truncation order in the polynomial model | On 𝒮₀ and 𝒮_± each edge evolves by the isolated map (N ≅ T), so each edge orbit is a single-dyad orbit. Off the surfaces the per-edge block map includes −(κ/3)ΣN and is not F̂ |
| NF-REM forward invariance, C₇ rows, telescoping corollary | No | Network forward invariance is not established |
| Anything about convergence to the surfaces, the separator or basins | **No** | Single-dyad chart results; the protocol forbids the transfer |
| Method: exact-rational majorants, supremum at the row boundary, rows kept separate, negative controls | **Yes, as template** | Usable for the FMS remainder in Δlog(\|u\|²/\|v\|²) = ⅓(\|u\|² − \|v\|²) + O(4) |
| Adopted single-dyad radial and phase laws on the surfaces (chart laws, 245/216 = \|μ\|² + 2Re a₃₂; PRIM-CTR) | **Import (conditional)**: on-surface edge asymptotics q_m ~ 1/m with known log correction | [OWNER] DYAD v6.4.13 applied to single-dyad edge orbits; conditional on the real lock surfaces (J) |

### 4.1 New warning: a chart offset that imitates the rate law `[ALG structure — SESSION]`

Read chiral modes in raw coordinates W_e = h(z_e) instead of in the transported chart. On the exact surface where the transported mode vanishes (u = 0), the raw mode does not: u_W = O(|v|²), hence |u_W|/|v_W| = O(|v|) ∝ m^{−1/2} **exactly on the lock surface**. This is the same exponent as the parabolic approach rate |u|/|v| ≍ m^{−1/2}.

The coefficient is convention-dependent (§0a), so only the order is stated as the result:
- Fourier convention: u_W = c₂₀v² + O(|v|³), |c₂₀| = 1/6 (only the z² harmonic of h₂ survives the ω-projection).
- OFN/Genesis convention: |u_W|/|v|² depends on the phase of v (sampled values 0.10 and 0.28 at two phases; `[NUM]`), and the raw readout also violates ΣW_e = 0 at O(|v|²).

Consequences:
- A raw-readout rate test cannot tell "on the surface" from "approaching at the predicted rate".
- FMS rate estimates must use transported-chart modes, or subtract the static offset. This is the network analogue of NUMGEN F1 and DYAD OPEN 3 §4a.
- The existing FMS simulations run in the z-chart, so they are not affected.
- Which readout chart is physical is part of the open carrier question.

## 5. OFN v0.10 delta / impact table

| # | Category | Item | Layer | Action in v0.10 |
|---|---|---|---|---|
| I-1 | Direct import (raw family only) | Genesis v2.8.8 K3/6S/mean-feedback RIDs | OWNER (v2.8.8 identity as release-checker reported) | §3.1, raw family: replace "[ALG — conditional on 6S]" by the owner RIDs with their scope (κ ∉ {0,2}, C³, (H_spec)/(H_prim)); repin K3 note v0.3 → Genesis v2.8.8. Not applied to class C |
| I-2 | Direct import (conditional) | DYAD v6.4.13 single-dyad laws on lock-surface edges | OWNER, conditional on J | §3.4: on-surface edge asymptotics; labelled single-dyad, not network |
| R-1 | Reference | ER-2B A.4 cubic cross-derivation | noncanonical + reproduced | §3.4 corroboration |
| R-2 | Reference | ER-2B C09 non-invariance of S = 0 (raw) | noncanonical | §3.4 separator remark |
| R-3 | Reference | ER-2B C13, C17A, C15, C19, C20 | noncanonical | §2 and §3.2 context |
| R-4 | Reference | Genesis scope note (L1/L2/L3, bridge premise, D-1…D-4) | Genesis SESSION | adopt its attribution of §4 exclusions as OFN's own reading |
| R-5 | Reference until v6.4.14 | DYAD OPEN 3 P1–P3 (leading offsets, T-OPEN3) | DYAD SESSION, externally accepted | §4.1 readout guard; import after owner adoption |
| R-6 | Reference | FMS ψ test plus the OFN κ-extension | SESSION | §3.5(a) |
| D1 | Decision wording | Q6 regularity: local C³; below C³ OPEN | proposal | §1 Q6 |
| D2 | Decision wording | Class-C range: formal properties for κ ∉ {0, 1, 2}; stability statements for 0 < κ < 2, κ ≠ 1; reason for excluding κ = 2 recorded | proposal | §3.4, §4 |
| D3 | Decision content (canonicity) | §3.5(a): "remaining members not conjugate — withdrawn as unproved" → **non-conjugate members exist** (iℝμ modulus at quintic order: κ = 1 by FMS, generic κ by OFN); a ∈ ℝμ gives identical models through degree 5 | SESSION | §3.5(a), (c): class C is a family with ≥ 1 real in-class modulus beyond κ |
| D4 | Decision wording | §3.1 grade upgrade per I-1, raw family only; the transported-family factor transfer stays a Genesis review item / OPEN (O-6) | — | §3.1 |
| D5 | Decision wording | Chirality statements are relative (ρ = S/N or \|u\|/\|v\|) with the §0a convention fixed; raw-readout offset guard (§4.1) | SESSION | §3.4 |
| — | **Unchanged** | Q1–Q6 verdicts; Standard C at cubic order; A1/A2/B excluded; C the primary candidate, formal until J | — | — |
| O-1 | OPEN kept | True basin boundary and two-basin existence; conditional basin role of the coincidence surfaces | PHYS-OPEN / SESSION | — |
| O-2 | OPEN kept, sharpened | Rigorous parabolic rate: leading order class-invariant; quintic corrections and the basin boundary are **member-dependent** (D3) | SESSION | — |
| O-3 | OPEN kept | J realization (OPEN 20: B-an, B-6, B-∞ existence) | DYAD | — |
| O-4 | OPEN kept, sharpened | In-class chart (ψ) selection: now a genuine modulus, needing a physical criterion | PHYS-OPEN | — |
| O-5 | OPEN kept | Physical isolation reading of Standard C; physical chirality; OPEN-OPA; RRF OPEN-A | PHYS-OPEN | — |
| O-6 | OPEN kept | D-4 reduction chain for the transported family (Genesis scoped item supported); D-2 sub-C³ decoupling; closure-mode factor (D-3, "neither") | SESSION / Genesis | — |
| O-7 | **New OPEN** | OPEN-C19-L: the ṽ = 0 subfamily of C19 carriers is not excluded by §3.2 at quadratic order | SESSION | §3.2 scope |
| O-8 | Housekeeping | Pin RRF v0.8.3 after reading; v0.7.2 SHA pin; FMS to register the Standard C route and refresh R7 | — | — |

## 6. Non-claims

- No OFN decision is changed by this note.
- No single-dyad result is used as a network basin statement.
- No physical carrier, chirality or isolation reading is selected.
- The κ-extension is formal, through degree 5, at sampled κ ("all but finitely many κ" by rationality).
- OPEN-C19-L is a gap in an exclusion, not a candidate model.
