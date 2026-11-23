# DYAD OPEN 3 — observable transport and spiral residual: scope note (v0.1.1)

**Date:** 19 October 2026 · **Author:** Claude (Dyadic DSN owner/editor) · **Status:** `[SESSION]` scope note. No computation campaign and no new certificate were run. No owner file is modified. **Supersedes:** v0.1 (SHA-256 `e02dc487ab32b69b74d691ccdb5472753919996359b980cd07e58480e7a92c13`), reviewed 19 Oct: `ACCEPT WITH CORRECTION`.

**Changes from v0.1 (review correction only):**
- §3: the v0.1 identity "[S_Q]₅ = P₅ transported" was wrong. It omitted the degree-5 cross term from −Q² versus −q². It is replaced by [S_Q]₅ = [P₅∘𝓛⁻¹∘h]₅ − 2q·D₃ (reviewer's correction). The radial bound statement is also narrowed: PRIM-CTR alone does not bound the transported S_Q remainder, and the Q ↔ q bridge must be used explicitly.
- §3a (new): a light exact-symbolic sanity check of the corrected identity, with negative controls. It is not the P2 gate.
- §0, §4 (M-1, new M-3r), §5 (P0 BLOCKED, P2, closure shape): updated to match.
- §2, §4, §4a: unchanged apart from fixing ω = e^{2πi/3}.

**Authorization:** PI decision of 19 Oct 2026 — scope work only. No adoption, no heavy computation, and no change to DYAD v6.4.13.

**Standing constraints (PI, 19 Oct):**
- C1. The geometric origin of the spiral residual (`[ALG structure]`) and a certified bound on it along all orbits are separate claims. The first is not promoted to `[THM]` by this note.
- C2. The numerical fit in `spiral_phase_fit.py` does not define the theorem. The observable and the inequality to be proved are stated independently of any fit (§2–§4).

**OPEN 20** remains PARTIAL (B-an, B-6, B-∞ existence OPEN). Work on OPEN 3 does not touch it.

## 0. Sources and their state

| Source | Version / identity | Used for |
|---|---|---|
| DYAD | v6.4.13 adopted, `5958f7fe…b968542` | OPEN 3 entry (§2); SG-1, SG-2, SG-7, SG-9, SG-19; §6.4 ISP coordinates; §6.5 burst; §6.14 NF6, PRIM-CTR, NF-INV, NF-REM; §8 artifact `DYAD-ART-SPIRAL-FIT` |
| RECOG | v0.3.20 (freeze candidate) | §6.13a `RECOG-THM-R9-MEMORY` (C_z track); §6.14 `RECOG-ALG-CHART-LAWS`; SG-R13, SG-R14 (track typing) |
| NUMGEN | v1.20.7 | L1 primitive radial identities (ΔQ₄ = −Q², ΔQ₅ = P₅, phase harmonic A(φ)); F1 correction ("Q_NF = Q_true" is false) |
| RRF | v0.8.2 (v0.8.3 adopted 19 Oct; the cited rows are unchanged) | §2.4 / §4.1a: comparator tracks C_W, C_z, C_W^{(h)}; transports are pullbacks, not identifications |
| `spiral_phase_fit.py` | **not available**: not in this session and not found in the accessible project files (reviewer, 19 Oct) (registered as `[ENG]`, DYAD §8) | not used; P0 is `BLOCKED — historical artifact unavailable` (§5) |

**Gap recorded.** The historical script and its exact residual definition, window and fitting ansatz could not be inspected. §2 therefore defines the object from first principles. The match to the historical fit is a separate, later check (§5, item P0). Under C2 this is acceptable: the theorem target must not depend on the script.

## 1. What the adopted record says about OPEN 3

- **DYAD OPEN 3 (§2).** "Mechanistic origin identified: geometric projection from 2Re(W̄h₂) `[ALG structure]`. Theorem-grade Taylor remainder bounds remain `[OPEN]`."
- **SG-9.** "The per-block phase residual carries an O(√Q) spiral contribution dominating the O(Q) quintic phase signal." Both orders are relative to the leading per-block phase step −τQ.
- **SG-7.** C_est / κ_est are window-dependent; window-dependent fit quantities are not certification objects.
- **SG-19.** Coefficients are not transferred between the raw, archival, projected and conjugacy objects.
- **NUMGEN F1.** Q_NF = |W|² = Q_true is false in the primitive frame. The frame correction starts at relative order O(√Q_true).

**Reading.** The spiral residual is the visible difference between primitive (ISP) observables and normal-form observables. It is produced by the non-identity chart h. It is a chart effect, not a dynamical term of the normalized return.

## 2. Definitions `[DEF]`

**Frames.**
- Primitive state x = (ρ, η), lifted, with |η| < π locally. Raw linear frame W = 𝓛x = ρ + ωη, with ω = e^{2πi/3}, i.e. W = ρ − η/2 + i(√3/2)η (DYAD §6.14), so Q = ρ² − ρη + η².
- Primitive amplitude Q := Q_prim = |W|². This equals Q_true when η = η_wrap (SG-1).
- Primitive phase Θ_W := continuous lift of arg W. The ISP angle Θ of DYAD §6.4 is arg W up to the fixed π/6 rotation of the anti-correlation frame, so differences in Θ and Θ_W agree.
- Normal-form chart W = h(z), with h the adopted degree-6 polynomial normalizer (`DYAD-ALG-NF6`), on |z| ≤ 1/10 (`DYAD-THM-NF-INV`).
- q := |z|². Θ_z := continuous lift of arg z.

**Dynamics.** One six-step block (SG-2): x ↦ T⁶x, i.e. W ↦ F_W(W) and z ↦ F̂(z) = h⁻¹ F_W h (z). The identity W_m = h(z_m) holds for every block index m along every orbit inside the certified domains. This is exact, not approximate.

**Static chart offsets** (functions of the state, not of the dynamics):

  D_Q(z) := |h(z)|² − |z|² = Q − q,
  D_Θ(z) := arg(h(z)/z) ∈ (−π/2, π/2) = Θ_W − Θ_z, using the principal branch; |h(z)/z − 1| ≤ M(s)/s < 1/16 on |z| ≤ 1/10 (NF-INV).

The lifts of Θ_W and Θ_z are chosen consistently: Θ_W(x_m) = Θ_z(z_m) + D_Θ(z_m) for all m.

**Per-block increments.**
- Primitive: ΔQ(x) := Q(T⁶x) − Q(x) and ΔΘ_W(x).
- Normalized: Δq(z) := |F̂z|² − q and ΔΘ_z(z).

**Spiral residual (primary object).**

  S_Q(z) := ΔQ − Δq = D_Q(F̂z) − D_Q(z),
  S_Θ(z) := ΔΘ_W − ΔΘ_z = D_Θ(F̂z) − D_Θ(z).

Both identities follow directly from W_m = h(z_m). They give the residual a definition with no fit, no window and no backbone. This is the object of C2.

**Leading structure `[ALG structure]`** (to be verified exactly in step P2; recorded as structure, not as a theorem):
- D_Q(z) = 2Re(z̄ h₂(z)) + O(|z|⁴). This is the "2Re(W̄h₂)" origin of the DYAD OPEN 3 entry. It is cubic: harmonics e^{±iΘ} and e^{±3iΘ}, since h₂ has z², zz̄, z̄².
- D_Θ(z) = Im(h₂(z)/z) + O(|z|²). This is O(√q), with the same harmonics.
- Per block, F̂z − z = μ q z + O(|z|⁵) (NF-REM / J). So S_Q = O(q^{5/2}) and S_Θ = O(q^{3/2}). Relative to the leading terms −q² and −τq, both are O(√q). This matches SG-9.

## 3. Radial part: adopted inputs and the corrected transport identity

The radial spiral term is closely tied to an adopted theorem, but it is not the same object as that theorem's quintic term.

- **`DYAD-THM-PRIM-CTR` (§6.14).** It works directly in primitive variables. In Q(T⁶x) = Q − Q² + P₅ + P₆ + P₇ + R_{≥8}:
  - P₅ = (Q/24)(5η³ − 43η²ρ + 4ηρ² − 5ρ³) is exact, with ceiling |P₅| ≤ 1.6931 Q^{5/2};
  - P₆ and P₇ have exact ceilings;
  - |R_{≥8}| ≤ 42355 Q⁴ on Q ≤ 1/400;
  - the combined |R_{≥6}| ≤ 108 Q³.
- **Normalized side.** The normalized radial law is |J|² = q − q² + O(q³) (RECOG-ALG-CHART-LAWS). Its q^{5/2} coefficient is zero because J is odd. Also |F̂|² − |J|² = O(|z|⁸) (NF-REM).

**Corrected transport identity `[ALG — SESSION]`** (v0.1.1; reviewer's correction). Write Q = q + D_Q with D_Q = D₃ + O(|z|⁴) and D₃ := 2Re(z̄h₂(z)). Then Q² = q² + 2qD₃ + O(|z|⁶). Subtracting the normalized law from the primitive one gives, at homogeneous degree 5:

  [S_Q]₅ = [P₅∘𝓛⁻¹∘h]₅ − 2q·D₃ = P₅(𝓛⁻¹z) − 2q·D₃(z).

The second equality holds because h = id + O(|z|²) and P₅ is homogeneous of degree 5. From the chart side (§2), [S_Q]₅ = D(D₃)(z)[μqz], where D is the real derivative. So the identity to be certified in P2 is

  **(I-5)** P₅(𝓛⁻¹z) = D(D₃)(z)[μ q z] + 2q·D₃(z).

**P₅ and S_Q are different objects.** P₅ is the degree-5 term of the primitive radial increment. S_Q is the difference between the primitive and normalized increments. The cross term −2qD₃ from −Q² versus −q² must be kept. Read with this term, (I-5) makes the 2Re(W̄h₂) origin of DYAD OPEN 3 explicit at radial order 5/2. It does not promote that origin (C1) until P2 passes and is reviewed.

**Radial bound, narrowed.** PRIM-CTR's 108Q³ bound controls the primitive increment only. It does not by itself give a certified bound for the transported remainder S_Q − [S_Q]₅. That bound needs three adopted inputs used together:
- PRIM-CTR on the primitive side;
- the normalized radial remainder (|J|² law, NF-REM C₇ / C_D);
- the explicit Q ↔ q bridge D_Q, with NF-INV bounds 225/256 q ≤ Q ≤ 289/256 q and the M(s) majorant for D_Q − D₃.

This is item M-3r (§4). No new primitive-map campaign is needed for it.

### 3a. Sanity check of (I-5) `[ALG — SESSION; not the P2 gate]`

A short exact-symbolic check (sympy, seconds) was run while preparing this correction. The script is `dyad_open3_p5_sq_identity_sanity.py`, SHA-256 `9ded29aa0484d695abc1d09e0e57312924a456bb52d3381214300b9fda5614d7`. It exits 0 only if the main identity holds and every negative control fails.

Inputs:
- h₂ = −(1+i√3)/12 z² − ⅓zz̄ + (1−i√3)/24 z̄² (NF6);
- μ = −½ − i·2√3/3;
- ω = e^{2πi/3} (§6.14).

| Check | Result |
|---|---|
| (I-5) as stated | holds identically |
| without +2qD₃ (the v0.1 form) | fails |
| with −2qD₃ | fails |
| with ω = e^{−2πi/3} | fails |

**Status.** This confirms the reviewer's correction and fixes the frame branch. It is a SESSION check by the author, not an independent replay. P2 remains the gate: an exit-gated script, independent review, and the degree-5 angular companion identities.

## 4. What is open: the angular spiral residual

**Target theorem (T-OPEN3-Θ), formulation only.** For 0 < q ≤ q_max on a certified row of NF-REM (|z| ≤ 1/20 or 1/40, rows not mixed), and for every z in the row's forward-invariant domain:

  |S_Θ(z) − L_Θ(z)| ≤ K_Θ q²,

where:
- L_Θ(z) is the explicit leading term of order q^{3/2}: L_Θ(z) = D(D_Θ)(z)·[μ q z], with D_Θ replaced by its leading part Im(h₂(z)/z). It is a trigonometric polynomial in Θ_z times q^{3/2}, to be computed exactly over ℚ(i√3).
- K_Θ is an explicit rational constant for each row.

Equivalently, at the primitive level, the per-block phase increment is

  ΔΘ_W = −τ q + L_Θ + O(q²) (certified).

Here −τq is the normalized leading phase step (RECOG-ALG-CHART-LAWS: arg(J/z) = −τq + O(q²)), and q can be rewritten in Q using D_Q.

**Proof route (chart route; no new primitive campaign):**
1. **Exact identities** (§2): S_Θ = D_Θ∘F̂ − D_Θ. Pure algebra.
2. **Static offset with remainder.** |D_Θ(z) − Im(h₂(z)/z)| ≤ c₁|z|² and a derivative bound ‖D(D_Θ)‖ ≤ c₂ on the row. Inputs: the NF-INV majorant M(s) = 7/12 s² + 39/500 s³ + … (coefficient-modulus ceilings of h − id; degree 2 exact) and M′(s), plus the log/arg bound |arg(1+u) − Im u| ≤ |u|²/(1−|u|) for |u| < 1/16.
3. **Block displacement.** F̂z − z = μqz + (J − z − μqz) + (F̂ − J), with J explicit (degree ≤ 5) and |F̂ − J| ≤ C₇|z|⁷ (NF-REM; C₇ = 100 or 30 by row).
4. **Taylor step.** S_Θ = D(D_Θ)(z)[F̂z − z] + second-order term. The second-order term is bounded with the derivative bounds of step 2 extended to a second derivative of h. NF-INV gives M″(R) at R = 1/10. Rows at r = 1/20 or 1/40 sit inside R = 1/10, so Cauchy-type majorant bounds apply.
5. **Collect.** L_Θ is the leading part; everything else is O(q²), with an explicit constant.

**Missing lemmas / certificates:**

| ID | Item | Grade target | Inputs | Effort |
|---|---|---|---|---|
| M-1 | Exact leading polynomials: [D_Q]₃ = D₃ = 2Re(z̄h₂), [D_Θ]₁, L_Θ; the corrected identity (I-5) P₅(𝓛⁻¹z) = D(D₃)[μqz] + 2qD₃ (§3; sanity-checked §3a) | `[ALG]` exact ℚ(i√3) | h₂ (NF6), μ | light, exact-symbolic |
| M-3r | Certified radial remainder |S_Q − [S_Q]₅| ≤ K_Q q³ per row, from PRIM-CTR + normalized radial remainder + explicit Q ↔ q bridge (§3) | `[THM]` | PRIM-CTR, NF-REM, NF-INV, M(s) | light to moderate; exact-rational |
| M-2 | Static offset remainder constants c₁, c₂ (and second derivative c₃) on each row | `[ALG]` exact-rational from M(s) | NF-INV majorant | light |
| M-3 | Remainder constant K_Θ per row | `[THM]` (analytic majorant + exact-rational arithmetic) | M-1, M-2, NF-REM (C₇, C_D) | light to moderate; exact-rational script, can run on the PI machine |
| M-4 | Primitive asymptotic-phase transfer (§4a) | `[ALG]` | R9, D_Θ, D_Q | light |
| M-5 | Consistency audit against the historical fit (§5 P0) | `[NUM]` only | `spiral_phase_fit.py` and its outputs | needs the script |

Nothing here needs new primitive-map interval arithmetic. All analytic inputs are adopted DYAD certificates.

### 4a. RECOG R9 in primitive variables `[ALG — SESSION observation; to verify in M-4]`

`RECOG-THM-R9-MEMORY` is proved on the C_z track, for Ψ = Θ_z − τ log q. Define the primitive analogue Ψ_W := Θ_W − τ log Q. Then

  Ψ_W(x_m) − Ψ(z_m) = D_Θ(z_m) − τ log(1 + D_Q(z_m)/q_m) = O(√q_m) → 0,

so Ψ_{W,∞} = Ψ_∞: the asymptotic phase is chart-independent. Hence

  M_W(x₀) := Ψ_{W,∞} − Ψ_W(x₀) = M(z₀) − [D_Θ(z₀) − τ log(1 + D_Q(z₀)/q₀)].

The bracket is a static O(√q₀) offset, larger than M's own O(q₀) leading term.

**Consequences:**
- (i) In primitive variables the retained memory is dominated by a known chart offset, which is a function of the initial state. Only after subtracting it does the R9 lattice term appear.
- (ii) This is consistent with RECOG's refusal (SG-R14) to apply R9 directly on the raw C_W^{(h)} track. It also suggests how a raw-track statement could be obtained: R9 plus the explicit offset. No such statement is made here.
- (iii) It explains SG-9 at the memory level, not only per block.

## 5. Proposed proof order

| Step | Content | Output | Gate |
|---|---|---|---|
| P0 | Compare with the historical `spiral_phase_fit.py` definition, window and ansatz | provenance note | **`BLOCKED — historical artifact unavailable`**. This does not block P1–P4, which are fit-independent (C2). It reopens only if the script resurfaces |
| P1 | Fix the objects of §2 in owner wording | definitions | review |
| P2 | M-1 exact symbolic identities, including the corrected (I-5) | exit-gated script, light; negative controls include deliberately dropping the −2qD₃ cross term | PASS |
| P3 | M-2, M-3 and M-3r exact-rational constants per row | certificate script; heavier parts can run on the PI machine (Windows/PowerShell) | PASS; constants stated per row, not mixed |
| P4 | M-4 asymptotic-phase transfer | short proof | review |
| P5 | SESSION proof record → external review → DYAD successor proposal (OPEN 3 → CLOSED or PARTIAL) | record | owner/PI decision |

**Expected closure shape.**
- Radial part: (I-5) at order 5/2, plus the certified remainder M-3r, which uses PRIM-CTR together with the Q ↔ q bridge. It is not an identification of S_Q with P₅.
- Angular part: T-OPEN3-Θ with explicit L_Θ and K_Θ per row.
- If M-3 constants come out too weak to be useful on the R9 rows, OPEN 3 is recorded PARTIAL with the exact leading terms. The geometric origin stays `[ALG structure]` until M-1 makes it exact (C1).

## 6. Explicitly not claimed

- No new inequality or constant is asserted in this note. (I-5) is a SESSION algebraic identity with an author sanity check only.
- The `[ALG structure]` origin is not promoted.
- No identification Q ↔ q, Θ_W ↔ Θ_z beyond the stated offsets (NUMGEN F1; RRF pullback rule).
- No statement on the window-dependent fit quantities C_est and κ_est (SG-7).
- No transfer of 47/54, c_θ^{(6)}, a₁ or a₂ into the chart (SG-19).
- No effect on OPEN 20, G2 or any physical reading.
