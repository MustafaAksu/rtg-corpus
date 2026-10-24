# DYAD LH2012 — J1 closeout and stage-2 receiving disposition

**Date:** 23 October 2026. **Reviewer:** ChatGPT. **Status:** SESSION receiving review; no canonical amendment, adoption, release, tag, notice or Stokes computation.
**Reviewed commit:** `ae78387bfc6a6f3925b1b232affeb1bf12b667dd`, PR #21, branch `claude/dyad-open20-lh2012`.
**Scientific baseline:** DYAD v6.4.22; Methodology v1.4. B-an and B-6 remain ACTIVE.

## 1. Disposition

**J1 CLOSED at receiving-review scope. STAGE-1 EXACT PREPARATION ACCEPTED at the stated finite-jet scope. LIMITED STAGE-2 NUM SCOUTING MAY PROCEED. STAGE 3 NOT AUTHORIZED BY THIS REVIEW.**

The previously conditional stage-2 clearance is now satisfied. The repair preserves the full raw degree-7 jet until the blow-up substitution has been made. S6 links the vertical leading forcing to the independently solved graph equation; S7 compares the vertical jet with direct substitution into the raw jet. The T control reproduces the precise former defect: all S1–S5 checks pass, while S6 and S7 fail. No new draft or DSN release is needed for this closeout.

Read the commit diff, corrected source, stored JSON and the revised design section 7. Unchanged all-order branch results and the LH2012 theorem were not re-proved in this focused review. No sectorial sum or jump was calculated.

## 2. File identity and replay (EV-HASH, EV-CODE, EV-RUN)

The source was reconstructed locally from the retained immutable prior script plus the GitHub commit delta. Before execution its SHA-256 and Git blob were checked against the repository; both matched:

- `dyad_open20_an_stage1_prep.py`: SHA-256 `5c22ff7aab5d9dabdf243bfc6e279616b4fdbc5ea9d8429fa513c3b2584d8568`; Git blob `23cea0a85292687b536a0861c7516473039993fb`.
- Helper `dyad_h4_real_route_check.py`: SHA-256 `dd06a1a20466dbe16da9c9b2e5bfe01a209decbedeed5a2c4a3ba33c783c1e6d`.

Commands: `python -I -B dyad_open20_an_stage1_prep.py --out positive.json`, and separate runs with `--control B`, `R`, `A`, `T`.

| Run | Exit | Failed gates |
|---|---:|---|
| Positive | 0 | none; seven logical groups / nine reported subgates PASS |
| B | 1 | S4, S5_form, S6 |
| R | 1 | S4, S5_form, S6 |
| A | 1 | S4 |
| T | 1 | S6, S7 only; S1–S5 remain PASS |

The generated positive JSON has SHA-256 `2c9ae6376e0c482f2ba520a7ea8e2b38606a6821f7ac3bfa259d4d6020d04739` and Git blob `88bb04c23c6e911d96092d9d0fa0399abac6c81f`, matching the committed output. A structured receipt is `evidence/dyad/open20-an/stage1_j1_receiving_replay.json`.

These are same-code receiving replays. S7 is a second coordinate-computation route using the same raw jet and arithmetic, not a completely independent primitive engine. S1 is interval root isolation; the polynomial identities use exact quotient arithmetic. No running-time claim is imported from the owner environment.

## 3. Mathematical check of the repair

The corrected S3 substitutes into `FzS` and `FwS` before applying the lifted output cutoff. In particular, the nonzero raw `d13*z*w^3` term is no longer discarded before its retained order-x^5 vertical contribution is formed.

For the correctly solved graph, set beta = b2/c^2. Then

`Y(xi) = beta*xi^2 + O(xi^3)`.

Invariance with `F1 = xi - xi^4 + ...` and `F2 = Y - alpha*xi^3*Y + psi0*xi^5 + ...` gives, at degree five,

`-2*beta = -alpha*beta + psi0`,

hence the new exact S6 condition

`psi0 = (alpha - 2)*b2/c^2`.

The current output satisfies this identity. S7 computes `F_w(z,w)/F_z(z,w)^2 - a - b1*F_z(z,w)` after the direct substitution `z=xi/c`, `w=(xi/c)^2*(a+b1*xi/c+Y)` and agrees coefficient by coefficient at the declared cutoff. The T control demonstrates that these checks reject the original error instead of merely inverting the same incorrect jet.

Comparison with the retained pre-fix output confirms unchanged root-isolation data, S2 data, b1, b2, k=3, m=2, alpha, raw-coefficient entries and the reported horizontal coefficients. The corrected psi0 and rotated inverse forcing replace the former values; the old vertical jet is not an input to scouting.

This acceptance is finite-jet preparation only. No inverse-domain, analytic remainder, curved-domain invariance, contraction, weighted-tail or residual-enclosure bound is supplied.

## 4. Stage 2 — limited NUM scope

Stage 2 can begin without another permission round for J1. Its purpose is to estimate a useful coefficient/Borel scale and candidate overlap points, not to prove convergence, divergence or a nonzero Stokes quantity.

Required scope:

1. Use the corrected script/output identities above and the algebraically isolated a_pil branch. Record any new coefficient generator and its relation to the exact low-order data.
2. Compare at least two truncation orders and two precision settings. Report the settings and observed stability or lack of stability; a finite stability observation is NUM, not an asymptotic theorem.
3. A candidate z_* belongs to a common raw-z overlap of two sums of the same branch, not merely to the union of the sectors. Since a certified admissible radius is not yet known, it remains a candidate, not a point certified to lie in the analytic computation domain.
4. Preserve commands, inputs, outputs and hashes under records/evidence and label estimates NUM / non-certified. No resolved scale is an admissible outcome, recorded as inconclusive NUM.
5. Do not run the stage-3 interval jump certificate or claim a validated sectorial sum, root obstruction or convergence conclusion. Stage 3 remains a separate decision after its analytic bounds are available.

The pinned design section 5 still says `inside the union S_j` and `not recorded as evidence`, while section 6 retains the older stage-1-start sentence. Update those working sentences in place when recording the scout: overlap rather than union; not theorem/certificate evidence rather than omitted provenance; stage 1 complete and stage 2 cleared at receiving-review scope. These are routine record synchronizations, not new scientific blockers and not grounds for another release/review cycle.

## 5. Custody

This closeout and its replay receipt are added to the reviewed branch only. The owner script, owner JSON, design, canonical DSN, RID set, OPEN status and notices are unchanged by this receiving review. PR #21 is not merged and no tag is created. Merge remains the PI's action; scientific adoption remains separate from SESSION acceptance.
