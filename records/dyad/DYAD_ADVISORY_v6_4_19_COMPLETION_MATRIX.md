# DYAD — completion matrix of the v6.4.19 atlas advisory (closeout C-1, C-2, C-4)

**Date:** 22 October 2026.
**Prepared by:** Claude (atlas owner), for the Dyadic owner and the PI. **Status:** working record, noncanonical. The owner decides; this record proposes the completion state.
**Contract:** `records/dyad/ATLAS_ADVISORY_DYAD_v6_4_19.md` (34 rows). **Pre-implementation decisions:** `records/dyad/ATLAS_DISPOSITION_DYAD_v6_4_19_SESSION_v0_1.md` §8 (ACCEPT 30, REVISE 1, INVESTIGATE 1, DEFER 2). **Closeout:** `records/dyad/ATLAS_CLOSEOUT_DYAD_v6_4_20.md`.
**Editions:** v6.4.20 adopted (`0b2d5a44…4852`, tag `dyad-v6.4.20`); v6.4.21 candidate on branch `claude/dyad-v6.4.21`, round 2 after the targeted review (`records/dyad/DYAD_v6_4_21_TARGETED_REVIEW.md`) — stage 1 commit `6622dcd` (intermediate `f2b20419…9119`), stage 2 commit `6f4a667` (candidate `277e6408…7510`). Round 1 (`649441a`, `a5b1a12`) is in git history. v6.4.21 is not adopted.
**Revision:** working record at a fixed path; one primary state per row (review R21-04).

States (one per row): **DONE v6.4.20** (implemented in the adopted edition) · **DONE v6.4.21** (implemented in the candidate; final at its adoption) · **OPEN** (work remaining, with the next step) · **DEFERRED** (reason and next test) · **RESEARCH** (Tier C, not a maintenance blocker).

## C-1 Completion matrix

