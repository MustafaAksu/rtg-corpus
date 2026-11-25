# OFN v0.13 DRAFT candidate — Claude co-owner review, 25 November 2026

**Status:** [SESSION] co-owner candidate review. It is not an adoption, a PI decision, a merge or tag instruction, or a pipe-state change. The governing OFN is still `ofn-v0.12`.

**Reviewed:** PR #381, branch `chatgpt/ofn-v0.13-stage1`, head `2cc3af56d3c85a0193c4c9a996d92bdb140d0afe`. The candidate is `dsn/RTG_ONTOLOGICAL_FOUNDATIONS.md`, SHA-256 `7f026a9d3da6c2572281972e7c35c7635fb74888307d9cfe28088087b14613d7`.

**Verdict: ACCEPT WITH CHANGE.**
- There is one required wording correction (N1). It changes one edit payload, so the candidate hash changes.
- Two nits are optional (N2, N3).
- The release record and the Claude entry-note lane need updating with the native replay result and the current checkpoint (N4, N5).
- Everything else in the 145 edits is accepted at the scopes stated in the release record.

## 1. Native reproduction (requested in the release record §2)

Script: `evidence/ofn/scripts/ofn_v0_13_review_claude.sh` with `evidence/ofn/scripts/ofn_v0_13_locators_claude.py`. Output: `evidence/ofn/v0.13_review_claude/review_output.txt`. Environment: Node v22.23.5, Python 3.13.18, in a fresh checkout. The script reads every candidate file with `git show` from the PR head.

| Check | Result |
|---|---|
| R1 native build, `node build_ofn_v0_13.js` from `ofn-v0.12` bytes (`55ff8ba8…76aa`) | BUILD PASS, 145 edits. The candidate and `edit_log.json` are **byte-identical** to the committed files. Node's native SHA-256 of the rebuilt candidate is `7f026a9d…13d7`, so the hand-written JS SHA-256 agrees with it. |
| R2 native checker, Node crypto SHA-256 | `check_output.txt` is byte-identical, C0–C10 PASS. The negative-control output is byte-identical, NC1–NC20 caught. |
| R3 `tools/dsn_lint.py --prev` | Informational: +11,108 bytes (+5.5 %), 8 new external RIDs cited, no near-duplicate paragraphs. |
| R4 `tools/pipes_index.py --check` | `pipes OK: 149 items in 20 inboxes` |
| R5 locators re-resolved from tags, independently of `source_verification.json` | All 22 live `[import:]` locators resolve: the tag exists, every anchor exists and every RID is declared. The pins are `tdrg-v2.13` 11, `recog-v0.3.27` 7, `gen-v2.10` 3 and `dyad-v6.4.24` 1. All 44 `NAME_vX §… #anchor` locators resolve. |

Limitation: C2's "independent rebuild" is part of the builder author's own checker. R1–R2 above are the independent native replay. Neither is a semantic proof; §2 covers the content.

## 2. Content review of the changed claims (against the producer tags)

I read all 145 edits from `edit_map.json` and checked each substantive new text against the cited source. The 100-odd edits that only change a version string (TDR-G 2.12.14→2.13, RECOG 0.3.26→0.3.27, GEN 2.9→2.10, DYAD 6.4.22→6.4.24, Programme 1.3→1.4) are covered by R5 and by the S1/S3/S4 comparisons in PR #379.

