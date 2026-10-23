# DYAD LH2012 — receiving review and written-pilot disposition

**Date:** 23 October 2026. **Reviewer:** ChatGPT. **Status:** SESSION; not a DSN amendment, owner adoption, release, notice or Stokes computation.
**Reviewed source commit:** `be9ea79c9284bbb2bf84614b977e64db535fab80`, branch `claude/dyad-open20-lh2012`.
**Governing scientific edition:** DYAD v6.4.22, tag `dyad-v6.4.22`; the OPEN 20 analytic branches remain ACTIVE.

## 1. Disposition

SCIENTIFIC APPLICATION CONFIRMED AT SESSION SCOPE; TWO LOCAL CORRECTIONS REQUIRED IN THE WORKING RECORD/CHECKER. WRITTEN PILOT DESIGN SUPPORTED.

The owner assessment correctly keeps the LH2012 application dependent on the P1-c SESSION branch results. The two-blow-up germ has order four, so the summation order is three. The selected branches have at most six possible singular summation directions, and their sums give parabolic curves after blow-down. Neither convergence nor divergence of the branches, log F, F^(1/2), or F^(1/6) has been proved here. No scientific RID is allocated.

This review does not repeat the full all-order P1-c branch proof, the isolatedness certificate, or the original article's proofs. It reads the owner assessment in full, inspects and runs its finite-input checker, and checks the additional algebra below. The source is the supplied Markdown article transcription, not an independently compared publisher PDF.

## 2. Replays and their limits

The exact repository scripts were copied to the execution environment and matched their recorded SHA-256 values before execution:

- `dyad_lh2012_transfer_check.py`: `6b443e2893f142414cb5babbcaa755c2d05b08abf65b1972584600cafffa13e5`.
- `dyad_h4_real_route_check.py`: `dd06a1a20466dbe16da9c9b2e5bfe01a209decbedeed5a2c4a3ba33c783c1e6d`.

Commands: `python -I -B dyad_lh2012_transfer_check.py`, followed by separate runs with `--control C` and `--control S`.

| Run | Actual exit | Result |
|---|---:|---|
| Positive | 0 | L1-L9 PASS |
| C | 1 | L3 FAIL, other gates PASS |
| S | 1 | L8 and L9 FAIL, other gates PASS |

These are EV-RUN, same-code receiving replays, not an independent proof of the summability theorem. L5 contains a numerical nonzero subtest; see R2 below.

The original receiving-review payload was also available locally. Its script `check_lh2012_dyad_transfer.py` (`71bf1c70cc637eba08823998d380cb85ba76a5d8776138dc4605c0defa79853d`) was rerun: 9/9 positive gates and three intended negative rejections. All four result JSON files reproduce the original bytes. This makes the payload inspectable by the owner; it does not retroactively mean the owner has already inspected or rerun it.

## 3. R1 — summability is stronger than a coefficient Gevrey bound

The owner assessment's Terminology bullet currently writes `Gevrey-1/3 <=> 3-summable`. Replace that equivalence by:

> The LH2012 theorem establishes 3-summability in z, which implies Gevrey order 1/3. A Gevrey-1/3 coefficient bound alone does not establish 3-summability. Under the appropriate residue-class decomposition after t=z^3, summation order becomes one; the components, directions and branches must be specified.

This is a wording correction, not a withdrawal of the LH2012 application: the application uses the summability theorem itself, not just the older Gevrey coefficient bound. The phrase "corresponds to" in the unchanged external receiving review is a convention correspondence, not the missing converse.

## 4. R2 — replace the numerical nonzero test in L5

The owner's current L5 uses `abs(complex(sp.N(l, 30))) > 1e-6`. It is a numerical check, despite the record describing all finite inputs as exact. The nonzero assertion is correct and has the following short exact certificate.

Use the recorded coefficients and let P(a)=Aa^2+Ba+C, ell(a)=c40+mu*a. Since mu is nonzero, an ell-zero root would require a=-c40/mu. Exact arithmetic in Q(i sqrt(3)) gives

\[
P(-c_{40}/\mu)=-\frac{49}{8640}+\frac{307i\sqrt3}{25920}\ne0.
\]

Equivalently,

\[
\ell_+\ell_-=-\frac{22487}{2540160}+\frac{16661i\sqrt3}{7620480}\ne0.
\]

Both identities were evaluated exactly in this receiving session. Replace the floating-point predicate by an exact algebraic-field comparison of P(-c40/mu) with zero; retain the distinct-root and opposite-ell checks. A useful targeted negative control sets C=B*c40/mu-A*(c40/mu)^2, so the exact nonzero gate must fail. Numeric root values may remain display-only.

This is a certificate-implementation repair, not a gap in the previously proved nonzero result. It does not prevent starting the written pilot design. Amend the working files in place on this branch; no DSN release is needed.

