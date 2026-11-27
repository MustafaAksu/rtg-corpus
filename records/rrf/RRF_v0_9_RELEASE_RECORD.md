# RRF v0.9 — Release Record (publication preparation)

**Date:** 27 November 2026.
**Decision:** ADOPTED by the PI at RRF working representation standard scope. In the RRF co-owner conversation, responding to Claude's final exact-head ACCEPT SCOPED (review 6085047516), the PI stated verbatim: **“v0.9 u benimsiyorum”**. Recorded at [PR #417 comment 7213581950](https://github.com/MustafaAksu/rtg-corpus/pull/417#issuecomment-7213581950). Exact adopted review candidate: `8de7a8cd338f37bce3a73910648eecc9a5628b2c`, SHA-256 `2950dbc0a2fd3468005a9b86190fe4513068019a21444fd8c431124043ba942d`, 121,279 bytes. The earlier explicit approval of the four closure criteria is [comment 7202555052](https://github.com/MustafaAksu/rtg-corpus/pull/417#issuecomment-7202555052). This record prepares publication, not a completed merge or tag. Until the PI authorizes publication and the annotated tag is verified, `rrf-v0.8.4` governs. No adoption of owner science, physical choice, BR-Q2, new profile or OPEN closure.

## 1. Source identities and build stages

