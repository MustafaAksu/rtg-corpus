# Remaining grade items after v1.20.7 — ruling table (DRAFT)

**Doc ID:** `NG_V1207_REMAINING_GRADE_TABLE_DRAFT_v1` · **Base:** v1.20.7 candidate · **Criterion:** frozen K1–K6 (`NG_V1206_RULING_LEDGER.json`)
**Status:** proposals only; nothing applied. If ruled before the v1.20.7 freeze, the approved rows can be folded into v1.20.7; otherwise v1.20.8.

**Correction to the v1.20.7 working note.** I first classed B8–B11 as needing a ruling because each summarizes several owners. Checking the owners shows every summarized module is single-grade `[RESULT] [from: ALG]` — N-1 (L420), N-2 (L1166), N-2-ORD (L1281), NG-7A (L2337), NG-8A (L2494), NG-8B (L2513), and C1–C6 / N5-PHYS-1 (all ALG, v1.20.6 review). So B2 and B8–B11 are **pure K5 mirrors**; only B5 and the DEF/INTERP row bundle parts of different status.

| row | v1.20.7 line | text (short) | summarized owners | proposal |
|---|---|---|---|---|
| B2 | §6.3a N-2-ORD | "physical order is reachability-first …" | N-2-ORD `[RESULT][from: ALG]` | **K5 sync** → `[RESULT] [from: ALG]` |
| B8 | §8 | "NG-8A and NG-8B are now closed" | NG-8A, NG-8B, both ALG | **K5 sync** → `[RESULT] [from: ALG]` |
| B9 | §8 | "NG-7A closed at v1.5 and N-2-ORD at v1.6" | NG-7A, N-2-ORD, both ALG | **K5 sync** → `[RESULT] [from: ALG]` |
| B10 | §8 | "Foundational chain complete: N-1 → N-2 → N-2-ORD" | N-1, N-2, N-2-ORD, all ALG | **K5 sync** → `[RESULT] [from: ALG]` |
| B11 | §8 | "N-5 architecture has negative and positive physical tests" | C1–C4, C5, C6, N5-PHYS-1, all ALG | **K5 sync** → `[RESULT] [from: ALG]` |
| B5 | §6.6 | "C7C-WD ADOPTED; C7C-0 CLOSED" | C7C-WD `[DEF]` (L1973); C7C-0 `[RESULT][from: ALG]` (L1980) | **SPLIT (K2)**: framework-adoption sentence → `[DEF]` mirror of C7C-WD; descent/involution sentence → `[RESULT] [from: ALG]` mirror of C7C-0 |
| DI | §8 | "Paradigm synchronization complete … composition-first … no universal claim that ratio is ontologically prior … NG-0R/SG-NG-22 require sector-specific mechanisms" | paradigm stance (NG-0R, SG-NG-22) | **SPLIT (K1/K2)**: stance ("composition-first and representation-after-construction"; sector-specific mechanisms required) → `[DEF]`; "makes no universal claim that ratio/proportion is ontologically prior …" → `[GUARD]` (a scope restriction, not an interpretation claim) |

Effect if all rows are approved: 0 bare RESULT and 0 combined truth-status tags left in live text.
