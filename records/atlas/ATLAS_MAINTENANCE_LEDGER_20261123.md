# Atlas maintenance ledger — the Atlas's own open debts at `atlas-v0.15`

**Date:** 23 November 2026. **By:** Claude, Atlas owner.
**Status:** [SESSION] maintenance record. It changes no byte of the accepted Atlas, starts no edition and decides nothing. Each item below becomes a reviewed item (Atlas Method v0.3 §7) of whichever later refresh opens its domain.
**Asked by:** the PI's work order relayed on 23 Nov 2026, 12:01 +03:00, item 4: the four compound heads in D5, OPENM.U10 and the checker's coverage outside Dyadic, in one maintenance record; no Atlas v0.16; no verdict on U10 before UVM's independent reading is compared.
**Basis:** `atlas-v0.15` (`483e6003…02df`), its manifest and check report; `tools/atlas_check.py` at `main` `98a4a80`; the 18 owner sources at their manifest tags. Counts are mechanical scans made for this record (`EV-SRC-READ`); no owner certificate was run.

## 1. Compound grade heads

**Carried so far:** "four Atlas-side compound heads in D5" (v0.14 record §3; v0.15 record §6).
**Found now:** a scan of every node head of `atlas-v0.15` for two grade tokens joined by "/" gives **13 heads, not four**. Nine lie outside D5. The earlier count came from the D5 opening of v0.14 and was never extended to the other domains. It was an undercount, not a regression: all 13 heads are byte-identical in `atlas-v0.14`.

A compound head is one of two kinds, and the kind decides who acts:
- **M — mirror.** The owner's text carries the compound token. The Atlas records it as declared. Unpacking is the owner's work (Methodology v1.4 §8.4); the Atlas follows the owner's next edition.
- **A — Atlas-side.** The owner's text gives separate, single grades, and the Atlas head joined them. The Atlas corrects its own head.

| Line | Head at `atlas-v0.15` | Domain, locator | Owner text observed for this record | Kind (provisional) |
|---|---|---|---|---|
| 103 | `O-LOCK DEF/ALG (formal family; …)` | D1, `@OFN§5.5.4` | not located by the string "O-LOCK" in `ofn-v0.12`; to be read at the opening | not yet read |
| 390 | `*DYAD:historical-fit-P0 ENG/NUM` | D2, `@DYAD§6.14` | `[ENG]` on the historical fit (line 872) and a separate `[NUM]` on the two-harmonic amplitudes (line 425) | A |
| 482 | `NUMGEN-OPEN-NG0R-COV OPEN→ALG/NUM` | D2, `@NUMGEN§6.1a` | RID line 363 read; the grade wording of §6.1a was not | not yet read |
| 649 | `*RECOG:resonance-arithmetic ALG/HEUR` | D3, `@§6.2` | two tagged sentences in one paragraph, `[ALG]` … `[HEUR]` … (line 403) | A; see §2.2 |
| 1050 | `GEN-OPEN-PHASE-MOMENT ALG/RES` | D4a, `@§2` | registry line 1266 ends `` `[ALG]`/`[RESULT…` `` | M |
| 1055 | `*GEN:OPEN1A-candidates RES/FAIL` | D4a, `@§2` | an Atlas pseudo-node; owner wording not read | not yet read |
| 1143 | `GEN-OPEN-SOURCE-PAIRING ALG/OPEN` | D4b, `@GEN§2,§6.9` | `[ALG]` `[scope: conditional on the declared lowering/sign branch]` (line 1274); "OPEN" is the item's status, not a grade | A |
| 1168 | `UVM-R7 INTERP/HYP` | D4b, `@UVM` | `` `[INTERP/HYP]` `` (line 307) | M |
| 1170 | `UVM-HYP-FRACTURE INTERP/HYP` | D4b, `@UVM` | `` `[INTERP/HYP]` `` (line 254) | M |
| 1310 | `*TDRG:TDR-24-factorization ALG/NUM` | D5, `@TDRG` | `tdrg-v2.13` carries no compound token; the owner's separate grades were not read | A |
| 1313 | `*TDRG:edge-builder ENG/ALG` | D5, `@TDRG` | as above | A |
| 1314 | `*TDRG:slot-volume ALG/NUM strong (TDR-24D CLOSED)` | D5, `@TDRG` | as above | A |
| 1345 | `*NUMGEN:imp-DISC DEF/THM import` | D5, `@NUMGEN§1.1` | two import blocks: `[DEF]` `[import: …DISCRETE_GENESIS_DSN_v2.12.13 §6.1 \| RID unavailable]` (line 69) for the state space; the recurrence block's grade was not read | A |

Kinds are provisional. A head is unpacked only against the owner's sentence, read at the opening; nothing is unpacked from this table. The mirror heads (M) belong to METH.M1 on the owner side. For UVM they are in the reactivation triage (PR #361, draft).

## 2. Grade diagnostics that may misdescribe the owner's tag

### 2.1 OPENM.U10 (UVM half) — no verdict

- **Atlas row:** "UVM-RESULT-M3A carries the compound grade [ALG/typing] … (METH §8.4 unpacking; ≡ METH.M1)".
- **Owner text** (`uvm-v0.7.1`, line 285): `` `[RESULT]` `[from: ALG/typing audit]` ``. The Atlas row misquotes it: the tag is a `[from: …]` qualifier on a `[RESULT]`, not a grade `[ALG/typing]`.
- **UVM co-owners' reading so far** (`records/uvm/UVM_REACTIVATION_TRIAGE.md` on PR #361, head `a9fd8b8`; a draft, not an owner disposition): not a false positive in substance. Methodology §3.4 pairs `[RESULT]` with exactly one canonical status, and "ALG/typing audit" is not one. On that reading the Atlas row quotes the tag wrongly and cites the wrong rule (§8.4 for §3.4).
- **State:** open. The Atlas owner's earlier suggestion of a possible false positive (PR #355, comment `7063674852`) is not maintained against that reading and is not withdrawn either: the UVM owners' disposition decides. After it, the row is reworded to the exact tag and rule, or retired. The GEN half of U10 (`GEN-OPEN-PHASE-MOMENT`, `*GEN:OPEN1A-candidates`) is GEN's.