| Object | Commit/tag or locator | SHA-256 | Bytes |
|---|---|---|---:|
| Adopted predecessor | rrf-v0.8.4 → d7d661c0b89c6f3d9ceea2e205bf75fccfcfbf8d | 2fb0a0fe9d998be91618cb731e2dee7301952ffdbe374f4889dd5e61c5cbafce | 108615 |
| S2a corrected intermediate (#404) | 98da97c311a917d1539b9c31afaba779bc75a73f | 390f75e447b7d5a9dcb01810d7eb513e9feef3c157f0de2f2f79afb259b39d72 | 131089 |
| S2b exact PI-adopted candidate (#417) | 8de7a8cd338f37bce3a73910648eecc9a5628b2c | 2950dbc0a2fd3468005a9b86190fe4513068019a21444fd8c431124043ba942d | 121279 |
| Publication-ready fixed DSN (not yet published) | dsn/RTG_RRF_REPRESENTATION_REGISTRY.md | 28c9c101c715b402b5ed60eeab8bfa2c7e5e637fef3cd2b00961dfa60553075d | 121216 |
| S2b movement map | evidence/rrf/v0.9/s2b_movement_map.json at 8de7a8cd338f37bce3a73910648eecc9a5628b2c | 22234d2bc010ee74fe3d591e501d60183b9348f68567893323aaf4ed86c2ce34 | 73831 |
| RRF-specific adapter | evidence/rrf/scripts/check_rrf_s2b.py at 8de7a8cd338f37bce3a73910648eecc9a5628b2c | 70f828bd01e8649ced0c8248ab9137e45d0adb494e571a6220b24f487e87ab5b | 7114 |
| Publication transform | evidence/rrf/v0.9/publication_transform.json | 29807cae4af52ab47851d3d61637fc6da6ef052072ed19fdfa584657169bbb61 | 13761 |
| Publication checker | evidence/rrf/scripts/publish_rrf_v0_9.py | e7de37baea609767826677e85a3749ee137f957a66de4214ea0fa79d1de5acba | 3472 |

Predecessor adoption record: `records/rrf/RTG_RRF_REPRESENTATION_REGISTRY_v0_8_4_ADOPTION_RECORD.md` (recovered and verified in S0). Governing Methodology `methodology-v1.4`, §§13.1,13.5–13.9, CONVENTIONS §§1–9. Main checkpoint `c167f80701eb706bca520b4aafcdab1b546a40a9` (pre-publication). No source-owner file is amended.

- S0: scoped custody acceptance at #397; #394/#397/#396/#399 merged. 17 placements and 37 digest links; regenerated diffs are not originals; missing original v0.8 QA JSON and PRR review ZIP remain declared.
- S1: 28 row matrix, ten open notices/question; reviewer C1–C4 resolved at `2c087763`, review 6074506269; #400/#401 merged. Source identities/reading extent and actual owner pins in `records/rrf/RRF_S1_SOURCE_INTERFACE_MATRIX_20261126.md` (accepted correction head `2c087763e94ac23768c8b778aecc3bb8a57e508d`). This is targeted owner-source/interface review; no repeated scientific certificate campaign.
- S2a: assertion-gated build, 38 operations, independently accepted at `98da97c311a917d1539b9c31afaba779bc75a73f` (review 6076472389; `records/rrf/RRF_S2A_REVIEWER_VERDICT_PR404_20261126.md` §5; #406 merged). Native checks reviewer-reported PASS: 131,089 bytes, four negatives, 89 tokens / zero loss apart from explicit predecessor filename substitution; original P2-B archive identity, not replay. Build plan `evidence/rrf/v0.9/s2a_build_plan.json` and script `evidence/rrf/scripts/build_rrf_s2a.py` at frozen commit; build record `records/rrf/RRF_V0_9_S2A_BUILD_REVIEW.md`.
- S2b: review 6079644693 at `917f76ef` ACCEPT WITH CHANGES; C1 restored predecessor adoption-record pointer, C2 cites PI approval. Final review 6085047516 at `8de7a8cd338f37bce3a73910648eecc9a5628b2c` ACCEPT SCOPED; independent record `records/rrf/RRF_S2B_REVIEWER_VERDICT_PR417_20261126.md` at #418 head `6b84479ee3068806cb09bcf40138b606145650c5` §6 (unmerged at preparation), blob `d6c054fd66da3c5d2674fe5dac51cded8d4b6d33`. Reviewer native adapter 4/4 negatives, 691→654 split lines / 76 operations, exact candidate identity and ancestry PASS. Independent reviewer checker blob `6441801c305937c82c138be8ab4a63f33fc5c7d4`: 0 lost tokens outside archive, 46/46 import lines indexed, 26/26 owner-grade readouts, wrong-grade control; all 10 archive spans and editorial/navigation classes read. Trial merge and pipes 197/20 reviewer-reported, at pre-publication head, not a test of the new publication commit.
- Publication preparation: 20 explicitly enumerated status-only line substitutions (line numbers 5, 8, 9, 74, 204, 293, 331, 338, 357, 475, 477, 479, 486, 500, 508, 573, 575, 577, 647, 653). Header/date/supersession, six local identities, OPEN descriptive aliases/approved-criteria status, live identifier index and release-state navigation, Appendix A and footer. The PI adopts the entire reviewed working standard, including its local-ID routing; registration metadata makes that status current, not a new owner RID or scientific predicate. Four OPEN rows byte-identical, all ACTIVE; B→E1→E2 unchanged. No new proof, scope, model, numerical constant, transport, source pin or BR-Q2 conclusion. Connector exact forward/reverse reproduction and three negative controls executed PASS (coefficient with rehash, missing edit, wrong anchor). Native publication check pending independent review. Reviewed draft stays immutable at `8de7a8cd338f37bce3a73910648eecc9a5628b2c`; the S2b adapter is replayed on that checkout, not on the publication-ready metadata variant.

## 2. Scientific and interface scope

Six RRF-local identifiers (passive transport, S-decomposition, finite swap transport, typed covariance, odd-root equivalence, event-transport convention) and four descriptive OPEN IDs are registered at RRF working-standard scope on publication; no owner theorem re-owned. Existing four dyad profiles + one provisional network profile, four transport keys/composite and guards remain unchanged. Exact inherited owner grades, conditions, charts and clocks in §§2–6 and 60 use-index entries in §7.2. Historical evidence pins are not bulk repins. Standard C and OFN smooth class-C mathematical candidate family corrected; OFN SESSION lock/causal/modulus evidence not promoted; DYAD finite/formal/smooth/analytic distinction; R9 sharper rows distinct; NUMGEN M4 HOLD and Census-1 status; TRIAD same-vector OPEN convention; RER adopted NONCANONICAL scope; UVM reference-only. No physical geometry or gauge selected. OPEN20 analytic B-an/B-6 remain open. BR-Q2 #410 is SESSION; #414 independent review separate and not adopted here. PRR v0.3 status and GIIL receiving dispositions remain separate; no scientific source status inferred from custody. LIT dependencies: none.

## 3. Mandatory G1 and checker limitations

The S2a baseline is exactly `98da97c311a917d1539b9c31afaba779bc75a73f`, SHA-256 `390f75e447b7d5a9dcb01810d7eb513e9feef3c157f0de2f2f79afb259b39d72` (131,089 bytes). Complete archive spans M003/M016 are retrievable only in that commit, not verbatim in the adopted predecessor tag (the M016 embedded old receipt body also appears there). The other eight archive spans are predecessor-tag retrievable according to the independent review. Do not squash or rebase #417: integrate by **merge commit only** and verify `git merge-base --is-ancestor 98da97c311a917d1539b9c31afaba779bc75a73f main` after integration and before tagging. Also preserve the exact adopted S2b candidate commit as an ancestor.

The RRF-specific adapter is accepted only for this edition (review 6079644693 and final readback 6085047516); shared tooling was not changed. Its limitations:
1. Archive and editorial classifications are not mechanically established. The independent archive/editorial readings carry those semantic judgments; a dishonest reclassification with a rehashed candidate could pass mechanically.
2. Navigation text is not constrained beyond declared bytes. Independent review of the navigation and owner-grade readouts carries scope/accuracy; the checker does not certify unrestricted prose equivalence.
3. Archive commit reachability must be checked explicitly. The adapter enforces the frozen reference and ancestry on review HEAD; verify again on actual main after authorized merge. The publication checker checks both frozen and reviewed candidate ancestry.

Mechanical PASS is not scientific validation or adoption. No owner certificate rerun or new physics certification. EV-SRC-READ/EV-BYTES/EV-HASH on actual identities and scoped readouts, EV-RUN/EV-INDEP for reviewer-reported native checks on the reviewed heads, EV-NOT-RERUN for unchanged scientific campaigns.

## 4. Size report and publication readback

Informational size report `evidence/rrf/v0.9/publication_size_report.json` (connector, declared nonstandard RRF section map). Predecessor 108,615 bytes; S2a 131,089; S2b 121,279; publication-ready 121216; growth against predecessor 12601 bytes (11.6%); S2b reduction -7.48%. Lexical RID counts are not registration counts; §1 equation syntax profile exception, orientation core N/A. Native lint including near-duplicates pending at release review; advisory only.

At the publication branch head:
```bash
python -I evidence/rrf/scripts/publish_rrf_v0_9.py
tmp=$(mktemp -d)
git show rrf-v0.8.4:dsn/RTG_RRF_REPRESENTATION_REGISTRY.md > "$tmp/base.md"
python tools/dsn_lint.py dsn/RTG_RRF_REPRESENTATION_REGISTRY.md --prev "$tmp/base.md"
python tools/pipes_index.py --check
git merge-base --is-ancestor 98da97c311a917d1539b9c31afaba779bc75a73f HEAD
git merge-base --is-ancestor 8de7a8cd338f37bce3a73910648eecc9a5628b2c HEAD
```
For exact S2a/S2b replay use the respective immutable commit in a separate checkout/worktree (the status transform is intentionally not the DRAFT input to the compaction checker). Re-run only changed metadata/record/queue checks; no need to repeat unchanged scientific campaigns. Before publication verify current main, exact reviewer head, release-readback verdict, mergeability, pipe indexes and final hashes.

## 5. Outbound and incoming interface state

The following notice files are staged on the publication branch, tagged in their front matter only by **existing** predecessor and recipient tags; their bodies name the exact PI-adopted candidate and publication-ready hash, and condition successor use on the verified `rrf-v0.9` tag. This avoids pretending a not-yet-created tag exists or failing the pipe validator. After publication, confirm the successor tag in the notices in a separate scoped post-tag follow-up (append actual tag to tag list and add verified receipt pointer; do not overwrite the original record).
- PROG: `pipes/PROG/20261127-RRF-v0-9-release-interface-notice.md` — IF30/31/33 scoped synchronization of actual current uses/retained proof pins.
- RER: `pipes/RER/20261127-RRF-v0-9-closure-interface-notice.md` — IF33/G7–G10/CND01 source/use boundary; retain historical pins, noncanonical scope and exclusions.

Prepared/filed on review branch only; sent, received, statement accepted, adopted use: not asserted. No sender-side state changes on existing items. Native pipe validator at release head pending; connector regeneration of existing affected indexes matched prior bytes before adding entries. No automatic receiving adoption. S1's nine notice dispositions are represented by the adopted scope of the new edition; actual queue closeout is a separate post-tag receiving action, referencing the accepted S1 matrix §3 and this record. The tenth item, BR-Q2, stays open; no closure or reply on the basis of this release. GEN/RER GIIL decisions and unnumbered owner-RID follow-up are separate. No LIT use.

## 6. Publication gate and BASELINE

PI adoption is recorded; **independent release readback and PI publication/merge/tag/BASELINE authorization remain pending**. Do not publish #404 separately. #417 incorporates the frozen S2a ancestry. #418 is an independent reviewer record, not itself a release; integrate in reviewed order #417 then #418 by merge commits (actual clean merge and ancestry must be verified on current main). Preserve distinct Claude lane. Do not merge #414 as part of v0.9. Tag `rrf-v0.9` must be annotated at the actual authorized merge commit; include the final DSN SHA-256 `28c9c101c715b402b5ed60eeab8bfa2c7e5e637fef3cd2b00961dfa60553075d` in the tag message. Verify tag target, tagged DSN hash, ancestry and actual manifest before claiming governing publication. No tag or main change performed in preparation.

BASELINE RRF row prepared for the actual authorized publication transaction (other rows unchanged):
```text
| RRF | `RTG_RRF_REPRESENTATION_REGISTRY.md` | v0.9 | `28c9c101c715b402b5ed60eeab8bfa2c7e5e637fef3cd2b00961dfa60553075d` | OWNER: release record `records/rrf/RRF_v0_9_RELEASE_RECORD.md`; PI adoption 27 Nov 2026 (PR #417 comment 7213581950); independent S2b readback 6085047516; predecessor v0.8.4 `2fb0a0fe…afce` (`rrf-v0.8.4`) | `rrf-v0.9` |
```
Do not install this row as a verified current tag before tag creation/verification. Actual final merge/tag IDs, final native test outputs and post-tag source readback belong in the dated post-tag record, not retroactive changes to the frozen release record.
