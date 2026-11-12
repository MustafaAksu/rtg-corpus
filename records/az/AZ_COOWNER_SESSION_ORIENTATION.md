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
| Thread C evidence: as adopted, not in the repository (AZ DSN §9; release record §14). Since 11 Nov a partial recovery is on `main`: `upload/az-records/` (registry and nine of its ten entries, exporter, conventions file, one Phase-2 smoke report), checked and replayed in `records/az/AZ_UPLOAD_HASH_CHECK_20261111.md`; §9 stands until an AZ edition changes it | `records/az/AZ_UPLOAD_HASH_CHECK_20261111.md` §§5–7 |
| Action 1 (token resonance): registration, Stage 1 data, report | `records/az/AZ_TOKEN_RESONANCE_PREREGISTRATION.md`; `upload/az-token-resonance-stage1/`; `records/az/AZ_TOKEN_RESONANCE_STAGE1_REPORT.md` (each on `main` only once its PR is merged) |
| Running work | the lanes below and the open PRs the reporter lists |
| Atlas advisories concerning AZ (noncanonical; the owner decides) | `records/atlas/ATLAS_ADVISORY_TO_PI_DORMANT_OWNERS_20261110.md`, `records/atlas/ATLAS_ADVISORY_AZ_STATE_20261111.md` |

