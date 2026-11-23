# RER Phase B-01: relevance of Genesis v2.8.9 §6.3c to RER-GEN-K3-MODAL, G6 and OFN v0.10 IMP-O10-01/02

**Date:** 19 Oct 2026.
**From:** Claude, RER co-owner (preparer). The preparer does not accept his own work.
**Status:** NONCANONICAL Phase B input for independent receiving review.
- This note is not a Phase B disposition.
- No RER record, grade, contract table or OPEN status is changed.
- Nothing is adopted, frozen or published.

**Starting hypotheses (receiver, Phase A r5 decision):**

| Item | Hypothesis |
|---|---|
| RER-GEN-K3-MODAL | `CONTEXT_ONLY` |
| G6 | `OUT_OF_SCOPE` |
| IMP-O10-01/02 | `CONSUMER_CHECK_PENDING` |

## 0. Sources and evidence labels

| Source | Identity | How it was used here |
|---|---|---|
| Genesis v2.8.9 | `d143673e…c6fc` | Project copy read in full (§1, §5 row, §6.3a–§6.3c, SG-15/16, §7 export, §8). The hash is owner-reported and receiver-computed (Phase A r4), and was not recomputed here. |
| OFN v0.10 | `acb70a8c…5dfa` | Project copy read in full (§5.5, §11.4, §11.5). The receiver byte-verified it (Phase A r5); the preparer did not. |
| Genesis notice erratum (OFN Q6) v0.1 | — | Read |
| RER v0.2 DRAFT r4.6 | `2fa878ff…4772` | Read: §3 (common modal contract), RER-GEN-K3-MODAL (lines 814–858), RER-TRIAD-FORMAL-INVOLUTION (lines 901–943), G5/G6 rows |
| `b01_cubic_compare.py` (this note) | `098eefdc…7dbe` | Exact sympy check of the printed Genesis coefficients only. EXECUTED by the preparer, exit 0. Not an owner certificate replay. |

No owner certificate was rerun.

## 1. Scope comparison: RER-GEN-K3-MODAL and §6.3c are not the same statement

| Axis | RER-GEN-K3-MODAL (owner theorems imported) | Genesis §6.3c, `GEN-THM-TRANSPORTED-CHIRAL-FACTOR-NOGO` |
|---|---|---|
| State space | R⁴, the modal carrier. It is identified with C = {Σwₑ = 0} by E. | R⁶ (edges w₁, w₂, w₃), including the mean mode D |
| Map | The raw analytic edge map T, reprojected after each primitive step (RER §3): N, with E∘N = F₁∘E | Any real C³ germ G whose third jet in some C³ coordinates equals that of the mean-feedback form G⁽ⁿ⁾_γ over N₃(z) = λz + n z²z̄ |
| Quadratic part | T has a nonzero quadratic part (e.g. the ρ²/2 in e^ρ − 1) | (H-JET ii): zero quadratic part |
| Family parameter | None. The model is the γ = 1 projected carrier ("γ = 1 equivalent", RER Non-transfer line). | γ ∈ ℝ∖{0,2}; γ = 1 is included |
| Extra hypotheses | Six-step `GEN-THM-K3-SIXSTEP-FACTOR-NOGO`: none on T′. Primitive `GEN-THM-K3-PLANAR-FACTOR-NOGO`: none on T′. | (H-μ) μ = 6λ̄n ≠ 0, and (H_spec) |
| Clocks | Primitive (C¹ for d = 1, 3; C³ for d = 2) and six-step (C³, d = 1–3), each with an owner RID | Six-step only, as a theorem. The primitive companion is `[ALG]` with no RID, is not exported, and is no corollary of the six-step theorem. |
| Six-step cubic, in chiral coordinates (u, v) | Lemma S form with (c, β) = (c₀, β*) = (1/6 + i√3/9, 2√3/9) (§6.3a(d); §6.3b at γ = 1 gives the same values) | Lemma S form with (c, β) = (−μ/3, 2iμ/3). At μ = μ₆: (1/6 + 2i√3/9, 4√3/9 − i/3). |

**Coefficient check.** The two cubic coefficient pairs differ: Δc = i√3/9 and Δβ = 2√3/9 − i/3 (`b01_cubic_compare.py`, exact). Four identities are confirmed:
- 6λ̄n_T = μ₆;
- §6.3b at γ = 1 reproduces (c₀, β*);
- the coefficient pairs differ;
- the §6.3c instance lies in the adopted Lemma S branch.

**What follows.** Tangent-to-identity C³ conjugacy preserves the six-step cubic, because the six-step map has identity linear part and no quadratic term. So the raw reprojected model and the polynomial transported model at γ = 1 (instance C1) are not tangent-to-identity C³-conjugate.

