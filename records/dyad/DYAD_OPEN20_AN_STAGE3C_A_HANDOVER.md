# DYAD OPEN 20 (analytic branch) — stage 3c-a: hand-over (W8)

**Date:** 12 November 2026 (r2 of the same day, after review `5875142356`; §5 and §8 updated the same day after the merge, with the inbox dispositions; §5, §6 and §8 updated on 13 November 2026 with the written seed and divergence step; §4 and §8 on 14 November 2026 with the preparation of stage 3c-b). **From:** Dyadic DSN owner (Claude). **Status:** working record (SESSION). It closes stage 3c-a as a set of development and working records. **It is not a certificate and it makes no statement about the jump, about divergence, or about B-an and B-6.**
**Authority:** PI decision of 11 November 2026 for stage 3c-a (`records/dyad/DYAD_OPEN20_AN_STAGE3C_A_PLAN.md` §1). **Stage 3c-b (a certification run) is not authorized.** Whether to authorize it is the PI's decision; this record states what such a run would consist of and what it could and could not claim.
**Governing edition:** DYAD v6.4.24. OPEN 20 B-an and B-6 are ACTIVE.

## 1. What stage 3c-a delivered

| Deliverable | Where | State |
|---|---|---|
| Proof record | `records/dyad/DYAD_OPEN20_AN_STAGE3C_A_PROOF_RECORD.md` | written; accepted as a working record (review `5874133624`); corrected in W8 (§4.3 step 1, §10) |
| Engine and checks | `evidence/dyad/scripts/dyad_open20_an_stage3c_*.py` | W1–W7 merged as development records; W8 adds machine checks and the certification options |
| Development runs | `evidence/dyad/open20-an/stage3c-a/` (`run_w1.sh` … `run_w8.sh`, outputs, `SHA256SUMS_W*.txt`) | OWNER-RUN; file hashes checked independently by the co-owner; no REVIEWER-REPLAYED run |
| Plan record with the log of every package | `records/dyad/DYAD_OPEN20_AN_STAGE3C_A_PLAN.md` | current |

## 2. The package

| Script | Role | Gates | Controls |
|---|---|---|---|
| `…_stage3c_lib.py` | the engine: coefficient balls, series, Cauchy constants, remainder constants, tube step, local inverse, piece check, zone I, arc, legs | — | — |
| `…_w1_check.py`, `…_w2_check.py`, `…_w2b_check.py` | engine checks against stage 2 and against independent evaluation | G0, structural consistency, soundness | SHIFTCOEF; TAMPER; SHRINKREM, SHIFTINV |
| `…_w7_structure.py` | exact derivation of S1, S2, S3, S5 | LIN, S5Z, S5W, P4, LEAD | SCALE, SHIFT |
| `…_w3_zone2.py` | zone II on a cover of each chart sector (P7, P8) | G0, ENG, Z2, SND | CORE, SIGMA, QZERO |
| `…_w4_zone1.py` | zone I for both sides, seam with zone II (P3) | G0, ENG, Z1F, Z1G, SEAM, SND | BIGZONE, SIGMA, CORE, ALPHA, BRANCH |
| `…_w7_branch.py` | the three facts behind the one inverse branch | G0, ENG, INJ, SRC, SRC1 | SMALLSECTOR |
| `…_w5_arc.py` | the common arc (P9) | WEDGE, CHAIN, TAIL, LINK, SND | BIGSTEP, CORE, BRANCH, LOGBRANCH |
| `…_w6_legs.py` | the two legs and the two-disc test (P10) | G0, ENG, LEGF, LEGG, SEP, SND | ZEROJUMP, SHORT |

Environment of the development runs: Python 3.13.16, python-flint 0.9.0, mpmath 1.3.0, sympy 1.14.0; two cores.

## 3. Fixed parameters

| Quantity | Value |
|---|---|
| Truncation N; series degree D; Cauchy circle; arcs | 40; 360; \|x\| = 1.10; 16 000 |
| Remainder profiles (X, arcs); fibre polydisc | (0.90, 8 000), (1.03, 32 000); \|d\| ≤ 0.02 |
| Precision | series at 400 digits; disc work at 160 bits |
| Common point; tube | ξ* = 0.40e^{iπ/6}; q₁ = q₂ = 9, R(ξ*) = 2·10⁻³, wall offsets 0.25 and 0.15, η₀ = π/8 |
| Chart sectors and guard cores | design §3 |
| σ, κ | 0.05, 0.15 |
| Zone boundary | ρ₀ = ξ₀ = 0.05 |
| Zone-II cover | rectangles of side 0.02 in (log\|ξ\|, arg ξ), cut into four up to depth 5, up to \|ξ\| = 0.60 |
| Arc | chain: relative radius 2%, step factor 0.8; tail: \|ξ₀\| ≤ 0.04, relative radius 3% |
| Legs | 334 steps, 5 rounds, `--full-fibre` |
| Sector of the inverse branch | S₁ = {\|ξ\| ≤ 0.47, 0.03π ≤ arg ξ ≤ 0.50π} |

