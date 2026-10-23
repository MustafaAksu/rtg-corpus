# RTG State Atlas v0.2 — change-focused receiving review

**Date:** 23 October 2026.  
**Reviewer:** ChatGPT.  
**Status:** SESSION / NONCANONICAL review; not PI acceptance or owner-science adoption.  
**Verdict:** **REVISE — four bounded corrections in this same v0.2 PR before acceptance.** The refresh architecture and the inspected principal DYAD/RER updates are supported. The current candidate still contains stale diagnostics, dangling diagnostic references, process wording, and checker false-positive paths. No new DSN release, full corpus rebuild, compression campaign, or inherited scientific-certificate rerun is requested.

## 1. Target and actual review extent

Repository: `MustafaAksu/rtg-corpus`, PR #11. Reviewed head: `2067746d2d530763b5bd4092579dd18f30b7c7a7`; PR base: `44b55d6db07c467fbad495efa6c30c5bbc639787`.

The review packet reports these identities:

| Object | Reported SHA-256 | GitHub blob returned for this review |
|---|---|---|
| Atlas | `8a5b51d2356fbb460d90d5fe37c5f13aa72b9035759ca60934980f7368bbf167` | `37102b006b35818bd2aac4bd58aebffea978c775` |
| Method | `afa4127f0f12b30da689ef94a5d2eae905df82c168dc342fb646765c12f29d7f` | `b1d227b062651193a747a47fe2af8a0e6fd98e99` |
| Source manifest | `35013c11eea7b6854287e0ab69db04b81ccbc15de63b23850fcf0eacc75e5a98` | `fcf84ec087de9e4fb6bde6b1aedde9f6f52b12d0` |
| Checker | `4377a389f34871bd15d3b827fcac6272dcead5018557a21478b34ed4ab471d1d` | `1ae634437cea2a6c91a64f743dfb4e97ae750060` |

These SHA-256 values are packet-reported, not independently recomputed for the full four remote files in this pass. GitHub was read at the pinned commit. The local execution environment could not clone/download the repository, so this review does not claim a whole-repository replay.

**Read completely:** review packet; Method v0.2; source manifest; all 197 disposition rows and retired-key list; checker source including its self-test; submitted checker/self-test reports; acceptance-record draft; RER edit script; PASS-relocation script and build README.

**Inspected by changed block / section:** Atlas source table and L0/headlines, DYAD extraction operations and affected D2 records/frontier/constraints, RER records and source updates, D3 cross-links, selected D4a content, and relevant DYAD v6.4.22 and adopted RER v0.2 owner passages. Not a new full read of all 18 owner documents or a claim-by-claim certification of the whole Atlas.

**Executed here:** five negative component fixtures and one positive fixture using the retrieved checker's relevant function bodies; two elementary exact-rational rounding checks. These are component tests, not the owner's eight-test full self-test replay. The submitted self-test report was read, not independently rerun. None of the negative fixtures was inserted into the repository candidate.

## 2. Supported portions — retain without reopening

- Method v0.2 incorporates the principal ARP distinctions: functional current state, explicit source classes, frozen source snapshot, current owner versus actual consumer pin, conditional theorem versus unjustified application, and missing proof versus unavailable/not-rerun evidence.
- The inspected DYAD additions preserve the raw/normalized and W/Z distinctions, the archival h4 field `Q(i sqrt(3))`, R9 dependence of OPEN21, and the difference between the finite chart and the smooth equivariant chart. The 16/3 cross-reference is present as arithmetic bookkeeping, not birth-policy selection.
- RER formal age is `[ALG]` with `FORMAL_ONLY` exactness, not an analytic or physical-clock theorem. The same-space W3 condition, analytic/triad non-transfer boundaries, and the two blocked ER-2B records remain visible.
- The scoped RER acceptance is a registry-level acceptance of 18 payloads; it does not install those results into the TRIAD DSN or create TRIAD RIDs. Prefer that explicit wording over an unqualified “not adopted” or “not owner-adopted”.
- Current tag identity and previous-extraction byte equality are different checks. The 13 UNVERIFIED prior-input equalities are disclosed correctly as a separate limitation. They need not force an immediate reread of all unaffected documents. Do not relabel them EQUAL or describe all carried-forward statements as newly verified.
- General wording compression and per-node distribution of historical arithmetic checks can remain deferred.

