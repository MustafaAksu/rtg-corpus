# RER Phase B-02: source and scope reading note for RER-GEN-C01, C02 and C03 — r1

**Date:** 19 Oct 2026 (r1).
**From:** Claude, RER co-owner (preparer). The preparer does not accept his own work.
**Status:** NONCANONICAL Phase B input for independent receiving review. This is not a record disposition.
**r1:** answers receiver finding **B02-R1** (receiving review `04184e0e…3846`, 19 Oct 2026): the C02 reconstruction formula in §2 had the wrong sign on the Ω term. Corrected below; nothing else changes. The r0 note (`05327252…e19e`) is preserved as history. The correction concerns this note only; the RER r4.6 C02 record never contained the formula.
- No RER record, grade, contract table or OPEN status is changed.
- Nothing is adopted, frozen or published.

**Inputs:**
- RER v0.2 DRAFT r4.6 (`2fa878ff…4772`), records at lines 173–278.
- Phase A r7 (`2a13e279…a4d3`), source-currency matrix.

## 0. Sources

| Key | Cited section | Bytes | Use here |
|---|---|---|---|
| `GENMODEL`, `GENESIS_TO_RER_TRIAD_CLOSURE.md` (`721d9059…3304`) | §2 (lines 17–42), §3 (43–86), §4 (87–128), §5 (129–140) | **BYTE_VERIFIED_HERE** (Phase A r6/r7; content hash receiver-confirmed) | Read in full, lines 1–140 |
| `HARM`, `TRIAD_RECEIVING_REVIEW_AND_HARMONICS.md` §2 (lines 35–55) (`7a888515…acd`) | cited by C01, C02 and C03 | **MISSING**: not available to the preparer or, per its review, the receiver | **Not read.** Every statement below that depends on HARM is marked |
| `JET` (`15a7d056…2824`) | model cubic/quartic data | BYTE_VERIFIED_HERE | Not used: the jet was re-derived from the model definition (K2) |

**Dependency on HARM.** The three records cite HARM §2, "Three model-specific closure results". It is presumably a second, Triadic-side statement of the same three results, but that is an assumption.
- Without HARM, this note cannot confirm that the RER wording matches that source.
- It can confirm only the agreement with GENMODEL and with an independent re-derivation.
- **Full source coverage for C01–C03 therefore stays open.**

## 1. Independent re-derivation (preparer SESSION, exact)

**Script.** `b02_gen_c01_c03_check.py` (`d2ab599f…ffb3`):
- exact sympy;
- EXECUTED by the preparer, 46 s, exit 0, 10/10 checks;
- output in `b02_gen_c01_c03_check_output.txt` (`bad99fbb…ae4e`).

It rebuilds the RER §3 model from its definition only: E, P, the raw T_e, reprojection after each primitive step, and F = N⁶. It uses no imported jet file and no source script. Series are truncated at degree 7, which is exact for this map, since it fixes the origin.

| Check | Result |
|---|---|
| K1 | DN(0) = A ⊕ A with A³ = −I; F = X + O(3), with no quadratic part |
| K2 | The cubic jet G₃ of F equals the printed G_s, G_c of GENMODEL §3, component by component |
| K3 | DG₃(X)·𝒥X − 𝒥G₃(X) = 0, with 𝒥 = diag(J_Q, J_Q) (infinitesimal SO(B)-equivariance) |
| K4 | C01 witness. The unsigned Gram (Q_s, Q_c, I) agrees at the two states; for J₃ = Id + G₃, **ΔI = √3 t⁴(7t² + 6)/54 = (√3/9)t⁴ + (7√3/54)t⁶** exactly |
| K5 | C03 witness. Φ(X_t) = Φ(−X_t) for X_t = (t,0,0,t); **ΔQ_s = (349/288)t⁵ + (911/576)t⁷ + O(t⁸)**; even coefficients are 0 |
| K6 | GENMODEL §4 side value on the pure-parent ray: ΔQ_s = (5/32)t⁵ + O(t⁷) |
| K7 | Negative control: 349/287 is rejected |

This is a third, independent computation. GENMODEL reports two: a quartic-dictionary contraction and a Fraction composition. It is not an owner certificate and not a scientific acceptance.

## 2. Record-by-record reading

### RER-GEN-C01 — Unsigned Gram fails for the exact cubic surrogate

| Item | Reading |
|---|---|
| Claim vs source | Matches GENMODEL §3, last paragraph: equal unsigned triples (t², t², 0) and a leading successor-I difference of √3t⁴/9 |
| Grade `[ALG]`, `EXACT_SURROGATE` | Supported. The witness is an exact polynomial identity for J₃ (K4). The record's "+O(t⁶)" is the exact term (7√3/54)t⁶. |
| Scope | Correct. The statement concerns the surrogate J₃ only, not the analytic F, and the record says so. |
| Memory/transfer lines | Consistent with the source. The loss is present-state chirality, with no history claim. |
| Gap | Wording agreement with HARM §2 not checked (HARM missing) |
| Suggested disposition (for the receiver) | `SCOPE_CONSISTENT_WITH_GENMODEL; SOURCE_COVERAGE_INCOMPLETE (HARM)` |

