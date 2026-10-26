# v1.20.2 Reverse Relocation Inventory, INV-S, INV-P — Report

**Report ID:** `NG_V1202_INVENTORY_REPORT_v1` · **Date:** 2026-09-25 · **Auditor:** Claude
**Base:** frozen v1.20.1 (`00174c3a…c927b`), fingerprint `c4b51f45…fdd3` (generator v2.1 `574d3319…f2e0`)
**Scope (per ruling):** inventory + INV-S + INV-P only. **No block moved.** v1.20.2 structural rewrite **HOLD**.

## 1. Result

All **119** §2 theorem-grade blocks (the INV-3 set) carry exactly one disposition and a destination:

| disposition | n |
|---|---|
| MOVE | 114 |
| REGISTRY-ONLY | 4 |
| MIRROR-RECONCILED | 1 |
| STOP | **0** |

Destinations: §6.2 N-1 → 33 · §6.3 N-2 → 6 · §6.3a N-2-ORD → 3 · §6.4 N-3 → 18 · §6.6 N-5 → 46 · §6.8 NG-7 → 9 · §6.9 NG-8 → 2 · **NEW-HEADING (NG-10) → 1** · registry (queue) → 1. Relationship metadata from the 24-pair review is kept as a separate field (`relationship`), not as a disposition.

## 2. Manual corrections to the first pass — three would have lost content

The first machine pass was corrected after reading every non-MOVE and every flagged block in full:

- **L645 (N-1C status) → MOVE, not REGISTRY-ONLY.** The status line carries a substantive residual clause on the same line: *primitive event-type/domain alignment is closed by the unified v0.9 six-phase `T`-tube construction; only general branching/topology-changing history semantics remain OPEN.* Reducing it to a registry row would have lost that OPEN claim.
- **L1735 (NG-7A status) → MOVE.** The status header is followed by the certificate pointer (`NG_NG7A_HOLONOMY_NULL_CERT_v1` + script/log). Provenance belongs in the §6.8 body.
- **Heading depth.** The first pass read only `##`–`####` and absorbed `###### L1 — Primitive-frame phase-uniform contraction` (own RID `NUMGEN-RESULT-L1-PRIMITIVE-CONTRACTION`) into N-1C. Now: **destination** from the nearest module-level ancestor; **`s2_submodule`** from the deepest heading. A first attempt at widening depth broke 16 destinations; the two-field design fixes that.

## 3. One ruling needed — DESTINATION-GAP (not a STOP)

**L2094, NG-10** — `[RESULT][from: NUM]` imported from Genesis (`GEN-ART-SATURATION`). §6 has **no NG-10 heading**, so the block has no authoritative destination. No content drift; a structural decision. Options: **(a)** create `§6.x NG-10 — Genesis saturation and counting truncation` (heading only, no new claim); **(b)** keep NG-10 as a §2 registry entry with the imported result as its §6 body under an existing heading. Recommend **(a)**: NG-10 is a named programme target with its own RID-bearing import.

## 4. INV-S — status conservation

Covers all **29** `Status:` lines, keyed by full heading path (depth ≤ 6) plus RID where present — including the 9 the block fingerprint cannot see. A change passes only via an allowlisted TAG-NORM that preserves the living-state keywords and the `[scope: …]` brackets. Self-tests: silently turning NG-7B `OPEN → CLOSED` → **exit 1**; stripping a `[scope: …]` bracket from N-1A-MIN → **exit 1**; baseline vs itself → **exit 0**.

## 5. INV-P — inventory / pointer integrity, before any file is written

P1 one allowed disposition per block · P2 destination is an existing §6 heading or a flagged NEW-HEADING · P3 every MIRROR-RECONCILED names a retained twin present in §6 (L996 → §6 L2357, hash attached) · P4 REGISTRY-ONLY only for bare status headers or the queue · P5 inventory set == INV-3 set exactly. On the inventory: **PASS**, one NEW-HEADING ruling pending. Self-test: a nonexistent destination → **exit 1**.

`[COR]` My first self-test run printed `exit=0` for failing cases: I had piped output through `tail`, so `$?` reported `tail`'s status, not the checker's. Re-run reading the checker's own code: all three mutations exit 1, both identities exit 0. The checkers were correct; the harness was not.

## 6. Gate status for v1.20.2

| gate | status |
|---|---|
| STOP list empty | ✅ (STOP-01 resolved in v1.20.1; inventory found none) |
| 119-block reverse inventory | ✅ complete — **pending your review** |
| INV-S | ✅ built, self-tested |
| INV-P | ✅ built, self-tested, PASS |
| NG-10 destination | ⏳ ruling needed |

Not yet claimed: that the 37 NONE §6 blocks need nothing. They are §6-resident and do not move; INV-1/INV-2 guard them at rewrite time.
