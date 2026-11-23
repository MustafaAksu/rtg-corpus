# RRF — OPEN 19 formal-centralizer closure proposal: scoped review and consumer synchronization

**Date:** 2026-10-16  
**Status:** `[SESSION] NONCANONICAL — REVIEW / CONDITIONAL CONSUMER ACTION; DYAD OWNER ADOPTION PENDING`  
**Owner boundaries:** DYAD owns the formal centralizer theorem and OPEN 19; RRF owns representation/realization contracts; Genesis owns its K3 projected-factor result. No owner DSN, adopted RRF registry, or G2 review was edited.

## 1. Source manifest

Read in this review:
- `RTG_DYADIC_OSCILLATOR_DSN_v6_4_11.md`, notably OPEN 19 (§2), §6.15 and §7 (adopted source, **OPEN 19 remains OPEN in this released file**).
- `RTG_RRF_REPRESENTATION_REGISTRY_v0_8_1.md`, notably §§2.3–2.4, 4.2, 6.2, 8.12 (adopted working standard).
- `RTG_RRF_G2_PRIMITIVE_EXCHANGE_INTERFACE_REVIEW_v0_2_1.md`, notably §§2–6 (noncanonical).
- `K3_CUBIC_FACTOR_OBSTRUCTION_SESSION_RECORD_v0_1.md`, especially §§1–5 (noncanonical SESSION; only C³ planar no-go established in this record).
- User's 16 October OPEN 19 closure review, including reported independent `sympy` kernel ranks and two proposed textual corrections.

Not received or rerun: `cent.py`/output, proposed DYAD owner successor text, its release/adoption record, or the original K3 external certificate scripts. The reported rank results are not independently re-executed here.

## 2. [SESSION/ALG] Assessment of the proposed formal centralizer proof

The reported real homogeneous vector-field kernel sequence for \(\mu=-\tfrac12-\tfrac{2\sqrt3}{3}i\), degrees \(k=2,\ldots,9\), is `0,1,0,0,0,0,0,0`. The claimed recurrence/pairing and degree filtration can imply \(\ker\mathrm{ad}_{X_3}=\mathbb RX_3\) in the relevant formal tangent-to-identity class **provided the proof covers all higher degrees and the indicated real-pair boundary cases**. The user supplied an independent finite-degree computational check, not a full all-degree rerun here. Two conditions are structurally necessary for the stated centralizer collapse in the reviewed argument: nonzero imaginary (chiral) and nonzero real (radial) parts of \(\mu\). Do not turn finite-degree kernel ranks alone into an all-degree theorem.

Before DYAD adoption, ensure:
1. The homogeneous-monomial pairing treats the boundary \(a=0\) separately: the formal partner \((b+1,-1)\) does not exist; its unmatched coefficient is forced to zero by the \(\bar c\mu\) term.
2. Status reads `PROPOSED CLOSURE [THM — formal, candidate]` in a pre-adoption candidate; after owner adoption use `CLOSED (formal) [THM — formal]`, with independent provenance recorded separately. Do not use contradictory `CLOSED / adoption pending` status.
3. Define \(F=T^6\) explicitly: the argument in branch (b) uses the centralizer of the **six-step return** \(F\). Cross-references to the one-step formal normal form must state the equivalence and its hypotheses rather than conflate targets.
4. Record the full-degree induction/filtration or formal logarithm centralizer reduction explicitly. Kernel checks only up to degree 9 are corroboration, not a substitute for an all-degree proof.

## 3. Consequence **conditional on owner adoption of OPEN 19**

Let \(\widehat S=\widehat h(-I)\widehat h^{-1}=T^3(T^6)^{-1/2}\) be the formal nontrivial involution, with the correct inverse-square-root branch and normalization. Assume the proposed formal centralizer theorem gives uniqueness among formal involutions with linear part \(-I\) commuting with \(F\) (and the corresponding formal primitive statement).

