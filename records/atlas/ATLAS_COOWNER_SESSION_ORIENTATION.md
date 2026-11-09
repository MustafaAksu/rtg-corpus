# ATLAS — Co-owner Session Orientation

**[SESSION] Pilot proposal; no scientific or release authority.**  
**Maintainer:** Atlas owner (Claude). Shared structure (ENTRY, LIVE_STATE, lane headings, PI_PENDING) approved by the owner on 6 November 2026 with the edits of PR #191. Each co-owner edits only its own lane thereafter; cross-lane corrections are review requests. The owner lane below is deliberately unfilled, not an inferred decision.

## ENTRY — discovery and authority

Read **from GitHub**, repository `MustafaAksu/rtg-corpus`; do not assume project synchronization includes `records/`. Before merge, this note is on PR #188, branch `chatgpt/atlas-session-orientation-pilot`; after merge, use its fixed path on `main`.

Start with `CONVENTIONS.md`, this note, `BASELINE.md` and `pipes/ATLAS/INDEX.md`. Fetch missing files through the GitHub connection or an authenticated clone. Failure to access them means **UNVERIFIED**, not an empty queue. Read relevant owner sections before scientific work; consult Methodology when evidence, editing or publication requires it. Atlas refresh policy is **Atlas Method §7**, not this note.

For inherited owner-held obligations, follow §5 of `records/atlas/RTG_STATE_ATLAS_v0.10_RELEASE_RECORD.md`; consult the corresponding post-tag verification for later publication events. Do not duplicate that list here.

## LIVE_STATE — generated, never copied here

Reporter: `tools/orient.py` (PR #190, under co-owner review; not on `main` yet). Once merged: `git fetch origin --tags && python3 -I tools/orient.py ATLAS`. Until then use equivalent read-only Git/GitHub queries.

Generate adopted-tag/release identity, target and file hash, observed `main` and local ref/fetch state, open PRs matched by changed paths **and explicit dependencies**, and inbound/outbound queue states. Include Atlas-owned tooling: `evidence/atlas/tools/`, `records/atlas/` and relevant shared tools; title searches alone are insufficient. Inspect #113/#114 as tool/review dependencies, not as automatically ready-to-merge work.

Report query time, input refs and scan coverage. Distinguish a frozen source snapshot from live repository state. Missing permissions, pagination, offline mode or unrecognized adoption records produce **partial/UNVERIFIED**, never “no work”. A newest tag is not necessarily an adopted tag.

## OWNER_LANE — Claude

**Last checked by owner:** 6 November 2026, 15:25 +03:00. Read: `origin/main` `e4f3dbf` (PR #187 merge), `atlas-v0.10` with its release record and tag verification, PR #188 head `dbbaad4`, PR #189 head `ebd97b0`, PRs #113/#114 open. Ran `tools/orient.py ATLAS` at that `main`: 4 matched PRs (#113, #114, #188, #189), inbox 7/7 closed, no outbound open.

**Intent / decision held:** the two-layer design is accepted: LIVE_STATE is generated, this note holds intent only. #189 (Methodology v1.5) is deferred; generalization, if the pilot passes, goes through CONVENTIONS §9 and a later natural Methodology revision. #113/#114 (`check_compaction` tool and its review) stay on their own review track; they are open Atlas tool work, not release work. No Atlas refresh is due: no source tag after `fa3db80` and no open Atlas inbox item.

**Resume:** tool work on `claude/tool-orient` (PR #190, commit `029524a`); command `python3 -I tools/orient.py ATLAS --json <out>`; sample runs in `evidence/atlas/tools/orient_20261106/`. Owner-lane edit on `claude/atlas-orientation-owner-lane` (PR #191, stacked on #188). Nothing uncommitted of value; the scratchpad prototype was superseded by the committed tool.

**Next actions / acceptance criteria:**
1. PR #190 reviewed by the co-owner against the four named properties (path-based PR discovery, tag ≠ adoption, incomplete scan ≠ no work, no writes); then PI merge.
2. Freeze the blind-test answer key (refs, PR numbers, pipe states, next action) in `evidence/atlas/orientation_pilot/` before either test; run one fresh ChatGPT session and one fresh Claude project session from the bootstrap message alone. Pass = correct governing tag and record, all four Atlas PRs found, no inherited private reasoning claimed, access failures reported as UNVERIFIED.
3. On pass: PI decision on merging #188; then the CONVENTIONS §9 generalization proposal, with each owner choosing one entry path.

## REVIEWER_LANE — ChatGPT

**Last checked:** 9 November 2026; full PR #190 code at `029524acb3117fcfa46665412385dfbe36aba928`, producer examples, PR #191 diff/file at `e673840fbbf537c00a6852a95a655c2f7f9e780e`, and CONVENTIONS. Executed 21 offline fixture controls against unchanged, hash-verified reporter bytes: 10 PASS, 11 FAIL. No live reporter or blind-session run.

**Intent / decision held:** PR #190 REVISE, one owner correction batch O190-R1–R4 (uncertainty propagation, exact tag/record identity, deterministic PR discovery, safe JSON output). PR #191 ACCEPT SCOPED for its pilot base, with two nonblocking notes. Full findings: `records/atlas/ORIENT_PR190_RECEIVING_REVIEW_CHATGPT.md` on PR #192. #189 remains deferred; no new Atlas scientific refresh requested.

**Resume:** `chatgpt/orient-pr190-receiving-review`, PR #192, durable checkpoint `2ec275bf8e4dfec0198ea351ef37f6e99edbe1d3`. Command: `python3 -I evidence/atlas/tools/orient_receiving/test_orient_receiving.py --tool <pinned-script-file> --out <temporary-output-directory>`; exact source extraction and expected exit 1 are in the review. No review code is assumed merged.

**Next:** receive the owner's single correction batch and rerun scoped controls; then assess fresh ChatGPT and Claude-project tests against a pre-frozen answer key. Neither blind test has been performed by this reviewer.

## PI_PENDING — maintained by owner

**Open with the PI (6 November 2026):**
- PR #191 (this owner lane) → merge into `chatgpt/atlas-session-orientation-pilot`, so #188 carries both lanes. No CLI block issued yet.
- PR #190 (`tools/orient.py`) → merge into `main` after the co-owner review. No CLI block issued yet.
- PR #188 itself → decision after the blind tests; not requested yet.
- #189 → deferred by the proposer; no action requested.
- Project instruction: the two-sentence entry rule proposed in the project conversation (fetch CONVENTIONS and the entry note from GitHub; `records/` is not in project knowledge). Project settings are the PI's; nothing changed.

The owner records later PI requests and issued CLI blocks here with their exact source.

Update intent after meaningful decisions or resumable work checkpoints, not each PR-state change. Keep immutable evidence elsewhere; unknown uncommitted work stays unknown. Before wider rollout, each owner selects one entry path and explicitly supersedes or redirects older entry notes.
