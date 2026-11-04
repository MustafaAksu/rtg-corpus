# RECOG R1–R6 — cross-co-owner reconciliation proposal (ChatGPT)

**Date:** 3 November 2026.
**Status:** [SESSION] NONCANONICAL proposal for co-owner reconciliation. This is **not** a joint co-owner verdict or PI authorization. No canonical DSN, release record, certificate, pipe item, merge, or tag is changed by this record.
**Purpose:** compare PR #169 (ChatGPT independent disposition) and PR #170 (Claude independent disposition), adjudicate their R2 difference with a bounded independent check, and define one acceptance checklist for an eventual v0.3.27 content stage.
**Source identities:** RECOG owner at tag recog-v0.3.26 (SHA-256 45e307f8333c81a344158ada07ad34a1a3afab6e1b93b2aa04ee09f84878dd34); DYAD owner at tag dyad-v6.4.23 (SHA-256 9f874ccc1cd684482f26a27fca13b37102977cba2a80a75e762ecd7b300425cb). Governing methodology methodology-v1.4; CONVENTIONS.md.
**Independent records inspected:** PR #169, records/recog/RECOG_OWNER_DISPOSITION_INBOX_20261103_CHATGPT.md (entire file); PR #170, records/recog/RECOG_OWNER_DISPOSITION_INBOX_20261103_CLAUDE.md (entire file), plus its RUN_NOTE.md, script, c7cj_check.json and PR body. PR #168 advisory and entry note (entire files). Owner RECOG §6.13a–b, §6.16e, §7–8 (targeted; the entire v0.3.26 DSN was read in the preceding RECOG co-owner review); DYAD §6.14 NF6/NF-REM/OPEN3/LPHASE (targeted); two certificate scripts (targeted lines for constants). The complete underlying Arb/Lohner packages were not rerun in this reconciliation.

## 1. Reconciliation matrix

| Item | PR #169 | PR #170 | ChatGPT reconciliation proposal | Conditions |
|---|---|---|---|---|
| R1: c'_Q | Accept with change | Accept with change, adding corrected grid | **Converged**; include corrected grid (Claude C2) in the owner dependency replay. | 0.36916 at five current-use text sites and part-1b L55; [COR] at points of use; affected scripts/outputs rehashed; no new theorem or printed result inferred from rerun |
| R2: (D5) | Choose narrow (a) pending independent bounds | Choose (b), extract a RECOG-side substatement | **Choose (b) with one additional rounding correction and independent claim-level review**, fallback (a) if proof/typing gate fails. | See §2: source-independent jet/remainder lemma with its own **proposed** RID, no circular Depends on; correct unsupported printed 100.23 upper ceiling to outward 100.231 or expressly state rounded display while using a certified bound; one exact rational gate; PI acceptance separate |
| R3: C7-SHARP | Accept scoped import | Accept scoped import; NC2 unchanged | **Converged**. | Import DYAD-THM-NF-REM-C7-SHARP at matching disks; remove former C7 assumption; preserve C_D and NC2; do not recompute K_epsilon in this edition |
| R4: source audit | Quote current theorem strings with negative controls | Also catch prefix matches | **Converged**; use delimiter-aware context plus negative control. | Old quoted values may occur as prefixes of new exact decimals and in historical COR notes; previous release scripts stay unchanged |
| R5: OFN | Receipt only | Receipt only | **Converged**. | No imported scientific claim changes; current companion reference may point to ofn-v0.12; pipe reception distinct from adopted use |
| R6: pins | Claim-level use pins | Repin every Dyadic pin | **Compatible on current uses**: repin all *live, current-use* Dyadic claim citations to dyad-v6.4.23; preserve intentionally historical/provenance pins, identified as historical. | Repin audited NUMGEN uses to numgen-v1.21, companion GEN to gen-v2.10, OFN to ofn-v0.12; preserve TDR-G as reference-only; no automatic consumer acceptance |

This is the ChatGPT reconciliation proposal, not yet a confirmed two-co-owner reconciliation.

## 2. R2 — independent sufficient proof and new precision finding

[OWNER: RECOG v0.3.26 §6.13b / RECOG-ALG-A1C-COMBINED-TAIL] The adopted block derives pointwise majorants for the two tail terms from the adopted NF6 jet and NF-REM C7=100, then sums these over the orbit. Its proof paragraph presently prints c_J^R=0.5008 and c_7^R=100.23. The block as a whole depends on RECOG-ALG-A1C-TAIL-HARMONICS, which itself carries (D5): citing the entire combined-tail result as an upstream proof of TAIL-HARMONICS would create a dependency cycle.

[SESSION — ALG] Extract the **pointwise jet/remainder sublemma only**, with no reference to TAIL-HARMONICS, from the actual G2 formula of evidence/recog/scripts/recog_a1c_combined_tail_cert.py:

Let q=|z|^2 in (0,q*], q*=256/140625<1/400; J(z)/z=1+mu q+(a32+a05 exp(-6iTheta))q^2, with DYAD-ALG-NF6 coefficients. Let A5=|a32|+|a05| and u=|mu|q+A5 q^2<1. DYAD-THM-NF-REM bounds |Fhat-J|<=100|z|^7; set w=100q^3/(1-u)<1. Principal-angle log-series bounds imply

  |Arg(J/z)+tau q| <= cJ(q) q^2,
  cJ(q) = |Im(a32-mu^2/2)|+|a05|+|mu|A5 q+A5^2 q^2/2+u^3/[3(1-u)q^2],

  |Arg(Fhat/J)| <= c7(q) q^3,
  c7(q)=100/[(1-u)(1-w)].