This agrees with RRF v0.8.3 §0.3 and OFN v0.10 §5.5.4: re-imposed mean feedback in new coordinates is a **different conditional model**.

Not examined here: whether a non-tangent-to-identity linear change could relate the two. It is not needed for any RER claim.

**Conclusion for §1.** The two scopes are different. The raw modal map is not shown to lie in the §6.3c class, and §6.3c is not needed for it.

## 2. RER-GEN-K3-MODAL

### 2.1 Recorded claims

**Proposed disposition: `CONTEXT_ONLY` — confirmed.**
- The record's closure (`NO_LOWER_DIMENSIONAL_FACTOR_AT_EITHER_CLOCK`) rests on the two raw owner theorems, transported by the `[ALG]` E-conjugacy. Neither theorem needs (H_spec) or μ ≠ 0.
- §6.3c neither strengthens nor weakens those claims.
- Genesis v2.8.9 states that §6.3a, §6.3a.1, §6.3b and SG-15/16 are unchanged, and that the five K3/6S RID lines are unchanged. This is owner-reported in its header, §6.3c preamble and Appendix A. It was not byte-compared here, because no v2.8.7 bytes are in this workspace.
- The record's pins stay on byte-verified v2.8.7 (`d5d1e57c…e361`). No repin is proposed.

### 2.2 The record's OPEN item "other carriers, including the h-transported carrier"

**Proposed: `CANDIDATE_SCOPE_EXTENSION — NOT FOR INSTALLATION`.**

§6.3c, instance C3, covers every real C³ germ with the stated third jet, "whether or not it is exactly transported". It therefore bears on transported network models in their 6D mean-feedback form, for γ ∉ {0,2}, under (H_spec).

The RER modal carrier is 4D and reprojected at γ = 1, so the theorem does not apply as stated. A consumer-side step would be needed. The preparer proposes the following one, at preparer SESSION grade.

**Proposed lemma (`[ALG — SESSION, preparer; not reviewed]`, RER-native transport, analogous to the existing E-conjugacy step).** Let Ñ be a real C³ edge germ with:
- DÑ(0) = A;
- no quadratic part;
- third jet λz + n z²z̄ with μ = 6λ̄n ≠ 0.

Let M = P_C∘Ñ^{×3}|_C be its reproject-each-step modal map. Up to E it is the RER §3 model with T replaced by Ñ. Then M admits no local C³ submersive six-step factor E′∘M⁶ = T′∘E′ with d ∈ {1,2,3}.

*Argument, using only the §6.3c statement.*
1. Put G := G^Ñ_1 = P_C∘Ñ^{×3} on R⁶. G satisfies (H-JET) at γ = 1 and (H-μ). Its image lies in C, and G|_C = M.
2. Given E′, set E := E′∘G. DG(0) maps R⁶ onto C, so E is a C³ submersion. Then E∘G⁶ = E′∘M⁶∘G = T′∘E.
3. From E′∘M⁶ = T′∘E′ and DM⁶(0) = I, DT′(E(0)) = I. So (H_spec) at γ = 1, 0 ∉ spec DT′, holds.
4. §6.3c then excludes E, hence E′. ∎

**Boundaries.**
- The lemma uses the six-step theorem only. The primitive companion is not used. No primitive-clock statement for M is made.
- The raw modal map is **not** covered: T has a quadratic part. That case is already closed by K3-SIXSTEP.
- **Carrier identification is not verified.** The phrase "h-transported carrier" in RER comes from the G2 note v0.4 §5b. That note is `UNAUTHENTICATED_NO_HASH` and was not read for this note. Whether its carrier is a reproject-each-step model over an edge germ in 𝒩₃ is unverified.
- No existence claim is made. Instance C2 (exact transport, Φ commuting with A) stays conditional on DYAD OPEN 20. C3 needs no such existence.
- Before any change to the record, three things are required:
  1. identification of the carrier;
  2. independent review of the lemma;
  3. a receiver decision on whether RER should carry it. This would be a new subclaim, not a current-use overlay.

## 3. G6 (RER-TRIAD-FORMAL-INVOLUTION, P1 table)

**Proposed disposition: `OUT_OF_SCOPE` — confirmed.**
- **G6 asks** whether span{A, B} extends to a two-parameter formal centralizer of F = N⁶ for the **raw** modal map. The cubic kernel is built from the raw (a, β*) = (c₀, β*).
- **§6.3c gives** a factor (semiconjugacy) exclusion for the **transported** third-jet class. It makes no statement about centralizers, formal flows or uniqueness of involutions, and its cubic differs (§1).
- **No logical route** was found from a factor no-go to the formal centralizer dimension, in either direction. This is a reading result: independence is not proved.
- **Further scope limits of §6.3c:**
  - it is not stated for formal power series as such (G-JET);
  - it does not touch convergence of Ŝ_triad;
  - it does not touch the degree-7 graph question (P1).
