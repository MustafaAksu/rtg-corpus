# RTG Dyadic Oscillator DSN v6.4.21 — release record

**Status:** DRAFT — candidate prepared; **not adopted**. This record is completed at adoption and frozen from then on (Methodology v1.4 §13.7).
**Prepared by:** Claude (atlas owner), at the PI's direction of 22 Oct 2026 to start the pilot. **Owner/PI adoption:** pending.
**Governing methodology:** DSN Methodology v1.4 (tag `methodology-v1.4`).
**Predecessor:** v6.4.20, tag `dyad-v6.4.20`, SHA-256 `0b2d5a44eb818598bb330464dfa4f2e9d75521715f577a7c2e589e165f1a4852`.
**Instructions implemented:** `records/dyad/ATLAS_CLOSEOUT_DYAD_v6_4_20.md` at commit `7856c9e` (closeout with editor finding M14R-05 applied).

## 1. Build stages (branch `claude/dyad-v6.4.21`)

| Stage | Commit | File SHA-256 | Builder | Check |
|---|---|---|---|---|
| Adopted v6.4.20 | tag `dyad-v6.4.20` | `0b2d5a44…4852` | — | — |
| 1 — corrected intermediate (build stage, not an edition) | `649441a` | `0572120aa6ad74b520d8338e10a712838f5a0b97c00f37e921f1915e16f836b5` | `evidence/dyad/scripts/build_dyad_v6_4_21_stage1.py` (25 assertion-gated edits, live text only) | targeted review of the stage-1 diff (pending) |
| 2 — compacted candidate | `a5b1a12` | `31523bd87de9e55dd719a35f4f665caf88608e3dc16f0ecb36a319374104d12d` | `evidence/dyad/scripts/build_dyad_v6_4_21_stage2.py` (19 declared operations) | `tools/check_compaction.py`: PASS |

Reproduce: `git show dyad-v6.4.20:dsn/RTG_DYADIC_OSCILLATOR_DSN.md > v.md` → stage-1 builder → `0572120a…36b5`; then the stage-2 builder with the intermediate and `v.md` → `31523bd8…d12d`. The check reads the v6.4.20 archive through `git show`.

## 2. Changes

**Stage 1 — scientific/scope wording (targeted review required).** Diff: `git diff dyad-v6.4.20 649441a -- dsn/`.

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

No RID added, renamed or regraded. One scope tag changes text (§6.14 primitive-variable form: "remainder not certified" → "remainder certified separately, OPEN 21"); the `[ALG]` grade of the formal expansion is unchanged.

**Not done in stage 1:** S-6a (FA-05 residual): the §1 label "$h_4$ exact over $\mathbb Q(\sqrt3)$" needs the owner check against `normalize_p6_liegauge_exact.py`, which §8 records as a 120-digit numerical script, not exact. S-6b (FB-20 residual) needed no edit: the pointer is already in the §6.11 paragraph.

**Stage 2 — layout only (mechanically checked).** Diff: `git diff 649441a a5b1a12 -- dsn/`. Movement map: `evidence/dyad/v6.4.21/movement_map.json`.
- M01 header: current-only fields; §1 profile exception (E-1); *Supersedes* = v6.4.20 and its hash; Methodology v1.4.
- M03 tag normalization map (v6.4.19→v6.4.20 spellings) left in v6.4.20; M18 Appendix G section map left in v6.4.20 (pointer kept).
- M16 Appendix A: compact entries for v6.4.21 and v6.4.20, one line per earlier edition; full records at tag `dyad-v6.4.20` (E-2). Draft-round records, review verdicts and the 55 replaced release lines are not copied (Methodology v1.4 §13.7: no redundant copies).
- M05, M06, M13, M15 history pointers removed; M02, M04, M07–M12, M14, M17 references repointed to the tagged edition.
- M19 one footer.

