# DZT v0.18 — release record

**Status:** DRAFT, for review. **Not adopted.** `dzt-v0.8` governs until the PI adopts this edition and the annotated tag `dzt-v0.18` exists. This draft is completed at adoption (§12) and frozen then.
**Candidate file:** `dsn/RTG_DYADIC_ARITHMETIC_RESONANCE_TRANSFORM_DSN.md`, SHA-256 `db74f0a28ca2bda7c62ae436bc12fc4d71e9741ebdfe0e192837658cbe2375bf`, 42,850 bytes (stage-2 candidate, commit `9de9b438c735159ff5d8980efe0263951aa6ca2d`).
**Predecessor:** v0.8, tag `dzt-v0.8`, SHA-256 `cad20982d294775d52592c304d743695c6ec2d8cf4975c78de203db3d6a92ff2`, 50,547 bytes. It has no release record; it was tagged at the 22 Oct 2026 baseline (`BASELINE.md`, "PI").
**Prepared by:** the DZT co-owner (Claude), 18 November 2026. Second co-owner and independent reviewer: ChatGPT (D6).

This record invents no hash, approval or review identifier. Steps after adoption (publication commit, merge, tag, notices) are listed in §10 and are carried by their own commits, tag and pipe items.

**Authority.**
- BOOTSTRAP 3 of `records/dzt/DZT_COOWNER_SESSION_ORIENTATION.md`.
- PI decisions D1–D7, 18 Nov 2026, 00:00 +03:00 (`records/dzt/DZT_REACTIVATION_TRIAGE.md` §7). D1: `dzt-v0.8` is the edition basis and v0.9–v0.17 are sources. D2: no retrospective tags. D3: $\lvert N_+\rvert$ labels and no sign OPEN. D5: Methodology v1.4 in the same cycle as a separate stage. D6: Claude prepares, ChatGPT reviews, the PI adopts.
- PI decision on triage §8, 18 Nov 2026 (project conversation; the time is not recorded in this session), verbatim: "1- Önerin uygun 2- v0.18 başkaca karışıklık çıkmasını istemeyiz." ("1 — your proposal is fine; 2 — v0.18, we do not want any further confusion.") Scope: list (i) of triage §6 as written. Number: v0.18, above the recovered chain.

## 1. Bytes and how to rebuild

| Stage | File | SHA-256 | Bytes |
|---|---|---|---|
| base | `dsn/RTG_DYADIC_ARITHMETIC_RESONANCE_TRANSFORM_DSN.md` at tag `dzt-v0.8` | `cad20982d294775d52592c304d743695c6ec2d8cf4975c78de203db3d6a92ff2` | 50,547 |
| 1 — corrected intermediate (commit `6600ada1628b392d7a9157236f04d508c74d3255`) | same path | `a552c01c318ec41dca3ac6e1cc223d65ee53f7063394c3e185cd0a4fd7b51cdc` | 54,254 |
| 2 — compacted candidate (commit `9de9b438c735159ff5d8980efe0263951aa6ca2d`) | same path | `db74f0a28ca2bda7c62ae436bc12fc4d71e9741ebdfe0e192837658cbe2375bf` | 42,850 |
| published — the adopted file | — | pending adoption (§12) | — |

```bash
python3 -I evidence/dzt/v0.18/stage1/build_dzt_v0_18_stage1.py --out /tmp/inter.md --log /tmp/edit_log.txt
sha256sum /tmp/inter.md                                                              # a552c01c…1cdc
git show 6600ada1628b392d7a9157236f04d508c74d3255:dsn/RTG_DYADIC_ARITHMETIC_RESONANCE_TRANSFORM_DSN.md | sha256sum   # the same
diff /tmp/edit_log.txt evidence/dzt/v0.18/stage1/edit_log.txt                         # empty
git diff dzt-v0.8 6600ada1628b392d7a9157236f04d508c74d3255 -- dsn/RTG_DYADIC_ARITHMETIC_RESONANCE_TRANSFORM_DSN.md   # stage-1 delta
T=$(mktemp -d)
python3 -I evidence/dzt/v0.18/stage2/build_dzt_v0_18_stage2.py --emit-base "$T/stage1_intermediate.md"
python3 -I tools/check_compaction.py "$T/stage1_intermediate.md" dsn/RTG_DYADIC_ARITHMETIC_RESONANCE_TRANSFORM_DSN.md evidence/dzt/v0.18/stage2/movement_map.json
python3 -I evidence/dzt/v0.18/stage2/stage2_negative_controls.py
```

