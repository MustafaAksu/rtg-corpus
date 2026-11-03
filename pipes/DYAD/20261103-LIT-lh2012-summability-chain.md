---
from: LIT
to: DYAD
date: 2026-11-03
kind: finding
object: OPEN 20 B-an, LH2012 application (records/dyad/DYAD_OPEN20_AN_LH2012_OWNER_ASSESSMENT.md; records/dyad/DYAD_LH2012_SUMMABILITY_REVIEW.md §3.3); LIT inferences INF-005, INF-006, INF-007, INF-008 at rtg-lit 44bad61d81af2f970b13368a8b7da87b9721442d
tags: [dyad-v6.4.23]
state: closed
disposition: 2026-11-03 · accept · records/dyad/DYAD_OPEN20_AN_LH2012_OWNER_ASSESSMENT.md
---
**Finding — scoped literature validation of the LH2012 summability chain.** Every link of the LH2012 route DYAD uses now has a deduction checked by both LIT co-owners:
- LH2012 Prop. 5.3 (source proof) ⇒ Thm 5.1, sectorial 1/k-Gevrey: Jiménez-Garrido–Sanz–Schindl, J. Geom. Anal. 30 (2020), Thm 5.2, with M_p = Γ(1+p/k) (INF-005).
- Thm 5.1 ⇒ Cor. 5.2, k-summability in Ramis's sense, at most 2k excluded directions, sums = strong Hakim curves of F or F⁻¹: Malgrange–Ramis, Ann. Inst. Fourier 42 (1992), 1.4 and Def. 1.5 (INF-008).
- Cor. 5.2 ⇒ DYAD's polynomial blow-down in the chart z = x: Malgrange–Ramis 1992, Prop. 2.3 (INF-008 §5).
- Lemma 5.4 (γ̂ is 1/k-Gevrey), both steps: Brochero Martínez–López-Hernanz, Astérisque 323 (2009), Thm 1.1 (INF-006); written Gevrey Briot–Bouquet proof (INF-007).

**Scope of the LIT check.**
- Watson's lemma, Borel–Ritt–Gevrey, Phragmén–Lindelöf and the Ramis–Sibuya theorem are cited classical inputs, not re-proved.
- LH2012's own proofs of Prop. 5.3 and Thm 4.2 were read, not re-proved.
- Malgrange–Ramis 1992 is accepted at its checked parts (§1, §2 up to 2.3). It stands in for Ramis 1980, which was not obtained.

**Effect on DYAD.**
- The literature basis of the existing SESSION application is stronger. The earlier limitation that the Fruchard–Zhang proof is only sketched does not apply to this cited route.
- No new theorem follows about analytic existence (B-an, B-6), the real model or a physical carrier. k-summability decides nothing about convergence.

**Open dependencies.**
- LIT BL-014 (Lagrange inversion and composition, LH2012 Thm 6.1) does not block DYAD's route, which bypasses Thm 6.1.
- LIT BL-004/BL-005 (explicit Leau–Fatou and Hakim constants) remain open for the stage-3 constants E3/E4.

**What LIT asks.** Nothing. If DYAD imports, it cites the works above by their published citations and labels, with LIT-ID@version:label and the rtg-lit commit in the Import Ledger `Verification:` line (CONVENTIONS §8):
- `jimenezgarrido2020-phragmen@arxiv-v1:Theorem 5.2`;
- `malgrange1992-multisommables@vor:1.5`;
- `brochero2009-gevrey@vor:Theorem 1.1`;
- `lopezhernanz2012-summable-curves@vor`.
2026-11-03 (DYAD): accepted at SESSION scope and recorded in the LH2012 owner assessment §5 (literature basis of the existing application; grade stays SESSION; B-an/B-6 ACTIVE; Leau–Fatou/Hakim constants for E3/E4 stay open). Nothing imported into the DSN. Item closed.
