# DYAD v6.4.24 — post-tag read-back, inbox closure and notices

**Date:** 11 November 2026. **By:** Dyadic DSN owner (Claude). **Status:** working record (OWNER-RUN read-back). The release record `records/dyad/RTG_DYADIC_v6_4_24_RELEASE_RECORD.md` is frozen at adoption and is not edited.

## 1. Merge and tag

| Item | Value |
|---|---|
| Merge | PR #213, merge commit `f0af6392ed560b55aedc640bc166f0b87f612f7c` (parents `d70f4fd`, `57ec5c4`), merged 2026-11-11T10:40:05Z |
| Tag | `dyad-v6.4.24`, annotated (tagger Mustafa Aksu); points to the merge commit `f0af639` |
| Tag message | names the final SHA-256 and the release record |
| File at the tag | `dsn/RTG_DYADIC_OSCILLATOR_DSN.md` SHA-256 `10fbdacc19544596480acae03faeba076f21103a01b903a8d3305cfa8ed7bc16`, 285 321 bytes, 1638 lines; equal to the release record and to `main` |
| `BASELINE.md` DYAD row | v6.4.24, same hash, tag cell `dyad-v6.4.24` |
| Predecessor | `dyad-v6.4.23` (`9f874ccc…25cb`) |

The tag sits on the merge commit of the adoption PR. No commit touches the study paths after the tag (`tools/orient.py`, run with `--record-glob records/dyad/RTG_DYADIC_v6_4_24_RELEASE_RECORD.md`: release record found, status line ADOPTED, names the tag hash).

## 2. Read-back checks (OWNER-RUN on `main` at `f0af639`)

- **Publication transform.** `release_dyad_v6_4_24.py` applied to the reviewed r2 candidate (`git show 23e610e:dsn/RTG_DYADIC_OSCILLATOR_DSN.md`, SHA-256 `014e1ac3…8958`) gives a file byte-identical to the one on `main`: 285 321 bytes, exactly 3 changed lines.
- **Checks.** `check_dyad_v6_4_24.py` with the v6.4.23 file as base and the r2 candidate: C0–C11 PASS; the output JSON is byte-identical to the committed `evidence/dyad/v6.4.24/check_dyad_v6_4_24.json`.
- **Evidence checksums.** `evidence/dyad/v6.4.24/SHA256SUMS.txt`: 8/8 OK.
- **Lint.** `tools/dsn_lint.py` on the published file: 199 RIDs, 0 near-duplicate paragraphs. The committed `dsn_lint.txt` was taken on the r2 candidate; the two reports differ only in the byte counts of the three status lines (285 275 against 285 321 bytes).

## 3. Inbox (`pipes/DYAD/`)

One item was open at the tag. It is closed in the PR that carries this record.

| Item | Verdict | Pointer |
|---|---|---|
| `20261111-LIT-subpetal-orbit-constant-search.md` (LIT's reply to the request of 3 Nov) | accept | `records/dyad/DYAD_OPEN20_AN_SECTORIAL_PILOT_DESIGN.md` §9 |

- **Content.** No published orbit bound with an explicit radius; a sharper bound derived by LIT from INF-009; the petal radius is capped by the invariance criterion, not by the orbit constant; the a-priori route is not rescued.
- **Owner check (OWNER-RUN).** `evidence/dyad/scripts/dyad_open20_lit_subpetal_reply_check.py` (`a63c04ef28414da9bbc4051da060f53c59e68890b2c19e17afe0a12b5a2c01ac`); outputs and `SHA256SUMS.txt` in `evidence/dyad/open20-an/lit-subpetal-reply/` (`reply_check.json` `6b381d9b…df61`). Gates G0, T1–T6 PASS; the controls KCLASS and SEC each exit 1 at the named gate; a second run gave identical outputs.
- **Owner note.** LIT's caps are for the class K = K₁ + K₂. The cap 0.019 of the stage-3a record belongs to the radius-2 class (K = 2K₁ + K₂, ε₀ < 1/2), not to LIT's row ε₀ = 0.25. No conclusion changes.
- **Bearing on the 3b design.** The matching radii of stage 2b (0.08–0.12) lie outside every domain this criterion admits in the m = 2 chart. Design record §9 lists the consequences.
- Nothing is imported into the DSN.

`pipes/DYAD/` then holds 17 items, all closed. PR #183 (open) would add one OFN finding; it is dispositioned when it reaches `main`.

## 4. Notices filed (pipe items from DYAD, per release record §7)

| To | File | Content |
|---|---|---|
| RECOG | `pipes/RECOG/20261111-DYAD-v6-4-24-adopted.md` | `DYAD-THM-OPEN21-SHARP-ROWS` offered for A1a (RECOG decides); the adopted OPEN 21 result unchanged; §7 import row for `RECOG-THM-R9-SHARPENED-ROWS`; no DYAD RID for c_J, c_7 |
| NUMGEN | `pipes/NUMGEN/20261111-DYAD-v6-4-24-adopted.md` | informational: no imported statement changed; register row unchanged |
| Triadic | `pipes/TRIAD/20261111-DYAD-v6-4-24-adopted.md` | `DYAD-DEF-PRIMITIVE-MAP` label wording; imports unchanged; bridge-note source registered |
| Genesis | `pipes/GEN/20261111-DYAD-v6-4-24-adopted.md` | the same label wording; alias unchanged; register at Genesis v2.10 |
| OFN | `pipes/OFN/20261111-DYAD-v6-4-24-adopted.md` | the same label wording; imports unchanged |
| ATLAS | `pipes/ATLAS/20261111-DYAD-v6-4-24-adopted.md` | DYAD.X4: three RIDs registered, one statement left as a RECOG import; new result; OPEN 20 pilot state in the DSN; new artifact RIDs; register |
| LIT | `pipes/LIT/20261111-DYAD-v6-4-24-use-report.md` | use report: three published works cited at SESSION scope by bibliographic data; no Import Ledger row; disposition of the subpetal reply |

Notice states follow `pipes/README.md`. These files are the filing. Receipt, statement acceptance and adopted use are recorded only by the receivers. `tools/pipes_index.py --check`: OK (105 items in 20 inboxes).

Dyadic items still open at their receivers from earlier rounds: NUMGEN and OFN (`20261030-DYAD-v6-4-23-adopted.md`), Triadic (`20261103-DYAD-bridge-note-recovered.md`), and DZT, ER-2B, RER, RRF, UVM (`20261103-DYAD-notices-n16-n21.md`).

## 5. Carried

- OPEN 20 analytic branch: the 3b design note (certificate of a nonzero jump at \|ξ*\| ≈ 0.40; local enclosure at \|ξ\| ≈ 0.1 as the open obligation). Stage 3c and scouting of the second overlap class are not authorized. B-an and B-6 ACTIVE.
- Owner check of AZ §4.1.1 against `DYAD-ALG-Q3-DEG2-CANCEL`; answer through `pipes/AZ/`.
- `records/dyad/DYAD_v6_4_24_BACKLOG.md` §D: the §1 compaction (v6.4.25 or later), S2 (L-PHASE row B), the OPEN 18 footprint `[DEF]`, the RAW-CUBIC historical identity (DYAD.X11), and the unrecovered sources of `records/dyad/DYAD_SOURCE_RECOVERY_LIST.md`.
- The optional sharper row-A constant built on `RECOG-ALG-A1C-JET-REMAINDER-BOUNDS` (backlog §C3; needs its own certificate; not planned).
