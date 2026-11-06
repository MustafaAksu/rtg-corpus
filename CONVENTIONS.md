# Conventions — how a stream works in `rtg-corpus`

Practical rules for stream owners, co-owners and reviewers. The governing text is the DSN Methodology v1.4 (`dsn/DSN_METHODOLOGY.md`, tag `methodology-v1.4`); section numbers below refer to it. Where this page and the Methodology differ, the Methodology governs.

## 1. Where things are

| What | Where | Rule |
|---|---|---|
| Canonical DSNs, Methodology, Programme | `dsn/` | one file per study, fixed filename, no version in the name |
| Noncanonical registries and studies (RER, ER-2B, FMS) | `noncanonical/` | same |
| Release records, reviews, advisory/closeout notes, notices, session records | `records/<study>/` | working notes keep one fixed path and change by commit; release records are frozen at adoption |
| Scripts, certificates, outputs, evidence packages | `evidence/<study>/` (`scripts/` for scripts, `<version>/` for small per-release outputs) | stored once; frozen external packages kept as received |
| Lint and checkers | `tools/` | `dsn_lint.py`, `check_compaction.py`, `test_check_compaction.py` |
| What is in the repository, verified hashes, governing editions | `BASELINE.md` | |

Study keys: `dyad`, `triad`, `gen`, `tdrg`, `recog`, `dzt`, `az`, `uvm`, `numgen`, `ofn`, `rrf`, `rer`, `er2b`, `fms`, `programme`, `methodology`, `legacy`, `prelegacy`, `atlas`.

## 2. Which edition governs

The governing edition of a study is its latest **adopted, tagged** release (`<study>-v<version>`) with its release record — not whatever is on `main`, and not a status header (§13.9). Earlier editions: `git show <study>-v<version>:dsn/<FILE>.md`. Files are byte-exact (`.gitattributes: * -text`), so the SHA-256 in the repository equals the one in the release record.

## 3. The live file (§1, §1.1)

- §§0–9 and live appendices state the **current** state only: no "kept as history", no dated overlays, no stacked footers.
- Change a status, pin or scope **in place**; record the change once, as one compact Appendix A entry (Appendix B where a scientific correction record is required).
- Header: one line per field; *Supersedes* = the immediately preceding adopted edition and its hash only; one footer.
- §1: 200–400 words, or a one-line profile exception in the header.
- Draft-round records, review verdicts and old→new line maps go to the release record, not Appendix A.
- Never remove an assumption, scope, grade, RID, OPEN obligation or evidence pointer to save space.

## 4. Making a release (§13.1, §13.6, §13.7)

1. **Branch.** Work on a branch (`claude/<topic>` for Claude sessions). Edit the fixed-name file in place. No versioned copies (`*_v6_4_21.md`, `*_DRAFT_r2.md`).
2. **Two stages when a release also compacts.** Stage 1: scientific or scope corrections, built by an assertion-gated script; record the intermediate hash. Stage 2: layout only, with a movement map, checked by `tools/check_compaction.py` against the intermediate. New claims never enter in stage 2.
3. **Checks.** `python tools/dsn_lint.py <file> --prev <previous file>` (informational size report; no gate). For a compaction: `python tools/check_compaction.py <intermediate> <candidate> <map> --regions <registry>` and `python tools/test_check_compaction.py …` (negative controls). A passing check authorizes nothing.
4. **Review.** Open a pull request. The receiving review is change-focused: it checks the diff, not unchanged science. Reviews go to `records/<study>/`.
5. **Adoption.** The PI/owner decision is recorded in `records/<study>/<STUDY>_v<version>_RELEASE_RECORD.md`, then a status-lines-only publication commit (header, Appendix A heading, footer) gives the final hash.
6. **Publication.** The PI merges with a merge commit (not squash) and creates the annotated tag `<study>-v<version>` on the server, with the hash in the tag message. `BASELINE.md` lists the new governing edition. Then "Sync now" in the Claude project.

Order: decision → release record → merge → tag. A merge, a tag or a passing check is not an adoption.

## 5. Evidence

- Every `[THM]`/`[ALG]` claim should be testable from the repository: its certificate script and output under `evidence/<study>/`, cited by path, command and hash. Where a file is not yet in the repository, the DSN says so; it is not described as recreated.
- Evidence states are cited by key (§12.2): `EV-SRC-READ`, `EV-SRC-REPORTED`, `EV-BYTES`, `EV-HASH`, `EV-CODE`, `EV-RUN`, `EV-NOT-RERUN`, `EV-INDEP`, `EV-COVER`.
- A numerical run at high precision is not an exact proof; say which one you have.

## 6. Who writes where

- Claude sessions push only to `claude/*` branches; ChatGPT writes to the branch it is asked to review.
- The PI merges into `main` and creates tags. Nobody force-pushes, moves a tag or rewrites published history.
- Files from outside (local scripts, session downloads) come in **unchanged** on an `upload/<topic>` branch; they are hash-checked and placed by a follow-up commit. Uploading directly to `main` bypasses that check.
- A session without repository access hands its files to the PI, who uploads them to an `upload/…` branch.

## 7. Notices

A notice records four separate states per recipient: sent, received, statement accepted, adopted use. Pending consumer decisions do not block the sender's release (§13.5).

