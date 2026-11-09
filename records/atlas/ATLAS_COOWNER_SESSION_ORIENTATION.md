# ATLAS — Co-owner Session Orientation

**[SESSION] Pilot proposal; no scientific or release authority.**  
**Maintainer:** Atlas owner (Claude). Shared sections need owner approval. Each co-owner edits only its own lane thereafter; cross-lane corrections are review requests. The owner lane below is deliberately unfilled, not an inferred decision.

## ENTRY — discovery and authority

Read **from GitHub**, repository `MustafaAksu/rtg-corpus`; do not assume project synchronization includes `records/`. Before merge, this note is on PR #188, branch `chatgpt/atlas-session-orientation-pilot`; after merge, use its fixed path on `main`.

Start with `CONVENTIONS.md`, this note, `BASELINE.md` and `pipes/ATLAS/INDEX.md`. Fetch missing files through the GitHub connection or an authenticated clone. Failure to access them means **UNVERIFIED**, not an empty queue. Read relevant owner sections before scientific work; consult Methodology when evidence, editing or publication requires it. Atlas refresh policy is **Atlas Method §7**, not this note.

For inherited owner-held obligations, follow §5 of `records/atlas/RTG_STATE_ATLAS_v0.10_RELEASE_RECORD.md`; consult the corresponding post-tag verification for later publication events. Do not duplicate that list here.

## LIVE_STATE — generated, never copied here

The proposed `tools/orient.py` reporter is not yet repository-verified. Until reviewed and installed, use equivalent read-only Git/GitHub queries; do not invent an invocation.

Generate adopted-tag/release identity, target and file hash, observed `main` and local ref/fetch state, open PRs matched by changed paths **and explicit dependencies**, and inbound/outbound queue states. Include Atlas-owned tooling: `evidence/atlas/tools/`, `records/atlas/` and relevant shared tools; title searches alone are insufficient. Inspect #113/#114 as tool/review dependencies, not as automatically ready-to-merge work.

Report query time, input refs and scan coverage. Distinguish a frozen source snapshot from live repository state. Missing permissions, pagination, offline mode or unrecognized adoption records produce **partial/UNVERIFIED**, never “no work”. A newest tag is not necessarily an adopted tag.

## OWNER_LANE — Claude

**Last checked by owner:** not supplied; owner entry pending.  
**Intent / decision held:** owner to fill.  
**Resume:** branch, last pushed work commit, command and next unfinished operation: owner to fill; no job execution inferred.  
**Next actions / acceptance criteria:** owner to select, maximum three.

## REVIEWER_LANE — ChatGPT

**Last checked:** 9 November 2026; full reporter PR #190 `34e55078fcce6041169ee2cab624eef55600b202`, prior requirements and pinned runners, current PR #191/#192 metadata and CONVENTIONS. Independently verified reporter SHA-256 `dfbcb1da…cd0c` and Git blob; executed the unchanged 21 + 6 fixture contracts: 27/27 PASS, exit 0. No live reporter or blind-session run.

**Intent / decision held:** PR #190 ACCEPT SCOPED; all O190-R1–R4 blockers discharged. PR #191 remains ACCEPT SCOPED at `404bfb6`; base integration is separate. Full current decision: `records/atlas/ORIENT_PR190_RECEIVING_REVIEW_CHATGPT.md` on PR #192. No further reporter correction cycle requested. #188 still needs both blind-platform tests; #189 stays deferred.

**Resume:** `chatgpt/orient-pr190-receiving-review`, PR #192, durable checkpoint `b5f13ea0cfe2453b5c6efb1a190ceab56dfb8bf4`. Command: `python3 -I evidence/atlas/tools/orient_receiving/check_orient_round3.py --tool <pinned-script-file> --out <temporary-output-directory>`; extraction/pins and expected exit 0 are in the review. The runner changes only two target pins in memory; prior tests/outputs remain unchanged. No review code is assumed merged.

**Next:** after PI-approved integrations, verify the actual reporter/ref identities and freeze captured PR-response inputs with the answer key; assess fresh ChatGPT and Claude-project tests without hard-coding the former four/seven PR count. This returning session is not a blind test. Preserve both lanes when refreshing the stacked #191 base.

## PI_PENDING — maintained by owner

**Request raised by this reviewer:** review the revised pilot approach after owner reconciliation and tests; no merge/tag approval requested yet. No pilot CLI block issued. #189 is deferred; no Methodology migration is requested. The owner records subsequent PI requests and issued CLI blocks here with their exact source.

Update intent after meaningful decisions or resumable work checkpoints, not each PR-state change. Keep immutable evidence elsewhere; unknown uncommitted work stays unknown. Before wider rollout, each owner selects one entry path and explicitly supersedes or redirects older entry notes.
