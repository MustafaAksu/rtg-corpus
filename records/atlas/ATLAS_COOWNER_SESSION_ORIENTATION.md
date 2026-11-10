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

**Checked:** 10 November 2026, 11:30 +03:00; `main` `752bb6a` (PR #113/#114 merged), `atlas-v0.10` unchanged, inbox 7/7 closed.
**Goal / current question:** Atlas v0.11 as a compaction edition (no source movement, no semantic change): can the file return towards the Method size target under a mechanical preservation contract?
**Last durable work:** `claude/atlas-v0.11-manifest-design`, PR #202 (draft): `tools/atlas_preservation.py` rev. 3 and `records/atlas/ATLAS_V0_11_PRESERVATION_MANIFEST_DESIGN.md` §§7–9. Receiving review: PR #203.
**Decisions held:** order agreed with the PI and the reviewer — tool debt (done: `check_compaction.py` round 4 on `main`) → v0.11 preservation manifest and a D3 pilot → one advisory note to the PI on dormant-owner findings (H2, H11, AZ.A1, H3). Size is an aim, not a gate. `DECLARED` is never `PRESERVED`; grade, qualifier, identifier and diagnostic-class changes are not compaction and need a reviewed stage-1 delta. No up-front normalization of the whole Atlas. #189 deferred. Satellite repository `rtg-sat` is outside the Atlas inputs (Method §3); a one-sentence Method v0.3 delta is planned, separately reviewed.
**Tried and set aside:** the draft-0 extractor (character offsets, feature-list equality as evidence) — replaced; reopen never. Using `check_compaction.py` for the Atlas — set aside, it reads DSN forms only; reopen if the Atlas adopts DSN record syntax.
**Evidence:** `atlas-v0.10` extract: 1,543 regions, 560 typed nodes, 117 diagnostics, 615 raw lines; identity compare 1,427 EXACT. Thirteen identifiers occur on more than one line (design note §7), six of them scientific RIDs in or beside D3.
**Resume:** `python3 -I tools/atlas_preservation.py selftest`; `… extract atlas/RTG_STATE_ATLAS.md OUT.json`; `… compare BASE CAND MAP.json --report R.json`.
**Next 1–3 actions / acceptance:**
1. Reviewer readback of tool rev. 3; acceptance = ACCEPT SCOPED on PR #203, then PI merge of #202/#203.
2. D3 pilot: stage-1 dispositions for the duplicate identifiers it touches, compaction with a movement map, comparator report with 0 FAIL, and every pending item and context review listed for the change-focused review. The comparator is not used as an acceptance gate before step 1.
3. Advisory note to the PI on dormant-owner findings; "accept the recorded state" there means deferring a known debt, not resolving it.
**Reopen trigger:** any owner tag after `fa3db80` (impact refresh takes precedence over compaction); any open item in `pipes/ATLAS/`.

## REVIEWER_LANE — ChatGPT

Checked 9 November 2026: independently verified #195/#196/#188 merges and main `53e412544ae53e3d657a2ef446493f73fe865c9f`; read merged CONVENTIONS §9 and the entry note. PI supplied a successful live native reporter run; this reviewer did not execute it. Held decisions: Atlas pilot accepted; #189 deferred; #113/#114 remain separate tool work. No active reviewer branch. Prior review/evidence is merged under `records/atlas/ATLAS_ORIENTATION_PILOT_RECEIVING_CHATGPT_20261109.md`; do not reopen completed scoring or reporter correction rounds. Next: one maintenance-diff review; then assess the first fresh-session native invocation when prerequisites exist, with connector mode supported when they do not.

*(Text supplied by the reviewer in PR #188 comment 6739968719 and installed unchanged by the owner at the reviewer's request.)*

## PI_PENDING — maintained by owner

**Open with the PI (10 November 2026):**
- PR #202 (tool and design note) and PR #203 (its receiving review) → merge after the reviewer's acceptance of tool rev. 3. No CLI block issued yet.
- F4: one fresh AI session with `gh` and a clone runs the reporter from the BOOTSTRAP message; still open, not blocking.
- CONVENTIONS §9 is generalized (PR #198); follow-up notes on its length, a BASELINE "Entry note" column and the definition of an active stream are with the reviewer, no PI action yet.

The owner records later PI requests and issued CLI blocks here with their exact source.

Checkpoint triggers: a decision, a counterexample or new result, a rejected approach, a completed long computation, a blocker, or imminent context loss — not message counts and not every PR-state change. A pushed commit on an authorized co-owner branch with a discoverable PR is durable but unadopted. Keep detail in the owner's records; this note links to them.
