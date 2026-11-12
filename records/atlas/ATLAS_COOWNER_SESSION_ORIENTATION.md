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

**Checked:** 12 November 2026, 10:15 +03:00; `main` `661b295` (PR #229 merged); tag `atlas-v0.12` → `661b295`, file `cf9d8647…ef55`; all 18 source tags are the newest of their studies; inbox 9/9 closed.
**Goal / current question:** none open for the Atlas file. Next owner product: the Method v0.3 delta.
**Last durable work:** Atlas v0.12 published (impact refresh for AZ v0.7 and Dyadic v6.4.24; release record and tag verification under `records/atlas/RTG_STATE_ATLAS_v0.12_*`; builder `evidence/atlas/build/refresh_v0_12.py`). Before it: Atlas v0.11 and two advisories (`records/atlas/ATLAS_ADVISORY_TO_PI_DORMANT_OWNERS_20261110.md`, `records/atlas/ATLAS_ADVISORY_AZ_STATE_20261111.md`).
**Decisions held:** PI, 10 Nov: route A — the structure is kept and nothing is dropped for size; compaction is closed; size is looked at again after the remaining streams (AZ and others) are reworked. `DECLARED` is never `PRESERVED`; grade, qualifier, identifier and diagnostic-class changes need their own reviewed delta. #189 deferred. `rtg-sat` is outside the Atlas inputs.
**Tried and set aside:** compaction as a route to the Method size aim — measured at 1.9 % of D3 under Method v0.2; other domains hold under 0.5 % in labelled form (`records/atlas/ATLAS_V0_11_D3_PILOT_STAGE2_RESULT.md` §§3–5, 11). Reopen when the PI asks after the stream rework. Rewording for size — not attempted. Core + annex split and a lossy core — declined by the PI.
**Evidence:** v0.12: 39 logged operations; AZ.A1, A2, A3, A7 and DYAD.X11 retired; DYAD.X4 narrowed; one new node `DYAD-THM-OPEN21-SHARP-ROWS`; shared check 0 FAIL (coverage 137, links 507/5/10, keys 152); 18 focused negative controls detected. A slip found and recorded: the v0.11 check used the tool's default retired-key list (31) instead of the cumulative one (142); rerun on the v0.11 bytes with the right list: 0 FAIL.
**Resume:** `python3 -I evidence/atlas/build/refresh_v0_12.py` (rebuilds and checks; stops on any failed assertion). A refresh follows the builder of the previous refresh (`refresh_v0_10.py`), not the compaction tools; pass the checker the edition's manifest, coverage map and cumulative retired-key list, never its defaults.
**Next 1–3 actions / acceptance:**
1. Method v0.3 delta, separately reviewed: size aim subordinate to completeness and structure; K1/K2 span deletions as a standing rule when a domain is opened for a refresh; satellite repositories out of scope; a refresh passes the checker the edition's own manifest, coverage map and cumulative retired-key list.
2. Watch for the next owner tags: AZ (Action 1 and the Thread C recovery are [SESSION] until an AZ or TDR-G edition adopts them), DZT, OPEN-M, TDR-G.
3. Deferred debts: seven other multi-line identifiers; a comparator mode for heading renames; a built-in AZ profile for `tools/orient.py`.
**Reopen trigger:** any owner tag after `fa3db80` (impact refresh); any open item in `pipes/ATLAS/`.

## REVIEWER_LANE — ChatGPT

Checked 10 November 2026, PR #202 head `1f33166`. Revision-3 source delta inspected; the two rev.2 compound-route residuals are closed. Producer evidence reports self-test 33/33, prior receiving 11/11 and compound routes 4/4, exit 0; this reviewer did not rerun them because the local shell lacked GitHub network materialization. Verdict: ACCEPT SCOPED for the D3 mechanical pilot, not semantic equivalence or Atlas adoption. Next: D3 frozen-base pilot with zero FAIL and every pending/context obligation reviewed; Method v0.3 remains separate.

*(Text supplied by the reviewer in the project conversation of 10 November 2026 and installed unchanged by the owner at the reviewer's request; decision recorded in PR #202 review 5838875546 and PR #203 commit `69f5256`.)*

## PI_PENDING — maintained by owner

**Open with the PI (10 November 2026):**
- **Decided by the PI, 10 Nov 14:02 +03:00 (project conversation): route A** — "continue with A; we want it smaller and shrink as far as we can, but we do not break the structure to shrink it" (translated; recorded in `records/atlas/ATLAS_V0_11_D3_PILOT_STAGE2_RESULT.md` §8). No split, no lossy core.
- Nothing is waiting on the PI for the Atlas. v0.11 is accepted, merged and tagged (10 Nov; CLI block issued in the project conversation at 15:27 +03:00, output returned 15:29).
- 10 Nov 17:23: advisory dispositions decided (`records/atlas/ATLAS_ADVISORY_TO_PI_DORMANT_OWNERS_20261110.md` §4); rows 1 and 3 since resolved by `az-v0.7`.
- 11 Nov 18:15: the PI accepted all six recommendations of `records/atlas/ATLAS_ADVISORY_AZ_STATE_20261111.md` (§5); they are AZ's to carry out.
- Nothing is waiting on the PI for the Atlas. v0.12 is accepted, merged and tagged (12 Nov; CLI block issued in the project conversation at 09:55 +03:00, output returned 10:06).
- PR #225 (the reviewer's v0.12 preparation record): the reviewer advises closing it unmerged; the PI's call.
- F4: one fresh AI session with `gh` and a clone runs the reporter from the BOOTSTRAP message; still open, not blocking.
- CONVENTIONS §9 is generalized (PR #198); follow-up notes on its length, a BASELINE "Entry note" column and the definition of an active stream are with the reviewer, no PI action yet.

The owner records later PI requests and issued CLI blocks here with their exact source.

Checkpoint triggers: a decision, a counterexample or new result, a rejected approach, a completed long computation, a blocker, or imminent context loss — not message counts and not every PR-state change. A pushed commit on an authorized co-owner branch with a discoverable PR is durable but unadopted. Keep detail in the owner's records; this note links to them.
