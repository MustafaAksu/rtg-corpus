# RTG State Atlas v0.2 — change-focused review packet

**Date:** 23 October 2026. **From:** Claude (atlas owner). **To:** reviewer (ChatGPT); PI (Mustafa) for acceptance.
**Branch:** `claude/atlas-v0.2`. **Base:** atlas v0.1 at `main` `44b55d6` (atlas sha256 `88353763…8cc6`).
**Plan and plan review:** `records/atlas/ATLAS_REFRESH_PLAN.md`; `records/atlas/ATLAS_REFRESH_PLAN_REVIEW.md` (ACCEPT WITH SCOPED EDITS, ARP-01–05).

The atlas is derived and noncanonical. Nothing in this packet adopts owner science; certificates were not rerun.

## 1. Identities at packet time

| object | path | SHA-256 |
|---|---|---|
| Atlas v0.2 | `atlas/RTG_STATE_ATLAS.md` | `8a5b51d2356fbb460d90d5fe37c5f13aa72b9035759ca60934980f7368bbf167` |
| Method v0.2 | `atlas/RTG_STATE_ATLAS_METHOD.md` | `afa4127f0f12b30da689ef94a5d2eae905df82c168dc342fb646765c12f29d7f` |
| Source manifest | `evidence/atlas/source_manifest_v0_2.json` | `35013c11eea7b6854287e0ab69db04b81ccbc15de63b23850fcf0eacc75e5a98` |
| Checker | `tools/atlas_check.py` | `4377a389f34871bd15d3b827fcac6272dcead5018557a21478b34ed4ab471d1d` |

If review edits change any of these, the acceptance record takes the final values.

## 2. What to review (in this order)

1. **Method v0.2** — `git diff 44b55d6 -- atlas/RTG_STATE_ATLAS_METHOD.md`.
2. **Source table and L0** — the SOURCES table and `## L0 KEY` / `### L0.M`.
3. **DYAD delta** — `## D2` (L1–L4) and the DYAD edges elsewhere (§5 below).
4. **RER delta** — the RER nodes in `## D4a` and the RER queue line in `D4a.L3` (§6 below).
5. **Changed cross-domain edges** — §7 below.
6. **L5 dispositions** — `records/atlas/ATLAS_V0_2_L5_DISPOSITIONS.md` (197 rows).
7. **Check report** — `evidence/atlas/atlas_check_report_v0_2.md` and `evidence/atlas/atlas_check_selftest_v0_2.txt`.
8. **Acceptance record draft** — `records/atlas/RTG_STATE_ATLAS_v0.2_RELEASE_RECORD.md`.

Unchanged-source content outside these areas was carried forward and is not in scope, except where a disposition row says otherwise.

## 3. Method v0.1 → v0.2

| change | where | from |
|---|---|---|
| current scientific state only; evidence limits, rejected claims and source class/scoped acceptance stay; chronology, review and notice handling go to `records/atlas/` | §4 rules 1–3 | plan §1, ARP-01 |
| frozen source manifest; "unchanged" = equal bytes; unknown previous hash recorded as unverified; no switching inputs mid-build | §3 | ARP-02 |
| consumer pin kept separate from owner node; edges never deleted mechanically | §2, §4 rule 10 | ARP-03 |
| D-GRADE (H⇒P is a valid THM), D-PIN (age alone is not a defect), D-PROOF (a/b/c) | §6 | ARP-04 |
| impact-based refresh replaces "full rebuild on method change"; L5 dispositions recorded | §7 | ARP-04, review §6 |
| typed identifiers; typed coverage; owner-resolved links; phantoms reported separately; unchecked ≠ PASS | §4 rule 11, §7 | ARP-05 |
| PASS lists replaced by `atlas-checked:` content | §6 last paragraph | plan §3 step 6 |
| annotated tag `atlas-v<version>` plus acceptance record; adopts no owner science | §7 | plan Q3 |
| advisories never mentioned in the atlas; L5 keys stable, never reused | §5, §7 | plan §3 step 1 |

## 4. Source table and L0

- Inputs: 18 sources at their tags (manifest). Byte equality with the v0.1 extraction input: **CHANGED** for METH (v1.3→v1.4), DYAD (v6.4.19→v6.4.22), RER (DRAFT r4.6→v0.2 ADOPTED); **EQUAL** for NUMGEN and RECOG (hash retained in v0.1 context); **UNVERIFIED** for the other 13 (no v0.1 input hash retained; edition labels match). For the unverified sources only edges and diagnostics touching changed inputs were re-checked (Method v0.2 §7).
- Source table: tag and class columns; RER row states its adopted scope (18 records; RER-ER2B-T6D and RER-ER2B-CARRIER BLOCKED_SOURCE_UNVERIFIED).
- L0: identifier types; D-PROOF states; namespace registry (METH v1.4 §4.2); EV-* evidence keys (§12.2); governing-edition rule (§13.9); live-file rule (§1.1, §13.7); D-PIN semantics.

