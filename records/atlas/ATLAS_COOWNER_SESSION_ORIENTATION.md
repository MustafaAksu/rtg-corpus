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

**Checked:** 11 November 2026, 15:30 +03:00; `main` `5ffec34`; tag `atlas-v0.11` unchanged; **two source tags moved** since the v0.11 snapshot: `az-v0.7`, `dyad-v6.4.24`; inbox: two items dispositioned (AZ, DYAD), seven closed.
**Goal / current question:** impact refresh Atlas v0.12 for `az-v0.7` and `dyad-v6.4.24` (Method §7). Second advisory written: `records/atlas/ATLAS_ADVISORY_AZ_STATE_20261111.md` (state of AZ after reactivation; six questions to the PI).
**Last durable work:** Atlas v0.11 published (release record and tag verification under `records/atlas/RTG_STATE_ATLAS_v0.11_*`): six second homes → typed cross-references, 21 D3 span deletions (edition labels, method detail), three stale `(D5)` tags corrected against `recog-v0.3.27`. No source moved.
**Decisions held:** PI, 10 Nov: route A — the structure is kept and nothing is dropped for size; compaction is closed; size is looked at again after the remaining streams (AZ and others) are reworked. `DECLARED` is never `PRESERVED`; grade, qualifier, identifier and diagnostic-class changes need their own reviewed delta. #189 deferred. `rtg-sat` is outside the Atlas inputs.
**Tried and set aside:** compaction as a route to the Method size aim — measured at 1.9 % of D3 under Method v0.2; other domains hold under 0.5 % in labelled form (`records/atlas/ATLAS_V0_11_D3_PILOT_STAGE2_RESULT.md` §§3–5, 11). Reopen when the PI asks after the stream rework. Rewording for size — not attempted. Core + annex split and a lossy core — declined by the PI.
**Evidence:** chain `443b5990…` → stage 1 `0f8ba5c0…` → 2a `ace0b408…` → 2b `66f0b2eb…` → v0.11 `8d7a43f0…`; each builder asserts its input hash. Known tool limit: `atlas_preservation.py` reports the whole file when the title heading changes (heading context); such a step is shown by a line diff.
**Resume:** `python3 -I tools/orient.py ATLAS`; `python3 tools/atlas_check.py --manifest evidence/atlas/v0.11/source_manifest.json` (the default manifest is an old one).
**Next 1–3 actions / acceptance:**
1. Atlas v0.12 impact refresh: AZ rows (AZ.A1, A2, A3, A7 expected to close; H2, H3 reworded; Thread C evidence qualifier) and the Dyadic notice items; source manifest at the new snapshot; change-focused review; PI acceptance.
2. Close the two dispositioned inbox items when v0.12 is published.
3. Method v0.3 delta, separately reviewed (size aim subordinate to completeness and structure; K1/K2 at refreshes; satellite repositories out of scope). Deferred debts: seven other multi-line identifiers; a comparator mode for heading renames.
**Reopen trigger:** any owner tag after `fa3db80` (impact refresh); any open item in `pipes/ATLAS/`.

## REVIEWER_LANE — ChatGPT

**Checked:** 11 November 2026; `main` merge commit `c8e71980d053545edcc2f4d1fc5ccf92460de48f` (PR #219 merged). Governing Atlas: `atlas-v0.11`; changed source tags: AZ `az-v0.7`, DYAD `dyad-v6.4.24`; the other 16 v0.11 manifest source hashes still match `BASELINE.md`.

**Goal:** change-focused source-impact preparation and subsequent independent receiving review of Atlas v0.12; no ownership or adoption of another stream's science.

**Last durable work:** PR #225, `records/atlas/ATLAS_V0_12_CHATGPT_SOURCE_IMPACT_PREPARATION_20261111.md`. Verified the two tagged owner editions, release/adoption records and related Atlas v0.11 records; mapped AZ.A1/A2/A3/A7 closure, retained AZ.A5/DZT.Q1, H2/H3 narrowing; DYAD.X4 partial closure, three pseudo-RID replacements, the R9-conditional OPEN21 sharpened theorem and the SESSION ceiling of OPEN20. No live Atlas, DSN, pipe or Method content changed.

**Decision/evidence boundary:** Atlas owner Claude prepares the actual v0.12 frozen source manifest and candidate. The review note is SESSION/preparation, not a review verdict on unbuilt candidate; no owner certificate, Atlas builder or checker rerun. Post-tag partial AZ Thread C recovery is evidence custody, not an adopted AZ claim or grade change.

**Resume:** inspect PR #225 against `atlas-v0.11`, `az-v0.7`, `dyad-v6.4.24`, and release records; on receiving an owner candidate, check its manifest, exact changed lines, L5 lifecycle, all new RID coverage, pending comparator items and `atlas_check.py` 0-FAIL report. Do not rerun unchanged scientific campaigns without a new inconsistency.

**Next actions:** (1) Atlas owner review/consume PR #225 as input, (2) targeted receiving review of the owner's v0.12 stage-1/extraction and change map, (3) independent verdict on final candidate before any PI acceptance. **Reopen trigger:** a new adopted owner tag or new inbox item after this source freeze.

## PI_PENDING — maintained by owner

**Open with the PI (10 November 2026):**
- **Decided by the PI, 10 Nov 14:02 +03:00 (project conversation): route A** — "continue with A; we want it smaller and shrink as far as we can, but we do not break the structure to shrink it" (translated; recorded in `records/atlas/ATLAS_V0_11_D3_PILOT_STAGE2_RESULT.md` §8). No split, no lossy core.
- Nothing is waiting on the PI for the Atlas. v0.11 is accepted, merged and tagged (10 Nov; CLI block issued in the project conversation at 15:27 +03:00, output returned 15:29).
- 10 Nov 17:23: advisory dispositions decided (`records/atlas/ATLAS_ADVISORY_TO_PI_DORMANT_OWNERS_20261110.md` §4); rows 1 and 3 since resolved by `az-v0.7`.
- 11 Nov 18:15: the PI accepted all six recommendations of `records/atlas/ATLAS_ADVISORY_AZ_STATE_20261111.md` (§5). They are AZ's to carry out; the Atlas needs no decision for its own refresh.
- F4: one fresh AI session with `gh` and a clone runs the reporter from the BOOTSTRAP message; still open, not blocking.
- CONVENTIONS §9 is generalized (PR #198); follow-up notes on its length, a BASELINE "Entry note" column and the definition of an active stream are with the reviewer, no PI action yet.

The owner records later PI requests and issued CLI blocks here with their exact source.

Checkpoint triggers: a decision, a counterexample or new result, a rejected approach, a completed long computation, a blocker, or imminent context loss — not message counts and not every PR-state change. A pushed commit on an authorized co-owner branch with a discoverable PR is durable but unadopted. Keep detail in the owner's records; this note links to them.
