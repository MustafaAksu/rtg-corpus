# RER v0.2 r4.4: Phase A change record

**Date:** 19 Oct 2026.
**From:** Claude, RER co-owner (preparer). The preparer does not accept his own work.
**Status:** NONCANONICAL Phase A candidate. Nothing is adopted, frozen or published.
**Answers:** `RER_R44_RECEIVER_DECISIONS_20261019.md` §V, items (i)–(v).

## 1. Base

The base is the exact r4.4 bytes, `5df4738685ecebf979da4f48d432ef2f9af01b6964dfefb62d7ac31887caa9d8`, from package `0c08ae63…f91f`.

Phase A edits no Markdown. Every output below is generated from that file, plus:
- two preparer catalogs (`catalog_sources.json`, `catalog_records.json`);
- two package manifests (r4 and r4.4).

Input hashes are pinned in `PINS.json`.

## 2. Deliverables

| Item | File | Content |
|---|---|---|
| (i) | `out/RER_REGISTRY_v0_2_r4_4_PHASEA.json` | 20 records, 4 gap entries (G7–G10), and the 16 legacy v0.1 entries. The legacy entries are a separate block labelled `HISTORICAL_SNAPSHOT_NOT_AN_ADOPTION_COHORT`. Every record has `adoption_status: PENDING`. The two ER-2B records are `BLOCKED_SOURCE_UNVERIFIED`, `accepted_cohort_eligible: false`, `grade_status: SOURCE_CLAIMED_NOT_RER_ADOPTED`. |
| (ii) | `out/SOURCE_CURRENCY_MATRIX.json` / `.md` | One row per import occurrence (76 rows) with the fields of decision record §III.2: `source_doc`, `cited_version`, `cited_sha256` (cited hash), `current_owner_version`, `verified_current_hash`, `section_or_RID`, `inspection_extent`, `status`, `reviewer_disposition` (all PENDING). Extra fields: bytes status, package-path presence (r4 and r4.4), currency and the reason for it. |
| (iii) | `out/BLOCKED_SOURCE_REGISTER.json` / `.md` | Lists ER-2B v0.2 and the two coincidence sources cited by CND01. Also records the packaging finding and the byte-availability gap. |
| (iv) | `build_phaseA.py`, `check_phaseA.py`, `check_phaseA_output.txt` | Deterministic builder; 14 gates; 8 negative controls. |
| (v) | `RRF_EDITOR_QUESTION_PACKET_RER_PHASEA_20261019.md` | Eight questions on G7–G10, the v0.8→v0.8.3 pins, the non-normative status and the CND01 ownership split. |

## 3. Gates (14/14 PASS; 8/8 negative controls fail as required)

| Gate | Check |
|---|---|
| A1 | r4.4 source hash and all input pins |
| A2 | Determinism: a fresh in-memory build equals the stored outputs byte for byte |
| A3 | Forward direction (Markdown → JSON): the set and order of record headings equals the JSON ids; 20 records, no duplicates; gap entries kept separate |
| A4 | Reverse direction (JSON → Markdown): for each record, the grade line, task, the six contract cells, the import count and the OPEN count are re-found in the Markdown by an independent line scan that does not use the parser |
| A5 | One matrix row per import occurrence; required fields present; all dispositions PENDING |
| A6 | Every `BYTE_VERIFIED_MATCH` file exists and re-hashes to the cited value. A package path is claimed only if it is in that package's manifest. |
| A7 | Owner rows whose cited version is not the current one carry a status other than CURRENT, with a reason |
| A8 | ER-2B firewall |
| A9 | No promotion: adoption PENDING everywhere |
| A10 | CND01 provenance split (see §4) |
| A11 | The legacy snapshot is separate and labelled historical |
| A12 | The blocked register covers every missing primary input and every "Direct source not available" row |
| A13 | The packaging finding lists every cited file lost between r4 and r4.4 |
| A14 | Status vocabulary: VERIFIED requires a byte match; `verified_current_hash` is set only where the current owner file was byte-hashed |