The stage-1 builder reads the base from the tag with `git show` and asserts its hash. It applies 29 edits, each located by an anchor that must occur exactly once (`evidence/dzt/v0.18/stage1/edit_log.txt`). It stops on a missing or repeated anchor; on a forbidden string left in the live body (nine superseded Dyadic strings, "M_p=|Q_p|", `[THM/ALG]`, `[ALG fin-hor]`, `[HEUR diagnostic]`, "[ALG finite horizon"); on the loss of any of the 22 registered DZT RIDs; and on the loss of any of SG-DZT-1 to SG-DZT-8. The stage-2 builder reads the intermediate from commit `6600ada1` and asserts its hash. No second copy of a DSN state is kept (Methodology §13.7).

## 2. What stage 1 changes (triage list (i), stage 1)

| Triage row | Edits (log keys) | What |
|---|---|---|
| 1 — norm object | E02c, E03, E05, E07, E11, E12, E14, E24 | $M_p:=Q_p/(i\zeta_p^3)\in\mathbb Q(\zeta_p)^+$ is the defined object; "$M_p=\lvert Q_p\rvert$" is gone. Every tabulated value and finite-horizon statement reads $\lvert N_+(M_p)\rvert$, and the sign is stated as not determined. No value changed. Correction record in Appendix B |
| 8 — table scope | E03, E07, E13, E14, E19, E24 | The §1 validation table and the §6.3 table are the same 14 points ($p=12$–$64$). The anomaly set ($p=8\ell^a$, 20 points on $p\le1000$) is given in the same paragraph. The v0.6 `[OBS]` "$p=40$ is the sole anomaly" and its v0.7 `[COR]` leave the live text and are recorded in Appendix B as `[SUPERSEDED]` |
| 9 — pins except Methodology | E00a, E00b; in the body E09, E11, E16, E23 | Header: Programme `programme-v1.4`, Dyadic `dyad-v6.4.24`, AZ `az-v0.10`, OFN `ofn-v0.12`. Body: Dyadic `dyad-v6.4.24`. Each tag is in `BASELINE.md` and is the newest tag of its study |
| 10 — Appendix F repins | E02, E02b, E06, E08, E09, E11, E16 | Every Dyadic string resolves to a RID at `dyad-v6.4.24`, or is marked as text without a RID: VANISH-B2/B3/B4 are three RIDs; `DYAD-OPEN-B5-ALLP` → result `DYAD-ALG-B5-ALLP-NONVANISHING`; `DYAD-THM-Q403-PHASE-ALLP` → `DYAD-THM-Q403-PHASELAW` `[THM]`; P1, REALITY, LEAD, R and CF-Q403 are cited as parts of PHASELAW; the $p=12$ value is §6.11 text; the cascade artifact is `DYAD-ART-Q403-EXTRACT` "by content; no byte identity". No alias is created |
| 11 — certificate | E16, E17 | Cited as `DYAD-ART-Q403-CERT`, not in the repository |
| 13 — compound grades | E04, E05, E06, E07, E11, E14, E15, E18, E20, E21, E23; aliases E01 | No `/`-joined or abbreviated grade remains. The finite-horizon statements are `[ALG]` with an explicit `[scope: …]`; the mechanism stays `[HYP]`; owner results carry the owner's grade. The alias table follows Methodology v1.4 §8.4; `[import-ref]` is a label; the standard clause **[RECOVERED]** is defined once |
| 16 — §8 evidence states | E12, E14, E17 | Each script is cited by its recovered path and SHA-256 as `EV-BYTES`, with "historical execution evidence not available; `EV-NOT-RERUN`". Where two contents exist, both are cited and the one matching the DSN's description is named, without asserting identity. Exit codes are source-reported |