| Edit(s) | Claim in candidate | Source check | Verdict |
|---|---|---|---|
| E0986, E0248 (F2) | $\Sigma\delta$ changes by $-x$ at a birth (minus the sum of the centre tokens for simultaneous births); it is invariant under the phase gauge and relabelling; "gauge-like" is withdrawn; the common token shift is outside $G_{\rm cov}$ | `tdrg-v2.13` SG-3 (L428) says $-x \pmod N$; BIRTH-SPECTRUM-INJECTION says $-\sum_a x_a$; SG-14 "Not in $G_{\rm cov}$: (i) the com[mon shift]" | accept |
| E0220, E1057, E0622, E1086 (F3) | Single-star domain; CONV-TICK classification order; ties are path-rule outcomes; tick order unchanged | Matches `tdrg-v2.13` CONV-TICK step 4 and the v2.12.15 `[COR]` (see the reconciliation, R3) | accept |
| E1163, E0248, E0364, E1097 (F3) | §6.13 laws cited reference-only; conditional census interface $c_{t+1}(y)=c_t(y)+b_t(-y)$; $N=24$ owner counterexample | EVENT-INVENTORY (six policies of §6.3), TOKEN-CENSUS-LAW (ii)/(iii), SPECCONS-N, BIRTH-SPECTRUM-INJECTION (old–new $\lvert x_a+y\rvert_c$ and new–new $\lvert x_a-x_b\rvert_c$ entries) and BIRTH-SPECTRUM-NOT-CLOSED ($N=24$, $C=(1,3,4,5)$) all match | accept |
| E1163 (F3) | "one-step sufficient and quotient-minimal for the census output" | Given $c_t$, the map $b_t\mapsto c_{t+1}$ is injective, so $b_t$ carries exactly the information of $c_{t+1}-c_t$. This is trivially true, and the sentence keeps the "not shown that the census determines the selected centres" limit | accept (a SESSION restatement, not graded and not an OFN result, as stated) |
| E1151 (F6, R379-2) | §6.18: the Gram relation is a first-variation coefficient identity, not an exact discrete conservation law; truncated coefficient ODE with $Q_s,Q_c>0$, time in six-step blocks; off-root extension not unique; $D=\mathcal G/Q_s=Q_c(1-K)$ with (b) $\dot D=0$ and (a) $\dot D=rq_1D$; no finite-$u$, global-stability or physical-carrier conclusion; CN-02 requested action | `triad-v1.7` §6.18: "Type of the Gram relation" (first-variation, degree-3 coefficient); boundary tangency; "The off-root extension is not unique"; Remark $D$ with (a)/(b); scope line "Finite-$u$, $r$-dependent and global corrected dynamics are not computed here", "do not establish stability". The CN-02 requested action matches the S2 r2 finding | accept; this meets the R379-2 boundary requirement |
| E1149/E1155/E1185, L665 (F6) | Triadic components repinned to v1.7; Genesis v2.8.5 components keep "(claim-level pin; not re-read at `gen-v2.9`)" | As agreed in the reconciliation §3; C8 guards the GEN text | accept |
| E1249 (F4, P05) | D5B: (D5) discharged by DYAD-THM-LPHASE-ROWA-BRIDGE, DYAD-THM-OPEN3-SPIRAL-REM and RECOG-ALG-A1C-JET-REMAINDER-BOUNDS; D5A not adopted; R9 kept; RECOG-THM-R9-SHARPENED-ROWS is a distinct conditional use | `recog-v0.3.27` status line (D5B), §6.13b and §6.16e present; the three RIDs are declared or imported; release record row D5A "not adopted (variant only)" | accept |
| E1295 (R379-1) | DYAD-THM-OPEN21-SHARP-ROWS (§6.14) is a companion conditional on RECOG-THM-R9-SHARPENED-ROWS, not a replacement; R9 not discharged | `dyad-v6.4.24` L894, in §6.14: `[assuming: RECOG-THM-R9-SHARPENED-ROWS]`, proof "of …PRIMITIVE-PHASE-REMAINDER with the R9 constant replaced" | accept |
| E1074 (F5) | IMP-O08-12: "registered provisional" replaced by the Programme reference-map scope marker, with generator selection open | Matches the PR #379 P06 disposition | accept |
| E1294 (F5/O9) | "for this draft" replaced by a dated limitation: the four current RID blocks match v6.4.22; the v6.4.14/15 historical chain was not re-verified | Matches S1 and ChatGPT's block comparison | accept |
| E0056/E0242/E0246/E1018/E1058/E1146/E1378/E1399/E1420 (F1) | Custody XFER-O08-01 open, a separate decision of both owners; the RID remains OFN's | These are the nine sites in both receiving records. C7/C8 guard against "deferred … v2.13" and "transferred" | accept |
| E1145, E1265, E1143 (NUMGEN delta) | v1.22 §6.6 P2 re-annotation: 158/158 positive controls; DISC-2 40 exposed / 20 changed / 124 PASS, ten labels unchanged; DISC-1 0/22 / 0/22; not a certificate replacement; M-4 HOLD pending approved design/preregistration | `numgen-v1.22` §6.6 L1971 (`[NUM]` P2 re-annotation) and L2047 (`[HOLD]` M-4) match number for number; the record file `records/numgen/NUMGEN_v1_22_S1_P2_REANNOTATION.md` exists at the tag | accept |
| E1394 (NUMGEN) | §9.1 export row confirms the v1.21 reference and vocabulary-only N-1A2 use | `numgen-v1.22` L2813 export row | accept |
| E1393 (NUMGEN) | "NUMGEN v1.22 §9.1 records receipt of OFN v0.11/v0.12 **and the scoped P2 update (RF-O08-01)**" | §9.1 (L2750–2816) records the OFN v0.11/v0.12 receipt (L2782, REQ-O09-03 row). It has **no** P2 or RF-O08-01 row. The P2 re-annotation is a TDR-G orientation consumer update in §6.6, not an OFN receipt | **change, N1** |

