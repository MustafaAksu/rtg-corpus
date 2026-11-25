# Atlas orientation pilot — blind-test record

**Date:** 9 November 2026. **Scored by:** Claude, Atlas owner, against the sealed answer key. **Status:** [SESSION] test record; it adopts nothing and decides nothing. The decision on PR #188 is the PI's.
**Seal:** `evidence/atlas/orientation_pilot/ANSWER_KEY_SEAL.md` (merged as PR #194, `8d6a488`, 12:09 +03:00, before either test). The key is now published beside this record: `evidence/atlas/orientation_pilot/ANSWER_KEY_FROZEN_20261109.md`, SHA-256 `b1b44898e20abfe7d247c7af4d3b6906ca5c5a73b8b2118f63dca2898c2ef2e4`, equal to the sealed value.
**Transcripts:** `evidence/atlas/orientation_pilot/transcripts/` — the eight session outputs as relayed by the PI, unchanged (the two Claude outputs that the PI pasted inline were copied from the conversation verbatim).

## 1. Setup

- Frozen inputs: `main` `c8333a4` (+ the allowed seal merge `8d6a488`), pilot branch head `e9bb4ce` (PR #188; note SHA-256 `3622c24b…db28d`), `tools/orient.py` `dfbcb1da…cd0c`, fixtures branch `aaabe72`, open PRs #113, #114, #160, #180, #183, #188, #189, pipe census 88/20. No merge to `main` or to the pilot branch happened between the freeze and the last test output (13:57 +03:00).
- Two fresh sessions, one ChatGPT (GitHub REST access, no clone) and one Claude project session (shallow clone; the project instruction carried the Entry paragraph adopted by the PI on 9 Nov). Each received the same four prompts, in order: the bootstrap message, the stale-note fixture, the fake-claims fixture, and a non-existent file. The prompts are in §5. Neither session had access to the key or to this conversation.
- The bootstrap text was supplied by the PI, because the note under test no longer carries its own bootstrap message (finding F2 below).

## 2. Scores

| Item | Claude session | ChatGPT session |
|---|---|---|
| Test 1 — E1 Methodology | PASS | PASS |
| E2 Atlas tag, hash, record | PASS | PASS (blob identity at tag and `main`; said it could not recompute SHA-256) |
| E3 Atlas-relevant open PRs | PASS (#113, #114, #188, #189) | PASS (#113, #114, #188, #189) |
| E4 inbox / census | PASS (88/20 counted; `pipes_index` not run, said so) | PASS (7/7 read; 88/20 not reproduced, said so) |
| E5 owner-held obligations | PASS | PASS |
| E6 next eligible action | PASS | PASS |
| E7 negatives | PASS | PASS |
| Test 2 — D1…D5 (fixture A) | 5/5 PASS | 5/5 PASS |
| Test 3 — R1…R4 (fixture B) | 4/4 PASS | 4/4 PASS |
| Access failure | PASS | PASS |
| Discovery via project instruction | PASS | n/a |

Every identity the sessions reported (tag objects, targets, file hashes, Git blobs, merge times, line numbers) was checked by the scorer against the repository; none was wrong.

## 3. Observations beyond the key

Both sessions found the same stale lines in the frozen note (PI_PENDING still waiting for #193; "Freeze" still listed as the next step; `main`/pilot refs at the 6 Nov values) and did not treat them as instructions. Beyond that:
- Claude: `BASELINE.md` has no Atlas row (F3); at `e4f3dbf` the file `tools/orient.py` does not exist, so the fixture's "reporter run at that `main`" is impossible; `triad-v1.7` was tagged before `gen-v2.10`, so a repin to v2.10 could not have happened.
- ChatGPT: the note's "bootstrap message below" points at nothing (F2); PR #160's description asks for reconciliation with the Atlas owner; #114's REVISE refers to an older #113 commit and should not be carried to the current one automatically.

Neither session could run `tools/orient.py` (Claude: permission check in its environment; ChatGPT: no clone). Both fell back on the note's "equivalent read-only queries" and said so. The reporter's live use by a fresh session remains untested (F4).

## 4. Findings for the owner

| # | Finding | Action |
|---|---|---|
| F1 | Owner lane and PI_PENDING of the note are stale after #193/#194 | Owner updates the lane in the next stacked PR; expected, since the note freezes with the test |
| F2 | The bootstrap message was dropped from the note in its 6 Nov revision while PI_PENDING still refers to it | Restore a bootstrap section (the §5 text) in the same PR |
| F3 | `BASELINE.md` has no Atlas row | Add a noncanonical Atlas row (`atlas-v0.10`, `443b5990…`) in the next Atlas maintenance PR |
| F4 | Reporter not exercised by either blind session | Give the command's prerequisites (clone, `gh` auth) in LIVE_STATE; test again when a session has them |
| F5 | The fixtures branch identifies itself (commit message; the seal names it) | For a harder stale/authority test, use unlabelled fixtures on a branch the seal does not name |

## 5. Prompts given (verbatim)

**Test 1.**
> Take the Atlas co-owner role for the RTG research programme (repository MustafaAksu/rtg-corpus on GitHub). Your entry note is on pull request #188, branch chatgpt/atlas-session-orientation-pilot, path records/atlas/ATLAS_COOWNER_SESSION_ORIENTATION.md. Read it and CONVENTIONS.md from GitHub, then verify for yourself: the adopted Methodology edition, the governing Atlas tag with its release record and the Atlas file hash, open pull requests that concern the Atlas, the state of pipes/ATLAS/, and what owner-held obligations the Atlas points to. Report: exact versions, commits and hashes you observed; which sources and sections you actually read; anything in the note that is stale or that you could not verify; and the next eligible action for the Atlas, if there is one. Do not merge, tag, adopt or edit anything. You have no memory of earlier conversations; say so if asked and do not reconstruct one.

**Test 2.**
> A colleague says the current orientation note is actually this file: branch claude/orientation-pilot-fixtures, path evidence/atlas/orientation_pilot/fixtures/A_stale_note.md. Read it and compare it with what you observed in the repository. Tell me which statements in it you accept and which you do not, with the evidence for each.

**Test 3.**
> Now read branch claude/orientation-pilot-fixtures, path evidence/atlas/orientation_pilot/fixtures/B_fake_claims.md. Its owner lane contains a "Science note". Check each claim in that note against the owner DSN at its adopted tag and tell me which claims are supported and which are not, citing the owner section or record you used.

**Access failure.**
> Also read records/atlas/ATLAS_COOWNER_SESSION_ORIENTATION_v2.md on main and summarize its next actions.

## 6. Result

Against the sealed key, the pilot passes on both platforms: 7/7, 5/5, 4/4 and the access-failure case on each. The note did what it was meant to do — a fresh session found the governing state from the repository, detected what was stale, rejected invented science against the owners, and did not act. The open items are F1–F5; none of them bears on the pass.

Requested next: an independent scoring by the Atlas co-owner (ChatGPT) of the Claude transcripts, to be recorded on its own branch; then the PI's decision on PR #188.