- **G6 stays OPEN.** Nothing in Genesis v2.8.9 changes its Next test: solve [X, Y] = 0 order by order and compute the cokernel obstruction.

## 4. OFN v0.10 IMP-O10-01/02: consumer check

**RER dependency: none.**
- RER r4.6 cites OFN only through the OFN9 pins, at §8 and §12.4 (RER-RRF-CND01).
- No RER record cites OFN §5.5, IMP-O10-01 or IMP-O10-02.
- Proposed status: `NO_RER_CONSUMER — CONTEXT`.

**Statement-level comparison** (OFN co-owner context; OFN v0.10 itself is adopted and outside RER custody):

| OFN text | Genesis v2.8.9 | Reading |
|---|---|---|
| IMP-O10-02 hypothesis list: real C³; (H-JET); (H-μ); κ ∈ ℝ∖{0,2}; (H_spec); d ∈ {1,2,3}; closed under C³ conjugacy; Lemma S adopted branch; guards G-JET, G-20, G-SEL, G-OFN | §6.3c theorem, guards and evidence | Matches the source statement item by item |
| §5.5.3 corollary uses the six-step theorems; the primitive companion is not used | §7 export: companion not exported as a theorem; erratum §1 | Consistent |
| IMP-O10-01: MEANFEEDBACK for κ ∈ ℝ∖{0,2} under (H_spec); K3-SIXSTEP at κ = 1 | §6.3b and §6.3a.1 | Consistent; see O-3 |

**Observations** (for the OFN owners and RER use; nonblocking; none changes a conclusion):

- **O-1 — Notation collision.**
  - OFN §5.5 writes **κ** for Genesis's family parameter **γ** (IMP-O10-01: "γ ≡ κ").
  - In RER, `kappa` is the **Triadic birth coefficient**, and RER's r4 notation line forbids interchanging κ and γ.
  - Any future RER citation of OFN §5.5 must translate κ_OFN → γ at the point of use.
- **O-2 — Undefined symbol.** IMP-O10-02 writes "n = n₂₁" for instance C1. Genesis writes n_T = 1/8 − 7i√3/72. n₂₁ is not defined elsewhere in the OFN v0.10 text read here, so its equality with n_T is not checked here. The μ₆ statement itself agrees with Genesis (`b01_cubic_compare.py`, check 1).
- **O-3 — κ = 1 route.** At κ = 1 the narrow-Q6 corollary cites K3-SIXSTEP. That theorem is stated on a neighbourhood of 0 in C, while the corollary's Eᵢ live on R⁶. The reduction is the §6.3b(a)–(b) step under (H_spec). Alternatively, MEANFEEDBACK covers γ = 1 directly on R⁶, since 1 ∈ ℝ∖{0,2}. The Genesis erratum (§2) already accepted this routing. Recorded here only as a precision note.
- **O-4 — Overlap with blocked ER-2B.** OFN §5.5.4 declares class C a different conditional model under RRF §0.3. This is the same distinction as RER-ER2B-CARRIER, "passive transport is not reimposed additive closure". That record stays `BLOCKED_SOURCE_UNVERIFIED`, and OFN v0.10 does not unblock it, because it supplies no ER-2B primary bytes.

## 5. Summary of proposed Phase B-01 dispositions

| Object | Proposed | Basis |
|---|---|---|
| RER-GEN-K3-MODAL, recorded claims | `CONTEXT_ONLY` | §2.1: closure rests on raw owner theorems with no (H_spec); §6.3c not needed; pins stay on v2.8.7 |
| RER-GEN-K3-MODAL, OPEN "other carriers" | `CANDIDATE_SCOPE_EXTENSION — NOT FOR INSTALLATION` | §2.2: proposed preparer lemma; carrier identification, review and receiver decision pending |
| G6 | `OUT_OF_SCOPE` | §3 |
| IMP-O10-01/02 | `NO_RER_CONSUMER — CONTEXT`; statement-level match | §4; O-1 to O-4 |

## 6. Not in this note

- No change to the r4.6 Markdown or the Phase A machine registry.
- No byte comparison of v2.8.7 against v2.8.9.
- No reading of the G2 note.
- No rerun of the owner certificates `d4_transported_cubic_cert.py` and `k3_obstruction_exact_check.py`.
- No Phase B disposition of the other 19 records.
- The two Triadic author-conflict records remain for independent recipient disposition.
- ER-2B stays blocked. G6, the degree-7 graph and the Stage-2 global certificate stay OPEN.
