# Discrete Genesis v2.12.14 — atlas row check (candidate `3be72923…2392`)

**Date:** 28 October 2026. **By:** Claude, atlas owner (advises; does not adopt). **Object:** PR #92 `claude/tdrg-v2-12-14-stage1` (head `e3f55c7`, round 2): candidate `dsn/RTG_DISCRETE_GENESIS_DSN.md` SHA-256 `3be72923cd40523399363e0dc044bba6246862d12b2bca190c74969e2cce2392` (1,387 lines) built from `tdrg-v2.12.13` (`aa232643…053f`) by `evidence/tdrg/scripts/build_tdrg_v2_12_14.py` (`71d990b3…286e`) with 105 logged edits; checker `check_tdrg_v2_12_14.py` (`d27b946b…2847`); reference implementation `tdrg_orient_v2_12_14.py` (`ca59e9b9…d59c`); DRAFT release record `records/tdrg/TDRG_v2_12_14_RELEASE_RECORD.md`. ChatGPT change-focused review PR #94: round-2 PASS (R1 SG-14 scope, R2 branch-free C8 closed).
**Status:** record. **Verdict: ACCEPT FOR ADOPTION (atlas side).** One publication condition (§4.1) and two non-blocking remarks.
**Reruns:** `evidence/atlas/rowcheck/tdrg_v2_12_14/` (summary, checker/controls/exhaustive outputs). Owner sources read at their tags (`EV-SRC-READ`); the motif-log and BIND3 campaigns were not rerun (`EV-NOT-RERUN`, PI decision Q3).

## 1. Independent rerun

| Step | Result |
|---|---|
| `git show tdrg-v2.12.13:…` → builder | candidate `3be72923…2392` and edit log `c94ff966…edcb` **byte-identical** to the branch files; 105 edits, 39 new RIDs |
| `check_tdrg_v2_12_14.py` C0–C10 | 11/11 PASS; output identical to the committed `check_output.txt` (C4 39/39 declarations, form OK, no collision; C5 no compound tag left, bare `[RESULT]` 0; C8 engine hash and session-manifest hash OK from commit `386e9d4`; C10 fixture, K_{2,3} fixture, mirror probe and 9,000 random states as expected) |
| `--controls` K1–K8 | all caught; output identical |
| `--exhaustive` | k=1: v18 [72, 72], v2.12.14 [0, 0]; output identical (63 s) |
| Session-scripts upload (`386e9d4`, `upload/tdrg-session-scripts/`) | `SHA256SUMS.txt` 17/17 OK (`00ce64d9…`) |
| Atlas script on the (b) rule (27 Oct, `evidence/atlas/tdrg/`) | inert/(b) policy: 20 of 136 DISC-2 records change, ten labels unchanged — the figure the candidate carries |

## 2. Row checks — the 105 edits against the fixed dispositions (`TDRG_OWNER_DISPOSITION_RECONCILIATION_v2_12_13.md` §3)

