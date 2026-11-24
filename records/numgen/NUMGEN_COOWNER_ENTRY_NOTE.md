# Note to the Number Genesis co-owners — current state and entry route

**Date:** 24 November 2026. Earlier version: 26 October 2026, in git history.
**From:** the NUMGEN co-owner session (Claude).
**Status:** [SESSION] working note. It is operational context only: not scientific authority, not an approval, and not recovered memory of earlier chats.

**Entry route** (Programme project instructions):
1. Read `CONVENTIONS.md` and this note.
2. Check yourself: the adopted tag and its release record, the open PRs, and `pipes/NUMGEN/`.

## 1. How we work

The full rules are in `CONVENTIONS.md` and Methodology v1.4 (`dsn/DSN_METHODOLOGY.md`, tag `methodology-v1.4`).

**Source.** The source is `dsn/RTG_NUMBER_GENESIS_DSN.md`. The governing edition is the latest `numgen-v…` tag together with its release record. The live file holds the current state only. Appendix A has one compact entry per edition; older history is at the tags.

**Release route.**
1. Work on a branch (`claude/*` for this session) and open a PR.
2. The other co-owner and the atlas owner review the change.
3. Write the release record.
4. The PI adopts.
5. The PI makes a merge commit (never squash) and the annotated tag.

**Stages.** One content stage suffices when the layout does not change. Layout compaction is a separate stage 2, checked by `tools/check_compaction.py`.

**Evidence and identifiers.**
- Evidence goes in `evidence/numgen/`.
- Held records are on the branch `upload/numgen-records`, now merged; see `records/numgen/NUMGEN_UPLOAD_HASH_CHECK_20261026.md`.
- Never invent hashes, RIDs or approvals.

**Cross-stream items** (`pipes/README.md`):
- Inbox `pipes/NUMGEN/`.
- The receiver sets `state` and `disposition`.
- A notice never creates adopted use.
- Validator: `python3 -I tools/pipes_index.py --check`.

## 2. Current state

| Item | Value |
|---|---|
| Governing edition | v1.21, tag `numgen-v1.21`, SHA-256 `4805760d683bb3abddfdaab4737f6bb75beed392906bd4c54d8ae79245f15701`; release record `records/numgen/NUMGEN_v1_21_RELEASE_RECORD.md` |
| In progress | v1.22, one content stage (receiving and synchronization); DRAFT on branch `claude/numgen-v1.22`; release record `records/numgen/NUMGEN_v1_22_RELEASE_RECORD.md` (DRAFT) |
| Work list for v1.22 | `records/numgen/ATLAS_ADVISORY_NUMGEN_SYNC_20261123.md` (rev. 2); owner disposition `records/numgen/NUMGEN_OWNER_DISPOSITION_SYNC_20261123_CLAUDE_20261124.md` (PR #374) |
| S1 evidence | `records/numgen/NUMGEN_v1_22_S1_P2_REANNOTATION.md` (PR #375): P2 re-annotation of 158 witnesses under TDRG-DEF-ORIENT |
| Inbox | eleven notices dispositioned in `records/numgen/NUMGEN_v1_22_RECEIVING_LEDGER.md` (on the v1.22 branch); to be closed after the tag |
| Outbound | the four items of 26 Oct 2026 are closed by their receivers |

## 3. Open scientific frontier (unchanged by v1.22)

- **C7C-M.** The target is a non-degenerate composable three-stream witness and full-interface typed WD-DOM (OPEN).
  - M-4 stays on HOLD pending approval of a design/preregistration for the missing non-degenerate composable-chain witness (middle-interface and outer-pair admissibility). The P2 policy is answered. All 158 Census-1 TDR-G records are `(SWAP, P3)`; the two dyad records are separate. Finding the witness is the target, not a prerequisite to launching a properly authorized search.
  - Census-1 stays INCONCLUSIVE / INCONCLUSIVE.
  - A new evidence universe needs its own preregistration (Census-2).
- **C7B global breadth** is OPEN. DISC-3 is deferred.
- **N-4, N-6 and full NG-8** are OPEN.
- **φ* vs `C_D^ext`** stays OPEN as a comparison. No identification is claimed.

## 4. Next checkpoint

PR #377 round 2: the ChatGPT co-owner applied the bounded R1–R4 repairs requested in review `6041922508`. Rebuild/check records and the previous candidate identity are in the draft release record. Read the receiving inbox again before the final release record; native builder/checker rerun and Atlas row check precede PI adoption. No campaign or merge is authorized by this checkpoint.

## 5. Not asked

- No rerun of the N-5, C7A or DISC campaigns.
- No change to the C7C algebra or Census-1.
- No ALG→THM promotion by header edit.
- No new compaction or general regrading.
- No action on other streams' inboxes.

*END OF NOTE.*
