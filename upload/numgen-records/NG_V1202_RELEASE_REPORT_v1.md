# v1.20.2 Sync Patch + Checker v2 — Release Report

**Report ID:** `NG_V1202_RELEASE_REPORT_v1` · **Date:** 2026-09-25 · **Auditor:** Claude
**Ruling implemented:** freeze manifest APPROVED · 119-block inventory APPROVED, NG-10 → `§6.9a` · v1.20.2 two-item sync patch GO · structural rewrite HOLD, renamed **v1.20.3**.

## 1. Blockers — all four reproduced independently before any fix
STOP-02 (L2493 "relational-category architecture"), STOP-03 (L2554 "Dyadic v6.4.9"), INV-P false pass (valid 24-char prefix + `THIS IS BOGUS` → exit 0), INV-S unable to represent a legitimate verbatim relocation (N-1B status → §6.2 → exit 1).

## 2. v1.20.2 — two live corrections, nothing else
`RTG_NUMBER_GENESIS_DSN_v1_20_2.md` · 3207 lines · LF · `35fe1a65…dd1053`. Fingerprint v2.1 diff vs v1.20.1: exactly **2** blocks changed — the blocks *enclosing* the two corrected sentences (`Full NG-8 target` at L2487; proof-package item 6 at L2553, whose un-anchored item 7 carries the pin) — plus **3** new changelog blocks. Explicit RIDs identical; broad identifiers gain only `STOP-02`, `STOP-03`, `INV-LIVE`. Note: item 7's `[CLOSED by import]` is not an anchor, yet the edit was caught because block hashing absorbs it into item 6 — a line-level fingerprint would have missed it.

## 3. INV-LIVE — why STOP-02/03 escaped, and the fix
The inventory generator scanned only §2 theorem blocks, so §6 and §7 were invisible. INV-LIVE scans **all live text**, excluding the changelog, the Appendix A historical narrative, explicitly version-scoped `Historical (v…)` lines, Appendix B, and `[COR]` quotations. On v1.20.1 it flags **exactly** STOP-02 and STOP-03; on v1.20.2 it is **clean**; a planted withdrawn phrase is caught. `[COR]` A first draft flagged the `Historical (v1.19):` line — an explicitly historical record — because the history-block exit logic re-admitted that line as live; fixed.

## 4. Checkers v2
**INV-P v2:** exact normalized heading equality; one explicit exception, `APPROVED_NEW_HEADINGS = {§6.9a NG-10 …}`; new **post-write** mode resolving every MOVE hash under its destination, every retained twin, every discarded mirror's absence, and the approved heading's existence.

**INV-S v2:** relocation-aware — multiset conservation of normalized status text; MOVE statuses under the exact destination; REGISTRY-ONLY statuses on a registry row; registry-native statuses keep module identity (RID or deepest heading). Two modes: `final` (everything at target) and `partial` (each status unmoved *or* at target), so intermediate commits and single-relocation tests are checkable. `[COR]` The first v2 had only final semantics and failed the base-vs-base identity test with 18 errors — correct for a final check, useless for incremental verification; the partial mode fixes that.

| self-test | want | got |
|---|---|---|
| INV-S partial · identity | 0 | 0 |
| INV-S partial · co-owner relocation N-1B → §6.2 | 0 | 0 |
| INV-S partial · same status to wrong module §6.8 | 1 | 1 |
| INV-S partial · relocated and reworded | 1 | 1 |
| INV-S final · unmigrated base (= workload) | 1 | 1 — **18**: 15 MOVE + 3 REGISTRY-ONLY statuses |
| INV-P pre-write · rebased inventory | 0 | 0 |
| INV-P · co-owner false pass (prefix + BOGUS) | 1 | 1 |
| INV-P post-write · unmigrated base | 1 | 1 (116: 114 MOVE + 1 mirror + NG-10 heading) |

## 5. Inventory rebased
`NG_V1203_REVERSE_INVENTORY_v2.json` — base v1.20.2. All **119** block hashes unchanged (edits are outside §2). Every destination is an **exact** §6 heading or the approved `§6.9a`. Approved dispositions: 114 MOVE / 4 REGISTRY-ONLY / 1 MIRROR-RECONCILED / 0 STOP.

## 6. Superseded
v1.20.1 owner bannered (content without banner = frozen `00174c3a…`); `ng_migration_checks_v1.py` bannered; `NG_V1202_REVERSE_INVENTORY_v1.json` superseded by `NG_V1203_REVERSE_INVENTORY_v2.json` (base and NG-10 destination changed; dispositions identical).

## 7. Gate for v1.20.3
All four blockers closed; INV-LIVE, INV-S v2, INV-P v2 built and self-tested. **Awaiting co-owner freeze of v1.20.2 and GO for v1.20.3.**