| Disposition | Edits | Check | Result |
|---|---|---|---|
| TA-01 / I01 — option (b) | E53, E57, E97 | `TDRG-DEF-ORIENT`: tie on S=0 ∧ 2E≡0 (E∈{0, N/2}) for all n, forward/reversed on 0<\|E\|<N/2, policies unchanged; `TDRG-ALG-ORIENT-NOGO` states the (S,E) reversal invariance and records G as the unadopted alternative with the palindromic caveat; the superseded node-ID completion named with its scope and `[conv: v18 path orientation]`; Appendix B gains the specific [FAIL] row under the general one. Matches the Claude record §1 text and the reconciliation §2.2. | ✓ |
| TA-02 | E53 | `TDRG-DEF-SIGNED-CENTERED` ((−N/2, N/2], named as the source of the stratum), `TDRG-DEF-SIGNED-DEFECT-ERROR` (sign flips under reversal on a defect edge since \|·\| ≤ k < N/6) — agrees with v18 lines 38–55 | ✓ |
| TA-03 / I11 — SG-14 | E32, E91 | group Sym(V) × Z_N^phase; equality modulo relabelling of newborn nodes; token shift and mirror outside; `largest_center` ID tie-break recorded (N1) and `all_centers` scoped; scope sentence per ChatGPT R1 ("on the canonical branch, and on any other policy only once its covariance is separately established"); two OFN entries | ✓ |
| TA-08 / I02 | E79, E84, E90 | §6.12: "mirror-inventory check" wording; `TDRG-ALG-ORIENT-ANTIPODAL-FIXTURE` (θ_pre=(0,11,12), δ=(0,1,12)); `TDRG-NUM-ORIENT-EQUIVARIANCE-N24` (72/72, 168/168; 0; four-node 112 vs 0) with the owner evidence hashes; the atlas census bound block cites my script/JSON hashes correctly (`5684da96…`, `2d15b12f…`) and states the BIND3-IC exposure as undetermined; `TDRG-ALG-MIRROR-NOT-STEP-SYMMETRY` | ✓ |
| TC-14 / I03 | E90, E91 | DISC-2 effect **20 of 136** under (b) (10 / 12 for comparison), ten labels unchanged, 96 unexposed unchanged, DISC-1 NUMGEN's; §7 NUMGEN row; the inbox request `dispositioned · accept · <release record>` with a dated owner line; `tools/pipes_index.py --check` on the branch: OK | ✓ |
| TA-05 / I04 | E10, E38, E65, E67 | "period dividing 2, least period 2 for d≠0, fixed point at d=0"; no aliasing caveat (band < N/3) | ✓ |
| TA-06 / I05 | E81 | "therefore, in particular" + N=24 counterexample; LEM-SPECCONS unchanged under the extended tie (identity) | ✓ |
| TA-04 / I06 | E06, E13–E15, E20, E21, E33, E34, E72, E73 | headline `[NUM]` with full-range scope and window dependence citing the owner's own Exp-0 line (N^{−0.730} on 480–1440); "1.593 ≈ 0.757 + 0.836" withdrawn as `[COR]`; crystallization `[HEUR]` (TDR-22b/23 rows); no refit. Tag census: every `[NUM strong]`/`[HEUR strong]` removal is one of these TA-04 lines or the alias table (E09); no other grade moved | ✓ |
| I07 | E06, E17, E23, E36, E99, E100, E103 | D/F closed at mechanism level, analytic constants OPEN, A→B→C the gate; TDR-24B current line; Appendix C gate aligned | ✓ |
| TA-07 | E37, E98, E101, E102 | K₃ 96:1 and T-6 wedge / x* marked historical continuous references (TRIAD v1.6.1, CN-05) | ✓ |
| TB-09 / I08 | E39–E64 etc. | 36 new claim RIDs in `TDRG-<CAT>-<DESC>` form (Methodology v1.4 §4.2) + 3 ART; consumer names `TDRG-ORIENT`, `TDRG-ZN-STATE`, `CONV-*`, `LEM-*` and the atlas names mapped as aliases in the §7 owner RID map; OPEN-module RIDs untouched; collisions none (C4) | ✓ (form remark §4.2) |
| TB-11 / I08 | E92 | §8 custody register with placed / replayed / held / missing: engine `4c94d874…` placed + replayed for two files (`engine_replay_log.txt`), v18 `9d787b43…` byte-equal to NUMGEN's copy, v17/v16 corpora partly placed / held with the manifest hashes — agrees with `TDRG_UPLOAD_HASH_CHECK_20261027.md`; the four suites and v6 outputs **missing**; `TDRG-ART-SESSION-SCRIPTS` (commit `386e9d4`, manifest `00ce64d9…`); `TDRG-ART-ORIENT-V2-12-14` | ✓ (condition §4.1) |
| TB-10 / I09 / I10 | header, E91 | governing editions named, declared methodology stays v1.2 by PI decision, historical pins kept; §7 imports (OFN statement accepted, custody deferred, REQ-O09-05 answered) / consumers (NUMGEN, OFN, AZ, Genesis blocked) / pins / exports; "RID unavailable" count 2 (both in context text, no load-bearing import) | ✓ |
| TB-12 | E09 and tag edits | compound tags unpacked (C5: none left); alias table replaced | ✓ |
| TB-13 (content part) | header, TDR-24B, App. C | date line, one current TDR-24B statement, Appendix C gate; footer chain and Appendix A ordering left for v2.13 as decided | ✓ |
| TC-16, TC-17, I12 | §6.2, §2, AZ rows | AZ cross-citation, `TDRG-ZN-STATE` alias, the v1.2 owner-review tasks restored in §2 (antipodal tie discharged), AZ 4\|q scoped | ✓ |

**Methodology census.** Declared v1.2 (kept by decision); every `[RESULT]`-type tag carries a grade (C5 "bare RESULT 0"); Appendix A gains one v2.12.14 entry in the existing (v1.2) style; no publication transform needed — the candidate carries no DRAFT marker, so the adopted bytes can be the candidate's.

## 3. Shared tools and side files

`tools/` unchanged. `BASELINE.md` row TDRG already points to v2.12.14 and tag `tdrg-v2.12.14` on the branch — correct once the PR is merged and tagged (the merge commit is the tag target); until then it names a tag that does not exist (remark §4.3). `pipes/TDRG/` request dispositioned by the owners (their ruling, independent of adoption); the notice already `dispositioned · no action`; both to be closed after the tag.

## 4. Conditions and remarks

1. **Publication condition (ChatGPT's, confirmed):** the candidate's §8 and the checker's C8 read commit `386e9d44…` (session scripts) and `c359e21…` (PR #91). Both must be reachable from `main` at the release: **merge PR #91** and **open and merge a PR from `upload/tdrg-session-scripts`** (no PR exists yet; the commit is reachable only through that branch) before or together with PR #92. Otherwise a later branch deletion would orphan an identity the DSN cites.
2. **RID form (non-blocking):** the fixed disposition said "adopt the consumer names `TDRG-ORIENT` / `TDRG-ZN-STATE`"; the build registered `TDRG-DEF-ORIENT` / `TDRG-DEF-ZN-STATE` (Methodology v1.4 §4.2 category form) and mapped the consumer names as aliases in §7. The category form is the right one; consumers resolve through the map. Concur.
3. **BASELINE before the tag (non-blocking):** acceptable because adoption precedes the merge; the atlas verifies the row after the tag as usual.

## 5. Asked of the PI

Adoption of v2.12.14 on the bytes `3be72923cd40523399363e0dc044bba6246862d12b2bca190c74969e2cce2392`; merge order #87, #91, the session-scripts upload PR, #94, #92 (merge commits); annotated tag `tdrg-v2.12.14` on the PR #92 merge commit naming the hash. Then: tag verification by the atlas owner; owner notices to NUMGEN, OFN, AZ and closure of the two inbox items; atlas v0.7 (D5 TDRG rows, D5.X1, H4, H9, N1 row, TC-17 fix, custody notes).
