# Atlas advisory — Programme Overview v1.2 → v1.3

**Date:** 23 October 2026. **From:** Claude (atlas owner). **To:** the PI and the Programme editor. **Status:** advisory; the Programme editor and the PI decide every row. Nothing here changes a document.
**Object:** `dsn/RTG_PROGRAMME_OVERVIEW.md` v1.2, tag `programme-v1.2`, SHA-256 `4207da05dca24256e7bc528cb9814f848838bcd98e3d01222fb2a633ec9fd359`, adopted 20 Sep 2026 under Methodology v1.3. 686 lines.
**Basis:** atlas v0.3 (`atlas-v0.3`) H10, PROG.G1–G7; `BASELINE.md` at `main` (`bfd88cd`); the owner files at their tags; `CONVENTIONS.md`; Methodology v1.4 §§1.1, 13.6–13.9.

## 0. Why now

Programme v1.2 is the corpus's entry point and the only Tier 0 document. It describes the September 2026 snapshot: 14 homes at editions that were current then, owner status reports written from those editions, and a maintenance sequence that has since been largely executed. Since then eight of its fourteen homes have new adopted editions, four live documents it does not list have been adopted or placed, Methodology moved to v1.4, and the corpus moved into the git repository with tags as the governing identity. Every current reader — including every AI session that starts from the Programme — is pointed at superseded owner states (atlas H10).

The Programme itself foresaw this: §9.2 says pass two "updates the consumers … and the Programme scientific synthesis" and that a material change needs a new immutable version. This advisory is the input to that pass-two version.

## 1. Proposed outcome and release contract

- **Programme Overview v1.3** under Methodology v1.4, built in two stages like DYAD v6.4.21 and RECOG v0.3.23: stage 1 corrections (current editions, inventory, interfaces, status reports, governance pointers), stage 2 layout-only compaction (current-only header, Appendices B/C history to records), checked with `tools/check_compaction.py` on a Programme profile.
- **No science.** The Programme owns no theorem. v1.3 changes no OPEN-P status (P0, P1, P2A, P2B, P3 stay ACTIVE), no maturity grade, no scope guard wording unless the editor proposes it, and transfers nothing.
- **Governing-edition rule (new, small):** the Programme inventory lists each home by its governing tag (Methodology v1.4 §13.9) and says that `BASELINE.md` is the machine-readable form. It does not restate owner status summaries; it points to them.
- **Editor:** v1.2's revision editor was ChatGPT. The PI names the v1.3 editor; the other party and the atlas owner review. Suggested branch `claude/programme-v1.3` or `chatgpt/programme-v1.3` per CONVENTIONS §6.

## 2. Findings register

Types: S stale, I identifier/edition, Y synchronization, E editorial/structure, G governance. Tier A = must be in v1.3; B = same release unless the editor objects; C = optional.

### 2.1 Tier A

**PA-01 | I/S | Inventory editions (§6.1 table, §0.1, Appendix C).** Nine of fourteen rows name superseded editions:

| Key | §6.1 says | Governing now (`BASELINE.md`, tag) |
|---|---|---|
| METH | v1.3 | v1.4 `methodology-v1.4` |
| PROG | v1.2 | v1.3 on adoption |
| OFN | v0.7 | v0.10 `ofn-v0.10` |
| LEGACY | v0.6 | v0.7 `legacy-v0.7` |
| NUMGEN | v1.18 | v1.20.8 `numgen-v1.20.8` |
| DYAD | v6.4.9 | v6.4.22 `dyad-v6.4.22` |
| TRIAD | v1.5 | v1.6.1 `triad-v1.6.1` |
| GEN | v2.8.4 | v2.8.9 `gen-v2.8.9` |
| UVM | v0.6 | v0.7.1 `uvm-v0.7.1` |
| RECOG | v0.3 | v0.3.23 `recog-v0.3.23` |
| PREL, DZT, TDRG, AZ | v0.8, v0.8, v2.12.13, v0.6 | unchanged |

Action: replace the "selected edition" column by governing edition + tag; drop the filename-with-version column (CONVENTIONS: fixed filenames); note that `BASELINE.md` carries the hashes. Appendix C's per-source "inspected locations / package paths under `sources/`" are history (PA-08).

