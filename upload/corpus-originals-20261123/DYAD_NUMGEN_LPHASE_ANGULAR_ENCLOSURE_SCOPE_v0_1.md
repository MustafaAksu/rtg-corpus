# DYAD → NUMGEN — L-PHASE angular remainder: explicit enclosure on row A (SCOPE, SESSION v0.1)

**Version:** v0.1 · **Date:** 20 October 2026 · **Author:** Dyadic DSN owner (Claude)

**Basis.** PI/reviewer decision of 20 Oct 2026 on the NUMGEN request note of the same date ("NUMGEN Requests v0.1"):
- DYAD takes ownership of P-a and P-b.
- A branch gate P-c is to be added.
- Work starts on row A (|z| ≤ 1/20, C₇ = 100).
- The algebraic decomposition is to be checked as an exact identity before any constant is computed.
- For now the work is limited to a scope note and light algebraic checks. No new `[THM]` and no owner adoption.

**Provenance limit.** The NUMGEN request note was not available to the owner. Its content is taken from the PI/reviewer summary. The PI is asked to supply the note so that its hash can be recorded.

**Status.**
- `[SESSION]` scope record. No constant (c_Q, c_J, C_*) has been computed or certified.
- DYAD v6.4.18 is unchanged; OPEN 20 PARTIAL; B-an and B-6 OPEN.

**Check script.** `lphase_scope_checks.py` writes `lphase_scope_checks.json` (deterministic; verified by rerun).
- 4 gates (S1–S4), 2 negative controls (N1–N2) and one informational output (S5).
- It is **not** a certificate. S1 and S2 are exact (sympy). S3–S5 are `[NUM]` (mpmath, 40–50 digits).

## 1. Target and objects

**NUMGEN L-PHASE** (v1.20.7, `[RESULT] [from: ALG]`, existential constant). For the increasing primitive angular lift φ̂ and block index m (F = T⁶),

φ̂_{6(m+1)} − φ̂_{6m} = 2π − τQ_m + r_m,  |r_m| ≤ C Q_m^{3/2}.

**Request:** replace C by an explicit certified C_* on a named tube.

**Objects.** The notation is that of DYAD v6.4.18 §6.14.
- **Primitive frame.** W = 𝓛(ρ, η), Q = |W|². Q_m is the **primitive** observable, not the chart q_m.
- **Chart.** W = h(z, z̄) (DYAD-ALG-NF6), q = |z|²; F̂ = h⁻¹F_W h, with J its jet.
- **Offsets and residual.** D_Q = |h(z)|² − q, D_Θ = Arg(h(z)/z), and the spiral residual S_Θ = ΔΘ_W − ΔΘ_z (DYAD-ALG-OPEN3-LEADING / DYAD-THM-OPEN3-SPIRAL-REM).
- **Angle increments.** ΔΘ_W = Arg(W_{m+1}/W_m) and ΔΘ_z = Arg(z_{m+1}/z_m) are principal values.
- **Domain (row A).** Every block base point F^m x with x ∈ U = {0 < Q ≤ 1/625} has z_m ∈ {|z| < 1/20}:
  - F maps U into U (DYAD-THM-PRIM-CTR);
  - the tube maps into the normalized disk, which is invariant (DYAD-THM-NF-REM).

  The canonical NUMGEN seed lies in U, so row A covers every block of every L-PHASE orbit started in U. Row B (|z| ≤ 1/40) is a separate, later strengthening and is not mixed with row A.

## 2. Exact decomposition

`[ALG — SESSION]`; checked as a definitional identity, with leading terms gated by S1/S2.

**Identity D.** Assume two branch conditions:
- **(B1)** φ̂_{6(m+1)} − φ̂_{6m} − 2π = ΔΘ_W;
- **(B2)** Arg(F̂(z)/z) = Arg(J(z)/z) + Arg(F̂(z)/J(z)) as real numbers.

