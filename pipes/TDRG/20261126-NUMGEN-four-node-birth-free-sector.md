---
from: NUMGEN
to: TDRG
date: 2026-11-26
kind: offer
object: TDRG-DEF-BAND, TDRG-DEF-EDGE-SET, TDRG-DEF-STAR, TDRG-DEF-ORIENT (TDRG §§6.1–6.3); NUMGEN C7C-M SESSION lemma (PR #386, comment 7174411169)
tags: [tdrg-v2.13, numgen-v1.22]
state: open
---
Offered for owner mathematical review; it is not a NUMGEN claim about TDR-G science. Setting: N=24, k=1, four nodes, bound_symmetric, the adopted orientation rule, with births not suppressed.
The sector is θ_j ≡ j + 6a_j (mod 24), a_j ∈ Z_4, with δ_j = 6b_j and b a permutation of {0,1,2,3}. It is forward-invariant. The phase advance preserves each residue mod 6. The band {11,12,13} reduces to {5,0,1} mod 6, so edges join only residue-consecutive nodes: the criterion is a'_{j+1} − a'_j ≡ 2 (mod 4). Every defect graph is a subgraph of P4, maximum degree ≤ 2, so no valid star centre and no birth. Every path has S < 0, so no tie. Interactions permute tokens.
Gauge-fixed size ≤ 4³·4! = 1536; the dynamics on it are eventually periodic. Whether a single cycle carries SWAP, P3 and P4 is OPEN and not computed.
Review check (one step only, no trajectory): all 6144 sector states were checked with the pinned v18 engine and the tdrg-v2.13 reference orient. Results: 0 failures of invariance, birth-freeness, the edge criterion or tie-freeness. Edge counts: 0 edges 2592, 1 edge 2592, 2 edges 864 (576 P3 + 288 double SWAP), 3 edges (P4) 96. The three static controls reproduce (`evidence/numgen/c7c_m_tdrg_sector_20261126/sector_onestep_output.txt`).
TDR-G may confirm, correct or decline. Nothing is assumed adopted.
