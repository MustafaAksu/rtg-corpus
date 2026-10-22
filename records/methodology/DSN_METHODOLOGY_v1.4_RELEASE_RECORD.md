# DSN Methodology v1.4 — release record

**Study:** Methodology (governance reference). **Edition:** v1.4. **Status:** ADOPTED.
**Adoption:** PI (Mustafa), 22 October 2026, 17:53 +03:00, in the Claude session that prepared the edition (https://claude.ai/code/session_01EfNnfvRHBdjEtEr5z2sbfW). Statement: "I approve the adoption of new version."
**Adopted file:** `dsn/DSN_METHODOLOGY.md`, SHA-256 `cdacab5feb79161cd86313086065ca67313ef354e30ceaf205386cf2f3a0f2df`, 983 lines, 86,709 bytes.
**Predecessor:** tag `methodology-v1.3` (commit `d7d661c`), SHA-256 `3e23ba94606706b3c8d50aecfb2184df52042cf8e65cdd3c3e0cd3159254ec7e`.
**Tag:** `methodology-v1.4`, annotated, created by the PI on the `main` commit carrying the hash above; tag message carries the hash.
**Prepared by:** Claude. **Revision editor:** ChatGPT.

This record is frozen on adoption (§13.7). Later facts go in a dated addendum.

## 1. Build history

All on branch `claude/methodology-v1.4` and then `claude/m14-review-request`.

| Stage | Commit | File SHA-256 |
|---|---|---|
| Assembled draft (merged to `main` by PR #3 before adoption; see §5) | `327629e` | `d9f52d8c9f98055ab2fe815d9e8a57985862f868ec0adeb994930be7a9381505` |
| Editor-review edits applied | `a9c83e8` | `b87ae3bc5c2b22fee0154e00d2566a91d8a2aea377799e43a76c5bec37be19c4` |
| Adopted (status lines only: header, Appendix A heading, Appendix B key sentence, footer) | this commit | `cdacab5feb79161cd86313086065ca67313ef354e30ceaf205386cf2f3a0f2df` |

## 2. Inputs relied on (exact revisions)

| Record | Commit | SHA-256 |
|---|---|---|
| `records/methodology/DSN_SIZE_DISCIPLINE_PROPOSAL.md` | `87a9045` | `6dff3bec94c9e55a7d35f9cdd0f2d3428fbeafc673f9c6d6d1257c7d33677984` |
| `records/methodology/DSN_METHODOLOGY_v1_4_AMENDMENT_DRAFT.md` | `87a9045` | `45d4fa81cb385d7d4d79be7309e7835a280928052e25bcd584f4c57769b56188` |
| `records/methodology/DSN_METHODOLOGY_v1_4_EDITOR_REVIEW.md`, round 1 (findings M14R-01–06) | `87a9045` | see that commit |
| `records/methodology/DSN_METHODOLOGY_v1_4_REVIEW_REQUEST.md` | `da3a2f1` | `6111f9e299ce389548c909f9453b20577597ac0eb254049a3468c65c8370ec44` |
| `records/methodology/DSN_METHODOLOGY_v1_4_EDITOR_REVIEW.md`, round 2 (ACCEPT WITH EDITS) | `799e344` | `821a9cd5fcf447213eda4bf9d4c71f9630859e0ab47af4dc2b691bb70861e6b1` |

PI decisions D1–D5 (22 Oct 2026) as recorded in the amendment draft. D4 (history location) was later replaced by the repository decision: history is the tagged editions and release records (§13.7); the editor accepted this in round 2.

## 3. Changes

Governance only. No scientific result, RID, grade or OPEN status in any DSN changes.

- **§§0.4, 1, 1.1** live-file rule; current-only header with immediate predecessor and hash; compact Appendix A; §1 exception declared in the header.
- **§§6.1, 13.8** no fixed size budgets; advisory size reporting.
- **§12.2** evidence-state keys `EV-*`.
- **§13.6** compaction change: per-claim-block preservation, movement map, two-stage build.
- **§§13.1, 13.4, 13.7, 13.9** repository workflow and custody (`rtg-corpus`): fixed filenames, tags, decision before merge, drafts on branches, adoption before use, working-note commits pinned, tags never rewritten, no redundant copies, governing edition = adopted tag.
- **§0.5** noncanonical registry/study profile. **§4.2** `RRF` namespace (v1.4).
- **§11** six anti-patterns; changelog row aligned.
- **Appendix B** correction keys M14-C01 (location of provenance), M14-C02 (Appendix A content), M14-C03 (orientation-core line budget), M14-C04 (versioned outputs).

## 4. Checks

| Check | Extent | Result |
|---|---|---|
| Scope of change | `git diff --stat methodology-v1.3` over `dsn/` and `noncanonical/` | Only `dsn/DSN_METHODOLOGY.md` changed (+149 / −76 lines) |
| Edits applied | Each scripted replacement asserted a unique match | PASS |
| Header (§1 rules) | Status current only; *Supersedes* = v1.3 with hash and tag; one footer | PASS, by inspection |
| Editor review | Round 1 findings M14R-01–06; round 2 required edits (§4.2, §13.9) and optional edits (§§13.1, 13.4, 13.7) | All applied; M14R-05 belongs to the DYAD closeout, open there |
| Hash | `sha256sum` of the adopted file | `cdacab5feb79161cd86313086065ca67313ef354e30ceaf205386cf2f3a0f2df` (EV-HASH) |

Not done: `tools/dsn_lint.py` and `check_compaction.py` are specified, not implemented. The editor did not recompute hashes (EV-SRC-REPORTED for those in the request).

## 5. Size report (§13.8; manual count)

| Metric | v1.3 | v1.4 |
|---|---:|---:|
| Bytes | 73,372 | 86,709 (+18.2%) |
| Lines | 910 | 983 |
| Appendix A words (whitespace split) | 79 | 128 |
| New RIDs | — | N/A (governance only) |

## 6. Deviations and notes

- The draft was merged into `main` (PR #3) before adoption, contrary to the order now in §13.1. Between that merge and this adoption, `methodology-v1.3` governed; `BASELINE.md` recorded the divergence. No history was rewritten.
- Existing DSNs keep their declared governing edition until their next release (§13.4). First application: DYAD v6.4.21, together with the closeout errata and editor finding M14R-05.
