# Methodology v1.4 amendment — editor review and replacement clauses v0.1

**Date:** 22 October 2026.
**Status:** SESSION / NONCANONICAL editorial-governance review. No adoption, source-file amendment, script execution, or stream notice is performed by this document.
**Reviewer:** ChatGPT.
**Decision:** Accept the direction and the one-release DYAD pilot. Revise the checker contract, archive wording and conflicting instructions before whole-file assembly. Do not reopen unchanged scientific results.
**Latest PI clarification:** History files are kept in the archive, not in the active project-document set. This overrides the submitted amendment's D4 location wording.

## 1. Sources actually inspected

| Source | Inspection | SHA-256 of supplied bytes |
|---|---|---|
| `DSN_METHODOLOGY_v1_4_AMENDMENT_DRAFT_v0_1.md` | Complete; 78 lines, 7,449 bytes | `45d4fa81cb385d7d4d79be7309e7835a280928052e25bcd584f4c57769b56188` |
| `ATLAS_CLOSEOUT_DYAD_v6_4_20_FINAL_v1_2.md` | Complete; 234 lines, 19,709 bytes | `32185ee4d6ea651c43b92044ccd3dcca3635a9fdc8cd5a494cb4cf396bec6a8c` |
| `DSN_METHODOLOGY_v1_3.md` | Relevant provisions in §§0–7, 9–13 and Appendix A; not a fresh full-document scientific review | `3e23ba94606706b3c8d50aecfb2184df52042cf8e65cdd3c3e0cd3159254ec7e` |

The v1.3 hash matches the amendment's declared base. The original size-discipline proposal was not inspected. The PI clarification is supplied in the current conversation. Historical review/test counts quoted inside the closeout were not replayed here.

## 2. Findings and dispositions

| Key | Location | Required resolution |
|---|---|---|
| M14R-01 | Decision D4; A8; closeout §8 | Archive-only history; one logical filename, but retrievable immutable release snapshots. A changing path alone is not a durable hash-pinned reference. |
| M14R-02 | A7 | Preserve qualified claim blocks and their associations, not a global bag of RIDs/tags/equations. Retaining a removed passage in the predecessor proves recoverability, not live-claim preservation. |
| M14R-03 | A7; closeout checker instruction | Separate the approved correction delta from mechanical compaction. Compare compaction against the corrected intermediate baseline; do not require stale statuses to survive in live text. |
| M14R-04 | A4 | Apply by profile and function, including live technical appendices. Keep current assumptions, negative constraints and genuinely used older source pins. No compulsory migration of live claims into history. |
| M14R-05 | Closeout S-1/S-2/E-1/E-2/§5/§8 | Replace older contrary instructions at their own locations. Do not add another overlay leaving both instructions active. |
| M14R-06 | A2/A3/A5/A6/A9/A11; v1.3 §6.1; integration | Reconcile the inherited 800-line rule with D2; preserve consistency safeguards; define evidence shorthand; clarify nonblocking metrics, ordinary adoption and pilot authorization. |

### Why A7 needs revision

A hypothetical theorem block can retain its RID, THM tag and displayed equation while losing the prose sentence that restricts it to a selected model and local domain. Every listed token check can still pass; the removed sentence is necessarily present in the predecessor; no new words need be added. The resulting statement is nevertheless broader. This is a counterexample to the sufficiency of the proposed checks, not a finding against an RTG theorem.

Conversely, legitimate deduplication changes occurrence counts and section order. A checker must preserve distinct, qualified records and valid references, not require every duplicate occurrence or global tag sequence to survive.

## 3. Replacement A7 — §13.6 Compaction release

A **compaction change** performs layout, deduplication, navigation and history relocation without changing scientific content. It requires no new scientific review when the mechanical-preservation checks below pass. Passing these checks establishes editorial eligibility only; owner/PI adoption and immutable release identity remain governed by §13.1. Unchanged scientific certificates are not rerun solely for compaction.

Use a source-to-destination movement map. For each affected block record its source locator/hash, destination locator/hash, and operation: retain, move, replace an exact duplicate by a pointer, extract an identical standard clause, archive superseded history, or apply an independently approved correction. Unnumbered blocks use version/section/span locators; the checker does not invent scientific RIDs.

The checker verifies:

1. **Qualified content preservation.** Every distinct live claim remains at its designated live home, together with its statement, status, assumptions, quantifiers, domain, conventions, clock/order, dependencies, guards and evidence/proof references. These may remain inline or resolve through an explicitly mapped, unchanged clause. Formula and tag checks are per claim, not global set membership. A live result cannot be removed to Appendix B merely to satisfy a token-presence test.
2. **Mechanical scope.** Protected scientific text is unchanged, except for declared purely presentational transformations and exact reference substitution. Every otherwise changed scientific passage belongs to the separately approved correction delta. New navigation/status summaries are mapped to their authoritative records; the checker does not certify arbitrary paraphrase as semantically equivalent. An unexplained substantive edit requires scoped review of that edit only.
3. **Removal accounting.** Each removed passage maps either to the surviving identical qualified record, or to an identified historical source with exact location and retrievable immutable bytes. A copy in the predecessor is sufficient for historical recovery only when that predecessor is archived and specifically referenced. It is not sufficient to justify removing a current obligation, assumption or result.
4. **Integrity.** RIDs, applicable OPEN states, anchors, imports, proof/evidence locators and clause references resolve after moves. Existing unavailable artifacts remain explicitly unavailable; relocation does not fabricate their recovery. Broken links introduced by the move fail the check. Record parser limitations rather than treating unparsed content as absent or preserved.
5. **Presentation.** Check the current-only header, immediate-predecessor identity, one current footer, and the required current-state/history separation using the document's declared profile.

