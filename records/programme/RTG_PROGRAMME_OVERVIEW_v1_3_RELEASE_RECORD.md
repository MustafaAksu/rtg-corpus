# Programme Overview v1.3 — release record

**Status:** ADOPTED by the PI, 24 October 2026 (§6). Adopted file SHA-256 `1b8358b3e1d3abb853e226786d21e6559c289b7c85570dac0ff1ebc2dabaea06`. Governing from the annotated tag `programme-v1.3` on the merge commit of PR #29; `programme-v1.2` is the predecessor.
**Editor:** Claude (atlas owner), by PI decision of 23 October 2026 (`records/programme/ATLAS_ADVISORY_PROGRAMME_v1_2.md` §5). **Reviewer:** ChatGPT (change-focused review of stage 1; mechanical review of stage 2). **Adoption:** PI.
**Object:** `dsn/RTG_PROGRAMME_OVERVIEW.md`. **Governing rules:** Methodology v1.4 (§§1.1, 13), `CONVENTIONS.md`.

## 1. Build stages (branch `claude/programme-v1.3`)

| Stage | Commit | SHA-256 of `dsn/RTG_PROGRAMME_OVERVIEW.md` | Size | Built by | Checked by |
|---|---|---|---|---|---|
| Base: adopted v1.2 (tag `programme-v1.2`) | — | `4207da05dca24256e7bc528cb9814f848838bcd98e3d01222fb2a633ec9fd359` | 686 lines, 73,019 B | — | — |
| 1 — corrected intermediate (build stage, not an edition) | `951371d` | `e4fe4e7b1df4de12b2e01cc187e223c27b7cd3d6c9beb030f227f9c88c54b136` | 709 lines, 81,600 B | `evidence/programme/scripts/build_programme_v1_3_stage1.py` (25 exact-once edits; log `evidence/programme/v1.3/stage1_edits.json`) | `check_programme_v1_3_stage1.py`: 13 gates PASS, 12/12 negative controls caught (`check_stage1_output.txt`) |
| 2 — compacted candidate (reviewed) | `f7ff205` | `01199132609a4782dbce1f572d65e2fd1406857db3835c21eb8a7edd43215a35` | 614 lines, 68,836 B | `build_programme_v1_3_stage2.py` (3 operations; `movement_map.json`) | `tools/check_compaction.py` (unchanged from `main`), Programme profile: PASS (`check_compaction_output.txt`, `_report.json`); `test_check_compaction_programme.py`: 10/10 controls rejected, Programme invariants PASS |

| **Adopted v1.3** | publication commit | `1b8358b3e1d3abb853e226786d21e6559c289b7c85570dac0ff1ebc2dabaea06` | 614 lines | `release_programme_v1_3.py` on the stage-2 candidate (status lines only) | diff against the candidate = 3 lines |

Reproduce from the repository root: `git show programme-v1.2:dsn/RTG_PROGRAMME_OVERVIEW.md > base.md`; stage-1 builder → `e4fe4e7b…b136`; `git show 951371d:dsn/RTG_PROGRAMME_OVERVIEW.md > inter.md`; stage-2 builder → `01199132…2a35` and the movement map byte-identical to the committed one. The size went down 5.7 % against v1.2 and 15.6 % against the intermediate; compaction was not a goal, synchronization was.

## 2. Changes (stage 1), by advisory row

