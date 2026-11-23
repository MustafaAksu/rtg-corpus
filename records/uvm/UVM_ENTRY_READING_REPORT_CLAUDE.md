# OPEN M (UVM) — Entry Reading Report (Claude)

**Status:** [SESSION] / NONCANONICAL. Deliverable A of `records/atlas/ATLAS_ADVISORY_UVM_REACTIVATION_20261121.md` §5 and BOOTSTRAP 1 of `records/uvm/UVM_COOWNER_SESSION_ORIENTATION.md`. Read-only entry and source audit. No DSN edit, no pipe disposition, no certificate run, no merge or tag. Nothing here adopts, grades or re-grades UVM science.
**By:** Claude, UVM scientific co-owner — preparer and triage owner by PI assignment of 21 November 2026. No authority to adopt science; every edition, scope and campaign decision is the PI's.
**Checkpoint:** `MustafaAksu/rtg-corpus` `main` `a79e420c7ea0e1fde189e2ca0caeb67747e9d97b`; tags and open PRs queried 2026-11-22 14:03–14:10 UTC (17:03–17:10 +03:00). Access mode: shell clone (depth 1 per ref) with all 61 tags fetched; `gh` REST for PRs. These are observations at that time, not standing facts.
**Independence:** written before opening §3 of the 21 November advisory, before reading Atlas L5 rows `OPENM.U1–U11`, and before any other co-owner report existed (no `chatgpt/uvm-entry-reading-report` branch at query time). Details in §(e).

Evidence keys are those of Methodology v1.4 §12.2. "Derived copy" has the meaning given in §(a).4.

---

## Summary of what the PI and the second co-owner should look at first

1. **The governing edition is identified by bytes, not by a release record.** `uvm-v0.7.1` → `dsn/RTG_OPEN_M_DSN.md`, SHA-256 `0a51644d…f53e`, equal to `BASELINE.md` and to RER v0.2 §7 (`EV-HASH`), and `main` equals the tag. All ten named v0.7 / v0.7.1 governance documents are absent, so the 7 October 2026 owner adoption is header-reported only (`EV-SRC-REPORTED`).
2. **No UVM certificate script, output or data pack is in the repository.** Every `[ALG]`/`[NUM]` certificate statement in §6/§8 is `EV-SRC-REPORTED`, `EV-NOT-RERUN`.
3. **Genesis v2.8.5 bytes are recoverable and hash-match** (§(a).4): reverse-applying the frozen `GENESIS_v2_8_5_to_v2_8_6_DRAFT.diff` to the frozen v2.8.6 draft, both inside `upload/gen-records/GENESIS_V2_8_6_DRAFT_PACKAGE.zip`, yields a file with SHA-256 `41ed7660…75cf`, the value recorded for adopted v2.8.5 by RER v0.2 §7 and by the Genesis v2.8.6 release record. The orientation note and `records/gen/GEN_UPLOAD_HASH_CHECK_20261024.md` list these bytes as missing. Nothing was placed in the repository; custody is the PI's decision.
4. **With that copy, every Genesis statement UVM imports was compared line by line against `gen-v2.10`:** all are byte-identical except the κ → κ_f renaming and one newly assigned RID (§(b).2). Dyadic v6.4.10, Triadic v1.6 and OFN v0.8 remain without bytes: old-side comparisons UNVERIFIED.
5. **Ten source-level observations for the discrepancy list** (§(d).5), of which the ones with scientific content are: the `0.024` target also inherits the single-jet hypothesis, which v0.7.1's condition lists do not name (O1); several UVM formulas assume `m > 0` while Genesis now records `B_*` as undefined with unknown sign (O2); `THM-3G` has no claim block, grade, RID or artifact row (O3); the pack `T100` is reported with `nm=2` in §2 and `nm=0` in §6 R14 (O4).
6. **The PI-decided `0.403` correction is confirmed against bytes, and has a second site** (§(b).6): the value is Pre-Legacy v0.8 §1.9; Legacy v0.7 does not contain it; the misattribution occurs at DSN line 271 (R12) and also at line 107 (OPEN-M-2D).

---

## (a) Manifest — what was actually read

### (a).1 Files read, with identity

