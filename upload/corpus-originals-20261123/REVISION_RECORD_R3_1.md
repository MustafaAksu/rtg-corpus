# RER r3 → r3.1 evidence-only change record

**Date:** 14 October 2026. **State:** noncanonical review candidate; no owner/RRF/physical adoption.

## Basis

The contributor accepted four exact-r3 records: C09, REGULAR-3FOLD, ER2B-T6D and RER-F3-N7N8. Exact reviewed r3 SHA-256: `6095e1d764792ca85f79b21ee695837be582a75e31efe41cdcdae38bb40033ff`.

The latest ZIP supplies the previously missing current driver, coarse configuration and two worker files, plus completed K6 pilot rows and the stopped K8 row. Their source hashes are now pinned as additional entries; earlier inspection snapshots are not overwritten.

## Changed

1. Four r3 scoped acceptances recorded with their exact reviewed hash. No RRF-crosswalk or whole-registry acceptance inferred.
2. Stage2 replay access gate changed from missing/reported to received and rerun: original 41/41 expectations, exit 0, empty stderr. The suite includes one fresh coarse K=4 retry job, not a pilot or sweep.
3. K6 pilot changed from 7/8 reported-without-rows to 8/8 received and contract-checked. Coverage is 4/904 per N, not the full governing plan. K8 remains 1/8, stopped and config-distinct.
4. The current work queue no longer asks for the four delivered replay inputs. It requests independent TM lemma review; any governing-region execution requires a separate decision.
5. The replay archive's stale checksum self-entry is explicitly recorded. All 19 other member hashes match. The original archive and checksum file are retained.

## Unchanged

All 16 original records; all 16 supplementary IDs; all scientific grade/exactness/formula/domain/clock/remainder fields; the 64 earlier source objects; RRF v0.8 and its section crosswalk; existing v0.1/r1/r2/r3 history; physical target `NO_TARGET_VECTOR_LAW_SELECTED`; null global constants; and no controlled-approximate-closure acceptance.

The source coefficient table, engine, contract, driver and coverage scripts were not altered. The 104 worker enclosures and nine pilot rows were not regenerated in this review. Only the regression's coarse retry job was executed. No claim of independent proof of the TM lemmas is made.

## Traceability

- `diffs/r3_to_r3_1.diff`: Markdown point-of-use changes.
- `diffs/REGISTRY_FIELD_CHANGES_R3_1.json`: field-level JSON changes.
- `evidence/ASSERTED_EDITS_R3_1.json`: asserted text substitutions.
- `data/R3_CONTRIBUTOR_ACCEPTANCE.json`: scoped review receipt, separate from adoption.
- `evidence/STAGE2_REPLAY/records/`: source identity, replay and coverage receipts.
- `evidence/VALIDATION_R3_1.json`: integration checks only, not independent mathematics.

## Next gate

Review the bounded evidence synchronization; RRF reviews the actual RER interface separately. The independent Taylor-model lemma review and full governing-region constants remain OPEN. There is no need to restart K8 merely to record this completed replay.
