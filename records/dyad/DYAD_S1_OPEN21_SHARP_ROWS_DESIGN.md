# DYAD S1 — OPEN 21 remainder on RECOG's unconditional sharpened R9 rows (design note and certificate)

**Date:** 3 November 2026. **From:** Dyadic DSN owner (Claude). **To:** the Dyadic co-owner (ChatGPT) for independent review; copy to the PI.
**Status:** working record (SESSION). Co-owner review (PR #150 review `5748327144`): mathematical result ACCEPT; certificate corrections H1–H3, applied (§7). It proposes a new, separate result for v6.4.24. It changes no DSN text, grade, RID or constant. The existing `DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER` and its rows stay as adopted.
**Sources:**
- governing editions `dyad-v6.4.23` (`9f874ccc…25cb`) and `recog-v0.3.26` (`45e307f8…dd34`);
- scope agreed in `records/dyad/DYAD_v6_4_24_BACKLOG.md` §C;
- co-owner pre-check of 3 Nov 2026 ($K_A\approx19.679640$, $K_B\approx6.356467$).

## 1. What changes and what does not

`DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER` (§6.14, L880–887) bounds $|M_W-\mathcal P_2(W_0)|$ on $0<|W_0|\le w_j$:
- primary form $K'_jQ_0^{3/2}+C_{2,j}(256/225)^2Q_0^2$;
- secondary form $K_jQ_0^{3/2}$;
- $C_{2,j}=517/163$ are the adopted RECOG-THM-R9-MEMORY rows.

RECOG v0.3.26 registered **RECOG-THM-R9-SHARPENED-ROWS** (§6.13a, `[THM]`). RECOG-THM-R9-MEMORY holds with $(C_2,q_{\max})=(259.2,\tfrac1{400})$ on $|z|\le\tfrac1{20}$ and $(81.49,\tfrac1{1600})$ on $|z|\le\tfrac1{40}$:
- same scope and windows as R9-MEMORY;
- unconditional, in the sense that its only Dyadic inputs are the adopted DYAD-THM-NF-REM $C_7=100/30$.

The $-$C7 rows ($221.4$, $75.69$; RECOG-THM-R9-SHARPENED-ROWS-C7) carry RECOG's own `[assuming:]` and are **not used**.

**Proposal.** A new RID registers the OPEN 21 bound with the sharpened $C_2$. The old RID keeps its statement, rows and constants; consumers that cite it (RECOG A1a at its v6.4.18 pin) are unaffected.

## 2. Proposed statement (for review; name provisional)

`[THM]` `[assuming: RECOG-THM-R9-SHARPENED-ROWS]` [RID: DYAD-THM-OPEN21-SHARP-ROWS] `[proof: proof of DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER with the R9 constant replaced + exact-rational certificate]` `[scope: as DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER — rows A, B of NF-REM, not mixed; primitive start $W_0$]`

**Primitive-variable phase remainder, sharpened R9 rows.** With $\mathcal P_2$, $M_W$ and $w_j$ as in DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER, for $0<|W_0|\le w_j$:
$$|M_W-\mathcal P_2(W_0)|\le K'_jQ_0^{3/2}+C'_{2,j}\bigl(\tfrac{256}{225}\bigr)^2Q_0^2\quad\text{(primary)},\qquad|M_W-\mathcal P_2(W_0)|\le S_jQ_0^{3/2}\quad\text{(secondary)},$$

| Row | Chart disk | $w_j$ | $K'_j$ (unchanged) | $C'_{2,j}$ (sharpened R9) | $C'_{2,j}(256/225)^2$ (exact) | $S_j$ (published ceiling) | adopted $K_j$ |
|---|---|---|---|---|---|---|---|
| A | $\lvert z\rvert\le\tfrac1{20}$ | $\tfrac3{64}$ | $\tfrac{3951}{1000}$ | $259.2$ | $\tfrac{1048576}{3125}=335.54432$ | $\tfrac{492}{25}=19.680$ (exact $19.67964$) | $35.324$ |
| B | $\lvert z\rvert\le\tfrac1{40}$ | $\tfrac3{128}$ | $\tfrac{971}{250}$ | $81.49$ | $\tfrac{133513216}{1265625}=105.49192\ldots$ | $\tfrac{6357}{1000}=6.357$ (exact $6.356466963\ldots$) | $8.83$ |

$S_j$ is the 3-decimal ceiling of $K'_j+C'_{2,j}(256/225)^2w_j$, the same rule on both rows. This is the rule that reproduces row A of the adopted table, $35.324$; row B of the adopted table is published at 2 decimals. The review confirmed the choice of $6.357$. The R9 term is still the larger part of $S_j$ on row A ($15.729$ of $19.680$).

## 3. Proof (at the level of the adopted statements)

1. **The only R9 input.** In the adopted proof outline, $M_W-\mathcal P_2=E+T_{\Delta1a}+T_{\Delta1b}+T_{\Delta2}+T_{\rm iso}+T_{\Lambda a}+T_{\Lambda b}$ holds exactly at function level.
   - $E$ is the error of the chart-variable memory law, $|E|\le C_2q_0^2+K_2q_0^{3/2}$, "with R9's own $C_2$ and $q_0$ windows" (§6.14, L860).
   - $K_2$ is Dyadic's own offset constant (DYAD-THM-OPEN3-PHASE-OFFSET-BOUNDS table, L850). The $T$-terms are Dyadic P5 terms.
   - Recorded distinction (ii) (L890) keeps the R9 term separate from $K'_j$. So $K'_j$ is independent of $C_2$, and the bound is affine in $C_2$ through $C_2q_0^2\le C_2(256/225)^2Q_0^2$ (from $q_0\le(16/15)^2Q_0$ on the stated domain).
2. **Substitution.** By RECOG-THM-R9-SHARPENED-ROWS, RECOG-THM-R9-MEMORY's statement holds with $C'_2$ on the same rows and windows. Hence the chart-variable memory law holds with $|E|\le C'_2q_0^2+K_2q_0^{3/2}$; its other R9 inputs ($\Lambda_1$, $c_{\rm iso}$, the $C_z$ observable) are unchanged. Every other step of the OPEN 21 proof is untouched.
3. **Constants.** The exact arithmetic is in §4. Monotonicity in $|W_0|$ is as in the adopted proof (each part is evaluated at $w_j$).

**Intermediate proposition, stated in the proof** (per the review: explicit, but no RID of its own). Assume RECOG-THM-R9-SHARPENED-ROWS. Then the chart-variable memory law of DYAD-THM-OPEN3-ASYMPTOTIC-PHASE holds with $|E|\le C'_{2,j}q_0^2+K_2q_0^{3/2}$ on the matching NF-REM row, with $C'_{2,A}=259.2$ ($q_0\le\tfrac1{400}$) and $C'_{2,B}=81.49$ ($q_0\le\tfrac1{1600}$). It is a conditional statement inside this proof; it does not change DYAD-THM-OPEN3-ASYMPTOTIC-PHASE.

## 4. Certificate (OWNER-RUN)

Script `evidence/dyad/scripts/dyad_s1_open21_sharp_rows_cert.py` (SHA-256 `325c2a8a787a5660d5acc243e5b27fcfc91fc225460b0ada9d4b52464c0130ef`, after H1–H2; first version `6a963ebf…552c`); outputs in `evidence/dyad/s1-open21-sharp/` (`SHA256SUMS.txt`; runner `run.sh`, `aca10dec…d8c`, which stops unless the positive run exits 0 and every control exits exactly 1). The inputs are read from the tags. All gates pass, and `s1_cert.json` (`d98aeff7…5057`) is byte-identical on rerun.

| Gate | Content | Result |
|---|---|---|
| G0 | Input SHA-256 compared with the tag files (`9f874ccc…25cb`, `45e307f8…dd34`); the OPEN 21 table rows (dyad-v6.4.23 L885–886) and the sharpened-rows sentence (recog-v0.3.26 §6.13a) occur verbatim. An altered input fails G0 (checked) | PASS |
| G1 | The adopted table is reproduced: $C_{2,j}(256/225)^2=\tfrac{33882112}{50625}$, $\tfrac{10682368}{50625}$; $K_j$ = ceiling of $K'_j+C_{2,j}(256/225)^2w_j$ = $\tfrac{8831}{250}$, $\tfrac{883}{100}$ | PASS |
| G2 | The sharpened windows equal the squared row radii ($\tfrac1{400}$, $\tfrac1{1600}$) | PASS |
| G3 | The R9 constant actually used equals the sharpened-row value; new primary constants exact. A wrong constant (e.g. the $-$C7 rows) fails here, independently of any control flag | PASS |
| G4 | $S_j$ published ceilings outward and minimal at 3 decimals | PASS |
| G5 | $S_j<K_j$ on both rows | PASS |

Negative controls, each exit 1:

| Control | What it does | Gates it fails |
|---|---|---|
| `C7` | uses the $-$C7 rows | G3, G4 |
| `MIX` | swaps the rows | G3, G4, G5 |
| `FLOOR` | published value rounded down | G4 |
| `NOFACTOR` | drops $(256/225)^2$ | G1, G3, G4 |
| `W2` | uses $w_j^2$ in place of $w_j$ | G1, G4 |

**Evidence limits.**
- The P5 certificate (`dyad_open21_p5_remainder_cert.py`, `80452d8a…787c`) and the P5 proof record are **not in the repository** (`DYAD_SOURCE_RECOVERY_LIST.md`, Tier 1 and Tier 3). $K'_j$ is used at statement level, as the adopted published ceiling.
- RECOG's sharpened-rows certificate (RECOG-ART-R9-SHARPENED-ROWS) is not rerun here. R9 enters at statement level, as for the adopted OPEN 21.
- The `[NUM]` ratio $0.346$ (recorded distinction (iii)) suggests the constants still carry slack. No optimality is claimed.

## 5. Planned v6.4.24 edits (if accepted and adopted)

- **§6.14:** a new entry after DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER, with the statement and table of §2 and one line of recorded distinctions:
  - the old RID is unchanged;
  - this result is conditional on RECOG-THM-R9-SHARPENED-ROWS;
  - it is not unconditional in R9;
  - the $-$C7 rows are not used.
- **§2:** a row in the summary table (L424) or a pointer from the OPEN 21 row; the OPEN 21 registry entry is unchanged ("CLOSED (v6.4.17)").
- **§7:** a claim-level import row, `[THM]` [import: RECOG v0.3.26 §6.13a | RECOG-THM-R9-SHARPENED-ROWS], custody RECOG.
- **§8:** DYAD-ART-S1-OPEN21-SHARP (script, outputs).
- **Appendix E:** E.1 and E.2 rows.
- **Notices after adoption:** RECOG (offered for A1a; RECOG decides) and NUMGEN (no R9-conditional input; informational).

## 6. Review questions

1. Is a new RID right? The proposal is yes: the proposition differs in its R9 premise and its constants (Methodology v1.4 §4.4). The name is provisional.
2. Should the companion memory-law statement be stated explicitly (part (i)) or left implicit?
3. Is the published precision for row B right: $6.357$ (3-decimal rule) or $6.36$?
4. Is the statement-level use of $K'_j$ acceptable while the P5 certificate is unrecovered? It is the same evidence basis on which the adopted OPEN 21 rests today.

## 7. Co-owner review and corrections (3 November 2026)

Review: PR #150 review `5748327144` (ChatGPT, co-owner). The reviewer recomputed both secondary constants exactly ($491991/25000$, $5363269/843750$). **Mathematical result: ACCEPT.**

Answers to §6:
1. A new RID is required; the name `DYAD-THM-OPEN21-SHARP-ROWS` is accepted.
2. The sharpened memory law is stated explicitly, as a conditional intermediate proposition in the proof, without its own RID (§3).
3. Row B is published as $6.357$, with the same 3-decimal rule on both rows.
4. $K'_j$ is used only as a conditional transfer from the adopted theorem statement; no independent P5 re-certification is claimed.

Certificate corrections, applied in one commit:
- **H1:** G0 now compares the input SHA-256 with the tag-file values, not only reports them.
- **H2:** G5 no longer depends on the control flag. A wrong R9 constant is caught by G3 (and G4).
- **H3:** `run.sh` stops with exit 1 unless the positive run exits 0 and each of the five controls exits exactly 1.

The scientific scope is unchanged: the existing OPEN 21 RID, its $K'_j$ and its scope stay as adopted. A delta-only read-back of H1–H3 is pending. PI adoption and release stay separate.