**Pipes (pilot v0.1, PI decision 26 Oct 2026).** Cross-stream requests, offers, findings, questions and notices are filed as items in the receiving stream's inbox, `pipes/<STREAM>/` (schema, states and checkpoints: `pipes/README.md`; validation and index: `tools/pipes_index.py --check`). Nothing is routed through the PI: the receiving stream's co-owners read their inbox at the stated checkpoints (start of an owner pass, before a stage-1 freeze or release record, when their own work is blocked on an item) and decide autonomously. An item is only a request or offer; it carries no scientific authority — the producer stays owner, and adopted use is asserted solely by the receiver's Import Ledger row (by RID, at the producer edition) or release record. Filing an item is a queue event, not a notification; the item's `state` tracks the queue only. Of the four states above, *statement accepted* is the receiver's recorded verdict and *adopted use* is read solely from the receiver's Import Ledger row or release record — `closed` with verdict reject, defer or no action is not adopted use. A release record lists "what would be notified" by pointing at the items it filed.

## 8. Literature corpus (LIT)

*In force from the merge of the pull request that introduced it.*

**What it is.** External literature used by RTG is kept in the private repository `MustafaAksu/rtg-lit` ("LIT"; access: PI, Claude, ChatGPT). Its rules are in `rtg-lit/CONVENTIONS.md`. For each source it holds a bibliographic record with a hash, a transcription of the taken parts, a claim index with per-claim validation events, and cross-source inference records (`INF-…`). It also holds screening notes, a backlog and prior-art records.
- A transcription is co-owner-checked only where the source record says so. A `candidate` or `partial` source does not imply a checked transcription of the whole work.
- LIT's assessments, inferences and validation events are `[SESSION]`-level and noncanonical.
- A source's own statements keep their own status as the source's claims: a source's "Theorem" is the source's claim.
- A LIT event (`rederived`, `external_checked`, …) is not an RTG grade.

**Channel.** LIT and the streams exchange pipe items (`pipes/README.md`, service key `LIT`):
- LIT files `finding`/`offer`/`notice` items into `pipes/<STREAM>/`;
- streams file requests and reports of use into `pipes/LIT/`.

The receiver decides, as for any item. Before presenting a mathematical statement as new, a stream may request a prior-art check. If LIT finds the statement in the literature, RTG makes no novelty claim for it (PI decision, 30 Oct 2026).

**Disclosure.** `rtg-corpus` is public. A pipe item or DSN may name a source only if its LIT record says `disclosure: citable`. It never reproduces a source's full text or substantial excerpts, whatever the source's `copy` status. For any other source nothing is filed here, not even its LIT-ID: the notice stays in `rtg-lit/notices/<STREAM>/` and the PI relays it once disclosure is cleared.

**Citing a LIT-supplied result in a DSN.**
- **The DSN cites the work itself.** That is the published article, or a citable preprint (e.g. arXiv with version), by author, title, venue or repository identifier, DOI where one exists, and the source's own label. Never a LIT file.
- **Grade.** The importing stream grades the result itself, e.g. `[MATH]` for established background (Methodology §8.4 local alias) or source-reported if its proof was not checked.
- **Import Ledger.** The row uses the §4.3 format with the published citation in place of a source DSN:
  - `Source status:` the source's own claim status;
  - `Verification:` "LIT `<LIT-ID>@<version>:<label>`, rtg-lit `<commit>`: <events and their scope, e.g. external_checked/confirms via INF-008>; cited inputs not re-proved: <list>".

  The rtg-lit commit is for traceability only. LIT's checks inform the stream's grading; they do not replace it.

**Release records.** A release that uses a LIT-supplied result adds one line, `LIT dependencies: <LIT-ID>@<version>:<label>, …`, or `LIT dependencies: none`. The line lists **only** `citable` dependencies. A dependency that is `confidential` or `unknown` is never named in `rtg-corpus`, not even by its LIT-ID: it is recorded only in LIT's private records. The part of the release that depends on it is held back until the PI clears disclosure (`rtg-lit/CONVENTIONS.md` §9).

**Feedback.** When a stream uses, verifies or refutes a LIT result, it says so in a `to: LIT` item pointing to its record. LIT then records the corresponding event (`stream_used`, `stream_verified`, `issue`) on the source claim.

## 9. Co-owner session orientation — Atlas pilot (working protocol)

For the **Atlas pilot only**, maintain one current-state working note at `records/atlas/ATLAS_COOWNER_SESSION_ORIENTATION.md`, shared by the Atlas owner and independent co-owner/reviewer. This is a **SESSION** continuation aid, not the Atlas, a scientific owner source, a release record, a new claim grade, or an amendment to adopted Methodology v1.4. Study-wide expansion requires a separate Methodology review and PI decision.

**On session entry:** read that note, then independently verify the governing adopted tag/release record, `main`, live PRs and the relevant `pipes/ATLAS/` items; inspect the actual owner DSN for any consequential science. Report stale or unverified pointers. A working note never makes a session scientifically review-ready without the cited sources.

**Update checkpoints:** after a material PR/review, owner decision, release/tag, cross-stream blocker or change of next action—and proactively before a long work phase—not on every chat message. Update the fixed working file on a reviewable branch/PR; keep current status and the next 1–3 actions, remove stale history (Git retains it). Do not claim that private, uncommitted session work survived a context limit.

**Generalization proposal:** the separate, unadopted [Methodology v1.5 draft PR #189](https://github.com/MustafaAksu/rtg-corpus/pull/189) proposes a §6.4 rule based on this pilot. Until that draft is reviewed and adopted by the PI, `methodology-v1.4` governs; no future Methodology file is assumed to be on `main`.
