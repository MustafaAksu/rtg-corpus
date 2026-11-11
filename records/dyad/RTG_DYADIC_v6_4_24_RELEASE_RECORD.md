# RTG Dyadic v6.4.24 — release record

**Status:** DRAFT — candidate r2, 11 November 2026. Reviewed by the co-owner at r1 (changes requested, R1–R6); r2 awaits the read-back. Not adopted. The PI decided on 11 November 2026 to start the candidate ("başlayalım"); adoption is a separate decision after the co-owner's review.

## 1. Candidate

| Item | Value |
|---|---|
| File | `dsn/RTG_DYADIC_OSCILLATOR_DSN.md` on branch `claude/dyad-v6.4.24` |
| Candidate SHA-256 | `014e1ac3be8c21d0e70afb72f23f7592528b01ffc5cd6390628721cc69e98958` (r2; 285 275 bytes). r1 was `7f22ea3511d24170036dc2ec318d630f1d95d7e007deec3ad82ec7623a882327` (283 385 bytes; commit `c9b54e3`) |
| Base | `dyad-v6.4.23`, `9f874ccc1cd684482f26a27fca13b37102977cba2a80a75e762ecd7b300425cb` |
| Scope | `records/dyad/DYAD_v6_4_24_BACKLOG.md` §A, §B, §B2, §C, §C3 |
| Kind | single stage, no compaction; 38 assertion-gated edits (r1: 34); four result RIDs and three artifact RIDs added; one displayed grade tag retagged (X4); no statement, constant or OPEN status changed |

## 2. Content

