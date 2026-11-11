# DYAD — Co-owner Entry Note

**[SESSION] Operational working memory of the Dyadic stream (CONVENTIONS §9). No scientific or release authority.** Created 11 November 2026 by the Dyadic DSN owner (Claude). The shared sections are owner-maintained; each co-owner edits only its own lane.
**Owner/editor and math auditor:** Claude. **Co-owner:** ChatGPT. **Final authority:** the PI. (Roles as assigned by the PI in the project sessions; `BASELINE.md` names no owner. The v6.4.23 release record and the inbox records were written under these roles.)

## ENTRY — discovery and authority

Read **from GitHub**, repository `MustafaAksu/rtg-corpus`, fixed path `records/dyad/DYAD_COOWNER_ENTRY_NOTE.md` on `main`. Project synchronization does not include `records/`, `pipes/`, `evidence/` or `tools/`. Start with `CONVENTIONS.md`, this note, `BASELINE.md` and `pipes/DYAD/INDEX.md`. Failure to access a source means **UNVERIFIED**, not an empty queue.

The governing edition is the newest **adopted** tag with its release record. At the time of writing: v6.4.24, adopted by the PI on 11 November 2026, file `dsn/RTG_DYADIC_OSCILLATOR_DSN.md`, SHA-256 `10fbdacc19544596480acae03faeba076f21103a01b903a8d3305cfa8ed7bc16`, release record `records/dyad/RTG_DYADIC_v6_4_24_RELEASE_RECORD.md`; its tag `dyad-v6.4.24` is created by the PI after the merge of PR #213. Until that tag exists, `dyad-v6.4.23` (`9f874ccc…25cb`) is the newest tag. Recheck; do not trust this line.

`records/dyad/DYAD_OWNER_ENTRY_NOTE_INBOX_20261030.md` is the note of one closed inbox round. It is history, not a second entry point.

## LIVE_STATE — generated, never copied here

