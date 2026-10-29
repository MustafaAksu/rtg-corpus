# Ontological Foundations v0.11 — atlas row check (candidate `df3c465f…00eb`)

**Date:** 30 October 2026. **By:** Claude, atlas owner (advises; does not adopt). **Object:** PR #112 `claude/ofn-v0.11`, head `ba61f51` (round 2 + ChatGPT receipt): candidate `dsn/RTG_ONTOLOGICAL_FOUNDATIONS.md` SHA-256 `df3c465fb79f049f686f07635d889613e8ab112895cdbcd5af7af029e97400eb` (stage 2, layout only) built from the frozen stage-1 intermediate `9f31badf…a822` (165 logged edits on `ofn-v0.10` `acb70a8c…5dfa`); DRAFT release record `records/ofn/OFN_v0_11_RELEASE_RECORD.md` (`b02172a6…`); change-focused review `records/ofn/OFN_v0_11_CHATGPT_REVIEW.md` and round-2 receipt (PR #112 review `5704839026`, ACCEPT SCOPED, R112-C1/C2/N1 closed).
**Status:** record. **Verdict: ACCEPT FOR ADOPTION (atlas side)**, with one publication condition (§4.1) and four non-blocking remarks (§4.2–4.5).
**Reruns:** `evidence/atlas/rowcheck/ofn_v0_11/` (summary, build/check/tool/guard outputs, content checks, upload check, v0.10 chain replay). Owner sources read at their tags (`EV-SRC-READ`); no owner certificate and no OFN SESSION computation rerun (`EV-NOT-RERUN`).

## 1. Independent rerun (`EV-RUN`, `EV-HASH`)

| Step | Result |
|---|---|
| `git show ofn-v0.10:…` → stage-1 builder | intermediate `9f31badf…a822` and edit log `9dda88f1…bea5` **byte-identical** to the branch files (165 edits) |
| stage-1 checker | K1–K9 PASS; controls C1–C17 caught; output identical to `stage1_check_output.txt` |
| stage-2 builder on the intermediate | candidate `df3c465f…00eb` and movement map `2e9ea570…3fd4` **byte-identical** |
| `tools/check_compaction.py` on `main` (`2ba2a409…7306`) | PASS; output identical to `check_compaction_output.txt` (188/188 claim blocks byte-identical) |
| the same with the PR #113 tool (`a93cec00…6971`) | PASS on the committed map (238 claim blocks with `RTG-OFN-*` now tracked; RID set, hashes preserved); PASS with profile `history_appendix: "C"` (the v0.8 baseline, v0.9 and Draft-2 hashes reported as relocated to Appendix C) |
| owner guards `check_ofn_v0_11_stage2.py --fixtures` | G0–G10 PASS; F1–F14 caught; output identical |
| every hash in release record §2 | recomputed, equal (13 artifacts; round-1 intermediate `cf38b61b…7ce3` at `762d273`) |
| custody upload `upload/ofn-records` `c6fd574` | 20/20 OK; 13 hashes equal to those OFN v0.10 prints; Draft 1 → Draft 2 → `ofn-v0.10` replayed byte-exact from the placed builders (`records/ofn/OFN_UPLOAD_HASH_CHECK_20261030.md`) |

## 2. Content checks against the governing tags (`EV-RUN`; `atlas_ofn_v0_11_checks.py`)

