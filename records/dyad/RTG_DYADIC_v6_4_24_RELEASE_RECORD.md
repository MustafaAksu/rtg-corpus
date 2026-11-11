# RTG Dyadic v6.4.24 — release record

**Status:** DRAFT — candidate r1, 11 November 2026. Not reviewed, not adopted. The PI decided on 11 November 2026 to start the candidate ("başlayalım"); adoption is a separate decision after the co-owner's review.

## 1. Candidate

| Item | Value |
|---|---|
| File | `dsn/RTG_DYADIC_OSCILLATOR_DSN.md` on branch `claude/dyad-v6.4.24` |
| Candidate SHA-256 | `7f22ea3511d24170036dc2ec318d630f1d95d7e007deec3ad82ec7623a882327` (r1; 283 385 bytes) |
| Base | `dyad-v6.4.23`, `9f874ccc1cd684482f26a27fca13b37102977cba2a80a75e762ecd7b300425cb` |
| Scope | `records/dyad/DYAD_v6_4_24_BACKLOG.md` §A, §B, §B2, §C, §C3 |
| Kind | single stage, no compaction; 34 assertion-gated edits; four result RIDs and three artifact RIDs added; one displayed grade tag retagged (X4); no statement, constant or OPEN status changed |

## 2. Content

| Group | Edits | What changes | Source |
|---|---|---|---|
| S1 | S1-1 to S1-3 | New result `DYAD-THM-OPEN21-SHARP-ROWS` `[assuming: RECOG-THM-R9-SHARPENED-ROWS]` in §6.14: S_A = 492/25, S_B = 6357/1000, with recorded distinctions; pointers in the header summary and in the OPEN 21 registry entry. The adopted `DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER` line and table are byte-identical | S1 design record; co-owner reviews `5748327144`, `5748500129` (PR #150) |
| X4 | X4-1 to X4-4 | RIDs registered for three existing statements: `DYAD-ALG-NOT-AREA-PRESERVING` (§6.1, cited in §1), `DYAD-ALG-P6-LINEAR-ORDER`, `DYAD-ALG-HOMOLOGICAL-RESONANCE` (§6.6). The first is retagged `[THM]` → `[ALG]` in both places | Atlas DYAD.X4; backlog §B |
| B2 | B2-1, B2-2 | `DYAD-DEF-PRIMITIVE-MAP`: "provisional" replaced by a `[scope:]` note. `DYAD-ART-BRIDGE-NOTE`: path, hash, availability, and the K = 1 remark | backlog §B2; `DYAD_UPLOAD_HASH_CHECK_20261103_BRIDGE_NOTE.md` |
| S3 | S3-1 | One `[SESSION]` paragraph in the OPEN 20 entry on the analytic-branch pilot: stage 1 (exact), literature basis through LIT with its limits, stage 2 (`[NUM]`), stage 3a (negative), stage 2b (`[NUM]`: jump numerically nonzero). It claims no result | PI instruction of 3 Nov 2026; design record §8, §9; stage-2b record |
| ART, E | ART-1, E-1, E-2 | §8: `DYAD-ART-OPEN21-SHARP-ROWS`, `DYAD-ART-BRIDGE-NOTE-CHECK`, `DYAD-ART-OPEN20-AN-PILOT`. Appendix E.1 and E.2 rows for the four result RIDs | — |
| REG | REG-1 to REG-12 | §7.0 rows and §7 lines to RECOG v0.3.27, Genesis v2.10, Triadic v1.7, Programme v1.4, AZ v0.7; notice-table and Appendix F state sentences | `DYAD_INBOX_20261111_OWNER_DISPOSITION.md`; `BASELINE.md` |
| ED | ED-1 to ED-9 | title, date, status, supersedes, release record, Appendix G note, footer, Appendix A entry, own §7.0 row | — |

**Not in this edition:** the §1 compaction; S2 (L-PHASE row B); any OPEN 20 result; a DYAD RID for RECOG's c_J and c_7; a RID for the cubic radial rate across p.

## 3. Build and checks (OWNER-RUN, 11 November 2026)

Scripts in `evidence/dyad/scripts/`; outputs in `evidence/dyad/v6.4.24/` (`SHA256SUMS.txt`).

| Script | SHA-256 | Result |
|---|---|---|
| `build_dyad_v6_4_24.py` | `2e4a2bba38d80a376b8c37ac408cc18122d315a6aa0a44f322fb56a937d9f886` | 34 edits, each old text found exactly once; output `7f22ea35…2327` |
| `check_dyad_v6_4_24.py` | `d85bbaefc8dbb8e76ec30c26040a69e7ac0d8bf4beb2ea0ce461ab08751c5eac` | C0–C11 all PASS |
| `check_dyad_v6_4_24_controls.py` | `f762d66283ab7decb2c47100dc84604bb7e4d7f60063bd6e61efb260f2163c17` | Q1–Q12 each exit 1 at the expected gate |

Gates:

| Gate | Content |
|---|---|
| C0, C1 | base identity; the candidate is the build output; two clean builds are byte-identical |
| C2 | confinement: undoing the 34 logged edits gives the base byte for byte; Appendix A kept, one entry inserted |
| C3 | every RID of the base kept; exactly the seven declared RIDs added; the only removed grade tags are the two `[THM]` of the declared retag; every changed math span belongs to a logged edit |
| C4 | adopted OPEN 21 constants kept; S_A and S_B recomputed as three-decimal ceilings in exact fractions; superseded register wordings absent |
| C5 | the adopted OPEN 21 result line and rows are byte-identical to the base; the new entry carries its assumption and import pin; RECOG's `RECOG-THM-R9-SHARPENED-ROWS` entry is byte-identical at `recog-v0.3.26` and `recog-v0.3.27` |
| C6, C7 | edition lines; §2 "Status:" lines identical to the base |
| C8 | every script, source and output hash cited in the new §8 entries equals the repository file; the cited outputs report all_pass |
| C9 | exact spot checks: det DT; order of λ; resonance condition; P′(u) = α(c₄₀ + μu); the stage-2b figures against `jump_scout.json`; the bound 1.76·10⁻⁶ recomputed (1.7596·10⁻⁶) |
| C10 | every Dyadic-pattern string of `az-v0.7` is an owner RID, except the two named in Appendix F |
| C11 | the five register hashes equal `BASELINE.md` and the files at their tags |

`tools/dsn_lint.py`: informational report in `dsn_lint.txt` (one footer line; Appendix A at most 297 words per edition). `tools/pipes_index.py --check`: OK.

## 4. Decision points for the review

1. **Retag (X4).** "The map is not globally area-preserving" goes from `[THM]` to `[ALG]`: it is a direct Jacobian computation, and the recovered bridge note already grades it `[ALG]`. The content is unchanged. If the co-owner or the PI prefers to keep `[THM]`, edits X4-1 and X4-2 lose their retag clause and nothing else changes.
2. **RID names** of the three registrations.
3. **`DYAD-DEF-PRIMITIVE-MAP` wording.** The scope note names the Programme's reference map and `RTG-OPEN-GENERATOR-SELECTION`. Triadic v1.7 §7.1 quotes the old word "provisional"; it gets an informational notice.
4. **S3 paragraph.** It reports stage 2b as `[NUM]` scouting with no proved error bound and keeps "No conjecture on the analytic or existence outcomes is recorded". The co-owner has not replayed stage 2b.
5. **Open dependencies.** NUMGEN and OFN have not answered the v6.4.23 notice; their rows are unchanged. DZT, ER-2B, RER, RRF, UVM and Triadic have open items from 3 November.
6. **Import pin of S1.** RECOG v0.3.26 §6.13a, where the certificate read it; the entry is byte-identical at v0.3.27 (C5).

## 5. Reviews and decision

| Step | Record | Verdict |
|---|---|---|
| Co-owner change-focused review of r1 | — | pending |
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
