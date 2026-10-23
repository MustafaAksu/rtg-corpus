# DYAD LH2012 — receiving review of stage-1 exact preparation

**Date:** 23 October 2026. **Reviewer:** ChatGPT. **Status:** SESSION working review; no canonical amendment, adoption, release, notice or Stokes calculation.
**Reviewed commit:** `272d273c64b2b2db573e859f125d301f99736b67`, PR #21, branch `claude/dyad-open20-lh2012`.
**Scientific baseline:** DYAD v6.4.22 / Methodology v1.4. B-an and B-6 remain ACTIVE.

## 1. Disposition

DESIGN REPAIRS P-R3/P-R4 ACCEPTED AS SPECIFICATIONS. ORIGINAL REPLAY REPRODUCED. STAGE-1 JET FIDELITY NEEDS ONE LOCAL CORRECTION BEFORE ITS COEFFICIENTS ARE USED.

The fast exact arithmetic is useful and the branch selection / graph equation results survive. However, the implementation cuts raw w powers before the blow-up substitution. This loses a nonzero `z*w^3` contribution to three coefficients of the normalized vertical component. All existing owner gates still pass, because they test the expected leading shape and invert the same already-truncated map, rather than compare that map with the actual coordinate transform.

The defect is local and has a one-line delayed-truncation repair. It does not refute the prior LH2012 application, the order k=3, m=2, alpha, or the formal branch results. The original S4/S5 coefficient output should not be used as the normalized jet of F until corrected.

## 2. Sources and actual replay

Read the complete stage-1 script and revised pilot design at the reviewed commit; inspected the helper; re-read the accessible LH2012 transcription Definition 4.1 and Theorem 4.2 / operator setup. The transcription is not compared with publisher PDF bytes in this review and is not committed.

Source identities copied into the execution environment and checked against repository Git blobs:

- `dyad_open20_an_stage1_prep.py`: SHA-256 `c3c110543e0ea768109377de8781a9849dd9b61caf89195c1075561b91112cc4`; Git blob `cb9ac9d8cdf0bce9824602a99373f79475ff45a9`.
- `dyad_h4_real_route_check.py`: SHA-256 `dd06a1a20466dbe16da9c9b2e5bfe01a209decbedeed5a2c4a3ba33c783c1e6d`; Git blob `73534a326d43db4bd6d71118a955a1e62d4e708e`.

Commands: `python -I -B dyad_open20_an_stage1_prep.py --out positive.json`, then separate `--control B`, `--control R`, `--control A` runs.

| Run | Actual exit | Actual failed gates |
|---|---:|---|
| Positive | 0 | none: S1, S2, S3_div, S3_order, S4, S5_comp, S5_form PASS |
| B | 1 | S4, S5_form |
| R | 1 | S4, S5_form |
| A | 1 | S4 |

The positive JSON has SHA-256 `f1efcb59dac073dd2ad92d3205d9d0e490367f7341bfac56b2252d13df1833c8`, Git blob `0123dd10b969d12deff2dbc231800ba559b7bf92`, equal to the committed `stage1_prep.json` blob. Reproducibility is confirmed; mathematical fidelity is tested separately below. Evidence: EV-HASH, EV-CODE, EV-RUN. These are same-code replays, not an independent primitive engine.

## 3. J1 — raw-variable truncation before substitution loses retained coefficients

The problematic line is:

```python
Fzl = Ser(FzS.d, 7, NY).compose(Xb, W2); Fwl = Ser(FwS.d, 7, NY).compose(Xb, W2)
```

Here `NY=2`. The constructor drops raw monomials with w exponent greater than two BEFORE substituting `w=x^2(a+y)`. But raw w degree is not lifted y degree: `(a+y)^j` contains constant, linear and quadratic terms even when j>2.

[ALG — SESSION receiving calculation] In the actual raw return,

\[
d_{13}=[F_w]_{(1,3)}=-\frac16+\frac{2i\sqrt3}{9}\ne0.
\]

The dropped term becomes `d13*x^7*(a+y)^3` in the second raw component. Dividing by the leading `x'^2` in the blow-up gives a contribution of order x^5, inside the declared target jet. After `xi=c*x`, `Y=y-b1*x`, the missing terms are exactly

\[
\mathcal F_{2,\mathrm{true}}-\mathcal F_{2,\mathrm{script}}
=\frac{d_{13}}{c^5}\xi^5(a^3+3a^2Y+3aY^2)
\pmod{(\xi^6,Y^3)}.
\]

In particular,

\[
\psi_{0,\mathrm{true}}-\psi_{0,\mathrm{script}}=\frac{d_{13}a^3}{c^5}\ne0.
\]

The nonzero conclusion uses d13!=0, C!=0 (so a!=0), and c^3=-ell!=0. The affected forward coefficients are `(5,0)`, `(5,1)`, `(5,2)` of the vertical component; the horizontal component is unchanged. Corresponding vertical inverse and rotated-inverse coefficients are also affected.

### A short independent consistency identity

The correct graph jet from S2 is

\[
Y(\xi)=\frac{b_2}{c^2}\xi^2+O(\xi^3).
\]

Comparing its invariance equation at degree five with
`F1=xi-xi^4+...`, `F2=Y-alpha*xi^3*Y+psi0*xi^5+...` gives

\[
\boxed{\psi_0=(\alpha-2)\frac{b_2}{c^2}.}
\]

The original script fails this identity exactly; its difference is the dropped term above. S2 itself uses all raw powers and is not affected by the pre-substitution cutoff in S3.

