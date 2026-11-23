# RER Phase A r19 — change record (21 Oct 2026, preparer)

**Role.** PREPARER_ROLE. This record describes what r19 changes relative to r18 and how it can be replayed. It is not an acceptance, grade or PASS/FAIL judgement of any record; those belong to the independent receiving review.

**Authorization.** Receiving decision on OWNER_SECTION_CHECK_r1 (21 Oct 2026, ACCEPT SCOPED; review file `e279fd3c3cc47b0cbe02b85f50c21fc97f45d2e808f5e953b118ad63ff2cd323`, pinned here as `inputs/receiving_review_owner_section_20261021.md`), §5: "one r19 may be prepared; r18 and RER r4.13 do not change", with the row-level permissions of its table.

## 1. What does not change

- Source: RER v0.2 DRAFT r4.13, `e92991bd90d24599248410a20845a14588f4ae75e6582681aaa300de370f368c` (package `3cf88b73…ab00`). Not edited.
- Phase A r18 (`1dafb50fbd1e37a98b6804c84a2285d709d9810384a0a0fa5ce5820fbb4ca249`): kept as history. Its outputs and checker record are pinned in `inputs/phaseA_r18_outputs/` (gate A24 requires its `34/34 gates PASS` record; A25 requires registry identity with r18 apart from the schema label; A28 compares the matrix row by row).
- Registry (`out/RER_REGISTRY_v0_2_r4_13_PHASEA.json`): identical to r18 except `schema` → `RER-REGISTRY-PHASEA/19`. 20 records, 4 gap entries; grades, OPEN items, adoption PENDING, B-07/B-08 receipts unchanged.
- Every pin (cited version and hash) of all 91 rows; every `bytes_status` and `authentication`; the blocked register (6 BLOCKED rows); the SYNC-DYAD-OPEN20-BINF receipt and its receiving disposition; the G9/0–G9/3 per-reference audit state (PENDING_PER_REFERENCE_AUDIT); the 12 RRF08_ADOPTED rows' source limit (v0.8 original still not recovered).
- No adoption, freeze or publication.

## 2. Catalog delta (`catalog_sources.json`, `inputs/owner_versions_known.json`)

| Entry | r18 | r19 | Basis |
|---|---|---|---|
| owner_current Dyadic v6.4.19 `40c9e63f…6ec9` | OWNER_REPORTED | **BYTE_VERIFIED** | file `sources_available/DYAD6419__RTG_DYADIC_OSCILLATOR_DSN_v6_4_19.md` (275,935 bytes) hashed here; `inputs/source_custody_r19.json`; section check (cited blocks IDENTICAL, §6.14 CHANGED) |
| owner_current RECOG v0.3.22 `0dcce9e4…bcd9` | OWNER_REPORTED | **BYTE_VERIFIED** | file `RECOG0322__RTG_RELATIONAL_RECOGNITION_DSN_v0_3_22.md` (329,148 bytes); custody r19; section check (§6.6a, §6.16g IDENTICAL) |
| owner_current RRF v0.8.4 `2fb0a0fe…afce` | OWNER_REPORTED | **BYTE_VERIFIED** | file `RRF084__RTG_RRF_REPRESENTATION_REGISTRY_v0_8_4.md` (108,615 bytes); custody r19; section check (9 identical / 11 changed / 2 new) |
| history `phaseA_r17_r18` (three owners) | — | added | the r17–r18 OWNER_REPORTED state with its note, kept as history |
| key DYAD6418 rule | UNCHANGED_OWNER_REPORTED | **UNCHANGED_VERIFIED** | §2 OPEN 20 and §6.17 byte-identical v6.4.18 → v6.4.19; pin v6.4.18 unchanged; receiver receipt appended |
| key RECOG rule | UNCHANGED_OWNER_REPORTED | **UNCHANGED_VERIFIED** | §6.6a/§6.16g byte-identical on the two checked legs v0.3.20 → v0.3.21 → v0.3.22; receiver also compared v0.3.20 → v0.3.22 directly (RECEIVER-REPORTED); pins v0.3.20 unchanged; G9/0–G9/1 per-reference audit still pending |
| key RRF083 | RECHECK_IN_PHASE_B | RECHECK_IN_PHASE_B (unchanged) | reason appended: §2.3 byte-identical, §2.4b CHANGED v0.8.3 → v0.8.4; new `receiver_section_check`: consumer-compatible at the RER use point, keep HISTORICAL, **not whole-row equality** |
| key RRF082 | RECHECK_IN_PHASE_B | RECHECK_IN_PHASE_B (unchanged) | **OSC-N2 correction**: the adoption-record statement "only §2.4c changed" is kept as an earlier report; the receiver's direct v0.8.2 → v0.8.3 comparison found **both §2.4b and §4.2 changed**; §4.2 is identical only on the v0.8.3 → v0.8.4 leg. v0.8.2 file not held here → authentication stays RECEIVER_BYTE_VERIFIED |
| key DYAD6413 | RECHECK_IN_PHASE_B | RECHECK_IN_PHASE_B (unchanged) | reason appended: receiver's direct v6.4.13 → v6.4.19 comparison (OPEN 19, §6.15, §6.16 identical; OPEN 20 and §6.17 changed as wholes, Lemma F / F1–F3 paragraphs retained) recorded as RECEIVER-REPORTED, not replayed here; file not held |
| key RRF08_ADOPTED | RECHECK_IN_PHASE_B | unchanged | reason appended: v0.8 original still not recovered; the current file hash does not verify an old pin |
| `_catalog_checked` | 2026-10-21 (Phase A r17, preparer) | 2026-10-21 (Phase A r19, preparer) | — |
| `_source_authority` Dyadic/RECOG/RRF | record-stated, bytes not held | files held and hashed here; custody r19; section check | — |

