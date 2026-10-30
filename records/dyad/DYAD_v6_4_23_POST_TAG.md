# DYAD v6.4.23 — post-tag read-back, pipe closures and notices

**Date:** 30 October 2026. **By:** Dyadic DSN owner (Claude). **Status:** working record (OWNER-RUN read-back). The release record `records/dyad/RTG_DYADIC_v6_4_23_RELEASE_RECORD.md` is frozen at adoption and is not edited.

## 1. Merge and tag

| Item | Value |
|---|---|
| Merges | PR #125 (`1379255`), PR #127 (`546fde7`), PR #130 (`5420f16`), PR #134 (`9607c01`), PR #132 (`33d21d8`) — merge commits, in the planned order |
| Tag | `dyad-v6.4.23`, annotated (tagger Mustafa Aksu); points to commit `ab8749b2a48d5d26082c5e5b16d5ef72298bcec3` |
| Tag message | names the final SHA-256 and the release record |
| File at the tag | `dsn/RTG_DYADIC_OSCILLATOR_DSN.md` SHA-256 `9f874ccc1cd684482f26a27fca13b37102977cba2a80a75e762ecd7b300425cb` = release record = `main` |
| `BASELINE.md` DYAD row | v6.4.23, same hash |

**Observation (no action).** The tag sits on `ab8749b`, the `main` head after two later merges (PR #131 and PR #133, Atlas/Triadic records), not on the PR #132 merge commit `33d21d8`. Between the two commits no file under `dsn/RTG_DYADIC_OSCILLATOR_DSN.md`, `records/dyad/`, `evidence/dyad/` or `BASELINE.md` differs (`git diff 33d21d8 ab8749b` touches only the five triad/atlas files). The tag therefore identifies the adopted edition exactly. Tags are not moved (CONVENTIONS); this note is the record.

## 2. Read-back checks (OWNER-RUN on `main` at `ab8749b`)

- The adopted file at the tag hashes to the release-record value. Re-running the publication transform on the reviewed r2 candidate (`5894fae`) reproduces it: 268 947 bytes, exactly 3 changed lines.
- `evidence/dyad/v6.4.23/SHA256SUMS.txt`: 8/8 OK. `evidence/dyad/inbox-20261030/SHA256SUMS.txt`: 14/14 OK.
- The owner checks were rerun from the uploads now on `main`:
  - inputs: `upload/dyad-sources/`: P2-B v2 zip `e4e2bab0…`, NUMGEN review zip `a7fc9ed6…`, OPEN 18 source `a9acb69f…`;
  - result: RESULT PASS, and `owner_checks.json` is byte-identical to the committed file (`f8aaf00d…05e1`).
- The cited records are on `main`:
  - the Atlas advisory, the hash check and the entry note;
  - both independent dispositions;
  - the reconciliation;
  - the Atlas row check (`records/atlas/ATLAS_DYAD_v6_4_23_R2_ROW_CHECK_CHATGPT.md`).

## 3. Inbox closures (`pipes/DYAD/`)

All seven items are `closed`, each with a dated disposition (`tools/pipes_index.py --check`: OK).

| Item | Verdict | Pointer |
|---|---|---|
| NUMGEN q* question | accept with change (answer: no) | `DYAD-THM-OPEN18-STEP-MONOTONE` |
| NUMGEN v1.21 notice | accept | release record |
| RECOG $C_7$ ceilings | accept | `DYAD-THM-NF-REM-C7-SHARP` |
| RECOG (D5) bridge constants | accept with change ($c'_Q=0.36916$) | `DYAD-THM-LPHASE-ROWA-BRIDGE` |
| RECOG v0.3.26 notice | accept (OPEN 21 re-basing deferred) | release record |
| OFN v0.11 notice | accept | release record |
| OFN v0.12 notice | accept | release record |

## 4. Notices filed (pipe items from DYAD; PI decision of 26 Oct 2026: pipes are not routed through the PI)

| To | File | Content |
|---|---|---|
| RECOG | `pipes/RECOG/20261030-DYAD-v6-4-23-adopted.md` | the two RIDs; **$c'_Q=0.36916$**; asks RECOG to re-check its uses of $0.36915$ before dropping `[assuming: (D5)]` |
| NUMGEN | `pipes/NUMGEN/20261030-DYAD-v6-4-23-adopted.md` | the q* answer (**no**, $q_{3/4}$, successor RID); N15 receipt; nothing asked |
| OFN | `pipes/OFN/20261030-DYAD-v6-4-23-adopted.md` | receipt of v0.11 and v0.12; register; identity; nothing asked |
| ATLAS | `pipes/ATLAS/20261030-DYAD-v6-4-23-adopted.md` | NUMGEN.N-Q* answered; RECOG.R-A1 stays open; new RIDs |

Notice states follow `pipes/README.md`. These files are the filing. Receipt, statement acceptance and adopted use are recorded only by the receivers.

## 5. Carried

- The OPEN 21 re-basing (deferred owner item).
- A footprint `[DEF]` with its own legality certificate (not planned).
- OPEN 20 analytic track: stage 2 `INCONCLUSIVE — NUM`; N=432 deferred; stage 3 not authorized.
- B-an and B-6 ACTIVE.
- N16–N21 as recorded.
- The unrecovered sources of `records/dyad/DYAD_SOURCE_RECOVERY_LIST.md`, including the OPEN 18 footprint audits.