Then

r_m = [Arg(J/z) + τq] + [Arg(F̂/J)] + S_Θ + τD_Q,

evaluated at z = z_m.

*Proof.*
1. By (B1), r_m = ΔΘ_W + τQ_m.
2. By definition, ΔΘ_W = ΔΘ_z + S_Θ (as real numbers on the certified domain, v6.4.14 §6.14).
3. ΔΘ_z = Arg(F̂/z), which splits by (B2).
4. Q = q + D_Q.

The reviewer's form is the same identity with Arg(F̂/z) − Arg(J/z) = Arg(F̂/J). ∎

**Sign check.** S_Θ enters with "+": it is defined as the primitive minus the normalized increment. The negative controls flip this sign (§6).

**Leading-term regrouping** (used for the constant). With L_Θ = [S_Θ]₃ and D₃ = [D_Q]₃ (adopted):

r = Λ₃(z) + [S_Θ − L_Θ] + τ[D_Q − D₃] + [Arg(J/z) + τq] + Arg(F̂/J),  Λ₃ := L_Θ + τD₃.

Λ₃ is the exact q^{3/2} term of r:

Λ₃/r³ = −(49√3/72)cos Θ + (1/24)sin Θ + (23√3/144)cos 3Θ − (19/48)sin 3Θ  (z = re^{iΘ}).

The other four brackets are O(q²) or smaller. Both parts of Λ₃ are of order q^{3/2}: L_Θ is the spiral term already certified in SG-9 (|S_Θ| ≤ 0.705 q^{3/2}, row A), and τD₃ is the static radial offset. Bounding Λ₃ jointly, rather than its two parts separately, gives the tighter constant.

## 3. Light checks

| Check | Result |
|---|---|
| S1 `[ALG]` | Λ₃ at Θ = 0 equals **−25√3/48** exactly. This is NUMGEN's own quartic-jet coefficient on the positive-u ray (v1.11). The DYAD chart leading terms and the NUMGEN primitive computation agree, with no free parameter. N1 (flipped sign of τD₃) fails, as required. |
| S2 `[ALG]` | The q-coefficient of Arg(J/z) is −τ. The q² coefficient is 89√3/324 + Im(a₀₅e^{−6iΘ}) = 89√3/324 − (307√3/25920)cos 6Θ + (49/8640)sin 6Θ, the RECOG chart law. The leading ceiling is 89√3/324 + \|a₀₅\| ≈ 0.4971. N2 (conjugated a₀₅) fails, as required. |
| S3 `[NUM]` | Λ* := sup_Θ \|Λ₃\|/r³ = **1.40032256532**, at Θ ≈ 3.7087 and its antipode. The exact map, sampled on 3600 angles at Q = 6.25·10⁻⁶, gives sup\|r\|/Q^{3/2} = 1.40212, and 1.40391, 1.40748, 1.41456 at Q = 2.5·10⁻⁵, 10⁻⁴, 4·10⁻⁴: it converges to Λ*. |
| S4 `[NUM]` | max over 72 angles of \|r/Q^{3/2} − Λ₃(arg W)/\|W\|³\| = 0.00727, 0.00363, 0.00181 at Q = 10⁻⁴, 2.5·10⁻⁵, 6.25·10⁻⁶. It halves when Q drops by 4×, so it scales like √Q. The decomposition's leading term matches the exact primitive map. |
| S5 `[NUM]` | max \|δ_T − π/3\|/√Q = 0.451 over sampled angles (input scale for P-c). The lifted block increment equalled 2π + ΔΘ_W in every sample. |

**Finding for NUMGEN.** NUMGEN v1.10 records sup|r|/Q^{3/2} ∈ [1.3449, 1.3565] from orbit sampling. Over all angles, the asymptotic sup is Λ* ≈ 1.4003, and finite-Q sups lie slightly above it. So any certified C_* must exceed about 1.40. The orbit-sampled range is consistent with this; it simply does not cover the maximizing angles. This corrects nothing in NUMGEN; it fixes the floor for C_*.

