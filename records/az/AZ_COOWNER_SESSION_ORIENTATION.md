# AZ — Co-owner Session Orientation

**[SESSION] Operational working memory of the AZ stream (Arithmetic Resonance and Zeta); no scientific or release authority.** Created 10 November 2026 by the Atlas owner (Claude) at the PI's request to reactivate the stream. Shared sections brought to the post-v0.7 state by the same drafter on 11 November 2026 (PI request for an Atlas review; `records/atlas/ATLAS_ADVISORY_AZ_STATE_20261111.md`). From the AZ co-owner's next checkpoint the shared sections are maintained by the co-owner holding the working lane (Claude; PI decision of 11 Nov 2026, 18:15 +03:00).
**Owner per `BASELINE.md`:** PI. Each co-owner edits only its own lane.

## ENTRY — discovery and authority

Read **from GitHub**, repository `MustafaAksu/rtg-corpus`, fixed path `records/az/AZ_COOWNER_SESSION_ORIENTATION.md` on `main`; project synchronization does not include `records/`, `pipes/`, `evidence/` or `tools/`. Start with `CONVENTIONS.md`, this note, `BASELINE.md` and `pipes/AZ/INDEX.md`. Failure to access a source means **UNVERIFIED**, not an empty queue.

The governing AZ edition is the newest adopted tag with its release record; on 11 November 2026 that is `az-v0.7` with `records/az/AZ_v0_7_RELEASE_RECORD.md` (corrections only; declares Methodology v1.2, names v1.4 as governing; migration not done). Verify it yourself with the command below. Memory of earlier chats, project copies and file headers are not authority.

## LIVE_STATE — generated, never copied here

`git fetch origin --tags && python3 -I tools/orient.py AZ --tag-prefix az-v --file dsn/RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN.md --paths dsn/RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN.md records/az pipes/AZ evidence/az --record-glob 'records/az/AZ_v*_RELEASE_RECORD.md'`
Without `--record-glob` the reporter prints "release record: None" although the record exists (no built-in AZ profile). Without a shell: obtain the same facts (tag, file hash, open PRs touching these paths, `pipes/AZ/` states, the AZ notices in other inboxes) through the GitHub connection and say what could not be covered.

## WHERE THINGS ARE

| Topic | Home |
|---|---|
| What changed around AZ between June 2026 and v0.7, row by row, with the PI's scope decisions | `records/az/AZ_REACTIVATION_TRIAGE.md` |
| What v0.7 changed, what it kept on purpose, what it did not do, open items carried forward | `records/az/AZ_v0_7_RELEASE_RECORD.md` §§3, 6, 11, 14 |
| Thread C evidence: not in the repository (`EV-SRC-REPORTED`, `EV-NOT-RERUN`) | AZ DSN §9; release record §14 |
| Running work | the lanes below and the open PRs the reporter lists |
| Atlas advisories concerning AZ (noncanonical; the owner decides) | `records/atlas/ATLAS_ADVISORY_TO_PI_DORMANT_OWNERS_20261110.md`, `records/atlas/ATLAS_ADVISORY_AZ_STATE_20261111.md` |

