# TDR-G v2.12.15 — ChatGPT co-owner change-focused review

**Date:** 2026-11-12  
**Verdict:** **CONDITIONAL PASS** — one required mathematical-scope correction (R1), one bounded precision clarification (R2); no new campaign or model rerun. Review only, **not adoption**.  
**Target:** PR #248, `claude/tdrg-v2-12-15-stage1`, head `e2db210dfdef96c0d0274a02fe4acd5c2e050650`. Candidate SHA-256 `429a57f220b32ccc6559abc26f146d5db4fbf081bcd02529f286723f37b54f19`.  
**Governing base:** `tdrg-v2.12.14`, `dsn/RTG_DISCRETE_GENESIS_DSN.md`, SHA-256 `3be72923cd40523399363e0dc044bba6246862d12b2bca190c74969e2cce2392`.  
**Rules:** repository-root `CONVENTIONS.md` on `main` (blob `eafa6f6189675516d860b1390283ccedc6061571`), adopted Methodology v1.4 for review and release discipline; candidate explicitly keeps declared Methodology v1.2, with v2.13 migration separate under PI direction.

## 1. Reading extent, identity and evidence grade

**[SESSION]** Read the complete PR #248 changed-file inventory and the candidate's changed scientific clauses in §§1–3, §6.3, §6.12, new §6.13, §§7–8, Appendix A/B and release record. Compared the 32-entry exact-once edit log with the source sections and inspected the builder, the checker C0–C10 including its seven negative controls, and the stored outputs. Cross-checked `TDRG-DEF-STAR`, `CONV-TICK`, `LEM-SPECCONS` and the event inventory against `tdrg-v2.12.14` and the pinned engine source. Reviewed the relevant `AZ_TOKEN_RESONANCE_PREREGISTRATION.md` §2 and the TDR-G owner inbox disposition PR #243 and its test evidence. Historical BIND3, NKSCAN, scaling campaigns and unaffected sections were not reviewed/recomputed anew.

**[SESSION — independent source identity check]** Computed SHA-256 on GitHub-fetched full text for:
- candidate `429a57f220b32ccc6559abc26f146d5db4fbf081bcd02529f286723f37b54f19`;
- builder `e14f465f9e3a5f6cb7b7d606cc6366b55d88531bacc774203efbb1926bbb526d`;
- checker `b633738baacc99e70ccff18bbf1102d716d63ea30c75abb70d24d807565b52d4`;
- edit log `35824f8c3deebee23ae0413efecc1e3cbf4ff062c828bd640058d67f462d0815`;
- source AZ preregistration `198d2f4af9ae338fec007874d003c755674ac90da087411c57c51d63714fb829`.

The hashes match the release-record source identities. The builder reports 32 edits and the candidate registers exactly 9 new RIDs. The owner-run `check_output.txt` reports 11/11 gates; `controls_output.txt` reports 7/7 negative controls caught (including a mutated engine star map that fails C10). Its bounded C10 sample reports 12,635 ticks, zero token-law violations and the two expected star/spectrum fixtures. These are **source-reported owner-run checks**; this reviewer inspected the checker and stored outputs but did **not** execute a fresh full Git checkout or repeat the owner's random campaign.

## 2. Validated scientific changes

**[SESSION]** N4, the correction of `TDRG-DEF-STAR` to the actual single-valid-centre component domain, is meaningful and well-defined, not merely typographical. The valid-centre condition, classification precedence and inertness of other component nodes agree with the inspected engine. In the narrow-band domain `k<N/6`, the new `TDRG-ALG-NARROW-BAND-CLASSES` implication follows algebraically: triangles are forbidden, hence every vertex of degree at least 3 has pairwise nonadjacent neighbours; a connected triangle-free component with maximum degree at most 2 is an edge/path or (length at least 4) cycle. The residual graph classes cannot occur in that domain. This does **not** select a unique physical multistar policy or establish node-label covariance of `largest_center`.

The token census proposition follows event-by-event from permutations, identity, and `x -> (-x,x)`; the birth-spectrum injection formula follows by multiset enumeration, including pairs among several newborns. It is a multiset identity, **not** a list of unchanged old edges plus newborn-incident edges. The `n`-node birth-free spectrum invariant follows from the unchanged token multiset. The `D(C)=D(C')` counterexample correctly shows that the unlabelled difference spectrum alone does not determine its birth update. The parent–child phase formula is conditional on persistent centre and child tokens; it does not establish survival, a growth mechanism or a TDR-26 defective-basin result. AZ's Stage 1 numerical risk differences are not imported into this edition.

