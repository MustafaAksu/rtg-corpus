# Atlas advisory — state of the AZ stream after its reactivation

**Date:** 11 November 2026, checked 14:55–15:30 +03:00 on `main` `5ffec34`. **By:** Claude, Atlas owner, at the PI's request ("review AZ's current state as Atlas and write an advisory note"). **Status:** [SESSION] advisory. The Atlas owner advises and does not decide; no DSN is edited; nothing here is adopted, and nothing here authorizes or blocks a campaign.
**Read for this note:** `records/az/AZ_v0_7_RELEASE_RECORD.md` in full; `records/az/AZ_REACTIVATION_TRIAGE.md` §§6–7; the AZ orientation note on `main` and on the PR #211 branch; the AZ DSN at `az-v0.7` (targeted: header, §2, §3 guards, §6, §8, §9, Appendix B); PR #211 at head `47dee46`: description, reviews `5855522171` and `5857601141`, preregistration §§0–4, 6.6, 10–12; `pipes/ATLAS/` and `pipes/AZ/`; `records/dyad/RTG_DYADIC_v6_4_24_RELEASE_RECORD.md` (AZ rows only). **Not done:** no script, fixture or gate was rerun; the proofs of the preregistration §2 were read, not checked line by line; the statistical design was not audited (the co-owner review did that); the 59 edits of v0.7 were not re-compared with their owner texts.

## 1. What the stream did in one day — verified facts

| Item | Observation | Evidence |
|---|---|---|
| Triage | 34 drift rows, two inbox items, five Atlas findings, split into a corrections list and new work; reviewed by the second co-owner; six scope questions decided by the PI | PR #207, merge `f5e548e`; triage §7 |
| AZ v0.7 | Corrections only: 59 logged edits built by script from the tagged v0.6 bytes; gates 7/7; negative controls 4/4; change-focused review and readback by the second co-owner; adopted by the PI on 11 Nov | release record §§1–4, 13 |
| Tag | `az-v0.7` is annotated; target = merge commit `b1c30b7` of PR #208 (parents `f5e548e`, `b9fce79`); file SHA-256 at tag and `main` `2294d2a3287651802824a77ea22fb8f3896f6837cca1162fd8479ff02839fc94`, equal to the release record and to `BASELINE.md` | `git cat-file`, `git rev-parse`, `sha256sum`, this session |
| Advisory rows 1 and 3 (10 Nov) | **Resolved in the adopted text.** The "legal ×2" sentence survives only as the quoted retraction in Appendix B; §6 now carries the OPEN-M v0.7.1 R15/R16 verdict. `DYAD-ALG-Q3-DEG2-CANCEL` and `TDRG-DEF-ZN-STATE` are cited; the old strings appear only as named history | grep of the tagged file, this session |
| Pipes | Both inbox items closed with a disposition. Five notices filed after the tag; Dyadic has answered (its v6.4.24 re-read Appendix F at `az-v0.7`); TDRG, PROG, ATLAS and DZT are open | `pipes/`, reporter |
| New work | AZ Action 1, token resonance and basin selection: preregistration, runner, fixtures, negative controls, fail-closed analysis, frozen exploratory pilot. Review: corrections required, then accepted (scoped). No confirmatory run exists. Open as PR #211, 53 files | PR #211 |

**Assessment.** The corrections cycle is the cleanest reactivation in the repository so far: the edition is a logged transformation of the tagged predecessor, the scope was decided before the edit, AZ-owned content is shown byte-identical, and the record says what was not done. The Atlas has no finding against `az-v0.7`.

## 2. Points for the PI, in order of weight

### 2.1 Decide where an Action 1 result will live before the data exist

The AZ DSN describes itself as "an infrastructure ledger, not an active scientific study", Maturity Level A, and its registry says it "covers scope and infrastructure questions only". Two of its open items are exactly the questions Action 1 runs into:

- **AZ-OPEN-PROMO** — the conditions under which AZ becomes a Level B scientific DSN, "including required artifact and transcript provenance", are not stated.
- **AZ-OPEN-SCOPE-ARITH** — whether the ℤ_N divisibility structure of TDR-G is a bridge-candidate observable or "purely internal to the TDR-G DSN" is not decided.

Action 1 is a confirmatory campaign on TDR-G's engine about TDR-G's dynamics, with three propositions about TDR-G's event rules. The preregistration is careful here: everything is a proposal to the TDR-G owner, the OPENs stay TDR-G's (SG-AZ-6), and §6.6 says the home and grade are "decided later by the owners and the PI". The design fixes the statistics in advance; it does not fix the **institutional reading** in advance. If the result is strong, the pull will be to promote AZ on the strength of it.

*Advice:* record now, in one paragraph, the rule for each outcome — for example: a supported contrast enters AZ as a `[NUM]` diagnostic inside Level A and is offered to TDR-G; it does not by itself answer AZ-OPEN-PROMO; it becomes a TDR-G statement only by a TDR-G edition. This costs nothing and does not delay Stage 1.

### 2.2 File the offer to TDR-G now

The item drafted in the preregistration §11 is not filed; the reviewer recommends filing it. The Atlas agrees, for a reason beyond courtesy: the primary profile P1 (the adopted `TDRG-DEF-ORIENT`) is not the profile of TDR-G's own historical numbers (P2, `[conv: v18 path orientation]`), and Corollary 1.2 states for n nodes what TDR-G records as conjectured. Both need the TDR-G owner's reading, and TDR-G has had no owner session answering its inbox (the AZ v0.7 notice there is open). An offer filed before the run shows that the question was put before the answer was known.

