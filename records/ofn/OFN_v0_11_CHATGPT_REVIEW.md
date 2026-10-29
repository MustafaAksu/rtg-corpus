# OFN v0.11 — ChatGPT change-focused co-owner review

**Date:** 29 October 2026.
**Reviewer:** ChatGPT, OFN co-owner; not the builder.
**Object:** PR #112, branch `claude/ofn-v0.11`, reviewed head `b408cef3cdc9ad32e86118e6390b4af9938cde58`.
**Verdict:** **ACCEPT SCOPED for the scientific/contract delta; two bounded current-state corrections required before adoption.** One additional clarification is recommended in the same patch. No unresolved scientific disagreement with the joint reconciliation is identified. This review is not PI adoption, merge authorization or an assertion that the Atlas replay has happened.

## 1. Identities, source reads and verification boundary

The inspected candidate is `dsn/RTG_ONTOLOGICAL_FOUNDATIONS.md`, Git blob `081101e5897480988ae975b41e02f57362c00767`. The release record identifies its SHA-256 as `709d613eb2f8608813a105d95c36b3b3564ac4064c384336996649d9c15a4887` and the frozen stage-1 SHA-256 as `cf38b61b5cd3e268e412dbd10b28a2117f86f1c7423fd2dd33f466a8e5437ce3`. These two SHA-256 values are **builder-recorded identities**, not independent whole-file hash measurements by this review.

Read directly through the connected repository, at the fixed review commit unless otherwise stated:

| Source | Reading extent / purpose |
|---|---|
| `CONVENTIONS.md` | Full; read before this review write |
| `records/ofn/OFN_COOWNER_ENTRY_NOTE.md` at `b0dc6dbe` | Review order, source authority, scope, and separation of co-owner review from Atlas replay |
| `records/ofn/OFN_v0_11_RELEASE_RECORD.md` | Authorization/identity table, all disposition-to-edit rows in §3, custody/inbox/consumer boundaries, all stage-2 operations and tool limitations in §7, proposed finalization |
| Candidate DSN | Targeted: §5.5, the affected §9 reduction/frustration entries, §11.2 affected imports, §11.3–§11.5 reference/import records, §12 and the Appendix A boundary. This is not a new full reading of every unchanged foundational proof |
| `build_ofn_v0_11_stage1.py` | Targeted: build preconditions/edit modes, global repins, header and six DEF registrations, TDR-G/custody edits, and §5.5 amendments |
| `check_ofn_v0_11_stage1.py` | Full: K1–K9 and C1–C14 definitions |
| `build_ofn_v0_11_stage2.py` | Full: all 16 operations, archived-intermediate contract, and generated profile |
| `check_ofn_v0_11_stage2.py` | Full: G0–G10 and F1–F14 definitions |
| `tools/check_compaction.py` | Targeted: vocabulary, RID expression, `split_regions`, `base_history_start`, `live_text`, feature and claim-block extraction |
| DYAD at `dyad-v6.4.22`, §6.17 | Smooth embedding E1–E4, recorded distinctions, smooth equivariant chart, and remaining OPENs; directly checked against the new imports |

The joint settlements previously confirmed on PR #110 remain the decision basis. Their substantive choices are not reopened here. Old scientific certificates, the FMS P4 campaign, the 20-file custody intake, and unrelated owner results were **not** replayed in this review.

**Execution boundary.** The two v0.11 builders and the complete K/G/negative-control suites were not independently executed here. Their PASS counts in the release record remain builder reports. Direct repository download into the calculation container was unavailable; source inspection through the connector was available. The small independent checks described in §5 were executed. The planned Atlas task remains the full build/hash/row replay, not a purported second replay by this reviewer.

## 2. Accepted scientific and contract changes

### 2.1 Rows 1–3

The new smooth-realization use follows the inspected owner statements. `DYAD-THM-SMOOTH-EMBEDDING` supplies the local smooth roots and J; `DYAD-THM-SMOOTH-EQUIVARIANT-CHART` supplies Phi with D Phi(0)=I and N_Phi commuting with A. The draft keeps the E2 zero-linear-part uniqueness restriction, qualitative radius, SG-19 non-transfer of finite-chart constants, and the analytic/physical OPENs.

