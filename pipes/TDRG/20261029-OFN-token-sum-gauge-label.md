---
from: OFN
to: TDRG
date: 2026-10-29
kind: finding
object: tdrg-v2.12.14 SG-3 (L445–446), §2 total-momentum row (L114), Appendix B (L1319) versus SG-14 (L478); OFN v0.10 §10 token-sum row
tags: [tdrg-v2.12.14, ofn-v0.10]
state: open
disposition:
---
Both OFN co-owners found a label inconsistency (joint record `records/ofn/OFN_OWNER_DISPOSITION_RECONCILIATION_v0_10.md` §3.4, §6; PR #110).
- SG-3 calls $P=\sum\delta_i$ "gauge-like".
- §2 (L114) and Appendix B (L1319) call it a "gauge artifact".
- SG-14 (L478) says the common token shift $\delta_i\mapsto\delta_i+c$ is outside $G_{\rm cov}$, "a symmetry of the birth-free sector only, not a gauge".
- The nonconservation itself is already stated by the owner in the SG-3 violation line ("$P$ changes under birth"; under TDRG-DEF-STAR, $\Sigma\delta$ changes by $-\delta_A$ mod $N$). OFN agrees with it and asks for no new proof or campaign.
What OFN needs: a TDR-G decision on whether the "gauge-like"/"gauge artifact" wording stays, is reworded (e.g. "not conserved at births; not a gauge quantity under SG-14"), or is explained. Whether $P$ or a variant is a physical observable stays TDR-G's decision; OFN v0.11 will cite whichever wording TDR-G adopts.
