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

**Checked:** 21 November 2026, 14:50 +03:00; `main` `2788ebf`; tags `atlas-v0.14` (verified), `atlas-method-v0.3`, `dzt-v0.19` (20 Nov; annotated, → `5f3b205`); inbox: no open item. Between the v0.15 snapshot `357b963` and `2788ebf` nothing changed under `dsn/`, `atlas/`, `pipes/` or in `BASELINE.md`.
**Goal / current question:** Atlas v0.15 candidate (draft PR #349) awaits the reviewer's change-focused review, then the PI's decision on named bytes. `atlas-v0.14` governs until then.
**Last durable work:** Atlas v0.15 candidate, branch `claude/atlas-v0.15`, head `46a4105`: file `483e6003…02df` (542,028 bytes), manifest `5fadeb23…46cd`, snapshot `357b963`; one moved source (DZT `dzt-v0.8` → `dzt-v0.19`); record `records/atlas/RTG_STATE_ATLAS_v0.15_RELEASE_RECORD.md` (DRAFT); builder `evidence/atlas/build/refresh_v0_15.py`, evidence `evidence/atlas/v0.15/`. Programme work list `records/atlas/ATLAS_PROGRAMME_WORK_LIST_20261120.md` (PR #337, open, advisory; snapshot 20 Nov, with the 21 Nov additions A2 RRF records, A6 PRR Wrap-up, A7 other absent sources). Before it: Atlas v0.14 (published, verified), the DZT entry note and the DZT recovery intake (PR #289).
**Decisions held:** PI, 10 Nov: route A — the structure is kept and nothing is dropped for size; compaction is closed; size is looked at again after the remaining streams are reworked. PI, 16 Nov: onboarding starts with DZT; the other onboarding questions come later. `DECLARED` is never `PRESERVED`; grade, qualifier, identifier and diagnostic-class changes are separate reviewed items. A PI adoption names specific bytes; new bytes need a new decision. #189 deferred. `rtg-sat` and `rtg-lit` are outside the Atlas inputs.
**Tried and set aside:** compaction as a route to a size aim (`records/atlas/ATLAS_V0_11_D3_PILOT_STAGE2_RESULT.md` §§3–5, 11).
**Evidence:** v0.15 candidate: 27 logged operations; 1 new node (`DZT-THM-CASCADE-NORM-LAW`, cert `DZT-ART-NORMLAW-CHECK`); `*DZT:mechanism HYP` and `*DZT:p40-flag` removed; DZT.Q1, Q4, Q5 and headline H3 retired; no rule-4.1 deletion; shared check 0 FAIL (coverage 137, links 531/2/1, keys 162, wording 13 WARN); 22 focused negative controls detected. Producer records until the reviewer reproduces them.
**Resume:** `python3 -I evidence/atlas/build/refresh_v0_15.py` on `claude/atlas-v0.15` (rebuilds and checks; stops on any failed assertion; it imports helpers from `refresh_v0_13.py` and `refresh_v0_10.py`; it stops by design once any source tag is newer than its manifest). The shared checker's coverage check sees Dyadic RIDs only; for other moved sources the builder asserts the homes itself (`HOMES`, `homes_check`).
**Next 1–3 actions / acceptance:**
1. Answer the reviewer's findings on PR #349; any change to the candidate gives new bytes and a readback.
2. After the PI's decision: BASELINE row and record on the branch, one CLI block for merge and tag, then the tag verification.
3. With the reviewer: the per-stream state matrix proposed in the reviewer lane, starting from the work list's §1 table (one maintained table, not two). Carried forward: the four Atlas-side compound heads in D5; DZT B1 (PR #347) enters through a later refresh.
**Reopen trigger:** a review on PR #349; any owner tag after the v0.15 snapshot `357b963`; any open item in `pipes/ATLAS/`.

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
- 13 Nov, 11:23 +03:00 (project conversation): v0.13 to be built as one refresh once `az-v0.9` is tagged; 14 Nov: the PI reported the tag; the candidate was built.
- 16 Nov 2026, 15:45 +03:00: the PI accepted Atlas v0.13 and adopted TDR-G v2.13. `atlas-v0.13` tagged and verified (`records/atlas/RTG_STATE_ATLAS_v0.13_TAG_VERIFICATION.md`).
- 17 Nov 2026: the PI started Atlas v0.14 (08:30) and accepted it (09:29, "Atlas v0.14 ü benimsiyorum"); `atlas-v0.14` tagged and verified (`records/atlas/RTG_STATE_ATLAS_v0.14_TAG_VERIFICATION.md`). Nothing for the Atlas is waiting on the PI.
- TDR-G v2.13 (PR #265, candidate `c79898f9…36f4`): atlas row check ACCEPT FOR ADOPTION after F1 (`records/tdrg/ATLAS_ROW_CHECK_TDRG_v2_13.md` §6, PR #277). After its tag: Atlas v0.14 refresh.
- 21 Nov 2026 (project conversation): the Atlas owner proposed v0.15 (00:07 +03:00); the PI relayed the reviewer's recommendation to start now with four acceptance criteria (00:17); the candidate was built on that (PR #349). **Waiting on the PI, after the review:** acceptance of named v0.15 bytes. Also open with the PI: the five questions of the work list §4 (PR #337), among them the status of RER, ER-2B, FMS and the PRR Wrap-up, and where the RRF records and the PRR Wrap-up bytes are (the PI noted on 20 Nov that these never reached GitHub).
- F4: one fresh AI session with `gh` and a clone runs the reporter from the BOOTSTRAP message; still open, not blocking.
- CONVENTIONS §9 is generalized (PR #198); follow-up notes on its length, a BASELINE "Entry note" column and the definition of an active stream are with the reviewer, no PI action yet.

The owner records later PI requests and issued CLI blocks here with their exact source.

Checkpoint triggers: a decision, a counterexample or new result, a rejected approach, a completed long computation, a blocker, or imminent context loss — not message counts and not every PR-state change. A pushed commit on an authorized co-owner branch with a discoverable PR is durable but unadopted. Keep detail in the owner's records; this note links to them.
