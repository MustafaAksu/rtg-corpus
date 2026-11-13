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

**Checked:** 13 November 2026, 12:10 +03:00; `main` `2de679b`; tags `atlas-v0.12` and `atlas-method-v0.3` unchanged; **two source tags moved** since the v0.12 snapshot: `az-v0.8`, `tdrg-v2.12.15`; AZ v0.9 candidate open (PR #253, not adopted); inbox: one item open (AZ v0.8), nine closed.
**Goal / current question:** Atlas v0.13 as one impact refresh for AZ and TDR-G, built after AZ v0.9 is adopted (sequence relayed by the PI on 13 Nov; early two-source refresh only if the AZ review drags).
**Last durable work:** `records/atlas/ATLAS_V0_13_IMPACT_PREPARATION_20261113.md` (impact map, no build, no frozen manifest). Before it: atlas row check of TDR-G v2.12.15 (`records/tdrg/ATLAS_ROW_CHECK_TDRG_v2_12_15.md`, PR #252, merged); Atlas v0.12 and Method v0.3 published.
**Decisions held:** PI, 10 Nov: route A — the structure is kept and nothing is dropped for size; compaction is closed; size is looked at again after the remaining streams (AZ and others) are reworked. `DECLARED` is never `PRESERVED`; grade, qualifier, identifier and diagnostic-class changes need their own reviewed delta. #189 deferred. `rtg-sat` is outside the Atlas inputs.
**Tried and set aside:** compaction as a route to the Method size aim — measured at 1.9 % of D3 under Method v0.2; other domains hold under 0.5 % in labelled form (`records/atlas/ATLAS_V0_11_D3_PILOT_STAGE2_RESULT.md` §§3–5, 11). Reopen when the PI asks after the stream rework. Rewording for size — not attempted. Core + annex split and a lossy core — declined by the PI.
**Evidence:** v0.12: 39 logged operations; AZ.A1, A2, A3, A7 and DYAD.X11 retired; DYAD.X4 narrowed; one new node `DYAD-THM-OPEN21-SHARP-ROWS`; shared check 0 FAIL (coverage 137, links 507/5/10, keys 152); 18 focused negative controls detected. A slip found and recorded: the v0.11 check used the tool's default retired-key list (31) instead of the cumulative one (142); rerun on the v0.11 bytes with the right list: 0 FAIL.
**Resume:** `python3 -I evidence/atlas/build/refresh_v0_12.py` (rebuilds and checks; stops on any failed assertion). A refresh follows the builder of the previous refresh (`refresh_v0_10.py`), not the compaction tools; pass the checker the edition's manifest, coverage map and cumulative retired-key list, never its defaults.
**Next 1–3 actions / acceptance:**
1. When `az-v0.9` is tagged: verify the tag, redo §4 of the preparation record against the adopted bytes, freeze the manifest, build v0.13 under Method v0.3 (`refresh_v0_13.py` on the pattern of `refresh_v0_12.py`), with the RID assertions for TDR-G and AZ that the shared checker lacks.
2. In the build: one node per claim across AZ and TDR-G (the diagnostic under AZ's RID, the token laws under TDR-G's); `PROP-AZ-CORE-EQUIV` THM-ALG → THM as its own reviewed item; TDRG.G9 re-evaluated; D5 cleaned by rules 4.1 and 4.7.
3. Change-focused review, PI acceptance, tag; close the AZ v0.8 inbox item.
**Reopen trigger:** any owner tag after the v0.12 snapshot `c8e7198` (impact refresh); any open item in `pipes/ATLAS/`.

## REVIEWER_LANE — ChatGPT

**Checked:** 12 November 2026, via GitHub; `main` `2679f37d4f50eb4f02f575f863ddbb5c9be5ce7c`. Atlas v0.12 is published (`atlas-v0.12`, SHA-256 `cf9d8647b4c33206537e46ca37c7879d4fc33b1a936e0a50330a469f054def55`). Atlas Method v0.3 is published (`atlas-method-v0.3`, SHA-256 `a29217352d989f75310f1c5fbb5e666cb02be9bc9a7c3b67d03d6e138115509f`). PR #225 is closed without merge. Subsequent commits after `f390087` affect DYAD working evidence, records and pipes, not Atlas or Method content.

**Goal / current question:** No receiving review is pending. Resume when a new Atlas candidate or methodological change requires independent examination.

**Last durable work:**

- Atlas v0.12 receiving review: PR #229, review `5869585886`, ACCEPT SCOPED. Reviewed AZ v0.7 and DYAD v6.4.24 source impacts, new RID coverage, conditional results, diagnostic retirements and evidence boundaries.
- Atlas Method v0.3 receiving review: PR #234, initial review `5871391538` (ACCEPT WITH CHANGE), final readback `5872066576` (ACCEPT SCOPED). All requested changes closed.
- Reviewer preparation PR #225 closed unmerged, with its findings incorporated into the v0.12 review. Its historical checkpoint must not overwrite the current shared orientation note.

**Decisions held:** Preserve completeness, scientific scope and the L0–L5 / D1–D6 structure; no quantitative size target, split or fact-for-pointer substitution. Apply K1/K2 deletion rules during affected-domain refreshes, never as automatic scientific changes. Preserve intentional consumer pins, owner grades, hypotheses, negative results and evidence limitations. A mechanical PASS does not establish semantic equivalence, scientific validity or adoption. Atlas Method v0.3 governs future Atlas work; owner DSNs govern scientific claims.

**Evidence:** Independently verified Atlas v0.12's full-file SHA-256 and reproduced its 39 logged transformations byte-for-byte from `atlas-v0.11`. Checked the two changed source identities, targeted owner statements, new conditional theorem, and cumulative L5 retirements. Independently verified the final Method v0.3 SHA-256 and established that its final correction changed exactly one line (§4.6). Published identities were checked against `BASELINE.md`; publication and tag-verification records belong to the owner release workflow.

**Not rerun:** Owner scientific certificates and numerical campaigns; Atlas builder/checker campaigns and their negative controls; unchanged scientific content of the other sixteen Atlas inputs. The producer-reported structural PASS results were inspected, not independently re-executed. No independent post-tag certificate campaign was performed by this reviewer.

**Resume / next actions:**

1. At the next adopted owner tag, inspect the Atlas owner's impact assessment and frozen source manifest under Method v0.3.
2. Review the changed Atlas records, owner-source correspondence, RID coverage, conditionality, evidence qualifications, L5 dispositions, and all declared preservation obligations.
3. Produce a change-focused receiving verdict before PI acceptance. Do not repeat unchanged expensive scientific campaigns without a concrete discrepancy.

**Reopen trigger:** A new adopted owner tag after the v0.12 snapshot (`c8e7198`), a newly open `pipes/ATLAS/` item, a proposed Method change, a substantive counterexample, or a PI request. No outstanding action remains from PR #225 or the v0.12/Method v0.3 publication reviews.

*(Text supplied by the reviewer in the project conversation of 12 November 2026, 15:07 +03:00, and installed unchanged by the owner at the reviewer's request; it replaces the PR #202 checkpoint text of 10 November. SHA-256 of the installed block, heading through the reopen-trigger paragraph: `1fb25d8b1174388bd9d92180f73febd6fd0f6f174377d19ab2143ca7b07c5604`.)*

## PI_PENDING — maintained by owner

**Open with the PI (10 November 2026):**
- **Decided by the PI, 10 Nov 14:02 +03:00 (project conversation): route A** — "continue with A; we want it smaller and shrink as far as we can, but we do not break the structure to shrink it" (translated; recorded in `records/atlas/ATLAS_V0_11_D3_PILOT_STAGE2_RESULT.md` §8). No split, no lossy core.
- Nothing is waiting on the PI for the Atlas. v0.11 is accepted, merged and tagged (10 Nov; CLI block issued in the project conversation at 15:27 +03:00, output returned 15:29).
- 10 Nov 17:23: advisory dispositions decided (`records/atlas/ATLAS_ADVISORY_TO_PI_DORMANT_OWNERS_20261110.md` §4); rows 1 and 3 since resolved by `az-v0.7`.
- 11 Nov 18:15: the PI accepted all six recommendations of `records/atlas/ATLAS_ADVISORY_AZ_STATE_20261111.md` (§5); they are AZ's to carry out.
- Nothing is waiting on the PI for the Atlas. v0.13 is prepared, not built; it starts when `az-v0.9` is tagged (13 Nov, project conversation, 11:23 +03:00).
- F4: one fresh AI session with `gh` and a clone runs the reporter from the BOOTSTRAP message; still open, not blocking.
- CONVENTIONS §9 is generalized (PR #198); follow-up notes on its length, a BASELINE "Entry note" column and the definition of an active stream are with the reviewer, no PI action yet.

The owner records later PI requests and issued CLI blocks here with their exact source.

Checkpoint triggers: a decision, a counterexample or new result, a rejected approach, a completed long computation, a blocker, or imminent context loss — not message counts and not every PR-state change. A pushed commit on an authorized co-owner branch with a discoverable PR is durable but unadopted. Keep detail in the owner's records; this note links to them.