Reactivation history: the four staged bootstrap messages of 10 November are done (entry and reading; triage, PR #207; corrections edition, PR #208, tag `az-v0.7`; frontier advisory, which led to Action 1). Their text is in Git history.

## BOOTSTRAP — first message for a fresh AZ session

> Act as AZ co-owner (stream: Arithmetic Resonance and Zeta). From GitHub `MustafaAksu/rtg-corpus`, read `CONVENTIONS.md` and `records/az/AZ_COOWNER_SESSION_ORIENTATION.md`. Verify governing sources and live work; report gaps and next actions. Temporary files/clones, hashes and the reviewed reporter are permitted within normal permissions. Use connector queries when unavailable. During entry, do not modify shared content, push, merge, tag, change pipes or adopt. Do not rely on memory of earlier chats.

## OWNER / CO-OWNER LANES

*(Each session writes its own lane under its own heading with a check stamp: goal, last durable work, decisions held, tried and set aside, evidence, resume, next 1–3 actions, reopen trigger.)*

### CO-OWNER LANE — Claude

**Checked:** 12 November 2026, 08:25 +03:00; `main` `3bc5202`; tag `az-v0.7` → `b1c30b7`, file `2294d2a3…fc94`; `pipes/AZ/` two items, both closed; outbound notices `20261111-AZ-v0-7-adopted.md`: DYAD closed (accept; asks AZ for nothing), ATLAS dispositioned, TDRG, PROG and DZT open; open AZ PRs: #211 (registration, head `47dee46`), #227 (custody of `upload/az-token-resonance-stage1`, head `95db7af`), #228 (this lane with the Stage 1 report) and #230 (the offer to TDR-G, `pipes/TDRG/20261112-AZ-token-alphabet-law-offer.md`, open in the queue once merged).
**Shared sections:** maintained by this lane since the PI's decision of 11 Nov, 18:15 +03:00 (Atlas advisory §5, row 6); updated here: the Thread C row and the Action 1 row of "Where things are", and PI_PENDING.
**Goal / current question:** AZ Action 1 — does the tail of `bound_symmetric` runs depend on a seed token with `4x ≡ 0 (mod N)`. Stage: Stage 1 is run and reported; both confirmatory contrasts read *supported, unqualified* in the registered analysis; the report waits for the second co-owner's independent rerun and for the PI.
**Last durable work:** `records/az/AZ_TOKEN_RESONANCE_STAGE1_REPORT.md`; `evidence/az/token_resonance/stage1/` (verification script, rerun outputs, byte-identical to the campaign machine's). Before it: Thread C partial recovery (PRs #221, #222, merged; `records/az/AZ_UPLOAD_HASH_CHECK_20261111.md`); preregistration draft r2 (PR #211, reviews `5855522171`, `5857601141`); triage (PR #207), AZ v0.7 (PR #208), notices (PR #209).
**Decisions held:** PI, 11 Nov: Action 1 is the next AZ study; large computations run on the PI's Ubuntu server, not in an AI session (14:02 +03:00); full authority to this lane for depositing the recovered Thread C files (16:41 +03:00); the six rows of the Atlas advisory §5 (18:15 +03:00). Earlier: the six triage decisions; "AZ v0.7 benimsiyorum"; Methodology v1.2 stays declared until the v0.8 edition.
**Tried and set aside:** five seed covariates fixed before the pilot — not significant on 252 runs. Explanations by the arithmetic of `N` are `[FAIL]` at the owner (TDR-G §6.9). Snapshot graph statistics as a dynamical observable — a defect graph is a function of the phase occupancy alone (`[SESSION]`). Plain Wald interval; "interval contains zero" as neutrality; detuned arm against `BASE` on all draws as a control (the registered run shows the predicted bias: −0.013, interval excluding zero, while the eligible-draw control reads equivalent); a hand-written worker loop in PowerShell. A server block that used the working tree of `~/rtg-corpus` — it is not clean; the campaign runs in a separate worktree.
**Evidence:** `evidence/az/token_resonance/SHA256SUMS` (SHA-256 `81c87dcf…d6eb`); `upload/az-token-resonance-stage1/HASHES.txt` and `CAMPAIGN_COMPLETE.json`; `evidence/az/token_resonance/stage1/verify_output.txt`; pilot provenance `evidence/az/token_resonance/pilot/PROVENANCE.md`; `upload/az-records/` with `evidence/az/az_v5_replay/`.
**Resume:** the LIVE_STATE command above; then the Stage 1 report §§8–10 and the state of the three AZ PRs; `bash evidence/az/token_resonance/stage1/verify.sh`.
**Next 1–3 actions / acceptance:**
1. Independent rerun and review of the Stage 1 report by the second co-owner; PI confirmation of the outcome rule (report §9). Acceptance: `VERIFY PASS` on the reviewer's side; the PI's wording recorded.
2. The offer to `pipes/TDRG/` (PI decision, Atlas advisory §5 row 2) is filed as PR #230: Propositions 1–3 only, cited at commit `47dee46`; `tools/pipes_index.py --check` passes. It reaches the TDR-G inbox when the PI merges it (after #211, so that the cited paths are on `main`). The Stage 1 numerical result is not in it; a separate item follows the outcome rule once the PI has confirmed one.
3. After Stage 1 is closed: AZ v0.8 by the usual release cycle — Programme §6.7 reduction with the Methodology v1.4 migration (row 5), the corrected availability statement of §9 for the recovered Thread C files, the two `G_birth(w)` definitions and the identifier `TDRG-AZ-EXPORT-BASELINE`, and, by the PI's decision, the Action 1 diagnostic. Stage 2 and Stage 3 of Action 1 are proposals that need design decisions first.
**Reopen trigger:** a review point on the Stage 1 report; a TDR-G decision on its engine or orientation profile, on `TDRG-OPEN-SPECCONS-STAR` or on TDR-26; further Thread C files found; a new item in `pipes/AZ/`; a receiver's disposition on one of the notices that asks AZ for something.

## PI_PENDING

- **Decided by the PI, 11 Nov 2026, 18:15 +03:00:** all six recommendations of `records/atlas/ATLAS_ADVISORY_AZ_STATE_20261111.md` accepted (its §5). State on 12 Nov: row 4 (Thread C evidence) started — partial recovery merged (PRs #221, #222); row 6 (shared sections) in effect; row 5 (v0.8) waits for the close of Stage 1; row 2 (TDR-G offer) filed as PR #230, waiting for the PI's merge.
- **Rows 1 and 3 could not be met as worded:** Stage 1 had been started by the PI at about 14:17 +03:00 and resumed at 16:36 +03:00, before the decision; it finished at 21:11 +03:00 and is uploaded. See `records/az/AZ_TOKEN_RESONANCE_STAGE1_REPORT.md` §8.
- **Open with the PI:** the outcome rule for Action 1 — the report (§9) proposes the wording the Atlas advisory gave before any analysis existed; whether to record an authorisation of Stage 1 naming the bytes after the fact; the merge order — proposed #211 (registration), #227 (custody), #228 (report), #230 (offer); Stage 2 and Stage 3.
- No CLI block is pending for AZ in this note; blocks issued by a co-owner are recorded in that co-owner's lane.
