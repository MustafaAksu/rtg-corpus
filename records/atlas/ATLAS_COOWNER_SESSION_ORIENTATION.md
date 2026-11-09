# ATLAS — Co-owner Session Orientation

**[SESSION] Operational working memory of the Atlas stream; no scientific or release authority.** Pilot accepted by the PI on 9 November 2026 (PR #188 merge `53e4125`; blind-test record `records/atlas/ATLAS_ORIENTATION_PILOT_BLIND_TESTS_20261109.md`). Generalization to other streams is a separate PI decision (CONVENTIONS §9).
**Maintainer:** Atlas owner (Claude). Shared sections (header, ENTRY, LIVE_STATE, BOOTSTRAP, PI_PENDING) are the owner's; each co-owner edits only its own lane; cross-lane corrections are review requests.

## ENTRY — discovery and authority

Read **from GitHub**, repository `MustafaAksu/rtg-corpus`, fixed path `records/atlas/ATLAS_COOWNER_SESSION_ORIENTATION.md` on `main`; project synchronization does not include `records/`. Start with `CONVENTIONS.md`, this note, `BASELINE.md` and `pipes/ATLAS/INDEX.md`. Failure to access a source means **UNVERIFIED**, not an empty queue. Atlas refresh policy is **Atlas Method §7**; inherited owner-held obligations are §5 of `records/atlas/RTG_STATE_ATLAS_v0.10_RELEASE_RECORD.md`, read together with the post-tag verification. Neither is duplicated here.

Two supported working modes, chosen after checking the session's own capabilities (details: `records/atlas/COOWNER_EXECUTION_AND_WORKING_MEMORY.md` §§1–2):
- **Native reporter** — Python, Git, a clone with tags, `gh`: run the reporter below.
- **Connection-assisted verification** — no shell or no network: obtain the same refs, tags, release records, PRs and pipe states through the GitHub connection; compute hashes locally when exact bytes are available; state what the mode could not cover (pagination, outbound census).
Temporary files, a temporary clone, local ref refresh and hash computation are permitted within normal permissions. During the entry check: no shared-content change, push, merge, tag, pipe-state change or adoption.

## LIVE_STATE — generated, never copied here

Reporter: `tools/orient.py` on `main` (rev. 3, PR #190; receiving review PR #192, 27/27). Command: `git fetch origin --tags && python3 -I tools/orient.py ATLAS`. Its only write is an optional `--json` report it creates itself. It reports the newest tag with its release-record evidence (never adoption by itself), the governing file's hash at tag and `main`, commits after the tag on Atlas paths, open PRs by changed paths and explicit references, inbound/outbound pipe states, query time, ref freshness and an UNVERIFIED list. A PR that only names a closed PR drops out of the match set; decisions about such PRs live in the lanes (example: #189, deferred). Native runs so far: the PI's server, 9 Nov 2026 08:54 and 12:19 UTC (`evidence/atlas/orientation_pilot/native_run_pi_server_20261109.md`); no fresh AI session has yet invoked it natively.

## BOOTSTRAP — first message for a fresh session

> Act as Atlas co-owner. From GitHub `MustafaAksu/rtg-corpus`, read `CONVENTIONS.md` and `records/atlas/ATLAS_COOWNER_SESSION_ORIENTATION.md`. Verify governing sources and live work; report gaps and next actions. Temporary files/clones, hashes and the reviewed reporter are permitted within normal permissions. Use connector queries when unavailable. During entry, do not modify shared content, push, merge, tag, change pipes or adopt.

## OWNER_LANE — Claude

**Goal / current question:** keep the Atlas current with owner releases and keep this note usable as the stream's working memory; no scientific question open on the Atlas side.
**Last durable work:** `claude/atlas-orientation-maintenance`, this PR (F1–F3 of the test record, bootstrap, BASELINE row, native-run evidence). Before it: PR #195 (test record, `d147d41`), PR #194 (seal), PR #193 (lane), PR #190 (reporter).
**Decisions held:** two-layer design (generated state, intent here) — accepted and tested; #189 deferred by its proposer, no Methodology edition for this; #113/#114 are open Atlas tool work on their own review track (#114's REVISE refers to an older #113 commit, not carried forward automatically); no Atlas refresh due — no source tag after `fa3db80`, no open Atlas inbox item; next refresh counts the pipe items filed after `fa3db80` at its own snapshot.
**Tried and set aside:** a standalone Methodology v1.5 for session orientation (#189) — set aside as too heavy for an operational rule; reopen if CONVENTIONS §9 generalization needs a Methodology hook. Hand-copied live inventory in the note (pilot rev. 1) — set aside after it went stale within a day; reopen never.
**Evidence:** reporter run at `main` `53e4125`: COMPLETE, matched #113 and #114, inbox 7/7 closed, no outbound. Blind tests 9 Nov: both platforms 7/7, 5/5, 4/4, access PASS (sealed key `b1b44898…`).
**Resume:** no unfinished owner computation. Reporter command above.
**Next 1–3 actions / acceptance:**
1. #113/#114: change-focused readback of #113's round-3 fixes (`74ca65e`) against #114's two hash-binding counterexamples; acceptance = receiving verdict recorded on #114's branch.
2. F4: first fresh AI session with native prerequisites runs the reporter and records stdout, status and the tool hash under `evidence/atlas/orientation_pilot/`; connector-mode sessions keep "native NOT RUN".
3. Next Atlas refresh when a source tag moves or an Atlas inbox item opens (Method §7); also add the BASELINE Atlas row's hash to the next release record's checklist.
**Reopen trigger:** any owner tag after `fa3db80`; any open item in `pipes/ATLAS/`; a PI decision to generalize CONVENTIONS §9.

## REVIEWER_LANE — ChatGPT

Checked 9 November 2026: independently verified #195/#196/#188 merges and main `53e412544ae53e3d657a2ef446493f73fe865c9f`; read merged CONVENTIONS §9 and the entry note. PI supplied a successful live native reporter run; this reviewer did not execute it. Held decisions: Atlas pilot accepted; #189 deferred; #113/#114 remain separate tool work. No active reviewer branch. Prior review/evidence is merged under `records/atlas/ATLAS_ORIENTATION_PILOT_RECEIVING_CHATGPT_20261109.md`; do not reopen completed scoring or reporter correction rounds. Next: one maintenance-diff review; then assess the first fresh-session native invocation when prerequisites exist, with connector mode supported when they do not.

*(Text supplied by the reviewer in PR #188 comment 6739968719 and installed unchanged by the owner at the reviewer's request.)*

## PI_PENDING — maintained by owner

**Open with the PI (9 November 2026, after the pilot acceptance):**
- This maintenance PR → merge into `main` after the reviewer's maintenance-diff review. CLI block to follow.
- F4 smoke test: when convenient, start one fresh AI session that has `gh` and a clone, give it the BOOTSTRAP message plus "run the reporter and paste its output"; the owner files the result.
- #113/#114: no PI action until the readback above is recorded.
- CONVENTIONS §9 generalization: PI decision, not requested yet; each owner would choose one entry path and redirect older entry notes.

The owner records later PI requests and issued CLI blocks here with their exact source.

Checkpoint triggers: a decision, a counterexample or new result, a rejected approach, a completed long computation, a blocker, or imminent context loss — not message counts and not every PR-state change. A pushed commit on an authorized co-owner branch with a discoverable PR is durable but unadopted. Keep detail in the owner's records; this note links to them.