**PA-02 | I | Inventory omits four live documents and the atlas (§0.1, §6.1, §7).** Not listed: RRF v0.8.4 (adopted working standard; namespace `RRF` registered in Methodology v1.4 §4.2), RER v0.2 (adopted noncanonical registry), FMS v0.6.4 and ER-2B v0.3 (noncanonical, `noncanonical/`), and the derived State Atlas (`atlas/`, noncanonical, accepted v0.3). "14 document homes" is therefore no longer the count. Action: add a class column (canonical / adopted standard / noncanonical registry or study / derived map) and rows for RRF, RER, FMS, ER-2B, ATLAS with their tiers and roles; state in §0.1 what noncanonical and derived mean for a reader (owner DSN wins; no claim sourced from them). Atlas PROG.G2.

**PA-03 | S/E | Owner status reports (§6.2–6.5) are September snapshots.** Examples that are now wrong or misleading: NUMGEN "the missing dedicated defect-threshold theorem RID is an owner-assignment task" (v1.20.8 registers `NUMGEN-THM-N5AS1-DEFECT-THRESHOLD-RATIO` and the N5AS1 RIDs; the Lemma 3 closure the Programme reports is still correct, at v1.16); DYAD "v6.4.9 reports the cubic module… higher-order interface in the owner-review queue" (v6.4.22: §6.14 return enclosure, OPEN 3/21 closed conditional on RECOG R9, L-PHASE row A THM, smooth embedding); RECOG "general-return theorem offered to Dyadic, not transferred… NUMGEN v1.18 synchronization an owner task… event rule and explicit-return-enclosure dependent results remain open" (v0.3.23: R2, R7–R11 CLOSED, R1/R3 PARTIAL, R4–R6 ACTIVE; bridge-lemma custody settled as DYAD RID + RECOG proof, no transfer pending; NUMGEN imports by RID at v1.20.8); OFN "v0.7 baseline; typing pending" (v0.10); UVM "v0.6… 2× short headline not adopted" (v0.7.1 R16: no certified deficit, 2× branch superseded); TRIAD, GEN, LEGACY likewise. Action (Methodology v1.4 §1.1 one home per statement): do not re-narrate owner science in the Programme. Each study gets a short, current, non-scientific row — edition/tag, role, programme-relevant open interfaces — plus a pointer to the owner's own status summary. Anything the Programme needs to say about an owner's state is a quotation with the edition named. Atlas PROG.G1.

**PA-04 | Y/I | Interface register (§7.1 graph, §7.2 IF01–IF25) stale and incomplete.**
- Edition pins in every IF line (OFN v0.7, TRIAD v1.5, GEN v2.8.4, UVM v0.6, NUMGEN v1.18, RECOG v0.3, METH v1.3) → current tags.
- IF14 "RECOG pins NUMGEN v1.15; target v1.18 pending" → RECOG v0.3.23 imports `NUMGEN-DEF-N5AS1-DEFECT`, `NUMGEN-RESULT-N5AS1-INF1` and the L1/N1C rows at `numgen-v1.20.8`; the v1.15 producer pins remain where load-bearing (RECOG §7).
- IF16 "primitive/normalized quintic interface unresolved" → RECOG R11 CLOSED at final-chart ledger scope (RECOG-ALG-CHART-LAWS); frame rule DYAD-ALG-KP-FRAME-SCALE.
- IF17 "RECOG → DYAD transfer proposal, not transferred" → closed as a custody split: `DYAD-ALG-BRIDGE-LEMMA` is Dyadic's RID, the general-$p$ proof is RECOG-ALG-LEADING-RETURN-EQUIVARIANCE; no transfer pending (RECOG v0.3.23 §6.10, DYAD §6.9). Retype as declared mutual citation or retire.
- New edges the owners now declare: DYAD → RECOG is now also RECOG → DYAD (DYAD v6.4.22 imports RECOG-THM-R9-MEMORY for T1/T2/OPEN 21 and RECOG-THM-A1A-RECIPROCAL-AMPLITUDE; `[THM] [assuming: RECOG-THM-R9-MEMORY]`); NUMGEN → RECOG is answered by RECOG → NUMGEN receipts (N15 row); RECOG → OFN (comparator DEFs, RF-O09-01/02), RECOG → RRF (§4.2a, §6.3), RECOG → RER (G9), RRF → DYAD/RECOG/OFN/GEN/TRIAD (representation standard), RER ↔ GEN/TRIAD/RECOG, FMS ↔ DYAD/GEN/RRF/OFN/NUMGEN, ER-2B ↔ TRIAD/GEN (atlas PROG.G2, H7). Types per §7.1 vocabulary; the Programme records that the owners declare them, it does not certify them.
- "RECOG -?-> DYAD general-return adoption" and "UVM -?-> GEN physical UV inputs" in the §7.1 request list: the first is closed (above); the second stands (OPEN M v0.7.1 still supplies no physical UV blocks).
Atlas PROG.G4.

