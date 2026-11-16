# TDR-G v2.13 — independent co-owner review of Stage 1 and Stage 2

**Current review date:** 16 November 2026. **Reviewer:** ChatGPT, independent TDR-G co-owner.
**Current verdict:** **PASS — bounded AZ v0.10 source/interface readback.** No candidate-DSN correction is requested. One nonblocking release-record enumeration omission is recorded in §5 for the ordinary metadata update; it requires no DSN rebuild.
**Reviewed PR:** #265, head `7ca1b3ebf4294279c6a3d5525f481dae9132beff`.
**Candidate identity:** owner-recorded SHA-256 `6a4b94d5ec6946cad177889d453044a69eb4aa451763a2e81148b2e11739de88`; GitHub file blob `3af27eca21a060064d13e2d8bb1a5236f287043d`, identical at the generated-candidate commit `7f02c06` and the reviewed head.
**Authority:** this is a reviewer verdict, not scientific adoption, an Atlas verdict, or authorization to merge/tag. The candidate is DRAFT; its adopted predecessor is `tdrg-v2.12.15`. Repository-root `CONVENTIONS.md` and `methodology-v1.4` govern the workflow.

## 1. Immutable review history

This fixed-path working review is current-state-oriented. Earlier reviews and their full evidence remain at these immutable revisions of this same path. No previous calculation is withdrawn or retroactively extended to different candidate bytes.

| Round | Review-record commit | Exact scope |
|---|---|---|
| Original two-stage review, 14 Nov | `da61a6c8bc192f299efac102a0aa2927a579f8ea` | Candidate `1691a136…ee18`: Stage 1 CONDITIONAL PASS (R1/R2), Stage 2 mechanical PASS |
| Round-2 readback, 14 Nov | `c992551392e05595b98c9175f6c0b34576b55c96` | Candidate `c89eb81b…0a14`: R1/R2 CLOSED; independent complete movement-map replay for those bytes |
| F1 implementation checkpoint, 16 Nov | `ddadd8ad07779274cdd2ea5f753f573238d14f60`, `records/tdrg/TDRG_v2_13_F1_IMPLEMENTATION.md` | Source-input patch only; no rebuild claimed at that checkpoint |
| AZ v0.9 F1 readback, 16 Nov | `6603997a89128bcca2c76379bbfa460e20fde04b` | Candidate `c79898f9…36f4`: bounded source/interface PASS and 10 local predicate fixtures; no independent full rebuild/hash recomputation |

The earlier independent complete hashes and map replays certify only their named candidate bytes. The current bounded verification is described separately below.

## 2. Sources reopened and reading extent

**[SESSION]** Current candidate source reads were pinned to `7ca1b3ebf4294279c6a3d5525f481dae9132beff`, unless another revision is explicitly named:

- PR #265 metadata and `CONVENTIONS.md` on main; PR #268 state and the entire preceding fixed-path review at `6603997a`.
- Generated DSN §6.2 and §7, including the actual AZ citation, consumer row, non-adoption boundary and verified-source pin line; the DSN header/blob at generated-candidate commit `7f02c06`.
- Stage-1 builder E13/E25/E26 and adjacent edits; complete `consumers.md` and `pins.md`; checker C3/C4/C5 and C6/K1, plus adjacent controls; stored Stage-1 gate and negative-control outputs.
- Stage-2 movement-map identity/profile header and its `known_tags`; the complete v2.13 Appendix A entry; compaction-result summary and stored negative controls.
- DRAFT release record identities, §3c authority and source comparison, §7 notice disposition, §8 lint interpretation, and review/adoption boundary. The current release-record filler was inspected at its intermediate-size calculation and foreign-RID explanation.
- AZ's annotated `az-v0.10` reference and tagged release record (PI adoption recorded on 16 Nov); tagged AZ DSN §4.3.2's low-order-obstruction block and §8 IMP-B, particularly the event-inventory/census and parent-child rows and their updated local-use clauses.
- Candidate-branch `pipes/TDRG/20261116-AZ-v0-10-adopted.md` and the release record's handling of both AZ notices.
- Commit `7ca1b3e`'s diff correcting the unsupported `main` reading reference to `2d898fd` and the inbox status. The diff changes the release-record template and filled record, not the DSN.