- **Analytic local germs**, under the origin/domain hypotheses of `DYAD-THM-LOCAL-INVOLUTION-GERM` §6.15(b): a nonidentity analytic involution \(R\) commuting with \(F=T^6\) has \(DR(0)=-I\), hence Taylor series \(\widehat S\). Since \(R\) is analytic, \(\widehat S\) converges to \(R\); as \(\widehat S\) commutes with \(T\) formally, \(RT=TR\) analytically. Thus analytic six-step and primitive nontrivial involution existence coincide *for the stated local germ class*. A negative analytic Problem B excludes such an analytic six-step involution; it does not exclude a \(C^\infty\) one.
- **Smooth local germs**: \(j^\infty R=\widehat S\), and \(RT-TR\) has zero full Taylor series (is **flat** at the origin). Exact primitive commutation is **not** thereby proved.
- **Finite \(C^r\)**: `DYAD-THM-LOCAL-INVOLUTION-GERM` requires \(r\ge3\) for six-step linear dichotomy; all-order Taylor and analytic equality are unavailable. Existing C¹ primitive statements must not be casually transferred to C¹ six-step.
- **Fixed \(h_6\) map**: \(S_h=h_6(-I)h_6^{-1}\) is exactly an involution, but equality with the formal \(\widehat S\) is only its matched degree-6 jet; convergence does not promote \(S_h\) itself to an exact commuting map.
- **Physics**: none of the preceding determines physical node exchange, an edge-factor \(EF=TE\), submersive encoding, or OPEN-A/B/E closure.

## 4. Consumer edits after **actual DYAD owner adoption** (not before)

1. **RRF v0.8.1 §2.4 and §4.2:** replace `source-pending formal G1` language with primary **DYAD owner RID/version/section** for adopted centralizer/uniqueness theorem, retaining the formal/finite and physical/representation guards. OFN/RECOG may be consumer cross-references only. No RID should be invented before owner assignment.
2. **RRF §6.2:** replace the overbroad assertion that six-step-only commutation can never imply primitive commutation with a precise *regularity-qualified* statement: adopted DYAD §6.15 already gives \(DR(0)=\pm I\) for \(C^3\) six-step involutions in its tube; after formal uniqueness adoption analytic nontrivial six-step involutions also commute with primitive \(T\), while smooth only yields flat commutator under formal equality. Crucially, \(EF=T^6E\) is still not the same **factor contract** as \(EF=TE\).
3. **RRF §8.12:** remove the phrase denying owner adoption *only after* the owner release. Retain statements that analytic convergence is not automatic from a formal theorem and that \(S_h\ne\widehat S\) beyond the proven degree-6 jet.
4. **G2 interface v0.2.1 §3:** correct the superseded first-derivative-only text `DT^6(0)=I; no ±I restriction` using `DYAD-THM-LOCAL-INVOLUTION-GERM` §6.15(b); qualify the `six-step need not commute with primitive` phrase by regularity. If formal uniqueness is not yet owner-adopted, keep the analytic equivalence conditional.
5. **G2-PRE:** primitive odd-chart existence and six-step analytic nonidentity involution existence become equivalent **conditional on adopted formal centralizer uniqueness**. This does **not** identify either with complete physical G2, whose network encoding/fiber/clock conditions remain OPEN.
6. **K3 session:** the mounted `K3_CUBIC_FACTOR_OBSTRUCTION_SESSION_RECORD_v0_1.md` establishes a named **C³** planar primitive-factor obstruction. It does not establish positive C¹ or C² factors, nor any asserted `d=1,3` classification; do not import an uninspected degree-indexed classification into RRF.

## 5. Disposition

`ACCEPT SCOPED [SESSION]` for the mathematical and dependency analysis. **DYAD OPEN 19 stays officially OPEN in v6.4.11 until an adopted owner successor/source explicitly changes it.** No RRF v0.8.1/G2 scientific status change was made. Pending owner-adoption of a complete all-degree proof, prepare a separate targeted `RRF v0.8.2` editorial/consumer synchronization candidate; do not represent it as an adopted theorem beforehand.