| Row | Subject | Decision | State | Where (section / RID / closeout item) | Remaining / reason |
|---|---|---|---|---|---|
| FA-DYAD-01 | §7 dependency description | ACCEPT | DONE v6.4.21 | §7 dependency structure; S-3 | — |
| FA-DYAD-02 | one status per module | ACCEPT | DONE v6.4.21 | §1 OPEN 3 entry, §2 OPEN 3b and OPEN 9 lists, §5 spiral row, §6.14 (three places), §8 DYAD-ART-ATLAS-P2; S-1. Round 2: the R11 label in §1 and §6.5 (RECOG R11 CLOSED; fitted-backbone identification OPEN) | — |
| FA-DYAD-03 | high-risk summaries mirror hypotheses | ACCEPT | DONE v6.4.21 | §1 Lemma F entry (existence pointer), §2 closed list OPEN 19 ($DG(0)=I$); S-1 | — |
| FA-DYAD-04 | VANISH-B2 explanation | ACCEPT | DONE v6.4.20 | §2 OPEN 9, DYAD-ALG-VANISH-B2 | — |
| FA-DYAD-05 | coefficient-field labels | ACCEPT | DONE v6.4.21 | sub-scope: main labels in v6.4.20; S-6a in v6.4.21: §1 "$h_4$ exact over ℚ(√3)" → coefficients in ℚ(i√3) (real parts in ℚ, imaginary parts in ℚ√3); §8 pins the script | Evidence: owner script `normalize_p6_liegauge_exact.py` (`cec918f8…5835`, PI-supplied 22 Oct 2026, now in `evidence/dyad/scripts/`) run here: its 120-digit values match its closed forms to $10^{-100}$ (EV-RUN). Exact: `dyad_h4_archival_exact_check.py` recomputes the degree-4 part of $F^6$ in the script's frame with sympy and matches the four closed forms exactly, $h_4^{(0,4)}=0$ (EV-RUN, exact). The archival object, not the DYAD-ALG-NF6 normalizer (SG-19). |
| FA-DYAD-06 | §6.6 summaries tagged [THM] | REVISE | DONE v6.4.20 | §6.6 retags ([THM]→[ALG], [THM]→[DEF]); recorded in v6.4.21 Appendix A | — |
| FA-DYAD-07 | frame typing of the bridge lemma | ACCEPT | DONE v6.4.20 | §6.9 DYAD-ALG-KP-FRAME-SCALE | — |
| FA-DYAD-08 | RAW-CUBIC statement | INVESTIGATE | DONE v6.4.21 (provenance item open) | §2 OPEN 9, Appendix F; S-5: "formula recovered and algebraically verified; identity with the historical proposition not yet established", range $p\ge3$ | Historical match needs `OPEN9_full_onestep_normalization_table_v2.md` (`af90dc13…700e`), see C-2. Range check: EV-RUN, float evaluation of the coefficient from the cubic Taylor terms against the displayed formula, $p=3..24$, agreement $\le5\cdot10^{-15}$ (this record; not an exact proof). |
| FB-DYAD-09 | DZT/AZ crosswalk | ACCEPT | DONE v6.4.20 | Appendix F | — |
| FB-DYAD-10 | result-level RIDs | ACCEPT | DONE v6.4.20 | 13 RIDs registered at adoption | — |
| FB-DYAD-11 | OPEN 9 projector definitions | DEFER | DONE v6.4.21 (recovery partial) | Appendix D (v6.4.20); §6.11 projector inventory and eigenframe lemma name the eight unrecovered objects, the source and the next step; S-5 | Owner locates the v5.4.x OPEN 9 working files or records them as unrecoverable. |
| FB-DYAD-12 | leading decay vs fitted backbone | ACCEPT | DONE v6.4.20 | §6.5 | — |
| FB-DYAD-13 | smooth equivariant chart export | ACCEPT | DONE v6.4.20 | §6.17 DYAD-THM-SMOOTH-EQUIVARIANT-CHART | Notice N16/N20 (C-3) |
| FB-DYAD-14 | L-PHASE export contract | ACCEPT | DONE v6.4.20 | §7.0a | — |
| FB-DYAD-15 | near-cancellation sign / re-scope | ACCEPT | DONE v6.4.20 | §2 OPEN 9 | — |
| FB-DYAD-16 | edition pins, consumer table | ACCEPT | DONE v6.4.20 | §7.0 | — |
| FB-DYAD-17 | RECOG corrections carried out | ACCEPT | OPEN (records) | C-2 evidence supplement | Files listed under C-2 are not in the repository. |
| FB-DYAD-18 | notice states, one recipient per cell | ACCEPT | DONE v6.4.21 | §7 notices, N11→RECOG row: adopted use; S-2 | RECOG reconciles its own §7.2 mirror (N21). |
| FB-DYAD-19 | outbound notices N16–N19 | ACCEPT | OPEN (prepared, not sent) | `records/dyad/DYAD_NOTICES_N16_N21.md`; C-3 | PI sends; receipt states recorded per recipient. |
| FB-DYAD-20 | UV threshold citations | ACCEPT | DONE v6.4.20 | §1 OPEN-P0 entry; §6.11 DYAD-ALG-P6-FACEFLUX; §6.12 | Residual S-6b: the §6.11 paragraph already carries the `[v6.4.20: Audit-1 = OPEN-M v0.7.1 R16, UVM-RESULT-AUDIT1 … five conditions … GEN-OPEN-UVJET-SCOPE]` pointer in the same paragraph as OPEN-GEN-II-7B; no further edit made. |
| FB-DYAD-21 | route $S_h=j^6R_0$ | ACCEPT | OPEN (prepared, not sent) | N19 (C-3) | PI sends. |
| FB-DYAD-22 | orientation in header and §1 | ACCEPT | DONE v6.4.21 | header (§1 profile exception, current-only fields, one footer); compact Appendix A; E-1, E-2 | — |
| FB-DYAD-23 | notation dictionary | ACCEPT | DONE v6.4.21 | Appendix C ($J_Q$ row corrected; $U$, $\widehat h/h_6/h$, $M(s)$, $\kappa$, $r/r_m$ rows); S-4. Round 2: $U$ row names the start/base-point set and points to the tube $U_T$ | — |
| FB-DYAD-24 | grammar, rendering, anchors | ACCEPT | DONE v6.4.20 | — | — |
| FB-DYAD-25 | $c_\theta^{(6)}$ high-risk cell | ACCEPT | DONE v6.4.20 | §5 | — |
| FB-DYAD-26 | SG-14, export protocol | ACCEPT | DONE v6.4.20 | §3, §7 | — |
| FB-DYAD-27 | OPEN registry hygiene | ACCEPT | DONE v6.4.20 (completed v6.4.21) | §2; the struck "Next required artifacts" line and the two closed items left in the OPEN 9 active list were fixed under S-1 | — |
| FB-DYAD-28 | fixed-point scope at first use | ACCEPT | DONE v6.4.20 | §1 table | — |
| FB-DYAD-29 | claim-to-evidence matrix | ACCEPT | DONE v6.4.20 | Appendix E | — |
| FB-DYAD-30 | constant identities | ACCEPT | DONE v6.4.20 | §6.3 | — |
| FC-DYAD-31 | large-$p$ $q=4,(0,3)$ behaviour | DEFER | RESEARCH | §2 OPEN 9 active list names it | Owner reviews the peer SESSION expansion; coordinate with DZT. |
| FC-DYAD-32 | R9-free existence on U | ACCEPT (research) | RESEARCH | — | SESSION result, not adopted; OPEN 21 keeps R9. RECOG decides H-NG. |
| FC-DYAD-33 | lag-sign corollary | ACCEPT (research) | OPEN (prepared, not sent) | N18 (C-3), base points only | NUMGEN checks anchor indexing and seven-step coverage. |
| FC-DYAD-34 | shear/recoil relation | ACCEPT (reference note) | DONE v6.4.21 | §6.12 export table, shear/healing row: $(4\sqrt3/3)^2=16/3$ = Genesis v2.8.9 §6.3 leading ratio | Verified against Genesis v2.8.9 §6.3 ($\kappa_{\rm shear}=-2\sqrt3/3$, $\kappa_{\rm recoil}=-\tfrac12$, ratio $16/3$; EV-SRC-READ). |

