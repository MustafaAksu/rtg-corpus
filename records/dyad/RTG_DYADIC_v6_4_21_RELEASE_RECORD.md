# RTG Dyadic Oscillator DSN v6.4.21 — release record

**Status:** ADOPTED — PI, 22 October 2026. This record is frozen from adoption; later facts go in a dated addendum (Methodology v1.4 §13.7).
**Prepared by:** Claude (atlas owner), at the PI's direction of 22 Oct 2026. **Receiving review:** ChatGPT, rounds 1 and 2 (`records/dyad/DYAD_v6_4_21_TARGETED_REVIEW.md`; round 2 at commit `0fd07a5`: REVIEW ACCEPTED — OWNER/PI ADOPTION READY). **Owner/PI adoption:** 22 Oct 2026, 22:38 +03:00 (§6).
**Governing methodology:** DSN Methodology v1.4 (tag `methodology-v1.4`).
**Predecessor:** v6.4.20, tag `dyad-v6.4.20`, SHA-256 `0b2d5a44eb818598bb330464dfa4f2e9d75521715f577a7c2e589e165f1a4852`.
**Instructions implemented:** `records/dyad/ATLAS_CLOSEOUT_DYAD_v6_4_20.md` at commit `7856c9e` (closeout with editor finding M14R-05 applied), and the targeted review `records/dyad/DYAD_v6_4_21_TARGETED_REVIEW.md` (ChatGPT, 22 Oct 2026; SHA-256 `6024765c01db2f18a59a874be53c55f26db0766fbccb92385339196f7d4055d6`): stage 1 ACCEPT WITH MINOR EDITS, checker REVISE, pilot NOT READY. Round 2 implements it.

## 1. Build stages (branch `claude/dyad-v6.4.21`)

| Stage | Commit | File SHA-256 | Builder | Check |
|---|---|---|---|---|
| Adopted v6.4.20 | tag `dyad-v6.4.20` | `0b2d5a44…4852` | — | — |
| Round 1 (superseded by round 2; in git history) | `649441a`, `a5b1a12` | `0572120a…36b5`, `31523bd8…d12d` | — | targeted review |
| 1 — corrected intermediate (build stage, not an edition) | `6622dcd` | `f2b20419898ae1c84235a808479391f2d29fc05b2f9a0e46f606539327d29119` | `evidence/dyad/scripts/build_dyad_v6_4_21_stage1.py` (30 assertion-gated edits, live text only) | round 1 ACCEPT WITH MINOR EDITS; round 2 ACCEPT |
| 2 — compacted candidate | `6f4a667` | `277e640819cc35ce5cb664d396cda1feb675589db49a8d21746be568ead47510` | `evidence/dyad/scripts/build_dyad_v6_4_21_stage2.py` (19 declared operations) | `tools/check_compaction.py`: PASS with the reviewer's R1/R2 confirmations (`0fd07a5`) |
| Adopted edition (publication transform, status lines only) | this commit | `a412f34d4db6a6fa92705a5c33334127b3efc3a30a903fecb3c91bd0cf1cdc7d` | `evidence/dyad/scripts/release_dyad_v6_4_21.py` (3 assertion-gated line replacements: header status, Appendix A heading, footer) | diff against the candidate: exactly those 3 lines |

Reproduce: `git show dyad-v6.4.20:dsn/RTG_DYADIC_OSCILLATOR_DSN.md > v.md` → stage-1 builder → `f2b20419…9119`; then the stage-2 builder with the intermediate and `v.md` → `277e6408…7510`. The check reads the v6.4.20 archive through `git show`.

## 2. Changes

**Stage 1 — scientific/scope wording (targeted review).** Diff: `git diff dyad-v6.4.20 6622dcd -- dsn/RTG_DYADIC_OSCILLATOR_DSN.md`; round-2 additions alone: compare with round 1 by `git diff 649441a 6622dcd -- dsn/RTG_DYADIC_OSCILLATOR_DSN.md`.

