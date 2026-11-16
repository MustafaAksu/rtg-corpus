# AZ v0.10 — release record (DRAFT; candidate built, not adopted)

**[SESSION] Not adopted.** `az-v0.9` governs until the PI adopts this edition, the record is completed, and the PI merges and tags. Prepared by the AZ co-owner (Claude), 16 November 2026. It invents no hash, approval or review identifier.

## 1. Authority

- **PI, 12 Nov 2026** — outcome rule for Action 1 (Stage 1 report §11 item 3): a validated, supported contrast is eligible for a PI-approved `[NUM diagnostic]` entry in AZ Level A with its exact scope and provenance; it closes no `AZ-OPEN-PROMO`, promotes no maturity and is no TDR-G claim.
- **PI, 16 Nov 2026** — given in the second co-owner's conversation and recorded verbatim in review `5915724946` (PR #275), relayed to this session by the PI at 12:13 +03:00; source-reported to this lane: "I accept the report"; "Continue as proposed"; "TDR-G gets no separate item for the numerical result." As recorded there: authorisation to prepare the separate entry `AZ-NUM-TOKRES-S2` / `AZ-ART-TOKRES-S2` in an AZ v0.10 candidate, Level A and `AZ-OPEN-PROMO` retained; not the adoption of this file.

## 2. What changes

| Object | Path | SHA-256 | Bytes |
|---|---|---|---|
| base, `az-v0.9` | `dsn/RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN.md` | `c198a8bbddb23ce0d546c3ed03bddcdcf02dd83b974da7651a89a3fec5ac7598` | 100,978 |
| candidate r1 (commit `ff753f5`; review `5917774476`) | same path | `7336ab384288e4cffc58ae3b550a6567e08252ec340f5f657a0276686f256cfa` | 111,765 |
| **candidate r2 (DRAFT)** | same path on this branch | `b672fd03cfe73e4cd674721bca24a3da4b76c0fe09cf52727d92ed932a178217` | 112,563 |

One content stage. `evidence/az/v0.10/build_az_v0_10.py` reads the base with `git show az-v0.9:…` (hash asserted), asserts the Stage 2 package (`25b796b3…eb4b`) and data (`3e211e6a…a7e7`) hashes and the presence of the cited records, applies 19 exact-once edits (`evidence/az/v0.10/edit_log.txt`; the block is `evidence/az/v0.10/block_4_2_2.md`), and asserts that every base line not named in an edit is unchanged and in order: 618 of 631; six lines replaced (title, *Date*, *Document status*, *Supersedes*, the §4.2 heading, footer), seven edited in place. It also asserts that the line declaring `AZ-NUM-TOKRES-S1` is unchanged and that each new identifier is declared once.

| Where | Change |
|---|---|
| header, footer | edition v0.10, DRAFT; *Status summary* names both diagnostics |
| §0.1 | the routing row covers §4.2.1 and §4.2.2 |
| §0.2 Thread B | readout of `AZ-NUM-TOKRES-S2` |
| §1.1 | the criterion sentence names both diagnostics; the criterion and its status unchanged |
| §4.2 | heading "(bridge-candidate family; AZ-owned diagnostics)"; ownership sentence; **new §4.2.2** (the block) |
| §5 | one high-risk row for `AZ-NUM-TOKRES-S2` |
| §8 | local-use clauses of `TDRG-ALG-TOKEN-CENSUS-LAW` and `TDRG-ALG-PARENT-CHILD-PHASE` name the second check and intervention; the owner statements and pins unchanged |
| §9 | artifact entry `AZ-ART-TOKRES-S2` |
| Appendix A | v0.10 entry |

New identifiers: `AZ-NUM-TOKRES-S2`, `AZ-ART-TOKRES-S2` (80 in the file). None removed. No pin changes: `dyad-v6.4.24`, `tdrg-v2.12.15` govern per `BASELINE.md`.

**Content of §4.2.2.** Exactly the registered output, corrected report wording (review `5915724946`, R1–R2): cells as `(N, k)` pairs; the order-2 intervention only at `N = 240, 480`; the support criterion for `RD > 0.05` with its nominal simultaneous coverage and no exact finite-sample familywise guarantee; the near-quarter control; the controls; the calibration and its out-of-sample check; the post-pilot design decision named; what it is not; evidence keys (`EV-INDEP` limited to the second co-owner's recomputation from the published counts).

## 3. What does not change

`AZ-NUM-TOKRES-S1` and its scope; Level A; the OPEN registry, `AZ-OPEN-PROMO` included; the milestones; the owner pins; every other AZ-owned statement. No mechanism, no `N`-law, no order hierarchy below 2, nothing on TDR-26; no TDR-G claim; OPEN-P1 untouched.

## 4. Checks (this session)

| Check | Result |
|---|---|
| Build from the tag, base and evidence hashes asserted, 19 exact-once edits | r2 `b672fd03…8217` (rebuilt twice, equal; and again after merging `main` `e817a63`) |
| Base lines unchanged and in order | 618 of 631 |
| `tools/dsn_lint.py` (informational) | 112,563 bytes; one footer line; 80 identifiers; history phrases unchanged from v0.9 (10 / 5 / 1) |
| `tools/pipes_index.py --check` | OK, 126 items |
| `bash evidence/az/token_resonance/stage1/verify.sh` | `VERIFY PASS` |
| `bash evidence/az/token_resonance/stage2_result/verify.sh` | `VERIFY PASS` |

## 5. Review record

- **Review `5917774476`** (second co-owner, 16 Nov 2026, 09:34Z, on `ff753f5`): *accept with two minor scope corrections; not adopted.* The ten rows match the corrected report; cells, horizons, thresholds, support criterion and approximate simultaneous coverage correctly carried; the S1 block unchanged in the full diff; Level A, OPEN registry, pins and the TDR-26 boundary kept. By its own statement it did not run the builder or the `verify.sh` scripts and did not recompute the candidate hash; those are source-reported to it.
  - **R1** — "θ(N) equates baseline rates" replaced: the thresholds were calibrated to match approximately the reference rate in non-resonant native pilot draws; equality of population rates is not shown; the out-of-sample rates inside the pilot interval are a consistency report, not an equivalence test (§4.2.2, two sentences).
  - **R2** — the subsets of the control equivalences carried: G4 sham on draws whose native and perturbed slot token are both non-resonant; G5 detuned on draws whose native slot token is non-resonant; equivalences stated for those subsets only.
  - Non-blocking, applied: runs capped before tick 800 count positive on E_100; the near-quarter result is one registered mixture arm (token drawn from the four values), not four tests — in §4.2.2 and the §0.2 readout.
  - No number, reading or control decision changed. Candidate r2 `b672fd03…8217`. Changed-text readback requested: `git diff ff753f5 HEAD -- evidence/az/v0.10/block_4_2_2.md evidence/az/v0.10/build_az_v0_10.py`.

## 6. Steps

| # | Step | By | State |
|---|---|---|---|
| 1 | Candidate | AZ co-owner | done |
| 2 | Change-focused review, corrections, readback | second co-owner | review and corrections done (§5); readback pending |
| 3 | Adoption decision | PI | pending |
| 4 | Publication commit (status lines; this record; `BASELINE.md` AZ row) | AZ co-owner | pending |
| 5 | Merge (merge commit) and annotated tag `az-v0.10` | PI | pending |
| 6 | Edition notices (TDRG — edition notice only, no separate item for the numerical result; ATLAS; PROG if affected) | AZ co-owner | pending |

PR #275 (Stage 2 report) was merged on 16 Nov 2026 (`e817a63`, review `5917746984`), before this edition, since §4.2.2 and §9 cite its files.