**PA-05 | G | Governance pointers.** Header and §0.1: "DSN Methodology v1.3 governs" → v1.4 (tag `methodology-v1.4`); "available-source snapshot is September 20, 2026; selected source means the edition supplied" → the repository and its tags are the source (CONVENTIONS §1–§2); release-record and change-record file names (`RTG_PROGRAMME_OVERVIEW_v1_2_RELEASE_RECORD.md`, `…_CHANGE_RECORD.md`, `adoption_record.json`, `source_inventory.json`, `interface_register.json`) are cited but none is in the repository (`records/programme/` does not exist). Action: v1.3 gets its own release record at `records/programme/RTG_PROGRAMME_OVERVIEW_v1_3_RELEASE_RECORD.md`; the v1.2 originals are uploaded unchanged on `upload/programme-records` and hash-checked, as for RECOG; if an original cannot be found, that is recorded, not reconstructed.

**PA-06 | S | Maintenance sequence (§9.2) executed in part.** "Next owner OFN, then Legacy, Pre-Legacy, Dyadic, TDR-G, Number Genesis, DZT, Genesis primitive, Triadic, Genesis geometry, OPEN M, RECOG, AZ." Done since: OFN (v0.8–v0.10), Legacy (v0.7), Dyadic (v6.4.10–v6.4.22), Number Genesis (v1.19–v1.20.8), Genesis (v2.8.9), Triadic (v1.6.1), OPEN M (v0.7.1), RECOG (v0.3.1–v0.3.23); Methodology moved twice (v1.3 → v1.4). Not moved: Pre-Legacy (v0.8, June; atlas PROG.G6, PREL.P1), TDR-G (v2.12.13), DZT (v0.8), AZ (v0.6). Action: replace the sequence by the current state and the remaining queue; the Pre-Legacy pass is the oldest outstanding item and its stale pointers to OFN/GEN content are listed in the atlas (PREL.P1).

### 2.2 Tier B

**PB-07 | Y | OPEN-P registry owner pointers (§5).** P2B "no owner is assigned by this release" → OFN v0.10 holds the criterion as OPEN-OFN-3B (`RTG-OFN-OPEN-PRIMACY-3B`, invariant reduction; row agreement explicitly insufficient) and the atlas P2B-CRITERION node records the three-way identity P2B ≡ OPEN-OFN-3B ≡ (RRF reduction criterion). Programme should cite OFN as the criterion home and name no construction owner unless one exists (atlas PROG.G5). P0: OFN v0.10 and RRF v0.8.4 carry the admissibility/representation criteria; cite. P3: OPEN M v0.7.1 state (R15/R16) replaces the v0.6 text; the "2× short" line is now simply "no certified deficit" (atlas H2). P1: unchanged; note that NUMGEN's DISC sector and TDR-G remain the only discrete inputs and that no bridge charter exists.

**PB-08 | E/G | Live-file rule (Methodology v1.4 §1.1) — stage 2.** Current-only header (one status summary; "Revision base: 360 lines preserved byte-for-byte", "Revision editor", pass-one/pass-two narrative to the release record); Appendix A compact; Appendix B (twelve PROG12-C replacement entries of v1.1 wording) and Appendix C (package paths, "inspected locations") to `records/programme/`, kept at tag `programme-v1.2`. §0.1's "This adopted release completes the inventory/architecture stage of pass one…" paragraph is release narrative, not orientation.

**PB-09 | I | Maturity table (§4).** The "previous or owner-declared" column cites v1.1 and September headers (RECOG "A requested in v0.3 header"). Re-read the current headers; if an owner now declares a maturity, quote it with edition; if none does, say so. No grade is issued by the Programme (SG-PROG-2 stays).

**PB-10 | E | Count and wording of §0.1.** "six continuous technical homes … 14 document homes" → recount with RRF, RER, FMS, ER-2B, ATLAS and their classes; "Genesis's source header still says Tier 3/4" → check against `gen-v2.8.9`.

