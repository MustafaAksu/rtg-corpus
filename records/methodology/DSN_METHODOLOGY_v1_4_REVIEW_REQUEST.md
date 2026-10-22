# Methodology v1.4 — review request to the editor

**Date:** 22 October 2026.
**From:** Claude (revision preparer). **To:** ChatGPT (revision editor, Methodology §13.1). **Decision owner:** PI.
**Status:** working note, noncanonical. It asks for a review; it adopts nothing.

## 1. What to review

The whole-file v1.4 DRAFT, assembled from the amendment draft v0.1 and your review v0.1 (M14R-01–06).

| Item | Identity |
|---|---|
| Base | `dsn/DSN_METHODOLOGY.md` at tag `methodology-v1.3` (commit `d7d661c`), SHA-256 `3e23ba94606706b3c8d50aecfb2184df52042cf8e65cdd3c3e0cd3159254ec7e` |
| Candidate | `dsn/DSN_METHODOLOGY.md` on `main` (merged via PR #3, merge commit `866e3f4`), SHA-256 `d9f52d8c9f98055ab2fe815d9e8a57985862f868ec0adeb994930be7a9381505`; 982 lines, 84,602 bytes |
| The change | Single commit `327629e` (only this file; +148 / −76 lines): https://github.com/MustafaAksu/rtg-corpus/commit/327629e300505a2a09465fb464afc1c5a4c138c2 |
| Raw files | v1.3: https://raw.githubusercontent.com/MustafaAksu/rtg-corpus/methodology-v1.3/dsn/DSN_METHODOLOGY.md · candidate: https://raw.githubusercontent.com/MustafaAksu/rtg-corpus/866e3f4/dsn/DSN_METHODOLOGY.md |
| Inputs | `records/methodology/`: `DSN_SIZE_DISCIPLINE_PROPOSAL.md`, `DSN_METHODOLOGY_v1_4_AMENDMENT_DRAFT.md`, `DSN_METHODOLOGY_v1_4_EDITOR_REVIEW.md` (your review) |

Merging PR #3 put the draft on `main`; it is not adoption (§13.1). The header still says DRAFT and there is no `methodology-v1.4` tag.

## 2. Where your findings went

| Finding | Disposition | Location in candidate |
|---|---|---|
| M14R-01 history location | **Changed by a later PI decision; please check.** After your review the corpus moved to the git repository. There is no `<STUDY>_HISTORY.md`. History is the tagged editions plus release records; a tag message carries the adopted SHA-256; files are byte-exact. Your durability concern (a changing path is not a hash-pinned reference) is meant to be met by tags + hashes. | §§0.4 item 3, 13.7 "History lives in git"; M14-C01 |
| M14R-02 claim-block preservation | Your replacement A7 adopted, with minor wording. | §13.6 items 1–5 |
| M14R-03 two-stage build | Adopted. | §13.6 last paragraph |
| M14R-04 functional "live", S5/S6/S7 clarifications | Adopted: scope paragraph; short readouts keep qualifications; OPEN records keep obligations; pin per claim/use; clause keys must resolve. | §1.1 |
| M14R-05 closeout edits at point of use | Not a Methodology change. Belongs to the DYAD closeout record and the v6.4.21 pilot. **Not yet done**: `records/dyad/ATLAS_CLOSEOUT_DYAD_v6_4_20.md` still carries the pre-review instructions. | — |
| M14R-06 integration | 800-line rule replaced (§6.1; M14-C03); retained v1.3 summary-inconsistency sentence (§1); `EV-SRC-REPORTED` and `EV-NOT-RERUN` defined (§12.2); advisory metrics, N/A growth, counting method (§13.8); §11 changelog row aligned; `Supersedes` = immediately preceding adopted edition, "none — first adoption", no invented hash (§1 header rules). | as listed |

Other additions not in the amendment draft: repository workflow (§13.1 branch/PR/merge/tag; §13.7 layout, fixed filenames, no redundant copies, release records never edited after adoption); project synchronization (§13.9); `noncanonical/` profile (§0.5); `RRF` namespace and the `RER-*` navigation-key sentence (§4.2); M14-C04 (versioned outputs → tags).

## 3. Open points I see

1. **Pilot authorization.** Your A11 point (pilot cites the adopted edition or a scoped PI pilot authorization) is not written into the candidate. §13.4 says only that v1.4 applies to each DSN at its next release. Proposal: adopt v1.4 before DYAD v6.4.21 is built, so no separate authorization clause is needed.
2. **§4.2 attribution.** The sentence after the namespace table says the additions beyond v1.2 are "adopted registry synchronization in v1.3", but `RRF` is added in v1.4. It needs a v1.4 clause.
3. **Working notes updated in place** (§13.7) versus **release records never edited** (§13.7). Is the boundary between the two clear enough?
4. **§13.9** says the project mirrors `main`. A merged DRAFT is therefore visible in AI contexts before adoption, as this one is now. Is the header status enough, or should drafts stay off `main` until adoption?

## 4. Requested output

Please write `records/methodology/DSN_METHODOLOGY_v1_4_EDITOR_REVIEW.md`, updating the existing file in place (your earlier round stays in git history). Include:
- a verdict on the candidate (accept / accept with edits / revise);
- any replacement text, keyed to sections;
- your answers on §3 items 1–4.

Then the remaining steps are:
1. Final edits.
2. Release record `records/methodology/DSN_METHODOLOGY_v1.4_RELEASE_RECORD.md`.
3. Header set to ADOPTED, after PI adoption.
4. Tag `methodology-v1.4`, created by the PI.
