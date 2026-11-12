# DYAD OPEN 20 (analytic branch) — stage 3c-a: hand-over (W8)

**Date:** 12 November 2026. **From:** Dyadic DSN owner (Claude). **Status:** working record (SESSION). It closes stage 3c-a as a set of development and working records. **It is not a certificate and it makes no statement about the jump, about divergence, or about B-an and B-6.**
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

Not authorized. If the PI authorizes it, the run is the following commands at a frozen commit, on a machine of the PI's choice, followed by an independent replay by the receiving reviewer and by a release record that states the scope of §6.

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

About 85 minutes on two cores. `run_w6.sh` is the earlier form of the legs and is superseded by the legs part of `run_w8.sh`. For a certification package the eight scripts would be wrapped in one command with one checksum file; that wrapper is not written, because it belongs to the authorized run.

## 5. Obligations of the design, at hand-over

| # | Obligation | Covered by | State |
|---|---|---|---|
| P1 | Tube lemma, with guard and inward property | proof record §5 (the Rouché step for F and G, zero count), §4 (branch) | the step is written; **the seed (Q1–Q3) and the start of the induction are not** |
| P2 | withdrawn | — | — |
| P3 | Zone I | W4; proof record §7 | development run; derivation written and read back by the co-owner |
| P4 | Divergence argument | design §5 step 6 | **not rewritten; conditional on L3** |
| P5 | Enclosures of a₂…a₄₀ | W1 | development run |
| P6 | Bounds of the lifted map and of the inverse branch | W2a, W2b; proof record §3, §4.1 | development run |
| P7 | Zone II for F | W3; replayed in W8 with the machine check of every piece | development run |
| P8 | Zone II for G with a validated inverse | W3, W7 (branch), W8 (`--strict-e`); proof record §4, §6 | development run |
| P9 | Domain and arc | W5; proof record §8 | development run; (Q1) belongs to the seed, open |
| P10 | Fibre enclosures and the two-disc test | W6, W8 (`--full-fibre`); proof record §9 | development run; the method differs from the design's step 3 and was accepted as the development approach (review `5872115882`) |
| P11 | Negative controls | ZEROJUMP, SHORT (legs); ALPHA, BRANCH (zone I); LOGBRANCH (arc) | all four controls of the design exist |
| L1–L3 | López-Hernanz 2012, Theorems 4.2(3) and 5.1 | `pipes/LIT/20261111-DYAD-lh2012-thm42-uniqueness-use.md` | **open at LIT** |

The five conditions recorded in the design (§12 there) before a certification run can claim anything:

| # | Condition | State |
|---|---|---|
| 1 | LIT's verdict on L3, or an independent proof | **open** |
| 2 | A quantified proof of the seed (Q1, Q2) and the full zone-I bounds | zone I: done as a development run with its derivation; **the seed: open** |
| 3 | Certified guard property and cover of (A), (B) on zone II for both sectors | scripts and development runs exist; a certified run is 3c-b |
| 4 | Certified tail of the arc and validated compact continuation | script and development run exist |
| 5 | Rigorous transport and inverse, and disjoint enclosures | script and development run exist; the inverse branch is proved under INJ, SRC, SRC1 |

**Conditions 1 and 2 (seed) are not met.** Until they are, a run of §4 could at most certify the *computational* statements (zones, arc, enclosures, two-disc test) under the stated hypotheses. It could not by itself give the divergence of the formal branch.

## 6. What a certificate could and could not say

- *Could say, if every gate passes in an authorized and replayed run:* under the remainder constants of W2b and the structural facts S1–S5, the hypotheses (G), (A1), (A2), (B) of the tube lemma hold on D₀ for F and on D₁ for the inverse branch G; the arc γ lies in D₀ ∩ D₁; and, **if** each sectorial curve is a graph in its tube whose orbit from ξ* stays in the tube, the two values at ξ* lie in two disjoint discs.
- *Could not say without the open items:* that the graphs exist and are the sectorial curves of the literature (seed, L1); that a nonzero jump implies divergence of the formal branch (L3, P4); anything at theorem grade in the DSN (the literature inputs are at SESSION scope).
- *Not related:* LIT's harmonic target s₁ on the other overlap class (plan record §4, 11 Nov).

## 7. W8 changes

1. **The G leg in the form the proof covers** (`leg_G(full_fibre=True)`, script option `--full-fibre`): recomputed in a development run; result in the plan record §5, W8. The radius of the W6 run is not evidence for the corrected algorithm.
2. **Strict membership in SND** (`--strict-snd`): the independent values must lie in the discs, with no tolerance.
3. **Machine checks of the float bounds** (library): every float that stores a rigorous upper bound is compared in ball arithmetic with the ball it bounds (`_assert_up`) at the moment it is made: the sup bounds and Cauchy constants on circles, the remainder constants, the radius of every arc ball, the radius of every disc of the legs, and the disc of every piece of the zone-II cover (`piece_disc`, which checks in ball arithmetic that the disc contains its rectangle with a margin that makes neighbouring rectangles overlap). The first disc of the arc is checked against the exact t* and x* as balls. The values themselves are unchanged, and the earlier outputs are reproduced byte for byte (`w8_replay.txt`).
   - *Not machine-checked:* the mathematical lemmas the checks rest on (|e^δ − 1| ≤ e^{|δ|} − 1; chord ≤ arc), and the Python-level control flow.
4. **Control "wrong branch"** (zone-I script, `--control BRANCH`): the other root of the quadratic for a₂ gives a second valid formal curve, with consistent structural zeros. Against the tube data of the pilot branch it is rejected: the first functional *decreases* along its orbits (Re Δτ ≈ −1.1), so (A1) and (B) fail on both sides.
5. **Proof record:** §4.3 step 1 now derives |E(x₀)| below the tube radius from the checked inequality itself and from the new `--strict-e` check; §10 refers to the machine checks.

## 8. Open at hand-over

- L1–L3 at LIT; the seed (Q1–Q3); P4. These decide whether anything can be claimed (§5).
- The triangular form of the recursion behind S4 is taken from the stage-1 and stage-2 records.
- Analyticity of the new δ in the base variable in the Rouché step is stated as standard, not written out.
- No REVIEWER-REPLAYED run exists.
- A single wrapper command and package checksum for 3c-b are not written.