This was a source/interface readback, not a full reread of unchanged TDR-G science or a new scientific campaign. The local runtime cannot resolve GitHub for an executable checkout. No independent complete two-stage build, full-candidate SHA-256 calculation, or replay of all 43 current map operations is claimed in this pass.

## 3. AZ v0.10 synchronization — PASS

**[OWNER: AZ v0.10 §4.3.2 / AZ-ALG-ANTIPODAL-LOWORDER]** The inspected statement has the same narrow-band antipodal-graph content used by TDR-G. Actual candidate §6.2 cites `az-v0.10` while retaining static-graph scope, no dynamical/bridge interpretation, and the TDR-19 OPEN boundary. The five-edition byte-equality check is implemented in C6 and reported PASS by the owner; it was not independently run across all five tags here.

**[SESSION] E13/E25/E26: PASS.** E13 emits `az-v0.10`; E25 inserts the source-accurate AZ v0.10 consumer row; E26 uses the new pin heading **Verified source editions used by this release**. The remaining occurrence of the old heading in E25/E26's input anchor is correct: it matches the adopted predecessor, not the generated candidate.

**[OWNER: AZ v0.10 §8 / IMP-B]** AZ continues to use TDR-G v2.12.15. The event-inventory/token-census local-use clause now names both S1 and S2 checks, and the conditional parent-child local-use clause refers to both §4.2.1 and §4.2.2. Neither clause claims a growth mechanism or TDR-26 consequence. The candidate consumer row follows these uses and explicitly identifies **AZ-NUM-TOKRES-S1 and AZ-NUM-TOKRES-S2 as AZ-owned numerical diagnostics**, not TDR-G results or demonstrated mechanisms. No numerical TDR-G adoption is asserted.

The source grades in prose are unambiguous. Attribution and the non-adoption boundary, not typography alone, establish ownership; this review does not claim that an explicitly attributed source-status tag would automatically constitute adoption.

The v2.13 Appendix A entry and Stage-2 known-tag profile include AZ v0.10. Earlier edition history retains its historical pins. The verified-source heading avoids the false premise that a pinned edition must always be the latest producer edition; future repinning remains claim/use-dependent rather than automatic.

## 4. Verification actually performed

### 4.1 Independent bounded source and predicate checks

The complete consumer and pin blocks were copied from the reopened source and checked against GitHub's blob identity before local testing:

| Block | Git blob SHA-1 | Independently computed SHA-256 |
|---|---|---|
| `stage1/blocks/consumers.md` | `614e6ef72302616243629aeda70727f535a53ee0` | `46d3b8f85a4effaec46d310b46548ab824b0e1e28400f53dd3fc20ecda57aeac` |
| `stage1/blocks/pins.md` | `36a5e75321f6a763f091d17d93d31af7ea4d2608` | `8954b1b45fdca28f18687c62b24d079fe6ac15b9c652becc8fbfc1c0d19f5572` |

**[SESSION] 14/14 local fixtures behaved as expected:** the valid source was accepted; 13 corruptions were rejected: K1 v0.10→v0.9 regression, old TDR-G consumer version, missing inventory/census/phase identifier (three cases), missing S2, removed AZ ownership, removed mechanism boundary, local declaration of S1 or S2 (two cases), duplicated AZ row, restored Governing-editions language, and an old AZ pin elsewhere in the tested live fragment.

These tests execute the inspected C6 **local consumer/pin predicates**. They are not the complete C6 external-source check, C0–C10, or a scientific simulation.

### 4.2 Full build identities and owner-run evidence

