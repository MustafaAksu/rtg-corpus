# Atlas v0.12 — ChatGPT source-impact preparation

**Date:** 11 November 2026. **Status:** [SESSION] co-owner review input, **not** an Atlas v0.12 candidate or acceptance. **Repository:** `MustafaAksu/rtg-corpus`; starting `main` snapshot `c8e71980d053545edcc2f4d1fc5ccf92460de48f` (PR #219 merge). **Responsibility:** Atlas owner Claude prepares and owns the next Atlas source refresh; this is a review-side, change-focused impact map. No adopted Atlas, DSN, Method, pipe or release record is changed by this note.

## 1. Sources and verification boundary

| Input | Governing identity | Read here |
|---|---|---|
| `CONVENTIONS.md` | `main` after PR #219 | Working rules, scope and authority |
| Atlas Method | `atlas/RTG_STATE_ATLAS_METHOD.md`, v0.2 at `atlas-v0.11` | Full method; especially §§3–7 |
| Atlas | `atlas-v0.11`, SHA-256 `8d7a43f05a42c6a69b50eb97b98dd96ddda7eea327333ae5cc73e03dee46f358` | Entire text fetched; programmatic scan and targeted reading of affected L0, D2, D4b, D5 and L5 records (not a full independent semantic reread) |
| Atlas v0.11 manifest | `evidence/atlas/v0.11/source_manifest.json` | All 18 source identities inspected against `BASELINE.md` on `main`; 16 identities unchanged |
| AZ | `az-v0.7`, SHA-256 `2294d2a3287651802824a77ea22fb8f3896f6837cca1162fd8479ff02839fc94`; predecessor `az-v0.6` `dec78a47…0b8a` | `records/az/AZ_v0_7_RELEASE_RECORD.md` §§1–7 and targeted owner DSN header, §§2, 4.1–4.3, 6–9. Tag and `main` Git blobs equal |
| DYAD | `dyad-v6.4.24`, SHA-256 `10fbdacc19544596480acae03faeba076f21103a01b903a8d3305cfa8ed7bc16`; predecessor `dyad-v6.4.23` `9f874cc…25cb` | `records/dyad/RTG_DYADIC_v6_4_24_RELEASE_RECORD.md` §§1–7 and targeted owner DSN §§1–2, 6.1, 6.6, 6.14, 7–8, Appendix E/F; tag and `main` Git blobs equal |
| Thread C intake | `records/az/AZ_UPLOAD_HASH_CHECK_20261111.md` on `main`; PRs #221/#222 | Targeted custody and replay-limit reading; SESSION evidence only |

The v0.11 manifest's 18 source entries were compared with the current full hashes in `BASELINE.md`: only **AZ** and **DYAD** differ. Current adopted tag, release-record SHA and fetched tag/main blob identity were checked for those two. Other 16 editions are hash-unchanged in `BASELINE.md`; that comparison is a **manifest/baseline identity check**, not a fresh independent owner-certificate run. The v0.12 owner must freeze its own snapshot and recheck tag/ref freshness at build time.

**Evidence boundary:** no owner scientific campaign, Atlas builder, `atlas_check.py` or `atlas_preservation.py` was run for this preparation. Source-reported gates and PASS lines are not independently reproduced.

## 2. Required v0.12 source manifest delta

Starting from the 18-entry v0.11 manifest, replace **exactly two** governing source rows (all other input identities retain their bytes):

| Key | v0.11 tag → proposed tag | New tag target (adopted release merge) | New SHA-256 | Authority |
|---|---|---|---|---|
| AZ | `az-v0.6` → `az-v0.7` | `b1c30b7a2d425bd6d7400c49ede0a491b1b2a453` | `2294d2a3287651802824a77ea22fb8f3896f6837cca1162fd8479ff02839fc94` | `records/az/AZ_v0_7_RELEASE_RECORD.md` |
| DYAD | `dyad-v6.4.23` → `dyad-v6.4.24` | `f0af6392ed560b55aedc640bc166f0b87f612f7c` | `10fbdacc19544596480acae03faeba076f21103a01b903a8d3305cfa8ed7bc16` | `records/dyad/RTG_DYADIC_v6_4_24_RELEASE_RECORD.md` |

**Build requirement:** record the new repository snapshot, freeze the full manifest, update the Atlas SOURCES table, and verify source-key coverage, consumer pins and all affected edges. A newer source does **not** automatically repin an intentional older consumer import.

## 3. AZ source impact — adopted v0.7, no new AZ science

The AZ release record certifies a **corrections-only** change (59 logged edits; AZ-owned §4.3 and guards byte-identical). It retains Level A, the static-\(\mathbb Z_N\) classification of the `4|q` angular rule, the bridge disqualification and AZ-OPEN-PROMO/Scope OPENs.

| Atlas v0.11 item | Present problem | v0.12 disposition proposed | Owner check and guard |
|---|---|---|---|
| H2 (L45), high-priority raw diagnostic (L58), AZ.A1 (L1390), UVM cross-reference (L1184/L1260) | Current AZ falsely portrayed as still asserting a certified “legal ×2” correction | **Close AZ.A1** in the review disposition, remove the current-source conflict/false-claim wording from live Atlas; **retain** the UVM negative-deficit and conditional-conversion node and the non-AZ part of H2 | [OWNER: AZ v0.7 §6; OPEN-M v0.7.1 R15/R16]. Two premises are still unproved: source-to-\(\|H\|_B\) identity and \(E\propto A^2\). Historical withdrawn wording may remain in AZ Appendix B but is not a current AZ result |
| AZ.A2 (L594/L1391), DYAD-Q403 consumption (L449), AZ Thread A `*AZ:A-heur` (L465) | q=4,(0,3) formula and Genesis OPEN 1C represented as stale | **Close AZ.A2**; change the live Thread A reference to DYAD's closed `DYAD-THM-Q403-PHASELAW`, and Genesis pointer to `gen-v2.10` as AZ v0.7 does | [OWNER: AZ v0.7 §§4.1.2, 6, 8]. Do not turn AZ's `[import-ref]` into an AZ-owned theorem |
| AZ.A3 (L1392), `*AZ:programme-patch-request` (L1375) | Programme patch reported outstanding although it was already incorporated | **Close AZ.A3**, remove the obsolete open-request representation; retain current registration as a pointer to Programme v1.4 §§6.1, 6.5, 7.1–7.2 | [OWNER: AZ v0.7 §7]. Document placement does not authorize a physical bridge |
| H3 (L46), AZ.A7 (L1394), `*AZ:B-ledger` (L1360), reference-only edges | AZ's historical strings mistaken for owner RIDs | **Close AZ.A7** for current AZ v0.7 uses; update references to `DYAD-ALG-Q3-DEG2-CANCEL`, `TDRG-DEF-ZN-STATE` and the exact TDRG BIND3/OPEN RIDs. **Retain DZT.Q1 and the DZT-only part of H3.** | [OWNER: AZ v0.7 §§4.1, 4.2, 8; DYAD v6.4.24 Appendix F]. `TDRG-ZN-STATE` survives only as an explicitly typed historical consumer alias, not an active phantom RID |
| AZ.A5 (L1393); D5.X3 (L1396) | Similar “divisible by four” vocabulary across different objects | **Retain** as a non-equivalence/bridge guard, with no cross-branch relation promoted | [OWNER: AZ v0.7 SG-AZ-7; DZT SG-DZT-1]. DZT anomaly set and static `4|q` geometry are distinct |
| `*AZ:A-ledger`, `*AZ:A-heur`, `*AZ:B-ledger`, AZ §8 references; L0 SOURCES | v0.11 imports refer to AZ v0.6 and some Dyadic v6.4.8.1 context | Replace **current-use** source pins and scope/grade qualifiers with adopted AZ v0.7; retain historical pins where they really describe an earlier edition or a current consumer's deliberate import | Source-reference-only role; one owner node per claim; no blanket repinning |
| AZ Thread C records, `AZ-ALG-ANTIPODAL-LOWORDER`, `TDRG-AZ-STATIC-ZN-4Q`, guards and OPENs | Same AZ-owned scientific text; evidence availability has changed **after** v0.7 adoption | Preserve claim statements, grades and static-geometry negative result. Mark v0.7 owner evidence state as **source-reported at adoption**, and distinguish the later **SESSION partial recovery**, if cited, without rewriting owner authority | [OWNER: AZ v0.7 §§4.3, 9]; [SESSION: `AZ_UPLOAD_HASH_CHECK_20261111.md`]. Nine of ten AZ-1A/1B registry entries original/hash-equal, tenth report regenerated with matching hash, but Phase-2 harness/outputs and other listed files still unavailable; exporter vs loader/manifest not joined; `G_birth(w)` convention conflict remains open |

**L5 lifecycle rule:** AZ.A1, A2, A3 and A7 retire only after their changed owner assertions are checked at the frozen tag; their identities stay in this versioned disposition record and must not be reused. H2 and H3 are **narrowed**, not deleted wholesale. AZ.A5 persists. The four closed diagnostics are historical evidence, not Atlas v0.12 live faults.

## 4. DYAD source impact — adopted v6.4.24

| Atlas v0.11 item | Required change | Owner scope |
|---|---|---|
| D2 `*DYAD:not-area-preserving` (L316) and DYAD.X4 (L591) | Replace pseudo-ID by registered **`DYAD-ALG-NOT-AREA-PRESERVING`** and grade **ALG**, not the old THM; preserve determinant identity and its non-global scope | [OWNER: DYAD v6.4.24 §§1, 6.1]. Source explicitly retags THM → ALG; no change to the formula |
| D2 `*DYAD:p6-linear-order` (L327) | Replace pseudo-ID by **`DYAD-ALG-P6-LINEAR-ORDER`**, ALG; only the linear multiplier's exact order six, not unique resonance or full dynamics | [OWNER: DYAD v6.4.24 §6.6] |
| D2 `*DYAD:homological-resonance` (L328) | Replace pseudo-ID by **`DYAD-ALG-HOMOLOGICAL-RESONANCE`**, ALG, with the \(a-b-1\equiv0\pmod6\) condition and nonresonant divisor bounds | [OWNER: DYAD v6.4.24 §6.6]; don't confuse order-\(6\) linearization with nonlinear homological resonance |
| DYAD.X4 (L591), `*DYAD:cubic-rate-across-p` (L330) | **Narrow** the D-RID finding to the sole remaining unsigned Dyadic source statement; do not falsely mark the whole DYAD.X4 item closed | [OWNER: DYAD v6.4.24 release §2/X4]. The cubic rate remains an imported RECOG statement without a DYAD RID |
| D2 after `DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER` (L381) | Add **`DYAD-THM-OPEN21-SHARP-ROWS`**, separate `THM·c` node, conditional on **`RECOG-THM-R9-SHARPENED-ROWS`**. In the same declared \(W_0\) and NF-REM row domains: \(\lvert M_W-\mathcal P_2(W_0)\rvert\le K'_j Q_0^{3/2}+C'_{2,j}(256/225)^2Q_0^2\le S_j Q_0^{3/2}\); **A**: \(w_A=3/64\), \(K'_A=3951/1000\), \(C'_{2,A}=259.2\), \(S_A=492/25\); **B**: \(w_B=3/128\), \(K'_B=971/250\), \(C'_{2,B}=81.49\), \(S_B=6357/1000\). `cert` `DYAD-ART-OPEN21-SHARP-ROWS` | [OWNER: DYAD v6.4.24 §6.14]. No mixing of A/B, no `-C7` rows, no unconditional R9 or optimal bound; \(K'_j\) P5 evidence remains missing; older OPEN21 result **unchanged** |
| D2 OPEN 20 frontier (L554 and relevant dependencies) | Register the **SESSION-level** analytic-branch pilot as owner-reported progress: formal curves \(\Gamma_\pm\), Stage-2b finite-radius numerical sectorial difference, negative Stage-3a operator estimate; distinguish from an exact/Stokes certificate | [OWNER statement of SESSION work: DYAD v6.4.24 §2 OPEN 20]. B-an and B-6 stay OPEN; B-∞ smooth existence CLOSED. No certification of analytic divergence or asymptotic exponent, no new theorem RID, no physical claim |
| `DYAD-DEF-PRIMITIVE-MAP` and `DYAD-ART-BRIDGE-NOTE` references | Check the new Programme-scope wording and registered artifact identity; no new map and no physical generator selection | [OWNER: DYAD v6.4.24 §§1, 8]; prior definition formula unchanged |
| Consumer edges | Check `DYAD-THM-OPEN21-SHARP-ROWS` dependency against the **owner's import pin** `recog-v0.3.26` §6.13a (byte-identical relevant entry at v0.3.27); keep the previously recorded intentional older consumer pins | [OWNER: DYAD v6.4.24 §§6.14, 7]. A current owner edition is not an automatic new consumer import |

**New source RIDs to cover:** four results `DYAD-ALG-NOT-AREA-PRESERVING`, `DYAD-ALG-P6-LINEAR-ORDER`, `DYAD-ALG-HOMOLOGICAL-RESONANCE`, `DYAD-THM-OPEN21-SHARP-ROWS`; plus three artifact RIDs `DYAD-ART-OPEN21-SHARP-ROWS`, `DYAD-ART-BRIDGE-NOTE-CHECK`, `DYAD-ART-OPEN20-AN-PILOT`. Artifacts belong in `cert`/evidence references, not as scientific L2 claims.

## 5. Acceptance criteria for the Atlas owner build

1. **Frozen identity:** Source manifest has 18 entries, with 16 unchanged by full SHA-256, exactly AZ and DYAD changed by the hashes above; source table matches. Commit/ref state and release records checked on the date of the actual build.
2. **Coverage:** Every new DYAD scientific RID has a home exactly once, and all three new artifact RIDs have valid certificate/evidence references or a documented unavailability state. AZ's adjusted imports are reference edges, not second scientific homes.
3. **L5 lifecycle:** A1/A2/A3/A7 dispositions justified and removed from current diagnostics; AZ.A5 and DZT.Q1 retained; H2/H3 narrowed only in the changed clauses; DYAD.X4 reduced to the remaining unregistered owner statement (not falsely closed). L5 keys never reused.
4. **Scientific precision:** Conditional OPEN21 theorem carries row/domain/premise and its certificate limitation; no source-reported numerical run becomes THM. OPEN 20 pilot remains SESSION/provisional. No numeric/physical strengthening of AZ `4|q` or OPEN-M ×2.
5. **Edit transparency:** Every changed line and every changed extractor field has a reproducible edit/movement map and a manual disposition of all `DECLARED_PENDING_REVIEW` and context reviews. The v0.11 heading-rename limitation, if triggered, is controlled by an independently checked exact line diff; a comparator PASS alone is not equivalence.
6. **Check/review:** Run `tools/atlas_check.py --manifest evidence/atlas/v0.12/source_manifest.json --atlas atlas/RTG_STATE_ATLAS.md` (0 FAIL required; UNVERIFIED and warnings listed), source coverage checks and change-focused receiving review. No owner proof campaign rerun without a specific discrepancy.
7. **Release guard:** This note is not authorization for Atlas adoption/merge/tag. The Atlas owner prepares the actual v0.12 candidate and release record; PI acceptance precedes the merge commit and annotated `atlas-v0.12` tag.

## 6. Open items not settled by this review

- The exact v0.12 candidate text and source manifest have not been built; possible later owner tags require an impact refresh of this plan.
- `AZ-OPEN-PROMO` and `AZ-OPEN-SCOPE-ARITH` remain OPEN; AZ Action 1 preregistration is SESSION and not an adopted owner result.
- The post-v0.7 Thread C recovery is partial; Phase-2 proof/evidence remains unavailable and its source-grade effects belong to the AZ owner.
- Method v0.3 is a separate proposal, not bundled with this Atlas source refresh.
- The Atlas user's reviewer lane is not changed in this PR; the owner lane remains the Atlas owner's.