| Object | Ref | SHA-256 | Extent read | Evidence |
|---|---|---|---|---|
| `CONVENTIONS.md` | `main` a79e420 | not hashed | full | `EV-SRC-READ` |
| `records/uvm/UVM_COOWNER_SESSION_ORIENTATION.md` | `main` | not hashed | full (includes one Atlas paragraph, see §(e)) | `EV-SRC-READ` |
| `dsn/RTG_OPEN_M_DSN.md` (v0.7.1) | `uvm-v0.7.1` | `0a51644de0a15035797ab03945207cf319fd6d7514a04b8cae441d9d6e93f53e` | **full**, 444 lines / 92,170 bytes, header to footer | `EV-SRC-READ`, `EV-BYTES`, `EV-HASH` (= BASELINE, = RER v0.2 §7) |
| `BASELINE.md` | `main`; also at the baseline commit | not hashed | full | `EV-SRC-READ` |
| `pipes/README.md`, `pipes/UVM/INDEX.md`, four items | `main` | item hashes in §(c) | full | `EV-SRC-READ`; `tools/pipes_index.py --check` → `pipes OK: 147 items in 20 inboxes` (`EV-RUN`, structural only) |
| RER v0.2, `noncanonical/RTG_RELATIONAL_EMERGENCE_REGISTRY.md` | `rer-v0.2` | `58feee5ff1f16a37fc4ee029f24499928ea7439731de0a090d8794c1cbe57ad0` | §7 source table and its evidence vocabulary; nothing else | `EV-SRC-READ`, `EV-HASH` (= BASELINE) |
| Pre-Legacy v0.8 | `prelegacy-v0.8` | `22ecf37869cd1192b7fc3a13efe364d6cc2644928f4ecf5afe38e0ad8b95a446` | targeted: quick table, §1.2, §1.3, §1.4, §1.9, §1.12, §3 SG-PL-13, §6.2, §6.3, Appendix A v0.8 lines; all occurrences of `0.403`, `β₁`, `void`, `OPEN M` | `EV-SRC-READ`, `EV-HASH` |
| Legacy v0.7 | `legacy-v0.7` | `3b707c90eb5e048717513c6ba161b738d0d1d4cd341eb0a125fb15779afd7e13` | string search only (`0.403`, `40.3`, `β₁`, `void`, `cooled`, `η`) | `EV-HASH`; search, not a reading |
| Genesis v2.10 | `gen-v2.10` | `63c3b020d9c63a43a2e5e9a43c411fad2d07dfcab33995bd928683435bb13d62` | targeted: status summary, §1 lines 67–76, §2 OPEN M entry and OPEN-GEN-II-7B/9/9B/9C, §3 SG-6, §6.7, §6.8 face-lift block, §6.9 9A/9C lines, §7 UVM export row, §8 rows named in §(b).2 | `EV-SRC-READ`, `EV-HASH` |
| Genesis v2.9, v2.8.9 | `gen-v2.9`, `gen-v2.8.9` | `9178ca2c…00ac`; `d143673e…c6fc` | extracted and hashed; not read beyond the v2.9 release record lines 59, 218–220 | `EV-HASH` (v2.9 = tag message) |
| Genesis v2.8.5 (derived copy) | no tag | `41ed76602c1c87c42972ac5b3f0a53f6973ac484427473ac371c57db1ab475cf` | header; §2 OPEN M entry and 7B/9B/9C; §3 SG-6; §6.6 line 803; §6.7; §6.8 line 822; §6.9 lines 866, 903, 905; §8 rows; GCL references | `EV-SRC-READ`, `EV-HASH` against two recorded values; **derived, not a received original** |
| Dyadic v6.4.24 | `dyad-v6.4.24` | `10fbdacc19544596480acae03faeba076f21103a01b903a8d3305cfa8ed7bc16` | targeted: §1 lines 81, 103, 109; §2 lines 127, 225; SG-15; §5 rows on OPEN-M; §6.2 line 467; §6.11 line 676; §6.12 lines 743–745; §6.14 line 778; §7.0 line 1117; Appendix C R11 row | `EV-SRC-READ`, `EV-HASH` |
| Triadic v1.7 | `triad-v1.7` | `506f3403628ca01d5a904f885df055d9bfbdf1ef5e474e24e83d4797c122e64a` | targeted: header, §1 T-6s/t/u lines, SG-17, §6.17 table and `[COR]`, §7.4 notices and consumer-state matrix | `EV-SRC-READ`, `EV-HASH` |
| Triadic v1.6.1 | `triad-v1.6.1` | `95340abe57e999ed48681502152113d8fdb3102f74f45a25aa66c2d0092d451f` | line comparison with v1.7 only | `EV-HASH` |
| OFN v0.12 | `ofn-v0.12` | `55ff8ba85d4bb48b52266bdd9a44aa84efcd2cc19903d059266fa406a6bb76aa` | lines naming OPEN M / UVM; OPA entries (lines 338, 908–914); RF-O08-08, RF-O08-11 | `EV-SRC-READ`, `EV-HASH` |
| OFN v0.10 | `ofn-v0.10` | `acb70a8c…5dfa` | extracted and hashed only | — |
| Programme v1.4 | `programme-v1.4` | `37d857d08bb47771ed50fc5829584be74aab120a23e922eba7c84bae097f28c0` | §6.3 UVM entry, §7.2 register framing and IF08–IF11, IF23, IF32, §7.3, §8 SG-PROG-1–4, §9.2 line 546, all lines naming OPEN M | `EV-SRC-READ`, `EV-HASH` |
| Programme v1.2 | `programme-v1.2` | `4207da05dca24256e7bc528cb9814f848838bcd98e3d01222fb2a633ec9fd359` | SG-PROG-1–4 and IF08–IF11, IF23 lines | `EV-HASH` (= `BASELINE.md` at the baseline commit) |
| Methodology v1.4 / v1.3 | `methodology-v1.4` / `-v1.3` | `cdacab5f…f2df` / `3e23ba94…ec7e` | v1.4 §1.1, §3.3, §3.4, §4.3, §8.1–8.4, §12.2, Appendix A v1.4; v1.3 by section hash comparison | `EV-SRC-READ`, `EV-HASH` |
| `records/atlas/ATLAS_ADVISORY_TO_PI_DORMANT_OWNERS_20261110.md` | `main` | `889ca8de43019894d7e3fa49779f2e4bc2a82664d0e605536fc334a900ec6188` | header (3 lines), §4 preamble, §1 row 4 and §4 row 4 only | `EV-SRC-READ` |
| `records/atlas/ATLAS_ADVISORY_UVM_REACTIVATION_20261121.md` | `main` | `81e4b102ef17fbf933dd600aa4ef643882f55736ac882dc02e79155351ca288a` | header, §1, §2, §5, §6. **§3 (lines 33–52) not opened. §4 (lines 53–65) also not opened**, by my own choice, to keep §(c) independent | `EV-SRC-READ` (partial) |
| `records/gen/GEN_v2_9_RELEASE_RECORD.md`, `GEN_v2_10_RELEASE_RECORD.md` | `main` | not hashed | lines naming UVM only | `EV-SRC-READ` (partial) |
| `upload/gen-records/` (README, `SHA256SUMS.txt`, `GENESIS_V2_8_6_RELEASE_RECORD.md` lines 12, 20; zip listings) | `main` | zip `7c50d62a…4dfc` = its `SHA256SUMS.txt` line | as stated | `EV-HASH` |

**Not read:** `atlas/RTG_STATE_ATLAS.md` (not opened at all); advisory §3 and §4; any other co-owner's report; RER beyond §7; Genesis, Dyadic, Triadic, OFN, Programme and Methodology outside the sections listed; the DZT, AZ, RECOG, NUMGEN, TDRG, RRF bodies (only a line count of OPEN-M mentions and a few matching lines in AZ and DZT were viewed).

### (a).2 Identity and adoption state of the governing edition