**E-1 record correction (for v6.4.20).** The v6.4.20 footer described the r2→final step as "metadata only". That holds for r2→final; the P1 pass earlier in the cycle changed grades of three unnumbered statements: §6.5 historical backbone ansatz `[ALG]`→`[DEF]`; §6.6 $p=6$ linear order `[THM]`→`[ALG]`; §6.6 classification by $p$ `[THM]`→`[DEF]`. Tag-map preservation in the v6.4.20 release was semantic, not textual. Now recorded in v6.4.21 Appendix A. The v6.4.20 release record is not edited.

## 3. Checks

| Check | Extent | Result |
|---|---|---|
| Stage-1 edits applied | each edit asserts a unique match in live text; base hash asserted | PASS (25/25) |
| Stage-1 acceptance search (closeout S-1) | live text searched for OPEN 3, R11, OPEN 21, P4, P2 provenance | no contradicting current status; observation on the "(R11)" label in §1/§6.5 recorded in the completion matrix |
| RAW-CUBIC range | float evaluation, $p=3..24$, of the $z^2\bar z$ coefficient from the cubic Taylor terms vs the displayed formula | agreement $\le5\cdot10^{-15}$ (EV-RUN; not an exact proof; the owner's exact P1-2 check stands) |
| FC-34 | Genesis v2.8.9 §6.3 read | ratio $16/3$, $\kappa_{\rm shear}=-2\sqrt3/3$, $\kappa_{\rm recoil}=-\tfrac12$ (EV-SRC-READ) |
| Compaction | `tools/check_compaction.py` on intermediate → candidate with the movement map | PASS: re-derivation exact; 609 claim blocks in live text, 573 byte-identical, 36 changed by declared operations, 0 unexplained; RID set, heading anchors, source hashes and qualifier tags preserved; references resolve; presentation. Report: `evidence/dyad/v6.4.21/check_compaction_report.json` |
| Negative controls | `tools/test_check_compaction.py` | 12/12 rejected: silent or declared assumption deletion; scope widening; wrong RID association (declared and undeclared); broken links (unknown tag, missing appendix); removed text not in the archive; live results relocated; two footers; hash pin altered; result paragraph deleted. Report: `evidence/dyad/v6.4.21/negative_controls_report.json` |
| Reproduction | builders and checker rerun from repository state | PASS |

Checker limits: byte comparison, regular-expression features; it does not assess semantic equivalence of rewritten prose or prove mathematics (listed in the report). A passing check authorizes nothing.

## 4. Size report (`tools/dsn_lint.py`; informational)

| Metric | v6.4.20 | v6.4.21 candidate |
|---|---:|---:|
| Bytes | 411,765 | 255,492 (−38.0%) |
| Lines | 2,793 | 1,561 |
| Header characters | 3,251 | 2,193 |
| Live body characters | 254,180 | 247,954 |
| Appendix A characters | 150,738 | 3,647 |
| §1 words | 1,434 | 1,466 (profile exception declared) |
| Footer lines | 1 (two-line footer) | 1 |
| New RIDs | — | 0 (growth per new RID: N/A) |
| History phrases in live text (advisory) | historical 49, relocated 8, superseded 11, former 8 | historical 52, relocated 0, superseded 11, former 7 |

Report: `evidence/dyad/v6.4.21/size_report.json`. The remaining "historical"/"superseded" phrases are mostly current statements about historical objects (fits, archival normalizations); they were not reviewed one by one in this pilot.

## 5. Records and closeout state

- Completion matrix (C-1), evidence supplement (C-2), installation read-back (C-4): `records/dyad/DYAD_ADVISORY_v6_4_19_COMPLETION_MATRIX.md`.
- Notices N16–N20 and the v6.4.21 delta N21 (C-3): `records/dyad/DYAD_NOTICES_N16_N21.md` (prepared, not sent; pending consumer decisions do not block adoption).
- Open before the closeout criterion is met: S-6a owner check; C-2 files; sending the notices.

## 6. Adoption

Pending. At adoption: the header status and the Appendix A heading of v6.4.21 become ADOPTED (status lines only), the adopted hash is recorded here, the PR is merged, the PI creates the tag `dyad-v6.4.21`, and `BASELINE.md` is updated.
