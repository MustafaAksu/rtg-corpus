# RER Phase A r20 — change record (21 Oct 2026, preparer)

**Role.** PREPARER_ROLE. Describes what r20 changes relative to r19 and how to replay it. Not an acceptance, grade or PASS/FAIL judgement of any record.

**Authorization.** Receiving review of OWNER_SECTION_CHECK_r2 (21 Oct 2026; ACCEPT SCOPED; file `inputs/receiving_review_owner_section_r2_20261021.md`), **§6** "Phase A r20 — explicitly authorized preparation scope", items 1–7. r20 is AUTHORIZED_TO_PREPARE, not yet reviewed.

**Locator correction (receiver r19 review §6; item 7).** The r19 change record cited the owner-section receiving review's **§5** as the r19 authorization; the authorization table is its **§6** (§5 is the scientific consumer review). Recorded here only; the accepted r19 bytes are not rewritten.

## 1. What does not change

- Source RER v0.2 DRAFT r4.13 `e92991bd…368c`; Phase A r19 `683046e7…fe06` kept as history (`inputs/phaseA_r19_outputs/` incl. its 34/34 checker record; gates A24, A25, A28).
- Registry identical to r19 except `schema` → `RER-REGISTRY-PHASEA/20` (20 records, 4 gap entries, grades, OPEN items, receipts, adoption PENDING).
- All 91 pins (cited version/hash), line ranges, cited paths, package-presence flags; currency and status of every row; `owner_current` (Dyadic v6.4.19 / RECOG v0.3.22 / RRF v0.8.4 BYTE_VERIFIED, r19 evidence); the SYNC-DYAD-OPEN20-BINF receipt and disposition; the 13 gap-reference audits (PENDING_PER_REFERENCE_AUDIT); the 6 BLOCKED rows and the two ER-2B blocks.
- No adoption, freeze, publication, repin or G10 text maintenance.

## 2. The two-row change

| Row | r19 | r20 |
|---|---|---|
| RER-DYAD-FORMAL-INVOLUTION / RECORD_IMPORT / 0 / **DYAD6413** (pin v6.4.13 `5958f7fe…8542`) | PRINTED_ONLY, RECEIVER_BYTE_VERIFIED, no file | **BYTE_VERIFIED_MATCH, BYTE_VERIFIED_HERE**, `sources_available/DYAD6413__RTG_DYADIC_OSCILLATOR_DSN_v6_4_13.md` (187,458 bytes), FULL_FILE_HASH |
| RER-DYAD-FORMAL-INVOLUTION / RECORD_IMPORT / 1 / **RRF082** (pin v0.8.2 `f09dbb12…5461`) | PRINTED_ONLY, RECEIVER_BYTE_VERIFIED, no file | **BYTE_VERIFIED_MATCH, BYTE_VERIFIED_HERE**, `sources_available/RRF082__RTG_RRF_REPRESENTATION_REGISTRY_v0_8_2.md` (88,773 bytes), FULL_FILE_HASH |