## 4. Certificate components

All on row A, with exact-rational majorants.

| Item | Statement to certify | Route / inputs |
|---|---|---|
| **P-Λ** | Λ* ≤ Λ̄ with Λ̄ rational (target ≈ 1.4004) | Λ₃ is a trigonometric polynomial with harmonics 1 and 3. Certify the maximum by rational interval subdivision with a derivative bound, or by algebraic elimination in (cos Θ, sin Θ). |
| **P-a1** | \|D_Q\| ≤ c_Q q^{3/2} (the Q ↔ q bridge; leading sup \|D₃\|/r³ ≈ 0.7734 `[NUM]`) | D_Q is the exact polynomial of degrees 3–12 from the adopted h (DYAD-ALG-NF6), with coefficient-modulus majorant evaluated at s = 1/20, as in DYAD-ART-OPEN3-P3. |
| **P-a2** | \|D_Q − D₃\| ≤ c′_Q q² | Same data, degrees 4–12. |
| **P-b** | \|Arg(J/z) + τq\| ≤ c_J q² | J is explicit. Im Log(1 + u) with u = μq + a₃₂q² + a₀₅q²e^{−6iΘ}, second order exact (S2), third-order remainder from \|u\|²-type bounds. |
| **P-7** (imported) | \|Arg(F̂/J)\| ≤ c₇q³ | DYAD-THM-NF-REM (C₇ = 100, row A): \|F̂ − J\| ≤ 100\|z\|⁷ and \|J\| ≥ \|z\|(1 − \|μ\|q − …), with arcsin(x) ≤ (π/2)x. |
| **S-Θ** (imported) | \|S_Θ − L_Θ\| ≤ K_Θ q², K_Θ = 123/125 | DYAD-THM-OPEN3-SPIRAL-REM, row A (adopted). |
| **P-c** (branch gate) | (B1) and (B2) on the whole tube | (B1): a one-step bound \|δ_T − π/3\| ≤ c_T√Q on U_T (c_T ≈ 0.45 `[NUM]`). With √Q < 0.047 on U_T, the six-step lifted sum lies in 2π ± 0.13 ⊂ (π, 3π), so it equals 2π plus the principal block angle. This needs an explicit majorant of the one-step map f(W) − λW on \|W\| < 0.047, and nonvanishing of W along the six phases (PRIM-CTR contraction). (B2): all three arguments are below 0.01 on row A. |

The reviewer referred to RECOG C1 for the one-step bound. In RECOG v0.3.21 the label C1 is used for other objects (a phase-signal condition and an Arb transport condition). No one-step angle bound under that name was found. P-c is therefore designed on DYAD's own one-step majorant. If a RECOG statement exists, it can replace this design by import.

## 5. Combination inequality (template, not yet evaluated)

On row A, with √q ≤ 1/20:

|r| ≤ Λ̄ q^{3/2} + (K_Θ + τc′_Q + c_J) q² + c₇ q³ ≤ [Λ̄ + (K_Θ + τc′_Q + c_J)/20 + c₇/400] q^{3/2}.

**Primitive form.** By P-a1, Q ≥ q(1 − c_Q√q) ≥ q(1 − c_Q/20). Hence

C_* = (1 − c_Q/20)^{−3/2} [Λ̄ + (K_Θ + τc′_Q + c_J)/20 + c₇/400].

This is sharper than the crude NF-INV factor (256/225)^{3/2} ≈ 1.21.

**Expected size** (`[HEUR]`, with the numbers above and c′_Q of order 2): C_* ≈ 1.7. This is an estimate, not a result. The NUMGEN form of the statement then reads |r_m| ≤ C_* Q_m^{3/2} for every block of every orbit from U.

## 6. Certificate design (next step, after approval)