**Recovered v6.4.13 and v0.8.2.** The receiver recovered both files from `TRIAD_RER_RECEIVING_REVIEW_20261019.zip` and placed them in its handoff zip (`OWNER_SECTION_RECEIVER_HANDOFF_20261021.zip`). That zip is not available to the preparer, so the receiver's permission to mark DYAD6413 and RRF082 `BYTE_VERIFIED_HERE` "if the files are placed in the package and re-hashed" is **not exercised** in r19; both rows keep `RECEIVER_BYTE_VERIFIED` and the receiver's direct comparisons are recorded as RECEIVER-REPORTED. This can be done in a later authorized step once the files are supplied.

**OSC-N1.** The preparer's chat summary of the section check said RRF 10/10/2; the correct count, as in the package table and JSON and as confirmed by the receiver, is **9 identical / 11 changed / 2 new**. The r19 notes, watch item and gate A29 use 9/11/2; a control (`A29 RRF note with the wrong block count (10/10/2)`) rejects the wrong count.

## 3. Effect on the matrix (`out/SOURCE_CURRENCY_MATRIX.json`)

- 91 rows; **18 rows differ from r18**, exactly the receiver's 18-row table: DYAD6418 (1), DYAD6413 (1), RECOG (2), RRF083 (1), RRF082 (1), RRF08_ADOPTED (12). They differ only in owner-currency fields (`currency`, `currency_reason`, `current_owner_evidence`, `verified_current_hash`, `status`, `receiver_section_check`); pins, bytes and authentication are unchanged in every row (gate A28).
- Status counts: **31 VERIFIED / 2 OWNER_REPORTED / 52 HISTORICAL / 6 BLOCKED** (r18: 28/5/52/6) — equal to the receiver's prospective accounting. The three status changes are DYAD6418 and the two RECOG rows (OWNER_REPORTED → VERIFIED). The remaining OWNER_REPORTED rows are the two GEN287 rows.
- Authentication counts unchanged: 60 BYTE_VERIFIED_HERE / 6 RECEIVER_BYTE_VERIFIED / 24 HASH_PRINTED_UNVERIFIED / 1 UNAUTHENTICATED_NO_HASH.
- `verified_current_hash` is now set on all Dyadic, RECOG and RRF rows (the current owner file was byte-hashed here); no row is CURRENT for these owners.
- Watch items: r18 list + one r19 item. The r19 item also carries the receiver's note that RER G10 still has the dated "v0.8.3 … governs" wording (for a later authorized consumer-source maintenance; not a contradiction in the scoped records).

## 4. Package changes