## 4. What a certification run (3c-b) would be

Not authorized. **Since 14 November 2026 the run is prepared as one command with a manifest and one acceptance rule** (`DYAD_OPEN20_AN_STAGE3C_B_PREP.md`; PI decision of that day: preparation only). If the PI authorizes the run, it is that command at a frozen commit, on a machine of the PI's choice, followed by a replay and by a release record that states the scope of §6. The command runs the processes of the following list, each once, with every control:

```
bash evidence/dyad/open20-an/stage3c-a/run_w1.sh
bash evidence/dyad/open20-an/stage3c-a/run_w2.sh
bash evidence/dyad/open20-an/stage3c-a/run_w2b.sh
bash evidence/dyad/open20-an/stage3c-a/run_w7.sh      # structure (exact) and the inverse branch
bash evidence/dyad/open20-an/stage3c-a/run_w3.sh      # zone II, both sides
bash evidence/dyad/open20-an/stage3c-a/run_w4.sh      # zone I and the seam
bash evidence/dyad/open20-an/stage3c-a/run_w5.sh      # the arc
bash evidence/dyad/open20-an/stage3c-a/run_w8.sh      # legs with --full-fibre --strict-snd; inverse branch with --strict-e; controls
```

About 100 minutes on two cores. `run_w6.sh` is the earlier form of the legs and is superseded by the legs part of `run_w8.sh`. The driver `dyad_open20_an_stage3c_b_run.py` replaces this list: 11 positive processes and 23 negative controls, about 50 minutes on two cores.

## 5. Obligations of the design, at hand-over

| # | Obligation | Covered by | State |
|---|---|---|---|
| P1 | Tube lemma, with guard and inward property | proof record §5 (the Rouché step for F and G, zero count), §4 (branch) | the step is written; **the seed (Q1–Q3) is written, conditionally** (proof record §12: conditional on L1 and on (G), (A) on the seed domain) |
| P2 | withdrawn | — | — |
| P3 | Zone I | W4; proof record §7 | development run; derivation written and read back by the co-owner |
| P4 | Divergence argument | proof record §13; co-owner's first text `DYAD_OPEN20_AN_SEED_P4_COOWNER_ARGUMENT.md` | **written, conditionally**: four hypotheses, among them L3 (LIT-checked use at SESSION scope) and a certified point jump, which does not exist |
| P5 | Enclosures of a₂…a₄₀ | W1 | development run |
| P6 | Bounds of the lifted map and of the inverse branch | W2a, W2b; proof record §3, §4.1 | development run |
| P7 | Zone II for F | W3; replayed in W8 with the machine check of every piece | development run |
| P8 | Zone II for G with a validated inverse | W3, W7 (branch), W8 (`--strict-e`); proof record §4, §6 | development run |
| P9 | Domain and arc | W5; proof record §8 | development run; (Q1): proof record §12 steps 1–3, its inequality checked in ball arithmetic up to r₀ = 0.18 (`evidence/dyad/open20-an/seed/`, OWNER-RUN, development) |
| P10 | Fibre enclosures and the two-disc test | W6, W8 (`--full-fibre`); proof record §9 | development run; the method differs from the design's step 3 and was accepted as the development approach (review `5872115882`) |
| P11 | Negative controls | ZEROJUMP, SHORT (legs); ALPHA, BRANCH (zone I); LOGBRANCH (arc) | all four controls of the design exist |
| L1–L3 | López-Hernanz 2012, Theorems 4.2(3) and 5.1 | request `pipes/LIT/20261111-DYAD-lh2012-thm42-uniqueness-use.md` (closed by LIT on 12 Nov, pointing to the reply); LIT's reply `pipes/DYAD/20261112-LIT-lh2012-thm42-use-check.md` | **dispositioned by the owner on 12 Nov 2026: accepted as a check of use at SESSION scope** (`DYAD_INBOX_20261112_OWNER_DISPOSITION.md` §1; source cut below) |

