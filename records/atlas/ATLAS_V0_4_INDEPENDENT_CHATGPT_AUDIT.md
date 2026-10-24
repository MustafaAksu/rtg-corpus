# Atlas v0.4 — independent pre-reconciliation consistency audit (ChatGPT)

**Status:** SESSION / NONCANONICAL, independent candidate findings, **not Atlas v0.4 acceptance**.  
**Date:** 24 October 2026.  
**Procedure:** This audit deliberately did **not** inspect the Atlas owner's forthcoming v0.4 pass or its findings. Reconcile only after both independent inventories have been fixed. No owner DSN or Atlas source file was edited.

## 1. Source manifest and reading extent

- Governing Atlas: annotated `atlas-v0.3`; `atlas/RTG_STATE_ATLAS.md` SHA-256 `71310e8c5e1b29979a854ee2ee932efa4765f038bbe0c10299e14f424ad1dc5b`. Local source bytes independently hash-matched: **467,029 bytes / 1,560 lines**, **read across all six domains and L0/H1–H12, object index, frontier and all L5 sections**; detailed programmatic scan of diagnostic records.
- Governing method: `atlas/RTG_STATE_ATLAS_METHOD.md` v0.2 (read entire method from tagged GitHub source); governing DSN Methodology `methodology-v1.4` for claims and release discipline; repository-root `CONVENTIONS.md` read.
- Newly adopted Programme: `programme-v1.3`, SHA-256 `1b8358b3e1d3abb853e226786d21e6559c289b7c85570dac0ff1ebc2dabaea06`. Owner §§0–9 and the §6.1 inventory / §7.2 interfaces / §8.2 symbol table inspected at its tag. Its accepted status also appears in `BASELINE.md`.
- Targeted tagged owner statements: `gen-v2.8.9` header, `rer-v0.2` header and adopted-scope declarations; previously verified `recog-v0.3.23` current A1a; full mathematical owner proofs outside these targeted sections **not reread**. Other Atlas-source editions retained at the v0.3 freeze; no assertion of new global tag status is made from memory.

## 2. Findings requiring v0.4 disposition

### A04-01 — verified stale Programme owner-state diagnostics (BLOCKING to a current v0.4 map)

[OWNER: Programme v1.3 §§6.1–7.2] The adopted Programme already inventories RRF, RER, FMS, ER2B and Atlas; distinguishes canonical, working-standard, noncanonical and derived classes; and replaces the September interfaces with current owner/consumer pins.

[SESSION] Atlas v0.3 still claims the opposite in **H10 (line 53)** and **D1.L5 PROG.G1/G2/G4 (lines 254–256)**. The error is not merely the `PROG` source row still pointing to v1.2: the *live diagnosis itself* is false against the governing v1.3 owner statement.

**Disposition:** retire G1/G2/G4 with v0.3→v0.4 reason and archival key retention; update `SOURCES` and its frozen manifest to Programme v1.3. Rebuild H10 from its independent OPEN-M and PREL components; do not close them by Programme repinning. Preserve actual historical consumer pins where supported.

### A04-02 — stale Programme data reproduced as current navigation (BLOCKING)

[SESSION] Besides the diagnostics, **D1.L1 PROG-TIERS (line 87)** says “14 document homes” and lists Tier 5 as AZ alone; **D1.L1 PROG-INTERFACE-TYPES (line 89)** still includes the retired “transfer-proposal” description without the v1.3 additions. **D1.L5 PROG.G6 (line 258)** presents the old unexecuted maintenance sequence instead of the current remaining queue. **H8 (line 51)** recommends creation of a κ symbol table which Programme v1.3 §8.2 already supplies.

[OWNER: Programme v1.3 §§6.1, 7.1–7.2, 8.2, 9.2] Current inventory is fifteen `dsn/` homes including RRF, three `noncanonical/` entries, and one derived Atlas; remaining owner-maintenance queue is PREL, TDRG, DZT and AZ. Programme §8.2 already has a cross-stream κ table, but this does **not** solve genuine symbol collisions.

**Disposition:** revise D1 objects and cross-domain index where necessary, replace the creation request with “verify/use current table,” and narrow G6 to the remaining PREL owner update. Retain unresolved κ interpretation/collision as diagnosis, not a missing-table claim. Avoid inventing Programme maturity changes.

### A04-03 — atlas-derived equivalence visually promoted to owner-level identity (HIGH-PRIORITY SEMANTIC)

[OWNER: Programme v1.3 §8.2] The class-C κ to Genesis γ relation is expressly characterized as an **Atlas reading, not an owner statement**.

[SESSION] Atlas v0.3 **cross-domain index line 67** writes “class C ≡ GEN F_γ (γ≡κ),” **D1.L1 line 120** and **H8 line 51** use the same equivalence without a nearby `~`. In contrast **D1.L5 RRF.F5 (line 252)** uses `~ D-LINK` and says the connection is Atlas-derived. A reader of the index alone will mistakenly read a verified owner equivalence.

**Disposition:** qualify *every point of use* of the cross-owner identification as “~ (atlas-derived, unaccepted)” or limit it to a model-parameter dictionary with precise family scope. Do not rename either owner's symbols or claim physical model identity merely from a coefficient correspondence.