### RER-GEN-C02 — Signed Gram closes the cubic polynomial surrogate

| Item | Reading |
|---|---|
| Claim vs source | Matches GENMODEL §3: equivariance of G₃, and exact signed-Gram closure for J₃. The source also says the exact reduced map has degree-6 terms, and the record states this. |
| Equivariance | K3 confirms the infinitesimal identity. For the connected group SO(B) it integrates to finite common rotations, as the source states. Then J₃ = Id + G₃ is equivariant. |
| Orbit separation (static completeness) | *Preparer reading.* On Q_s > 0 the vectors s and J_Q s form a B-orthogonal basis with equal Q, because B·J_Q is antisymmetric and J_Q is a B-isometry. With I = sᵀBc and Ω = sᵀBJ_Q c this gives **c = (I·s − Ω·J_Q s)/Q_s** (the r0 note wrote +Ω; corrected in r1, B02-R1). Hence Φ = (Q_s, Q_c, I, Ω) fixes (s, c) up to one common proper B-isometry. This is the "Q_s > 0 reconstruction patch" of the record's domain line. Checked exactly: `b02_r1_reconstruction_check.py` (R1–R3; the plus-sign formula fails at s = (1,0), c = J_Q s, where I = 0 and Ω = −1). |
| Grade `[ALG]`, `EXACT_SURROGATE` | Supported, given K3 and the orbit separation above |
| Scope | Correct: the closure is for J₃ only. The record's Next-test line forbids identifying J₃ with the full return. Admissibility descent is listed as a constraint. |
| Gap | HARM not checked. The output/exit chart of the domain line was not inspected; it is not in GENMODEL. |
| Suggested disposition | `SCOPE_CONSISTENT_WITH_GENMODEL; SOURCE_COVERAGE_INCOMPLETE (HARM)` |

### RER-GEN-C03 — Signed Gram fails for the named analytic six-step model

| Item | Reading |
|---|---|
| Claim vs source | Matches GENMODEL §4: the same signed readout at ±X_t, and ΔQ_s = (349/288)t⁵ + O(t⁷) |
| Independent check | K5 reproduces 349/288 from the raw map itself, and gives the next coefficient, 911/576. Φ(X_t) = Φ(−X_t) is exact. |
| Grade `[ALG]`, `EXACT_LOCAL` | Supported. The leading coefficient is an exact series coefficient of an analytic function, so the difference is nonzero for all sufficiently small t > 0. As the record says, no numerical radius is claimed. |
| Robustness (GENMODEL §5) | The source's pairing argument is that the N₄ contribution to the six-step quartic cancels. *Not re-checked here*, because K5 uses the full analytic map, so the witness does not depend on it. |
| Scope | Correct. The fibre is the common −I, a proper B-isometry, so the lost datum is the common frame angle, not chirality. The record says both representatives must be admissible. The witness is local and selects nothing physically. |
| Gap | HARM not checked |
| Suggested disposition | `SCOPE_CONSISTENT_WITH_GENMODEL; INDEPENDENTLY_REDERIVED (preparer); SOURCE_COVERAGE_INCOMPLETE (HARM)` |

## 3. Cross-record observations

- **B02-O1.** The three records form a consistent ladder:
  - unsigned Gram fails even for J₃ (C01);
  - adding Ω restores closure for J₃ (C02);
  - for the analytic F, signed Gram fails again, because the common frame angle is lost (C03).

  The RER text keeps J₃ and F apart in every Map/clock line. No overclaim was found.
- **B02-O2.** All three Evidence lines read "original scientific source pins and earlier verification scopes are retained from r2… no historical mathematical certificate is rerun". After Phase A r6/r7 the GENMODEL bytes are verified, and this note adds a preparer re-derivation. Any update to those Evidence lines is a later RER edit decision. It is not proposed here.
- **B02-O3.** In the `HARM` source-table row, line 1008 labels it version "0.1; NONCANONICAL_SOURCE". If HARM cannot be recovered, the receiver may decide whether GENMODEL alone suffices for these three records. That is a decision, not something this note assumes.

## 3a. r1 record of receiver evidence (RECEIVER-REPORTED)

The receiving review (`04184e0e…3846`) reports an independent exact `Fraction` implementation that composes the six primitive updates directly, without the preparer's script, jets or coefficients. It reproduces ΔQ_s = (349/288)t⁵ + (911/576)t⁷ + O(t⁹) along (t,0,0,t), and (5/32)t⁵ + (11/60)t⁷ on the pure-parent ray, and the exact C01 polynomial √3t⁴(6 + 7t²)/54. The receiver's identical-script replay of `b02_gen_c01_c03_check.py` timed out, so no receiving PASS is claimed for that script itself. Receiving dispositions: C01, C02, C03 `ACCEPT_SCOPED_MATH / HARM_MISSING`; C02 additionally `B02-R1_NOTE_CORRECTION`, answered by this r1.

## 4. Not in this note

- No reading of HARM, ANGLE_DATA or RANKDATA, which are missing.
- No check of the JET file or of the source checker scripts.
- C04–C09 are the next batch.
- No disposition is made. The two Triadic involution records stay with the receiver.