### 2.3 Stage 1: the Atlas has no objection; two custody points

Stage 1 is small (19,900 runs, about half an hour), preregistered, reviewed and fail-closed. Two things would make its record stronger:

- The PI's authorization names the bytes: PR #211 head `47dee46` and the hash of `evidence/az/token_resonance/SHA256SUMS`.
- The registered package is on `main` before the run. PR #211 is [SESSION] material and a merge adopts nothing; with the package merged, the registration has a commit that precedes the data in the public history, and the upload branch with the results is compared against `main`, not against an unmerged branch.

### 2.4 Thread C evidence is the stream's largest standing debt

AZ §9 now says that none of the Thread C files, including the hash registry `AZ-ART-AZV5-REGISTRY`, is in the repository (`EV-SRC-REPORTED`, `EV-NOT-RERUN`). Every AZ-owned result — PROP-AZ-CORE-EQUIV, the antipodal-band obstruction, the `4|q` diagnostic and its reclassification — rests on that evidence, and AZ-OPEN-PROMO names artifact provenance as a promotion condition. The statement is honest; the debt is real. Locating the `az_v5` package on the PI's machines is worth more to this stream than any further edition. If it cannot be found, the options are a rerun from recovered scripts or a recorded downgrade of the evidence qualifier; that is the AZ owners' and the PI's call.

### 2.5 The next AZ edition should be structural, and after Action 1

v0.7 grew by 13 % because it now restates its owners' statements correctly, with their RIDs and qualifications. That is right for a corrections edition and expensive to keep: one day later Dyadic is at `dyad-v6.4.24` and AZ's pins are one edition behind. Dyadic filed no notice to AZ and re-read its Appendix F at `az-v0.7`, so nothing AZ imports appears to have changed; this note did not verify that statement by statement (UNVERIFIED), and AZ can record the check at its next checkpoint without an edition.

The remedy is the one Programme v1.4 §6.7 already proposes: imports by pointer (RID, tag, one line of scope) instead of restated owner science. Then an owner edition touches AZ only when an imported RID changes. *Advice:* one edition v0.8 that does the §6.7 reduction and the Methodology v1.4 migration together, after Stage 1 is closed, so that the DSN does not move while a campaign pinned to `az-v0.7` is running. This is also where the PI's hope of the content "coming together" is realised for the Atlas: fewer restated statements in consumers means fewer second homes.

### 2.6 Housekeeping

- **Entry note.** Its shared sections were written by the Atlas owner before v0.7 and were stale (they named `az-v0.6` as governing). They are brought to the current state in the PR that carries this note; lanes are untouched. The PI should name who maintains the shared sections from here on; the natural choice is the AZ co-owner who holds the working lane.
- **Reporter.** `tools/orient.py` has no built-in AZ profile; without `--record-glob 'records/az/AZ_v*_RELEASE_RECORD.md'` it prints "release record: None" although the record exists. The full command is in the entry note. A built-in profile is a small tool change with its own review.
- **`BASELINE.md`** AZ row: correct (v0.7, hash, record, tag).

## 3. Atlas side

- `pipes/ATLAS/20261111-AZ-v0-7-adopted.md` and `pipes/ATLAS/20261111-DYAD-v6-4-24-adopted.md`: dispositioned *accept*, pointer to this section. Two source tags have moved since the snapshot of Atlas v0.11 (`az-v0.6` → `az-v0.7`, `dyad-v6.4.23` → `dyad-v6.4.24`); the other sixteen are unchanged. An impact refresh (Atlas v0.12) is due under Method §7 and is the Atlas owner's next work.
- Expected in that refresh, to be confirmed against the owner texts: AZ.A1, AZ.A2, AZ.A3 and AZ.A7 close; HEADLINE H2 loses its AZ clause and H3 its AZ half (the DZT half stays); the Thread C evidence limit becomes a qualifier on the AZ nodes; the Dyadic items of its notice (DYAD.X4 RIDs, `DYAD-THM-OPEN21-SHARP-ROWS`, the OPEN 20 pilot paragraph) are taken up.
- Action 1 material is [SESSION] and is not Atlas content. The Atlas reads AZ results only from an adopted AZ or TDR-G edition.
- Advisory of 10 November: rows 1 and 3 are resolved by `az-v0.7`. Rows 2 (DZT), 4 (OPEN-M) and 5 (Legacy, Pre-Legacy) stand as dispositioned.

## 4. Decisions this note puts to the PI

| # | Question | Atlas advice |
|---|---|---|
| 1 | Outcome rule for Action 1 (home and grade path per result), recorded before Stage 1 | yes, one paragraph in the preregistration's amendment log or in the AZ lane |
| 2 | File the TDR-G offer now | yes |
| 3 | Merge PR #211 before the run; authorization names `47dee46` and the `SHA256SUMS` hash | yes |
| 4 | Thread C evidence: search the PI's machines for the `az_v5` package | before any further AZ edition |
| 5 | Next edition v0.8 = §6.7 reduction + Methodology v1.4 migration, after Stage 1 | yes, as one edition |
| 6 | Maintainer of the AZ entry note's shared sections | the AZ co-owner holding the working lane |
