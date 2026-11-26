# RRF v0.9 — S2b structural candidate and review gate

**Status:** DRAFT / SESSION. No adoption or merge of a DSN is authorized. Governing edition remains rrf-v0.8.4. PI on 26 November 2026: "S2b kabul / Merge işlemleri yapılabilir." Interpreted as approval of the narrowed OPEN criterion wording for this candidate and S2b work, and merge authorization for the separately requested #406 and #410 records only. No scientific acceptance of BR-Q2 or registration/release decision.

## Entry

- S2a freeze: #404 `98da97c311a917d1539b9c31afaba779bc75a73f`, SHA-256 `390f75e447b7d5a9dcb01810d7eb513e9feef3c157f0de2f2f79afb259b39d72`, 131,089 bytes; Claude ACCEPT SCOPED review 6076472389, merged reviewer record #406.
- PI-authorized record merges: #406 `b29b5afc326f7af10761b881b53ec8f33aec3cc2`; #410 `5bb35b9aa531891659e8b7f4c99a027b0eef4b72` (BR-Q2 SESSION only).
- Main checkpoint `5bb35b9aa531891659e8b7f4c99a027b0eef4b72`; RRF blob equals adopted rrf-v0.8.4. All twelve accepted S1 governing tags rechecked, same editions. Ten open RRF items at checkpoint; no queue change. #414 is separate, pending independent scientific review.
- S2b candidate SHA-256 `6f258d1833cfe7d67d47addf4ff32f9873c08987b484d803c96e9745183f5dd2`, 120196 bytes, 654 split lines. The accepted S2a freeze is an ancestor of this review branch, not a versioned duplicate DSN or an adopted tag.

## Structural scope

The complete map `evidence/rrf/v0.9/s2b_movement_map.json` binds every source and destination line span and its SHA-256. 76 operations: 33 exact spans (525 source lines), 10 archival spans (128 lines), 18 bounded editorial replacements, 15 navigation insertions. The map distinguishes archive, exact retention/movement, candidate metadata/heading changes and added navigation; all archive spans resolve to the actual immutable S2a commit. The adopted predecessor is also the source of its dated history. No second stored DSN.

- Current DRAFT header and declared infrastructure/registry section map; retain §1 annotation syntax profile exception.
- Superseded publication/OPEN20 overlays, explicitly historical §0.2 receipts and old §9/§10 publication histories relocated to immutable Git, not to a live claim appendix. Retain actual proof-source rows and evidence limits in §§0.1,7.5; RF-O09-03/04, SG-15 and P2-B archive pointers survive.
- Five profile headings, all technical map/comparator/transport/formula paragraphs, owner import tags and four OPEN question/criterion/dependency rows preserved exactly (metadata-only closure column heading/preamble correction for the PI approval). No BR-Q2 result introduced.
- Six proposed RRF-local identifiers attached as navigation to their already accepted candidate homes; existing ID index retained. No scientific owner result re-owned and no identifier registered before adoption.
- OPEN registry moved to §6.5; consumer/source/evidence registers to §7 with a distinct unregistered-object subsection. Import use index: 60 actual inline source tags, locators to unchanged qualified local blocks, actual historical/current source distinction and unavailable-RID governance follow-up. The one unversioned DYAD §6.12 guard is given the current exact-text source locator (DYAD v6.4.24 §6.12, projection-order identity, inspected); no scientific regrade or pin substitution in the original line. Owner-grade coverage and remaining §4.3 ledger field adequacy are reviewer obligations, not certified merely by the index.
- One Appendix A entry and Appendix B correction routing to the already reviewed S2a; single DRAFT footer.

## Mechanical and scientific gate

The shared `tools/check_compaction.py` was read (operation classes, header/appendix assumptions, history checks, and movement constraints), as was its DYAD-oriented negative-control harness. It assumes a Markdown field header and history regions under `##`, disallows the required cross-section byte-exact moves, and rejects explicitly historical tagged paragraphs outside its narrow region types. The frozen RRF intermediate has YAML and a nonstandard section structure; the shared checker cannot be claimed to pass on these raw inputs. Do not weaken shared tooling or fake a generic PASS. Proposed RRF-specific exact-span adapter `evidence/rrf/scripts/check_rrf_s2b.py` implements full source/destination accounting, byte-equivalence for exact spans, immutable archive locator identity, per-span hash, exact indexed import use, OPEN status and profile preservation. Requires independent profile calibration acceptance before release (Methodology §13.6). Its mechanical success does not prove that history classification or editorial replacements are semantically appropriate.

Preparer executed connector-side JavaScript exact-span reconstruction and 3 negative controls (coefficient changed with file rehash, missing operation, duplicate operation). All rejected as expected. Native Python adapter and its additional archive-locator negative control are provided but **not executed by the preparer**. Independent reviewer should run:

```bash
python -I evidence/rrf/scripts/check_rrf_s2b.py
tmp=$(mktemp -d)
git show 98da97c311a917d1539b9c31afaba779bc75a73f:dsn/RTG_RRF_REPRESENTATION_REGISTRY.md > "$tmp/s2a.md"
python tools/dsn_lint.py dsn/RTG_RRF_REPRESENTATION_REGISTRY.md --prev "$tmp/s2a.md"
```

Review every archive span and editorial change against the frozen source (particularly operative source/evidence boundaries, §§0.1/0.2,6.5,7.2/7.5). Accept or correct the profile-specific checker and its negative controls; check import-ledger completeness and source locators, proposed local IDs and OPEN aliases, header and section map. Lint is informational. If the shared checker must run on raw RRF bytes, a separately reviewed profile extension is required; no such extension is included in this PR. Do not move to release until the independent reviewer has resolved this gate. S2a native check can still be reproduced on the immutable S2a checkout; it is not meant to compare against the compacted candidate.

No protected owner DSN, BASELINE, pipe state, source archive, shared tooling or existing reviewer record changed. BR-Q2 research PR #414 remains separate, with no adoption inferred from #410's merge. Final adoption, outbound notices, tag and BASELINE update remain PI_PENDING. LIT dependencies: none.
