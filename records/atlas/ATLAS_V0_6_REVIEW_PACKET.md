# RTG State Atlas v0.6 — change-focused review packet

**Date:** 26 October 2026. **Prepared by:** Claude, Atlas owner.
**Status:** DRAFT / NONCANONICAL — candidate for receiving review (ChatGPT, Atlas co-owner); no PI acceptance or owner-science adoption. `atlas-v0.5` governs until acceptance.

## 1. Inputs and identities

Base `atlas-v0.5`, SHA-256 `cf250c9140e6ee26c65b2497a2a61dc1e326a69574d590132f0cea9646a2b0e5`. Source snapshot `origin/main` `38ed5bb` (after PR #78, NUMGEN v1.21 post-tag notices; full id in the manifest). **One moved source: Number Genesis v1.21** (`numgen-v1.21`, tag object `6f1a08a7…`, merge commit `7b77eab848558fdf5fbce46fc4733a415e05ee0d`, file `4805760d683bb3abddfdaab4737f6bb75beed392906bd4c54d8ae79245f15701`; tag verified by the atlas owner 26 Oct: annotated, target = PR #77 merge commit, file hash equal at the tag and on `main`, candidate→published diff = three status lines). The other 17 sources are byte-equal to their v0.5 inputs (manifest `v0_5_input_equality`). Method edition v0.2, unchanged.

| Object | SHA-256 |
|---|---|
| `atlas/RTG_STATE_ATLAS.md` (candidate) | `35ebee6d61f4db93211f2ed6f2de2bb973aa2fc6f2ea3cdf670656b1e961bd8a` (479,995 bytes, 1,544 lines) |
| `atlas/RTG_STATE_ATLAS_METHOD.md` (unchanged) | `fbd2efb34cae6f291d1881cf79f6c521ea337c8a513d92b7d42deb889ed42c04` |
| `evidence/atlas/v0.6/source_manifest.json` | `c4ce6967a34802c780139e08df9653883c6635d16cec399e1c62c947fded17eb` |
| `tools/atlas_check.py` (unchanged) | `0db3a23b9cb78bc87f4b9393baf417c7329421f719f7acbaec2f4ca36626004d` |
| `evidence/atlas/build/refresh_v0_6.py` | `b8cbe56068e81bbfe31fb5ff4a5969af042faffebc5ca5791159d5a321a1ab48` |

Decision basis: the NUMGEN cycle records — `records/numgen/ATLAS_ADVISORY_NUMGEN_v1_20_8_RECONCILIATION.md`, the two owner dispositions and `NUMGEN_OWNER_DISPOSITION_RECONCILIATION_v1_20_8.md`, `ATLAS_ROW_CHECK_NUMGEN_v1_21_STAGE1.md` §4 (atlas-side notes) and `…STAGE2.md`, `NUMGEN_v1_21_RELEASE_RECORD.md` (§§3, 6, 7, 8, 9, 15).

## 2. Review scope

Impact refresh of one domain; 54 exact-once operations (`evidence/atlas/v0.6/edit_log.json`); no other domain re-extracted.

**NUMGEN v1.21 (D2, D3 imports line, D5, H4, H5, H8, H9, cross-domain index).**
- SOURCES row and D2 header to v1.21 (Methodology v1.4 declared; every `[RESULT]` paired — no bounded migration).
- Row-A import executed: the L-PHASE node, the DYAD row-A node's consumer edge, the D2.L3 "phase constants" frontier line and NUMGEN.N-A record the import at §6.6 (pin `dyad-v6.4.22` §6.14, producer v6.4.19; distinct `[THM]` block; NUMGEN-RESULT-N5AS1-L-PHASE keeps its existential tube; 403/250 only in the import block and the matrix row).
- RECOG explicit-domain theorems: recorded as consumer-side confirmations (§9.1 acceptance matrix, 8 rows, three error types, nothing imported) at H5, the INF1 node, the LIFT-ALIGNMENT node, NUMGEN.N-B, N-E, N-SC1; the index "memory and return" line.
- Domain labels: `U_NG`, `U_NG,tube`, `U_D,base`, `U_D,tube`, `U_R,base` (U_NG ≡ RECOG's U_NUMGEN; no inclusion asserted) at H8, the index PRIM-CTR line, the D2.L1 domains heading; NUMGEN.N-S1 retired.
- RIDs: five nodes renamed from `*NUMGEN:` aliases to owner RIDs (GAPLOCK-1/2/3, INF-2, first-nonlinear-average → NUMGEN-RESULT-N5AS1-GAPLOCK-ALPHABET / -COUNT / -SLIP-RATIO, NUMGEN-RESULT-N5AS1-INF2, NUMGEN-RESULT-N3CP-CYCLIC-AVERAGE); H4, the exports line, DYAD-ALG-CUBIC-PARABOLIC's alias and NUMGEN.N-R1/N-R2 updated; tier-2 items listed as still unregistered.
- Pins, aliases, conventions: NUMGEN.N-F narrowed to the declared residue; N-L1 records DYAD-ALG-P5-RADIAL (gate A1); N-L3, N-L5, N-L7, N-G1, N-T2, N-T3 retired with reasons; N-C1 and N-D1 marked owner-stated/declared; N-T1 kept as a declared exception (LOGSLIP block in place; its RID without a live `[RID:]` declaration → checker link UNVERIFIED, documented); NG0R-COV node and N-D/N-L4 record the pinned φ* comparison conventions (identity OPEN).
- Pipes: H5/N-L6 (GEN offer), N-Q* (DYAD question), H9/D5.X1 (TDRG request, C7C-M4 HOLD) cite the filed items by path (receiver undecided); new row NUMGEN.N-I1 lists the five post-tag notices (`state: open`). Builder asserts every cited pipe path exists at the snapshot.
- Retired: NUMGEN.N-S1, N-L3, N-L5, N-L7, N-G1, N-T2, N-T3 (reasons in `dispositions.json`). Reworded: N-A(+DYAD.X10), N-D, N-B, N-E, N-L6, N-L1, N-L4, N-SC1, N-R1, N-R2, N-F, N-C1, N-D1, N-T1, N-Q*, D5.X1. New: N-I1.

Not changed on purpose: RECOG's and the Programme's own pins on NUMGEN v1.20.8 (RECOG-DEF-A1A-PHASE-INTERFACE node, *PROG:IF-register IF14) — owner text; the D3 imports line says "RECOG pins v1.20.8; governing counterpart v1.21".

## 3. Dispositions and mechanical checks

24 touched L5 rows: 7 retired, 16 reworded, 1 new (`dispositions.json`, hashes). Retired keys added to `retired_l5_keys.json`, not reused (guarded). Two builds give identical bytes; reproduce with `python3 -I evidence/atlas/build/refresh_v0_6.py` (asserts base hash, every source tag's hash and commit, tag/snapshot equality, NUMGEN file = `4805760d…5701`, no stale "import deferred / lemmas unnumbered / U/U_T denote both / not imported by v1.20.8" wording, every new RID present in the tagged source as `[RID: …]`, `DYAD-THM-LPHASE-ROWA-REMAINDER]` and `DYAD-ALG-P5-RADIAL` present in NUMGEN v1.21, every cited pipe path present at the snapshot).

Shared checker: **zero FAIL**; PASS sources 72, coverage 128, qualifiers 3, links 423, artifacts 99, keys 91. Carried unchanged from v0.5: 4 link UNVERIFIED + 3 artifact UNVERIFIED, 11 DOCUMENTED-UNRESOLVED, 16 wording WARN (same sites, lines shifted). **One new link UNVERIFIED:** `NUMGEN-CAND-N5AS1-LOGSLIP` — present in NUMGEN v1.21 only inside the `[COR]` historical block; its registration line went to the tag with the changelog (documented at NUMGEN.N-T1). Shared negative controls 18/18; focused controls 6/6 (H cites a retired key; retired key reused; SOURCES row older than manifest; new RID misspelled; stale "import deferred" wording; nonexistent pipe path). H→L5 map: 12 H lines, 130 L5 rows, 0 dangling, 0 high rows without H.

## 4. Questions for receiving review

1. NUMGEN extraction: are the reworded N-A, N-B, N-E and the L-PHASE/INF1/LIFT-ALIGNMENT nodes faithful to NUMGEN v1.21 §6.6 and §9.1 (import states, "comparison only; no inclusion claimed", three error types, custody unchanged)? Anything load-bearing in §6.2 (alias table) or §9.2 (evidence clause) omitted?
2. Node renaming: replacing the five `*NUMGEN:` aliases by the owner RIDs — acceptable, or should the alias be kept beside the RID for continuity?
3. N-I1: is a receiver-side row on open pipe notices an atlas diagnostic, or should the atlas cite pipes only from the receivers' ledgers once dispositioned?
4. Retirements: any of the seven retired rows still live in the owner text?
5. Anything in the 98-line diff outside the scope of §2.

## 5. Publication boundary

Not accepted by this build. Acceptance needs the receiving review, then PI acceptance identifying the bytes `35ebee6d…bd8a`, a merge commit (not squash) of `claude/atlas-v0.6` into `main`, and an annotated `atlas-v0.6` tag naming the hash. No owner DSN, grade, source tag, Method edition or consumer adoption is changed. `atlas-v0.5` remains the accepted Atlas until that decision.
