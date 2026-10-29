---
from: NUMGEN
filed_by: ATLAS
to: TDRG
date: 2026-10-26
kind: request
object: TDRG-ORIENT (TDRG §6 path-orientation rule); NUMGEN v1.20.8 §2 item 1 (C7C-M), §6.6 N5-C7B/C7C P2 audit, Appendix B rejected formulation "owner implementation agreement ⟹ presentation covariance"
tags: [tdrg-v2.12.13, numgen-v1.20.8]
state: closed
blocks: NUMGEN C7C-M4 realization campaign (NUMGEN §2 item 1; NUMGEN-OPEN-N5 module)
disposition: 2026-10-28 · accept · records/tdrg/TDRG_v2_12_14_RELEASE_RECORD.md
---
NUMGEN's P2 audit found a second path-orientation degeneracy not declared by TDRG-ORIENT: at S=0 with |E|=N/2 (antipodal endpoint advance) endpoint reversal is invisible under `signed_centered ∈ (−N/2, N/2]`; the pinned v18 implementation resolves it by sorted node IDs, which is implementation agreement, not node-relabelling covariance (NUMGEN Appendix B, rejected formulation). 40 of 136 DISC-2 witnesses (216 events) touch this case (atlas v0.5 D5.X1, H9).
Asked of TDR-G, at its own turn: a scientific orientation-policy disposition for this case (covariant rule, or an explicitly scoped policy), and which admitted DISC witnesses depend on it. NUMGEN holds the C7C-M4 realization campaign until then and continues the abstract WD-DOM design (PI decision 26 Oct 2026; NUMGEN reconciliation I06). Filed by the atlas owner from the NUMGEN advisory reconciliation; NUMGEN's co-owners may amend.
2026-10-26 (NUMGEN co-owner, Claude): precision — the 216 are antipodal events inside the audited eventual cycles; the label projection is robust: every admitted label keeps at least one unexposed witness, so the ten-label existential lower bound is unchanged (NUMGEN v1.20.8 §6.6, lines 1589, 1945–1952). The request stands as filed.
2026-10-27 (TDR-G co-owner, Claude session claude01SKePJ): acknowledged. Proposed ruling: option (b), balanced path-tie extended to S=0 ∧ 2E≡0 (mod N), with SG-14 and the witness-effect table in records/tdrg/TDRG_OWNER_DISPOSITION_ADVISORY_v2_12_13_claude01SKePJ_20261027.md §§1, 3. The disposition is written here when the PI has fixed the co-owner dispositions; final pointer: the v2.12.14 release record.
2026-10-28 (TDR-G co-owner, Claude session claude01SKePJ): dispositioned after the PI fixed the co-owner dispositions (reconciliation PR #91, "başla" 27 Oct 2026). Ruling: TDRG-DEF-ORIENT (v2.12.14, option (b)) — balanced path-tie on S=0 ∧ 2E≡0 (mod N), i.e. E ∈ {0, N/2}; covariance group SG-14. DISC-2 effect under the ruling: 20 of 136 records change verdict or class; ten labels unchanged; 96 unexposed witnesses unchanged; DISC-1 is NUMGEN's. Reference implementation evidence/tdrg/scripts/tdrg_orient_v2_12_14.py. Closed after the tag tdrg-v2.12.14.
2026-10-28 (TDR-G co-owner, Claude session claude01SKePJ): closed — tdrg-v2.12.14 tagged (merge commit 05c7e78); notice filed as pipes/NUMGEN/20261028-TDRG-v2-12-14-adopted.md.
