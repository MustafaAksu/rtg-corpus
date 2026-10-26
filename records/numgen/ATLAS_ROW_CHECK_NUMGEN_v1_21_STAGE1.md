# Number Genesis v1.21 — atlas row check, stage 1 (corrected intermediate `ab25c162…99d2`)

**Date:** 26 October 2026. **By:** Claude, atlas owner (advises; does not adopt). **Object:** PR #74 `claude/numgen-v1.21-stage1`, round-2 intermediate `evidence/numgen/v1.21/stage1_intermediate.md`, SHA-256 `ab25c162a727b0826adfb0b8fd5f3898969ed78260fc00e8bbcaa9e1e3b899d2` (3,471 lines), built from `numgen-v1.20.8` (`835a56f8…817e`) by `evidence/numgen/scripts/build_numgen_v1_21_stage1.py` with 45 logged edits.
**Status:** record. **Verdict: CONCUR — stage 1 implements the reconciled dispositions; nothing blocks stage 2.** One editorial remark (V1), non-blocking.
**Reruns:** `evidence/atlas/rowcheck/numgen_v1_21/rerun_summary.txt`. Owner sources read at their tags (`EV-SRC-READ`); the N-5/C7A/DISC campaigns were not rerun (`EV-NOT-RERUN`), as the hand-over requires.

## 1. Independent rerun

| Step | Result |
|---|---|
| `git show numgen-v1.20.8:dsn/RTG_NUMBER_GENESIS_DSN.md` → stage-1 builder | `ab25c162…99d2`, **byte-identical** to the archived intermediate; edit log `d31eaee0…813d` identical |
| `check_numgen_v1_21_stage1.py` C0–C13 | PASS (C5 five new RIDs, no collision; C6 delta `[THM]+1 [OPEN]−1 [DEF]+1 [RESULT]+1 [from: NUM]+1 [PROVENANCE]−1`; C7 no grade change; C8 one OPEN removed; C9 five imports, `403/250` on 3 lines; C12 labels `U_D,base U_D,tube U_NG U_NG,tube U_R,base`; C13 matrix 8 rows) |
| `--controls` NC1–NC12 | all caught |
| Gate A1 `numgen_v1_21_stage1_checks.py` (ΔQ₅ ≡ P₅, exact sympy) | PASS; `--neg` exits 1. Formula checked against NUMGEN v1.20.8 line 966/975 and DYAD v6.4.22 line 783 (`DYAD-ALG-P5-RADIAL`): identical polynomial |

## 2. Row checks — the 45 edits against the reconciled dispositions (`NUMGEN_OWNER_DISPOSITION_RECONCILIATION_v1_20_8.md` §§2–3)