| Group | Edits | What changes | Source |
|---|---|---|---|
| S1 | S1-1 to S1-3 | New result `DYAD-THM-OPEN21-SHARP-ROWS` `[assuming: RECOG-THM-R9-SHARPENED-ROWS]` in §6.14: S_A = 492/25, S_B = 6357/1000, with recorded distinctions; pointers in the header summary and in the OPEN 21 registry entry. The adopted `DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER` line and table are byte-identical | S1 design record; co-owner reviews `5748327144`, `5748500129` (PR #150) |
| X4 | X4-1 to X4-4 | RIDs registered for three existing statements: `DYAD-ALG-NOT-AREA-PRESERVING` (§6.1, cited in §1), `DYAD-ALG-P6-LINEAR-ORDER`, `DYAD-ALG-HOMOLOGICAL-RESONANCE` (§6.6). The first is retagged `[THM]` → `[ALG]` in both places; the history of the retag is in the Appendix A entry, not in the live tags | Atlas DYAD.X4; backlog §B |
| R1 | R1-1 | §7 claim-level import row `[RID: RECOG-THM-R9-SHARPENED-ROWS]` in the Methodology §4.3 format (source status, depends on, verification, synchronization) | co-owner review R1 |
| B2 | B2-1, B2-2 | `DYAD-DEF-PRIMITIVE-MAP`: "provisional" replaced by a `[scope:]` note. `DYAD-ART-BRIDGE-NOTE`: path, hash, availability, and the K = 1 remark | backlog §B2; `DYAD_UPLOAD_HASH_CHECK_20261103_BRIDGE_NOTE.md` |
| S3 | S3-1 | One `[SESSION]` paragraph in the OPEN 20 entry on the analytic-branch pilot: stage 1 (exact; the P′(u) identity as a SESSION owner-run finding, with no `[ALG]` tag), the published literature basis with its limits, stage 2 (`[NUM]`), stage 3a (negative), stage 2b (`[NUM]`: the two sectorial values differ numerically; nine finite-radius slopes consistent with e^{−2πT}). It claims no result | PI instruction of 3 Nov 2026; design record §8, §9; stage-2b record |
| ART, E | ART-1, E-1, E-2 | §8: `DYAD-ART-OPEN21-SHARP-ROWS`, `DYAD-ART-BRIDGE-NOTE-CHECK`, `DYAD-ART-OPEN20-AN-PILOT`. Appendix E.1 and E.2 rows for the four result RIDs | — |
| REG, F | REG-1 to REG-12, REG-9b, F-1, F-2 | §7.0 rows and §7 lines to RECOG v0.3.27, Genesis v2.10 (pin exceptions spelled out), Triadic v1.7, Programme v1.4, AZ v0.7; notice-table sentence; Appendix F re-read at `az-v0.7` (14 rows for its 16 strings). The AZ v0.6 crosswalk is not kept in the live appendix; it is in Appendix F of `dyad-v6.4.23` | `DYAD_INBOX_20261111_OWNER_DISPOSITION.md`; `BASELINE.md` |
| ED | ED-1 to ED-9 | title, date, status, supersedes, release record, Appendix G note, footer, Appendix A entry, own §7.0 row | — |

**Not in this edition:** the §1 compaction; S2 (L-PHASE row B); any OPEN 20 result; a DYAD RID for RECOG's c_J and c_7; a RID for the cubic radial rate across p.

## 3. Build and checks (OWNER-RUN, 11 November 2026)

Scripts in `evidence/dyad/scripts/`; outputs in `evidence/dyad/v6.4.24/` (`SHA256SUMS.txt`).

| Script | SHA-256 | Result |
|---|---|---|
| `build_dyad_v6_4_24.py` | `befdea1f3fef85ba8c8da48eef464ce4af4831418b11626ec58eabd06b364815` | 38 edits, each old text found exactly once; output `014e1ac3…8958` |
| `check_dyad_v6_4_24.py` | `efc73aec1c6ee87bc21212ec3801f5f241f75217461d7487eadaa56299b0c420` | C0–C11 all PASS |
| `check_dyad_v6_4_24_controls.py` | `9bbac86f65dda9c469dcc18570309d362a4753c699b572b5b02b333561c588e3` | Q1–Q17 each exit 1 at the expected gate (Q13–Q17 are the r2 controls) |

Gates:

| Gate | Content |
|---|---|
| C0, C1 | base identity; the candidate is the build output; two clean builds are byte-identical |
| C2 | confinement: undoing the 38 logged edits gives the base byte for byte; Appendix A kept, one entry inserted |
| C3 | every RID of the base kept; exactly the seven declared RIDs and the one §7 import tag added; the only removed grade tags are the two `[THM]` of the declared retag; no "v6.4.24: …" commentary in a live tag; every changed math span belongs to a logged edit |
| C4 | adopted OPEN 21 constants kept; S_A and S_B recomputed as three-decimal ceilings in exact fractions; superseded register wordings absent |
| C5 | the adopted OPEN 21 result line and rows are byte-identical to the base; the new entry carries its assumption and import pin; RECOG's `RECOG-THM-R9-SHARPENED-ROWS` entry is byte-identical at `recog-v0.3.26` and `recog-v0.3.27` |
| C6, C7 | edition lines; §2 "Status:" lines identical to the base |
| C8 | every script, source and output hash cited in the new §8 entries equals the repository file; the cited outputs report all_pass |
| C9 | exact spot checks: det DT; order of λ; resonance condition; P′(u) = α(c₄₀ + μu); the stage-2b figures against `jump_scout.json` and the nine slope ratios against `jump_law.json`; the bound 1.76·10⁻⁶ recomputed (1.7596·10⁻⁶) |
| C10 | the AZ rows of Appendix F list exactly the 16 Dyadic-pattern strings of `az-v0.7`; each is an owner RID except `DYAD-OPEN-B5-ALLP` (closed lifecycle item) and `DYAD-ALG-Q3-CANCEL` (historical mention); no AZ v0.6 row is left |
| C11 | the five register hashes equal `BASELINE.md` and the files at their tags |

`tools/dsn_lint.py`: informational report in `dsn_lint.txt` (one footer line; Appendix A at most 297 words per edition). `tools/pipes_index.py --check`: OK.

## 4. Review of r1 and the r2 corrections

Co-owner review of r1: PR #213, review `5856200509` (11 November 2026). Verdict: conditional scientific acceptance; document and import corrections required before a PI adoption decision. The review was filed as a comment because the PR was opened from the reviewer's account.

**Accepted at r1 (unchanged in r2):** the S1 result and its assumption; the three X4 RID names; the retag `[THM]` → `[ALG]` with its history in Appendix A; the primitive-map scope note; the exact identities 2A = αμ and B = αc₄₀; the stage-3a bound as chart-relative.

| Item | Request | r2 |
|---|---|---|
| R1 | a claim-level §7 import row for `RECOG-THM-R9-SHARPENED-ROWS` in the §4.3 format | added (edit R1-1); the `RECOG-THM-R9-MEMORY` row keeps its pin |
| R2 | do not promote P′(u) = α(c₄₀ + μu) to `[ALG]` inline, or declare it as a new adopted conclusion; cite published works, with LIT identifiers only in verification records | kept as "an exact owner-run finding at SESSION scope, not registered as a result of this ledger"; the three works are cited by authors, title, journal, volume, year and pages, with the arXiv version actually read; LIT identifiers removed from the DSN text |
| R3 | state the stage-2b law as consistency of finite-radius slopes, with the object, branch, overlap and direction named | done: "one branch (Γ₊), one overlap (S₀ ∩ S₁) and one direction (arg ξ* = π/6), with no certified truncation bound"; ΔY = Δw/z*²; "the nine local slopes … between the ten radii … are consistent with e^{−2πT} after the stated prefactor (ratio 0.984 to 0.9988); no asymptotic exponent is certified". The review wrote "ten slopes"; ten radii give nine slopes |
| R4 | Appendix F: current `az-v0.7` view, no historical AZ v0.6 overlay | the 11 AZ v0.6 rows are replaced by 14 rows for the 16 strings of `az-v0.7`; the v0.6 crosswalk stays in `dyad-v6.4.23` |
| R5 | the Genesis export bullet must not say that all rows pin v6.4.13 | rephrased from Genesis v2.10 §7: v6.4.13 for the historical rows, except `DYAD-ALG-NU5-P5` at `dyad-v6.4.23`; the two smooth rows at `dyad-v6.4.22` |
| R6 | version commentary out of live §1/§6 tags | removed from the four X4 tags and the primitive-map note; the Appendix A entry carries it |

Not rerun for r2, as agreed in the review: the S1 certificate, the stage-2b campaign, RECOG's evidence. Their recorded outputs are read by gate C8.

**Open dependencies (nonblocking):** NUMGEN and OFN have not answered the v6.4.23 notice; their rows are unchanged. The P5 proof source of the adopted OPEN 21 result is still missing; S1 uses K′_j at statement level.

## 5. Reviews and decision

| Step | Record | Verdict |
|---|---|---|
| Co-owner change-focused review of r1 (`c9b54e3`, `7f22ea35…2327`) | PR #213 review `5856200509` | scientific core accepted; corrections R1–R6 requested |
| r2 (`014e1ac3…8958`): R1–R6 applied | this record §4 | — |
| Co-owner read-back of r2 | — | pending |
| PI decision | — | pending |

## 6. Publication

Pending adoption. Planned, as for v6.4.23: a status-lines-only transform of the reviewed candidate (header status, Appendix A heading, footer), merge by the PI with a merge commit, annotated tag `dyad-v6.4.24`, post-tag read-back.

## 7. Notices (prepared, not sent; filed after adoption)

| To | Content |
|---|---|
| RECOG | `DYAD-THM-OPEN21-SHARP-ROWS` available for A1a (RECOG decides); `RECOG-ALG-A1C-JET-REMAINDER-BOUNDS` recorded as RECOG's, not registered by DYAD |
| NUMGEN | informational: no R9-conditional input changes; register row unchanged |
| Triadic, Genesis, OFN | `DYAD-DEF-PRIMITIVE-MAP` label wording; no change to the definition or the RID |
| ATLAS | DYAD.X4: three RIDs registered, one statement left without a DYAD RID; OPEN 20 pilot state now in the DSN |
| LIT | use report: the DSN cites four LIT source labels at SESSION scope in the OPEN 20 entry |