### 2.2 `*RECOG:resonance-arithmetic` — the same pattern, found by the scan of §1

The node carries the inline flag "! D-GRADE compound (M1)". The owner's paragraph (`recog-v0.3.27`, line 403) has two separately tagged sentences, `[ALG]` then `[HEUR]`. If each sentence carries one grade, there is no owner compound: the compound is the Atlas head, and the flag points at the wrong side. To be read at the next D3 opening; no change now.

## 3. The shared checker's coverage outside Dyadic

**What the tool does** (`tools/atlas_check.py`): `check_coverage` iterates over the `[RID: …]` declarations of the DYAD source only (lines 267–272; RER local keys per its header). `check_qualifiers` reads DYAD declarations with `[assuming: …]` only (lines 293–297). The other 17 sources are checked for identity (`sources`), for the links and artifacts the Atlas itself cites (`links`, `artifacts`), and for keys and wording. Nothing checks whether each of their declared identifiers has a home.

**What has covered the gap:** since v0.13 every impact-refresh builder asserts one home for each identifier that is new in a moved source (`HOMES`, `homes_check`: TDR-G and AZ at v0.13 and v0.14, DZT at v0.15). Identifiers that existed before those refreshes were never checked mechanically.

**Measured for this record** (a string scan, not a coverage check): `[RID: …]` declarations at the manifest tags whose identifier string does not occur anywhere in `atlas-v0.15`, leaving out artifact, engineering and export identifiers:

| Source | Declared RIDs | Claim-type RIDs with no occurrence in the Atlas |
|---|---|---|
| TRIAD `triad-v1.7` | 51 | 9: `TRIAD-ALG-T6S-INPLANE-CHIRALITY`, `TRIAD-ALG-T6T-CHIRALITY-COUNT`, `TRIAD-ALG-T6U-APEX-SOURCE`, `TRIAD-OPEN-T6J2`, `-T6M`, `-T6M2`, `-T6N`, `-T6O`, `-T6Q` |
| TDR-G `tdrg-v2.13` | 81 | 5: `TDRG-DEF-KINEMATICS`, `TDRG-DEF-NARROW-BAND`, `TDRG-OPEN-BIND3-MEMORY`, `-NKSCAN`, `-REGEN` |
| GEN `gen-v2.10` | 75 | 2: `GEN-OPEN-CHIRAL-ADMISS`, `GEN-OPEN-GENII-ARCHIVE` |
| RECOG `recog-v0.3.27` | 159 | 1: `RECOG-ALG-A1C-INBLOCK-ANGLE` |
| OFN `ofn-v0.12` | 55 | 1: `RTG-OFN-DEF-COMPARATOR-TYPING` |
| UVM `uvm-v0.7.1` | 45 | 1: `UVM-NUM-CARRIER` |
| DZT, AZ, NUMGEN, Legacy, Pre-Legacy, ER-2B | 31, 46, 11, 8, 1, 1 | 0 |

That is 19 identifiers. A missing string is not proof of a missing home: the Atlas may carry the statement under a pseudo-label (`*TRIAD:…`) or inside another node, and some sources declare identifiers in other forms than `[RID: …]` (NUMGEN, RRF, RER, PROG), which this scan does not see. It is a list to read, not a list of defects. The same scan gives 0 for DYAD, the one source the tool covers.

**Options (for the PI, with the reviewer's view):**
1. Keep the tool as it is; go on asserting homes in each builder; read the 19 at the next opening of their domains.
2. Extend `check_coverage` to every owner whose declarations are `[RID: …]` tags (`TAG_CONVENTION`), with a reviewed home map per source. This is a change to a shared tool: its own PR, with controls and review, and a first run that will report today's gaps as failures to be dispositioned.
The Atlas owner's recommendation is option 2, done once and not inside an edition, after the NUMGEN and OFN advisories, so that it does not compete with them for review.

## 4. Other items carried at `atlas-v0.15` (from its check report and records)

| Item | State |
|---|---|
| Links, documented-unresolved: 1 | `DYAD-CAND-PHISTAR-ENTRY-PHASE` (never a Dyadic identifier; recorded as such) |
| Links, UNVERIFIED: 2 | NUMGEN declaration forms the checker cannot parse |
| Artifacts, UNVERIFIED: 2 | GEN `cm.py`, `fit.py` |
| Wording: 13 WARN | unchanged since v0.14 |
| Pipe census (NUMGEN.N-I1) | dated at snapshot `357b963` (147 items, 62 open); it moves with every filing and is restated at each refresh |
| Headline numbering | H3 retired at v0.15; H4–H12 keep their numbers (display order only) |
| Builder chain | `refresh_v0_15.py` imports helpers from `refresh_v0_13.py` and `refresh_v0_10.py`; each builder stops by design once a source tag is newer than its manifest |

## 5. What this ledger does not do

It does not change `atlas/RTG_STATE_ATLAS.md`, any evidence file, any tool or any pipe. It does not classify a head finally, decide U10, or assert that an identifier lacks a home. It records where to look. The next refresh is triggered as before: an adopted owner tag after `357b963`, or a verified correction need in the Atlas's own text that the PI wants made.