- **Owner RIDs:** 70 distinct owner identifiers in the live text; **63 declared** as `[RID: …]` at `dyad-v6.4.22`, `gen-v2.9`, `tdrg-v2.12.14`, `recog-v0.3.26`, `numgen-v1.21`, `rrf-v0.8.4`, `uvm-v0.7.1`, `programme-v1.3`; the other 7 are owner names or wildcard mentions, not missing RIDs (`NUMGEN-OPEN-REC-HOL-OPERATOR` module label, `NUMGEN-THM-N5AS1-DEFECT-THRESHOLD-RATIO`, `RRF-CND-01`, `RRF-DYAD-W`, `RRF-NET-W-RAW`, and `TDRG-ALG-LEM-*` / `TDRG-DEF-CONV-*` in the alias sentence). No absent identifier.
- **OFN RIDs:** 43 declared, each once (37 of v0.10 + the six DEF RIDs `-ZERO-ORIGIN`, `-DISCRETE-REDUCTION-BOUNDARY`, `-CONTINUOUS-REPRESENTATION`, `-FINITE-DESCRIPTION`, `-DIST-ZN`, `-REDUCTION-TARGET`); none dropped; every mention declared. Status summary "seventeen registered definitions" = 11 + 6 ✓.
- **OPEN registry:** 21 status lines, 20 ACTIVE + 1 PARTIAL, unchanged from v0.10.
- **Residue removed from the live text:** "conditional on DYAD OPEN 20", "existence is not asserted", "real only once", `v2.12.13` — 0 each. "RID unavailable" only in the §11.1 rule sentence and IMP-O08-01 (Genesis registers no zero-origin RID at `gen-v2.9`, verified). "freeze candidate" only inside the §12.1 row that explains it and points to the freeze record. Older pins (Genesis v2.8.5, Dyadic v6.4.12–16, NUMGEN v1.20.7 in Appendix B) are labelled claim-level or historical.
- **Tags:** no dash-compound tag left; every `[RESULT]` tag paired (the one unpaired match is the prose "`[DEF]` and `[RESULT]` records" in §5.5 "Source and status").
- **Cited repository paths** resolve on `main` or on the prerequisite branches: the disposition records (#108, #109), the joint reconciliation (#110), the TDR-G finding item (#111), `upload/ofn-records/`, the freeze record (on `main`).

## 3. Row checks — the 165 edits against the fixed dispositions (joint reconciliation, PR #110)

Every edit is tagged with its row; rows 13, 17, 27 and 29 have no file edit by design (navigation only / no action / notices after the tag / pipe states in PR #110). Statements were checked at the owner lines.

| Row | Edits | Check | Result |
|---|---|---|---|
| 1 class-C realization | R01a–q, R04a | IMP-O10-06/07 restate `DYAD-THM-SMOOTH-EMBEDDING` (E1–E4, uniqueness only among generators with DX′(0)=0) and `DYAD-THM-SMOOTH-EQUIVARIANT-CHART` (Φ=⅙ΣA^{−k}J^k, ΦJ=AΦ, [N_Φ,A]=0, qualitative radius, SG-19, no analyticity) as at `dyad-v6.4.22` L1034–1036 and OPEN 20 L258–266. Five-row regularity table (formal / polynomial C1 / exactly transported C^∞ C2 / analytic OPEN / physical OPEN). The OFN-local `[ALG]` deduction that the lock surfaces of 𝓕_{κ,Φ} are real C^∞ invariant submanifolds: checked — [N_Φ,A]=0 with A³=−I gives N_Φ odd, so Σ N_Φ vanishes on 𝒮₀; ω-equivariance and 1+ω+ω²=0 give the same on 𝒮_±; exact edgewise N_Φ evolution follows. The nine sites restated; OPEN-3B says "C^∞ witness, not closure"; no analytic or physical claim | ✓ |
| 2 test class | R02a, R21g | §5.5.1 regularity becomes real C^∞ germs with real-analytic laws a distinguished subclass; Q6-REG stays local C³; recorded as OFN11-C02 (contract change) — the owners' accept-with-change of I02 | ✓ (remark §4.2) |
| 3 Standard C | R03a–c, R03e, R21g | the corrected `RTG-OFN-DEF-STANDARD-C`: positive-dimensional embedded C³ manifold germ through the null state, invariant as a germ, nonzero edge states arbitrarily near 0, uniform punctured-domain bound ‖I_e‖≤C‖r‖⁴, declared carrier/readout/norm/clock; singleton, finite records, isolated trajectories excluded; coincidence embedding admitted. Its quantifiers now match `RTG-OFN-ALG-RAW-STANDARD-C-NOGO` (positive-dimensional C³ submanifold through 0); class C's 𝒮₀, 𝒮_± satisfy it with I≡0. Old/new text and reason in Appendix B OFN11-C01; the A2 "loopholes" cell replaced by an out-of-test statement; R112-N1 sentence scoped | ✓ (remark §4.2) |
| 4 SG-19 | R04a, R01p | constants edgewise in the dyad chart; qualitative in Φ unless an estimate is supplied; R9 kept as an assumption | ✓ |
| 5 RRF | R05a–d, R01m, G10 | §6.2a row and ψ-readout entry quoted as at `rrf-v0.8.4` L426–437; "OFN adopts that reading at §5.5.4 scope"; no mandatory sign scalar | ✓ |
| 6 κ table | R06a, R01e | one table; κ=2 "not a proved Q6 failure", Genesis γ∈{0,2} OPEN (`gen-v2.9` L855, L903); γ≡κ a parameter convention | ✓ |
| 7 Finding A | S03, R07a–g, R08d | statement accepted / custody deferred to v2.13 / RID stays OFN's, at six sites, as at `tdrg-v2.12.14` L872, L880; R07g changes one inherited historical sentence's tense ("then remained") — acceptable as a §0.3 history line removed in stage 2 | ✓ |
| 8 REQ-O09-05 | R09i, R08a–d, R09o | endpoint component answered at SG-14 scope (canonical branch; finite N=24 check; `largest_center` exception `TDRG-ALG-LARGEST-CENTER-ID-TIEBREAK`); custody component deferred; six-constraint list not recovered; "a fixed-star 2c=0 is not a covariance theorem for all policies" | ✓ |
| 9 TDR-G RIDs | G01, G02, R09a–q, R09-IMP-O08-* | the twelve imports carry the §7-map RIDs (`tdrg-v2.12.14` L892–915); statements unchanged (v2.12.14 is corrections-only for these blocks); legacy names as aliases | ✓ |
| 10 OFN08-C12 | R09j, R09k | "as the owner now also states" — owner LEM-RETRIG wording verified | ✓ |
| 11 §10 token sum | R11a | Σδ changes by −δ_A at a star event (centre δ_A↦−δ_A, newborn δ_E=δ_A: checked) and is preserved by the token permutations; not a gauge of the full model (SG-14); TDR-G's "gauge-like" (SG-3, L446) and "gauge artifact" (§2 L114, App. B L1319) labels referred to TDR-G — the finding item (PR #111) quotes those lines correctly | ✓ |
| 12, 13 NUMGEN | G07, R12a–g | `NUMGEN-RESULT-N5AS1-L-BACKBONE`; q_m := Q_true(T^{6m}x) block-sampled primitive (`numgen-v1.21` L2154–2156); no domain inclusion inferred; §1.1 consumer row at v1.21 | ✓ |
| 14 RECOG | G03, G04, R14a–h | REQ-O09-02 fulfilled by `records/recog/RECOG_v0_3_20_FREEZE_DECISION_PROVENANCE.md` (`5c00f66d…9b55`) with its qualification; imports repinned to `recog-v0.3.26` — the cited formulas (g_k, μ₆(k), S∘T_k∘S=T_{−k}, T∘S_o−S_o∘T=(0,2(cosh ρ−1)), C_pole=e^{iη}, C_→=W̄_aW_b, a₁ sin η) found at the RID blocks | ✓ |
| 15 A1c witnesses | R15a | by exact claim, conditions kept, no event principle, the two v0.3.26-retracted order sentences not cited | ✓ |
| 16 map custody | G06, R16a–i | `DYAD-DEF-PRIMITIVE-MAP` (Dyadic custody, `dyad-v6.4.22` L49), `GEN-DEF-PRIMITIVE-MAP` alias (`gen-v2.9` L31); CUST-O09-01 / REQ-O09-04 closed; R112-C1 applied at IMP-O08-13; DYAD v6.4.10 pins moved to v6.4.22 — `DYAD-THM-PRIM-CTR` bound and tube unchanged at L785–787 | ✓ |
| 18 Q3b ↔ RRF-CND-01 | R18a | `RRF-CND-01` is RRF §6.2 (L403); "necessary, not sufficient" | ✓ |
| 19 notation | R19a–b | χ, N_ch replace ρ, N; formulas unchanged | ✓ |
| 20 Triadic | G08, R20a–e | v1.6.1 repin; pass-two receipt in RF-O08-02 matches `triad-v1.6.1` §7.4; Genesis v2.8.5 pins labelled "not re-read at `gen-v2.9`" | ✓ |
| 21 methodology | H01, H02, S01, S02, R21a–m, F01 | header in v1.4 form; qualifiers `[scope:]`/`[provenance:]` replace the dash spellings; narrow-Q6 single status `[from: ALG]` (v1.4 §3.4; Genesis THM premises in Depends on — admissible, the conclusion is an algebraic deduction); counts twenty-one; R112-C2 "historical integration input" at §5.5 and §12.1 | ✓ (remark §4.3) |
| 22 RIDs | R22a–i | six RIDs inserted in front of unchanged bodies (diff = RID token only); two homeless OPEN blocks pointed to FRUSTRATION/HOLONOMY-RANK and IQP | ✓ |
| 23 pins | G01–G11, H01, S05, R23b–e | governing-editions line in §11.1; repins only where checked | ✓ |
| 24 custody | R24a | §12.1 points to `upload/ofn-records/`; agrees with the hash check | ✓ (condition §4.1) |
| 25 ER-2B | R25a | cites `er2b-v0.3` (`80669c69…a134`) for three uses; the A.4 identities (ΔN = −Σ\|w_e\|⁴ = −½N²+2S² on the closure plane) found at `er2b-v0.3` L74–97; v0.3.1 stays source-reported | ✓ |
| 26 appendix map | S04 | one sentence in §0.4 | ✓ |
| 28 receipts | R28a–d, R07e | DYAD N4/N6/N14 (N6 = `DYAD-THM-LOCAL-INVOLUTION-GERM`, `dyad-v6.4.22` L1119–1120), Genesis IF32, RRF §2.3 guard import of `RTG-OFN-DEF-RANK-TYPING` (`rrf-v0.8.4` L164) and §6.2a | ✓ |

Stage 2: the 16 operations move only history (§0.1, §0.3, §6.4, §9, §12.1/12.2/12.5, Appendix C, footer); the shared tool and the owner guards agree; no claim, RID, grade, status or OPEN changes (§1).

## 4. Conditions and remarks

1. **Publication condition:** the candidate cites records that are on open branches only — PR #108 and #109 (dispositions), #110 (joint reconciliation and the three inbox dispositions), #111 (the TDR-G finding item), and `upload/ofn-records` (no PR yet). All five must be merged (merge commits) before or with PR #112, as the release record §1 says; otherwise the tagged edition would cite identities reachable only through branches. Order: #108, #109, #110, #111, the upload PR, then #112. (#113 is independent; see §4.4.)
2. **RID retention under v1.4 §4.4 (non-blocking):** OFN11-C01 states why `RTG-OFN-DEF-STANDARD-C` keeps its RID (the intended local content is what the no-go excludes — a correction of the same proposition). OFN11-C02 widens the admitted regularity class of `RTG-OFN-DEF-TRIAD-MODEL-CONTRACT` without saying why the RID is kept. Retention is defensible (Q1–Q6 unchanged; the field was declared "not a universal requirement"), but §4.4 asks for the reason to be on record; one sentence in OFN11-C02 or the release record suffices. The consumer notices (§6 of the release record) should name OFN11-C01/C02 to RRF and Genesis as well as to FMS/ER-2B: RRF §6.2a imports this RID, and Genesis IF32 consumes §5.5.
3. **One live draft-tense phrase (non-blocking):** IMP-O10-05 (§11.4, candidate L1286) keeps "not re-verified line by line for this draft" (pass-1 advisory OB-10 listed it). Either reword it at finalization or list it among the kept live-file exceptions; the finalization step as planned touches adoption-state wording only.
4. **Tool (non-blocking):** PR #113 makes `tools/check_compaction.py` track `RTG-OFN-*` and accept `history_appendix`; the candidate passes with it in both forms. Adding `"history_appendix": "C"` to the map is optional; if the owners add it after #113 merges, the candidate bytes do not change — only the map hash and the tool output — and the release record §7 "two tool limits" paragraph can point to the record of PR #113.
5. **Adoption bytes and BASELINE (non-blocking):** the PI adopts `df3c465f…00eb`; the planned finalization changes only the adoption-state lines listed in release record §8 and produces the published bytes, to be confirmed by a checker and by the atlas tag verification (precedent: NUMGEN v1.21, three status lines). BASELINE row OFN is not updated on the branch; at the release it should name v0.11, the published hash, tag `ofn-v0.11` and authority = the v0.11 release record.

## 5. Asked of the PI

Merge #108, #109, #110, #111 and the upload PR (merge commits); adoption of v0.11 on the candidate bytes `df3c465fb79f049f686f07635d889613e8ab112895cdbcd5af7af029e97400eb` with the finalization limited to the release record §8 list; merge #112; annotated tag `ofn-v0.11` on that merge commit naming the published hash. Then: atlas tag verification; owner notices (DYAD, GEN, RRF, TDR-G, NUMGEN, RECOG, FMS/ER-2B, Programme) and closure of the three inbox items; atlas refresh (H1, OFN.O1–O13, DYAD.X1, GEN.D15).