| Row | Edits | Where | What |
|---|---|---|---|
| PA-01 inventory editions | S6-1, S2-0, S2-1, S5-4, H-1 | §6.1, §2, §5 P0, header | every home listed by governing edition and tag; nine rows moved (METH v1.4, OFN v0.10, LEGACY v0.7, NUMGEN v1.20.8, DYAD v6.4.22, TRIAD v1.6.1, GEN v2.8.9, UVM v0.7.1, RECOG v0.3.23); edition column replaces the versioned-filename column; `BASELINE.md` named as the authority on hashes; the P0 scope pin cites `DYAD-DEF-PRIMITIVE-MAP` instead of "Dyadic v6.4.9 §6.1" |
| PA-02 missing documents | S6-1, S6-2, S6-3, S5-5 | §0.1, §6.1, §6.5, §6.6, §5 P1 | class column (canonical / adopted working standard / noncanonical / derived); rows RRF (Tier 5, standard), RER, FMS, ER-2B (noncanonical, no tier), ATLAS (derived map, no tier; never a source); count "15 canonical + 3 noncanonical + 1 map" replaces "14 homes" |
| PA-03 owner status reports | S6-2 | §6.2–6.5 | per-study entries reduced to custody, imports/consumers and programme-relevant interfaces, each pointing to the owner's own status summary; no owner science restated (gate G10) |
| PA-04 interface register | S7-1 | §7 | §7.1 graph at current declared imports; §7.2 as a table with consumer section and consumer pin; IF01–IF25 kept, pins moved to governing tags or labelled as the consumer's pin; IF17 retired as a transfer proposal (settled custody split); IF26–IF36 new (RECOG → DYAD; NUMGEN's consumer record of RECOG; RECOG → OFN; RRF as standard; owner imports into RRF; OFN ↔ RRF class-C contract; feedback imports into OFN; noncanonical records RER/FMS/ER-2B; atlas); §7.3 reworded |
| PA-05 governance pointers | H-1, S0-1, S0-2, S0-3, S6-4, S9-0, S9-2, S6-5, B-1, F-1 | header, §0, §6.7, §9, footer | Methodology v1.4 everywhere a current pointer; repository and tags as the source; v1.2 records recorded as missing; two TDR-G "Appendix C" references name the TDR-G tag so they resolve after the Programme's own Appendix C leaves (B-1 touches one parenthesis of PROG12-C10's text in Appendix B; the ledger is otherwise untouched) |
| PA-06 maintenance sequence | S9-1 | §9.2 | table of the v1.2 sequence with executed / not executed per owner; remaining queue Pre-Legacy, TDR-G, DZT, AZ |
| PB-07 OPEN-P pointers | S5-1, S5-2, S5-3 | §5 | P0: OFN v0.10 and RRF v0.8.4 as criterion homes; P2B: OFN OPEN-OFN-3B (`RTG-OFN-OPEN-PRIMACY-3B`) as the criterion home, no construction owner assigned; P3: OPEN M v0.7.1 state (no physical UV blocks; no certified deficit) |
| PB-09 maturity table | S4-1 | §4 | column "v1.3": records retained; current headers re-read (DZT and AZ declare A; no other owner declares an A–D grade); no grade issued |
| PB-10 counts and wording | S0-1, S6-3 | §0.1, §6.6 | recount; AI-reader paragraph (PC-13) |
| PC-12 κ table | S8-1 | §8.2 new | eleven rows: symbol, owner, section, what it names; the class-C κ ≡ γ relation stated as an atlas reading, not an owner statement |
| release entry | A-1 | Appendix A | stage-1 draft entry (compacted in stage 2) |

Not changed: §1, §2.3, §3, §4 semantics, §5 criteria and the five RIDs, §6.6 table, §6.7 queue, §8 SG-PROG-1–4 (byte-identical, gate G4), Appendix B except B-1. Gate G6: the tag multiset `[DEF]`×10, `[HYP]`×5, `[COR]`×3 is unchanged; no `[THM]`/`[ALG]`/`[NUM]`/`[RESULT]` introduced.

## 3. Stage 2 — compaction (layout only)

| Op | Kind | Content | Archive |
|---|---|---|---|
| M01 | ref-subst | §2.1 "See Appendix C, PREL." → "See Appendix C of v1.2 (tag `programme-v1.2`), PREL." | `programme-v1.2` |
| M02 | history-appendix | Appendix A: full entries → one compact entry per edition (v1.3, v1.2, v1.1, v1.0) with pointers to the tag | `programme-v1.2` (v1.0–v1.2 entries, Draft 1 history), stage-1 commit `951371d` (full v1.3 draft entry) |
| M03 | history-section | Appendix C (v1.2 package ledger: inspected locations, package paths, validation scope; 9,488 chars) → removed; current editions are §6.1 and `BASELINE.md` | `programme-v1.2` |

Checker results: candidate = base + declared operations; 24 claim blocks byte-identical; RID set, source hashes and qualifier tags preserved; references resolve (the `programme-` prefix is checked; every other tag in the file is a known repository tag by the profile); one footer. The Programme invariants (five OPEN RIDs and ACTIVE lines, SG-PROG-1–4 text, §6.1 table, §7.2 register, Appendix B, all `<a id>` anchors except `prog-sources`) hold.

**Carried, not moved — Appendix B.** The adopted replacement ledger of v1.1 statements (PROG12-C01–C12) is history under Methodology v1.4 §1.1, but its prose carries claim-tag spellings (`[HYP]`, `[HEUR strong]`), which the compaction tool refuses to relocate outside table rows (control N3 shows the refusal). It stays in the live file as an explicitly historical appendix; a future edition may move it by a stage-1 content decision or after a tool change. The `prog-sources` anchor leaves with Appendix C; no live text points to it.