**Source cut for L1–L3** (the pipe item as it stands on rtg-corpus `main` at `e3fafc8`, unchanged since `8f72092`; it names LIT's report at rtg-lit `a3628d4`, which the owner read for the disposition below):
- *L3 (use of Theorem 4.2(3)):* LIT finds that it holds as used. It is uniqueness among all holomorphic invariant graphs in the class, on a sufficiently small petal (condition C1: existential, explicit and very small in LIT's INF-010), for a graph that is in the class there (C2: analytic with S = O(ξ²)); the graph then extends by the identity theorem. The same holds for F⁻¹ in the rotated chart of D5.
- *L1 (use of Theorem 5.1):* uniform asymptotics on closed subsectors at every finite order hold as used, conditionally on Theorem 4.2(1) and Proposition 5.3 as read (called C3 in the co-owner's comment `6824805211`); the propagation to closed subsectors is supplied by a separate k = 3 proof in rtg-lit and by a published theorem (Jiménez-Garrido, Sanz, Schindl 2020, Theorem 5.2).
- *Limits stated by LIT:* a check of use, not a validation of the design; it supplies no value of any constant; it does not cover P1, P3–P11. **It does not prove the seed of the tube.** (The sender's dated correction of one sentence about constants is open as PR #246; it does not change the finding.)
- **Owner disposition (12 Nov 2026, after the merge of W8 r2 as `fdc4fc4`):** accepted as a check of use. The owner read LIT's report and compared C1, C2, C3 and the chart of D5 with the design; they are met by step 6 and by (Q2) as designed, with one precision for P4 (the equality S = u_j is used on the small sub-petal, which contains the arc for large t). L1 and L3 are LIT-checked uses at SESSION scope, L1 conditional on C3. This is not a theorem-grade import and proves neither the seed nor P4. The states of this record before that disposition ("open at LIT" at `2dbaaa1`; "reply received, not yet dispositioned" at `9c62927`) are in git.

The five conditions recorded in the design (§12 there) before a certification run can claim anything:

| # | Condition | State |
|---|---|---|
| 1 | LIT's verdict on L3, or an independent proof | **met at SESSION scope:** LIT's verdict of use (C1, C2; for L1 also C3), accepted by the owner on 12 Nov 2026 after a check against the design |
| 2 | A quantified proof of the seed (Q1, Q2) and the full zone-I bounds | zone I: done as a development run with its derivation; **the seed: written (13 Nov 2026), conditional on L1 at SESSION scope and on the tube hypotheses**; (Q1) is quantified, (Q2) needs no number |
| 3 | Certified guard property and cover of (A), (B) on zone II for both sectors | scripts and development runs exist; a certified run is 3c-b |
| 4 | Certified tail of the arc and validated compact continuation | script and development run exist |
| 5 | Rigorous transport and inverse, and disjoint enclosures | script and development run exist; the inverse branch is proved under INJ, SRC, SRC1 |

**State on 13 November 2026.** The seed and the divergence step are written (proof record §12, §13; reviewed between owner and co-owner, PRs #257 and #258). Both are conditional. What now separates the state from a claim:
- **no certified point jump exists** — every run so far is a development run, and stage 3c-b is not authorized;
- **no REVIEWER-REPLAYED run exists**;
- **the literature inputs L1 and L3 are LIT-checked uses at SESSION scope**, not theorem-grade imports (the owner has not read the article; LIT has not re-proved its Proposition 5.3).

A run of §4, if authorized and replayed, would certify the computational statements (zones, arc, enclosures, two-disc test). Together with §12 and §13 it would give the divergence of the formal branch **conditionally on L1 and L3 at their scope**. It would not decide B-an or B-6.

## 6. What a certificate could and could not say

- *Could say, if every gate passes in an authorized and replayed run:* under the remainder constants of W2b and the structural facts S1–S5, the hypotheses (G), (A1), (A2), (B) of the tube lemma hold on D₀ for F and on D₁ for the inverse branch G; the arc γ lies in D₀ ∩ D₁; and, **if** each sectorial curve is a graph in its tube whose orbit from ξ* stays in the tube, the two values at ξ* lie in two disjoint discs.
- *What the written seed and divergence step add (proof record §12, §13):* under L1, the graphs exist and are the sectorial curves of the literature; under L3, disjoint discs at ξ* contradict a convergent formal branch.
- *Could not say:* anything at theorem grade in the DSN, as long as L1 and L3 are at SESSION scope; anything about B-an or B-6.
- *Not related:* LIT's harmonic target s₁ on the other overlap class (plan record §4, 11 Nov).

## 7. W8 changes

1. **The G leg in the form the proof covers** (`leg_G(full_fibre=True)`, script option `--full-fibre`): recomputed in a development run; result in the plan record §5, W8. The radius of the W6 run is not evidence for the corrected algorithm.
2. **Strict membership in SND** (`--strict-snd`): the independent values must lie in the discs, with no tolerance.
3. **Machine checks of the float bounds** (library): every float that stores a rigorous upper bound is compared in ball arithmetic with the ball it bounds (`_assert_up`) at the moment it is made: the sup bounds and Cauchy constants on circles, the remainder constants, the radius of every arc ball, the radius of every disc of the legs, and the disc of every piece of the zone-II cover (`piece_disc`, which checks in ball arithmetic that the disc contains its rectangle with a margin that makes neighbouring rectangles overlap). The first disc of the arc is checked against the exact t* and x* as balls. The values themselves are unchanged, and the earlier outputs are reproduced byte for byte (`w8_replay.txt`).
   - *Not machine-checked:* the mathematical lemmas the checks rest on (|e^δ − 1| ≤ e^{|δ|} − 1; chord ≤ arc), and the Python-level control flow.
4. **Control "wrong branch"** (zone-I script, `--control BRANCH`): the other root of the quadratic for a₂ gives a second valid formal curve, with consistent structural zeros. Against the tube data of the pilot branch it is rejected: the first functional *decreases* along its orbits (Re Δτ ≈ −1.1), so (A1) and (B) fail on both sides.
5. **Proof record:** §4.3 step 1 now derives |E(x₀)| below the tube radius from the checked inequality itself and from the new `--strict-e` check; §10 refers to the machine checks.

6. **r2 (review `5875142356`).**
   - *R1.* `_leg_data` passed the fibre radius of the enclosures as a float rounded to nearest, which can lie below the bound by one unit in the last place. Both calls now use `_fup`, a float upper bound checked in ball arithmetic. The leg and the two-disc test were recomputed (plan record §5, W8 r2).
   - *The same defect elsewhere.* Every conversion of a ball to a float in the library and in the scripts of W3–W7 was read again. Corrected in the same way (`_fup`, `_fdn`): the fibre radius handed to the tube step and to the local inverse lemma in `piece_check`; the fibre radius of zone I; t_M and the relative bound of the arc tail (gate TAIL); the bounds of sup|b₀′ − 1| (gate INJ); the source discs recorded for SRC and SRC1. The zone-I part of SRC1 was decided in float arithmetic and is now decided in ball arithmetic. Where a margin factor was present but unchecked, the check was added and the value kept: the radius of the disc of zone I, the inner disc of INJ, the two radii of the model engine of control ZEROJUMP.
   - *Left as they are, with the reason:* floats that define a disc, a time or a sector (they enter Arb exactly); floats of the non-rigorous searches of the local inverse (the result is verified with the same floats); floats used only for their sign; printed values; the quality thresholds on tails and on vanishing coefficients (proof record §10); the routing test of the covers (it selects which rigorous test is applied, and the engine checks its own range); the default form of `leg_G`, which is kept only so that the W6 run can be replayed and is superseded by `full_fibre=True`. The scripts of W1, W2a and W2b test the engine against independent values and were not changed.
   - *R2.* `run_w8.sh` records the exit code of every positive process under a name and accepts the run only if each of the ten names occurs once with code 0 and every replay is byte-identical. The rule has its own control: a replay of W5 that writes the committed file and then exits 1 must be, and is, rejected. On an unexpected result the work files are kept.
   - *Run again with the corrected library:* the legs, both zone-II covers, both branch runs, W2a, W2b, zone I, the arc, and the controls ZEROJUMP and BRANCH.

## 8. Open at hand-over

- The seed (Q1–Q3) and P4 are written, conditionally (13 Nov 2026; §5). Open for a claim: a certified, replayed run; the scope of L1 and L3. The inbox items of 12 Nov are dispositioned (`DYAD_INBOX_20261112_OWNER_DISPOSITION.md`): LIT's reply on L1, L3 accepted as a check of use; LIT's INF-016 deferred.
- **Prerequisite of a certification run, from the read-back of r2** (review `5877317450`, item 2): in `arc_tail` the threshold t_M must be computed with the upper bound of \|A₃\| (the condition \|x₀\| ≤ X_M is \|w\| ≥ \|A₃\|/X_M³), or the inequality against that threshold must be checked in ball arithmetic. The present code uses the lower bound and relies on the slack 10⁻¹² of the float bound. Not a numerical failure. **Done on 14 November 2026** in the preparation of stage 3c-b (`wmin = up(A3) / XM ** 3`); the output of the arc script is byte-identical.
- The triangular form of the recursion behind S4 is taken from the stage-1 and stage-2 records.
- Analyticity of the new δ in the base variable in the Rouché step is stated as standard, not written out.
- No REVIEWER-REPLAYED run exists.
- The single command and the manifest for 3c-b are written (14 November 2026, preparation record). The production run and its replay are not authorized.
