# RTG State Atlas v0.7 — change-focused review packet

**Date:** 28 October 2026. **Prepared by:** Claude, Atlas owner.
**Status:** DRAFT / NONCANONICAL — candidate for receiving review (ChatGPT, Atlas co-owner); no PI acceptance or owner-science adoption. `atlas-v0.6` governs until acceptance.

## 1. Inputs and identities

Base `atlas-v0.6`, SHA-256 `35ebee6d61f4db93211f2ed6f2de2bb973aa2fc6f2ea3cdf670656b1e961bd8a`. Source snapshot `origin/main` `53b56e4445a8c2869e41198e30bc66aa0fb93073` (after PR #99, TDR-G v2.12.14 post-tag closeout). **Two moved sources:**

| Source | Tag | Tag object | Merge commit | File SHA-256 | Verified |
|---|---|---|---|---|---|
| Discrete Genesis v2.12.14 | `tdrg-v2.12.14` | `da941f3b…` | `05c7e78acf63dd1dc5bcbc7bb8364e152e9f0659` | `3be72923cd40523399363e0dc044bba6246862d12b2bca190c74969e2cce2392` | `records/tdrg/TDRG_v2_12_14_TAG_VERIFICATION.md` (28 Oct; PR #98) |
| RECOG v0.3.25 | `recog-v0.3.25` | `3cb20657…` | `bdb3712397da146d75cef8f7d2999838a0620a0e` | `86cae8ff094d63d077ec5c0887451775ec3a26485cfad95833d8390bda4bd7db` | file hash equal at the tag and at the snapshot (builder assertion); no separate atlas tag-verification record exists for this tag |

The other 16 sources are byte-equal to their v0.6 inputs (manifest `v0_6_input_equality`: 16 EQUAL, 2 CHANGED, asserted).

| Object | SHA-256 |
|---|---|
| `atlas/RTG_STATE_ATLAS.md` (candidate) | `3655d4043e5eee046e93811d37b1fbe7bc863146dceed8b95c4e9d031ca53078` (492,007 bytes, 1,545 lines) |
| `atlas/RTG_STATE_ATLAS_METHOD.md` (unchanged) | `fbd2efb34cae6f291d1881cf79f6c521ea337c8a513d92b7d42deb889ed42c04` |
| `evidence/atlas/v0.7/source_manifest.json` | `e88e5b15037261eb0c694d908e0330b951e0b006c095cdd0a1e445419d43865d` |
| `tools/atlas_check.py` (unchanged) | `0db3a23b9cb78bc87f4b9393baf417c7329421f719f7acbaec2f4ca36626004d` |
| `evidence/atlas/build/refresh_v0_7.py` | `5ff22bf19e5d49cce64f5a6736b04231450cd399a313aba1ec2028d6521226c3` |
| `evidence/atlas/v0.7/edit_log.json` | `a390d9b48bfef886397cf8f6db6aa81322c98ac77a20afc641201a89ae0abdd7` |

Decision basis. TDR-G: `records/tdrg/ATLAS_ADVISORY_TDRG_v2_12_13_RECONCILIATION.md` (§3 merged list, §5 PI decisions), `TDRG_OWNER_DISPOSITION_RECONCILIATION_v2_12_13.md` (§2.2 fixed resolutions, §2.3 N1/N2), `ATLAS_ROW_CHECK_TDRG_v2_12_14.md` (§2 edit-by-disposition table), `TDRG_v2_12_14_RELEASE_RECORD.md` (§§3, 7, 8, 13) with `TDRG_v2_12_14_POST_TAG_ADDENDUM_20261028.md`, `TDRG_UPLOAD_HASH_CHECK_20261027.md`; the owner text at `tdrg-v2.12.14` §§1, 2, 6.3, 6.5, 6.6, 6.12, 7, 8, Appendix B. RECOG: `records/recog/RECOG_v0_3_25_RELEASE_RECORD.md` and the owner text at `recog-v0.3.25` §§1 (A1a/A1b/A1c summary), 6.13a (R9 rows), 6.13b (sharpened schedule), 6.16e (decoder, fibers), 7 (requests to Dyadic).

## 2. Review scope

Impact refresh of two domains; 68 exact-once operations (`evidence/atlas/v0.7/edit_log.json`); no other domain re-extracted. Diff against the base: 60 insertions, 59 deletions (one net line: new row RECOG.R-A1; TDRG.G1–G7 removed, TDRG.G10, G11 and five D5.L2 nodes added).

**TDR-G v2.12.14 (D5, H4, H9, D1 METH.M2 / OFN.O5 / OFN.O7, D2 NUMGEN.N-I1).**
- SOURCES row and D5 header to v2.12.14 (October 2026 corrections edition; Methodology v1.2 declared by PI decision; v1.4 migration = v2.13); the D5 alias note replaced (compound grades unpacked; node heads carry the owner RIDs with the former atlas labels in parentheses).
- Orientation (TA-01 / I01, TC-14 / I03): `TDRG-DEF-ORIENT` rewritten — balanced tie on S=0 ∧ 2E≡0 (E∈{0, N/2}), `signed_centered` (−N/2, N/2] named as the source of the stratum, the v2.12.13 text and the v18 node-ID completion recorded as the superseded completion, every computed result kept `[conv: v18 path orientation]` EV-NOT-RERUN. Five new D5.L2 nodes from the owner text: `TDRG-ALG-ORIENT-NOGO` (with the recorded, unadopted G-alternative), `TDRG-ALG-ORIENT-ANTIPODAL-FIXTURE`, `TDRG-NUM-ORIENT-EQUIVARIANCE-N24` (owner counts 72/72, 168/168, 0, 0; four nodes 112 vs 0; the atlas census bound 77 of 9,800 cycles, 4.9 % of k=1 states, cited from the atlas script as before), `TDRG-ALG-MIRROR-NOT-STEP-SYMMETRY` (N2), `TDRG-ALG-LARGEST-CENTER-ID-TIEBREAK` (N1). SG-14 added to the D5.L4 guard line; the retired-FAIL line names the node-ID completion as an instance of the arbitrary-label tie-break; the multistar node's tie wording extended. H9 rewritten from "needs a ruling" to "ruled": the ruling, the census bound, the 20-of-136 witness effect, NUMGEN's remaining re-annotation / C7C-M4 decision (D5.X1), the N1 residue (TDRG.G10), the range-tagged exponent. D5.X1 reworded (ruled on the TDR-G side; residual on the NUMGEN side; the TC-17 citation fixed: the owner-review tasks are in TDR-G §2 since v2.12.14, Programme v1.3 §6.4 does not list them, v1.2 §6 did). `*NUMGEN:DISC-1` and `*NUMGEN:P2-exposure` point to the ruling; NUMGEN's re-annotation is NUMGEN's.
- RIDs (TB-09 / I08): 23 node heads renamed from atlas labels (`*TDRG:state`, `CONV-TICK`, `LEM-*`, `BIND3-*`, …) to the registered owner RIDs (`TDRG-DEF-*`, `TDRG-THM-*`, `TDRG-ALG-LEM-*`, `TDRG-ALG/NUM-BIND3-*`), the former label kept as "alias" in the head; every new RID asserted present as `[RID: …]` in the tagged file (30 TDRG, 14 RECOG). H4 narrowed (TDR-G registered; OFN's repin resolves its "RID unavailable" imports); METH.M2, OFN.O5 reworded (owner side done, repins are the consumers'); AZ.A7 reworded (`TDRG-ZN-STATE` an alias in the §7 map; BIND3-*, TDR-24/26 labels remain AZ's).
- Corrections (TA-04/I06, TA-05/I04, TA-06/I05, TA-07, TC-15, TC-16): `*TDRG:bulk-fits` carries the owner's range tags (full range −0.869 `[NUM]`; 480–1440 window from the owner's own Exp-0 line; χ=0.836 check withdrawn as `[COR]`); `*TDRG:crystallization` `[HEUR]`; LEM-RETRIG wording (period dividing 2; d=0 a fixed point; no aliasing caveat); LEM-SPECCONS "therefore, in particular" with the N=24 counterexample and the note that the extended tie is identity; the K₃ 96:1 and the T-6 wedge references marked historical (TDR-T ladder line, retired-FAIL line); the star node's OFN edge records "statement accepted, custody XFER-O08-01 deferred to v2.13"; the narrow-band node cites AZ-ALG-ANTIPODAL-LOWORDER; OFN.O7 records the owner-side correction with the OFN side (OFN08-C12) still open.
- Custody (TB-11): new row TDRG.G11 from the owner §8 register and the hash-check record (placed / replayed / held with hashes / missing suites); `TDRG-ALG-BIND3-CYCLE-N24K1` marked EV-NOT-RERUN with the census bound.
- Pipes: NUMGEN.N-I1 extended — the two TDRG inbox items closed with their dispositions, three TDR-G notices filed (`pipes/NUMGEN`, `pipes/OFN`, `pipes/AZ`, `20261028-TDRG-v2-12-14-adopted.md`); the other receivers undecided; builder asserts the notice paths exist at the snapshot (`tools/pipes_index.py --check`: OK, 15 items).
- Retired: TDRG.G1, G2, G3, G4, G5, G6, G7 (reasons in `dispositions.json`). Reworded: TDRG.G8 (residual footer / Appendix A layout → v2.13), D5.X1, AZ.A7, OFN.O5, OFN.O7, METH.M2, NUMGEN.N-I1. New: TDRG.G10 (N1), TDRG.G11 (custody). Kept: TDRG.G9.

**RECOG v0.3.25 (D3, H5).**
- SOURCES row and D3 header to v0.3.25.
- `RECOG-THM-R9-MEMORY` node: the sharpened rows block (RECOG-ALG-R9-SUM-LEMMA; RECOG-THM-R9-SHARPENED-ROWS (259.2, 1/400), (81.49, 1/1600); RECOG-THM-R9-SHARPENED-ROWS-C7 `[assuming: C₇ ≤ 85.1 / 27.7]` (221.4), (75.69)); adopted rows (517, 163) stated as still in force.
- `RECOG-THM-A1B-SLIP-SCHEDULE-U` node: RECOG-THM-A1C-SHARPENED-SCHEDULE `[assuming: (D5)]` with the known-a centre c‴_k(a) and E‴ = O_a((1+log(a+M_k))/(a+M_k)) — computable from (a, M_k, r_k), not from the record alone; the three ALG blocks (tail harmonics, in-block angle, combined tail).
- `RECOG-RESULT-A1C-RECORD-PHASE-READOUT` node: the record-only outer enclosure (admissible region ℛ_K, start offset n₀ ≤ 7, joint interval contractor with the true a never an input; windows, not identification; no uniqueness) and the record-fiber result (threshold coding; fibers on one C¹ level curve of Ψ_∞, empty interior; A1c-Q1′ connectedness / injectivity OPEN). R6 sub-items updated accordingly (A1c-decoder answered in bounded form; A1c-Q1′ reworded). RECOG.R-D1 names the four new artifacts (not rerun by the owner build either, per the release record).
- New row RECOG.R-A1 (D-LINK, cross-owner dependency): the (D5) proof constants (0.79246, 0.36915) and the C₇ ceilings are `[assuming:]` in RECOG until Dyadic registers them; RECOG's requests to Dyadic are in its release record §4, not filed as pipe items; RECOG still pins NUMGEN v1.20.8.
- H5 extended by one sentence listing the v0.3.25 additions.

Not changed on purpose: TDR-G's declared Methodology v1.2 and its historical pins (owner text; PI decision); the ten `[conv: v18]` results' numbers (no rerun); the NUMGEN D2 nodes beyond the two DISC pointers (NUMGEN's re-annotation is pending on its side and not an atlas source); RECOG's NUMGEN v1.20.8 pin; the `*PROG:IF-register` line (Programme not moved).

## 3. Dispositions and mechanical checks

18 touched L5 rows: 7 retired, 8 reworded, 3 new (`dispositions.json`, hashes). Retired keys added to `retired_l5_keys.json`, not reused (guarded; the two in-text references to TDRG.G6 rewritten). Two builds give identical bytes; reproduce with `python3 -I evidence/atlas/build/refresh_v0_7.py` (asserts base hash, every source tag's hash and commit, tag/snapshot equality, TDRG file = `3be72923…2392`, RECOG file = `86cae8ff…db7b`, 16 EQUAL / 2 CHANGED, no stale "`tdrg-v2.12.13` / `recog-v0.3.24` / needs a TDR-G scientific ruling / Discrete-owner ruling required / carry no RIDs / with a unknown no window" wording, every cited RID present as `[RID: …]` in its tagged source, the three notice paths and the hash-check record present at the snapshot, no retired key referenced, no dangling H→L5 citation).

Shared checker: **zero FAIL**; PASS sources 72, coverage 128, qualifiers 3, links 473, artifacts 99, keys 105. Carried unchanged from v0.6: 5 link UNVERIFIED + 3 artifact UNVERIFIED, 11 DOCUMENTED-UNRESOLVED, 16 wording WARN (same sites, lines shifted; five new WARN sites introduced by the first draft were reworded away before freezing). Shared negative controls 18/18; focused controls 6/6 (H cites a retired key; retired key reused; SOURCES row older than manifest; new TDRG node RID misspelled against the source; stale "needs a ruling" wording reintroduced; RECOG RID misspelled against the source). H→L5 map: every H cites existing L5 rows; no high L5 row without an H.

Fidelity checks done by hand against the tagged owner files (not by the checker): the antipodal fixture state and outcomes, the equivariance counts, the mirror-probe counts (2,661 of 2,703 in 60,000), the K_{2,3} fixture description, the custody states and engine hashes, the RECOG constants (258.4848 / 81.4328, 85.07 / 27.60, 11.13, 0.31, 0.79246 / 0.36915, a ≥ 625, n₀ ≤ 7, 3.5 %) and the c‴_k(a) formula.

## 4. Questions for receiving review

1. TDR-G orientation: do the rewritten `TDRG-DEF-ORIENT` node, the five new nodes and H9 state the v2.12.14 ruling faithfully (tie on S=0 ∧ 2E≡0; G-rule recorded, not adopted; superseded completion named; EV-NOT-RERUN with the census bound) without re-grading anything the owner did not grade?
2. Node renaming: 23 heads moved to owner RIDs with the former atlas label in parentheses — acceptable, or should the old label lead for continuity with the DISC/OFN consumer text?
3. Retirements: any of TDRG.G1–G7 still live in the owner text at `tdrg-v2.12.14`? (Each retirement cites the edit that closed it in the row check §2.)
4. RECOG: are the three extended D3 nodes and RECOG.R-A1 faithful to §6.13a/b and §6.16e — in particular "windows, not identification; no uniqueness; no Q1′ conclusion" and the `[assuming:]` scope — and is R-A1 (a cross-owner dependency on unregistered Dyadic constants) an atlas diagnostic or owner business only?
5. Anything in the 119-line diff outside the scope of §2.

## 5. Publication boundary

Not accepted by this build. Acceptance needs the receiving review, then PI acceptance identifying the bytes `3655d404…3078`, a merge commit (not squash) of `claude/atlas-v0-7` into `main`, and an annotated `atlas-v0.7` tag naming the hash. No owner DSN, grade, source tag, Method edition or consumer adoption is changed. `atlas-v0.6` remains the accepted Atlas until that decision.