## 5. The owner's additional alpha identity

ACCEPT as an exact SESSION identity for the named DYAD reduction. The load-bearing relation is

\[
B\mu=2Ac_{40},\qquad A=\bar\mu-2\mu.
\]

It implies the polynomial identity

\[
P'(a)=\frac{2A}{\mu}(c_{40}+\mu a),
\]

and, for the two nonzero ell values,

\[
\alpha=\frac{P'(a_\sigma)}{\ell_\sigma}
=\frac{2A}{\mu}=\frac{2\bar\mu}{\mu}-4
=-\frac{102}{19}-\frac{16i\sqrt3}{19}.
\]

Thus the ratio is independent of the selected root and C for this coefficient relation. Do not promote this to a statement that an arbitrary analytic germ's cubic coefficient alone fixes its reduced branch type: the relation involving the quartic coefficients was used. The BFM and LH2012 applications do not claim optimal Gevrey order or a nonzero jump.

## 6. Written pilot only — required deliverables

The next step may be one fixed-path SESSION design, for example `records/dyad/DYAD_OPEN20_AN_SECTORIAL_PILOT_DESIGN.md`. No numerical Stokes campaign, new DSN content, RID, adoption or convergence claim is authorized by this review.

1. **Identify one algebraic branch, not just a root-list index.** Give an isolating condition for a_sigma, ell_sigma, one choice of c_sigma^3=-ell_sigma, the chosen finite polynomial jet and normalized lifted coordinates. T exchanges the two formal branches, so one branch suffices for a convergence/divergence conclusion; it does not make all six jumps identical.
2. **Define the cover and maps.** For eta=pi/4, one possible geometric template in xi=c_sigma*z uses centers j*pi/3 and half-opening 5*pi/24, j=0,...,5. Adjacent sectors then have opening pi/12 in common, including the final-to-first overlap. Establish inclusion of sufficiently small such sectors in the actual wide Hakim domains; do not replace their dynamics by arbitrary straight sectors. Even j uses F, odd j uses F inverse with its correctly rotated normalization. The common radius remains a proof obligation, not a guessed numeric constant.
3. **Fix the selected functions and branches.** Specify the paper's H class, including |u|<=|xi|^(m-1), |u'|<=|xi|^(m-2), and compatible branches of Log(xi) for xi^alpha. Push both functions back to the same raw z graph before comparison. The real-slice exclusion is for nonzero points near the origin; 0 is in the closure.
4. **State a certifiable error budget.** Bound the actual analytic map and inverse, unit denominators of the blow-up, invariant orbit domains uniformly for trial functions in H, Hakim-operator contraction and orbit-sum tails. The article supplies qualitative existence, not DYAD numeric radii. Under a proved contraction factor L<1, an approximate fixed-point residual e gives a weighted-norm error e/(1-L). Include rounding, truncation, tail and coordinate-transport errors in both sectorial sums. The primitive map T and Hakim's fixed-point operator must have different notation.
5. **Fix the decision rule.** For one nonzero common point z*, a certified enclosure of the actual jump Delta_sigma,j(z*) excluding 0 proves a nonzero jump and hence divergence of the branch. An interval containing 0 is inconclusive. A proof of convergence requires analytic gluing on every overlap. A nonzero jump rules out a convergent zero-linear-part generator via the earlier Briot-Bouquet lemma; it does not settle B-an or B-6.

Compare sums of the same branch, never phi_+ against phi_-. Do not assume a single scalar Stokes constant or transfer the real PRIM-CTR/L-PHASE constants into complex sectors.

## 7. External material and repository custody

The eight original receiving-review payload files are imported unchanged on `upload/dyad-lh2012-review`, initially under `incoming/dyad-lh2012-review/`, for hash-checked follow-up placement. This includes the previously unavailable script and its original positive/negative outputs. The original review SHA-256 is `e5b815eacdcf99706bd6d3f28c2f2240223bb929cae9ba2eeab7cf822bd18d9f`. Each uploaded Git blob ID matches that computed from the original local bytes.

The source archive `DYAD_LH2012_REVIEW_EVIDENCE.zip` (SHA-256 `f6060ab28503177e61b289df1de7e838a2864496b3a4805a25828de83a7f7a80`) remains unchanged in the session delivery; the upload imports its extracted original files, not a repackaged ZIP. No publisher article or transcription is uploaded. The original Turkish cover file identified as `ef7fbc12...915b` is not available as bytes here and was not reconstructed from conversation text; exact intake of that cover remains pending.

No merge, tag, canonical DSN change, owner adoption or notice dispatch is made by this review. Existing historical SESSION inputs remain frozen; their old source-unavailable statements are answered by the new assessment and this receiving record, not retrospectively erased.