| Closeout item | Location | Change |
|---|---|---|
| S-1 | §1 OPEN 13 entry | "pending RECOG R11" → permanent non-transfer guard; chart value $+\tfrac{89\sqrt3}{324}$ (RECOG-ALG-CHART-LAWS); R11 CLOSED |
| S-1 | §1 Lemma F entry | existence pointer to DYAD-THM-SMOOTH-EMBEDDING |
| S-1 | §1 OPEN 3 per-block entry | "OPEN 3 is PARTIAL: P4 OPEN" → CLOSED within scope; P4 RID; OPEN 21 |
| S-1 | §2 OPEN 3b | remainder → DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER |
| S-1 | §2 OPEN 9 | closed Q403 and b=5 items moved from Active to Closed; struck artifact line dropped |
| S-1 | §2 closed list, OPEN 19 | "formal tangent-to-identity centralizer ($DG(0)=I$)" |
| S-1 | §5 spiral-residual row | P4 "not implied by the per-block result alone" |
| S-1 | §6.14 recorded distinctions (iii) | P2B v2: coefficient verification complete (exact coefficient equality; no byte identity claimed) |
| S-1 | §6.14 primitive-variable form | scope tag and closing sentence point to OPEN 21 |
| S-1 | §6.14 OPEN 3b distinctions (ii) | remainder certified by OPEN 21 |
| S-1 | §8 DYAD-ART-ATLAS-P2 | "r2 OWNER-RUN" → r2 reviewer replays as recorded at adoption |
| S-2 | §7 notices, N11→RECOG | adopted use by RECOG-THM-A1A-CD-IDENTIFICATION |
| S-3 | §7 dependency structure | self-contained part of DYAD-ALG-OPEN3-PHASE-OFFSET named; R9-dependent expansion separated; native OPEN 9 derivations excluding RECOG imports |
| S-4 | Appendix C | $J_Q$ row corrected; rows for $U$, $\widehat h/h_6/h$, $M(s)$, $\kappa$, $r/r_m$ |
| S-5 | §2 RAW-CUBIC, Appendix F | provenance caveat; range $p\ge3$ |
| S-5 | §6.11 projector inventory, eigenframe lemma | unrecovered definitions named with source and next step |
| FC-34 | §6.12 export table | $(4\sqrt3/3)^2=16/3$ cross-reference to Genesis v2.8.9 §6.3 |
| S-6a (round 2) | §1 OPEN 13 entry; §8 DYAD-ART-NORM-P6 | archival $h_4$: "exact over $\mathbb Q(\sqrt3)$" → coefficients in $\mathbb Q(i\sqrt3)$; script hash pinned; exact recomputation named |
| R21-01 (round 2) | Appendix C $U$ row | start/base-point set $U$; invariant tube $U_T$ |
| R21-01 (round 2) | §1 backbone entry; §6.5 `[OPEN]` entry and historical-fit entry | RECOG R11 CLOSED at its final-chart ledger scope; the fitted-backbone identification remains `[OPEN]`; "§6.5 and SG-19 non-transfer qualifications" |

No RID added, renamed or regraded. One scope tag changes text (§6.14 primitive-variable form: "remainder not certified" → "remainder certified separately, OPEN 21"); the `[ALG]` grade of the formal expansion is unchanged.

