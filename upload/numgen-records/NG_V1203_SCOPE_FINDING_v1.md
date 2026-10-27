# v1.20.3 Pre-Execution Scope Finding — the Inventory Moves Theorems Away from Their Definitions

**Memo ID:** `NG_V1203_SCOPE_FINDING_v1` · **Date:** 2026-09-25 · **Auditor:** Claude
**Ruling received:** v1.20.2 FROZEN (`35fe1a65…dd1053`) · v1.20.3 GO.
**Status:** **execution paused before the first write.** Nothing in the owner file has been moved. One ruling needed.

## 1. The finding

The approved inventory covers the **119 theorem-grade** §2 blocks. §2 also contains **111 non-theorem claim blocks** (36 GUARD, 30 DEF, 17 COR, 14 OPEN, 6 INTERP, 4 NUM, 2 HYP, 1 POSTHOC-DIAG, 1 HOLD) and **111 unanchored lines** (`**RID:**`, `**Status:**` of registry-native modules, `**Question:**`, candidate definitions, tables, code). In **29 modules**, **105** of those blocks sit beside theorem blocks that the inventory moves.

Executed as approved, theorems move to §6 and their **definitions, guards and hypotheses stay in §2**. Every gate would pass — text moves verbatim, nothing is lost, no status changes — and the document would still be scientifically worse. No checker can see this, because it is a *reading-context* defect, not a content defect.

**Case 1 — a theorem separated from its hypothesis.** M-1B reads *"On `D_chain`, M-1A gives `(A,C) ∈ R_bd` …"*. M-1A, M-1B and the WD-DOM/WD-VAL results are inventoried MOVE → §6.6; the `[DEF] Chain domain` defining `D_chain` (L1608) is not inventoried and stays in §2.

**Case 2 — the same, one level up.** L1674–1730 under the NG-7 parent heading is the NG-7 set-up: edge data `R_ij`, `a_ij = log R_ij`, node potentials — the objects NG-7A's null theorem `h = Ca` is *about*. NG-7A's theorems move to §6.8; the set-up (37 items) stays in §2.

## 2. Supplementary inventory — dry proposal only

`NG_V1203_SUPPLEMENTARY_INVENTORY_PROPOSAL_v1.json`, 222 items (111 blocks + 111 lines), rule: *a non-inventoried §2 item co-moves verbatim, in original order, with the module whose theorem blocks MOVE; modules with no theorem blocks are registry-native and stay in §2.* Result: **122 CO-MOVE**, **87 STAY-§2**, **13 OPEN/HOLD inside co-moving modules** (the open question below).

That rule is **not sufficient** as stated: Case 2 shows parent-level shared set-up is classified STAY because the parent has no theorem blocks of its own, although its CLOSED child's theorems move. A correct rule must be **hierarchical**.

## 3. Recommendation — module-level migration

Move each module **as a unit** — heading, set-up, DEF/GUARD/COR, theorems, and its OPEN/HOLD residuals, verbatim and in order — to its §6 destination. §2 then holds only the queue and **registry rows** (structural, one per ACTIVE/PARTIAL/OPEN/HOLD/SPLIT item, pointing to its §6 body), which is exactly the target architecture of spec v1.1 §2.

Reasons: (a) it is the only rule that keeps every theorem adjacent to its hypotheses and guards; (b) §6 destination headings already anticipate it — §6.8 reads *"NG-7A closed / NG-7B open"*, and §6.5 N-4 and §6.7 N-6 exist, so OPEN modules have homes; (c) block hashes are preserved more reliably, because each block keeps its original terminator; (d) the 13 OPEN/HOLD residuals keep their context (e.g. C7C-M's `[OPEN] Full-interface typed WD-DOM` stays beside M-1A/M-1B), while §2 gains a pointer row for each.

**Gates are unchanged in kind**: FP-v2 (verbatim, no loss/invention), INV-S final (statuses to registry rows or §6 bodies), INV-P extended to the supplementary items, INV-LIVE, queue identity, stale-grep.

## 4. What I need

A ruling on **scope**: (A) execute the approved 114/4/1 plan only, accepting that theorems separate from their definitions and §2 stays large; or **(B) module-level migration** as in §3, which relocates the 222 supplementary items as well, with a freshly frozen hierarchical inventory before any write. I recommend **(B)**. It is a larger relocation than the one approved, which is why I have not started it on my own authority.

## 5. Done in this pass (documentation only, non-blocking)
`ng_migration_checks_v2_1.py` — header now states INV-Ppost does **not** check REGISTRY-ONLY placement (INV-S final S3 does) and defines the **composite gate** FP-v2 + INV-S final + INV-Ppost + INV-LIVE. `ng_inv_live_v1_1.py` — role stated as **secondary lint**; FP-v2 is the primary no-content-change gate. **Both are comment-only: AST identical to their predecessors.**
