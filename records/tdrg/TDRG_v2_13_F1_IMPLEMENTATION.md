# TDR-G v2.13 — Atlas F1 implementation checkpoint

**Date:** 16 November 2026. **Author:** ChatGPT TDR-G co-owner.
**Status:** SOURCE INPUTS UPDATED; TWO-STAGE REBUILD NOT EXECUTED. Not review-ready, not adopted, and not a new candidate certificate.
**Authorization:** the PI instructed “F1 hemen uygulansın” in response to Atlas row-check PR #277. This authorizes the AZ v0.9 pin and consumer-interface correction, not adoption of AZ numerical results or publication of TDR-G v2.13.
**Working branch / PR:** `claude/tdrg-v2-13`, PR #265. Pre-F1 head: `fba3ea137c4771946fc2bd746fe0f4a7d140638b`. Source patch through `5b13de273b9f883aaa8dcf4f0eceba0fe03abb6d`.

## 1. Sources actually checked

- `CONVENTIONS.md` on main, including the two-stage release and evidence-state rules.
- PR #265 state and its pre-F1 candidate/release identity; Atlas row-check PR #277 and its F1–F4 scope.
- Annotated `az-v0.9` reference and `pipes/TDRG/20261114-AZ-v0-9-adopted.md` (open).
- AZ v0.9 §8 IMP-B: consumer use at `tdrg-v2.12.15`, corrected LEM-SPECCONS generalization, added event-inventory/token-census and parent–child-phase rows.
- AZ numerical ownership boundary in its v0.9 notice: `AZ-NUM-TOKRES-S1` is an AZ-owned diagnostic computed on the pinned TDR-G engine; neither a TDR-G result nor a demonstrated growth mechanism. No new TDR-G scientific import is made by the consumer-row correction.
- Existing Stage-1 builder and checker, their pinned predecessor `tdrg-v2.12.15`, source blocks and the release-record filler.

The earlier algebraic-line equality is supported by the Atlas check and AZ notice. The updated C6 checks equality at az-v0.6, az-v0.7, az-v0.8 and az-v0.9 when executed; that full gate has NOT been executed in this session.

## 2. Applied changes

| File | Applied correction |
|---|---|
| `evidence/tdrg/v2.13/stage1/blocks/consumers.md` | AZ v0.9 row, TDR-G v2.12.15 consumer pin, the two added token-law rows, and explicit AZ-owned diagnostic/non-adoption scope |
| `evidence/tdrg/v2.13/stage1/blocks/pins.md` | Current AZ edition v0.9 |
| `evidence/tdrg/v2.13/stage1/build_tdrg_v2_13_stage1.py` | E13 emits `az-v0.9`; E25 describes the v0.9 consumer-source update; original exact-once anchors and predecessor identity preserved |
| `evidence/tdrg/v2.13/stage1/check_tdrg_v2_13_stage1.py` | C6 checks four AZ editions, current consumer pin/token rows and the diagnostic ownership guard; K1 regresses v0.9 to v0.8. C3 permits the newly mentioned foreign AZ diagnostic identifier; C4 accounts for its source-status tag, not a TDR-G result grade. C7 and the other existing gates retain their prior behavior. |

Source diff was checked against the pre-F1 head: only these four files changed. No canonical DSN, engine, pipe item, BASELINE row, tag or adopted release record changed.

## 3. Verification actually performed and not performed

**Performed:** source and diff inspection; eight narrow local checks of the new consumer-scope predicate (valid v0.9 row accepted; stale AZ pin, stale TDR-G consumer pin, removed AZ ownership, removed mechanism guard, local diagnostic RID declaration and duplicate row rejected; exactly one AZ source-grade tag counted). These are predicate-fixture checks, not the full repository checker or a scientific campaign.

**Not performed:** Stage-1 regeneration and full C0–C10/K1–K10 execution; new intermediate commit; Stage-2 generation and movement-map/negative-control replay; new candidate hash; release-record regeneration. The execution sandbox has Git but cannot resolve github.com, and the connector reads/writes files without providing an executable repository checkout. No source bytes, tags, hashes or PASS logs have been reconstructed or invented to conceal this limitation.

Consequently, the stored candidate `c89eb81b8456b3d77e5608d2e288378d581477d36bb0acc80ee1c8b21c3a0a14`, intermediate `472e26e99a1da054447b57c4755adf50cacfc9dbe56ea7b8d5eaa2beb17856ff`, movement map and stored PASS logs are **pre-F1 outputs**. They remain evidence for the earlier pinned build only and do not certify the changed inputs. PR #265 explicitly states this pending-build status.

## 4. Exact remaining continuation

1. **Finish the bounded source propagation.** In `stage2/blocks/appendix_a.md`, change only the v2.13 current AZ pin/readout to v0.9 and state the unchanged algebraic statement across v0.6–v0.9; preserve historical entries for earlier TDR-G editions. Add `az-v0.9` to the Stage-2 builder's known-tag list. In `release_record_template.md`, update the current AZ pin, consumer readout and post-tag notice to v0.9; replace the obsolete empty-inbox assertion with the actual open AZ v0.9 item and its explicit pending disposition. Preserve the completed R1/R2 review history and distinguish the new foreign diagnostic reference from adoption.
2. **Rebuild Stage 1 and Stage 2 using the existing release process.** Run Stage 1 from the real `tdrg-v2.12.15` tag, regenerate `stage1/edit_log.json`, then gates and negative controls. Record a new intermediate commit. Update Stage-2 `BASE_COMMIT`/`BASE_SHA` and the negative-control source identity to that actual commit/hash; do not reuse `fd96f8a`/`472e26e9` for changed bytes. Rebuild the candidate/map and rerun the unchanged compaction checker and Stage-2 controls. Preserve the intermediate through reachable Git history. No old scientific campaign is needed.
3. **Regenerate and re-read the release record.** The filler currently hardcodes the pre-F1 intermediate size and assumes only one newly mentioned foreign RID. Update it to the measured intermediate size and the actual reference inventory: new TDR-G RID declarations remain zero; the additional `AZ-NUM-TOKRES-S1` is AZ's existing RID and its `[NUM diagnostic]` is a source grade. Keep raw lint output and per-new-TDR-G-RID growth N/A. Fill real hashes/output records only after successful execution, then request a bounded readback of E13/E25/E26, C6/K1, the v2.13 history entry and the new candidate identity.

**F2:** No inbox state was changed here. Receipt/disposition and adopted use remain distinct; the AZ notice is not automatically closed by this patch.
**F3:** BASELINE remains untouched until the authorized publication step, which must preserve current main's AZ v0.9 row.
**F4:** PR #263 is not closed or merged by this action.

**PI_PENDING:** no further decision is required to apply F1; scientific adoption/publication of the regenerated candidate still requires the PI's separate decision. The next eligible action is the above source completion plus two-stage rebuild in a real repository checkout. No background execution is underway.