All terms in these majorants are nonnegative and increasing in q on (0,q*]; the term u^3/q^2 increases since u=q(|mu|+A5 q). Therefore it suffices to bound q=q*. These are exact analytic inequalities, not fitted coefficients. The tail estimates follow by summing pointwise bounds with the already adopted one-orbit contraction.

[SESSION — ALG, exact-rational sufficient envelopes] Set
  sqrt(3)<1732051/1000000,
  1.2583<|mu|<1.259,
  1.0768<|a32|<1.077,
  0.02128<|a05|<0.0213.
The inequalities follow by squaring and comparing exact rationals using |mu|^2=19/12, |a32|^2=(97/432)^2+3(197/324)^2, |a05|^2=(49/8640)^2+3(307/25920)^2. Using these bounds in the monotone formulas at q* proves (all rational comparisons):

  cJ(q*) < 0.500819 < 0.50220;
  100.2300186 < c7(q*) < 100.230147 < 100.231 < 157.58.

The particular **published majorant formula** therefore exceeds 100.23, although the true phase remainder might satisfy a sharper bound. No counterexample to the underlying phase inequality has been constructed. The exact-rational gate evidence is evidence/recog/inbox_reconciliation_20261103/recog_r2_rational_bounds.py (SESSION script; run completed: 6/6 PASS, no owner certificate replay). A 70-digit independent evaluation of the same formulas yields cJ(q*)=0.500798405701573... and c7(q*)=100.230019682581882....

**New finding R2-PRECISION-01 [SESSION]:** The bare equality c_7^R=100.23 at RECOG v0.3.26 §6.13b is not an outward-certified ceiling from the published formula. A suitable outward display is 100.231; retaining the current exact-interval formula in computational certificates does not require replacing those outputs. The RECOG owners must decide whether to introduce a point-of-use [COR] and a historical correction entry under Methodology §3.6. Do not silently preserve 100.23 as a rigorous ceiling or claim that it has been mathematically refuted as the optimal value.

**Proposed ownership/citation change:** At v0.3.27, a candidate RID such as RECOG-ALG-A1C-JET-REMAINDER-BOUNDS could state the two pointwise estimates, with conservative ceilings cJ<=0.50220 and c7<=157.58 (or stronger outward ceilings cJ<=0.500819 and c7<=100.231). Its proof depends *only* on DYAD-ALG-NF6, DYAD-THM-NF-REM and the declared q* disk, not on TAIL-HARMONICS or COMBINED-TAIL. Then DYAD-THM-LPHASE-ROWA-BRIDGE supplies the exact decomposition, c_Q and c'_Q; DYAD-THM-OPEN3-SPIRAL-REM supplies K_Theta. The five A1c (D5) uses can then cite these independent premises without [assuming: (D5)]. The proposed RID is not registered by this record and requires an owner decision and a separate change-focused scientific review, even if grouped into one maintenance-sized release.

**Fallback (a):** if source-independent proof, clock/norm, or acceptance gate fails, keep [assuming: c_J=0.50220 and c_7=157.58 as Dyadic proof constants] until a later proof/disposition. Never imply that a rounded certificate output is a proof of a sharper ceiling.

## 3. Implementation acceptance checklist (one content stage)

1. R1: replace five current-use 0.36915 strings and the single part-1b literal by 0.36916. Keep the adopted D5/U/row-A/branch-B contract until independently discharged. Run the **eight** owner A1c certificates and the additional corrected-grid computation, including the joint-transfer and drift proof-table outputs; bind source/output hashes, record the six-million-step part-1b input and one negative control. Historical releases and their scripts remain unchanged, apart from the expressly corrected live evidence script.
2. R2: extract a source-independent pointwise lemma and provide its algebraic proof/gate; certify outward rounding (R2-PRECISION-01), separate from a mere numerical 70-digit evaluation. Review the absence of cycles in the proof DAG before removing the five (D5) qualifiers. Update linked §1, §2 and §7 wording with the actual new proof status; no physical conclusion or theorem grade promotion.
3. R3: import C7-SHARP with rows unmixed and the old C_D values unchanged. Keep the B1 certificate and conservative NC2 intact. K_epsilon improvements using C7=85.1 stay outside this round.
4. R4: re-quote exact current owner theorem rows with delimiters; add fail-closed negative tests for 0.36915 in a current-use qualifier and for the source-quote prefix trap; do not modify historical claim-audit scripts.
5. R5–R6: synchronize current-use owner references (including NUMGEN GAP-LOCK Lemma-3 RID), with archival pins explicitly labelled; record OFN receipt and consumer notices without assuming accepted/adopted downstream use.
6. Review the complete change once, including the newly observed R2 precision correction. A script PASS is not scientific adoption. The PI decides the final content, merge and tag. No compaction or unrelated scientific campaign is required.

## 4. Disposition states and unresolved obligations

- R1, R3, R4, R5 and the current-use R6 scope: **provisional reconciliation agreement**, pending the other co-owner's explicit acceptance of this proposal.
- R2: **proposed option (b) with an outward-bound correction**, contingent on independent scientific review and PI authorization; if rejected, (a) is the nonblocking fallback.
- All R1–R6 statements concern the adopted, postulated continuous generator T; no event-token selection, network carrier bridge, R6 closure, physical exchange, or OPEN-P0 closure.
- PRs #168, #169 and #170 remain independent unmerged records; their recorded hashes and evidence are not altered by this proposal. No pipe item is closed by filing this document.