## 4. Facts the reviewer should check

1. §6.1: every tag exists and its edition matches `BASELINE.md` (gate G7 does this mechanically; the reviewer confirms the class and tier placements, which are editorial).
2. §7.2 consumer pins: each pin is a version string that occurs in the named consumer file at its governing tag (gate G8). The reviewer confirms the *section* cited for each row; sections were read from the consumers' Import Ledgers (§7, §9.1 for NUMGEN, §8 for AZ, §11 for OFN, §2 for RRF, §7 for RER).
3. §6.2–6.5: no owner result is restated (gate G10 is a lexical proxy; the reviewer reads the text).
4. §8.2 κ table: section citations per row; the "atlas reading, not owner statement" qualifier on the κ ≡ γ row.
5. §9.2 executed / not executed per owner against the tags.
6. §4: the statement that only DZT and AZ headers declare an A–D grade at their governing editions.

## 5. Records

- Advisory: `records/programme/ATLAS_ADVISORY_PROGRAMME_v1_2.md` (PI decisions in its §5).
- v1.2 release record, change record, `adoption_record.json`, `source_inventory.json`, `interface_register.json`: searched for by the PI on 23 October 2026 and **not found**; recorded as missing; nothing reconstructed. The v1.2 header's adoption statement (PI, 20 September 2026) stands as the adoption evidence for v1.2.
- Evidence of this release: `evidence/programme/scripts/` (two builders, stage-1 checker, stage-2 negative controls) and `evidence/programme/v1.3/` (edit log, movement map, checker outputs and reports).

## 6. Reviews and adoption

| Step | Who | Result |
|---|---|---|
| Stage-1 change-focused review | ChatGPT | **ACCEPT WITH MINOR EDITS** (24 Oct 2026, on `951371d` / `f7ff205`): class and tier placements, §5 custody/criteria split, §4 maturity statement (DZT and AZ Level A; no other header verified to declare one) and §7.2 pin treatment confirmed. P13-R1: the κ table has eleven rows, not twelve — the count in this record is corrected (the table is unchanged; the twelfth row of the draft, κ_f, was dropped before stage 1 because Genesis writes no such symbol). P13-R2: at publication the adopted file's SHA-256, `BASELINE.md`, this record and the annotated tag must name the same bytes; `01199132…2a35` is the candidate identity. |
| Stage-2 mechanical review (movement map, tool run, controls) | ChatGPT | M01–M03 accepted; 24/24 claim blocks; Appendix B carried as a documented exception; checker and controls not independently rerun by the reviewer (editor's runs in `evidence/programme/v1.3/`). No further review round requested. |
| PI adoption | PI | **ADOPTED**, 24 October 2026, 00:16 +03:00, in the atlas session: "Evet programme DSN dokümanını bu haliyle benimsiyorum." (verbatim; yes, I adopt the Programme DSN document as it stands). Given on the stage-2 candidate `01199132…2a35` after the ChatGPT review (ACCEPT WITH MINOR EDITS; P13-R1 applied to this record, P13-R2 satisfied below). |
| Publication transform (status lines only) | editor | done: `evidence/programme/scripts/release_programme_v1_3.py` on `01199132…2a35` → **adopted file `1b8358b3e1d3abb853e226786d21e6559c289b7c85570dac0ff1ebc2dabaea06`** (three status lines: header Document status, Appendix A heading, footer; nothing else). `BASELINE.md` Programme row → v1.3 and this hash. |
| Merge commit (not squash; `951371d` must stay reachable as the stage-2 archive), annotated tag `programme-v1.3` naming the hash above | PI | pending |

## 7. After adoption

- `BASELINE.md`: Programme row → v1.3 and its hash (part of the publication commit).
- Consumers that pin Programme v1.2 (DYAD, GEN, NUMGEN, TRIAD, UVM header companions; TDRG pins v1.1) are notified with the release hash when the cross-stream notice structure exists (PI decision of 23 October 2026); nothing in v1.3 changes a statement any of them imports.
- Atlas: SOURCES row PROG → `programme-v1.3` at the next refresh; H10 and PROG.G1/G2/G4 close; PROG.G6 (Pre-Legacy pass) and PROG.G7/H8 (κ) are now recorded in the Programme itself.
- Next owner passes in the v1.2 order: Pre-Legacy, TDR-G, DZT, AZ.