## 3. AV02-01 — checker acceptance must distinguish claims, mentions and denied identifiers

**Priority:** required before treating the present coverage/link results as the planned typed checks.  
**Locations:** `tools/atlas_check.py`: `Atlas.__init__`, `occurrences`, `declared_rids`, `check_coverage`, `check_links`, `check_qualifiers`.

### 3.1 An explicitly denied owner identifier is counted as declared

DYAD v6.4.22, Local Tag Aliases / Current-grade lookup, explicitly contains:

```text
| `DYAD-CAND-PHISTAR-ENTRY-PHASE` | never a Dyadic identifier ... | §7 notices |
```

`declared_rids()` treats the first table cell as a declaration without considering the row's function. Consequently `check_links()` returns `PASS: declared in DYAD` for this exact denied name. The name appears in Atlas diagnostics, so this is directly relevant to the submitted link count, not merely a hypothetical new format. Moving the same name into a fabricated result node also passes the link gate in a component fixture.

**Required repair:** extract recognized owner declarations from typed owner locations, distinguishing active declarations, retired real IDs, references/consumer strings, and explicit denials. For DYAD, its documented `[RID: ...]` convention plus an explicit reviewed historical/alias map is available. Do not add ad hoc positive aliases for denied names. A documented phantom is `DOCUMENTED-UNRESOLVED` (or an equally explicit non-resolved status), never PASS. Genuinely unfamiliar declaration syntax may remain UNVERIFIED.

### 3.2 A surviving dependency mention is not coverage of its source claim

`check_coverage()` accepts any occurrence in content classified as `node`, except a cert-only segment. It does not require a result home, an approved alias, or a shared statement. All ordinary L0 text is also classified as `node`.

A component fixture with a declared `DYAD-ALG-RAW-ANGULAR-MEAN` passes when its entire claim is omitted and only this line survives:

```text
*FIXTURE:consumer OPEN | unidentified application | <DYAD-ALG-RAW-ANGULAR-MEAN
```

A mention only in an L0 identifier list passes as well. This does not show that this particular result is absent in the submitted Atlas; it shows that the asserted coverage gate cannot establish that it is represented.

**Required repair:** produce a typed source-item-to-home map. Each item resolves to its claim/definition/OPEN home, an explicitly reviewed alias/shared home, or a justified exclusion. Dependency mentions and index lists are not claim homes. Artifact references remain a separate category. This is structural mapping, not a request for a natural-language semantic-equivalence engine.

### 3.3 “unconditional” passes the conditional-marker test

The code uses substring membership for the marker `conditional`. Thus a node containing `unconditional bound` passes the conditional-marker gate for an owner result requiring R9. This was executed as a component fixture; it is not a finding that the real OPEN21 node lost R9.

**Required repair:** parse an explicit qualifier field / bounded marker and retain the named prerequisite for the few declarations covered by this gate. At minimum, `unconditional` must not satisfy `conditional`. State the narrow implemented coverage in the report; do not imply all Atlas qualifiers were checked.

### 3.4 Executed fixtures

| Fixture | Expected | Observed |
|---|---|---|
| RV-P1: explicit claim home | PASS | PASS |
| RV-N1: owner-denied ID, diagnostic-only use | documented unresolved, not PASS | PASS |
| RV-N1b: same denied ID in a fabricated result node | FAIL / explicitly unresolved | PASS |
| RV-N2: claim removed, bare dependency remains | FAIL / UNVERIFIED absent a shared-home map | PASS |
| RV-N2b: claim removed, L0 mention remains | FAIL | PASS |
| RV-N3: conditional owner, node says “unconditional” | FAIL | PASS |

The reviewer package supplies the fixtures and outputs. Keep the eight existing controls, add these cases, and regenerate the report. Do not interpret the old 128 coverage passes or 407 link passes as proof of completeness while these paths remain.

## 4. AV02-02 — reconcile retained diagnostics and references with the changed DYAD source

