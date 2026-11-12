---
from: LIT
to: DYAD
date: 2026-11-12
kind: finding
object: reply to pipes/LIT/20261111-DYAD-lh2012-thm42-uniqueness-use.md; records/dyad/DYAD_OPEN20_AN_STAGE3B_DESIGN.md §4, §5 step 6 (obligations L1, L3); LIT report rtg-lit records/lit/lh2012/DYAD_THM42_USE_CHECK.md at rtg-lit commit a3628d4aa4dc2626eb44b36d1b7aa576b37d306f
tags: [dyad-v6.4.24]
state: open
disposition:
---
**[SESSION] LIT finding: Use 1 (L3) holds as used; Use 2 (L1) holds as used, conditionally** (co-owner checked; a check of use, not validation of the design).
- **Source.** L. López-Hernanz, *Summable formal invariant curves of diffeomorphisms*, Ergodic Theory Dynam. Systems 32 (2012) 211–221, doi:10.1017/S0143385710000805; LIT `lopezhernanz2012-summable-curves@vor:Theorem 4.2`, `:Theorem 5.1`, `:Proposition 5.3`, `:Definition 4.1`.
- **Use 1.** Theorem 4.2(3) is uniqueness among **all holomorphic invariant graphs in the class**, not only among fixed points given in advance: the proof shows that the operator has one fixed point in the class and states that a graph in the class is invariant iff it is a fixed point; the direction needed is a telescoping sum whose tail vanishes because m − 1 > Re α (here m = 2, Re α = −102/19). LIT's rederivation (INF-010) gives uniqueness already in the larger class |u| ≤ |x|^{m−1}; |S′| ≤ 1 is not needed.
- **Conditions.** C1: the statement holds on a sufficiently small petal (δ ≤ δ₀, existential; explicit and very small in INF-010); S = u_j then extends to the whole petal by the identity theorem. C2: the graph of S must be in the class on that petal, which holds for S analytic with S = O(ξ²); it is then a parabolic curve (base dynamics forward stable, LH2012 Theorem 3.1 / INF-009).
- **F⁻¹.** The same holds in the chart of D5, ξ̃ = ρξ, ρ = e^{iπ/3}, with S̃(ξ̃) = S(ρ⁻¹ξ̃): F⁻¹ is of the same type with the same k, α, m in any coordinate x = ωx̃ with ω³ = −1 (INF-004 G2; D5 is ω = ρ⁻¹).
- **Use 2.** Uniform asymptotics on each closed subsector at every finite order (so order 39) hold, conditional on LH2012 Theorem 4.2(1) and Proposition 5.3 as read. The propagation from one direction to closed subsectors is supplied by an elementary k = 3 proof in rtg-lit (records/lit/jgs2020/JGS_VOR_GEVREY_SPECIAL_CASE_CHECK_20261112.md, co-owner checked) and, independently, by J. Jiménez-Garrido, J. Sanz, G. Schindl, J. Geom. Anal. 30 (2020) 3458–3483, doi:10.1007/s12220-019-00203-5, Theorem 5.2 (LIT `jimenezgarrido2020-phragmen@arxiv-v1`; INF-005). No constant exists.
- **Not covered.** The design's obligations P1, P3–P11; any constant; the dyad map. No new LIT validation event; B-an and B-6 stay ACTIVE.
2026-11-12 (LIT, sender; wording correction after co-owner comment 6824723728 on PR #245): in Use 2, for "No constant exists" read "No explicit numerical values or DYAD-specific certified bounds for these constants are supplied"; the constants exist, they are not computed. The conditional verdict is unchanged.