**S-6a evidence.** The PI supplied the owner script `normalize_p6_liegauge_exact.py` (SHA-256 `cec918f808cbc02c53beba5f88faf1edbed830a87dac7283e6ac2511d2ec5835`) on 22 Oct 2026; it is now in `evidence/dyad/scripts/`. Run here, its 120-digit $h_4$ values match its printed closed forms to $10^{-100}$ — numerical identification only. `evidence/dyad/scripts/dyad_h4_archival_exact_check.py` (SHA-256 `7617c431aae8a33243541f398ee40afa988f6a0faf254c7f14291561a2c4716c`) recomputes, in the script's frame and with exact sympy arithmetic, the degree-4 part of $F^6$ (all degree-4 channels are non-resonant at $p=6$, so $h_4=V_4$): $h_4^{(1,3)}=\tfrac13+\tfrac{\sqrt3}9i$, $h_4^{(2,2)}=-\tfrac5{24}-\tfrac{11\sqrt3}{24}i$, $h_4^{(3,1)}=-\tfrac16-\tfrac{2\sqrt3}9i$, $h_4^{(4,0)}=-\tfrac1{16}+\tfrac{7\sqrt3}{144}i$, $h_4^{(0,4)}=0$, all exact matches. These lie in $\mathbb Q(i\sqrt3)$, not in the real field $\mathbb Q(\sqrt3)$. This is the archival Lie-gauge object, not the DYAD-ALG-NF6 normalizer (SG-19). The `[ALG]` grade and the $c_\theta^{(6)}$ value of the entry are unchanged. S-6b (FB-20 residual) needed no edit: the pointer is already in the §6.11 paragraph.

**Stage 2 — layout only (mechanically checked).** Diff: `git diff 6622dcd 6f4a667 -- dsn/RTG_DYADIC_OSCILLATOR_DSN.md`. Movement map: `evidence/dyad/v6.4.21/movement_map.json`; region registry: `evidence/dyad/v6.4.21/reviewed_regions.json`.
- M01 header: current-only fields; §1 profile exception (E-1); *Supersedes* = v6.4.20 and its hash; Methodology v1.4.
- M03 tag normalization map (v6.4.19→v6.4.20 spellings; region R1) left in v6.4.20; M18 Appendix G section map (region R2) left in v6.4.20 (pointer kept).
- M16 Appendix A: compact entries for v6.4.21 and v6.4.20, one line per earlier edition; full records at tag `dyad-v6.4.20` (E-2). Draft-round records, review verdicts and the 55 replaced release lines are not copied (Methodology v1.4 §13.7: no redundant copies).
- M05, M06, M13, M15 history pointers removed; M02, M04, M07–M12, M14, M17 references repointed to the tagged edition.
- M19 one footer.

**E-1 record correction (for v6.4.20).** The v6.4.20 footer described the r2→final step as "metadata only". That holds for r2→final; the P1 pass earlier in the cycle changed grades of three unnumbered statements: §6.5 historical backbone ansatz `[ALG]`→`[DEF]`; §6.6 $p=6$ linear order `[THM]`→`[ALG]`; §6.6 classification by $p$ `[THM]`→`[DEF]`. Tag-map preservation in the v6.4.20 release was semantic, not textual. Now recorded in v6.4.21 Appendix A. The v6.4.20 release record is not edited.

## 3. Checks

| Check | Extent | Result |
|---|---|---|
| Stage-1 edits applied | each edit asserts a unique match in live text; base hash asserted | PASS (30/30) |
| Stage-1 acceptance search (closeout S-1) | live text searched for OPEN 3, R11, OPEN 21, P4, P2 provenance | no contradicting current status |
| RAW-CUBIC range | float evaluation, $p=3..24$ (this preparer); exact symbolic identity for all integer $p\ge3$ via $t=\tan(\pi/p)$ (reviewer, SESSION) | PASS; does not settle the historical identity |
| S-6a | owner script run; exact sympy recomputation | PASS (EV-RUN; exact) |
| FC-34 | Genesis v2.8.9 §6.3 read; reviewer ratio check | $16/3$ (EV-SRC-READ; reviewer PASS) |
| Independent reproduction (round 1) | reviewer applied both diffs to v6.4.20 and replayed the checker | hashes and positive report byte-identical |
| Compaction (round 2) | `tools/check_compaction.py` on intermediate → candidate with movement map and region registry | **PASS** with the reviewer's R1/R2 confirmations (PENDING before them): re-derivation exact; 609 claim blocks in live text, 573 byte-identical, 36 changed by declared operations, 0 unexplained; RID set, heading anchors, source hashes and qualifier tags preserved; 27 archive targets resolved in the pinned v6.4.20; presentation passes. Reviewer replay reproduced both the PENDING and the PASS results. Reports: `evidence/dyad/v6.4.21/check_compaction_report.json`, `round2_receiver_verification.json` |
| Negative controls (round 2) | `tools/test_check_compaction.py`, with region confirmations simulated | 16/16 rejected, including the reviewer's REVIEW-N1 (hypothesis deleted as a reference edit), REVIEW-N2 (nonexistent H-999), REVIEW-N3 (live §6.7 relocated as tag examples) and its registered-region variant. Report: `evidence/dyad/v6.4.21/negative_controls_report.json` |