**About "reverse".** Phase A builds no Markdown, so there is no edit to reverse. The reversal requirement is met in two parts:
- A1: the Markdown in the package is byte-identical to r4.4.
- A3 + A4: a two-way Markdown↔JSON consistency check.

## 4. Decisions applied

- **D-2 firewall.** RER-ER2B-T6D and RER-ER2B-CARRIER keep their source-claimed grades ([ALG]) and are excluded from the accepted cohort.
  - ER-2B v0.3 (`80669c69…`) is recorded as background only.
  - Its Part A reports the identities of the v0.2 package (`8c635290…48ee`) and of the v0.2 study (`ea26d3d1…5e`). These are source-reported. The bytes are not available to me, and they do not unblock anything.
- **CND01.** `claim_provenance: RER_NATIVE_STANDARD_MATH`. The `[THM]` `Fσ=σF ⇒ F(Fix σ)⊆Fix σ` is attributed to standard mathematics. RRF v0.8.3 §6.2 is recorded as the `[DEF]` proposed interface, not as the source of the theorem grade.
  - The two coincidence sources block only the secondary-report witness, not the `[THM]`.
- **Genesis pins.** The v2.8.7 theorem pins stay. v2.8.8 is recorded as current (receiver-hashed `9abd3616…`), with status UNCHANGED_OWNER_REPORTED. A repin waits for section-level verification.
- **No path overclaim.** A file counts as present in a package only if it is in that package's manifest. Its hash counts as verified only if the bytes were hashed here.

## 5. Findings

1. **Packaging defect (r4.1–r4.4).** Seven cited Triadic evidence files were in the r4 package but were not carried into r4.1–r4.4:
   - `TRIAD_BGJ`, `TRIAD_BGJ_PY`, `TRIAD_CK_PY`, `TRIAD_EC_PY`, `TRIAD_GC_PY`, `TRIAD_KR_PY`, `TRIAD_SB_PY`.

   Their bytes are in this package under `sources_available/` and match the cited hashes. The next RER draft package must carry them at the cited paths.
2. **No in-record review receipt** for:
   - GEN-C01 to C06;
   - ER2B-CARRIER;
   - RRF-CND01.

   Under D-4 these cannot be closed by a prior acceptance. They go to deep review, or are blocked.
3. **Author conflict.** TRIAD-FORMAL-INVOLUTION and TRIAD-BIRTH-GRAPH-INVOLUTION rest on Triadic-side evidence that I wrote. The receiving co-owner dispositions them.
4. **G10 pin drift.** G10 cites RRF v0.8 §6.4 (lines 366–390). In v0.8.1 and later, that content lives in the separate proposal `RTG_RRF_RER_DYNAMICAL_CLOSURE_PROPOSAL_v0_1.md` (RRF v0.8.3 §6.4 is a pointer). This is packet Q3.
5. **Byte-availability gap.**
   - 27 keys (53 rows) have bytes that are not available here; they are in the r3.1 source package, so the receiving side can byte-verify them.
   - Of these, 52 rows have hashes printed in RER. The remaining row, `G2NOTE04`, has no printed hash.
6. **Status counts.** VERIFIED 23, OWNER_REPORTED 6, HISTORICAL 41, BLOCKED 6.
7. **Watch items.**
   - **Genesis v2.8.9 DRAFT** (`b2cc5c5c…`): adds a transported chiral factor no-go. Assess its relevance to GEN-K3-MODAL and G6 after it is adopted.
   - **Dyadic v6.4.15** (`be270dde…`, owner-adopted): I read the owner text. It adds OPEN 3b results only, and renames or regrades no RID cited by RER. Its reviewer release verification is still pending.

## 6. Requested

1. A receiving replay. Unzip the package, run `python -I build_phaseA.py`, then `python -I check_phaseA.py --tamper`, and compare the outputs with `SHA256SUMS.txt`.
2. Phase A→B gate: accept or reject the matrix and the register as complete.
3. The packet goes to the RRF editor, through the PI.

Not done: no record disposition (Phase B), no RRF amendment, no adoption, no freeze, no pilot.