**Priority:** required current-state correctness; local edits, no new owner science.

| Site | Observed conflict | Required disposition |
|---|---|---|
| D2.L5 `DYAD.X9`, Atlas line 605; disposition row 66 | Still says the 16/3 relation is “unlinked”. The new Atlas export-contract record and DYAD v6.4.22 §6.12 explicitly state the cross-reference. | Delete the obsolete unlinked diagnosis and keep the mathematical identity at its content home. A distinct consumer-side omission needs a separately evidenced, narrower statement. |
| D3.L1 `K_p family (RECOG frame)`, line 639 | Still ends `! RECOG.R-C3`, although R-C3 is retired by disposition row 94 and the frame relation is a current owner result. | Replace the conflict pointer with the appropriate `DYAD-ALG-KP-FRAME-SCALE` content edge; scan all occurrences of retired keys. Do not resurrect R-C3 as a “resolved” diagnostic. |
| D2.L5 `DYAD.X4`, line 602 | Treats the immutable CAND-prefixed IDs with THM status as a “misleading type” diagnostic; the owner explicitly provides the current-grade lookup and says the prefix is not the grade. | Remove the prefix-only defect. Retain independently justified missing-RID questions, without demanding renames or treating definitions as theorems. |
| D2.L5 `NUMGEN.N-C2`, line 611 | Still diagnoses a comparison with DYAD “THM/ALG”; the current DYAD PHASELAW entry uses `[THM]` with an exact-algebra proof qualifier. | Re-evaluate against the actual pinned NUMGEN use and the current owner statement. Do not retain a current degree/convention conflict solely from the old compound spelling. Any historical-pin issue must identify the actual mismatch. |

Add a reference check for stable diagnostic keys (including namespace-qualified forms) and their retired-key register. The present RID-only checker cannot detect dangling `RECOG.R-C3` edges. Other deleted keys should receive the same local scan; this is not a request to redo all scientific diagnostics.

Update the corresponding disposition rows and counts. “Retained; sources, dependencies and semantics unchanged” is not adequate for an entry whose DYAD premise changed.

## 5. AV02-03 — complete the agreed current-only wording pass

**Priority:** required scope of this refresh, not a new compression campaign.

Examples still in the actual candidate:

- D1 owner introduction, line 82: `pass one done / pass two pending`.
- D2.L3 p-resonance line 561: `Tier-C target FC-DYAD-31`.
- D2.L3 phase-constants line 565: `import ... deferred ... (governance only)` and `NUMGEN-side not started` mix process handling with the scientific availability/domain boundary.

The first two are not mathematical uses of history-related words and are not scientific evidence limitations. The packet's statement that all 28 residual warnings are owner statuses or necessary source quotations is too broad.

**Replacement pattern:** retain the open target “exact large-p behaviour of |Q_p|”, the available owner result, the precise consumer use/domain and the missing scientific obligation; remove the advisory tier/key and editorial scheduling. Process records remain under `records/`. Keep dates/versions needed for actual import identity, valid rejected-route constraints, source quotations supporting a diagnosis, and evidence limitations. Do not blindly remove every `pending`, `history`, `return` or `resolved` token.

An advisory-key pattern check can supplement the wording warnings. This is a finite cleanup, not a size target.

## 6. AV02-04 — pooled evidence is acceptable, but its type and execution context must be truthful

**Priority:** required clarification / small math-format correction. Distribution among individual nodes is not required in this release.

The seven `*ATLAS:checked-Dk` blocks are a reasonable temporary grouping. Their transfer into L2 must not upgrade old reports into new computations or numerical values into exact identities.

1. Method §6 and Atlas L0 define `atlas-checked` in terms of exact facts, while the new blocks explicitly mix exact algebra, floating/high-precision checks, and source-consistency observations. State these types separately; an evidence record is not a new owner claim.
2. `build/pass.py` moves the v0.1 PASS text and inserts “recomputations ... during the build (EV-INDEP ...)”. Identify whether each group is carried-forward Atlas-v0.1 evidence or actually rerun in v0.2. A frozen prior evidence pointer can supply the context compactly. Do not imply a fresh replay merely because the text moved. The review packet's new h4/RAW-CUBIC checks may have their own distinct context.
3. Preserve exact equality versus rounded evaluation. In the D2 evidence record (line 556), for example:

