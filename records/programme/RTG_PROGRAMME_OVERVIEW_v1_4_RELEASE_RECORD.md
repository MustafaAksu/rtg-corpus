# Programme Overview v1.4 — release record

**Status:** CANDIDATE — awaiting change-focused review (ChatGPT) and PI adoption. `programme-v1.3` governs until adoption.
**Editor:** Claude (atlas owner), by PI decision of 4 November 2026 in the atlas session: "programme i yapıp geçelim" ("let's do the Programme and move on"), given after the editor offered the Programme v1.4 sync as the next step. The editor role is as for v1.3. **Reviewer:** ChatGPT (change-focused). **Adoption:** PI.
**Object:** `dsn/RTG_PROGRAMME_OVERVIEW.md`. **Governing rules:** Methodology v1.4 (§§1.1, 3.3, 13), `CONVENTIONS.md`.

## 1. Build (branch `claude/programme-v1.4`)

There is one content stage and no compaction.

| Object | SHA-256 | Notes |
|---|---|---|
| Base: adopted v1.3 (tag `programme-v1.3`) | `1b8358b3e1d3abb853e226786d21e6559c289b7c85570dac0ff1ebc2dabaea06` | 614 lines |
| **Candidate v1.4** | `d109c78b9924b325e590159796b01223b82959211809106eea3dce009f6673bd` | 628 lines, 73,376 B |
| Builder `evidence/programme/scripts/build_programme_v1_4.py` | `ef4b313c9b889233e4c2294fbe46a970605b5446d627dbc5522560ca745b0a2a` | 71 exact-once edits (`rep` / `line`) |
| Edit log `evidence/programme/v1.4/edit_log.json` | `1c8617a94c4c1185be546e6401a1ac4fd02bfd6331d121b43d76fb5662ed1890` | old and new text with hashes for every edit |
| Checker `evidence/programme/scripts/check_programme_v1_4.py` | `f351e9f2fe405fd246f637415f72c4af3fda1b9406ec05077ba37bbd3c8200ce` | 17 gates (C0–C16) and 18 negative controls |
| Checker output `evidence/programme/v1.4/check_output.txt` | `ea401320548282e3b6e84c3d016261cdf3028c32d1c282ef3c69bbd4ae67198d` | 17/17 PASS; 18/18 controls caught |
| Publication transform `evidence/programme/scripts/release_programme_v1_4.py` | `ff68ac4aa8cc37763dc21d0569764cc893203578f55ae1e94e43d12ba7b922a4` | status lines only (3 lines): header Document status, Appendix A heading, footer |

**Reproduce** (repository root, with the tags):

```bash
git show programme-v1.3:dsn/RTG_PROGRAMME_OVERVIEW.md > base.md
python3 -I evidence/programme/scripts/build_programme_v1_4.py base.md cand.md log.json      # → d109c78b…73bd, log byte-identical
python3 -I evidence/programme/scripts/check_programme_v1_4.py base.md dsn/RTG_PROGRAMME_OVERVIEW.md evidence/programme/v1.4/edit_log.json --controls
```

Two runs of the builder gave byte-identical candidates and logs.

## 2. Changes, by input

