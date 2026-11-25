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

**Checked:** 21 November 2026, 14:55 +03:00; `main` `a2b3bbe`; tags `atlas-v0.15` (verified), `atlas-method-v0.3`; no source moved after the v0.15 snapshot `357b963`; inbox: no open item.
**Goal / current question:** Atlas v0.15 published (`atlas-v0.15`, verified). Next, with the reviewer: the per-stream state matrix (reviewer lane, stage B), starting from the work list's §1 table.
**Last durable work:** Atlas v0.15 published: `atlas-v0.15` → `a2b3bbe`, file `483e6003…02df`, record `records/atlas/RTG_STATE_ATLAS_v0.15_RELEASE_RECORD.md`, tag verification `records/atlas/RTG_STATE_ATLAS_v0.15_TAG_VERIFICATION.md`; builder `evidence/atlas/build/refresh_v0_15.py`, evidence `evidence/atlas/v0.15/`; one moved source (DZT `dzt-v0.8` → `dzt-v0.19`); review `6004985736` (ACCEPT SCOPED, one round). Programme work list `records/atlas/ATLAS_PROGRAMME_WORK_LIST_20261120.md` (PR #337, open, advisory; snapshot 20 Nov, with the 21 Nov additions A2 RRF records, A6 PRR Wrap-up, A7 other absent sources). Before it: Atlas v0.14, the DZT entry note and the DZT recovery intake (PR #289).
**Decisions held:** PI, 10 Nov: route A — the structure is kept and nothing is dropped for size; compaction is closed; size is looked at again after the remaining streams are reworked. PI, 16 Nov: onboarding starts with DZT; the other onboarding questions come later. `DECLARED` is never `PRESERVED`; grade, qualifier, identifier and diagnostic-class changes are separate reviewed items. A PI adoption names specific bytes; new bytes need a new decision. #189 deferred. `rtg-sat` and `rtg-lit` are outside the Atlas inputs.
**Tried and set aside:** compaction as a route to a size aim (`records/atlas/ATLAS_V0_11_D3_PILOT_STAGE2_RESULT.md` §§3–5, 11).
**Evidence:** v0.15: 27 logged operations; 1 new node (`DZT-THM-CASCADE-NORM-LAW`, cert `DZT-ART-NORMLAW-CHECK`); `*DZT:mechanism HYP` and `*DZT:p40-flag` removed; DZT.Q1, Q4, Q5 and headline H3 retired; no rule-4.1 deletion; shared check 0 FAIL (coverage 137, links 531/2/1, keys 162, wording 13 WARN); 22 focused negative controls detected. The reviewer replayed the 27 operations byte-identically; the builder, checker and control runs are producer records.
**Resume:** `python3 -I evidence/atlas/build/refresh_v0_15.py` (rebuilds and checks; stops on any failed assertion; it imports helpers from `refresh_v0_13.py` and `refresh_v0_10.py`; it stops by design once any source tag is newer than its manifest). The shared checker's coverage check sees Dyadic RIDs only; for other moved sources the builder asserts the homes itself (`HOMES`, `homes_check`).
**Next 1–3 actions / acceptance:**
1. At the next owner tag: impact refresh (Atlas v0.16) from `refresh_v0_15.py`.
2. With the reviewer: the per-stream state matrix, one maintained table with the work list's §1 (not two). A pin is `INTENTIONAL_PIN` only when its owner says so.
3. Carried forward: the four Atlas-side compound heads in D5, at the next D5 opening; DZT B1 (PR #347) enters through a later refresh.
**Reopen trigger:** any owner tag after the v0.15 snapshot `357b963`; any open item in `pipes/ATLAS/`.

## REVIEWER_LANE — ChatGPT

**Checked:** 21 November 2026, GitHub connection, targeted read. Repository `MustafaAksu/rtg-corpus` `main` `2788ebfdc5ab699122bc7f8909696fe4f2212ecd`; governing Atlas `atlas-v0.14` (SHA-256 `d34e5697ae47201133f513bce5f6b2b8438ed2f4e654fe33a73048a5ca7b1e85`, PI accepted and tagged 17 Nov; tag-verification record); Atlas Method `atlas-method-v0.3`. DZT `dzt-v0.19` (PI-adopted, owner release record); no later DZT tag. The current source manifest of `atlas-v0.14` includes 18 sources; DZT is its sole since-moved source. Latest owner tags/records and the `main` snapshot were checked for these relevant claims, not every owner scientific result.

**Goal / current question:** Consolidate Atlas reviewer knowledge and then help the scientific owners bring each stream's working entry, source identities, owner/consumer pins and inbox dispositions into a reviewable current state. This is an evidence and dependency synchronization programme, **not** an Atlas mandate to edit owner science or to repin consumers.

**Durable review checkpoints:**
- Atlas Method v0.3 receiving review: PR #234, reviews `5871391538` (change requested) and `5872066576` (ACCEPT SCOPED).
- Atlas v0.12 receiving review: PR #229, review `5869585886` (ACCEPT SCOPED); the older reviewer checkpoint was accurate for that edition but is superseded by this lane.
- Atlas v0.14 receiving review: PR #293, review `5933660459` (two scoped grade/convention corrections), readback `5933956213` (ACCEPT SCOPED). The v0.14 tag-verification record identifies the accepted bytes.
- Current candidate: **draft PR #349**, branch `claude/atlas-v0.15`, head `46a4105ce9f77def098186763133e715fe27d9c4`; impact refresh `dzt-v0.8` → `dzt-v0.19`, fixed source snapshot `357b963f4a8e33a2dd962952330761bda73a7c05`. Candidate SHA-256 **independently verified and byte-replayed** `483e60034ff3bb644216c5123d28b8bca253d3ba1b72cdf68bfb0056518d02df`. **Receiving review completed: ACCEPT SCOPED**, GitHub review `6004985736`, at the same PR #349 head. The reviewer independently SHA-256 checked the base/candidate and manifest, verified 27/27 unique anchors and 54/54 logged span hashes, reproduced the candidate byte-identically, checked affected owner scientific statements at DZT v0.19 and DYAD v6.4.24, and compared all source identities. The builder's shared checker (0 FAIL, 1 documented-unresolved link) and 22 focused negative controls were **reported and inspected, not independently run**. The candidate is **NOT PI-ACCEPTED OR TAGGED**.

**Entry findings (21 Nov, `main`):** `pipes/ATLAS/INDEX.md` has no open item. All twenty inbox indexes have 147 items: 80 closed, 5 dispositioned and 62 open (index read only; no fresh `pipes_index.py --check` execution). PR #337 is an **open advisory** on programme-wide work, with its 20 Nov frozen snapshot; not an adopted stream policy or a current mechanical census. Shared Atlas orientation's owner lane remains at its own 17 Nov checkpoint: **owner to refresh that lane**, not the reviewer. No owner or PI_PENDING shared text is changed here.

**Decisions/boundaries carried:** Atlas is derived NONCANONICAL; Atlas Method v0.3 and root CONVENTIONS govern maintenance. Owner statements, grades, scopes and RIDs prevail over Atlas. Old consumer pins are not defects by age alone. Maintain the L0–L5 / D1–D6 architecture, negative results, conditionality and provenance. No quantitative size target, lossy compaction or wholesale source reread. Receipt, review, accepted statement, adopted use, merge and tag are separate. No owner scientific campaign has been rerun here.

**Open obligations:** Four inherited compound Atlas heads in D5 (v0.14 record §3), the shared checker's limited non-Dyadic RID extraction, two UNVERIFIED links and two UNVERIFIED artifacts in the v0.15 **candidate** check (not a scientific result), plus the owner's reported F4 independent reporter-session pilot. Missing owner release records for some baseline-pinned streams remain owner/source-identity dependencies and must not be reconstructed from the Atlas. External repositories `rtg-lit` and `rtg-sat` are not Atlas source inputs.

**Next eligible actions / acceptance criteria:**
1. **Review PR #349: completed** — GitHub review `6004985736`, ACCEPT SCOPED on `46a4105`; no blocking Atlas-source fidelity issue. A PI exact-byte decision may now follow, with owner-side publication and BASELINE/tag-verification steps; re-review if candidate bytes change. No science was adopted by the review.
2. After the PI-selected Atlas candidate is accepted and tagged (if accepted), reconcile the Atlas working-memory owner lane with the actual tag, and use PR #337 as a *proposal* to build a dated, verified owner-stream readiness matrix. Owner controls its own lane and advisory disposition.
3. For each active stream, check tag+record+hash, working entry, methodological grade/scope, current owner pins and intentional consumer pins, inbox decisions, evidence state and open scientific dependency. Route one batched advisory per owner; receive the owner's disposition before any consumer repin or Atlas refresh. Start with incomplete cross-stream dependencies (OPEN-M/UVM, RRF and the high-backlog owner interfaces) subject to PI priorities and required source access.

**PI_PENDING for this reviewer:** the Atlas v0.15 receiving verdict is recorded (review `6004985736`); exact-object acceptance **now awaits the PI**. The broader stream activation order/status decisions are not inferred. No merge/tag/push of owner science is authorized by this note.

**Reopen:** PR #349 changes; a newer adopted owner tag; a material reviewer finding; an inbox item; a PI decision. This lane is a checkpoint, not a copied live inventory. Exact mutable refs and counts must be re-queried at resumption.

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
- 21 Nov 2026 (project conversation): the Atlas owner proposed v0.15 (00:07 +03:00); the PI relayed the reviewer's recommendation to start now with four acceptance criteria (00:17); the candidate was built on that (PR #349). Review `6004985736` ACCEPT SCOPED; the PI accepted the named bytes at 14:51 ("benimsiyorum"); CLI block issued 14:52, output returned 14:53; `atlas-v0.15` tagged and verified (`records/atlas/RTG_STATE_ATLAS_v0.15_TAG_VERIFICATION.md`). Nothing for the Atlas edition is waiting on the PI. Open with the PI: the five questions of the work list §4 (PR #337), among them the status of RER, ER-2B, FMS and the PRR Wrap-up, and where the RRF records and the PRR Wrap-up bytes are (the PI noted on 20 Nov that these never reached GitHub).
- F4: one fresh AI session with `gh` and a clone runs the reporter from the BOOTSTRAP message; still open, not blocking.
- CONVENTIONS §9 is generalized (PR #198); follow-up notes on its length, a BASELINE "Entry note" column and the definition of an active stream are with the reviewer, no PI action yet.

The owner records later PI requests and issued CLI blocks here with their exact source.

Checkpoint triggers: a decision, a counterexample or new result, a rejected approach, a completed long computation, a blocker, or imminent context loss — not message counts and not every PR-state change. A pushed commit on an authorized co-owner branch with a discoverable PR is durable but unadopted. Keep detail in the owner's records; this note links to them.