The OFN lock-surface deduction is valid: commutation with A, A^3=-I and I+A^2+A^4=0 give oddness, threefold equivariance and cancellation of the mean on the coincidence/equilateral surfaces. It supplies real smooth invariant submanifolds for C2; it is not a new DYAD existence proof, a basin theorem or closure of OPEN-OFN-3B.

The explicit test-class amendment to real C-infinity germs is accepted. Real-analytic laws remain a distinguished subclass; Q6 comparison regularity remains local C3. This is not a universal physical regularity axiom.

The corrected Standard C declaration matches the agreed positive-dimensional embedded C3 manifold-germ test, nonzero states arbitrarily close to zero and uniform punctured-domain order-four bound. It excludes a singleton without excluding a coincidence embedding merely because one edge vanishes. The raw-family no-go and the non-manifold/finite-amplitude boundary remain separate.

### 2.2 Other affected interfaces

- The narrow-Q6 conclusion is given the agreed single `[from: ALG]` status with the Genesis THM premises stated separately; actual C2 use is distinguished from formal series and polynomial representatives.
- The parameter table separates coupling-theorem scope, flatness, lock identities and mean-mode attraction. Exceptional values are not falsely declared failures of all lock identities.
- Finding A statement acceptance is distinguished from deferred custody transfer; N4 and N6 are different receipts.
- RRF's model-contract and representation-level readout deliveries are consumed without selecting a native physical profile or requiring a new sign-reading scalar.
- NUMGEN L-BACKBONE is typed as the primitive block-sampled observable; the DYAD contraction input remains separate.
- RECOG's old freeze provenance is distinguished from the newer governing source pin; reference-only event/record results do not become OFN physical event definitions.
- ER-2B A.4 and C11/C15B/C20 are both cited; Delta_4 S is correctly bounded to homogeneous degree four. Authentication of v0.3.1 remains deferred, with no whole-file substitution claim.
- The six new DEF identifiers, the existing OPEN statuses, FMS P4 evidence qualification and absence of physical carrier/modulus selection follow the agreed plan.

These acceptances concern the changed use and contract. They are not blanket re-certification of every upstream result or every unchanged sentence.

## 3. Bounded findings for one correction pass

The identifiers below are review-local finding labels, not scientific RIDs.

### R112-C1 — stale primitive-map custody sentence (required)

**Location:** §11.2, IMP-O08-13, Reconciliation sentence.

Current:

> Dedicated result ID located; separate map-definition custody remains unresolved.

This contradicts the same candidate's §12.3 `CUST-O09-01 — primitive-map identity: answered`, §12.4 REQ-O09-04 FULFILLED, IMP-O08-12 and settled row 16.

Replace with:

> Dedicated result ID located. Primitive-map custody is separately resolved by `DYAD-DEF-PRIMITIVE-MAP`, with `GEN-DEF-PRIMITIVE-MAP` retained as the Genesis alias (IMP-O08-12; CUST-O09-01 / REQ-O09-04 fulfilled).

**Acceptance criterion:** no live assertion that this map-definition custody is unresolved; the linear-order-six result remains distinct from map custody and generator selection. Extend the stale-state control narrowly enough to catch this sentence without deleting historical records.

### R112-C2 — historical handoff still labelled the sole current input (required)

**Locations:** §5.5 opening `Source and status` paragraph and §12.1 `governing handoff v0.8.2` row, whose Consequence cell still says `Single input for §5.5`.

The handoff was the single integration input for v0.10. It is not the single governing input for the revised §5.5: v0.11 also consumes the joint owner dispositions, changes two contracts, and imports the later DYAD smooth results. Registration of the retained RIDs in v0.10 and amendment of their bodies/use in v0.11 must not be conflated.

Suggested §5.5 opening:

> The historical integration input for v0.10 was `OFN_REPLY_TO_FMS_MODEL_SELECTION_v0_8_2.md` (SHA-256 `6e4fc3c3…564b1d`), accepted by both co-owners. Its DEF and RESULT identifiers were registered in v0.10. The present v0.11 changes are governed by the joint owner reconciliation and this edition's release record; the Standard C and test-class amendments are recorded in OFN11-C01/C02. Technical results retain their owner grades and FMS SESSION results remain reference-only.

Suggested evidence-row consequence:

> Historical single integration input for v0.10 §5.5; retained evidence baseline, amended for v0.11 by the joint owner reconciliation and current imports. Handoff acceptance is distinct from edition adoption.

