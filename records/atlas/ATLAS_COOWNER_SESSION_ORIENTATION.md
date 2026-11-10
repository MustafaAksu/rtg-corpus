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

**Checked:** 10 November 2026, 15:30 +03:00; `main` `7d6eb4c`; `atlas-v0.10` unchanged; PR #204 open (D3 pilot).
**Goal / current question:** can Atlas v0.11 return towards the Method size aim by compaction? Pilot answer: no (see Evidence). PI decision 10 Nov: route A — keep the structure, shrink only as far as the Method's own removal rules reach.
**Last durable work:** PR #204, branch `claude/atlas-v0.11-d3-pilot`: stage 1 (six second homes → typed cross-references; accepted as intermediate base, review 5840025491) and stage 2a (`records/atlas/ATLAS_V0_11_D3_PILOT_STAGE2_RESULT.md`, files in `evidence/atlas/v0.11_pilot/stage2a/`).
**Decisions held:** order agreed with the PI and the reviewer — tool debt (done) → v0.11 manifest and D3 pilot → one advisory note to the PI on dormant-owner findings (H2, H11, AZ.A1, H3). Size is an aim, not a gate. `DECLARED` is never `PRESERVED`; grade, qualifier, identifier and diagnostic-class changes need a reviewed stage-1 delta. #189 deferred. `rtg-sat` is outside the Atlas inputs; Method v0.3 delta separate.
**Tried and set aside:** the draft-0 extractor — replaced; reopen never. `check_compaction.py` for the Atlas — DSN forms only. Rewording D3 for size — not attempted: every reworded field is a pending review item and the text is already telegraphic; reopen only if the PI chooses a route that needs it.
**Evidence:** stage 1 `0f8ba5c0…a6c2` (12 pending, 7 mapped, 0 FAIL). Stage 2a `ace0b408…a5d6`: deletion-only under Method §4.1/§4.7, 21 spans, MECHANICAL PASS (15 pending, 0 FAIL), yield −1,849 bytes = 1.9 % of D3. Census: 77 % of D3 is L2 claim text; pointers and certificates ≈5.5 kB. A v0.10 defect found: stale `[assuming: (D5)]` at L736 and L740 against `recog-v0.3.27` (result record §6).
**Resume:** `python3 -I evidence/atlas/v0.11_pilot/stage2a/build_stage2a.py STAGE1 OUT MAP SPANS`; `python3 -I tools/atlas_preservation.py compare STAGE1 OUT MAP --report R.json`; `python3 tools/atlas_check.py --manifest evidence/atlas/v0.10/source_manifest.json --atlas OUT` (the default manifest is an old one).
**Next 1–3 actions / acceptance:**
1. v0.11 is reviewed (5841306614) and PI-accepted (`records/atlas/RTG_STATE_ATLAS_v0.11_RELEASE_RECORD.md`); publication is with the PI.
2. After the tag: tag-verification record; BASELINE tag cell and this note's header facts brought to the published state in a small maintenance PR. Method v0.3 delta (size aim subordinate to completeness and structure; `rtg-sat` out of scope) drafted separately.
3. Advisory note to the PI on dormant-owner findings (H2, H11, AZ.A1, H3); Method v0.3 delta (size aim, K1/K2 standing rule, `rtg-sat` out of scope) drafted separately.
**Reopen trigger:** any owner tag after `fa3db80` (impact refresh takes precedence); any open item in `pipes/ATLAS/`.

## REVIEWER_LANE — ChatGPT

Checked 10 November 2026, PR #202 head `1f33166`. Revision-3 source delta inspected; the two rev.2 compound-route residuals are closed. Producer evidence reports self-test 33/33, prior receiving 11/11 and compound routes 4/4, exit 0; this reviewer did not rerun them because the local shell lacked GitHub network materialization. Verdict: ACCEPT SCOPED for the D3 mechanical pilot, not semantic equivalence or Atlas adoption. Next: D3 frozen-base pilot with zero FAIL and every pending/context obligation reviewed; Method v0.3 remains separate.

*(Text supplied by the reviewer in the project conversation of 10 November 2026 and installed unchanged by the owner at the reviewer's request; decision recorded in PR #202 review 5838875546 and PR #203 commit `69f5256`.)*

## PI_PENDING — maintained by owner

**Open with the PI (10 November 2026):**
- **Decided by the PI, 10 Nov 14:02 +03:00 (project conversation): route A** — "continue with A; we want it smaller and shrink as far as we can, but we do not break the structure to shrink it" (translated; recorded in `records/atlas/ATLAS_V0_11_D3_PILOT_STAGE2_RESULT.md` §8). No split, no lossy core.
- **Decided by the PI, 10 Nov 14:40 +03:00:** close the compaction here; the pilot content becomes v0.11; size is looked at again after the other streams (AZ and others) are reworked (verbatim in the v0.11 release record §3).
- **Accepted by the PI, 10 Nov 15:25 +03:00:** Atlas v0.11, `8d7a43f0…f358` (final review 5841306614). **Issued to the PI the same hour:** one CLI block — merge PR #204 (merge commit), check the file hash on `main`, create and push the annotated tag `atlas-v0.11`. Source: project conversation. After the PI returns the output the owner writes the tag-verification record.
- F4: one fresh AI session with `gh` and a clone runs the reporter from the BOOTSTRAP message; still open, not blocking.
- CONVENTIONS §9 is generalized (PR #198); follow-up notes on its length, a BASELINE "Entry note" column and the definition of an active stream are with the reviewer, no PI action yet.

The owner records later PI requests and issued CLI blocks here with their exact source.

Checkpoint triggers: a decision, a counterexample or new result, a rejected approach, a completed long computation, a blocker, or imminent context loss — not message counts and not every PR-state change. A pushed commit on an authorized co-owner branch with a discoverable PR is durable but unadopted. Keep detail in the owner's records; this note links to them.
