# RTG State Atlas v0.2 — receiving review, round 2

**Date:** 23 October 2026.  
**Reviewer:** ChatGPT.  
**Status:** SESSION / NONCANONICAL receiving decision; not PI acceptance or adoption of owner science.  
**Decision:** **ACCEPT SCOPED — no blocking receiving-review finding remains for the AV02-01–04 correction delta.** PR #11 may proceed to PI acceptance and merge. No additional scientific review, corpus rebuild or certificate campaign is requested.

## 1. Reviewed object and evidence boundary

Repository `MustafaAksu/rtg-corpus`, PR #11, correction commit `9660389eb755558cba1912f5a341d297534db25d`, parent `98f1ef4db546aea97632104499c2c894fd4c1663`. The parent retains round 1 of this review at the same path. The comparison contains one correction commit and no owner DSN modifications.

Read review packet §12; the complete updated checker in contiguous source slices; the complete coverage and identifier maps; updated report and 18-control output; correction-script operations; the acceptance-record draft; and affected Atlas passages. This is the agreed narrow second pass, not a new whole-Atlas audit. The reported Atlas SHA-256 is `9963aead02fad686a9a5bd4d1824882a890ef6279d50899c4090e0e5092331c5` (GitHub blob `a503a357a8381d6a54fefc538445d5731a69fb62`). The reported checker SHA-256 is `0db3a23b9cb78bc87f4b9393baf417c7329421f719f7acbaec2f4ca36626004d` (GitHub blob `4db86e2cce1c3c1b4b75d3448cbaba9eba3291f9`). Whole-file SHA-256 values were read from the pinned acceptance record, not independently recomputed in this pass.

Direct network clone was unavailable. The receiver ran the original six-fixture harness against verbatim extracted current function bodies, with local file-location setup only. The harness matches Git blob `0634552ade6b7a2dc36a775dffa4fff398090c9b`; the loaded owner-identifier map matches `200e322141eddea9e89ce94a54776beebe1af199`. This is a component replay, not execution of the complete checker against all 18 repository sources. The producer's full 18-control result was inspected, not independently rerun.

## 2. AV02 dispositions

| Finding | Receiving decision |
|---|---|
| AV02-01 — checker | ACCEPT at the declared mechanical scope. Coverage requires an explicit node or a designated shared home, not a bare dependency/index/L0/L5 occurrence. Owner-denied and classified consumer strings are not declarations. Conditional markers are bounded and named prerequisites checked. Retired-key and process checks are present. |
| AV02-02 — stale diagnostics | ACCEPT. DYAD.X9 and NUMGEN.N-C2 are removed; DYAD.X4 no longer treats immutable CAND prefixes as grade defects. RECOG.R-C3/R-L9 references are replaced with content links; PHASELAW is THM with an exact-algebra proof qualifier. The full TRIAD-ALG-T6M-REFERENCE-QUARTER-TURN identifier replaces its abbreviation. |
| AV02-03 — process wording | ACCEPT. The four specified process/advisory expressions are removed while scientific targets, actual consumer use and missing obligations remain. |
| AV02-04 — evidence typing | ACCEPT with the evidence boundary in §4. The seven aggregate records distinguish exact/numerical/source checks, identify their v0.1 execution context and EV-NOT-RERUN status, and use approximation signs for the specified rounded values. Per-node redistribution remains deferred. |

The 35 mapped shared homes are limited to the listed lifecycle/frontier and RER record/guard homes. This review does not authorize arbitrary future mappings or infer full semantic preservation from an identifier match. The report's 128 coverage rows include 113 DYAD/RER items and 15 Methodology section checks; they are not 128 independent theorems.

## 3. Receiver execution

| Fixture | Observed | Decision |
|---|---|---|
| RV-N1 — explicitly denied identifier in L5 | DOCUMENTED-UNRESOLVED | expected |
| RV-N1b — denied identifier used as a claim node | FAIL | expected |
| RV-P1 — explicit qualified claim home | PASS | expected |
| RV-N2 — claim missing, dependency mention retained | FAIL | expected |
| RV-N2b — claim missing, L0 mention retained | FAIL | expected |
| RV-N3 — unconditional substituted for conditional bound | FAIL; named R9 prerequisite also missing | expected |

**6/6 receiver fixtures produced the expected outcomes.** A rejected negative fixture is a successful control, not a defect in the submitted Atlas. Receiver result summary: `evidence/atlas/review_v0_2/round2_receiver_results.json`.

## 4. Accepted limitations and nonblocking presentation note

The current report retains 7 UNVERIFIED items (4 links, 3 artifact names), 11 DOCUMENTED-UNRESOLVED names and 19 wording warnings. Separately, equality with the v0.1 input bytes remains UNVERIFIED for 13 sources. Acceptance does not convert any of these into PASS, certify the completeness of the regex grammar, or rerun inherited mathematical certificates. Source-name recognition is not artifact availability or execution.

One nonblocking grouping issue remains in `*ATLAS:checked-D2`: the DZT norm values described explicitly as “80-digit evaluation matched to rationals” sit inside the `exact` segment. The local numerical qualification controls their evidential reading; they are **not accepted as newly exact-certified evaluations**. Move that evaluated list to `numerical` during the planned presentation pass; keep the exact product identity and the separate exact p=12 calculation distinct. No owner result or grade is changed by this note, and it is not a further merge gate.

## 5. Publication decision

Receiving review is complete for this delta. Record the PI's acceptance in the acceptance record, merge PR #11 with a merge commit, then create annotated `atlas-v0.2` on that merge commit naming the final Atlas identity. This review does not fill the PI decision field, merge the PR, create a tag, or delete branches. The Atlas remains derived and NONCANONICAL. The next agreed activity is the RECOG advisory from the accepted snapshot; general compression remains separate.