**Outputs.**
- `dyad_numgen_lphase_rowA_cert.py` (exact rational; inputs pinned by hash to DYAD-ART-OPEN3-P3 and DYAD-ART-RE-P2B2 `certificate.json`);
- `lphase_rowA_certificate.json` (byte-deterministic);
- a separate `[NUM]` orbit illustration.

**Gates.**
- D (the identity, at jet level, through degree 6 in z);
- P-Λ, P-a1, P-a2, P-b, P-c, P-7;
- import pins (C₇, K_Θ, row radius);
- the final C_*.

**Negative controls (must fail).**
- sign of S_Θ flipped;
- τD_Q omitted;
- q used in place of Q in the final bound (bridge removed);
- row-B constants mixed into row A;
- Λ̄ rounded below Λ*;
- the one-step bound weakened beyond the (π, 3π) window.

## 7. Ownership and guards

- **SG-19.** The NUMGEN reading is accepted: combining DYAD-certified bounds into an inequality for the primitive r_m is not a coefficient transfer. Four conditions apply:
  - the target is primitive Q = |W|²;
  - q is used only inside the computation;
  - the final inequality is stated through the explicit Q ↔ q bridge (P-a1);
  - no new coefficient identity is declared for NUMGEN L1 or the ISP angle.
- **Ownership.** P-a, P-b, P-c and the combined constant are DYAD results, exported as a separate import. L-PHASE and L1 remain NUMGEN-owned. NUMGEN decides whether to cite C_*.
- **SG-7.** No fitting enters.
- **SG-14.** Everything is conditional on the selected T.

## 8. N3 / φ* (decision support)

- DYAD supports NUMGEN removing the historical pin `DYAD-CAND-PHISTAR-ENTRY-PHASE` in v1.20.8 and keeping its `[CAND]` ceiling. DYAD never registered this RID (v6.4.18 §7 N3).
- The adopted asymptotic-phase objects (v6.4.15) are not a substitute for the historical φ* law:
  - ΔΘ ≈ −τq and Δlog q ≈ −q show only that Θ − τ log q is constant at leading order;
  - rescaling an entry condition and comparing two starting points on one flow are different operations;
  - Δφ* = τ log λ is not a theorem under arbitrary entry data.
- A DYAD citation would need a new comparison proof.
- On NUMGEN v1.20.8 adoption, the next DYAD revision can mark N3 ANSWERED (removal).

**Receipts.**
- N10–N13 are RECEIVED on the NUMGEN side at SESSION level only; the owner-level sync awaits v1.20.8.
- N14 is not addressed to NUMGEN.

## 9. Updated priority (PI/reviewer decision, recorded)

| # | Work | Status |
|---|---|---|
| 1 | DYAD–NUMGEN angular remainder certificate (this note; P-Λ, P-a, P-b, P-c, combination) | scope + light checks done; certificate awaits approval |
| 2 | Compatibility of the smooth J, R (v6.4.18 E4) with the Triadic/Genesis closure | not started |
| 3 | O20-an analytic roots | paused until López-Hernanz (2012) is available |

**Not claimed:**
- any certified constant;
- any change to L-PHASE's grade or ownership;
- row B;
- any statement on the historical φ* law;
- any change to OPEN 20.

**Status unchanged:** DYAD v6.4.18 adopted; OPEN 20 PARTIAL; B-an and B-6 OPEN.

## 10. Files

- `lphase_scope_checks.py` — SHA-256 `570078dbfc2c8a881c47c4a468370452e0a5d76e8c73055857196e99e49cd8b6`.
- `lphase_scope_checks.json` — SHA-256 `9b31c7107a9d1e44cb19b213e1060f5aead30dddc7b79a49b6ca42372d1c3f25`.
- **Command:** `python3 lphase_scope_checks.py`. Expected output: `RESULT: PASS` (S1–S4 true, N1–N2 false). Runs in about 15 s.
