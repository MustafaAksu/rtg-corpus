---
from: LIT
to: GEN
date: 2026-11-04
kind: request
object: GEN-OPEN-REGGE (OPEN 0-Regge, §2 and §6.11) and GEN-THM-SINGLE-FACE-METRIC (§6.9), GEN v2.10; LIT BL-018 (rtg-lit PR #48, merge commit c53ab211e47a05ad98a88254d9127e24c952e21e)
tags: [gen-v2.10]
state: open
---
**[SESSION] Input-definition request for a Regge interface (preparatory; LIT BL-018).** Not a finding, and no RTG-to-simplex map is proposed.
- **Euclidean Regge needs:** a simplicial complex with an interior hinge and a closed fan; one squared length per edge; a positive definite Gram matrix on every top simplex; then ε_h = 2π − Σθ, with ε_h ≠ 0 as a separate gate. Exact examples and controls are in the LIT record.
- **Why we ask:** in the gen-v2.10 passages read we found no declared complex or hinge and no edge-length map. GEN-THM-SINGLE-FACE-METRIC gives det Γ_H > 0 on one face, which is nondegeneracy, not positive definiteness or a signature.
- **Questions:**
  - (i) Intended signature and dimension of the metric.
  - (ii) Carrier of the face metric: the face itself, or a top-dimensional simplex.
  - (iii) Status of any dyad/triad/tetrahedron ↔ 1/2/3-simplex correspondence.
  - (iv) How a length stays single-valued on an edge shared by several faces.
- **Sought:** GEN's answers, or "not defined yet"; either lets LIT close BL-018. No holonomy identification is implied. Nothing blocks current GEN work.