**PB-11 | G | Programme ↔ BASELINE consistency check (tool).** A small `tools/check_programme_inventory.py`: every row of §6.1 names the tag and edition that `BASELINE.md` and `git tag` give; every IF line's edition pin is a tag or an explicitly labelled historical pin; every cited record file exists. Run at each Programme release and, as a warning, at each owner release.

### 2.3 Tier C

**PC-12 | E | κ table (atlas H8, PROG.G7).** The Programme is the natural home for a one-page cross-stream symbol table for κ (class-C coupling κ ≡ GEN γ; Triadic/GEN birth κ; DYAD backbone κ; face-lift κ_f; RRF-CN05 κ; κ_RTG = 𝒢_e/J_e as HYP target; PREL κ = 2πc, κ_grav, κ_top, κ₃, κ′, κ_B), with owner and section per row. Navigation, not science; owners keep their symbols.

**PC-13 | E | AI-reader note.** One paragraph in §0 telling an AI session where to start: `BASELINE.md` for editions and hashes, `CONVENTIONS.md` and Methodology v1.4 for rules, `atlas/RTG_STATE_ATLAS.md` as a noncanonical map, the owner DSN for any claim.

### 2.4 Routed, no Programme edit

| Item | Owner | Note |
|---|---|---|
| Pre-Legacy stale pointers to OFN 3B / OPEN-OFN-6 / GEN sections | PREL | atlas PREL.P1; the Programme only records that the PREL pass is outstanding |
| OPEN-M-6 chart-dependent audit vs DYAD smooth equivariant chart | UVM | atlas OPENM.U1 |
| TDR-G launch-gate discrepancy (§6.4) | TDRG | unchanged since v1.2; Programme keeps recording it |

## 3. Owner disposition table (to be filled by the Programme editor; PI decides)

| row | tier/type | decision | reason | location | validation | consumers |
|---|---|---|---|---|---|---|
| PA-01 | A/I,S | | | §0.1, §6.1, App. C | inventory check vs `BASELINE.md` and tags | all |
| PA-02 | A/I | | | §0.1, §6.1, §7 | class column; RRF/RER/FMS/ER-2B/ATLAS rows | RRF, RER, FMS, ER-2B, atlas |
| PA-03 | A/S,E | | | §6.2–6.5 | no owner-science narration; pointers only | all owners |
| PA-04 | A/Y,I | | | §7.1, §7.2 | each IF pin a tag or labelled historical; new edges typed | DYAD, RECOG, NUMGEN, OFN, RRF, RER, FMS, ER-2B |
| PA-05 | A/G | | | header, §0.1, §9.3 | records uploaded or recorded missing | PI |
| PA-06 | A/S | | | §9.2 | — | PREL, TDRG, DZT, AZ |
| PB-07 | B/Y | | | §5 | OFN/RRF/UVM pointers at tags | OFN, RRF, UVM |
| PB-08 | B/E,G | | | header, §0.1, App. A–C | `check_compaction.py`, Programme profile | — |
| PB-09 | B/I | | | §4 | headers re-read | — |
| PB-10 | B/E | | | §0.1 | — | — |
| PB-11 | B/G | | | `tools/` | script + controls | — |
| PC-12 | C/E | | | new §8.2 or App. | owners confirm rows | all |
| PC-13 | C/E | | | §0 | — | — |

## 4. Open questions for the PI

1. Who edits v1.3 (ChatGPT as v1.2's revision editor, or Claude), and who reviews?
2. Are the v1.2 release and change records (and the three JSON registers) available for `upload/programme-records`?
3. Does the Programme list the atlas as a (derived, noncanonical) home? The atlas Method says it is never a source; listing it as a map, not a home, avoids that reading.
4. PC-12 κ table: Programme home, or a separate small record under `records/programme/`?

## 5. PI decisions (23 October 2026)

1. **Editor:** Claude (atlas owner) writes v1.3; ChatGPT reviews (change-focused review of stage 1, mechanical review of stage 2).
2. **v1.2 records:** the PI searched and did not find `RTG_PROGRAMME_OVERVIEW_v1_2_RELEASE_RECORD.md`, `…_CHANGE_RECORD.md`, `adoption_record.json`, `source_inventory.json`, `interface_register.json`. They are recorded as missing in the v1.3 release record; nothing is reconstructed. The v1.2 header's statement of the PI's adoption on 20 Sep 2026 stands as the adoption evidence.
3. **Atlas:** listed in the inventory as a derived, noncanonical map, not a home; never a source of a claim.
4. **κ table (PC-12):** inside the Programme (one section), not a separate record.