## 5. DYAD delta (v6.4.19 → v6.4.22; D2 and DYAD edges)

42 operations in D2 (`evidence/atlas/build/d2.py`). Main content:
- **New owner RIDs as nodes:** DYAD-DEF-CRITICAL-CURVE, DYAD-ALG-ISP-MAPS, DYAD-ALG-QC-CRITICAL-AMPLITUDE, DYAD-ALG-KP-FRAME-SCALE, DYAD-ALG-SIXSTEP-CUBIC-JET, DYAD-ALG-P5-RADIAL, DYAD-ALG-RAW-ANGULAR-MEAN, DYAD-ALG-ONE-BLOCK-BURST, DYAD-ALG-Q3-DEG2-CANCEL, DYAD-ALG-B5-ALLP-NONVANISHING, DYAD-THM-SMOOTH-EQUIVARIANT-CHART.
- **Restated nodes:** fixed-point scope (lifted chart; winding fixed points of the wrapped cylinder); RAW-CUBIC statement (p≥3); p6 linear order and homological resonance as two separate ALG items (the conflation is withdrawn); classification by p as DEF; cubic rate across p (import of RECOG-ALG-NU3-CLOSED-FORM, frame named); leading decay (import of RECOG-THM-A1A-RECIPROCAL-AMPLITUDE) and the backbone ansatz as a historical DEF; LIEGAUGE h₄ exact in ℚ(i√3) with coefficients; bridge lemma frame-named; P2B provenance replay status; L-PHASE offer with import deferred by NUMGEN.
- **atlas-checked:** h₄ coefficients recomputed exactly with sympy (equal to the owner's 120-digit values); RAW-CUBIC formula numerically for p=3..24; true sup|P₅|/Q^{5/2}=1.63878.
- **Frontier and constraints:** OPEN 9 remainder, OPEN 20 (B-an, B-6), L-PHASE row B, fitted-backbone identification; OPEN RIDs in L3; guards SG-14/16/17/18 and exports.
- **Coverage:** every live non-artifact DYAD RID declared by `[RID: …]` (73) maps to an atlas node or edge outside L5 (checker `coverage`). Artifact RIDs are cited in `cert` fields and link-checked.

## 6. RER delta (DRAFT r4.6 → v0.2 ADOPTED)

- Source line (D4a) and source table: adopted scope, the two blocked records, no owner re-adoption.
- RER-TRIAD-FORMAL-AGE: grade THM → **ALG·FORMAL_ONLY** (source-review grade).
- RER-TRIAD-FORMAL-INVOLUTION, RER-TRIAD-BIRTH-GRAPH-INVOLUTION: independent receiving review ACCEPT SCOPED ((ii)(b) not fully replayed; (d) conditional); still no TRIAD RID, not owner-adopted.
- RER-TRIAD-AGE-CURVATURE: receiving review ACCEPT SCOPED (w₁₃ identity independently confirmed).
- RER-F3-N7N8: the graded claim is the formal E7/E8 leading orders only; Stage1/Stage2 data are evidence status; K=6 pilot insufficient for regional coverage.
- RER-E-CONJ / RER-GEN-K3-MODAL: E-conjugacy transport step independently re-proved (ACCEPT SCOPED [ALG]); owner certificates not rerun.
- RER-DYAD-FORMAL-INVOLUTION: imports DYAD-THM-SMOOTH-EMBEDDING (pin v6.4.18, C^∞ germ scope); OPEN B-an, B-6; no transfer to triad, pole exchange or G2 carrier map.
- RER-ER2B-CARRIER: new node (BLOCKED_SOURCE_UNVERIFIED); RER-ER2B-T6D: blocked status stated.
- RER-RRF-CND01 and guards RER-G8–G10: RRF v0.8.4 is the current reference (12 lines ACCEPT SCOPED; v0.8 pins historical, v0.8 original bytes not found); RER-G9 W3 in the owner's same-space wording (different-space comparison is a separate OPEN RRF proposal).
- RER queue (D4a.L3) rewritten from RER §8 open items only.
- **Coverage:** all 40 RER local keys (20 records, RER-G7–G10, 16 v0.1 machine entries) map to atlas nodes outside L5.

## 7. Changed cross-domain edges (outside D2 and the RER nodes)

| site | change |
|---|---|
| CROSS-DOMAIN INDEX | SMOOTH-EMBEDDING line adds SMOOTH-EQUIVARIANT-CHART and its consumers; new frame-scale line (DYAD-ALG-KP-FRAME-SCALE) |
| D1 `*OFN:class-C-realization` | OFN import pin (DYAD OPEN 20, IMP-O10-04) kept; owner state (C^∞ existence, equivariant chart; analytic B-6 open) shown beside it — consumer pin not repinned (Method §4 rule 10) |
| D1 owners line | Methodology v1.4 semantics |
| D4a `*GEN:transported-instances` | C2: GEN does not assert existence of Φ; supplied in C^∞ by DYAD-THM-SMOOTH-EQUIVARIANT-CHART |
| D4a source line, PROG.G2 | RER v0.2 adopted (no draft revision label) |
| D3.L3, D4a.L3 | "governance" lines deleted (process state; residue in RECOG.R-P2, R-L4 and D4a F13) |
| D5.L3 TDR-0 | wording only |
| all domains L2 | `*ATLAS:checked-Dk` evidence record (former PASS lists) |

## 8. L5

197 dispositions: retained 107, reworded 66, deleted 16, moved 7 (PASS blocks), new 1 (F29). Main grounds:
- **DYAD changes:** X3, X5, X7, F21, R-L9, R-C3, DZT.Q2 deleted; H1/H3/H12, O1, X1, X4, X11, DZT.Q1, R-L5, R-L7, RRF.F7, N-D reworded.
- **RER changes:** F2, F4, F5, F8, F13, F18, F27 reworded; F29 new.
- **D-PIN v0.2:** age-only pin items deleted (OFN.O2, DZT.Q3, AZ.A3 part, GEN.D8, R-P1) or reduced to the demonstrated mismatch (RRF.F2, PROG.G1, NUMGEN.N-F, R-P2, R-P3, F8, OPENM.U1, TDRG.G3, AZ.A3, PREL.P1).
- **D-PROOF v0.2:** states named (OFN.O10, N-D1, R-D1, F14, GEN.D3); OPENM.U8 reclassified as D-STALE.
- **D-GRADE v0.2:** DYAD.X6 and R-L4 reclassified as custody links; R-L7 states that an H⇒P THM is valid and only the link is missing.
- **Process wording** ("Advisory", "merge-time", "resolved", notice/receipt state) removed; R-T3 deleted as notice handling.
- HEADLINE recomputed; H-numbers are display order only.

## 9. Check report (summary)

| check | PASS | FAIL | UNVERIFIED | other |
|---|---|---|---|---|
| sources | 72 | 0 | 0 | — |
| coverage | 128 | 0 | 0 | — |
| qualifiers | 3 | 0 | 0 | — |
| links | 407 | 0 | 15 | — |
| artifacts | 94 | 0 | 3 | — |
| wording | — | — | — | WARN 28 |

- The 15 unverified links are strings present in the owner file but not in a declaration form: the DZT/AZ strings classified by DYAD App F, DYAD-CAND-PHISTAR (never a Dyadic identifier), three AZ OPEN labels, NUMGEN-ART-ROTNUM-OBSTRUCTION and TRIAD-ALG-T6M. All are either L5 subjects (H3, DZT.Q1, N-D) or owner labels to inspect; none is counted as resolved.
- The 3 unverified artifacts are scripts named in a source other than the line owner (`cm.py`, `fit.py` on a GEN line; `prove_core_equiv.py` on a line without a namespace owner).
- The 28 wording warnings were read; the remaining ones are owner statuses or owner-quoted text ("pending", "RESOLVED", "was THM" in a COR record), kept by rule 4.12.
- Negative controls (`--self-test`): omitted claim with RID left in L5; wrong owner; lost conditional qualifier; invalid artifact RID; script named nowhere; fabricated RID only in L5 (reported DOCUMENTED-UNRESOLVED, not PASS) and in a node (FAIL); source-table mismatch — **all detected**.
- Checker limits: a "declaration" is a `[RID: …]` tag, a heading, a first table cell, an `RID:` field or a line-initial RID; owners using other forms show as UNVERIFIED, not PASS. The qualifier check covers DYAD declarations carrying `[assuming: …]` only. The checker does not judge content fidelity.

## 10. Known limitations and deferred work

1. `*ATLAS:checked-Dk` records hold the former PASS facts as one evidence record per domain; distribution to the individual nodes is deferred to the wording-compression pass (plan Q1: compression later).
2. For the 13 sources with UNVERIFIED byte equality, unchanged-looking text was carried forward without re-reading the owner; only items touching changed inputs or changed semantics were re-checked.
3. Size: 464k characters (v0.1: 452k); compression deferred.
4. DYAD source recovery (143 missing sources, `records/dyad/DYAD_SOURCE_RECOVERY_LIST.md`) is outside this refresh.

## 11. Questions for the reviewer

1. Is the PASS-block placement (one `*ATLAS:checked-Dk` evidence record per domain, distribution deferred) acceptable for v0.2?
2. Are the D-PIN deletions (age-only pin inventories) acceptable, given the inventories stay recoverable from v0.1 at `44b55d6`?
3. Should UNVERIFIED declaration forms (§9) be resolved now by per-owner declaration grammars in the checker, or left as UNVERIFIED for v0.2?