## 4. Direct coordinate route and controlled repair experiment

The receiving diagnostic uses the same exact field arithmetic and raw F jet, but constructs the normalized map by a different, direct coordinate substitution:

\[
z=\xi/c,\qquad w=(\xi/c)^2(a+b_1\xi/c+Y),
\]
\[
\mathcal F_1=cF_z(z,w),\qquad
\mathcal F_2=\frac{F_w(z,w)}{F_z(z,w)^2}-a-b_1F_z(z,w).
\]

Divisibility is handled before the final output truncation. This direct route agrees with the graph identity and disagrees with the original owner vertical jet. The original owner inverse also fails to invert this true transformed jet, despite S5_comp passing against its own map.

For diagnosis only, replace the offending line IN MEMORY by:

```python
Fzl = FzS.compose(Xb, W2); Fwl = FwS.compose(Xb, W2)
```

Then the output cutoff is applied after raw powers have contributed. With this local change, the original gates still all pass, the complete target jet agrees with the direct route, the graph identity holds, and the returned inverse inverts that direct jet in both orders.

| Receiving check | Original source | Delayed-cut diagnostic |
|---|---|---|
| Original owner gates | PASS | PASS |
| Horizontal jet vs direct substitution | PASS | PASS |
| Vertical jet vs direct substitution | FAIL | PASS |
| psi0=(alpha-2)*b2/c^2 | FAIL | PASS |
| Direct jet satisfies graph relation | PASS | PASS |
| Returned inverse vs direct true-map jet, both orders | FAIL | PASS |

This diagnostic is not a silent amendment of the owner script. It is an isolated repair experiment. The owner source and committed output were not edited by the reviewer. `check_lh2012_stage1_pullback.py` and the receiving JSON make the finding reproducible. This is a separate coordinate route with shared arithmetic and raw engine, not EV-INDEP for the entire pipeline.

### Required local completion

1. Delay raw-variable truncation until after substitution (or use a proved weighted-support filter).
2. Regenerate `stage1_prep.json`, including the forward and rotated-inverse psi0 values, and update its provenance.
3. Add the graph-jet consistency gate above; preferably retain the complete direct-coordinate comparison too.
4. Add a negative control restoring the premature raw-w cutoff. It must fail the new fidelity gate, not merely crash. Inverse self-composition alone cannot detect this regression.
5. Document why total raw degree seven and the chosen working orders suffice after division and the finite graph shift. Do not claim unrestricted commutation between rectangular truncation and substitution.

No new versioned draft or release is needed. A scoped commit and the new gate results in this PR are sufficient; prior replays need not be repeated outside the affected preparation.

## 5. What is accepted and unchanged

- P-R3: H, the operator, norms and orbit control now use the curved Hakim domains. Straight sectors are only comparison domains. Accepted as a repaired specification, not a numerical invariance certificate.
- P-R4: full analytic quotients are explicitly defined; inverse-branch certification is separated from entireness and from formal inverse jets. Accepted as a specification.
- Branch isolation / crosswalk, the exact b1 formula, exact b2 and m=2 from S2 are supported. The delayed-cut and direct calculations preserve k=3 and the recorded alpha.
- Coefficients are carried through the cubic scale relation; the pilot does not assume c in E. Polynomial identities in the quotient algebra map to the selected complex root. Field terminology does not substitute for an irreducibility proof if later general inversions are introduced.
- T^2 two-orbit symmetry retains the previous receiving scope: identical vanishing of graph-germ jumps in {0,2,4} and {1,3,5}, not equality of numerical jump values or a single Stokes constant.

## 6. Stage-2 and stage-3 dispositions

**Stage 2: conditionally supported as bounded NUM scouting AFTER the local J1 repair and new fidelity gate pass.** This is receiving scientific clearance, not PI adoption. No repeated broad review or DSN cycle is required just to implement this repair.

Scouting should record the corrected input hashes, branch/coordinate conventions, coefficient and precision budgets, at least two truncation/precision settings, and the stability or instability of the estimates. Choose a candidate point in an actual same-branch overlap, not merely in the union of sectors. The analytic admissible radius and certified error budget remain unproved; a scouting point is provisional until E1-E7 close. An estimate of exponential scale is not a lower bound, a nonzero Stokes multiplier, or proof of divergence. If no stable scale is observed, record an inconclusive NUM result instead of escalating automatically.

The design's sentence "not recorded as evidence" should mean "not theorem/certificate evidence": keep scouting artifacts and provenance under NUM, as the owner message already intends. The stage-1 'Next: can start' sentence is stale after execution and can be updated with the correction record.

**Stage 3: not cleared for a certified jump run yet.** Explicit forward/inverse domains, curved-domain invariance, contraction constants, weighted tails, residual bounds and transport enclosures are still needed. The corrected exact jet does not discharge E1-E7. A common consistent Log shift is not a failing control; use inconsistent orbit-branch assignments to test a real branch error.

Any future enclosure excluding zero must enclose an actual same-branch jump. It would establish branch divergence and, using the prior SESSION lemma, divergence of the tangent-to-identity formal log; it would not by itself decide B-an/B-6. An enclosure containing zero is inconclusive.

## 7. Repository scope

This review and its diagnostics are new receiving records on the reviewed branch. No owner script, owner output, canonical DSN, RID, OPEN status, notice, release tag or main branch was changed. PR #21 remains for PI disposition; no merge was performed.