A mixed release may combine scientific/interface corrections and compaction. Record the corrected intermediate baseline and its hash, then check the layout delta against that baseline. It is a build stage, not another adopted release. The scientific/interface delta receives only the review required by its content; the compaction delta receives the mechanical checks above. A stale summary correction is identified as a correction, not disguised as compression. Report which part was checked and which was not.

The checker does not prove mathematical truth or semantic equivalence of unrestricted natural-language rewrites (§12.4).

## 4. Replacement A8 — §13.7 History file

Each study maintains one logical cumulative history file, `<STUDY>_HISTORY.md`, **in the archive**, outside the active project-document set. It holds retired version-history entries and superseded prose not needed for current use; it is not a second current-state ledger. Its logical filename has no version number and it supersedes no document.

Entries are append-only. Corrections are appended as dated notes; previously archived entries are not silently edited. At every release that changes or cites this history, retain the exact referenced bytes in an immutable release package or immutable repository revision. Record the archive locator and content hash in the release manifest. The same logical filename may occur in successive frozen packages; this does not create separate history-owner documents or a history supersession chain.

Appendix A gives a short archive pointer and the frozen reference needed to recover the cited history. Subsequent appends must not invalidate an older release's ability to retrieve its pinned bytes. The archive must preserve the immutable adopted DSNs as well.

The DSN header names only the immediately preceding adopted edition and its hash. This removes expanding lineage lists from headers; it does not eliminate traceable predecessor relationships. No historical file is automatically loaded as current scientific context.

## 5. Remaining amendment integration edits

### Decision line and A2

Replace D4 with: **“History files are kept in the archive, outside the active project-document set; each study has one logical cumulative history file and no history-file supersession series.”**

In A2, use “immediately preceding adopted edition”; preserve “none — first adoption” where applicable. Do not invent a hash for an unavailable historical source. Keep current adoption attribution and a release-record pointer; only earlier-round narratives are removed.

### A3

Retain the proposed 200–400-word target and the declared-exception option above 500; these are not an absolute numerical cap. Also retain the v1.3 sentence inadvertently omitted by replacement:

> An inconsistency between the summary and detailed record must be reported and resolved, not settled by whichever location sounds stronger.

### A4

Insert the following scope paragraph before the numbered rules:

> “Live” is functional, not determined solely by section number: it includes current scientific appendices and the corresponding sections of nonstandard profiles (§0.5). A historical/legacy study's current assessment of historical evidence remains live content. Operative assumptions, negative constraints, proof limitations, source access and current adoption scope are not obsolete merely because their evidence or origin is old.

In S2, replace “one line in Appendix A” by “one compact change entry in Appendix A, cross-referenced from Appendix B where §7 requires a scientific correction record.” This records the change; it need not reproduce all superseded prose in Appendix A.

In S5, keep the full claim at one home but allow short accurate readouts with load-bearing qualifications. An OPEN registry record retains its question, residual obligations and closure criteria under §5; it is not reduced to a status-only pointer.

In S7, clarify that “one current pin per reference” is **per claim/use**, not one imposed edition per source document. Different claim-level uses may retain different actual editions. The latest companion edition and the actual proof-source pin are distinct fields.

In S6, preserve §2's first-use guard callout and later pointer pattern. A clause key must resolve in the supplied document/package and remain attached to every governed use. Quantifiers, model/domain restrictions and distinct evidence states are not deleted as generic disclaimers.

### A5

Use a frozen archive pointer under §13.7. Long draft-round material may be moved into a release-record supplement. Do not overwrite a previously frozen release record: add a pinned supplement/addendum or include a preserved copy in the new release package. Appendix B retains required scientific correction/rejection records and currently operative negative constraints.

### A6

Explicitly define the two added shorthand states:

- `EV-SRC-REPORTED`: attributed source or prior-executor report, not independently established by the present review.
- `EV-NOT-RERUN`: the named computation was not executed in the stated review; this neither retracts a prior run nor contradicts source inspection or hash verification.

Keys retain the claim/artifact, reviewer or executor, date/review context and verification extent required by §12. A key is not a blanket verification flag.

### A9 and the inherited §6.1 size rule

