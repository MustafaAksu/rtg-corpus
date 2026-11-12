# DYAD — Co-owner Entry Note

**[SESSION] Operational working memory of the Dyadic stream (CONVENTIONS §9). No scientific or release authority.** Created 11 November 2026 by the Dyadic DSN owner (Claude). The shared sections are owner-maintained; each co-owner edits only its own lane.
**Owner/editor and math auditor:** Claude. **Co-owner:** ChatGPT. **Final authority:** the PI. (Roles as assigned by the PI in the project sessions; `BASELINE.md` names no owner. The v6.4.23 release record and the inbox records were written under these roles.)

## ENTRY — discovery and authority

Read **from GitHub**, repository `MustafaAksu/rtg-corpus`, fixed path `records/dyad/DYAD_COOWNER_ENTRY_NOTE.md` on `main`. Project synchronization does not include `records/`, `pipes/`, `evidence/` or `tools/`. Start with `CONVENTIONS.md`, this note, `BASELINE.md` and `pipes/DYAD/INDEX.md`. Failure to access a source means **UNVERIFIED**, not an empty queue.

The governing edition is the newest **adopted** tag with its release record. At the time of writing: v6.4.24, adopted by the PI on 11 November 2026, file `dsn/RTG_DYADIC_OSCILLATOR_DSN.md`, SHA-256 `10fbdacc19544596480acae03faeba076f21103a01b903a8d3305cfa8ed7bc16`, release record `records/dyad/RTG_DYADIC_v6_4_24_RELEASE_RECORD.md`, annotated tag `dyad-v6.4.24` on merge commit `f0af639` (PR #213). Recheck; do not trust this line.

`records/dyad/DYAD_OWNER_ENTRY_NOTE_INBOX_20261030.md` is the note of one closed inbox round. It is history, not a second entry point.

## LIVE_STATE — generated, never copied here

`git fetch origin --tags && python3 -I tools/orient.py DYAD --tag-prefix dyad-v --file dsn/RTG_DYADIC_OSCILLATOR_DSN.md --paths records/dyad evidence/dyad pipes/DYAD`
Without a shell: obtain the same facts (tag, file hash, open PRs touching these paths, `pipes/DYAD/` states, DYAD's outgoing items in other inboxes) through the GitHub connection, and say what could not be covered. LIT work for DYAD lives in the private repository `MustafaAksu/rtg-lit`; DYAD uses LIT only through `pipes/LIT/` (PI rule, 3 Nov 2026).

## STREAM MAP — where the current work lives

| Thread | Records | State |
|---|---|---|
| v6.4.24 maintenance edition | `records/dyad/DYAD_v6_4_24_BACKLOG.md`; draft release record `records/dyad/RTG_DYADIC_v6_4_24_RELEASE_RECORD.md`; branch `claude/dyad-v6.4.24` | ADOPTED by the PI on 11 Nov 2026 (`10fbdacc…bc16`) and tagged; r1 review `5856200509`, r2 read-back `5857204402`; post-tag record `records/dyad/DYAD_v6_4_24_POST_TAG.md`; seven notices filed. Backlog §D carries over |
| S1, OPEN 21 on the sharpened R9 rows | `records/dyad/DYAD_S1_OPEN21_SHARP_ROWS_DESIGN.md`; `evidence/dyad/s1-open21-sharp/` | in the DSN since v6.4.24 as `DYAD-THM-OPEN21-SHARP-ROWS`; offered to RECOG for A1a |
| OPEN 20 analytic branch, sectorial pilot | `records/dyad/DYAD_OPEN20_AN_SECTORIAL_PILOT_DESIGN.md` (§7 stage 1, §8 stage 3a, §9 inputs to 3b); `…_STAGE2_SCOUTING_NUM.md`; `…_STAGE2B_JUMP_SCOUTING_NUM.md`; `…_LH2012_OWNER_ASSESSMENT.md` (§5, §6); `DYAD_OWNER_REVIEW_OPEN20_BOUNDS_PREFLIGHT.md` | stage 3a done, negative; stage 2b done (`[NUM]`: jump numerically nonzero); both LIT literature replies dispositioned (§9); state recorded in the DSN's OPEN 20 entry (v6.4.24); **3b design note r2** (`DYAD_OPEN20_AN_STAGE3B_DESIGN.md`, sampling in `evidence/dyad/open20-an/stage3b-design/`; PR #218): r1 reviewed REVISE (`5858511915`, R1–R5), r2 read back ACCEPT scoped (`5858796744`); **accepted by the PI on 11 Nov 2026 as the basis for the stage-3c certificate design** (note §12); **stage 3c-a authorized by the PI on 11 Nov 2026** (proof record and certificate script, no claim); plan and progress in `DYAD_OPEN20_AN_STAGE3C_A_PLAN.md`; 3c-b (certification run) not authorized; W1–W8 done as development and working records, hand-over in `DYAD_OPEN20_AN_STAGE3C_A_HANDOVER.md`; LIT's reply on L1, L3 accepted as a check of use (SESSION), so condition 1 of the design is met at that scope; LIT's INF-016 (first-harmonic route to B-an, B-6) deferred; the seed (Q1–Q3) and P4 open |
| Inbox rounds | `DYAD_OWNER_DISPOSITION_INBOX_20261030.md` with its reconciliation; `DYAD_INBOX_20261111_OWNER_DISPOSITION.md`; `DYAD_v6_4_24_POST_TAG.md` §3; `DYAD_INBOX_20261112_OWNER_DISPOSITION.md` | all closed |
| Source recovery | `records/dyad/DYAD_SOURCE_RECOVERY_LIST.md`; `DYAD_UPLOAD_HASH_CHECK_*.md` | bridge note placed 3 Nov; the rest still missing |

## OWNER LANE — Claude

**Updated:** 12 November 2026, 18:55 +03:00, with the owner dispositions of the inbox items of 12 Nov (branch `claude/dyad-inbox-20261112-disposition`). **Checked:** 12 November 2026, 18:50 +03:00; `main` `fdc4fc4` (PR #244, W8 r2, merged; co-owner read-back `5877317450`); tag `dyad-v6.4.24` → `f0af639`; `pipes/DYAD/` 20 items, **all closed with this branch** (`DYAD_INBOX_20261112_OWNER_DISPOSITION.md`). Open PR #183 would add one OFN finding. Outgoing, new and open at their receivers: `pipes/LIT/20261112-DYAD-lh2012-use-report.md`, `pipes/AZ/20261112-DYAD-q3-deg2-cancel-owner-check.md`.

**Goal / current question.** OPEN 20 B-an, stage 3c-a: write the proof record and build the certificate script for the tube route at \|ξ*\| = 0.40, with no certification claim. Work packages in `DYAD_OPEN20_AN_STAGE3C_A_PLAN.md`; W1 to W8 are done as development and working records. The hand-over is `DYAD_OPEN20_AN_STAGE3C_A_HANDOVER.md`. Stage 3c-a has no further package; nothing in it is a certificate.

**Last durable work.**
- v6.4.23 adopted 30 Oct 2026 (PR #132; post-tag record).
- S1 (PR #150), backlog (PRs #148, #156), bridge-note intake (PR #155).
- OPEN 20: stage-3a route check (PR #159), owner review and read-back of the co-owner's bounds preflight (PRs #163, #165, with #157), disposition of LIT INF-014/015 (PR #176).
- Checkpoint of 11 Nov (merge `841ed68`): inbox disposition of five items, entry note, real-slice limit of INF-014/015.
- Stage 2b (PR #212). v6.4.24 adopted and tagged 11 Nov 2026 (PR #213).
- Post-tag (PR #216): read-back record, seven notices, disposition of LIT's subpetal reply with an owner check (`evidence/dyad/open20-an/lit-subpetal-reply/`).
- 3b design note with `[NUM]` sampling (PR #218). r1 was reviewed REVISE; r2 has bounded local domains with a guard property, a precise seed, uniqueness through López-Hernanz 2012 Theorem 4.2(3), and the arc and the fibre enclosure as obligations. 16 gates PASS, two negative controls. LIT is asked to validate the use of Theorem 4.2(3) (`pipes/LIT/20261111-DYAD-lh2012-thm42-uniqueness-use.md`).

**Decisions held** (with their evidence):
- PI, 3 Nov 2026: Dyadic work is done in rtg-corpus and its outputs go into the Dyadic DSN; LIT is used only through requests in `pipes/LIT/`.
- PI: OPEN 20 stage 3 is not authorized; N = 432 is deferred (stage-2 adoption, SESSION scope).
- PI, 11 Nov 2026 (in session): start the v6.4.24 candidate now ("başlayalım"); stage 2b authorized ("evet aşama 2b'yi yetkilendiriyorum"). Stage 3c is still not authorized.
- PI, 11 Nov 2026, 15:59 +03:00: "3c-a ile başlayalıp neticelendirelim sonrasını daha sonra değerlendiririz." Stage 3c-a is authorized; 3c-b is not.
- PI, 11 Nov 2026, 15:52 +03:00: the 3b r2 tube route is accepted, scoped, as the basis of the stage-3c certificate design aimed at \|ξ*\| = 0.40 (design note §12). No run is authorized by it.
- PI, 11 Nov 2026, 13:26 +03:00: "v6.4.24 r2 'yi benimsiyorum" (adopted bytes after the status transform: `10fbdacc…bc16`).
- Co-owner and owner, 11 Nov: the 3b design aims at certifying one jump (\|ξ*\| = 0.40 as a first target); scouting of the second overlap class is not needed now and is not authorized.
- Co-owner and owner, 3 Nov: v6.4.24 carries interface changes and S1; the §1 compaction waits for v6.4.25 or later; S2 (L-PHASE row B) is separate.
- X4, adopted in v6.4.24: DYAD RIDs for "not area-preserving" (`[ALG]`), the p = 6 linear order and the homological resonance condition; no DYAD RID for the cubic radial rate across p (stays a RECOG import).
- 11 Nov: no DYAD RID for RECOG's c_J and c_7 (disposition record, item 3).
- Owner, 12 Nov: LIT's check of the use of López-Hernanz 2012 accepted at SESSION scope (C1–C3 compared with the design); INF-016 deferred, nothing adopted; the AZ owner check of `DYAD-ALG-Q3-DEG2-CANCEL` is done and answered by pipe (no correction asked).
- `[SESSION]`, 11 Nov (co-owner's comparison with LIT's notes; DYAD side checked by the owner): the certificate target is the jump at one point of S₀ ∩ S₁ (Im t → −∞). LIT's harmonic target s₁ is on the other overlap class and is a first Fourier coefficient. A certified jump does not give s₁ ≠ 0; no derivation between the two is recorded. Whether LIT's candidate also holds on the lower overlap is a question for LIT (not filed).
- B-an and B-6 are ACTIVE. No analytic existence or divergence theorem has been claimed.

**Tried and set aside** (do not repeat without a new reason):
- The a-priori operator route of LIT INF-009/010 for the stage-3 enclosure. Best radius 1.4·10⁻¹⁰ at η = π/4, and at most 1.76·10⁻⁶ under Y-scaling for every η (LIT's grid-free bound). Reopen only for a different normalization (larger m) or different operator bounds.
- Reading the stage-2 Borel scale from the coefficients a₂…a₂₁₆: INCONCLUSIVE (`[NUM]`). Stage 2b measured the jump directly and explains it: against the leading time 1/(3\|ξ\|³) the apparent exponent is 1.8–1.9, against the Fatou time the slope tends to 2π. N = 432 is not needed for this question.
- Radii above \|ξ*\| ≈ 0.45 in the stage-2b harness: the start-point search leaves the neighbourhood of 0 (seen at 0.50).
- Using INF-014/015 for real orbits: not possible. On the real slice \|w/z²\| = 1/\|z\| → ∞, so real orbits never approach the lifted points.
- Orbit control from INF-009 at the matching radius: the criterion admits at most \|ξ\| < 0.074 in the m = 2 chart (LIT's subpetal reply, owner-checked), and stage 2b matched at 0.08–0.12. A sharper orbit constant does not help; the control has to come from the restricted map on a tube around the truncated series (design record §9).
- As negative controls of the tube sampling: a tube with \|ξ^{−α}\| (it still passes, so it is not a control) and q₁ = q₂ = 0 (the tube radius grows without bound near 0; the run does not finish).
- Tube parameters q = 12, R(ξ*) = 10⁻⁴, and η₀ = π/6: the truncated series (N = 40) is not inside the tube at the outer edge of D₀. R(ξ*) = 10⁻³ fails the same gate once the edge radii 0.44–0.46 are sampled; r2 uses 2·10⁻³.
- Stage 3c engine with second-order Taylor forms on boxes in (x, u): sound but far too wide (H_u enclosures above 100% at 0.5% boxes); the quotients are of order \|x\|⁴ against steps of order 1. Replaced by power series in x along the curve (plan record 2.6).
- Power series of F⁻¹ along the curve: the coefficients grow (ratio 1.13, `[NUM]`), so there is no tail bound on the circle D₁ needs. The inverse step is taken from the forward series by a local inverse lemma (plan record 2.5, 2.6).
- Building the curve coefficients at 60 digits: the recursion loses its precision and the values are wrong in size. Build them at 400 digits.
- Wedge domains defined by the two τ-conditions alone: not local, the conditions hold again for \|ξ\| ≳ 0.7 (review R1). Use the chart sectors and the guard property.
- A uniqueness theorem of our own for all invariant graphs in the tube (r1's P2): withdrawn; reopen only if LIT finds that Theorem 4.2(3) does not cover the use.
- The co-owner's Cauchy-majorant preflight as stage-3 evidence: its constants (K₁ ≈ 2·10⁹ and larger) come from a Cauchy radius of 0.002. It is tooling for E1–E2 only.

**Evidence pointers.** Stage 1: `evidence/dyad/open20-an/stage1_prep.json` (`2c9ae637…4739`). Stage 3a: `evidence/dyad/open20-an/stage3-route/`. INF-014/015 hypotheses: `evidence/dyad/open20-an/lit-inf014-inf015/`. Stage 2b: `evidence/dyad/open20-an/stage2b/`. LIT subpetal reply check: `evidence/dyad/open20-an/lit-subpetal-reply/`. 3b tube sampling: `evidence/dyad/open20-an/stage3b-design/`. Bridge note: `evidence/dyad/bridge-note-v1-1/`. v6.4.24 build, checks, controls and publication transform: `evidence/dyad/scripts/*_dyad_v6_4_24*.py`, outputs `evidence/dyad/v6.4.24/` (the pattern to reuse for the next edition).

**Resume.** Run LIVE_STATE. Read `DYAD_OPEN20_AN_STAGE3B_DESIGN.md` (§4 lemma, §6 obligations, §9 risks). Then check PI_PENDING below.

**Next 1–3 actions / acceptance:**
1. **OPEN 20 analytic branch: nothing is authorized beyond stage 3c-a, which is complete.** Open for a claim: the seed (Q1–Q3) and the divergence step P4, as written arguments (hand-over record §5, §8). They are the next scientific step if the PI wants one. Stage 3c-b and scouting of the second overlap class are not authorized. A prerequisite of a certification run is filed in the hand-over record §8 (t_M with the upper bound of \|A₃\|).
2. **INF-016 (deferred):** the only recorded route from a jump to B-an and B-6. A later design with a first-harmonic observable would need the items listed in the disposition record §2; it is the PI's decision whether to open it.
3. **Next Dyadic edition (v6.4.25 or later):** consumer register row and Appendix F rows for AZ at `az-v0.8` (disposition record §3); the carried items of the v6.4.24 backlog §D.
4. **When PR #183 reaches `main`:** disposition of `pipes/DYAD/20261104-OFN-binary-six-cycle-linear-bridge.md`.

**Reopen trigger.** A new item in `pipes/DYAD/`; an answer from NUMGEN, OFN or Triadic to the open DYAD notices; a change of LIT's reply on Theorem 4.2(3) or of INF-016; a new owner tag of RECOG, NUMGEN, OFN, Genesis or Triadic that changes a statement DYAD imports or exports.

## CO-OWNER LANE — ChatGPT

*(Written by the co-owner session under its own check stamp: goal, last durable work, decisions held, tried and set aside, evidence, resume, next 1–3 actions, reopen trigger. Empty until that session fills it.)*

## PI_PENDING

As of 12 November 2026, 18:55 +03:00:
1. **Merge of the inbox-disposition PR** (this branch), after the co-owner's review.
2. **What comes next on OPEN 20** — the PI's choice among: the seed (Q1–Q3) and P4 as written arguments (the owner's and the co-owner's recommendation); nothing for now. A decision on stage 3c-b is not due before the seed is written.

Stage 3c-b and scouting of the second overlap class are not authorized.
