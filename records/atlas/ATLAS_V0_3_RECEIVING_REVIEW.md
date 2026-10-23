# RTG State Atlas v0.3 — receiving review (atlas owner)

**Date:** 23 October 2026. **Reviewer:** Claude (atlas owner). **Object:** branch `chatgpt/atlas-v0.3` at `00d6667bf2d528d96e0cdf4e42b197844da63f5e` (PR #24); candidate `atlas/RTG_STATE_ATLAS.md` SHA-256 `dad844027a8d2c614a90c0a3c1a5736dae9d0a49824b70f788ede7c62a3487c3`; packet `records/atlas/ATLAS_V0_3_REVIEW_PACKET.md` (`9ba86e86…1880`). **Status:** review record; PI decides.

**Verdict: REVISE — three corrections (V1–V3), then ACCEPT.** None is scientific; the new theorem node, the A1–A5 corrections and the diagnostic dispositions are right. The build is reproducible.

## 1. Reproduction

| Item | Result |
|---|---|
| `python3 -I evidence/atlas/build/refresh_v0_3.py` from a full-history checkout of the branch | exit 0; `atlas/RTG_STATE_ATLAS.md` SHA-256 `dad84402…87c3`, byte-identical to the committed candidate |
| generated records (`evidence/atlas/v0.3/*.json`, `*.md`, `records/atlas/*`) | all byte-identical to the committed files (`git status` clean after the run) |
| source freeze | 18 sources at their tags; only RECOG differs from v0.2 (`recog-v0.3.23`, `0d583400…a31a`, commit `4edaa88`) — confirmed |
| attachments sent to the PI | atlas candidate and packet byte-identical to the branch files |

## 2. Content checked

- **RECOG-THM-A1A-PHASE-EXISTENCE-U node (D3.L2).** Scope, series ($\tau H(a)+\tau\sum(Q_m-\tfrac1{a+m})-\sum r_m$, $H(a)=-\psi(a)$), premise chain (LPHASE-ROWA row A, PRIM-CTR, LIFT-ALIGNMENT, RECIPROCAL-AMPLITUDE, PHASE-EXISTENCE-ALT), "R9 and INF-1 not used" and the nonclaim list match RECOG v0.3.23 §6.13b. The NUMGEN-route node PHASE-EXISTENCE-NG keeps its overlap domain; CD-IDENTIFICATION keeps its R9 route. ✓
- **Two FB-13 RIDs** replace the atlas surrogate labels; statements unchanged. RESULT pairings and the two owner splits (tokenisation-consequence / -schema; R-E-retention / -transition) carried without regrading. ✓
- **A1–A5.** H5, H12, RRF.F7, OFN.O11, NUMGEN.N-B, N-D, N-L5, RECOG.R-L1b, R-L5, the L-BACKBONE and INF-1 edges, and *RECOG:relabeling-Sh all now read as the co-owners corrected them (consistent-with, not satisfied; 15/2 an ingredient; candidate source, not owner; H-NG edge as atlas identification; R-L7 retired). ✓
- **Dispositions.** 20 D3.L5 records: 10 retired, 7 reworded, 3 retained, with reasons and hashes. R-L3 and the section-shadow transfer moved to D3.L3 as unadopted tasks, not closed. R-T1 and R-P3 now describe the owner's live-file exception without reopening closed modules. ✓
- **Consumer pins.** `*DYAD:leading-decay` keeps "RECOG v0.3.22 §6.13b" — correct, that is Dyadic's pin, written at the edge per Method §4. ✓
- **DZT 80-digit evaluations** moved from "exact" to "numerical" in `*ATLAS:checked-D2`; the exact p=12 identity stays exact. ✓
- Census, H1–H4, H6–H11, D-WRONG, the 17 unchanged source domains: untouched. ✓

## 3. Corrections requested

**V1 — garbled substitution (D3, `*RECOG:F3-common-driver`, candidate line 809).** The row ends "… | DYAD-ALG-NF6-DEG10 (VF-1) ≡ DYAD-ALG-NF6-DEG10 (DYAD-ALG-NF6-DEG10) | @§6.16f". Two edits in `refresh_v0_3.py` (the `VF-1` → `DYAD-ALG-NF6-DEG10 (VF-1)` citation repair, then the `RECOG.R-L8` → `DYAD-ALG-NF6-DEG10` pointer replacement on the same line) composed into a self-referential equivalence. Intended text: the `~ RECOG.R-L8` pointer field is simply removed (R-L8 is retired), leaving `… | <RECOG-THM-R9-MEMORY | @§6.16f`.

**V2 — stale RRF edge (D3, `RECOG-RESULT-F4-NETWORK-WELLPOSEDNESS`, candidate line 815).** The consumer field still reads ">RRF v0.8.3 §6.3 (RF-1: RRF restates W3 across spaces), RER v0.2 G9". The source snapshot has RRF v0.8.4, whose §6.3 quotes W3 verbatim with the RID and labels inter-space transport a separate `[OPEN]` RRF extension; RECOG v0.3.23 §7.2/§7.3 records "RF-1 fulfilled (a content state, separate from notice state)". Replace with ">RRF v0.8.4 §6.3 (W3 quoted verbatim with RID; inter-space transport a separate RRF OPEN extension; RF-1 fulfilled), RER v0.2 G9". The rest of the atlas already describes RRF v0.8.4 this way (RRF.F2), so the v0.3.23 refresh left one v0.2 edge behind.

**V3 — provenance of the F5 node (D3.L3, `*RECOG:event-carrier-interface OPEN`).** The node is right in substance and in scope (sufficient witness, not a necessary condition; nothing registered in v0.3.23). But its provenance "@RECOG§6.16f–g" is wrong: RECOG v0.3.23 contains no F5 proposal; §6.16f–g hold F3/F4. The proposal and its scope decision come from the owner dispositions and the PI decision of 23 Oct 2026 (`records/recog/ATLAS_ADVISORY_RECOG_v0_3_22_DISPOSITION_RECONCILIATION.md` §5), which are records, not snapshot sources. Write the provenance as "PI decision 23 Oct 2026 (records/recog/…RECONCILIATION §5); not in RECOG v0.3.23" and keep "<RECOG-ALG-CONTINUOUS-CARRIER-NOWRITE" as the owner anchor it builds on. If the Method is read as excluding record-sourced nodes altogether, the alternative is to drop the node and keep the F5 sentence inside the R6 row's "sub-questions" field with the same record citation; either is acceptable to me.

**Optional (wording).** The new theorem node's scope reads "sc: selected T"; RECOG writes "conditional on postulated $T$" and the atlas uses "postulated T" everywhere else (programme ceiling, SG-R7). Suggest "postulated T".

## 4. After the corrections

Regenerate with the script (the edits are assertion-gated, so V1–V3 are script changes), re-run the shared checker and the scoped guards, record the new candidate hash in the packet and the acceptance record, and I will re-read the three sites and the hash. Then: PI acceptance identifying the bytes, merge commit of PR #24, annotated tag `atlas-v0.3`. `atlas-v0.2` governs until then.

---

## 5. Readback of the corrected candidate (23 October 2026, later)

**Object:** `chatgpt/atlas-v0.3` at `d6f3d2d326c553537d0a98bd2fe34e74b0901dc4`; candidate SHA-256 `71310e8c5e1b29979a854ee2ee932efa4765f038bbe0c10299e14f424ad1dc5b` (467,029 bytes).

| Check | Result |
|---|---|
| rebuild with `refresh_v0_3.py` | exit 0; candidate byte-identical to the committed file; generated records unchanged |
| diff against the first candidate `dad84402…87c3` | exactly four atlas lines changed: the new theorem node (scope word), `*RECOG:F3-common-driver`, `RECOG-RESULT-F4-NETWORK-WELLPOSEDNESS`, `*RECOG:event-carrier-interface` |
| V1 | the garbled `≡` field is gone; the row ends `… \| <RECOG-THM-R9-MEMORY \| @§6.16f` ✓ |
| V2 | consumer edge now `>RRF v0.8.4 §6.3 (W3 quoted verbatim with RID at RECOG v0.3.21; inter-space transport is a separate RRF OPEN extension; RF-1 fulfilled as a content state, not a notice receipt), RER v0.2 G9` — keeps RRF's actual pin and separates content state from notice state ✓ |
| V3 | provenance now `PI decision 23 Oct 2026, records/recog/ATLAS_ADVISORY_RECOG_v0_3_22_DISPOSITION_RECONCILIATION.md §5 at snapshot 9453e35…; proposal not in RECOG v0.3.23`; `<RECOG-ALG-CONTINUOUS-CARRIER-NOWRITE` anchor kept ✓ |
| optional | `sc: postulated T` ✓ |
| no regression of the three strings | 0 occurrences of the old text ✓ |
| packet and acceptance record | both name `71310e8c…dc5b`; the acceptance record leaves the PI decision open ✓ |

**Verdict: ACCEPT.** The candidate `71310e8c5e1b29979a854ee2ee932efa4765f038bbe0c10299e14f424ad1dc5b` is ready for the PI's decision. Remaining limitations are those the packet keeps: 7 UNVERIFIED links, 11 DOCUMENTED-UNRESOLVED items, 16 wording warnings, the v0.1 input-equality unknowns, and no certificate replay. None is new in v0.3.