- Tag `uvm-v0.7.1`: annotated tag object `34de100a15bcc885fe172b9abf7af0c065987d82` → commit `d7d661c0b89c6f3d9ceea2e205bf75fccfcfbf8d` (22 October 2026 baseline merge); tag message "uvm-v0.7.1 baseline 22 Oct 2026; hash in BASELINE.md". It is a **baseline tag**, shared with fifteen other baseline tags; it is not a tag created after a release record.
- `BASELINE.md` (current and at the baseline commit): UVM row verification = "XREF: RER v0.2 §7". RER v0.2 §7 row `OPENM`: "archived v0.1 source pin; ARCHIVED_SOURCE_STATUS", same hash. That is a source-identity cross-reference, not a UVM owner release record.
- `tools/orient.py UVM …` (`EV-RUN`, 14:03 UTC): newest tag `uvm-v0.7.1`; main equals tag; release record `None` → "adoption UNVERIFIED"; one commit after the tag on study paths (PR #356, the entry note); open PRs scanned 5, matched 0; inbox `{'open': 4}`.
- The DSN header reports: owner adoption 7 October 2026; revision base v0.7 SHA-256 `fea80656…7540`; accepted candidate `…v0_7_1_DRAFT2.md` SHA-256 `ebbf23ea…db95`. Neither hash matches any file or zip member in the tree. Both stay `EV-SRC-REPORTED`.
- Open PRs at query time: #347, #287, #189, #183, #160; none touches a UVM path.

### (a).3 Missing originals

Search coverage: all 3,000 tracked files at `main` a79e420 hashed and matched by name; all 46 zip files opened, 738 members (nested zips to depth 2) hashed and matched by name. **Git history and non-`main` branches were not scanned** (shallow clone): for those, UNVERIFIED. "Not found" below means not found in that coverage, not lost.

| Group | Names | Result |
|---|---|---|
| v0.7.1 governance (header, §8) | `RTG_OPEN_M_v0_7_1_OWNER_ADOPTION.json`; `RTG_OPEN_M_v0_7_1_RELEASE_RECORD.md`; `RTG_OPEN_M_DSN_v0_7_1_CHANGE_RECORD.md`; `RTG_OPEN_M_v0_7_1_RELEASE_VALIDATION.txt` | not found (4/4) |
| v0.7 governance (§8) | `RTG_OPEN_M_v0_7_OWNER_ADOPTION.json`; `RTG_OPEN_M_v0_7_RELEASE_RECORD.md`; `RTG_OPEN_M_v0_7_DRAFT2_VALIDATION.txt`; `…_DRAFT3_VALIDATION.txt`; `…_DRAFT3_1_VALIDATION.txt`; `RTG_OPEN_M_DSN_v0_7_DRAFT3_1_CHANGE_RECORD.md` | not found (6/6) |
| Predecessor editions | UVM v0.7 (`fea80656…`), v0.7.1 Draft 2 (`ebbf23ea…`), v0.6 and earlier, the "v0.5 addendum" cited at DSN line 121 | not found |
| §8 scripts and notes | `uvjet_equivariant_classification.py`; `open_m_constraint_scope.py`; `open1_liegauge_candidate.py` (+ "ledger"); `thm_m_lock_certificate.py`; `bch_two_face_word_probe.py`; `bch_minimal_jet_assembly.py`; `open_m_doc_consistency_check.py`; `hodge_decomposition_audit.py`; `harmonic_localization_invariant.py`; `open_m_2e_panel.py`; `open_m_2f_trajectory.py`; `open_m_2f_zh2_weighted.py`; `open_m_2f_staircase.py`; `open_m_2f_rho_assembler.py`; `esm_harmonic_report.py`; `EDIT_A_wiring_instructions.txt`; `t103_defect_carrier_test.py`; `single_sandwich_dichotomy_certificate.py` | not found (18/18: 17 scripts and one wiring note) |
| §7-only script | `open_m_3g_mini_protocol.py` (THM-3G certificate; named in §7, has **no §8 row**) | not found |
| Data | ESM packs and growth series (RUN05, RUN10, RUN11, T80…T120, T100, T103); script outputs | not found. R14 and §8 say "PI-reproduced on repo data" without naming the repository; it is not `rtg-corpus` |

There is no `evidence/uvm/`; `records/uvm/` held only the orientation note before this report.

### (a).4 Historical pinned editions

| Pin in UVM v0.7.1 | Tag | Recorded SHA-256 (where recorded) | Bytes |
|---|---|---|---|
| Genesis v2.8.5 | none | `41ed7660…75cf` (RER v0.2 §7 `GEN`; `GENESIS_V2_8_6_RELEASE_RECORD.md` line 12) | **derived copy available, hash-matched** (below) |
| Dyadic v6.4.10 | none | `74558119…56b7` (RER v0.2 §7 `DYAD`; RRF v0.8.4; RECOG records) | not found |
| Triadic v1.6 | none (`triad-v1.6.1` exists) | `c768687c…5b36` (RER v0.2 §7; Triadic v1.6.1 release records) | not found |
| OFN v0.8 | none (`ofn-v0.10` exists) | `56bc991d…a514` (RER v0.2 §7; RECOG records) | not found |
| Programme v1.2 | `programme-v1.2` | `4207da05…d359` (BASELINE at the baseline commit) | at tag, `EV-HASH` |
| Methodology v1.3 | `methodology-v1.3` | `3e23ba94…ec7e` (BASELINE; RER v0.2 §7) | at tag, `EV-HASH` |
| Pre-Legacy v0.8 | `prelegacy-v0.8` | `22ecf378…a446` (BASELINE, "PI") | at tag, `EV-HASH` |

**Genesis v2.8.5 — derived copy.** `upload/gen-records/GENESIS_V2_8_6_DRAFT_PACKAGE.zip` (SHA-256 `7c50d62a…4dfc`, equal to its line in `upload/gen-records/SHA256SUMS.txt`) contains `RTG_GENESIS_GEOMETRY_DSN_v2_8_6_DRAFT.md` and `GENESIS_v2_8_5_to_v2_8_6_DRAFT.diff`. Reverse-applying the diff reproduces the recorded v2.8.5 hash exactly (`EV-RUN`, twice, GNU patch 2.7.6):

```bash
Z=upload/gen-records/GENESIS_V2_8_6_DRAFT_PACKAGE.zip      # run from a checkout of main
mkdir -p /tmp/gen285
unzip -p "$Z" RTG_GENESIS_GEOMETRY_DSN_v2_8_6_DRAFT.md > /tmp/gen285/RTG_GENESIS_GEOMETRY_DSN_v2_8_5.md
unzip -p "$Z" GENESIS_v2_8_5_to_v2_8_6_DRAFT.diff      > /tmp/gen285/v285_to_v286.diff
patch -R --binary -s /tmp/gen285/RTG_GENESIS_GEOMETRY_DSN_v2_8_5.md /tmp/gen285/v285_to_v286.diff
sha256sum /tmp/gen285/RTG_GENESIS_GEOMETRY_DSN_v2_8_5.md
# expected: 41ed76602c1c87c42972ac5b3f0a53f6973ac484427473ac371c57db1ab475cf   (149,799 bytes)
```

What this is: a byte sequence whose hash equals the value two independent records give for adopted v2.8.5; its header reads "RTG_GENESIS_GEOMETRY_DSN_v2.8.5 … 5 October 2026 … ADOPTED owner ledger" with the same companion set UVM pins (Dyadic v6.4.10, Triadic v1.6). What it is not: a file received from its original custodian. I use it below as verified source bytes for comparison and label every such use "v2.8.5 (derived)". Whether it is accepted as the reference copy, and whether it is placed anywhere, is for the PI and the Genesis owners. I found no comparable route for Dyadic v6.4.10, Triadic v1.6 or OFN v0.8 in the searched coverage.

---

## (b) Pins, imports and grades

### (b).1 Pin by pin

| Pin | What UVM uses it for | Old-side bytes | Comparison with the governing edition |
|---|---|---|---|
| Genesis v2.8.5 (IF08) | §1 frame, no-go, 9B/9B-tau/9C, norm typing, 7B target, SG-6, dependency map, GCL-01–08 readings | derived, `EV-HASH` | done statement by statement, §(b).2 |
| Dyadic v6.4.10 (IF10) | `B`, `J_Q`, `μ_6`, `τ`, `λ=e^{iF_f/2}`, chart data; archival `h_3=0` vs adopted `h_3≠0`; `DYAD-CAND-P0-DYADIC` | none | **UNVERIFIED** on the old side. Current side read at `dyad-v6.4.24`: line 81 (archival `h_3=0`), line 778 (`h_3≠0`, channels (3,0),(1,2),(0,3)), SG-15 and `DYAD-CAND-P0-DYADIC` `[CAND]` `[scope: conditional]` agree with what UVM states. Dyadic's own "`[COR]` `[v6.4.10]`" labels are current-owner statements about the old edition, not old bytes |
| Triadic v1.6 (IF11) | T-6s, T-6t, T-6u, SG-17, CN-01–CN-05 | none | **UNVERIFIED** for v1.6 → v1.6.1. For v1.6.1 → v1.7 (both `EV-HASH`): the T-6s, T-6t, T-6u owner lines, their `[ALG]` claim lines, SG-17 and the CN-02, CN-03, CN-05 notice headers are byte-identical; CN-01 and CN-04 differ only in the status clause now pointing to the §7.4 matrix. Numbers UVM quotes (`16/√7 > 6`, benchmark `√2`, `√21/64`) are in v1.7 lines 83, 702–720 |
| OFN v0.8 | OPA relevance for OPEN-M-7 only | none | **UNVERIFIED** on the old side. `ofn-v0.12`: OPA is OPEN (`RTG-OFN-OPEN-OPA`, lines 338, 908); line 913 "UVM-OPEN-OPA-LINK is a hypothesis, not a premise resolving OPA"; RF-O08-08 and RF-O08-11 restate UVM v0.7.1 without strengthening it |
| Programme v1.2 | SG-PROG-1/2/4, tier/ownership | at tag | SG-PROG-1–4 lines **byte-identical** v1.2 → v1.4. IF08–IF11, IF23 keep their identifiers; v1.4 records UVM's pins as v2.8.5, v6.4.10, v1.6, v0.8 and states "A pin older than the governing edition is the consumer's declared state, not a defect" |
| Methodology v1.3 | grammar and discipline | at tag | §3.3, §3.4, §4.3, §8.1, §8.4 **byte-identical** v1.3 → v1.4. Changed or new: §1.1 live-file rule, §12.2 evidence keys, §13.5–13.9. v1.4 Appendix A: "No scientific result, RID, grade or OPEN status in any DSN changes" |
| Pre-Legacy v0.8 (IF23) | ladder, `Δω*`, ESM warnings, `K_vac` provenance, priors | at tag | same edition still governs; statement checks in §(b).6 |

No pin is classified here as intentional, stale or to be moved; that is BOOTSTRAP 2 and the owners' decision.

### (b).2 Genesis: imported statements, v2.8.5 (derived) against `gen-v2.10`

Method: for each owner line carrying the statement in v2.8.5 (derived), test whether the identical line exists in `gen-v2.10` (`EV-RUN`, exact string match; line numbers A = v2.8.5, B = v2.10).

| UVM use | Genesis statement | A → B | Result |
|---|---|---|---|
| §0.1 | `OPEN M — Quaternionic metric lift [RID: GEN-OPEN-UV-LIFT]`, with the whole registry entry including the 7B constraint-scoping block | 303–345 → 317–359 | identical (43 lines, empty diff) |
| §1.1 frame | `[DEF]` Minimal UV completion | 811 → 1008 | identical; still no RID |
| §1.1 no-go | `[THM]` Universal no-go, `T_H = T⊕T ⇒ w=0` | 809 → 1006 | statement identical; **added at v2.9:** `[RID: GEN-THM-QH-NOGO]` and "Proof source: GEN-ART-QH-NOGO (§8; not in the repository)" |
| §1.2 9C | header `[RID: GEN-OPEN-MSPIN2-ANISO]`; conditional criterion; "OPEN M target statement"; §6.9 criterion; §8 row | 473, 477, 487, 905, 1027 → 489, 493, 503, 1104, 1275 | identical |
| §1.2 9B / 9B-tau | header `[RID: GEN-OPEN-SOURCE-PAIRING]`; PARTIAL status lines; GCL-02 sign reconciliation; `K_+` remark; §8 row | 446, 448, 441, 96, 460, 903, 1026 → 462, 464, 457, 106, 476, 1102, 1274 | identical |
| §1.2 norm typing | Object-typed norm refinement (`‖gI‖_B = 2|g|`); `GEN-DEF-NORM-BNATIVE` | 216, 1028 → 228, 1276 | identical |
| §1.3 target | `(‖H‖/g)|w| ≳ 0.024` display; "which uses `‖M‖_op → 2g` and … `|α_f| ≳ 0.012`"; large-positive-`g` spectrum line; OPEN-GEN-II-7B priority line; HYP-B | 335, 336, 342, 87, 312 → 349, 350, 356, 96, 326 | identical |
| §1.3 single-jet | `[SG-6]` | 531 → 547 | identical |
| §1.3 face typing | OPEN 5/2B line; `GEN-OPEN-WPHASE` header and §8 row | 99, 163, 1020 → 109, 173, 1268 | identical |
| §1.3 phase side | Candidate #2 (GCL-07) | 148 → 158 | identical |
| R16 | ×2 cross-stream amplitude verdict, corrected GCL-08 | 214 → 226 | identical |
| §1.4 | `OPEN M_smooth ≺ OPEN 0_smooth`; OPEN 0-Regge blocked; item 1b "closed-form immediate" | 66, 102, 483 → 76, 112, 499 | identical |
| §8 scope | `GEN-OPEN-UVJET-SCOPE` | 1017 → 1265 | identical |
| R2, HYP-IDENT | face-lift display, `m = 2Q_sB_*` | 822 → 1019 | changed: `κ = |m||w|` → `κ_f = |m||w|` |
| — | new in v2.9: `[DEF]` Face-lift magnitude, sign and `B_*` (v2.10 line 1021): "`B_*` is not defined in the current owner text and its sign is unknown" | — → 1021 | **new** |
| — | scalar-M eigendecomposition: `λ± = (τ−g) ∓ κ, κ = m|w|` → `(τ−g) ∓ sgn(m) κ_f` | 429, 878 → 445, 1077 | **changed** (explicit `sgn(m)`) |
| not imported by UVM | Local sourced-junction theorem: v2.8.5 "has a valid minimizer" → v2.10 "exactly two antipodal solutions; selection of the physical branch is OPEN", `Δ₃>0` added | 62, 866 → 72 | changed; UVM v0.7.1 does not contain the word "junction" |

Reading: for the statements UVM actually imports, the pin age by itself changes no wording except notation; three things did move around them — an RID became available for the no-go, the no-go's proof artifact is now declared absent from the repository, and `B_*`/`sgn(m)` became explicit (see O2). `B_*` occurs once in v2.8.5 (derived), in the display at line 822, with no definition there either: v2.9 disclosed a gap that already existed.

### (b).3 "RID unavailable" imports

Of UVM's six "RID unavailable" Genesis imports: the no-go now has `GEN-THM-QH-NOGO`. The minimal-completion `[DEF]`, the 7B target display, SG-6 and the dependency lines still carry no dedicated RID in `gen-v2.10` (lines identical). The object-typed norm line itself has no RID, but `GEN-DEF-NORM-BNATIVE` (present already in v2.8.5 (derived), line 1028) records `‖gI‖_B = 2|g|`, and `GEN-OPEN-UVJET-SCOPE` records the conditional reduction to `{‖H‖, g}`. The GEN pipe item also names `GEN-THM-SINGLE-FACE-METRIC` and `GEN-THM-SOURCED-JUNCTION`; I found no UVM §1 import of either.

### (b).4 UVM's Import Ledger and tag grammar, against the Methodology UVM itself declares

Observed in the tagged text; none of this is a grade decision.

- §7 is a prose list per source document. It does not use the §4.3 entry format (RID :: claim :: source :: local use :: inherited scope, with `Source status / Depends on / Verification / Synchronization`), which is identical in v1.3 and v1.4. The header declares a "bounded owner-consumer migration", so this is a declared limitation.
- No `## Local Tag Aliases` block, while `[INTERP]` (2), `[INTERP/HYP]` (4), `[NUM diagnostic]` (2), `[CAND]` and `[ALG-grade symbolic]` are used. `[INTERP]` and `[NUM diagnostic]` are §8.4 example aliases but must be declared locally; `[INTERP/HYP]` is a slash mixture.
- `[RESULT]` companions outside §3.4/§8.2: `[from: DEF/RESULT registry]` (line 79), `[from: ALG/typing audit]` (line 285). §8 rows use `[ENG/RESULT provenance]`, `[ENG/NUM provenance]`, `[ALG/NUM provenance]`.
- Three Pre-Legacy imports use `[source: …]` rather than `[import: …]` (lines 81, 83, 85).
- §1 opens with "this branch asserts nothing in §1 on its own authority", but §1.3 contains two UVM-native `[COR]` guards and §1.4 a UVM-native inference ("Consequence for this branch: … candidate selection must come from structural constraints").
- Line 81 carries `[from: HYP]` for one block joining the spin-2 graviton row (Pre-Legacy: `[HYP — requires OPEN M closure…]`) and the gravity chain step 4, which Pre-Legacy §1.9 grades programme-level `[HEUR]`.

### (b).5 Identifiers

- `UVM-OPEN-2F` is declared twice: on the OPEN-M-2F registry entry (line 115) and on the result R14 / RESULT-M-2F (line 277). §8 uses `UVM-NUM-2F-TRAJ` for the same campaign's artifacts.
- R1–R11 have no result RIDs. Their only identifiers are artifact-row RIDs in §8 (`UVM-ART-EQUIV-CLASS`, `UVM-THM-LOCK / UVM-ALG-H3AUDIT`, `UVM-CONV-QPAIR / UVM-LEM-RJ / UVM-COR-R3 / UVM-THM-WORDSECTOR`, `UVM-ALG-2B-ASSEMBLY`). Consumers therefore cite by label: Dyadic v6.4.24 writes "OPEN-M R11" (Appendix C row; lines 109, 363, 415, 467, 676).
- `UVM-THM-LOCK` names a script row; R8 itself is tagged `[ALG]`. `UVM-ALG-H3AUDIT` shares that row although R9's conclusion is withdrawn.
- `LEM-M-CENTRAL`, `R-CHIRALITY-RECONCILIATION`, `HYP-2E-COUPLING` and `THM-3G` have no RID; the last two have no claim block either (O3).

### (b).6 Pre-Legacy and Legacy statements

| UVM text | Source check | Result |
|---|---|---|
| "the Legacy cooled-vacuum 0.403" — R12, line 271; "the Legacy cooled-vacuum value 0.403" — OPEN-M-2D, line 107 | Pre-Legacy v0.8: quick table line 47 (`η_irr = 0.403`, `[NUM strong]`, §1.9); §1.9 line 321 (grown `N=175`, `β₁=8`, "Cooled Vacuum"); §1.12 line 372; §6.3 line 630. Legacy v0.7: no occurrence of `0.403` or `40.3` | attribution is Pre-Legacy v0.8 §1.9. **Two sites, not one.** The PI decision of 10 November 2026 (advisory §4 row 4, "With the stream's rework (OPEN-M)") names line 271 only; the PREL side was UNVERIFIED in that advisory and is now checked against bytes. The number is not in question |
| "Connects to Legacy 'no β₁ → no vacuum'" (R12, line 271); "interpretive Legacy-aligned reading" (line 273); "the Legacy motivation that a legal β₁-type fracture may awaken graph-wide response" (line 293); Appendix A v0.6: "'no β₁ → no void' from Pre-Legacy v0.8" | Legacy v0.7 mentions `β₁` twice (line 291, a `[FAIL]` loop-onset proxy; line 849, "possible relation β₁≈8 (R0 only)") and never "void" or "vacuum" in this sense. Pre-Legacy v0.8 §1.9: `β₁` as topological matter (lines 296, 305, 307) and `[HEUR]` "void fails" (line 331) | the phrase is not literal in either file; the nearest source content is Pre-Legacy §1.9. Same family as the 0.403 attribution, **not covered by the PI decision**; for triage |
| `[source: PRE_LEGACY v0.8 §RG]` RG universality (line 83) | statement is Pre-Legacy §6.2 line 597, `[ALG]`; there is no "§RG" (§1.2 is "The RG Fixed Point") | locator imprecise; statement and grade match |
| `[source: … §1.12]` for spin-2 graviton and gravity chain step 4, `κ=−0.175` (line 81) | graviton row: §1.12 line 394. Step 4 and its OPEN M blocker, and `κ_grav=−0.175`: §1.9 lines 297, 326 | locator covers only half |
| SG-PL-13, `ℓ* ≈ 2.07 fm` (line 85) | §3 line 518 | matches |
| ERR-M-2F-THRESH five bands; "4D corridor … non-gauged per Pre-Legacy §1.4" (R14) | §1.3 table (0.28, 0.70, 1.55, 1.70); §1.4 "Why the 4D corridor … is not gauged" | match |
| `K_vac` provenance (§4, §7) | §1.5 line 190, `E_vac = ½ K_vac Σ z²` | present as a definition of the vacuum energy normalization; no statement about a spin-2 coefficient, consistent with RESULT-M-3A |

### (b).7 Methodology v1.4 normalization, informational

`tools/dsn_lint.py dsn/RTG_OPEN_M_DSN.md` (`EV-RUN`, informational, no gate): §1 = 973 words (v1.4 asks 200–400 or a header profile exception); 15 header fields, status summary 1,773 characters; Appendix A 12,570 characters over 8 editions; history phrases in live sections: "historical" 25, "superseded" 11, "former" 4. Live sections carry dated overlays ("v0.7 … correction … numerical body unchanged") next to preserved v0.6 bodies (R12, R14), and Appendix B holds a verbatim archive of the v0.7 R15 block. Under §1.1 these are layout questions for a stage-2 pass; the grammar sections UVM relies on did not change.

---

## (c) The four `pipes/UVM/` items

All four are `state: open`, `kind: notice`, and ask nothing. No state or disposition was changed. "Verified" below means the item's factual content was checked against the producer's tagged text.

| Item (SHA-256 of the file) | Content verified against | Effect on UVM, as I read it |
|---|---|---|
| `20261026-GEN-kappa-f-b-star-sourced-junction.md` (`e97061d15d6d141553c958cacc6b0888e4290475e59dffb6466f9e98b7d87695`) | `gen-v2.10` lines 1019–1021, 445–446, 1077–1078, status summary, §7 line 1234; `GEN_v2_9_RELEASE_RECORD.md` lines 59, 218–220. All three stated changes are in the owner text (`EV-SRC-READ`) | (1) `κ_f`: notation only; UVM never writes `κ` for the face-lift magnitude. (2) `B_*`: one literal use (R2, line 239), but the sign of `m` enters more UVM formulas than that — see O2. (3) Sourced-junction rescoping: no UVM statement cites the theorem; indirect only, through "OPEN M-foam blocked by OPEN M". (4) RIDs: `GEN-THM-QH-NOGO` now exists for the §1.1 no-go import; the other two named RIDs are not UVM imports by my reading (§(b).3) |
| `20261103-GEN-v2-10-adopted.md` (`5ca316ea9f6c0f778fbbd3c1271fbc0ef25cdae60341229c6ed912f0591be6d4`) | tag `gen-v2.10` and hash (`EV-HASH`); "changes nothing UVM imports" confirmed for every statement in §(b).2. The two informational results (`GEN-ALG-P4-DRIFT-IDENTITY`, the `G₂=0` route) were not read | none on imported wording. One thing neither GEN item mentions: since v2.9 the owner text marks the proof source of the no-go as "not in the repository" (the note is in `gen-v2.9` and `gen-v2.10`, not in `gen-v2.8.9` or v2.8.5 (derived)) |
| `20261103-DYAD-notices-n16-n21.md` (`159ec14aed2006b86d3832224502ea4dbe715e5698cdc124a2f437cd6109f5d0`) | `dyad-v6.4.24` Appendix C R11 row (item is tagged `dyad-v6.4.23`; that edition was not read) | no UVM statement changes. It makes visible that UVM's R-labels are the only handle consumers have (§(b).5) |
| `20261103-TRIAD-v1-7-adopted.md` (`64219b0b90aba85547ea91192a409ab7581a3ea5745988275cad1cbb8898f96d`) | `triad-v1.7` §7.4 matrix and lines compared in §(b).1. "T-6s, T-6t, T-6u unchanged" confirmed for v1.6.1 → v1.7. The v1.6 → v1.6.1 delta (CN-02 remainder `O(Q_s^{(p−3)/2})`) is `EV-SRC-REPORTED`: v1.6 bytes absent | UVM line 76 already states the GCL-06 dependence. Triadic §7.4 reads UVM v0.7.1 as: CN-02, CN-04, CN-05 received, statement accepted, adopted use "Import Ledger (§7)"; UVM §7 names the T-6 results by label, while Triadic RIDs exist (`TRIAD-ALG-T6S-COHERENT-CONJUGATE-FAMILY`, `…-T6T-JACOBI-MODE-SIGNS`, `…-T6U-APEX-SEED-DIAGNOSTIC`) |

Taken together: none of the four items changes a number or a grade in UVM v0.7.1. The first is the only one with scientific reach, through the sign of `m`.

---

## (d) Scientific frontier, negative results and certificate limits

### (d).1 What v0.7.1 holds, by kind

Everything in this subsection is the owner's tagged statement (`EV-SRC-READ`); no certificate is available to rerun.

- **Exact algebra, category-scoped:** R1 (source tower, unique minimal coupling `jΛz̄`), R2 (spin-2 block, `2θ` law), R3 corrected, R10 (word-sector dichotomy, degree-3 single sandwiches, constant coefficients), LEM-M-CENTRAL, R5 (HINDEX norm range), R11 (assembly conversion, `θ_f = 2π/3`, `4/125`), RESULT-M-3B (finite-`g` spectrum).
- **Exact but conditional:** R6, R8 / THM-M-LOCK (needs HYP-IDENT, the raw-array 9C premise and the `K_-` branch); CAND-M-BCH (symbolic, sector-functional normalization only).
- **Finite numerics:** R12, R13 (ESM 2D packs, named runs), R14 (one trajectory, `n=9`), R15 (proxy diagnostic `ρr⁴ = ℓQ_s²/(gC_m) ≈ 0.007–0.008`).
- **Hypotheses:** HYP-IDENT, HYP-M-FRACTURE, HYP-M-PREFRACTURE, single-jet, OPEN-M-7.
- **Headline:** no certified numerical OPEN-M deficit factor, in either direction.

### (d).2 Negative, withdrawn and superseded results that must be preserved

1. Block-diagonal extension gives `w=0` (Genesis `[THM]`; proof artifact not in the repository per `gen-v2.10`).
2. R3: the broad "polynomial jets excluded as `w`-sources" claim is withdrawn; the hole is `yk = k ȳ` for right-side `j/k` coefficients.
3. OPEN-M-4, verdict (C): single-jet as one constant-coefficient polynomial coupling term is refuted in that category; a mechanism-level single origin is neither derived nor excluded.
4. OPEN-M-2A: similarity transport sterile; its `h_3=0` explanation is now chart-scoped.
5. R9 / OPEN-M-6: gauge-class invariance from archival `h_3=0` withdrawn; the `1.006×10⁻²` envelope holds only in the archival chart.
6. R12: "physical cascade source `h=z_h²`" retyped to an ESM source proxy; RUN10's gate pass is defect-carried; for nonmanifold RUN10 "dimH 14" is an algebraic null space.
7. OPEN-M-2E-a: subcomplex deletion is not a valid legal/illegal split (dimH 14 → 31).
8. OPEN-M-2E: no clean A-candidate; RUN05 cleanup lowered loading; HYP-2E-COUPLING neither confirmed nor refuted.
9. R14: "corridor-borne" and the source-band/gauge-band "standing tension" withdrawn as inferences; the correlation stays as an association.
10. R15: the "~4× source deficit" reading superseded (`h` cancels). R16: "legal SU(2) correction = 2×" withdrawn as a physical verdict.
11. R-CHIRALITY-CLOSURE retired; OPEN-M-2G apex slot withdrawn; the historical T-6 wedge / no-basin / phase-steering imports withdrawn (SG-M-15); the unit-child / fixed-`F_W` corroboration and the "3-for-3" reading superseded.
12. RESULT-M-3A: `K_vac` (log-conformal) is not identified with Genesis `g`. RESULT-M-3B: `‖M‖_B → 2g` is not justified at `g=1`.
13. §1.5: the June 2026 negative inventory of AZ / Legacy / Discrete is search provenance, not a current-source absence claim.

### (d).3 Certificate limits

- **Availability.** None of the 18 named scripts (17 in §8, one in §7), no output and no pack is in the repository. "all PASS", "PI-audited", "PI-run confirmed", "exit-code gated" and "PI-reproduced on repo data" are `EV-SRC-REPORTED`. The v0.7 and v0.7.1 validations are declared "document validation only".
- **v0.7.1 itself reran nothing** (header, preservation boundary): "No growth run, Hodge recomputation, BCH certificate, or Genesis certificate is rerun". RESULT-M-3A/3B rest on an "in-session" audit "independently checked by the project reviewer"; that check's record is among the missing files.
- **Scope of each certificate as stated:** R3 item 2 is `[NUM]` through degree 5 for `j`-only dressings; R10 is degree 3, single sandwiches, constant coefficients; CAND-M-BCH is the two-face frame with three child transports (7 checks); R12's Hodge orthogonality is floating-point (`10⁻⁸`); R13's criterion bands are empirical (floor 0.28 "from RUN10", whose own value is 0.275); R14 is one growth series with `n=9`; THM-3G is "in the tested topology class" with a "mini protocol".
- **R14 statistics.** With `n=9`, `r=+0.654` corresponds to `t≈2.29` on 7 degrees of freedom (two-sided `p≈0.06`), and the stages of one growth series are not independent samples; `+0.654` against `+0.326` is not a resolved difference at this `n`. §5 already forbids reading it as a statistical law; the "weaker correlate" wording in the v0.7 correction deserves the same caution.
- **R15 arithmetic.** With `Q_s=0.1`, `g=C_m=1`, the reported `0.007–0.008` is simply `ℓ ≈ 0.7–0.8`: the diagnostic carries exactly one pack-derived number.

### (d).4 Checks done by hand in this pass (`EV-INDEP`, limited to the stated algebra; no script)

- R11: `f(θ) = sinθ·sin²(θ/2) = 2 sin³t cos t` with `t=θ/2`; `f' = 0` ⇔ `tan²t = 3` ⇒ `θ_f = 2π/3`; `f_max = 3√3/8`; prefactor `(2/√3)(3√3/8) = 3/4`; `0.024/(3/4) = 0.032 = 4/125`; at `r⁴ = 0.01`, `ρ ≥ 16/5`. Confirmed.
- R5: at `χ=0`, `‖H‖_B² = 4λ²/3`; at `|sin χ| = 1`, `‖H‖_B² = (4λ²/9)(3+2+4) = 4λ²`. Range `[2λ/√3, 2λ]` confirmed; R7's `c_χ ∈ [2/√3, 2]` consistent.
- RESULT-M-3B: at `ℑw=0`, `λ± = (2D+4g)/3 ± (2/3)|2D+g|`; `D/g = −1/2, 0, +1/2` give `‖M‖_B/g = 1, 2, 3`. Confirmed.
- 9C family: `K = ΔM_f + M_spin2(g,D) = [[g, D − mℜw],[D − mℜw, g]]`, eigenvalues `g ± (D − mℜw)`; with `D = −mℜw` the soft point is `g = 2|m||ℜw|`. Used in O2.
- T-6u: `√2 / (√14/16) = 16/√7 ≈ 6.05`. Confirmed.

These confirm internal arithmetic only. They do not replace the missing certificates and say nothing about physical premises.

### (d).5 Observations for the owners' discrepancy list

Each is a reading of tagged bytes, offered for the second co-owner to check; none is a verdict or a proposed edit.

**O1 — the `0.024` target also rests on the single-jet hypothesis.** Genesis (v2.8.5 (derived) lines 328–336, identical in v2.10) derives the target from `|α_f| ≳ 0.012` with "`α_f = c_0|w|`, `c_0 = ‖H‖/‖M‖_op`", under "`[scope: certified scalar-M frame + 9C raw-array modelling HYP + single-jet HYP]`"; `GEN-OPEN-UVJET-SCOPE` says the reduction "is conditional on the additional 9C raw-array … premise plus the single-jet hypothesis". UVM v0.7.1 lists the target's inherited conditions in six places (§1.3 scope tag, OPEN-M-2B, SG-M-7, §5 R11 row, the R11 `[COR]`, RESULT-M-3B) as reduced-wrapper, conditional 9C, large `g` and state/window matching; single-jet is guarded separately (SG-M-2) but is not named as a condition of the target or of `4/125`. Since OPEN-M-4 refuted single-jet in the one-term polynomial category and R11 builds `‖H‖_B` and `m|w|` from two tied sectors, whether `α_f = (‖H‖_B/‖M‖_B)|w|` holds for that construction is the same open question. Possible scope gap in the condition lists.

**O2 — implicit `m > 0`.** `gen-v2.10` records `B_*` (in `m = 2Q_sB_*`) as undefined with unknown sign and writes every `sgn(m)`-dependent statement explicitly. UVM writes `μr² = m|w|` (HYP-IDENT, line 136), `g_soft = 2m|μ_1|` and `2m|ℜw|` (lines 136, 289, 301), `m|w| = ℓ sin²(θ_f/2) r²` (R11, line 265). By the hand check in §(d).4 the soft point is `2|m||ℜw|`; the UVM forms agree with it only for `m>0`, and for `m<0` they would give a negative stiffness and a negative `μr²`. The ratio `|D|/g = 1/2` used in RESULT-M-3B is unaffected when written with `|m|`. So: no number changes, but several statements carry an unstated sign assumption that the producer has since made explicit. This is the concrete content of the first inbox item.

**O3 — `THM-3G` has no owner statement.** v0.7.1 calls it "OPEN-M-native" and "branch-native calibration theorem" (§4, §7) and corrects its provenance (Appendix B), but there is no §6 claim block, no status tag, no RID, no stated hypotheses or domain, and its certificate `open_m_3g_mini_protocol.py` is named only in §7, without a §8 row. Its described support ("mini protocol", "in the tested topology class") reads as a finite test, while the name says theorem. RESULT-M-3A (`[RESULT]` `[from: ALG/typing audit]`) depends on what THM-3G protects. Its grade is, on the tagged text, undeclared.

**O4 — `T100` inconsistency.** §2 OPEN-M-2E (line 110): "T100: `σ_{h,int}=0.252`, `L_{z_h}=0.527`, nm=2". §6 R14 (line 277): "Clean high-loading stages exist (T100: `σ_{h,int}=0.252`, nm=0, corridor 0.302), so loading is corridor-borne, not defect-borne". Same label, same `σ`, different nonmanifold count. Either two different packs share a label or one count is wrong; the R14 sentence uses `nm=0` as its evidence. UNVERIFIED without the original panel outputs.

**O5 — state/window matching has a concrete locator.** Genesis records its control-loss values for `Q_{s,0} ∈ [10⁻³, 10⁻²]` and at `Q_{s,0} = 5×10⁻²` (v2.8.5 (derived) lines 123, 321, 805, 1015; "not universal over the full wider window"). The phrase "primitive window `Q_s ∈ (0, 0.1]`" occurs in Genesis §6.6 (line 803) in a phase-coherence statement. The assembler's `Q_s = 0.1` therefore lies outside every initial state for which Genesis recorded a control-loss number. This supports the obligation v0.7.1 already states and gives OPEN-M-3C a starting point; whether `Q_s` in R11 and `Q_{s,0}` in the wrapper are the same variable is itself part of the matching question.

**O6 — attribution family around `0.403`.** Second site at line 107, and the "Legacy" attributions of the `β₁` motivation at lines 271, 273, 293 (§(b).6). The PI decision covers line 271.

**O7 — identifiers.** `UVM-OPEN-2F` on two objects; R1–R11 without result RIDs while Dyadic, AZ and OFN cite them by label (§(b).5).

**O8 — locators and grade tags on the Pre-Legacy imports** (`§RG`, `§1.12`, `[from: HYP]` over a `[HEUR]` chain; §(b).4, §(b).6).

**O9 — the foundation import.** The no-go that motivates the branch is `[THM]` in Genesis with its proof artifact declared "not in the repository". UVM imports it as `[RESULT]` `[from: THM]`. An evidence-custody limit of the producer that a consumer should carry.

**O10 — `θ_f = 2π/3` is used across streams.** UVM grades the angle `[ALG]` inside the assembly and `[INTERP]` as a tetrahedral / OFN 120° connection "pending a bridge theorem" (R11). Dyadic v6.4.24 line 467 states that it "equals the face flux `F_f` exactly … an exact arithmetic identity of the p=6 eigenvalue", with physical transfer a separate question (SG-15). The two are compatible as written — equal numbers, no bridge — but the consumer's sentence is stronger in tone than the owner's.

### (d).6 Frontier

Owner §9 order: (1) OPEN-M-6 full-map/observable source-coupling audit; (2) R16 constitutive/source bridge; (3) OPEN-M-3C exact finite-`g` target at a matched state; (4) OPEN-M-5 physical 9C / sign selection; (5) OPEN-M-2E-a legal/illegal harmonic decomposition; (6) pure-topology 2E run; (7) apex/UV embedding only if re-proposed; (8) Programme/OFN follow-through.

What each needs, from the sources read (a reading, not a choice of campaign):

- (1) is algebraic and its inputs are in the repository at a tag: Dyadic v6.4.24 §6.14 gives `h_2` explicitly and the nonzero `h_3` channels. No missing UVM original is required.
- (3) is algebraic on the Genesis `λ±` formula (bytes verified) but needs two decisions first: the matched state (O5) and the status of `c_0` (O1).
- (2) and (4) are derivation and model-selection questions; nothing to compute until a constitutive law or a selection principle is proposed.
- (5) and (6) need the ESM packs and Hodge scripts, which are missing; they are blocked on custody.

---

## (e) Reading order and Atlas exposure

Order (22 November 2026, +03:00; one session):

1. Project instructions and this session's working-preferences memory file (how the PI wants co-owner work delivered; no UVM science).
2. `CONVENTIONS.md`, full.
3. `records/uvm/UVM_COOWNER_SESSION_ORIENTATION.md`, full. **Atlas exposure 1:** its paragraph "[ATLAS: atlas-v0.15 L5 …]" names the eleven `OPENM.U1–U11` rows by bundle: chart/regularity (U1), proxy versus threshold/deficit (U2), RID/alias duplication and missing GEN RIDs (U3), GEN sector scope (U4), symbol/class collisions (U5), `2π/3` across domains without a bridge (U6), consumer currency and audit status (U7/U8), Pre-Legacy links (U9, U11), mixed grades (U10), and the factor-four/Pauli-lift remark on U11. Its SCIENTIFIC SCOPE paragraphs also summarize R11–R16 before I had read the DSN.
4. `BASELINE.md`; tag list; `uvm-v0.7.1` DSN, full, in three consecutive passes (lines 1–150, 149–310, 310–444).
5. `pipes/README.md` and the UVM inbox; `tools/orient.py`; `tools/pipes_index.py --check`; open PR list.
6. Tree and zip search for the missing originals; RER v0.2 §7; the Genesis v2.8.5 recovery test.
7. Pre-Legacy v0.8 and Legacy v0.7 checks.
8. `ATLAS_ADVISORY_TO_PI_DORMANT_OWNERS_20261110.md`: header, §4 preamble, §1 row 4, §4 row 4. **Atlas exposure 2:** row 4 names "H11, OPENM.U9 ≡ LEGACY.Y2" and gives the Atlas observation on line 271.
9. `ATLAS_ADVISORY_UVM_REACTIVATION_20261121.md`: header, §1, §2, §5, §6. **Atlas exposure 3:** §1 lists that advisory's reading extent and restates the conditional status of `0.024`, `4/125` and R15; §2 is the S0 custody table; §5 Deliverable C lists a downstream pointer census (OFN RF-O08-08/-11, AZ §6, Programme IF08–IF11, RER §7). **§3 and §4 not opened.**
10. Programme v1.4 / v1.2; Methodology v1.4 / v1.3; Genesis v2.8.5 (derived) and v2.10 with the line comparison; Dyadic v6.4.24; Triadic v1.7 / v1.6.1; OFN v0.12; citation census of OPEN M in the other owner files; `dsn_lint`.
11. This report written; then filed.

Declarations: advisory §3 remained unopened until filing; `atlas/RTG_STATE_ATLAS.md` was never opened, and my repository-wide searches excluded `atlas/` and `records/atlas/`; no report by the other co-owner existed or was read. This is a source-first reading, not an Atlas-blind one: after exposure 1, O6 overlaps the bundle named for U9, O7 the bundle named for U3, O10 the bundle named for U6, and the tag observations in §(b).4 the bundle named for U10. I found each in the tagged bytes at the lines cited, but I cannot claim I would have looked for them unprompted. O1, O2, O3, O4, O5 and O9, and the Genesis v2.8.5 recovery, correspond to nothing I had seen in an Atlas summary; whether they coincide with a U-row I do not know.

**Disagreement with the orientation note** (the only Atlas-side text I can compare so far): (i) it states that no verified original-edition bytes of Genesis v2.8.5 exist in the tree — a hash-matched derived copy does (§(a).4), which changes its BOOTSTRAP 2 instruction for Genesis from "mark UNVERIFIED" to a custody decision; (ii) it describes the R12 `0.403` correction as one citation — there are two sites; (iii) its evidence list omits `open_m_3g_mini_protocol.py`, which the DSN names only in §7.

---

## Limits of this report

- Not a re-derivation of any UVM result. The hand checks in §(d).4 cover displayed arithmetic only.
- Old-side comparisons for Dyadic v6.4.10, Triadic v1.6 and OFN v0.8 are UNVERIFIED and are not replaced by current-owner statements.
- Git history and other branches were not searched for the missing originals.
- Genesis, Dyadic, Triadic, OFN, Programme and Methodology were target-read, not read in full.
- The orientation note's working-memory section was not updated; that file is shared and its lanes are for the owners to set.

## Questions that are the PI's

1. **Custody of the UVM originals.** Where do the 18 scripts, their outputs and the ESM packs live ("repo data" in R14/§8), and can they come in unchanged on an `upload/…` branch? Likewise the ten v0.7 / v0.7.1 governance files and the v0.7 edition (`fea80656…`).
2. **Genesis v2.8.5.** Is the hash-matched derived copy acceptable as the comparison source for the UVM pin, and should it be placed (and where), or kept as a reproducible recipe only?
3. **Scope of the already-decided `0.403` correction.** Does the 10 November decision extend to the second site (line 107) and to the neighbouring "Legacy" attributions of the `β₁` motivation, or are those separate triage rows?

*End of report. No UVM statement, pin, grade, pipe state or evidence file is changed by it.*