**Other stage-1 text.** §1 keeps readouts with RIDs and pointers, with one home per statement (Methodology §1.1). E12b gives the $p=12$ computation its full statement at its §6.3 home; before, part of it was printed only in §1. E10 is the §6.3 heading in the mixed-content form (Methodology §3.5); its anchor is kept.

## 3. Stage 2 — compacted candidate

**Base:** the stage-1 intermediate `a552c01c…1cdc`, read from commit `6600ada1628b392d7a9157236f04d508c74d3255`. **Candidate:** `db74f0a2…75bf`. Builder `evidence/dzt/v0.18/stage2/build_dzt_v0_18_stage2.py`; movement map `evidence/dzt/v0.18/stage2/movement_map.json` (SHA-256 `8e747d5213f842733a409e30a2e4ff896c5c0bc1627c5c29f9165977f315b8e2`).

| Operation | Class | What |
|---|---|---|
| S2-H | replace-header (presentation) | v1.4 field order with Scope and Document status. One predecessor with its full hash. The Methodology pin `methodology-v1.4` (row 9, stage 2). The companion pins as set in stage 1. The §1 length exception is declared in the header (Methodology §1). The status summary is four sentences, each taken from the base summary or base §1; the version-by-version narrative of the old summary leaves the header (bytes in the intermediate and at `dzt-v0.8`) |
| S2-L1 – S2-L5 | edit (history-removal) | Five version labels leave live headings: "(v0.2)" twice, "(v0.4)" three times |
| S2-A | replace-section (history-appendix) | Appendix A: one v0.18 entry; one line saying v0.9–v0.17 are not part of this lineage; one pointer for v0.1–v0.8, whose entries are byte-identical in Appendix A of `dzt-v0.8` |
| S2-F | replace-footer (presentation) | one footer line |

**Checker** (`evidence/dzt/v0.18/stage2/check_compaction_output.txt`, report JSON beside it): **PASS**, exit 0.
- The candidate equals the base plus the declared operations.
- 99 claim blocks in the base live text: 96 byte-identical, 3 changed by declared operations, 0 unexplained.
- The RID set, heading anchors, source hashes and qualifier tags of the live text are preserved.
- References resolve.
- Required header fields are present, with one predecessor and one footer.

**Negative controls** (`stage2_negative_controls_output.txt`): **PASS**. The unmutated map passes. Each of eight mutations fails on the expected check:
- an undeclared word in the live text;
- a status-summary sentence not in the base (an all-$p$ proof claim);
- a history-removal of an identified span;
- an Appendix A entry naming an identifier absent from the live text (`DZT-THM-CASCADE-DENOMINATOR`, the route by which a recovered theorem could enter through history);
- a claim tag changed under the label of a reference substitution;
- two footer lines;
- a base that is not the stage-1 intermediate;
- a predecessor named without its hash.

**What the checker does not show:** it compares bytes and declared classes. The wording of the new header (Scope, Document class, Programme tier, Document status, the §1 length line) and of the Appendix A entries is presentation text for the reviewer to read.

## 4. Points for the change-focused review

Methodology §13.6: the stage-1 delta receives the review its content requires; stage 2 is checked against the intermediate. If the review changes stage 1, both stages are rebuilt (the stage-2 builder names the stage-1 commit) and the checks are rerun.

1. **E15, `[HEUR diagnostic]` → `[ALG]` + `[HYP]`.** The undeclared alias is unpacked. The verified finite statement is graded `[ALG]` with scope $p\le1000$; this is the grade `DZT-ALG-CASCADE-ANOMALY-SET` already carried at its §6.3 home. The mechanism stays `[HYP]`. Check that no component is raised.
2. **E03, §1.** It is rewritten as readouts with pointers. Check each readout against its home. §1 is 609 words; the exception is declared in the header.
3. **E16, Import Ledger.** Each row against Dyadic `dyad-v6.4.24` and its Appendix F. In particular, check the PHASELAW components (cited as parts, with their formulas kept) and the extractor definition ($R^{\rm raw}$, $K^{\rm extra}$, $\chi$), which is kept in §7.
4. **E17, §8.** Each path and hash against `upload/dzt-recovery-20261116/received/`. Where two contents exist, check which one matches the DSN's description.
5. **E01, the [RECOVERED] clause and the alias table.**
6. **E13 and E24.** The superseded `[OBS]` and `[COR]` and the two `[SUPERSEDED]` records in Appendix B.
7. **S2-H and S2-A.** The header text and the Appendix A text (presentation).