Added: `sources_available/DYAD6419__…v6_4_19.md`, `RECOG0322__…v0_3_22.md`, `RRF084__…v0_8_4.md`; `inputs/source_custody_r19.json` (PREPARER_DECLARED container chain: project-folder copies read through the project tool; the RRF text arrived inline and was written back from the session record; all three hashes equal the owner records and the receiver's identity receipts); `inputs/owner_section_check_r1/` (script, note, `compare_output.txt`, `owner_section_check.json`, `changed_blocks.diff`, `negcontrol_output.txt` — byte-identical to the accepted package `231201a5…7753`); `inputs/receiving_review_owner_section_20261021.md`; `inputs/phaseA_r18_outputs/` (r18 outputs + `check_phaseA_output_r18.txt`); `patch_r19.py` (the exact-once patch that produced r19 from the r18 package); this record. Removed: r18 change record and `patch_r18.py` (they stay in the r18 package). All new inputs pinned in `PINS.json` (gate A1).

Schemas: `RER-REGISTRY-PHASEA/19`, `RER-SOURCE-CURRENCY/19`, `RER-BLOCKED-SOURCES/19`.

## 5. Checker (`check_phaseA.py`)

34 gates, all PASS; **140 negative controls** (113 tampers + 27 file/input controls), each fails its named gate. Re-based gates:

- **A23** Dyadic: evidence BYTE_VERIFIED requires the v6.4.19 file in `sources_available` with hash `40c9e63f…`, the custody r19 entry, and the section-check output showing §2 OPEN 19/20, §§6.15–6.17 IDENTICAL and §6.14 CHANGED (one hunk inside listed blocks); r8–r18 history and v6.4.18/v6.4.17 identities kept; DYAD6413 RECHECK with the receiver report recorded; DYAD6418 UNCHANGED_VERIFIED/VERIFIED with pin v6.4.18.
- **A24** adds the r18 checker record. **A25** registry identical to r18 except schema. **A26** RECOG: file, custody, section check (§6.6a/§6.16g IDENTICAL), two-leg statement, frozen v0.3.20 edition with the G1 record, rows UNCHANGED_VERIFIED with v0.3.20 pins, per-reference audit pending. **A28** matrix vs r18 as in §3. **A29** RRF: file, custody, 9/11/2 with §2.3 IDENTICAL / §2.4b CHANGED / §4.2 IDENTICAL / §6.3 CHANGED; RRF083/RRF082 RECHECK/HISTORICAL with receipts (RRF082 reason with OSC-N2; "Old-to-current equality is not asserted"); 12 v0.8 rows keep the not-recovered limit; no RRF row CURRENT. **A32** the three owners BYTE_VERIFIED with files, custody and the pinned receiver review (ACCEPT SCOPED, 9/11/2, OSC-N2); counts 31/2/52/6 and 60/6.
- The r18 A23–A26/A28/A29/A32 controls are retired (their results stay in the pinned r18 record). New controls include: evidence left OWNER_REPORTED; owner entry left in the r18 state; r17–r18 history dropped; each new file withheld; custody hash altered; section-check output altered (§6.17 / §6.16g reported CHANGED, §2.4b reported IDENTICAL); receiver review altered; r18 record altered; DYAD6418 / RECOG rows left OWNER_REPORTED; pins silently moved to the new versions; DYAD6413 / RRF082 promoted or given BYTE_VERIFIED_HERE without the file; RRF083 promoted to UNCHANGED_VERIFIED or CURRENT, §2.4b reported identical, receipt without the non-equality limit; RRF082 OSC-N2 correction dropped; a v0.8 row given current-file verification as pin verification; G9/1 or G9/3 audits closed; the wrong 10/10/2 count; OPEN-A claimed closed; a fourth row promoted (count 32).

## 6. Replay

```
unzip RER_phaseA_r19.zip && cd RER_phaseA_r19
sha256sum -c SHA256SUMS.txt
python -I -B build_phaseA.py      # out/* byte-identical
python -I -B check_phaseA.py --tamper   # 34/34 PASS, 140 controls, exit 0
```

Determinism was verified here by two clean extractions (byte-identical `out/*` and checker output). `python -I` ignores `PYTHONDONTWRITEBYTECODE`; caches were removed before manifesting and the manifest excludes them (gate A30).

## 7. Not done in r19 (unchanged open items)

G9/1–G9/3 per-reference audits; G2 §5b; two ER-2B blocks; F3-N7N8 regional/global Stage-2 certificate; RRF v0.8 original bytes; DYAD6413/RRF082 file-level verification here; RER G10 dated "v0.8.3 … governs" wording (later authorized consumer-source maintenance).