## 3. Findings

**N1 — required. E1393 overstates the NUMGEN §9.1 receipt.**
- Replace the clause with: "NUMGEN v1.22 §9.1 records receipt of OFN v0.11/v0.12 (REQ-O09-03 fulfilled; N-1A2 vocabulary only); its separate §6.6 P2 re-annotation is recorded at RF-O08-01."
- One payload changes, so the candidate hash changes.
- The release-record sentence "At §6.6 and §9.1, the owner now records its own scoped P2 re-annotation and OFN receipt/export roles" is accurate as split and needs no change.

**N2 — nit. Origin of the NUMGEN delta.**
- `pipes/OFN/` holds no NUMGEN v1.22 notice; the inbox still lists 12 items: 9 open, 3 closed.
- The delta therefore comes from OFN's own reading of the governing edition, not from a receiving item.
- Suggest one sentence in release record §3 saying so, so that no tenth inbox disposition is expected after the tag.
- The UVM v0.7.2 adoption, also after the checkpoint, likewise sent no OFN notice. Its retained-pin treatment is fine.

**N3 — nit.**
- L631 (RF-O08-07 source report) still cites "TDR-G v2.12.14 §§6.3/6.6" for finite-campaign behaviour, without the "(historical campaign reference)" label that E1179 adds at L1185.
- Adding the same label would make the two uses consistent. It is optional; the pin is a correct claim-level pin.

**N4 — release record §2.**
- Replace "The native CLI adapters have not yet been independently executed … The native informational DSN linter and pipes checker were not run in this session" with a pointer to §1 of this review: native build, checker and controls byte-identical; lint informational; pipes OK.
- After N1 is applied, the rebuild must be rerun. I will rerun the native replay on the new head.

**N5 — entry note, Claude lane.**
- The inserted text is my pre-reconciliation checkpoint, and it still lists "file the S-P4 gate finding to `pipes/FMS/` after reconciliation" as a next step.
- Proposed replacement lane text:

> **25 November 2026 checkpoint (Claude).** Receiving: independent record and joint reconciliation merged (#379; S2 r2 after R379-2). Candidate review of v0.13 DRAFT `7f026a9d…13d7`: `records/ofn/OFN_v0_13_CANDIDATE_REVIEW_CLAUDE_20261125.md` — native build/checker/controls byte-identical, locators re-resolved from tags, content checked against producer tags; ACCEPT WITH CHANGE (N1 E1393 wording). S-P4: gate-adequacy closed only for the two constructed ideals (same-CAS rerun); bilinearity and universal κ open; an FMS notice is not filed and is not a v0.13 prerequisite (PI/FMS owner decide). Next: rerun native replay on the revised head; then PI adoption decision on the exact hash. PI_PENDING: v0.13 adoption.

## 4. Unchanged by this review

- No OFN RID, grade, OPEN status or definition changes.
- No custody transfer, physical selection or FMS regrade.
- The nine OFN inbox items stay open. The post-tag dispositions proposed in the release record §5 are acceptable as proposals.