`git fetch origin --tags && python3 -I tools/orient.py DYAD --tag-prefix dyad-v --file dsn/RTG_DYADIC_OSCILLATOR_DSN.md --paths records/dyad evidence/dyad pipes/DYAD`
Without a shell: obtain the same facts (tag, file hash, open PRs touching these paths, `pipes/DYAD/` states, DYAD's outgoing items in other inboxes) through the GitHub connection, and say what could not be covered. LIT work for DYAD lives in the private repository `MustafaAksu/rtg-lit`; DYAD uses LIT only through `pipes/LIT/` (PI rule, 3 Nov 2026).

## STREAM MAP — where the current work lives

| Thread | Records | State |
|---|---|---|
| v6.4.24 maintenance edition | `records/dyad/DYAD_v6_4_24_BACKLOG.md`; draft release record `records/dyad/RTG_DYADIC_v6_4_24_RELEASE_RECORD.md`; branch `claude/dyad-v6.4.24` | ADOPTED by the PI on 11 Nov 2026 (`10fbdacc…bc16`); r1 review `5856200509`, r2 read-back `5857204402`; merge and tag by the PI pending; post-tag read-back and notices pending |
| S1, OPEN 21 on the sharpened R9 rows | `records/dyad/DYAD_S1_OPEN21_SHARP_ROWS_DESIGN.md`; `evidence/dyad/s1-open21-sharp/` | accepted by the co-owner; enters v6.4.24 as `DYAD-THM-OPEN21-SHARP-ROWS` |
| OPEN 20 analytic branch, sectorial pilot | `records/dyad/DYAD_OPEN20_AN_SECTORIAL_PILOT_DESIGN.md` (§7 stage 1, §8 stage 3a, §9 inputs to 3b); `…_STAGE2_SCOUTING_NUM.md`; `…_STAGE2B_JUMP_SCOUTING_NUM.md`; `…_LH2012_OWNER_ASSESSMENT.md` (§5, §6); `DYAD_OWNER_REVIEW_OPEN20_BOUNDS_PREFLIGHT.md` | stage 3a done, negative; stage 2b done (`[NUM]`: jump numerically nonzero); 3b design not written; 3c not authorized |
| Inbox rounds | `DYAD_OWNER_DISPOSITION_INBOX_20261030.md` with its reconciliation; `DYAD_INBOX_20261111_OWNER_DISPOSITION.md` | both closed |
| Source recovery | `records/dyad/DYAD_SOURCE_RECOVERY_LIST.md`; `DYAD_UPLOAD_HASH_CHECK_*.md` | bridge note placed 3 Nov; the rest still missing |

## OWNER LANE — Claude

**Updated:** 11 November 2026, 12:30 +03:00, after the PI's decisions and stage 2b (branch `claude/dyad-open20-stage2b`). **Checked:** 11 November 2026, 10:40 +03:00; `main` `fe73d56`; tag `dyad-v6.4.23` → `ab8749b`, file hash equal on `main`; `pipes/DYAD/` 16 items, five open before this checkpoint and closed on branch `claude/dyad-checkpoint-20261111`; open PR #183 adds one OFN finding to the inbox.

**Goal / current question.** Two lines of work:
1. publish v6.4.24, a maintenance edition that registers what was accepted since v6.4.23 and records the OPEN 20 pilot's state in the DSN;
2. OPEN 20 B-an: stage 2b is done; write the 3b design note around its numbers.

**Last durable work.**
- v6.4.23 adopted 30 Oct 2026 (PR #132; post-tag record).
- S1 (PR #150), backlog (PRs #148, #156), bridge-note intake (PR #155).
- OPEN 20: stage-3a route check (PR #159), owner review and read-back of the co-owner's bounds preflight (PRs #163, #165, with #157), disposition of LIT INF-014/015 (PR #176).
- This checkpoint: branch `claude/dyad-checkpoint-20261111`. It also carries the unmerged `claude/dyad-inf014-real-slice-note` (real-slice limit of INF-014/015; `[ALG]` candidate P′(u) = α(c₄₀ + μu)).

**Decisions held** (with their evidence):
- PI, 3 Nov 2026: Dyadic work is done in rtg-corpus and its outputs go into the Dyadic DSN; LIT is used only through requests in `pipes/LIT/`.
- PI: OPEN 20 stage 3 is not authorized; N = 432 is deferred (stage-2 adoption, SESSION scope).
- PI, 11 Nov 2026 (in session): start the v6.4.24 candidate now ("başlayalım"); stage 2b authorized ("evet aşama 2b'yi yetkilendiriyorum"). Stage 3c is still not authorized.
- PI, 11 Nov 2026, 13:26 +03:00: "v6.4.24 r2 'yi benimsiyorum" (adopted bytes after the status transform: `10fbdacc…bc16`).
- Co-owner and owner, 11 Nov: the 3b design aims at certifying one jump (\|ξ*\| = 0.40 as a first target); scouting of the second overlap class is not needed now and is not authorized.
- Co-owner and owner, 3 Nov: v6.4.24 carries interface changes and S1; the §1 compaction waits for v6.4.25 or later; S2 (L-PHASE row B) is separate.
- X4, tentative: DYAD RIDs for "not area-preserving" (owner proposal `[ALG]`), the p = 6 linear order and the homological resonance condition; no DYAD RID for the cubic radial rate across p (stays a RECOG import).
- 11 Nov: no DYAD RID for RECOG's c_J and c_7 (disposition record, item 3).
- B-an and B-6 are ACTIVE. No analytic existence or divergence theorem has been claimed.

**Tried and set aside** (do not repeat without a new reason):
- The a-priori operator route of LIT INF-009/010 for the stage-3 enclosure. Best radius 1.4·10⁻¹⁰ at η = π/4, and at most 1.76·10⁻⁶ under Y-scaling for every η (LIT's grid-free bound). Reopen only for a different normalization (larger m) or different operator bounds.
- Reading the stage-2 Borel scale from the coefficients a₂…a₂₁₆: INCONCLUSIVE (`[NUM]`). Stage 2b measured the jump directly and explains it: against the leading time 1/(3\|ξ\|³) the apparent exponent is 1.8–1.9, against the Fatou time the slope tends to 2π. N = 432 is not needed for this question.
- Radii above \|ξ*\| ≈ 0.45 in the stage-2b harness: the start-point search leaves the neighbourhood of 0 (seen at 0.50).
- Using INF-014/015 for real orbits: not possible. On the real slice \|w/z²\| = 1/\|z\| → ∞, so real orbits never approach the lifted points.
- The co-owner's Cauchy-majorant preflight as stage-3 evidence: its constants (K₁ ≈ 2·10⁹ and larger) come from a Cauchy radius of 0.002. It is tooling for E1–E2 only.

**Evidence pointers.** Stage 1: `evidence/dyad/open20-an/stage1_prep.json` (`2c9ae637…4739`). Stage 3a: `evidence/dyad/open20-an/stage3-route/`. INF-014/015 hypotheses: `evidence/dyad/open20-an/lit-inf014-inf015/`. Bridge note: `evidence/dyad/bridge-note-v1-1/`. v6.4.23 build, checks and controls: `evidence/dyad/scripts/*_dyad_v6_4_23*.py` (the pattern to reuse for v6.4.24).

**Resume.** Run LIVE_STATE. Read `DYAD_v6_4_24_BACKLOG.md` §C3 and the design record §9. Then check PI_PENDING below.

**Next 1–3 actions / acceptance:**
1. **v6.4.24 post-tag work** (after the PI's merge and tag): verify the tag, the merge commit and the file hash; write `records/dyad/DYAD_v6_4_24_POST_TAG.md`; file the notices of the release record §7 as pipe items (RECOG, NUMGEN, Triadic, Genesis, OFN, ATLAS, LIT). Acceptance: `tools/pipes_index.py --check` passes; the file at the tag has the adopted hash.
2. **3b design note** for OPEN 20: certificate of Δ ≠ 0 at \|ξ*\| ≈ 0.40–0.45 (stage-2b record §6). First the same scouting on the second overlap class (S₁ ∩ S₂); then the local-enclosure obligation (invariant tube around a truncated series at \|ξ\| ≈ 0.1, to about 10⁻¹⁰). Acceptance: the note states every proof obligation and which are computer-checked; co-owner review; PI decision. No certification run.
3. **Small owner check for AZ:** AZ §4.1.1's two-component description of the degree-2 q = 3 cancellation against `DYAD-ALG-Q3-DEG2-CANCEL`; answer by an item in `pipes/AZ/`.

**Reopen trigger.** A new item in `pipes/DYAD/`; an answer from NUMGEN, OFN or Triadic to the open DYAD notices; a LIT reply on the subpetal request; a new owner tag of RECOG, NUMGEN, OFN, Genesis or Triadic that changes a statement DYAD imports or exports.

## CO-OWNER LANE — ChatGPT

*(Written by the co-owner session under its own check stamp: goal, last durable work, decisions held, tried and set aside, evidence, resume, next 1–3 actions, reopen trigger. Empty until that session fills it.)*

## PI_PENDING

As of 11 November 2026, 13:45 +03:00:
1. **Merge PR #213 and tag `dyad-v6.4.24`** (merge commit; annotated tag on the merge commit). The CLI block was issued in the owner session of 11 November 2026; it checks the file hash `10fbdacc19544596480acae03faeba076f21103a01b903a8d3305cfa8ed7bc16` before tagging.

No other decision is pending.