## 5. Differences from the triage and limits

- **Version labels kept in the live text.** The §9 provenance table names the edition of each historical entry; this is provenance and is kept. The `[FAIL]` record "The v0.4 hypothesis …" is kept, because the span carries math and tags, which a history operation may not remove. Appendix B records keep their version references.
- **Identifier left with history.** `DZT-ALG-CASCADE-NORM-2POWER` occurred only in the v0.8 Appendix A (it records the rename to `DZT-ALG-CASCADE-NORM`). It leaves with that appendix and stays at `dzt-v0.8`. No live RID is lost.
- **Formulas left out on purpose.** The 11-value table of the v0.8 §1, "$M_p=\lvert Q_p\rvert$", the superseded sentence on $p=20, 24, 56$, and $\arg Q_p$ as a DZT statement. Each superseded statement has its record in Appendix B, or its home in the Dyadic import.
- **Stage-1 review.** In the AZ v0.8 precedent, stage 1 was reviewed before stage 2 was built. Here both stages are submitted together; see §4 for what happens if stage 1 changes.

## 6. Size report (Methodology §13.8)

`python3 -I tools/dsn_lint.py --prev <dzt-v0.8> dsn/RTG_DYADIC_ARITHMETIC_RESONANCE_TRANSFORM_DSN.md` (informational; no gate). The counting method is the script's own.

| Metric | `dzt-v0.8` | v0.18 candidate |
|---|---|---|
| bytes | 50,547 | 42,850 (−7,697; −15.2 %) |
| §1 words | 697 | 609 (exception declared in the header) |
| orientation core (chars / words) | 17,996 / 2,161 | 16,783 / 2,065 |
| Appendix A (chars; editions; max words per edition) | 9,133; 8; 192 | 1,329; 3; 104 |
| history phrases in live sections | 8 | 6 |
| identifier strings (lint count) | 40 | 36 |
| near-duplicate paragraphs | 0 | 0 |
| footer lines (lint count) | 1 | 1 |

The identifier count falls because ten strings that are not RIDs or were superseded leave the text: nine Dyadic strings and the renamed DZT string (§5). Six owner RIDs enter in their place (§2, row 10). Growth per new RID is not meaningful for a shrinking file. The lint figures for `dzt-v0.8` were computed by the same script on the tagged bytes.

## 7. Received history (triage rows 15 and 18; D2)

DZT editions v0.9–v0.17 have no adoption record and are **received, not adopted**. No retrospective tag is created. The files are as received in PR #289 and placed as plain files in PR #308 (merge `5fa09bd`). Directory: `upload/dzt-recovery-20261116/received/originals/downloads/`. In the table, `…` stands for `RTG_DYADIC_ARITHMETIC_RESONANCE_TRANSFORM_DSN`. The 25 hashes were recomputed from the repository files for this record, and they equal `records/dzt/DZT_RECOVERY_READING_RECORD.md` §2.