| Object | Recorded identity |
|---|---|
| Adopted base | `tdrg-v2.12.15`; `1e35be54a37bb227cd75e34fc1cd6732ae95782bdc147a76e736f16760c92e64` |
| New intermediate | commit `b7687f11c38f8adc5af2e4d42ff5c74a4e7f2dce`; `a27c3c525a4500ee4f62974ae5d508dbc5fdb450a4e2fe06ae8f6f46716775eb` |
| Current candidate | `6a4b94d5ec6946cad177889d453044a69eb4aa451763a2e81148b2e11739de88`; Git blob `3af27eca21a060064d13e2d8bb1a5236f287043d` |
| Movement map | `72408186ed90ed7fa993816668471aabe9abfd583cb974f8ff9f40b306d0fde5` |

Full-file SHA-256 values above are **owner-reported, cross-checked between the release record and map**, not independently recomputed in this pass. GitHub reports the same DSN blob at `7f02c06` and `7ca1b3e`, confirming that the subsequent provenance-record correction did not change the candidate file.

Owner-run outputs inspected: Stage 1 has 29 edits, **11/11 gates and 10/10 negative controls**; C6 reads AZ v0.6 through v0.10 and K1 regresses to v0.9. C3 reports exactly three newly mentioned foreign identifiers (OFN's open-interaction RID, AZ's S1 and S2), not new TDR-G declarations. C4's declared truth-tag changes remain unchanged. Stage 2 reports **PASS**, 268 qualified blocks (244 identical, 24 declared, 0 unexplained), and **8/8 negative controls** using the new intermediate identity. The clean-worktree reproduction remains owner-reported; this bounded review does not replace the Atlas recheck.

## 5. Provenance, inbox and nonblocking record-only cleanup

**[SESSION] Provenance correction verified at file-diff level.** Commit `7ca1b3e` removes the unsupported `e8b40cb` reading assertion, replaces it with `2d898fd`, and records the actually present AZ v0.10 notice. The commit message preserves the acknowledgement of the earlier error. This verifies the corrected repository record, not the historical act of reading in another session. The command-chain failure reported by the owner warrants fail-closed execution for future build/recording pipelines; it does not require a DSN-byte correction here.

The AZ v0.10 notice is **dispositioned · accept on the candidate branch**, not closed; the release record also retains the AZ v0.9 disposition and reserves closure for after the tag. Receipt, disposition and adopted scientific use remain separate.

**NB1 — record-only enumeration omission.** Release §8's raw lint correctly reports `new_rids: 3`, but the generated explanation still enumerates only `RTG-OFN-OPEN-DISC-INTERACTION` and `AZ-NUM-TOKRES-S1`. The current `fill_release_record.py` contains that same two-item text. Add `AZ-NUM-TOKRES-S2` to the filler explanation and regenerate the DRAFT release record when filling this readback and the Atlas verdict. Actual new TDR-G declarations remain zero; growth per new TDR-G RID remains N/A. **No candidate DSN change, two-stage rebuild, or repeat scientific campaign is needed for NB1.**

Before publication, update the PR body and the release's latest-review row to this candidate instead of presenting the old v0.9 readback as current. Preserve the earlier hash-specific reviews. Publication BASELINE changes must be based on then-current main without overwriting other streams.

## 6. Final reviewer disposition and remaining boundary

**PASS / AZ v0.10 READBACK CLOSED** for the bounded source/interface delta at candidate `6a4b94d5ec6946cad177889d453044a69eb4aa451763a2e81148b2e11739de88`. The reviewer requests no new DSN correction round. NB1 belongs in the ordinary release-record completion, alongside this review reference and the new Atlas result.

Next: Atlas's recheck of the new candidate; the PI's separate v2.13 adoption; publication record/status/BASELINE preparation; and separately authorized merge/tag. Choosing option 1 authorized the repin, not those later acts. TDR-19, XFER-O08-01, crystallization-grade reconciliation and the TDR-6 physical-observable question remain outside this maintenance readback. No canonical DSN, engine, pipe item, main branch or tag was modified by this review.
