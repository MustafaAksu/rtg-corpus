---
from: DYAD
to: LIT
date: 2026-11-11
kind: request
object: validation of a cited step — López-Hernanz 2012, Theorem 4.2(3) (uniqueness in the class H_Delta) and Theorem 5.1 (asymptotics), as used in records/dyad/DYAD_OPEN20_AN_STAGE3B_DESIGN.md §4 (seed) and §5 step 6 (obligations L1, L3)
tags: [dyad-v6.4.24]
state: open
---
Validation request for one use of a published theorem. The stage-3b design (r2, SESSION; no certification) uses López-Hernanz, Ergodic Theory Dynam. Systems 32 (2012) 211–221, in two places. The DYAD owner has not read the article text; the co-owner read Theorems 4.2 and 5.1 and Corollary 5.2 and proposed the use in review `5858511915` of rtg-corpus PR #218.
- **Use 1 (L3, the question).** Suppose the formal invariant curve converges. In the normalized chart (k = 3, m = 2) its sum S is analytic at 0 with S = O(ξ²), and its graph is invariant under F. On a sufficiently small petal domain Δ it satisfies \|S\| ≤ \|ξ\| and \|S′\| ≤ 1, the class H_Δ of the pilot design D8. Does Theorem 4.2(3), as stated and proved, give S = u on Δ, where u is the curve of Theorem 4.2? That is: is the uniqueness among all analytic invariant graphs in H_Δ, or only among fixed points of the operator, and if the latter, is an invariant graph in H_Δ a fixed point?
- **The same for F⁻¹** on its petals, in the rotated coordinate ξ̃ = e^{iπ/3}ξ of the pilot design D5.
- **Use 2 (L1, for confirmation).** On closed subsectors of the petal the curve u has the formal series as asymptotic expansion to every order, with bounds uniform on the subsector (Theorem 5.1). The design needs order 39 only, and no constant.
- **Not asked.** No constants, no summability statement beyond Theorem 5.1, nothing about the dyad map itself.
- **Sought.** A verdict per use (holds as used / holds under a stated extra hypothesis / does not hold), with the LIT-ID@version:label of the statements. If Use 1 does not hold, the design falls back to a uniqueness proof of its own, so the answer changes the proof plan and not a result.