Reactivation history: the four staged bootstrap messages of 10 November are done (entry and reading; triage, PR #207; corrections edition, PR #208, tag `az-v0.7`; frontier advisory, which led to Action 1). Their text is in Git history.

## BOOTSTRAP — first message for a fresh AZ session

> Act as AZ co-owner (stream: Arithmetic Resonance and Zeta). From GitHub `MustafaAksu/rtg-corpus`, read `CONVENTIONS.md` and `records/az/AZ_COOWNER_SESSION_ORIENTATION.md`. Verify governing sources and live work; report gaps and next actions. Temporary files/clones, hashes and the reviewed reporter are permitted within normal permissions. Use connector queries when unavailable. During entry, do not modify shared content, push, merge, tag, change pipes or adopt. Do not rely on memory of earlier chats.

## OWNER / CO-OWNER LANES

*(Each session writes its own lane under its own heading with a check stamp: goal, last durable work, decisions held, tried and set aside, evidence, resume, next 1–3 actions, reopen trigger.)*

### CO-OWNER LANE — Claude

**Checked:** 11 November 2026, 09:30 +03:00; `main` `b1c30b7`; tag `az-v0.7` (annotated, object `b29d57f`) → merge commit `b1c30b7`, file `2294d2a3…fc94`, equal to `BASELINE.md` and to the release record; `pipes/AZ/` two items, both closed on branch `claude/az-v0.7-notices`; no other open PR or branch on AZ paths.
**Shared sections above are stale since the tag** (ENTRY still names `az-v0.6` as governing; the reading list and the inbox line describe the state before v0.7; BOOTSTRAP 1–3 are done). They are owner-maintained (CONVENTIONS §9) and are not edited by this lane. Until the owner updates them, the governing edition is `az-v0.7` with `records/az/AZ_v0_7_RELEASE_RECORD.md`.
**Goal / current question:** BOOTSTRAP 4 — state the AZ frontier as it stands after v0.7 and propose the next one to three actions. Not started; it waits for the PI's message.
**Last durable work:** triage `records/az/AZ_REACTIVATION_TRIAGE.md` (PR #207, merged `f5e548e`). AZ v0.7, corrections only (PR #208, merged `b1c30b7`): builder `evidence/az/scripts/build_az_v0_7.py`, 59 logged edits, gates 7/7, controls 4/4; ChatGPT reviews `5854287756` (two minor corrections, applied) and `5854348724` (accepted); adopted by the PI on 11 Nov 2026 (release record §13). Post-tag: five notices `pipes/{TDRG,DYAD,PROG,ATLAS,DZT}/20261111-AZ-v0-7-adopted.md` and the two inbox items closed, branch `claude/az-v0.7-notices`.
**Decisions held:** PI, 10 Nov: AZ reactivated, advisory row 1 first; the six triage decisions (triage §7). PI, 11 Nov 08:52: "AZ v0.7 benimsiyorum" (adopted bytes `2294d2a3…fc94`). Methodology v1.2 stays declared in v0.7; the v1.4 migration is a separate, PI-decided edition.
**Tried and set aside:** comparing AZ with the editions v0.6 pinned (Dyadic v6.4.8.1, TDR-G v2.12, Genesis v2.8.4, Programme v1.1, OPEN-M v0.6) — not possible, they are not in the repository; no longer load-bearing after v0.7. Nothing was computed in this cycle.
**Evidence:** release record §2 (hashes), §4 (gates, controls), §6 (exceptions kept, including the unverified two-component description of the degree-2 $q=3$ cancellation). The Thread C files of AZ §9 are absent from the repository; PI, 10 Nov: they may exist locally and were not located.
**Resume:** the LIVE_STATE command above with `az-v0.7`; then `pipes/AZ/INDEX.md` and the five outbound notices' states.
**Next 1–3 actions / acceptance:**
1. Merge of the notices PR by the PI (merge commit; no tag). Acceptance: `tools/pipes_index.py --check` passes on `main`.
2. BOOTSTRAP 4 on the PI's message: the AZ frontier after v0.7 (release record §14: evidence recovery; Methodology v1.4 migration; Programme §6.7 restructuring; AZ-2) with one to three proposed actions and acceptance criteria. No edit before the PI decides.
3. When the PI locates the Thread C files: unchanged on an `upload/…` branch, hash check against `AZ-ART-AZV5-REGISTRY`, placement under `evidence/az/`.
**Reopen trigger:** a new item in `pipes/AZ/`; a new owner tag of Dyadic, TDR-G, Genesis, Programme or OPEN-M that changes a statement AZ §8 imports; a receiver's disposition on one of the five notices that asks AZ for something.

## PI_PENDING

- **Decided by the PI, 11 Nov 2026, 18:15 +03:00:** all six recommendations of `records/atlas/ATLAS_ADVISORY_AZ_STATE_20261111.md` accepted (its §5): outcome rule for Action 1 before Stage 1; file the TDR-G offer now; merge PR #211 before the run and name the authorized bytes; Thread C evidence before any further edition; v0.8 = Programme §6.7 reduction + Methodology v1.4 migration after Stage 1; the shared sections of this note pass to the AZ co-owner holding the working lane (Claude).
- **Still open with the PI:** confirmation of the outcome-rule wording once drafted; the authorization of Stage 1 naming the bytes.
- No CLI block is pending for AZ in this note; blocks issued by a co-owner are recorded in that co-owner's lane.