| Input | Edits | What changed |
|---|---|---|
| Governing editions of 4 November 2026 (`BASELINE.md` and the tags) | H-1–H-8, S0-1, S6-0, S6-1-*, S6-2-*, S6-3-*, S6-4-TDRG, S6-5-ATLAS, S4-2, S4-3 | Eight §6.1 rows moved: OFN v0.12, NUMGEN v1.21, DYAD v6.4.23, TRIAD v1.7, GEN v2.10, RECOG v0.3.27, TDR-G v2.12.14 and Atlas v0.9. The §6.2–6.5 entries were re-read against each owner's Import Ledger at its tag. Corrections: DYAD's only scientific imports are RECOG's; GEN imports no OFN claim (OFN and the Programme are companion references there); TRIAD's RRF, OFN, Programme and TDR-G rows are reference-only; TDR-G pins OFN v0.10 and cites Programme v1.3. §4 records re-read at the two headers named in the table. |
| v1.3 residue | S6-1-PROG, S6-2-PROG | v1.3 kept its candidate wording after adoption ("v1.3 (this edition; v1.2 governs until adoption)", "v1.3 candidate"). v1.4 words the PROG row and the §6.2 entry so they hold before and after adoption, and the publication transform touches only the three status lines. |
| §7 interface register | S7-1, S7-2-* | Consumer pins were re-read at each consumer's governing tag for the consumers whose edition moved (DYAD, TRIAD, GEN, NUMGEN, RECOG, OFN, TDR-G): IF02–IF07, IF12, IF14, IF16, IF25–IF27, IF29 and IF31. Rows of unchanged consumers are unchanged. Two rows are new: **IF37** GEN → NUMGEN (`GEN-ART-SATURATION`, NG-10 only), an import present since before v1.3 (NUMGEN v1.20.8 §9.1) that v1.3 did not list; **IF38** NUMGEN → GEN (`NUMGEN-RESULT-N3CP-CYCLIC-AVERAGE`, GEN v2.10 §7). Both edges were added to the §7.1 graph. |
| `pipes/PROG/20261026-GEN-kappa-table-kappa-f-row-and-e-p13-1.md` and the v1.3 post-release note E-P13-1 | S8-2-1, S8-2-3 | The class-C κ row now reads "OFN §11.4 and RRF §6.2a record γ ≡ κ as the class-C parameter convention (Genesis writes γ)", the wording given in E-P13-1. A κ_f row was added (GEN §6.8 definition; Genesis states it distinct from the birth coefficient, κ_phys, κ_RTG and γ). |
| Section-pointer check of §8.2 at the new tags | S8-2-2, S8-2-4 | The CN-05 row points to TRIAD §6.18 and §7.4; TRIAD's header and §3 no longer carry CN-05 at v1.7. The TDR-G ρ·σ·κ row points to TDRG §2 (TDR-24B), where the rejected basis is recorded. |
| `pipes/PROG/20261030-OFN-v0-11-adopted.md`, `…-OFN-v0-12-adopted.md` | S5-1, S5-2, S6-2-OFN, S7-3 | OFN v0.12 is the criterion home of OPEN-P0 (§§5, 9) and OPEN-P2B (OPEN-OFN-3B, `RTG-OFN-OPEN-PRIMACY-3B`). The criterion wording was checked at `ofn-v0.12` (§8: "row agreement … insufficient"). Both notices are recorded as received in §7.3. |
| `pipes/PROG/20261103-TRIAD-v1-7-adopted.md` (CN-05; IF07/IF11) | S7-3, S7-2-IF07 | CN-05 is received and accepted, with no action: no Programme statement uses the withdrawn T-6 exports, and the Programme issues no cascade verdict. IF07 now carries Genesis's pin v1.7. IF11 stays v1.6, because it is OPEN M's own pin (`uvm-v0.7.1`), which the Programme records and does not set. |
| TDR-G v2.12.14 | S6-4-GATE-1/2, S7-3, S9-2-TDR-G | The launch-gate record now cites the owner's alignment of Appendix C with §§1–2 (v2.12.14, I07). It also records that one §7 export row (`TDRG-EXPORT-DISCRETE-TRIAD`) still names the earlier D/A/B gate. The TDR-G owner pass is recorded as "executed in part": a corrections edition, with the Methodology v1.4 migration planned for v2.13. |
| §9 maintenance record | S9-2-*, S9-3 | State at 4 November 2026; queue: Pre-Legacy, TDR-G (Methodology migration), DZT, AZ. The tag sentence is no longer tied to one edition. |
| Release entry | A-1, F-1 | Appendix A v1.4 DRAFT entry; footer. |

**Not changed:**
- §1, §2, §3;
- the §4 semantics;
- the §5 criteria, the five OPEN RIDs and their ACTIVE status;
- the §6.6 table and the §6.7 queue;
- SG-PROG-1–4;
- the anchors;
- Appendix B (byte-identical, gate C13).

The tag multiset `[DEF]`×10, `[HYP]`×5, `[COR]`×3 is unchanged (gate C6).

## 3. Checks (`evidence/programme/v1.4/check_output.txt`)

| Gate | What it establishes |
|---|---|
| C0–C2 | The base is `programme-v1.3`. The candidate equals the base plus the 71 logged edits, and undoing them recovers the base. |
| C3–C6 | The OPEN RIDs and ACTIVE lines, the scope guards, the anchors and the claim-tag multiset are as in the base. |
| C7 | Each §6.1 row names an existing tag that is the latest of its prefix, with a matching edition. The file's SHA-256 at the tag equals `BASELINE.md`. |
| C8 | 48 pins: each version in a §7.2 pin cell occurs in the named consumer file read at its governing tag. Presence only; the section reading is the reviewer's check (§4). |
| C9, C11–C14 | Heading set; no versioned filename; no stale Methodology pointer; Appendix B unchanged; no superseded tag of a moved study in §6.1–6.5. |
| C10 | §6.2–6.5 carry no owner mathematics: no number with three or more decimals, no "⇒" or "$$". |
| C15 | The four receiver items are answered in the text. |
| C16 | IF01–IF38, each once, in order. |