| Edition | File | SHA-256 | Bytes |
|---|---|---|---|
| v0.1 | `…_v0_1.md` | `c7656a7a9e9c5d43d14b6fe41d332f1f8afdb8fe72ece761983e051e0ff6ad99` | 21078 |
| v0.2 | `…_v0_2.md` | `838f49ea3ec6a60b1c94922e48e2a587b7919ce449849b7957ce2218630090ea` | 26282 |
| v0.3 | `…_v0_3.md` | `6af8db841f75e86630397c70b2942b4b4b0489ee2f2fc08800707a08422ebe3d` | 27678 |
| v0.4 | `…_v0_4.md` | `ad797e5d28ac5a4d316b3da618ef44d2760260982d236850713f12d5a2f632c7` | 33151 |
| v0.4 | `…_v0_4 (1).md` | `806ff90041365404513b34767d9f9ef0d2ea47519ae71089ee43af9bb8ac83e8` | 34605 |
| v0.5 | `…_v0_5.md` | `d59146da69443cb1901b2e97ad6244582fc5938d5f4f0d30853f11122a0d8fba` | 38055 |
| v0.6 | — | **NOT RECEIVED** | — |
| v0.7 | `…_v0_7.md` | `33b3030ce1e3fec5e3c0139788e6ac61461bd2a193671ec3902e41d86ebd3af0` | 45807 |
| v0.8 | `…_v0_8.md` | `57cbb30e8405ab961fcf2d3ceea1e6275aacd460948f42c6109622189d3cdceb` | 49224 |
| v0.8 | `…_v0_8 (1).md`; also `upload/dzt-recovery-20261116/received/originals/legacy-src/rtg-toolkit/scripts/dyadic/DSN/…_v0_8.md` | `cad20982d294775d52592c304d743695c6ec2d8cf4975c78de203db3d6a92ff2` (= `dzt-v0.8`) | 50547 |
| v0.9 | `…_v0_9.md` | `5e2e4462243d2e27934b277d305fb4d5bb218a36729371060ff0651fd5e6224e` | 55539 |
| v0.9 | `…_v0_9 (1).md` | `bf12113fb050ef3600d21d6e4a5141e8a75c8f574eff8e584104eaa3250448bf` | 54817 |
| v0.9 | `…_v0_9 (2).md` | `3990c411d4b89c54e1d4556fb361cd8f9d65bff6f393f1fb7548c367e571666e` | 56353 |
| v0.10 | `…_v0_10.md` | `6942d7cd5e224b7a016ca72fca9bf01a8b1000ab2363122ddd9b2522df9e285a` | 60338 |
| v0.10 | `…_v0_10 (1).md` | `a70c6522145bbb714a240db020b8b048b2fa275f615540ffcf0254a58174b400` | 61869 |
| v0.10 | `…_v0_10 (2).md` | `70a529d9eb38d00f76575634ef88ce56f579e23309597731849ff2fcc2331a75` | 62520 |
| v0.11 | `…_v0_11.md` | `ec75d6c9095adb38c29bc6f68fd97247d29bd5259cdbcf97c2625bf675b0b366` | 67128 |
| v0.11 | `…_v0_11 (1).md` | `0c5addf779bd5c1503e89a39007672281d2a56a23e18aef483ec0877a41767e6` | 67759 |
| v0.12 | `…_v0_12.md` | `032bf581fd424f03dffc9fc9c2825ba7ed0b4af441c47fc88b37e09d8080d2b2` | 71924 |
| v0.13 | `…_v0_13.md` | `1392acb37d75f34137ffcbfcd5b05898f353ab4f693aeacce7deb66e0b1cbe02` | 75267 |
| v0.14 | `…_v0_14.md` | `b3b56875868be5f2ee3c6b1d266587dd868a8401aa9904b9f2eec56cd9dde739` | 79768 |
| v0.15 | `…_v0_15.md` | `916ecab0861ff781e55d24197afe41a9c79415660522c426d1b4902735c87d5c` | 83938 |
| v0.16 | `…_v0_16.md` | `2b68463e6ef536c815d3e50744141ea1a4925247480e0a0c1714586aac317e5b` | 86638 |
| v0.16 | `…_v0_16 (1).md` | `975c7b98a3b316307df51a57cc2b0e3be2dc4357631ad8c39ccfd976becccf11` | 88425 |
| v0.17 | `…_v0_17.md` | `10ca26328ded751269081b3d85e5aa78c30ae97a85e899f017eee24ea07e2df8` | 92269 |
| v0.17 | `…_v0_17 (1).md` | `e24acfc150e3f4e9753ff06e6bd6edb89bf913e11382818743b9bce057bf1bcd` | 93107 |

**The v0.17 "closure freeze"** (`…_v0_17 (1).md` lines 59–61 only) is an unverified historical status record, not a PI decision (D4). It is not carried into v0.18 and is not cited as a decision. The edition number v0.18 follows the received chain, so that no version label is shared by two texts. It does not continue that chain: v0.18 is built on `dzt-v0.8` (D1).