The OFN token-sum correction is correct: `P=sum(delta_i)` is invariant under the declared phase gauge and node relabeling, but changes by `-x` under a star birth with centre token `x`. “Not adopted as a physical momentum observable” is a model commitment independent of both facts. The TDR-24A→B→C launch gate, source pins and TDR-6 `ACTIVE — PARTIAL` grade are preserved at their respective scopes.

## 3. Required correction R1 — unjustified universal no-invariant statement

**Locations:** Candidate §2 `TDRG-OPEN-BIRTH-INVARIANT` sub-item after the new predictable-change law; new §6.13 introductory guard. The phrases are:

- “TDR-6 is not closed — **no purely relational quantity is preserved across births**.”
- “**none is an invariant of the full dynamics across births** ...”

The first is an unproved **universal nonexistence claim**. The second, read as a mathematical claim about the listed token-state objects, is too broad.

**[SESSION — ALG; new bounded deduction, not adopted]** Under the same event inventory (E) one can construct an exact conserved *set of occupied signed-token classes*:

[
mathcal I(X)=igl{,[delta_i]_{pm}: iin V,igr},qquad
[x]_{pm}={x,-x}subsetmathbb Z_N.
]

Token permutations/identity preserve the set. Under a star birth at `x`, the pre-event `[x]` is represented by the centre, and after the event by both `-x` (centre) and `x` (newborn). No new signed class appears, and none disappears. Therefore `I(X_{t+1})=I(X_t)` for **all six policies and any number of simultaneous births**, as an algebraic consequence of (E). This is invariant under the *declared* phase gauge and node relabeling. Whether it qualifies as an **admissible physical/purely relational observable** under TDR-G's observable-selection contract is a separate, unresolved question; this review does not assert such adoption. It nonetheless defeats any unqualified mathematical claim that the full token dynamics has no invariant across births.

**Acceptance:** Preserve TDR-6 as **ACTIVE / PARTIAL** and the proved conditional birth-update law. Replace the universal statements with precise supported limits, e.g. “No autonomous update law for the unlabelled pairwise difference multiset alone, nor a sufficiently specified full-dynamics relational invariant closing TDR-6, has been established.” In §6.13 say explicitly that the *complete pairwise-advance spectrum* is **not conserved** across births, rather than “none is an invariant”. Either note the signed-class-support result as a nonadopted observation for future observable selection, or explicitly defer its physical interpretation without incorporating it as a new owner claim. No additional campaign or extra RID is required for this correction.

## 4. Bounded precision clarification R2 — parent–child order quantifier

**Location:** `TDRG-ALG-PARENT-CHILD-PHASE`, §6.13. The assertion “The separation stays in `{N/2,0}` iff `4x ≡ 0`” needs a clock quantifier. If the persistence hypothesis covers zero advances, the finite observed segment lies in the set for **every** `x`; the intended statement is the formal free orbit for **all** `j≥0` (or a segment containing the first advance), conditional on token persistence. Add that explicit quantifier. The displayed formula itself and the order-1/order-2 arithmetic are correct. This is a **nonblocking editorial precision fix** and should be bundled with R1.

## 5. Publication and provenance boundary

- PR #247 contains the two `no action` closures and is a direct parent of the PR #248 head (commit `fa122c51475f093453759cf2c1d9be47a99036b3`). **Merge #247 before #248**; re-check branch index and BASELINE after the integration.
- Candidate §7 correctly keeps historical owner pins where claim-specific, credits AZ's SESSION proposal without promoting the AZ Stage 1 numerical campaign, and keeps the Methodology v1.4 migration/compaction for TDR-G v2.13.
- The updated `BASELINE.md` row and DRAFT release record are **publication preparation only** until a PI adoption, merge commit and annotated tag. A checker PASS is neither adoption nor proof of semantic equivalence.
- Required next review steps remain an atlas row-check/replay on the corrected candidate, the PI's explicit scientific adoption, and the separately authorized merge/tag. No such actions are taken by this record.

**Review verdict:** **CONDITIONAL PASS**, with **R1 required** and **R2 recommended for the same correction batch**. No rerun of historical BIND3/NKSCAN/scaling or new token campaign is justified by these two wording/scope repairs.


## 6. Round-2 change-focused readback — 12 November 2026