**Negative controls K1–K18: 18/18 caught**, each at its target gate. They cover an undeclared edit, an OPEN status change, a guard edit, a dropped anchor, a THM tag, a wrong edition, a superseded tag, an invented pin, a pin from the wrong consumer, restated science, a versioned filename, a stale Methodology pointer, an Appendix B edit, a stale §6 tag, the E-P13-1 wording restored, a dropped CN-05 receipt, a duplicate IF id and a renamed heading.

**Limits:**
- The checks are administrative.
- C8 shows only that a pin exists in the consumer file. Whether it is the consumer's pin for this interface comes from the editor's reading of the Import Ledgers.
- No owner mathematics is re-proved, and no owner claim is restated.

## 4. Facts the reviewer should check

1. **§7.2 sections and pins** for the re-read rows (IF02–IF07, IF12, IF14, IF16, IF25–IF27, IF29, IF31) and the two new rows IF37 and IF38. The editor read:
   - DYAD §7.0 (current-editions table) and §7;
   - TRIAD §7.1, §7.2;
   - GEN §7 ("Consumers" and "Pins");
   - NUMGEN §9.1 (Import Ledger table and "Consumers and pins");
   - RECOG §7 (synchronization note);
   - OFN §11;
   - TDRG §7.
2. **"Executed in part"** for the TDR-G owner pass (§6.4, §9.2). This is the editor's reading of a corrections-only edition that advances the v1.2 owner-review tasks; the alternative is "not executed".
3. **The CN-05 disposition** (accept, no action) and the IF11 explanation.
4. **The κ_f row wording** against GEN v2.10 §6.8.
5. **The corrected import descriptions** of DYAD, GEN and TRIAD in §6.3. Each is narrower than the v1.3 wording.

## 5. After adoption (PI; then the editor)

1. **Publication transform.** The editor runs it on the reviewed candidate with the adoption date. It changes three status lines and nothing else. `BASELINE.md` Programme row → v1.4 and the adopted hash.
   - With the date "4 November 2026" the adopted file is `bf4dfe1368fb47c0c3171f3e21d1184dfbbccfdf6ed4c29c7a9fbe9afde48ba3`. This is a test value: the adopted hash is recorded only after the transform has run on the reviewed candidate with the actual date.
2. **The PI merges with a merge commit and creates the annotated tag `programme-v1.4`** naming that hash. On the server:
   ```bash
   cd ~/rtg-corpus && git fetch origin && git checkout main && git pull --ff-only
   gh pr merge <PR> --merge --repo MustafaAksu/rtg-corpus && git pull --ff-only
   sha256sum dsn/RTG_PROGRAMME_OVERVIEW.md        # must equal the adopted hash in this record
   git tag -a programme-v1.4 -m "RTG Programme Overview v1.4 — adopted <date>; SHA-256 <adopted hash>"
   git push origin programme-v1.4
   ```
3. **The editor closes the four `pipes/PROG/` items** as receiver, each with a disposition pointing here, and regenerates the inbox index.
4. **Notices to the consumers that pin Programme v1.3:** DYAD, GEN, NUMGEN, TRIAD, TDR-G and OFN. Nothing they import changes. SG-PROG-1–4 and `RTG-OPEN-GENERATOR-SELECTION` are unchanged.
5. **Atlas:** SOURCES row PROG → `programme-v1.4` at the next refresh; PROG.G8 (κ table) closes.

**Not done here, and outside the Programme's custody:** the `BASELINE.md` RECOG row still says the `recog-v0.3.27` tag is "to be created by the PI", although the tag exists. That row is maintained with the RECOG release.

## 6. Reviews and adoption

| Step | Who | Result |
|---|---|---|
| Change-focused review | ChatGPT | *(pending)* |
| PI adoption | PI | *(pending)* |
| Publication transform; `BASELINE.md` | editor | *(pending)* |
| Merge commit, annotated tag `programme-v1.4` | PI | *(pending)* |