## 8. Inbox (`pipes/DZT/`)

The four items were read before the stage-1 intermediate was fixed (checkpoint 2 of `pipes/README.md`). They are set to `acknowledged` in this PR. Dispositions are entered by the publication commit after adoption, with this record as pointer:

| Item | Disposition at adoption | Basis |
|---|---|---|
| `20261103-DYAD-notices-n16-n21.md` | `accept` | Appendix F crosswalk taken over in §7 at `dyad-v6.4.24` (rows 10, 11); $p=12$ value cited at §6.11 (row 22); VANISH-B2 range unchanged (row 24); RAW-CUBIC not cited (row 23) |
| `20261111-AZ-v0-7-adopted.md` | `no action` | superseded by the AZ v0.8 item; AZ pin now `az-v0.10` |
| `20261112-AZ-v0-8-adopted.md` | `accept` | AZ companion pin at the governing tag `az-v0.10`; SG-DZT-1 unchanged (row 21) |
| `20261113-LIT-norm-law-proof-candidate.md` | stays `acknowledged` | the verdict follows the triage row 2 review, list (ii); not part of v0.18 |

## 9. Notices (triage rows 14 and 20)

Filed after the tag, one item per inbox; each needs the tag `dzt-v0.18` to validate (`tools/pipes_index.py --check`). The receivers decide.

- **PROG** (`pipes/PROG/`): DZT v0.18 pins `dyad-v6.4.24`; the Programme's IF18 names Dyadic v6.4.8.1. IF19 is unchanged.
- **NUMGEN** (`pipes/NUMGEN/`): the NUMGEN provenance line citing DZT v0.8 and the "v0.17" report. The governing DZT edition is v0.18. v0.9–v0.17 are received history, not adopted (§7).
- **OFN** (`pipes/OFN/`): RF-O08-13 cites DZT v0.8 and the "v0.17" report. Same content as the NUMGEN notice.

## 10. Steps, in order

| # | Step | By | State |
|---|---|---|---|
| 1 | Stage 1 and stage 2, checks, this draft | DZT co-owner | done (this PR) |
| 2 | Change-focused review of stage 1, then of stage 2 (§4) | second co-owner | requested |
| 3 | Adoption decision (§12) | PI | pending |
| 4 | Publication commit on this branch: status lines only (a reviewed transform, as `evidence/az/v0.8/publish_az_v0_8.py`); the inbox dispositions (§8); this record completed and frozen; the `BASELINE.md` DZT row (v0.18, the adopted hash, this record, tag `dzt-v0.18`) | DZT co-owner | pending |
| 5 | Merge by a merge commit (not squash) | PI | pending |
| 6 | Annotated tag `dzt-v0.18` on that merge commit, with the adopted hash in the tag message | PI | pending |
| 7 | Notices (§9); lane in the orientation note | DZT co-owner, after the tag | pending |
| 8 | Tag verification and Atlas refresh | atlas owner | pending |

## 11. Not in v0.18

The following are list (ii) of triage §6. Each enters an edition only by a separate PI decision after review.
- The norm-law proof review and the LIT verdict (rows 2–5, 19).
- The B1 re-examination, starting from the dynamical object (row 6); v0.8's `DZT-OPEN-LOCAL-FORMAL-ZETA` stays as stated.
- Channel universality (rows 7, 12).
- The targeted search for missing sources (row 17).

No grade is raised. No recovered theorem, RID or B1 result enters. No sign OPEN is opened.

## 12. Adoption decision

Not given. To be completed with the PI's verbatim decision, its time, the adopted object (candidate hash and published hash) and what the adoption covers and does not cover. Order: decision → this record → merge → tag.

## 13. Open items carried forward

1. List (ii) (§11).
2. Missing material (row 17): the Dyadic `q4_03` certificate, extractor and data; `qb_extract.py` and DZT-REQ-001; v0.6 and the v0.17 session record; DZT-REQ-005.
3. The LIT record header at rtg-lit `8e2fb5cb` says "not reviewed / not offered" (row 19); this is named in the reply to the LIT item.
