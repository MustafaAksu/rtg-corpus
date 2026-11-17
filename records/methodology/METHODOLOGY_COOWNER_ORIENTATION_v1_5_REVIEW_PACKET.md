# Methodology v1.5 — co-owner session orientation proposal and review packet

**Status:** [SESSION] DRAFT CHANGE PROPOSAL — not adopted. The governing Methodology remains `methodology-v1.4` until an explicit PI decision and the ordinary release procedure. This packet is a review request, not the release record.  
**Date:** 6 November 2026. **Proposer:** ChatGPT, RTG cross-stream documentation review.  
**Candidate:** `dsn/DSN_METHODOLOGY.md` on `chatgpt/methodology-v1.5-session-orientation`, header `DSN_METHODOLOGY_v1.5`, SHA-256 **`4f12daa89b140adc8e88825e5756b664b01181dc270a3a6ffc9599d7f622f559`**, **91,616 UTF-8 bytes**, 1,012 lines (including final newline).  
**Predecessor:** adopted `methodology-v1.4`, SHA-256 `cdacab5feb79161cd86313086065ca67313ef354e30ceaf205386cf2f3a0f2df`, **86,709 bytes**.  
**Pilot:** `records/atlas/ATLAS_COOWNER_SESSION_ORIENTATION.md` and Atlas-only `CONVENTIONS.md` §9 on [PR #188](https://github.com/MustafaAksu/rtg-corpus/pull/188). The pilot is a working note and does not amend adopted Methodology.

## 1. Why an additional record is justified

**[OWNER: Methodology v1.4 §§6.1–6.3]** The AI Context Core tells a new AI what scoped scientific results, active problems and guards exist. It explicitly is *not guaranteed sufficient to reconstruct a proof or run an experiment*. **[OWNER: Methodology v1.4 §§13.7, 13.9]** Git tags, working-note records, owner release records and active import pins preserve the adopted research state and provenance. Existing `*_COOWNER_ENTRY_NOTE*` files for GEN, RECOG, OFN, TRIAD and TDR-G convey **dated, round-specific** coordination, but do not constitute a continuously updated starting point for a session that unexpectedly exhausts its context.

**[SESSION]** The missing capability is an operational index: *which PR/review/pipe checkpoint was last committed, what is actually waiting for whom, and what is safe to do next*. Trying to recover this from a past chat, inferring from `main` alone, or copying another long scientific summary risks stale roles and false adoption claims. A single compact record **per co-owned study** is more maintainable than one note per chat session. Keep distinct co-owner lanes within that record.

## 2. Draft rule and scope

The candidate makes exactly one new policy, `§6.4 Co-owner Session Orientation — Operational Continuity`, and two small repository/synchronization cross-references in §§13.7 and 13.9. It also updates the v1.5 draft header, an Appendix A *draft* entry and the footer. **No v1.4 claim/status/grade/evidence/import rule, Appendix B body or scientific owner is modified.**

The proposed §6.4 requires the note to record: (i) roles and PI decisions; (ii) latest **verified adopted** tag, target, release record, SHA if checked and last `main` identity; (iii) active branches/PRs and durable checkpoint, with incomplete work clearly marked; (iv) pipe states and blockers; (v) next 1–3 eligible actions with responsibility and acceptance criteria, or an explicit idle state; (vi) source-reading order, actual verification scope and staleness. New sessions re-check live sources before claiming readiness. The note has `[SESSION]` authority, never a new scientific claim/RID and never an assumed recovery of private reasoning.

**Update cadence:** after material work milestones (PR, review, reconciliation, adoption, tag, blocker) or before a lengthy campaign—not every chat message, and not a fixed timer. Update the same fixed-path note on a branch/PR; Git retains prior revisions. This design reduces repeated large handover packages and does not require a new DSN edition to update an orientation.

**Privacy boundary:** `rtg-corpus` is public. LIT's private/internal source identifiers and confidential research do not enter the public orientation. If a service lives in a different repository, its record belongs there under that repository's disclosure rules.

## 3. Changed-block inventory and verification

Exactly **12** text transformations against `methodology-v1.4`: title; date; scope; DRAFT status; predecessor identity; revision attribution; status summary; new §6.4; §13.7 link to working records; §13.9 replacement-session revalidation; Appendix A draft entry; footer.

**[EV-INDEP]** The proposer fetched the tagged predecessor and applied 12 asserted, exact-once replacements. SHA-256 was computed from the fetched UTF-8 bytes using a self-tested implementation (standard `abc` SHA-256 known-answer check passed). The resulting GitHub candidate was then fetched and SHA-256 recomputed. The historical Appendix B body is unchanged; only the terminal footer changes. Section profiles, imports, evidence definitions, scientific grades, RID grammar and PI authority are untouched.

**[EV-NOT-RUN]** The repository's Python lint suite and a real brand-new-session acceptance trial have not been run by this proposer. The editor/reviewer should perform the focused checks below; do not present the draft as fully validated by a script.

## 4. Acceptance criteria — one bounded methodology pass

1. **Source/authority:** `methodology-v1.4` still governs; the candidate explicitly says DRAFT. Branch/PR and release-record boundaries match §13.1. No merge, tag or adoption is inferred from this draft.
2. **Scientific noninterference:** old §§0–6.3, 7–12, 13.1–13.6, 13.8, Appendix B (except the footer) remain semantically and mechanically unchanged; no scientific claim, grade, RID, cross-stream acceptance or evidence state is changed by an orientation.
3. **Orientation schema:** the pilot's file is easy for a replacement session to locate, ties each field to a real source, and distinguishes `main` from governing adopted tag. Missing or stale state is exposed rather than guessed; both co-owner lanes have independent actions and no competing authority.
4. **Pilot test 1 — clean start:** have a fresh Atlas co-owner session read **only** the orientation + verified repository sources and produce its verified manifest, active PR/inbox status, scoped blockers and next safe action. It must not claim it inherited the previous session's private reasoning.
5. **Pilot test 2 — stale note:** after a test PR/inbox change, the replacement session must detect that the orientation's `main`/queue state is outdated and prefer the actual tagged/PR records.
6. **Pilot test 3 — authority:** a fake claim/grade in the note must be rejected when it conflicts with the owner DSN; an uncommitted script must be reported as unavailable.
7. **Operational maintenance:** a co-owner updates the working note in one minimal PR after a material checkpoint; unrelated DSN release artifacts, scientific campaigns and historical frozen records must not be rewritten.
8. **Editorial:** one compact review of the candidate's actual changed blocks, a reproducible SHA-256 and source comparison; `tools/dsn_lint.py` informational output may be attached. Do not initiate a multi-edition release loop for tiny wording fixes.

## 5. Proposed project-instruction addition (not applied to account settings)

A minimal, two-sentence addition is sufficient; the existing RTG standing protocol already governs scientific claims, ownership and releases:

> Before starting substantive co-owner work, read `records/<study>/<STUDY>_COOWNER_SESSION_ORIENTATION.md` if present, then independently verify the latest adopted owner tag, release record, active PRs, incoming pipe states and actual owner sections. After a material checkpoint, update that single working note through a reviewable Git commit; the note is [SESSION] operational context, never scientific authority, approval or recovered private memory.

No project-settings change has been executed. The PI decides whether this becomes part of the project instructions after the pilot.

## 6. Next action and decision boundary

**Pilot PR #188:** Atlas owner and one independent replacement-session reviewer assess the usability of `records/atlas/ATLAS_COOWNER_SESSION_ORIENTATION.md`; merge requires PI authorization for project workflow change.

**This methodology candidate:** request independent co-owner/editor review of §6.4 and affected §13 links. The PI then decides whether to adopt a v1.5 governance edition. Only after adoption should a release record, publication transform/manifest update, merge commit and annotated `methodology-v1.5` tag be prepared. The default extension of the rule to other study records should follow adoption, preferably on each stream's next natural owner pass; do not require all streams to open new scientific DSN editions solely for an orientation note.

**Not done:** no canonical Methodology v1.4 edit on `main`; no Atlas science change, no owner theorem change, no certificate or notice-status change, no publication, and no background automation.
