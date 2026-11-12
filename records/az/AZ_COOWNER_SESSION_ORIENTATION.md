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
| Action 1 (token resonance): registration, Stage 1 data, report | `records/az/AZ_TOKEN_RESONANCE_PREREGISTRATION.md`; `upload/az-token-resonance-stage1/`; `records/az/AZ_TOKEN_RESONANCE_STAGE1_REPORT.md` (results §§4–6, scope §7, review, PI outcome rule and merges §11); offer to TDR-G `pipes/TDRG/20261112-AZ-token-alphabet-law-offer.md`. All [SESSION]; nothing of it is in the AZ DSN |
| Running work | the lanes below and the open PRs the reporter lists |
| Atlas advisories concerning AZ (noncanonical; the owner decides) | `records/atlas/ATLAS_ADVISORY_TO_PI_DORMANT_OWNERS_20261110.md`, `records/atlas/ATLAS_ADVISORY_AZ_STATE_20261111.md` |

Reactivation history: the four staged bootstrap messages of 10 November are done (entry and reading; triage, PR #207; corrections edition, PR #208, tag `az-v0.7`; frontier advisory, which led to Action 1). Their text is in Git history.

## BOOTSTRAP — first message for a fresh AZ session

> Act as AZ co-owner (stream: Arithmetic Resonance and Zeta). From GitHub `MustafaAksu/rtg-corpus`, read `CONVENTIONS.md` and `records/az/AZ_COOWNER_SESSION_ORIENTATION.md`. Verify governing sources and live work; report gaps and next actions. Temporary files/clones, hashes and the reviewed reporter are permitted within normal permissions. Use connector queries when unavailable. During entry, do not modify shared content, push, merge, tag, change pipes or adopt. Do not rely on memory of earlier chats.

## OWNER / CO-OWNER LANES

*(Each session writes its own lane under its own heading with a check stamp: goal, last durable work, decisions held, tried and set aside, evidence, resume, next 1–3 actions, reopen trigger.)*

### CO-OWNER LANE — Claude

**Checked:** 12 November 2026, 11:30 +03:00; `main` `ffaf5e7`; tag `az-v0.7` → `b1c30b7`, file `2294d2a3…fc94`, `BASELINE.md` AZ row unchanged; `pipes/AZ/` two items, both closed; outbound: notices `20261111-AZ-v0-7-adopted.md` — DYAD and ATLAS closed (accept), TDRG, PROG and DZT open; offer `pipes/TDRG/20261112-AZ-token-alphabet-law-offer.md` open; AZ PRs #211, #227, #230, #228 merged by the PI on 12 Nov (`07a20c1`, `a36404c`, `16d28fa`, `082f702`); the only open AZ PR is the one carrying this update.
**Shared sections:** maintained by this lane since the PI's decision of 11 Nov, 18:15 +03:00 (Atlas advisory §5, row 6); updated here: the Thread C row and the Action 1 row of "Where things are", and PI_PENDING.
**Goal / current question:** AZ Action 1 — does the tail of `bound_symmetric` runs depend on a seed token with `4x ≡ 0 (mod N)`. Stage: Stage 1 is closed as session work — run, reported, reviewed (`5869662603`, accepted, scoped) and merged; both confirmatory contrasts read *supported, unqualified*. The result is in no DSN. The mechanism is OPEN.
**Last durable work:** `records/az/AZ_TOKEN_RESONANCE_STAGE1_REPORT.md` §11 (review, PI outcome rule, merges); the offer to TDR-G (PR #230); before them the report itself and `evidence/az/token_resonance/stage1/` (verification script, rerun outputs, byte-identical to the campaign machine's). Before it: Thread C partial recovery (PRs #221, #222, merged; `records/az/AZ_UPLOAD_HASH_CHECK_20261111.md`); preregistration draft r2 (PR #211, reviews `5855522171`, `5857601141`); triage (PR #207), AZ v0.7 (PR #208), notices (PR #209).
**Decisions held:** PI, 11 Nov: Action 1 is the next AZ study; large computations run on the PI's Ubuntu server, not in an AI session (14:02 +03:00); full authority to this lane for depositing the recovered Thread C files (16:41 +03:00); the six rows of the Atlas advisory §5 (18:15 +03:00). PI, 12 Nov: outcome rule for Action 1, confirmed after Stage 1 ("Metni onaylıyorum"; GitHub comment `6817166013` on PR #228; wording in the report §11 item 3) — a supported contrast is *eligible* for a PI-approved `[NUM diagnostic]` entry in AZ Level A and is offered to TDR-G; it closes no AZ-OPEN-PROMO, promotes no maturity, is no TDR-G claim. Earlier: the six triage decisions; "AZ v0.7 benimsiyorum"; Methodology v1.2 stays declared until the v0.8 edition.
**Tried and set aside:** five seed covariates fixed before the pilot — not significant on 252 runs. Explanations by the arithmetic of `N` are `[FAIL]` at the owner (TDR-G §6.9). Snapshot graph statistics as a dynamical observable — a defect graph is a function of the phase occupancy alone (`[SESSION]`). Plain Wald interval; "interval contains zero" as neutrality; detuned arm against `BASE` on all draws as a control (the registered run shows the predicted bias: −0.013, interval excluding zero, while the eligible-draw control reads equivalent); a hand-written worker loop in PowerShell. A server block that used the working tree of `~/rtg-corpus` — it is not clean; the campaign runs in a separate worktree.
**Evidence:** `evidence/az/token_resonance/SHA256SUMS` (SHA-256 `81c87dcf…d6eb`); `upload/az-token-resonance-stage1/HASHES.txt` and `CAMPAIGN_COMPLETE.json`; `evidence/az/token_resonance/stage1/verify_output.txt`; pilot provenance `evidence/az/token_resonance/pilot/PROVENANCE.md`; `upload/az-records/` with `evidence/az/az_v5_replay/`.
**Resume:** the LIVE_STATE command above; then the Stage 1 report §7 and §11; `bash evidence/az/token_resonance/stage1/verify.sh` (expected last line `VERIFY PASS`); the state of the two AZ items in `pipes/TDRG/`.
**Next 1–3 actions / acceptance:**
1. AZ v0.8 by the usual release cycle (Atlas advisory §5 row 5; Stage 1 is closed): Programme §6.7 reduction with the Methodology v1.4 migration; the corrected availability statement of §9 for the recovered Thread C files; the two `G_birth(w)` definitions and the identifier `TDRG-AZ-EXPORT-BASELINE`; and, only by a separate PI decision under the outcome rule, a `[NUM diagnostic]` entry for PC1/PC2 with the scope of the report §7. Acceptance: branch, PR, review, PI decision, release record; the PI merges and tags. Waits for the PI's word to start.
2. Offer of the Stage 1 numerical result to TDR-G as a separate item in `pipes/TDRG/` (the outcome rule says it is offered; the filed item covers Propositions 1–3 only). Acceptance: `tools/pipes_index.py --check` passes; the item cites the report on `main`.
3. Stage 2 (`N = 240, 242, 480`) and Stage 3 (TDR-26 in its own scope, with TDR-G) are proposals (preregistration §10): each needs a design decision by the PI and its own registration before any run; large runs go to the PI's server.
**Reopen trigger:** a review point on the Stage 1 report; a TDR-G decision on its engine or orientation profile, on `TDRG-OPEN-SPECCONS-STAR` or on TDR-26; further Thread C files found; a new item in `pipes/AZ/`; a receiver's disposition on one of the notices that asks AZ for something.

## PI_PENDING

- **Decided by the PI, 11 Nov 2026, 18:15 +03:00:** all six recommendations of `records/atlas/ATLAS_ADVISORY_AZ_STATE_20261111.md` accepted (its §5). State on 12 Nov, 11:30 +03:00: row 1 (outcome rule) — confirmed by the PI on 12 Nov, after Stage 1, not before it as the row asked (report §11 item 3); row 2 (TDR-G offer) — filed and merged, PR #230; row 3 — PR #211 merged on 12 Nov, after the run, and no authorisation naming the bytes is on record; row 4 (Thread C evidence) — partial recovery merged (PRs #221, #222), further files not found so far; row 5 (v0.8) — Stage 1 is closed, the edition has not been started; row 6 (shared sections) — in effect.
- **Open with the PI:** the start of the v0.8 cycle and whether the Action 1 diagnostic enters it; whether the Stage 1 numerical result is offered to TDR-G now, as a separate pipe item; whether to record an authorisation of Stage 1 naming the bytes after the fact; Stage 2 and Stage 3.
- No CLI block is pending for AZ in this note; blocks issued by a co-owner are recorded in that co-owner's lane.