| Disposition | Edits | Check against the owner sources | Result |
|---|---|---|---|
| NA-02 row-A import | E01–E03 | `[THM] [import: …v6.4.22 §6.14 (producer v6.4.19) \| DYAD-THM-LPHASE-ROWA-REMAINDER]` — Methodology v1.4 line 292 grammar (grade tag, then `[import:]`). (R) `2π − τQ_m + r_m`, `\|r_m\| ≤ (403/250) Q_m^{3/2}` = DYAD line 894/105; (B) `\|W(Ty)/(λW(y)) − 1\| ≤ 0.04654`, `\|δ_T − π/3\| ≤ arcsin ε < π/6` = DYAD line 895; scope "block base points in U_D,base; branch on U_D,tube" = DYAD scope line. Three states in N15 and the §9.1 import row (received / statement accepted / adopted use). `NUMGEN-RESULT-N5AS1-L-PHASE` unchanged; constant only in the import block and the matrix row (C9). Sampled range `[1.3449, 1.3565]` live as `[NUM]` with evidence `90eb6658…6e0b`, `41917710…ee36`, `4100e3a5…f755` — all three hashes present in `upload/numgen-records` (hash-check inventory); DYAD line 905 does cite that range | ✓ |
| NA-01 confirmations, no import | E07–E12 | Acceptance matrix in §9.1: 8 rows, ChatGPT column set, relationship ∈ {independent agreement, consumed theorem, not adopted}; domains "comparison only; no inclusion claimed" (R1). Counterparts exist at `recog-v0.3.24`: `RECOG-THM-A1A-RECIPROCAL-AMPLITUDE` with 15/2 (line 691), `-LIFT-ALIGNMENT` (688), `-PHASE-EXISTENCE-U`, `RECOG-RESULT-A1A-CD-AGREEMENT` on `U ∩ U_NUMGEN` (348), `RECOG-THM-A1B-SLIP-SCHEDULE-U` (B),(C′),(S) with deficit `0.927τQ < Δ < τQ + 1.82Q^{3/2}` (line 43). GAP-LOCK 3 row: ratio limit agreed, digamma schedule not adopted. Three error types separated. Notice row E12 names the inbox item | ✓ |
| NA-03 labels | E04–E06 | `[DEF]` domain table at §6.2 after the `U_T` definition (line 1055): `U_NG` (≡ RECOG's `U_NUMGEN`), `U_NG,tube`, `U_D,base` (Dyadic writes `U`), `U_D,tube` ⊂ {\|W\| < 47/1000}, `U_R,base`; no inclusion asserted; L1 coordinate `U` named as a coordinate; `q_m` ≡ Dyadic `Q_m` guard (NC-18). Exactly the reconciliation §3 resolution | ✓ |
| NB-07/NB-08 RIDs | E13–E18 | Five tier-1 RIDs at their statements (lines of GAP-LOCK 1–3, INF-2, the §6.4 cyclic-average theorem, line 1490); names as proposed, no collision against the 41 existing strings (C5). Identifier-scope guard: module RID points to result RIDs; category word ≠ grade (Methodology §4.2). Tier 2 untouched, as decided | ✓ |
| NA-04 pins | E19–E27 | Programme v1.3 (SG-PROG-1/2, `RTG-OPEN-GENERATOR-SELECTION` exist at `programme-v1.3`); Genesis v2.9 (`GEN-ART-SATURATION` at gen-v2.9 §6.6, lines 629/1104); §7 item 7 Q403 → v6.4.18 (RID present at `dyad-v6.4.22`, 12 occurrences); DZT provenance restated (`dzt-v0.8` governs; no v0.17); E27 `cefb7180…165b` written as prefix…last four (matches the uploaded freeze manifest) | ✓ |
| NC-19 consumers/pins | E11 (second table) | Imports (Dyadic ×2, TDR-G, OFN, Programme, Genesis) / export RECOG / received RECOG; `Pin used` vs `Current companion` separated; Programme IF rows named, not edited | ✓ |
| NA-05, NB-09, NC-12, NC-13, NC-14, NC-16, I06, I11 | E28–E45 | Scope words at N-1 tree / N-1A0 / N-1A1; evidence-state clause with the R2 wording (held records on branch `upload/numgen-records`, reachable at the release commit only if merged first) and six in-ledger keys; SG-NG-23 cross-reading; `DYAD-ALG-P5-RADIAL` alias (gate A1) and relay row; NG-0R-COV conventions, φ* ≟ C_D^ext OPEN; E42 one current RECOG row (v0.3.24) with the HEUR tag, the ALG use and the A1b route, no grade asserted, pipe item named; E44 C7C-M4 HOLD with the TDRG pipe pointer and the sensitivity-audit condition; E45 OFN v0.10 pointer, additive-rank scope (OFN SG-OFN-RANK, line 103) | ✓ |
| NC-17 deferred; NC-18 no bound change; no ALG→THM; no φ* identity; Census-1 unchanged | — | confirmed by C6/C7 and by reading: no edit touches those rows | ✓ |
| Inbox item | PR #74 | `state: dispositioned`, `disposition: 2026-10-26 · accept with change · dsn/RTG_NUMBER_GENESIS_DSN.md §9.1`; `tools/pipes_index.py --check` on the stage-2 tree: OK (7 items, 19 inboxes) | ✓ |

**Methodology v1.4 census.** Every `[RESULT]` in the intermediate is paired with one `[from:]` (183/183 live; the three regex hits without a following `[from:` are the backtick-separated legacy form `[RESULT]\` \`[from: THM]`, lines 67/75/2585, which is paired). No bounded migration needs declaring — unlike Genesis v2.9.

## 3. Remarks

- **V1 (editorial, non-blocking).** E42 writes RECOG v0.3.24's hash as `8c64bea2…69e7c1` (six trailing characters) while E27 fixes the prefix…last-four form for another citation; the file's last four are `e7c1`. Both forms identify the file; the owners may harmonise it in the next edition rather than reopen stage 1 (the publication transform touches status lines only).
- The `[THM] [import: …]` grammar of E01 follows Methodology v1.4 (line 292). NUMGEN's older import rows use `[RESULT] [from: THM] [import: …]` (lines 67, 75); both are tolerated by the checker; a later edition may unify them.
- Nothing in stage 1 touches the C7C algebra, Census-1, the DISC campaigns or any grade (C7).

## 4. Atlas-side notes for the refresh after the tag

D2.L5 NUMGEN rows: N-G1 reworded (RECOG §7 does tag HEUR; NUMGEN now records it); N-D1 explicit-domain confirmations → "acceptance matrix in §9.1, nothing imported"; new RIDs (five) enter the RID vacuum row H4 as closed; H5 (explicit-domain phase existence) → consumer-side confirmation recorded by the producer; H8 (tube naming) → resolved by the §6.2 alias table; N-Q* (q*) stays open pending Dyadic's pipe answer; D5 DISC rows: C7C-M4 HOLD with the TDRG request.