Both rows keep **RECHECK_IN_PHASE_B / HISTORICAL** — the section check r2 shows the cited OPEN 20 / §6.17 (Dyadic) and §2.4b / §4.2 (RRF) changed between the pinned and the current editions (OPEN 19 / §6.15 / §6.16 and §2.3 identical); whole-row old-to-current equality is not asserted. Only six fields differ per row vs r19: `bytes_status`, `authentication`, `available_file`, `inspection_extent`, `currency_reason` (r20 paragraph appended), `receiver_note` (r20 sentence appended; the receiver's 19 Oct recovery stays as the dated earlier report, not relabelled).

Derived lists: `bytes_not_available_to_preparer` and the blocked register's `byte_availability_gap.keys` lose exactly `DYAD6413` and `RRF082` (now 12 keys; RRF08_ADOPTED still listed — v0.8 not recovered).

Counts: statuses **31 / 2 / 52 / 6** (unchanged); authentication **62 / 4 / 24 / 1** (r19: 60/6/24/1) — equal to the receiver's expectation.

## 3. Custody (`inputs/source_custody_r20.json`)

Files came from the receiver source transfer `RER_HISTORICAL_SOURCE_TRANSFER_20261021.zip` (`efb824cc790052c5d2a7299ef8bf8fe0581e141f7cdc648c19d340d10a1e30af`, 4/4 manifest; pinned intact at `inputs/`), uploaded by the PI; hashed on receipt and again on copy. The receiver's archive/member chain (`TRIAD_RER_RECEIVING_REVIEW_20261019.zip` `9bfeca62…37c12` → previous owner-section handoff → transfer kit) is copied under `receiver_declared_chain` as RECEIVER-REPORTED, not replayed here; **external custody before the 19 Oct archive stays NOT_REAUTHENTICATED**. Container chain status PREPARER_DECLARED for the preparer-side steps. Preparer-local and receiver-local attributions are kept separate throughout.

## 4. Section check r2 pinned

`inputs/OWNER_SECTION_CHECK_r2.zip` (`e149b349…4a10`, intact archive — this also covers its nested historical `inputs/SHA256SUMS.txt`, receiver note **OSC2-T2**) and the extracted script, note and outputs in `inputs/owner_section_check_r2/`. Gates A23/A29 read `compare_output.txt` (Dyadic v6.4.13 → v6.4.18/v6.4.19: OPEN 19, §6.15, §6.16 IDENTICAL; OPEN 20, §6.17 CHANGED, §6.17 7/8 paragraphs retained; RRF v0.8.2 → v0.8.3/v0.8.4: §2.3 IDENTICAL, §2.4b and §4.2 CHANGED — OSC-N2 reproduced; §4.2 6/6 paragraphs retained) and `negcontrol_output.txt` (4/4 caught).

**OSC2-T1 (receiver):** in the r2 `--negcontrol` log the post-mutation file hash is printed with the pre-mutation `MATCH` label (display only; the section-level detection is correct and the normal-run hash checks are correct). The r2 bytes are kept unchanged as accepted; the note is carried here and in the r20 watch item. The r20 Phase A checker's own file/input controls do not have this pattern (they report only whether the named gate fails).

## 5. Package changes

Added: the two source files; `inputs/source_custody_r20.json`; `inputs/RER_HISTORICAL_SOURCE_TRANSFER_20261021.zip`; `inputs/OWNER_SECTION_CHECK_r2.zip`; `inputs/owner_section_check_r2/` (6 files); `inputs/receiving_review_owner_section_r2_20261021.md`; `inputs/receiving_review_phaseA_r19_20261021.md`; `inputs/phaseA_r19_outputs/` (5 outputs + `check_phaseA_output_r19.txt`); `patch_r20.py`; this record. Removed: r19 change record and `patch_r19.py` (in the r19 package). Catalog: `DYAD6413` and `RRF082` reasons/notes appended, `_about` appended, `_catalog_checked` → r20, `_source_authority` Dyadic/RRF historical-edition sentences. All new inputs pinned in `PINS.json`. Schemas `…/20`. **Manifest:** `SHA256SUMS.txt` lists every file except its own root path (no basename exclusion; `__pycache__`/`.pyc` excluded and absent).

## 6. Checker

34 gates PASS; **182 negative controls** (141 tampers + 41 file/input), each fails its named gate. Re-based: **A23** (DYAD6413 row byte-verified here only with the file, custody r20 incl. the NOT_REAUTHENTICATED boundary and receiver archive hash, and the r2 output; currency RECHECK/HISTORICAL; 19 Oct receiver note kept), **A24** (+ r19 record), **A25** (registry = r19 except schema), **A28** (vs r19: exactly the two rows differ, only in the six byte-availability fields; pins/lines/paths/currency/status/verified hashes unchanged; owner_current, warning, blocked list, G9 audits unchanged; missing-bytes lists lose exactly the two keys), **A29** (RRF082 analogous; OSC-N2 reproduced; 4/4 r2 controls), **A32** (62/4/24/1; transfer and r2 archives intact; receiver reviews r1/r19/r2 pinned; watch item carries OSC2-T1/T2 and the §5 → §6 correction). New controls include: either file withheld; custody hash or boundary altered; receiver archive hash altered; r2 output reporting §6.17 / OPEN 19 / §4.2 / §2.3 otherwise; r2 control log altered; rows left in the r19 state; promotion to UNCHANGED_VERIFIED / VERIFIED / CURRENT; silent repin to v6.4.19 / v0.8.4; non-equality limit or OSC-N2 replay removed from reasons; receiver 19 Oct report relabelled as a preparer run; a third row given the change; line range or package-presence flag changed; missing-bytes list keeping a recovered key or dropping a still-missing one; blocked register gap keys/note altered; ER-2B record dropped; owner_current evidence changed; G9/1 closed; SYNC disposition dropped; r2 review authorization sentence removed; archives altered; r19 record altered; counts 61/5 or 63. Retired: r19's "upgraded without the file" controls and the r18-based A28 controls (results in the pinned r19 record).

## 7. Replay

```
unzip RER_phaseA_r20.zip && cd RER_phaseA_r20
sha256sum -c SHA256SUMS.txt
python -I -B build_phaseA.py          # out/* byte-identical
python -I -B check_phaseA.py --tamper # 34/34 PASS, 182 controls, exit 0
```

Two clean extractions here gave byte-identical `out/*` and checker output; no bytecode cache created or listed.

## 8. Still open (unchanged)

RRF v0.8 original (12 RRF08_ADOPTED pins); G9/1–G9/3 per-reference audits; G2 §5b; two ER-2B blocks; Stage-2 regional/global certificate and multi-step error control; G10 dated wording (watch item only; separate authorization).