**Acceptance criterion:** preserve the accepted handoff identity and earlier registration provenance, but remove the claim that it alone governs the amended section. No source or evidence status is upgraded.

### R112-N1 — qualify the explanatory sufficiency sentence after Standard C (recommended)

**Location:** §5.5.2, `Physical-isolation scope` paragraph, immediately after the corrected definition.

The inherited sentence says that an invariant regime where interaction vanishes algebraically satisfies the mathematical contract. Read literally in isolation, that shortcut omits the newly explicit manifold/nontriviality requirements. The definition itself is correct; no additional contract decision is requested.

Recommended replacement:

> On a regime satisfying the manifold, nontriviality, domain and clock requirements above, I_e identically zero for every edge satisfies the recovery-order bound. Algebraic cancellation alone establishes neither the other regime requirements nor physical removal of the surroundings. Physical isolation remains OPEN-OFN-TRIAD-CLASS.

This is a point-of-use clarification of the settled row-3 decision, not a new restriction or a new theorem.

## 4. Stage-2 assessment

The full stage-2 builder confines its declared operations to header status wording, specified historical prose/labels, historical register/adoption sections and Appendix C. It retains the stage-1 intermediate as the byte archive and stable history pointers. The inspected operations do not introduce a new scientific claim or change a chosen model contract. Retaining Appendices A/B with their quotation boundaries is consistent with the declared foundational profile.

The owner guards address material generic-tool limitations: G2/G6 inspect RTG-OFN identifiers and register rows, and G9 checks identifiers against text outside the candidate's Appendix C. F5, F11 and F12 directly target those omissions. Preserving their role is necessary; a generic-tool PASS alone is not a sufficient OFN preservation argument.

This is a source/semantic review of the operations and guard design. The reported `188/188` byte-identical claim blocks, `43` OFN identifiers, `100` anchors and fixture PASS counts have not been remeasured by executing the full suites here.

Apply C1/C2, and preferably N1, in the **stage-1 content build**, retaining the previous frozen intermediate in Git history. Freeze the revised intermediate; rerun the unchanged layout stage against it; update hashes/maps and the draft release record. Do not hide these edits in the publication-only finalization step. This is one bounded correction pass on the existing PR, not a new release or a new scientific campaign.

## 5. Independent checks actually executed

A bounded reviewer implementation executed the following checks:

1. With the exact real matrix A=[[1,-1],[1,0]], A^3=-I, A^6=I and I+A^2+A^4=0. For an arbitrary output vector v, the tuples (v,-v,0) and (v,A^2 v,A^4 v) have zero sum and are unchanged by subtraction of kappa times that mean. **PASS.** The owner equivariance/existence premises are imported, not proved by this matrix test.
2. The exact `RE_RID` expression from the inspected generic tool returns no match for `RTG-OFN-DEF-STANDARD-C`, while matching `DYAD-THM-SMOOTH-EMBEDDING`. **Limitation reproduced**, with a positive control.
3. A function-level copy of the inspected `split_regions`, `base_history_start` and `live_text` functions, on a minimal candidate with a `Compact Version History` in Appendix C, retains a `DYAD-ALG-ONLY-HERE` identifier in `live_text(candidate)` even though it occurs nowhere outside that appendix. **Limitation reproduced.** This tests the parser behavior, not the full generic checker or the OFN fixture suite.

No output from these bounded checks is represented as a deterministic v0.11 build replay. The script and output were executed locally in this reviewer session; the repository checker was not modified.

## 6. Completion and authority

The substantial scientific/contract choices remain accepted. C1 and C2 are current-state consistency defects, not unresolved co-owner policy differences. N1 can be included with them without opening a new study. A delta check of those bounded edits and the scheduled Atlas row/build replay are sufficient next checks; unchanged scientific campaigns should not be rerun.

The accepted-object SHA must be updated after the correction pass. This record does not designate the current `709d613e…4887` bytes as final adoption-ready. The prerequisite records and authenticated intake must be present in the eventual release ancestry as agreed. No intake placement, main merge, tag, inbox closure, scientific adoption or canonical content edit is performed by this review.

`ofn-v0.10` remains the governing adopted edition. The PI's adoption remains separate from this co-owner review.
