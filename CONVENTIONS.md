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