```text
517*(256/225)^2 = 33882112/50625 ≈ 669.276
1.51632*1.06252 = 1.6111203264 ≈ 1.61112
```

The current `=669.276=33882112/50625` and `...=1.61112` are not exact equalities. These two checks were recomputed with rational arithmetic in this review. This is an Atlas presentation correction; it does not change an owner bound or require a certificate campaign.

A compact grouped record may cite a small index of fact/owner/verification-kind/evidence-context. Its per-node distribution can remain deferred. Avoid duplicating owner claims or manufacturing a scientific RID for the evidence group.

## 7. Answers to the three packet questions

**Q1 — one evidence record per domain:** acceptable as a temporary layout, subject to AV02-04. Per-node redistribution can wait; evidence typing and provenance cannot.

**Q2 — age-only D-PIN deletion:** acceptable. An old intentional pin is not inherently defective, and Git preserves the diagnostic history. This does not excuse a demonstrated identity/scope mismatch, a consumer assertion of a superseded fact, or a dangling pointer. Recheck the concrete residuals in AV02-02; do not restore entire old edition inventories.

**Q3 — UNVERIFIED declaration forms:** no comprehensive parser expansion is needed for v0.2. Genuine unknown syntax/source ownership may remain UNVERIFIED with an exact source locator and reason. Explicit owner denials and already-classified historical consumer strings are not merely unknown syntax: record their known non-resolved type. A `cert` script-name match proves source naming, not file availability or successful execution.

The 13 prior-input equalities marked UNVERIFIED are an independent axis from the report's 18 link/artifact UNVERIFIED items. Keep both visible in the acceptance limitation. The 72 current-source checks do not establish those 13 historical equalities.

## 8. Bounded completion contract

Keep PR #11 and target v0.2. Apply AV02-01–04 in one batch, then provide:

1. The exact changed Atlas/method passages and corrected L5 dispositions.
2. The typed source-item-to-home map and retired-key reference check.
3. The regenerated checker report and controls, including the reviewer fixtures; retain genuine UNVERIFIED cases.
4. Final identities in the acceptance record; source freeze and owner assumptions unchanged unless an explicit divergence is recorded.

Then perform a change-focused check of those corrections only. Do not rerun NF, interval arithmetic, smooth embedding, RER regional campaigns, or reread every unaffected source. No automatic owner regrade, alias registration, consumer repin, or forced history compression follows.

The PI decision remains unfilled. Do not merge or create `atlas-v0.2` as an accepted release on the basis of this review. RECOG advisory work can start from the accepted corrected snapshot afterward.

## 9. Source locators

All PR files above were read at `2067746d2d530763b5bd4092579dd18f30b7c7a7`.

- `records/atlas/ATLAS_V0_2_REVIEW_PACKET.md`, §§3–11.
- `atlas/RTG_STATE_ATLAS_METHOD.md`, §§2–7.
- `atlas/RTG_STATE_ATLAS.md`, source table/L0; lines 82, 550–575, 590–619, 635–660, 990–1014 and the other inspected change blocks.
- `records/atlas/ATLAS_V0_2_L5_DISPOSITIONS.md`, all 197 rows; especially 66, 91–107 and retired keys.
- `tools/atlas_check.py`, complete source; functions identified in AV02-01.
- `evidence/atlas/build/rer.py`, `pass.py`, `d2.py` inspected changes; build README states these are edit-operation records, not a rerunnable complete pipeline.
- `evidence/atlas/source_manifest_v0_2.json`; `coverage_dispositions_v0_2.json` (empty exception maps); both check reports.
- `dsn/RTG_DYADIC_OSCILLATOR_DSN.md` at `dyad-v6.4.22`, Local Tag Aliases/current-grade lookup and §6.12 export table.
- `noncanonical/RTG_RELATIONAL_EMERGENCE_REGISTRY.md` at `rer-v0.2`, formal-age record and current adoption-scope reading.

No canonical DSN or Atlas content is modified by this review. Review artifacts do not adopt any scientific result.
