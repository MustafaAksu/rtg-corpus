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

**Last checked:** 9 November 2026; full PR #190 code at `029524acb3117fcfa46665412385dfbe36aba928`, producer examples, PR #191 diff/file at `e673840fbbf537c00a6852a95a655c2f7f9e780e`, and CONVENTIONS. Executed 21 offline fixture controls against unchanged, hash-verified reporter bytes: 10 PASS, 11 FAIL. No live reporter or blind-session run.

**Intent / decision held:** PR #190 REVISE, one owner correction batch O190-R1–R4 (uncertainty propagation, exact tag/record identity, deterministic PR discovery, safe JSON output). PR #191 ACCEPT SCOPED for its pilot base, with two nonblocking notes. Full findings: `records/atlas/ORIENT_PR190_RECEIVING_REVIEW_CHATGPT.md` on PR #192. #189 remains deferred; no new Atlas scientific refresh requested.

**Resume:** `chatgpt/orient-pr190-receiving-review`, PR #192, durable checkpoint `2ec275bf8e4dfec0198ea351ef37f6e99edbe1d3`. Command: `python3 -I evidence/atlas/tools/orient_receiving/test_orient_receiving.py --tool <pinned-script-file> --out <temporary-output-directory>`; exact source extraction and expected exit 1 are in the review. No review code is assumed merged.

**Next:** receive the owner's single correction batch and rerun scoped controls; then assess fresh ChatGPT and Claude-project tests against a pre-frozen answer key. Neither blind test has been performed by this reviewer.

## PI_PENDING — maintained by owner

**Request raised by this reviewer:** review the revised pilot approach after owner reconciliation and tests; no merge/tag approval requested yet. No pilot CLI block issued. #189 is deferred; no Methodology migration is requested. The owner records subsequent PI requests and issued CLI blocks here with their exact source.

Update intent after meaningful decisions or resumable work checkpoints, not each PR-state change. Keep immutable evidence elsewhere; unknown uncommitted work stays unknown. Before wider rollout, each owner selects one entry path and explicitly supersedes or redirects older entry notes.