**[SESSION] Verdict: ACCEPT SCOPED, no remaining scientific/scope correction on the reviewed candidate.** This is a readback on the second candidate of PR #248, not a withdrawal of the original round-1 CONDITIONAL PASS above. PR #248 head when read: `9b82993d3e979b45c512304f49bea77c8c886c19`. TDR-G candidate SHA-256: `1e35be54a37bb227cd75e34fc1cd6732ae95782bdc147a76e736f16760c92e64` (196,268 UTF-8 bytes). Previous round-1 candidate: `429a57f220b32ccc6559abc26f146d5db4fbf081bcd02529f286723f37b54f19` (194,602 bytes). Both hashes were independently computed from the complete GitHub-fetched files (EV-BYTES, EV-HASH).

**Reading extent and diff boundary.** Compared the two full DSN texts by an independent line sequence diff: **8 changed blocks, 8 replaced old lines, 9 new lines**. Read every changed line (TDR-6, OPEN-SPECCONS-STAR, SG-12, LEM-SPECCONS, §6.13 scope guard, TDRG-ALG-TOKEN-CENSUS-LAW, TDRG-ALG-PARENT-CHILD-PHASE and Appendix A). Cross-checked against the previously reviewed event inventory, the owner release record's §3a, and the atlas row-check `records/tdrg/ATLAS_ROW_CHECK_TDRG_v2_12_15.md` (PR #252). No other DSN line changed between the two candidates. The PR #248 branch has since integrated `main` and PR #247 to resolve its pipe-index conflict; its DSN Git blob remains the one read here. This reviewer did not rerun the owner runner, historic campaigns, full checker, or negative controls; the Atlas owner reports an independent 11/11 gate and 8/8 negative-control rerun with byte-identical outputs (EV-SRC-REPORTED in this review, not EV-RUN).

**R1 — closed, including the owner's three-place extension.** Under `TDRG-ALG-EVENT-INVENTORY` (permutations / identity / snapshot star replacement \(x\mapsto(-x,x)\)), the token multiset only gains \(-x\) per birth. Hence the *set*, not multiset, of occupied signed-token classes
\[
\mathcal I(X_t)=\{[\delta_i]_\pm:i\in V_t\},\qquad [x]_\pm=\{x,-x\}\subset\mathbb Z_N
\]
is exactly conserved across every tick, for every listed policy, at the declared event scope. This is a symbolic deduction from the census law; admissibility as a *physical/purely relational observable* is not established. The new `TDRG-ALG-TOKEN-CENSUS-LAW` item (iii) states and proves this, without claiming to close `TDRG-OPEN-BIRTH-INVARIANT`. The revised TDR-6 text correctly says the **full pairwise-advance multiset** grows at birth and has no closed transition determined by \(D_t\) alone; it does not claim universal nonexistence of conserved quantities.

The extensions at OPEN-SPECCONS-STAR, SG-12 and LEM-SPECCONS correctly restrict the still-open obligation to a *spectrum-level* invariant or a law closed on the spectrum. Independent exact finite check at \(N=24\): \(C=(1,3,4,5)\) and \(C'=(2,4,5,6)\) have identical pairwise cyclic absolute difference multisets \(D=\{1,1,2,2,3,4\}\), but occupied signed classes \(\{[1],[3],[4],[5]\}\) versus \(\{[2],[4],[5],[6]\}\); thus \(\mathcal I\) cannot be recovered from \(D\) alone. On a birth at centres \(1\) and \(2\), the extra pairwise differences are \(\{2,4,5,6\}\) and \(\{4,6,7,8\}\), respectively. No physical invariant or dynamical mechanism is inferred.

**R2 — closed.** The amended `TDRG-ALG-PARENT-CHILD-PHASE` states the equivalence for the **entire formal free orbit**, conditional on the centre/child token-persistence hypothesis for all \(j\ge0\). Already at \(j=1\), \(\Delta_1=N/2+2x\in\{0,N/2\}\) iff \(2x\equiv0\) or \(N/2\pmod N\), equivalently \(4x\equiv0\pmod N\) for even \(N\). A window with zero advances yields no restriction. This does not assert persistence after interactions or infer a TDR-26 growth mechanism.

**Editorial provenance note:** The displayed formula in round-1 §3 above suffered a Markdown/escaping transcription error (including backspace characters); the correct formula is the \(\mathcal I\) display in this addendum. The earlier text is retained as historical review evidence and is not silently rewritten.

**Publication boundary.** This ACCEPT SCOPED readback finds no outstanding R1/R2 condition, but does not adopt the TDR-G result, validate the entire unchanged DSN, or certify the owner's 223,651-tick run. The PI decides adoption of these exact candidate bytes. PR #250 (this review record) should be merged before PR #248 so its referenced path is available; PR #247 merges before #248. PR #248's publication/pipe/BASELINE check and any final status-line transform are separate governance steps. No merge, tag, pipe state or owner DSN modification was performed by this reviewer.