**Count (one state per row):** DONE v6.4.20 18; DONE v6.4.21 10 (candidate; final only at adoption); OPEN 4 (FB-17, FB-19, FB-21, FC-33); RESEARCH 2 (FC-31, FC-32); total 34.

**Pilot engineering residuals (not scientific rows):**
- R21-02 checker false positives (review controls REVIEW-N1–N3): repaired in `tools/check_compaction.py` (reference grammar for substitutions; archive targets resolved in the pinned archive; registered, hash-bound, reviewer-confirmed regions for tag_examples/navigation). Controls 16/16 rejected.
- Regions R1 (tag normalization map) and R2 (Appendix G) in `evidence/dyad/v6.4.21/reviewed_regions.json` await reviewer confirmation; until then the checker result is PENDING.

## C-2 Evidence supplement

None of the requested files is in the repository yet. Their bytes are needed only to inspect them here; their absence means "not independently inspected", not "never done".

| File | Known hash | Where cited |
|---|---|---|
| `DYAD_v6_4_17_v6_4_18_RELEASE_RECORD_ADDENDA_v0_1_1.md` | not recorded here | closeout C-2 |
| `OPEN9_arithmetic_horizon_definitions.md` | `d944ad8c…7c29` | Appendix D |
| `DYAD_RESPONSE_TO_DZT_REQ-002.md` | `0f8c4b15…7dd3` | Appendix D |
| `OPEN9_full_onestep_normalization_table_v2.md` | `af90dc13…700e` | §2 RAW-CUBIC |
| P1 session/working record (`6f30f347…c905`) and the P2 records `DYAD_ATLAS_P2_R2_CORRECTION_SESSION_v0_1.md`, `DYAD_ATLAS_P2_EDITORIAL_INTERFACE_SESSION_v0_1.md` | P1 file hash in v6.4.20 Appendix A | v6.4.20 header, §8 |

Requested action: the PI uploads them to an `upload/…` branch; they are placed under `evidence/dyad/` (sources) or `records/dyad/` (session records) after their hashes are checked against the values above.

## C-4 Installation read-back

- **Repository:** `dsn/RTG_DYADIC_OSCILLATOR_DSN.md` on `main` (commit `72d8a83`) hashes to `0b2d5a44eb818598bb330464dfa4f2e9d75521715f577a7c2e589e165f1a4852`, the adopted v6.4.20 value (EV-HASH, 22 Oct 2026). The tag `dyad-v6.4.20` yields the same bytes.
- **Project knowledge:** the Claude project mirrors `main` through its GitHub sync. Synced files cannot be read back byte-for-byte from this session, so the project-side copy is not hash-checked here; the governing copy is the tagged repository file (Methodology v1.4 §13.9).
- The reviewer's ChatGPT-side copy hashes to the same value; its Git blob `dd1d12f…64d66` matches `main` and `dyad-v6.4.20` (targeted review §5). That verifies the reviewer's copy, not the Claude project sync.
- Separate from the external byte verification of v6.4.20 recorded in the closeout §0.
- Repeat for v6.4.21 after its adoption and merge.
