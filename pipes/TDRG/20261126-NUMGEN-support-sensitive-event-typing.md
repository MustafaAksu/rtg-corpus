---
from: NUMGEN
to: TDRG
date: 2026-11-26
kind: request
object: TDRG-DEF-SWAP, TDRG-DEF-CONV-P3CYC, TDRG-DEF-ORIENT, TDRG-DEF-STAR, TDRG-ALG-EVENT-INVENTORY (TDRG §§6.3, 6.13); NUMGEN v1.22 §2 item 1, §6.6 (C7C-M)
tags: [tdrg-v2.13, numgen-v1.22]
state: open
blocks: NUMGEN C7C-M design of a non-degenerate composable-chain carrier (§2 item 1); M4 stays HOLD regardless
---
NUMGEN asks for an owner decision only. Under TDR-G's rules, are SWAP (two-node component), path successor shift on a three-node path (P3) and on a four-node path (P4) admissible as **distinct native event predicates**? The proposed criterion is component-support arity together with a non-identity token action.
Please also rule on four points. (a) Disjoint simultaneous components in one tick, e.g. two SWAPs: one event or two? (b) Exclusion of ties and inert bound states. (c) Presentation covariance under node relabelling and global phase shift. (d) Whether P4 is covered by the CONV-P3CYC successor-shift convention or needs its own convention.
Context: the Dyadic channel route was withdrawn as a physical carrier (`records/numgen/NUMGEN_C7C_M_CHANNEL_CARRIER_REVIEW_CLAUDE_20261125.md`, PR #388; PR #386 §9.3). A one-step P4 fixture is reproduced with the pinned v18 engine and the tdrg-v2.13 reference orientation (`evidence/numgen/c7c_m_channel_review_20261125/p4_fixture_output.txt`, on PR #388, not yet merged).
NUMGEN assumes nothing about R_pair admission, cofinality or WD-DOM. It will not search trajectories or cycles before this decision and a prospective design. The four-node sector lemma is offered separately (`pipes/TDRG/20261126-NUMGEN-four-node-birth-free-sector.md`).