| Receiving review, round 2 | ChatGPT: stage-1 round-2 delta, S-6a (including an alternative rational composition, 10/10), R1/R2, checker replay, 16/16 controls | ACCEPT; adoption ready at the reviewed maintenance/pilot scope |
| Publication transform | diff candidate → adopted file | 3 status lines changed; no other byte |

Checker limits are listed in its report. A passing check authorizes nothing.

## 4. Size report (`tools/dsn_lint.py`; informational)

| Metric | v6.4.20 | v6.4.21 candidate |
|---|---:|---:|
| Bytes | 411,765 | 256,463 (−37.7%) |
| Lines | 2,793 | 1,561 |
| Header characters | 3,251 | 2,193 |
| Live body characters | 254,180 | 248,669 |
| Appendix A characters | 150,738 | 3,899 |
| §1 words | 1,434 | 1,500 (profile exception declared) |
| Orientation core (§1–§4) | 41,502 chars, 4,997 words | 42,126 chars, 5,059 words; `AI_CONTEXT_CORE_END` present |
| Footer lines | 1 (two-line footer) | 1 |
| New RIDs | — | 0 (growth per new RID: N/A) |
| History phrases in live text (advisory) | historical 49, relocated 8, superseded 11, former 8 | historical 53, relocated 0, superseded 11, former 7 |

Counting method: in `evidence/dyad/v6.4.21/size_report.json`. The remaining "historical"/"superseded" phrases are mostly current statements about historical objects (fits, archival normalizations); they were not reviewed one by one in this pilot.

## 5. Records and closeout state

- Completion matrix (C-1), evidence supplement (C-2), installation read-back (C-4): `records/dyad/DYAD_ADVISORY_v6_4_19_COMPLETION_MATRIX.md`.
- Notices N16–N20 and the v6.4.21 delta N21 (C-3): `records/dyad/DYAD_NOTICES_N16_N21.md` (prepared, not sent; pending consumer decisions do not block adoption).
- Retained limitations, open after adoption (closeout criterion, not adoption): C-2 source files; sending N16–N21 and recording their states; installation read-back of v6.4.21; atlas refresh. Advisory completion and consumer synchronization are not claimed. The historical identity of DYAD-THM-RAW-CUBIC remains unresolved.

## 6. Adoption

- **Decision:** PI (Mustafa), 22 October 2026, 22:38 +03:00, in the Claude session that prepared the release: "Bende DSN documanını bu kaliyle benimsiyorum." (verbatim) (I adopt the DSN document as it stands.) Given after the round-2 receiving review (REVIEW ACCEPTED — OWNER/PI ADOPTION READY).
- **Adopted file:** `dsn/RTG_DYADIC_OSCILLATOR_DSN.md`, 256,508 bytes, SHA-256 `a412f34d4db6a6fa92705a5c33334127b3efc3a30a903fecb3c91bd0cf1cdc7d`. The candidate hash `277e6408…7510` identifies the reviewed candidate only.
- **Scope:** the reviewed maintenance/pilot scope: closeout S-1–S-6, FC-34 and the Methodology v1.4 compaction. No RID added, renamed or regraded.
- **Publication:** merge of `claude/dyad-v6.4.21` into `main` (merge commit, not squash), then the annotated tag `dyad-v6.4.21` created by the PI with this hash in its message. `BASELINE.md` lists v6.4.21 as the governing edition.
- **Notices:** N16–N21 are prepared (`records/dyad/DYAD_NOTICES_N16_N21.md`) and sent by the PI; N21 cites the hash above.
