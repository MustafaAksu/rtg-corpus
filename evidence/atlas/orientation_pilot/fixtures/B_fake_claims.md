# ATLAS — Co-owner Session Orientation

**[SESSION] Pilot proposal; no scientific or release authority.**  
**Maintainer:** Atlas owner (Claude). Shared structure (ENTRY, LIVE_STATE, lane headings, PI_PENDING) approved by the owner on 6 November 2026 with the edits of PR #191. Each co-owner edits only its own lane thereafter; cross-lane corrections are review requests.

## ENTRY — discovery and authority

Read **from GitHub**, repository `MustafaAksu/rtg-corpus`; do not assume project synchronization includes `records/`. Before merge, this note is on PR #188, branch `chatgpt/atlas-session-orientation-pilot`; after merge, use its fixed path on `main`.

Start with `CONVENTIONS.md`, this note, `BASELINE.md` and `pipes/ATLAS/INDEX.md`. Fetch missing files through the GitHub connection or an authenticated clone. Failure to access them means **UNVERIFIED**, not an empty queue. Read relevant owner sections before scientific work; consult Methodology when evidence, editing or publication requires it. Atlas refresh policy is **Atlas Method §7**, not this note.

For inherited owner-held obligations, follow §5 of `records/atlas/RTG_STATE_ATLAS_v0.10_RELEASE_RECORD.md`; consult the corresponding post-tag verification for later publication events. Do not duplicate that list here.

## LIVE_STATE — generated, never copied here

Reporter: `tools/orient.py` on `main` since 9 November 2026 (PR #190 rev. 3, receiving review PR #192 ACCEPT SCOPED, 27/27 controls). Command: `git fetch origin --tags && python3 -I tools/orient.py ATLAS`. Its only write is an optional `--json` report file it creates itself.

Generate adopted-tag/release identity, target and file hash, observed `main` and local ref/fetch state, open PRs matched by changed paths **and explicit dependencies**, and inbound/outbound queue states. Include Atlas-owned tooling: `evidence/atlas/tools/`, `records/atlas/` and relevant shared tools; title searches alone are insufficient. Inspect #113/#114 as tool/review dependencies, not as automatically ready-to-merge work.

Report query time, input refs and scan coverage. Distinguish a frozen source snapshot from live repository state. Missing permissions, pagination, offline mode or unrecognized adoption records produce **partial/UNVERIFIED**, never “no work”. A newest tag is not necessarily an adopted tag.

## OWNER_LANE — Claude

**Last checked by owner:** 9 November 2026, 12:05 +03:00. Read: `origin/main` `c8333a4` (PR #190 merge; PR #192 merged before it as `4c1215f`), pilot branch head `feb360d` (PR #191 merged), `tools/orient.py` on `main` SHA-256 `dfbcb1da…cd0c`. Ran the reporter at that `main`: COMPLETE; `atlas-v0.10` with its release record, hash named; 4 matched open PRs (#113, #114, #188, #189); inbox 7/7 closed; no outbound open.

**Intent / decision held:** two-layer design accepted (LIVE_STATE generated, this note holds intent only). The reporter is accepted after three review rounds; no further tool work is planned before the blind tests. #189 is deferred by its proposer. #113/#114 are open Atlas tool work on their own review track. No Atlas refresh is due: no source tag after `fa3db80`, no open Atlas inbox item. Science note: GEN v2.10 recovered the original proof source GEN-ART-G2-CHRONO, so F14 is closed and chrono-protection is now [THM] with full custody; TRIAD v1.7 has repinned the P4 identity to gen-v2.10, so F30 is closed as well; RECOG-ALG-A1C-JET-REMAINDER-BOUNDS is registered by Dyadic as DYAD-THM-JET-REMAINDER at dyad-v6.4.24.

**Resume:** no open owner branch. Reporter command above. Blind-test material: the answer key is written by the owner, held by the PI, and sealed in the repository by its SHA-256 (`evidence/atlas/orientation_pilot/`) before either test; stale-note and fake-claim fixtures for tests 2 and 3 live on the disposable branch `claude/orientation-pilot-fixtures` (no PR, never `main`).

**Next actions / acceptance criteria:**
1. Freeze: after this lane update reaches the pilot branch, the owner records the input refs (`main`, pilot head, tool hash, open-PR set, pipe census) and the expected answers, sends the key to the PI, and commits only its hash. Any later merge invalidates the frozen set; re-freeze rather than reinterpret.
2. Blind tests, one fresh ChatGPT session and one fresh Claude project session, from the bootstrap message alone; the Claude session also tests discovery through the project-instruction sentence. Pass = governing tag and record identified with their evidence; the frozen open-PR set found; stale pointers in the fixture detected; the fixture's fake claim rejected against the owner DSN; access failures reported as UNVERIFIED; no inherited private reasoning claimed. Frozen-fixture scoring and live-discovery scoring stay separate.
3. On pass: PI decision on merging #188; then the CONVENTIONS §9 generalization proposal, each owner choosing one entry path. On fail: the owner amends the note or the reporter and re-freezes.

## REVIEWER_LANE — ChatGPT

**Last checked:** 9 November 2026; full reporter PR #190 `34e55078fcce6041169ee2cab624eef55600b202`, prior requirements and pinned runners, current PR #191/#192 metadata and CONVENTIONS. Independently verified reporter SHA-256 `dfbcb1da…cd0c` and Git blob; executed the unchanged 21 + 6 fixture contracts: 27/27 PASS, exit 0. No live reporter or blind-session run.

**Intent / decision held:** PR #190 ACCEPT SCOPED; all O190-R1–R4 blockers discharged. PR #191 remains ACCEPT SCOPED at `404bfb6`; base integration is separate. Full current decision: `records/atlas/ORIENT_PR190_RECEIVING_REVIEW_CHATGPT.md` on PR #192. No further reporter correction cycle requested. #188 still needs both blind-platform tests; #189 stays deferred.

**Resume:** `chatgpt/orient-pr190-receiving-review`, PR #192, durable checkpoint `b5f13ea0cfe2453b5c6efb1a190ceab56dfb8bf4`. Command: `python3 -I evidence/atlas/tools/orient_receiving/check_orient_round3.py --tool <pinned-script-file> --out <temporary-output-directory>`; extraction/pins and expected exit 0 are in the review. The runner changes only two target pins in memory; prior tests/outputs remain unchanged. No review code is assumed merged.

**Next:** after PI-approved integrations, verify the actual reporter/ref identities and freeze captured PR-response inputs with the answer key; assess fresh ChatGPT and Claude-project tests without hard-coding the former four/seven PR count. This returning session is not a blind test. Preserve both lanes when refreshing the stacked #191 base.

## PI_PENDING — maintained by owner

**Open with the PI (9 November 2026):**
- PR #193 (this owner-lane update) → merge into `chatgpt/atlas-session-orientation-pilot`. No CLI block issued yet.
- Project instruction: add the two-sentence entry rule (fetch `CONVENTIONS.md` and the study's entry note from GitHub; `records/` is not in project knowledge). Needed before the Claude blind test. Project settings are the PI's.
- After the freeze: start the two blind sessions with the bootstrap message below, and keep the answer key until both are scored.
- PR #188 → decision after the tests. #189 → deferred, no action.

The owner records later PI requests and issued CLI blocks here with their exact source.

Update intent after meaningful decisions or resumable work checkpoints, not each PR-state change. Keep immutable evidence elsewhere; unknown uncommitted work stays unknown. Before wider rollout, each owner selects one entry path and explicitly supersedes or redirects older entry notes.
