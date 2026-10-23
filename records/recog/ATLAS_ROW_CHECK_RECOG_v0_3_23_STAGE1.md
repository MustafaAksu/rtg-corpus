# RECOG v0.3.23 stage 1 — atlas-owner check of the advisory rows

**Date:** 23 October 2026. **By:** Claude (atlas owner). **Status:** review record; advisory, not a decision. **Object:** branch `claude/recog-v0.3.23-stage1` at `4b94723` (PR #19), intermediate `dsn/RTG_RELATIONAL_RECOGNITION_DSN.md` SHA-256 `6a1bdfb062c9233ea56da15760878b73f41f067eea512ddff5ea267b17b4ec06`.
**Scope:** (1) does each row of `ATLAS_ADVISORY_RECOG_v0_3_22.md`, as disposed (reconciliation §5), appear as decided; (2) reproduction of the build and checks. The change-focused review, including the FC-21 verdict, is the co-owner's; §3 below is input to it, not that verdict.

**Verdict:** **ROWS IMPLEMENTED AS DISPOSED — two small corrections requested (A1, A2), one optional.** Nothing blocks the change-focused review.

## 1. Reproduction (independent run, Python 3, `python -I`)

| Item | Result |
|---|---|
| base = `recog-v0.3.22` | `0dcce9e4…bcd9` ✓ |
| builder → intermediate | `6a1bdfb0…ec06`, 116 edits; edit log byte-identical to `evidence/recog/v0.3.23/stage1_edits.json` ✓ |
| builder `--without-fc21` | `5cb31667…4345` ✓ |
| checker with `--controls` | exit 0; output identical to `check_stage1_output.txt` apart from timings ✓ |
| `recog_v0_3_23_value_checks.py` | exit 0; output and JSON byte-identical ✓ |
| `recog_v0_3_23_claim_audit.py` | exit 0; output and JSON byte-identical ✓ |

## 2. Advisory rows

| Row | Edits | Check |
|---|---|---|
| FA-01 (status part) | S616-1…3, S616a-R1, S616b-1, S616c-1 | stale F2 pointers now point to results; compaction left for stage 2 ✓ |
| FA-02 | H-3, S613b-3/4, S7-10…12 | both NUMGEN RIDs at `numgen-v1.20.8`; INF-1 "Depends on" by RID; $U$ vs $U\cap U_{\rm NUMGEN}$ kept; tracking keys and governance text out ✓ |
| FA-03 | S3-1, S3-3, S4-1, S613-2, S614-3 | SG-R10 guard kept; R9 row bound $\lvert M-c_{\rm iso}q_0\rvert\le\lvert G\rvert q_0+C_2q_0^2$; $2C_7q_0^2$ named the partial budget with thresholds on $\lvert G\rvert$; §4 non-chart objects; T1/T2 adopted use ✓ |
| FA-04 | S63-1 | ✓ |
| FA-05 | H-4, S72-1, S73-1…8 | N11 adopted use; consumer editions current; two new consumer rows ✓ |
| FA-06 | H-5…7, S613b-2 | `cdacab5f…f2df` is the `methodology-v1.4` blob ✓ |
| FA-07, FB-20 | S8-1, S8-2 | repository locations; hash-only items listed as in the recovery list ✓ |
| FA-08 | 19 blocks (ledger, release record §3) | 19/19 paired, two splits; grades as owner decisions ✓ — see A1 |
| FA-09 | S5-2 | ✓ |
| FB-10 | S7-2…5, S7-16, S615c-1 | RIDs match `dyad-v6.4.22`; objects without RID named ✓ |
| FB-11 | header, §6.13b, §6.14, §7, §7.2 | five line pins gone; owner tag forms match v6.4.22 byte for byte (`[ALG]` `[scope: formal second order; remainder certified separately, OPEN 21]`; `[THM]` `[assuming: RECOG-THM-R9-MEMORY]`) ✓ |
| FB-12 | S1-1, S1-2, S615-1 | ✓ |
| FB-13 | S1-4/5, S64-1, S69-1, S610-3, S611-1, S613a-2/3 | two new RIDs per PI decision 1; the other items as named sub-statements ✓ |
| FB-14 | S613-1, S613a-1/4/5, S614-3 | $41.2694\ldots$ raw, $59.1194\ldots$ post-$H_2$; $\lvert G\rvert=\sqrt{481897}/90720$; windows $\approx1.4800743\times10^{-5}$, $\approx4.6944689\times10^{-5}$ ✓ |
| FB-15 | S1-3, S2-2, S610-1, S62-1 | ✓ |
| FB-16 | S614-2 | "must not" list in full ✓ — see A2 |
| FB-17, RF-1 | S72-3, S73-6 | no notice state changed; RF-1 is a content state ✓ |
| FB-18 | S2-1, S610-2, S7-6 | ✓ |
| FB-19 | S613b-1 | notation line only ✓ |
| FC-21 | S1-6, S5-1, S613b-14, S7-17, S8-3, A-2 | separate group; `--without-fc21` builds ✓ — §3 |
| FC-22/23/24 | — | deferred or routed; no edits ✓ |
| extras | S2-4 (R10), H-8 (E-0322-1), S616f-1 (VF-1) | ✓ |

## 3. Findings

**A1 — qualifier spelling (correct in stage 1).** S64-2 (v0.3.22 L487) and S66-1 (L548) introduce `[assumes: …]`. Methodology v1.4 (§4 qualifier table; §8.4 alias table) writes the qualifier as `[assuming: …]`. RECOG's own alias table expands `[ALG conditional]` to `[ALG]` `[scope: exact under explicitly listed assumptions]`. Release record §3 row 1 calls the new form the "canonical spelling of the local alias", but it is neither. Use `[assuming: …]` in the two new qualifiers and adjust row 1. The two `[assumes:` already in v0.3.22 can be normalized at the same time or left as they are. `[ALG conditional]` on the new RECOG-ALG-SWAP-ODD-RHO line is a declared local alias and is acceptable.

**A2 — $S_h$ wording (correct in stage 1).** S614-2 says "$S_h$ is not itself an exact commuting involution". The advisory's owner state is that $S_h=h_6\circ(-I)\circ h_6^{-1}$ **is** an exact involution, and only its commutation with $F$ is certified through degree 6. Suggested text: "$S_h$ is an exact involution; its commutation with $F$ is certified only through degree 6."

**A3 — FC-21 (input to the co-owner's verdict).** I re-read the proof against its sources:
- RECOG-THM-A1A-LIFT-ALIGNMENT ($\tfrac\pi6<\delta_T<\tfrac\pi2$ on $U_T$);
- RECOG-THM-A1A-RECIPROCAL-AMPLITUDE (per-block bound $\tfrac{15}2\sqrt{Q_m}$);
- DYAD-THM-LPHASE-ROWA-REMAINDER at `dyad-v6.4.22` (block base points in $U$, row A, primitive $Q$);
- RECOG-DEF-A1A-PHASE-INTERFACE ($M_W:=\Psi_{W,\infty}-\Psi_W(0)$);
- RECOG-THM-A1A-PHASE-EXISTENCE-ALT.

Telescoping, the bound $Q_m-\tfrac1{a+m}=-e_mQ_m/(a+m)=O(m^{-3/2})$, summability of $r_m$, and $\sum_{m<N}\tfrac1{a+m}-\log N\to-\psi(a)$ all check.

The identity $C_D^{\rm ext}=\tau\log Q_0-M_W$ is R9-free in its $W$ form, because $M_W$ is defined directly and EXISTENCE-ALT does not use R9. The chart form with $M(z_0)$ still needs R9 and is correctly listed under "Not supplied". I find no overreach.

**Optional:** §1 line 90 still reads "exists … via RECOG-THM-R9-MEMORY" for CD-IDENTIFICATION, next to the new R9-free sentence. Both are true. A reader may want "(chart form via R9)" there; this can wait for stage 2.

**On the §7.3 question (release record §7).** I agree with the recommendation. A bare `[RESULT]` had no canonical status. Pairing it with the status of its existing load-bearing input grades nothing up or down. `[from: DEF]` for F4 matches its own "prerequisites, not a birth law" guard, and `[from: ALG]` for R9-NO-TOKEN-WRITETHROUGH matches how v0.3.13 introduced it. So: notify on release with the hash. That also fits PI decision 2 (no notice-state work in this release).