The amendment currently leaves v1.3 §6.1 unchanged: “The core should not exceed 800 lines,” with an exception procedure. D2 requires reconciling this existing rule, not merely adding a contradictory no-budget paragraph later in the document. Replace that paragraph with:

> The orientation core has no fixed line-count budget. Report its size under §13.8. Move historical addenda, complete proofs, closed-module detail and raw tables to their proper locations when they obscure orientation; never remove assumptions to reduce a metric. The core boundaries, marker and profile map remain required.

Add to A9: “Metrics and near-duplicate flags are advisory; they do not automatically delete text or block release because of size. Required provenance and integrity checks remain separate. When no new RID is added, growth per new RID is reported as N/A. The report states its counting method.”

A3's expressly retained orientation target/profile-exception mechanism is distinct from an absolute size cap: exceeding 500 words alone is not a failed size gate. Record the exception when that option is used. If the PI instead removes this documentation threshold too, that is an explicit A3/E-1 policy change, not an inference from A9.

### A10 and A11

Apply wording consistently to existing examples and rules, not only new rows. In particular, the existing §11 changelog anti-pattern should point to compact Appendix A plus archived detail, not imply that full history belongs in the live Appendix A.

A11 applies after Methodology adoption, or through a separately recorded, scoped PI pilot authorization; citing a DRAFT does not adopt v1.4 across the corpus. Existing documents retain their declared governing edition until migration, including older editions. No extra DYAD release is required. Full v1.4 publication still requires its own recorded acceptance. The release record must identify all substantive governance changes, not just A1/A5; no additional scientific RID is needed for these administrative edits.

## 6. Closeout v1.2: edits at the points of use

| Location | Replacement instruction |
|---|---|
| §2 S-1, §6.14 row | Replace superseded wording in place. Archive the prior wording; retain only the current coefficient-verification and OPEN 21 pointers. Preserve the distinction between exact coefficient equality and file-byte identity. |
| §2 S-1 acceptance search | Check live assertions by profile. Explicit historical quotations in Appendix B are not contradictory current statuses. |
| §2 S-2 N11 | The live recipient row records the current adopted use and its evidence. Preserve the earlier v0.3.21 receipt/reference-only event in the archived notice history, with a pointer; do not erase or fabricate a receipt. |
| §2 E-1 footer | The new DSN has one current-version footer. The v6.4.20 r2→final comparison and P1 retagging explanation belong in their identified release records/addenda, not as inherited footer prose in v6.4.21. |
| §2 E-2; §5 completion | E-1 requires compact orientation or a declared profile exception, not a generic deferral. The scheduled archive move is an executed pilot deliverable; if uncompleted, report the pilot incomplete rather than automatically closed by a reason. Research Tier C remains nonblocking. |
| §8 history location | `DYAD_HISTORY.md` is archived under the revised A8, not kept in the active project set. |
| §8 checker | Use the revised A7 and the corrected intermediate baseline. Do not compare old stale status lines to the final live text as an invariant. |

## 7. Replacement closeout §8 — Pilot implementation

The one target release, DYAD v6.4.21, combines the established closeout errata with a mechanically checked compaction. No separate compaction release or full scientific re-audit is introduced.

Use two reproducible build stages within the same target:

`adopted v6.4.20 -> scoped correction baseline -> compacted v6.4.21 candidate`.

Record the intermediate hash. Review the first delta against S-1–S-6 and the other accepted closeout decisions; check the second delta under Methodology amendment A7 as revised by this review. An intermediate artifact is not an adopted version. New substantive claims, including optional Tier C results, cannot enter through the compaction stage.

Live records contain current status and valid claim-specific pins, with no stacked historical overlays. Preserve full qualified claim contracts and current negative constraints. Put superseded prose and older notice states in the archive; Appendix A gives concise change summaries and pointers, and Appendix B records scientific corrections when required.

Keep one current header/footer, with *Supersedes* identifying v6.4.20 and its hash. Meet E-1 through a compact §1 or its declared profile exception. Relocate long draft/review records into an immutable release-record supplement and older history into archived `DYAD_HISTORY.md`, retaining exact frozen references. Do not edit earlier frozen release records in place.

Attach the informational size report and the mechanical preservation report. A successful checker does not itself authorize publication. The final owner/PI adoption and successor hash are recorded normally; notices and installation read-back remain separate from other streams' subsequent adopted use.

The pilot cites the adopted Methodology edition or an explicit scoped pilot authorization, not a draft falsely labelled adopted. Unchanged mathematics and its previously accepted certificates are not reopened by the pilot.

## 8. Tooling boundary

`dsn_lint.py`: informational size/growth/duplication report with documented counting, no numerical size gate.

`check_compaction.py`: mechanical preservation against the movement map and the correct baseline; no unqualified claim of semantic verification. Missing assumptions, changed claim associations, unexplained status changes, dangling moved evidence pointers, and unavailable historical destinations must not silently PASS.

These scripts are specified here, not implemented or executed. Implementations should include small negative controls for those failure modes; no new scientific campaign is required. No source DSN, amendment input, closeout input or archived history was modified in this review.
