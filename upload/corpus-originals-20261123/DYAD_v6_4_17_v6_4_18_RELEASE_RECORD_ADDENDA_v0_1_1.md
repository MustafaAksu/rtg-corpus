# DYAD v6.4.17 and v6.4.18 — Release Record Addenda — v0.1.1

**Date:** 21 October 2026 · **Owner:** Dyadic DSN (Claude) · **Status:** `[SESSION]` successor addenda (ATLAS FB-DYAD-17, P2). Not adopted; noncanonical until the PI records otherwise.

**v0.1.1** supersedes v0.1 (`5b1730af95f788142a33cda04faa28b92442d0e6e2b2dbea8615d07c2d1c9570`, unchanged). The only change: the full SHA-256 of both release records, measured directly by the external reviewer in the r1 review of 21 Oct 2026 (§2, §3, §6). The owner has not re-measured them; the record files are not in this session.

- The adopted DSN files v6.4.17 and v6.4.18 and their release records are **not modified**. This record annotates them, as promised in `DYAD_REPLY_TO_RECOG_G3_v0_1_2.md` §1 and §4.
- No Dyadic OPEN status, RID or scientific grade is changed by this record.
- No notice is sent by this record.

## 1. Why addenda are needed

Both release records were written before external verification and both say "verification pending". The reviewer's verification reports came later and are identified only in the reports themselves and in the DYAD reply to RECOG G3. This record attaches them to the release records.

## 2. Addendum to the v6.4.17 release record

| Item | Value |
|---|---|
| Adopted file | `RTG_DYADIC_OSCILLATOR_DSN_v6_4_17.md` — SHA-256 `e07cf2b93b532554d9e1d05d2bfef3be34829b7cb892627c0bb03d1d182d4bfc` |
| Predecessor | v6.4.16 — `33c14c5cc27625c17a2b78be74e070ae61b5c7399ded49a1538098735ab559e0` |
| Release record | `9e7bfc633acfb1bfbf6e42d79f01145569eed731bf200476df74c729c7e9847c` — reviewer-measured (r1 review, 21 Oct 2026); agrees with the prefix and suffix `9e7bfc63…847c` in the v6.4.17 verification report |
| External decision | `RELEASE VERIFICATION PASSED — ADOPTED` (19 Oct 2026) |
| Verification report | SHA-256 `c0ef4446bdb2474d81cf6c218b8971a229ce82d7195273c11d2d00dc18611e39` (the report as received by the owner) |

**Report contents** (reviewer-executed, as stated in the report):
- final SHA match; release record `9e7bfc63…847c`; N13 `83dc8f57…d21c`; release ZIP `c4568707…dc6d`;
- inventory 29/29;
- clean-folder rebuild v6.4.16 → r1 → final, byte-identical;
- draft checker 13/13 with negative controls 7/7; release checker 12/12 with negative controls 6/6;
- P5 certificate 28/28, JSON hash match;
- all three diffs applied byte-exactly;
- RIDs 126 → 129, none lost;
- approval to send N13.

**Limits stated by the reviewer:**
- the project copy under `claude/` was not hashed back;
- RECOG's internal Arb certificate for R9 was not re-proved.

**Evidence level of this addendum:** a record of an external decision. The identities above are copied from the DYAD G3 reply, which quotes the reviewer report; the report file itself is not re-hashed in this session.

## 3. Addendum to the v6.4.18 release record

| Item | Value |
|---|---|
| Adopted file | `RTG_DYADIC_OSCILLATOR_DSN_v6_4_18.md` — SHA-256 `f70308f19f5955c0597c03a27b572abfd4c8746aef6922c959675eb0d56e458d` |
| Predecessor | v6.4.17 — `e07cf2b93b532554d9e1d05d2bfef3be34829b7cb892627c0bb03d1d182d4bfc` |
| External decision | `RELEASE VERIFICATION PASSED — ADOPTED` (20 Oct 2026) |
| Verification report | SHA-256 `473b6aaa5e1b96c4cc0eee539b3313ffc1860a08c57a60dbeba8af191762db27` |
| Release record | `0e8a58b6545bd0330232f4044ee541b01f6d8338069b4873e816d3ebb0506076` — reviewer-measured (r1 review, 21 Oct 2026); no earlier identifier to compare with |
| Later status | historical adopted release since v6.4.19 (`40c9e63f…6ec9`) was verified (`RTG_DYADIC_v6_4_19_RELEASE_VERIFICATION_RECORD.md`) |

**Owner check, v6.4.17 → v6.4.18** (from the G3 reply §2, owner-run on the adopted files): the RECOG-consumed passages §6.9, §6.11, §6.14, the OPEN 12 block and §7 up to "Outbound notices" are byte-identical; §1 keeps every v6.4.17 line and adds one summary line (§6.17). The v6.4.18 changes are confined to header metadata, the §1 summary line, OPEN 20, the §5 scope row, §6.17, the N14 row, §8 and Appendix A. No adopted RID is renamed or regraded.

## 4. RECOG editions and receipts (FB-DYAD-17 items)

**Editions** — kept separate:

| RECOG edition | SHA-256 | State | Use in Dyadic |
|---|---|---|---|
| v0.3.20 | `fdb8c9a72cbea67bae339a890f440b7d67c608979f7886279e2cd00bdabfb8df` | FROZEN (G1 freeze record `RECOG-ART-FREEZE-0320`, `5c00f66dae7d4de6ccd4a04d642a23edfc861bbd6bd55e432513747fbd679b55`) | historical `[import: RECOG v0.3.20 §…]` pins, kept |
| v0.3.21 | `a3459522c8f58204f83f5e65e3d1a99912f9651d1c17cc4fb0c090196f670ae3` | adopted 20 Oct 2026; superseded | — |
| v0.3.22 | `0dcce9e44d48fbedbcd5af083283fce12560cc17a3951a7632ff0e50db44bcd9` | adopted 20 Oct 2026; current | current-edition row in v6.4.20 DRAFT r1 §7.0 |

The v0.3.20 pins are kept. `p2_source_checks.py` S2 shows that every v0.3.20 paragraph carrying one of the seven cited RECOG RIDs occurs byte-identically in v0.3.22, so the pins are content-equivalent. Theorem custody is unchanged: the results stay RECOG's.

**Receipts** — as recorded in RECOG v0.3.22 §7.2 (one recipient: RECOG):

| Notice | RECOG state | RECOG use |
|---|---|---|
| N10 (v6.4.14) | RECEIVED | none; per-block chart statements, no RECOG claim made from them |
| N11 (v6.4.15) | RECEIVED | reference import for the SG-R14 quantitative note only (rows not mixed) |
| N12 (v6.4.16) | RECEIVED | none |
| N13 (v6.4.17) | RECEIVED; used from v0.3.22 adoption | used in `RECOG-THM-A1A-CD-PRIMITIVE-EXPANSION` (§6.13b) at the v6.4.18 pin, R9 premise discharged by RECOG's own R9 |

RECOG's verification field for N13 says the v6.4.17 release verification was "owner-reported, the report itself not independently read here". This record does not change that: RECOG decides whether to read the report.

## 5. Where these addenda land in v6.4.20

v6.4.20 DRAFT r1 §7.0 (unchanged in DRAFT r2) carries the edition table and the historical-pin note; its notice-state table carries the receipts above. The release records themselves stay as they are.

## 6. Carried open

- Whether RECOG reads the v6.4.17 verification report itself (RECOG decision).
- Owner re-measurement of the two release-record hashes in §2 and §3, when the record files are available to the owner (evidence level now: REVIEWER-MEASURED only).
