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

**Checked:** 11 November 2026, 13:30 +03:00; `main` `42ffb9e` (since `f540e4f`: LIT and DYAD pipe and record changes only; no AZ path except the DYAD disposition below); tag `az-v0.7` → `b1c30b7`, file `2294d2a3…fc94`; `pipes/AZ/` two items, both closed; outbound notices `20261111-AZ-v0-7-adopted.md`: DYAD closed (11 Nov · accept · `records/dyad/DYAD_INBOX_20261111_OWNER_DISPOSITION.md`; it asks AZ for nothing), TDRG, PROG, ATLAS and DZT open, no disposition; open PRs #215, #213, #189, #183, #160 touch no AZ path; PR #211 (branch `claude/az-token-resonance-prereg`, based on `f540e4f`) carries this lane and the Action 1 package.
**Shared sections above are stale since the tag** (ENTRY names `az-v0.6`; reading list, inbox line and BOOTSTRAP describe the state before v0.7). They are owner-maintained (CONVENTIONS §9) and are not edited by this lane; the PI kept their maintenance outside Action 1 (11 Nov). The governing edition is `az-v0.7` with `records/az/AZ_v0_7_RELEASE_RECORD.md`.
**Goal / current question:** AZ Action 1 of the BOOTSTRAP 4 advisory (PI message of 11 Nov, 10:00 +03:00, relaying the task text "Proceed with AZ Action 1 — Token Resonance and Basin Selection, as selected by the PI"): does the tail of `bound_symmetric` runs depend on a seed token with `4x ≡ 0 (mod N)`, tested by one-token interventions on the pinned TDR-G engine. Stage: preregistration draft r2 accepted (scoped) by the reviewer's readback `5857601141` (R1–R4 closed; two non-blocking notes, disposed in the preregistration §12); Stage 1 waits for the PI's authorisation; no confirmatory run exists.
**Last durable work:** `records/az/AZ_TOKEN_RESONANCE_PREREGISTRATION.md` (draft r2, amendment log §12); scripts `evidence/az/scripts/az_tokres_{run,analyse,fixtures,negcontrols,campaign}.py`; fixtures, negative-control output, test campaign and frozen pilot under `evidence/az/token_resonance/`. Before it: triage (PR #207), AZ v0.7 (PR #208, tag `az-v0.7`), notices (PR #209).
**Decisions held:** 11 Nov, the same message: Action 1 is the next AZ study; a large campaign only after independent review and PI authorisation; no DSN edit, no adoption, no pipe closure. Earlier: the six triage decisions; "AZ v0.7 benimsiyorum"; Methodology v1.2 stays declared, the v1.4 migration is a separate edition.
**Tried and set aside:** five seed covariates fixed before the pilot (equal/opposite seeds, slow tokens, first-return time, bindable differences and sums) — not significant on 252 runs. Deterministic explanations by the arithmetic of `N` are `[FAIL]` at the owner (TDR-G §6.9). Snapshot graph statistics as a dynamical observable — set aside: a defect graph is a function of the phase occupancy alone (advisory, `[SESSION]`). A plain Wald interval for the paired contrast — zero width without discordant pairs; replaced by Agresti–Min before registration. "The interval contains zero" as a neutrality criterion, and the detuned arm against `BASE` on all base draws as a neutrality control (not neutral by construction: the native slot token is resonant in about 3 % of the draws) — both replaced in r2 by margin-based control contrasts on eligible draws. A hand-written PowerShell loop over workers — replaced by a tested Python driver that enforces exit codes.
**Evidence:** `evidence/az/token_resonance/SHA256SUMS`; pilot provenance `evidence/az/token_resonance/pilot/PROVENANCE.md` (exploratory, seeds 5551 and 20261111 spent); fixtures output `evidence/az/token_resonance/fixtures/`. The Thread C files of AZ §9 remain absent from the repository.
**Resume:** the LIVE_STATE command above with `az-v0.7`; then the preregistration §12 (amendment log) and the state of its PR and review.
**Next 1–3 actions / acceptance:**
1. PI decision on Stage 1. Venue: the PI's Ubuntu server (PI, 11 Nov, 14:02 +03:00: large computations run there, not in an AI session); one bash block, preregistration §8, `JOBS=4`, same value on `--resume`.
2. After the run: directory arrives unchanged on `upload/az-token-resonance-stage1`; hash check against `HASHES.txt`; placement under `evidence/az/token_resonance/stage1/`; registered analysis rerun from the placed files by both co-owners; report with the PC3 wording erratum (N1). Acceptance: `CAMPAIGN_COMPLETE.json`; integrity and gates G1–G2 pass on rerun; output verbatim with qualifiers G3–G5.
3. On the PI's decision: file the offer to `pipes/TDRG/` drafted in the preregistration §11 (the reviewer recommends filing; not an authorisation). Carried, separate: Thread C evidence recovery; Methodology v1.4 migration; Programme §6.7 restructuring.
**Reopen trigger:** a review point that changes §§4–6 of the preregistration; a TDR-G decision on its engine or orientation profile, on `TDRG-OPEN-SPECCONS-STAR` or on TDR-26; a new item in `pipes/AZ/`; a receiver's disposition on one of the five notices that asks AZ for something.

## PI_PENDING

- **Decided by the PI, 11 Nov 2026, 18:15 +03:00:** all six recommendations of `records/atlas/ATLAS_ADVISORY_AZ_STATE_20261111.md` accepted (its §5): outcome rule for Action 1 before Stage 1; file the TDR-G offer now; merge PR #211 before the run and name the authorized bytes; Thread C evidence before any further edition; v0.8 = Programme §6.7 reduction + Methodology v1.4 migration after Stage 1; the shared sections of this note pass to the AZ co-owner holding the working lane (Claude).
- **Still open with the PI:** confirmation of the outcome-rule wording once drafted; the authorization of Stage 1 naming the bytes.
- No CLI block is pending for AZ in this note; blocks issued by a co-owner are recorded in that co-owner's lane.