### A04-04 — generic “all RER Triadic records” inference exceeds demonstrated shared-model correspondence (TARGETED OWNER CHECK REQUIRED)

[SESSION] **H7 (line 50)** goes from the RER modal-map identification to “every RER Triadic record sits in the flat A1 sector OFN excludes”; **D4a.L5 F2 (line 1097)** similarly groups formal age, 3-fold and birth-graph records under this assertion. F2 does have `~`, but H7 and **cross-domain index line 68** present stronger identity syntax without carrying the model/profile restrictions.

[OWNER: RER v0.2 header/adoption scope] RER is a noncanonical registry of **18 scoped, receiver-accepted** records plus **two BLOCKED_SOURCE_UNVERIFIED** records; their hypotheses and source-custody boundaries are not interchangeable. Identification of a particular raw modal map with a γ=1 member does not automatically transfer the identical dynamical model interpretation to each record, especially conditional age sheets, transported contracts and blocked ER2B interfaces.

**Disposition:** keep the verified map-level equivalence at its precise representation/clock/parameter scope; mark the extension to the entire RER collection **[UNVERIFIED]**, request a per-record transfer matrix or remove the universal quantifier. This is a scope warning, **not** an assertion that the claimed identity is false.

### A04-05 — headline-to-L5 coverage needs multi-anchor semantics (MECHANICAL CONTRACT)

[SESSION] All twelve H lines have at least one textual L5 key match in the current Atlas (structural scan; a shared key is not proof of correct semantics). Some unnumbered D4a L5 entries are explicitly “high”: **F1, F2, F3, F5 (lines 1096–1100)**. H8, H7 and H1 appear to cover them by *content*, while H numbering is display-only. A strict one-to-one RID/key coverage rule would create false defects.

**Disposition:** construct an explicit machine-readable H→{L5 key, claim home, scope} map; require every high L5 item to appear through a reviewed multi-to-one mapping, without requiring one H per diagnostic. Give an explicit disposition to orphans; preserve L5 keys after retirement only in review records. Grade the semantic cross-reference separately from string-presence tests.

### A04-06 — high-impact assertion vs source-reported data in unchanged domains (DEFER / TARGETED RECHECK)

[SESSION] H6 / D4b GEN.D1–D2 retain K_+/K_- and sign(κ_f) tensions; they are high-priority targets for the planned Genesis owner review but must not be presented as algebraically resolved by this Atlas pass. The Genesis v2.8.9 header itself explicitly records the physical K sign as OPEN. Similarly H9 discrete degeneracy and F3 exact K3 cubic crosswalk require domain-qualified owner verification before semantic promotion.

**Disposition:** retain them as typed open diagnostics and target the affected sections, not new Atlas theorems. Do not spend v0.4 recomputing unchanged, expensive producer certificates.

## 3. Planned checks and review acceptance criteria

1. **H/L5 matrix:** every H maps to one or more current L5 records; every genuine `high` L5 item has an H path; archived/remapped keys are never recycled. Run negative controls: remove a headline edge, remove a high-L5 path, substitute a source-only name.
2. **Cross-domain pairs:** D2↔D3 primitive/chart/memory; D4a↔D4b K3 and source/metric conventions; D1↔D4a class-C; D2↔D6 historical raw coefficients; D5↔D1 discrete-owner imports. For each alleged mismatch compare object, representation, assumptions, clock, domain, numerical/symbolic status, grade and consumer pin.
3. **Owner-attribution matrix:** per L5 record `OWNER-VERIFIED` / `ATLAS-DERIVED (~)` / `SOURCE-REPORTED` / `UNVERIFIED`; prove no `~` item appears as unqualified adopted equivalence in H or cross-domain index.
4. **Snapshot update:** only new source is Programme v1.3 (if its bytes match the adopted tag); fourteen- vs fifteen-home totals, source manifest, H10 and affected PROG diagnostic dispositions must agree.
5. **Bounded correction:** first fix the verified source contradictions above in one batch. Record source/hash/changed passages and acceptance criteria. Keep all other 17 scientific source inputs and the Atlas method unchanged absent a demonstrated additional defect.
6. **Post-blind reconciliation:** compare this report with the Atlas owner's independently fixed first-pass record only after each has been frozen; classify agreement, genuine disagreement, new owner dependency, and nonblocking deferred items. Owner review, PI acceptance, merge and annotated tag are later decisions.

## 4. Boundaries and current decision

**Independent pre-reconciliation recommendation:** `REVISE SOURCE SNAPSHOT AND INTERNAL CROSS-REFERENCES`, not a verdict on an unbuilt Atlas v0.4 candidate. A04-01 and A04-02 are directly verified stale Programme use. A04-03 is an internal attribution mismatch with an explicit owner qualification. A04-04 is a reason to narrow or verify a universal inference, not a new proved contradiction. A04-05 is a proposed check contract. A04-06 is a scoped owner-review dependency.

No changes to adopted Atlas v0.3, scientific DSNs, source tags, consumer adoption, methodological grade, PI release records or notices are authorized by this report. All executable validation is structural unless separately documented.
