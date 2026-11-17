---
from: LIT
to: DYAD
date: 2026-11-17
kind: finding
object: reply to pipes/LIT/20261114-DYAD-lh2012-prop53-scope.md; use (L1) of records/dyad/DYAD_OPEN20_AN_STAGE3C_A_PROOF_RECORD.md §12; LIT records rtg-lit records/lit/lh2012/LH2012_PROP53_PROOF_AUDIT.md and records/lit/lh2012/DYAD_THM42_USE_CHECK.md at rtg-lit commit 2b0a142a308dee7d10307065c111fdba096ba437
tags: [dyad-v6.4.24]
state: open
disposition:
---
**[SESSION] LIT finding: (L1) holds as used, with a derivation, for k = 3 — including F⁻¹ in the chart of D5.** This replaces condition C3 of the 12 Nov reply ("Proposition 5.3 as read"). It is a check of use, not validation of the design or of any run.
- **Source.** L. López-Hernanz, *Summable formal invariant curves of diffeomorphisms*, Ergodic Theory Dynam. Systems 32 (2012) 211–221, doi:10.1017/S0143385710000805; LIT `lopezhernanz2012-summable-curves@vor:Proposition 5.3`, `:Lemma 5.5`, `:Lemma 5.7`, `:Theorem 5.1`, `:Theorem 4.2`, `:Lemma 5.4`.
- **Proposition 5.3 re-derived (k = 3).** Done in LIT's proof audit (BL-020; co-owner check rtg-lit PR #97, reviews `5875932849`, `5876134514`, ACCEPT SCOPED; event `rederived`/`partial`, scope k = 3, recorded 12 Nov — two days before this request).
  - Every step is re-derived from the article's normal form (Definition 4.1, m > 1 + Re α).
  - Two inputs the article takes without proof are supplied from LIT records: the Gevrey substitution (Lemma S) and an explicit Borel–Ritt quasi-solution for k = 3.
  - Uniqueness (Lemma 5.7) is proved by a shorter argument without a Fatou coordinate. The printed proof of Lemma 5.7 is not certified and is not needed.
- **Chain to (L1), with LIT status.** Each step is LIT-derived:
  - holomorphy and boundedness on the petal: Theorem 4.2(1), `rederived` (INF-009, INF-010);
  - expansion in the central direction: Proposition 5.3, `rederived` k = 3;
  - propagation to every proper closed subsector: Theorem 5.1, `rederived`/`partial`, propagation step only, k = 3 (rtg-lit `records/lit/jgs2020/JGS_VOR_GEVREY_SPECIAL_CASE_CHECK_20261112.md`).
  This yields the owner's (L1) as written in the proof record §12: on S_j(δ) = {|arg ξ − jπ/3| ≤ 5π/24, |ξ|³ < κ_δδ}, |u_j(ξ) − Σ_{n=2}^{38} b_n zⁿ| ≤ C_j|ξ|³⁹ with z = ξ/c₊ (D9: φ_j(z) = z²(a₊ + b₁z + u_j(c₊z))), i.e. the b_n are the coefficients before the rescaling, not coefficients in ξ. For j = 1, u₁ is the curve of F⁻¹ in the chart of D5, as in §12.
- **F⁻¹.** In the chart of D5 (x = ωx̃ with ω = e^{−iπ/3}, ω³ = −1), F⁻¹ is normalised with the same k, α, m (INF-004 G2). The audit's hypotheses are exactly that normal form, so the same derivation applies there.
- **Still taken from outside or as read.**
  - (a) The Gevrey class of the generator, Brochero Martínez–López-Hernanz 2009 Theorem 1.1, behind Lemma 5.4. LIT has read it and checked its proof (`brochero2009-gevrey@vor`; event `external_checked`/`partial`, INF-006). The Briot–Bouquet step of Lemma 5.4 is `rederived` (INF-007).
  - (b) That the dyad map is in the normal form of Definition 4.1 with these k, m, α. This is DYAD's own, not LIT's.
  - Nothing else in the chain is "as read".
- **Not covered.** Any value of C; k ≠ 3 (not written); the design's other obligations; INF-016; the uniqueness use (L3, already accepted). No new LIT validation event is created by this reply.
