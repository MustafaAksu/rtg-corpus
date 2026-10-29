# TDR-G Response-Tensor Branch — Charter

**[RID: TDRG-RESPONSE-TENSOR]   Status: [BRANCH — exploratory, firewalled from canonical TDR-G]**

## Purpose
Test whether the TDR-G observable system is better described as projections of a single
**response tensor** over the control manifold, with its intrinsic dimension *read from
data* rather than imposed. Built as an isolated branch; folds into canonical TDR-G ONLY
after it succeeds on its own falsifiable terms.

## Governing methodological axiom (the reason this branch exists)
> Intrinsic dimensionality is the rank of the UNNORMALIZED observable response tensor over
> the full control manifold. Normalizations, factorizations, and quotient observables are
> admissible only as post-hoc coordinate diagnostics and must NEVER be used to determine
> rank or field count.

Corollary (premature-quotienting guard): dividing by a baseline policy/cell assumes
reducibility along that fiber and enforces rank collapse by construction. Forbidden as a
primary instrument.

## The two-sided discipline (from PI directive)
1. **Do not impose dimensions** on naturally grown structure (no ansatz, no normalization-first).
2. **Do not suppress dimensions** the math genuinely requires — if the response tensor asks
   for a new manifold, that must be allowed to surface, even if the count rises.
3. BUT a rising dimension count must be distinguishable from representation noise. Therefore
   every dimension claim is gated against a NULL MODEL: shuffle/resample with no real
   cross-control structure and measure how many singular values appear from sampling alone.
   A dimension is REAL only if its singular value exceeds the null ceiling.
4. Dimensions may later CONSOLIDATE: if two apparent directions collapse under a larger
   control set or more seeds, that is recorded as a merge, not a deletion — the branch keeps
   the provenance so a "natural path" (the PI's phrase) can be recognized if one emerges.

## Firewall
- All branch outputs tagged [BRANCH/NUM diagnostic]. Nothing crosses into canonical TDR-G
  DSN (v2.12.x) without an explicit promotion note approved by the PI.
- SG-PROG-1/4 still apply: no cross-branch (continuous/discrete) flow.
- The branch may not alter any canonical claim; it only proposes.

## Success criterion (what "earns its place" means)
The response-tensor formalism is promotable to canonical TDR-G iff, on a control manifold
with >=2 independent active levers (N and k/N at minimum):
  (a) its measured intrinsic dimension is stable across seeds and resamples (null-gated);
  (b) it reproduces the existing rank readout where they overlap (consistency with the
      k/N=1/15 rank-1 finding as a restricted slice);
  (c) it makes at least one falsifiable prediction the per-observable fits do not.

Until (a)-(c), it stays a branch.

---

## Calibration finding (first build, validated on synthetic data)
The null-gated dimension reader was tested against synthetic tensors of known intrinsic
dimension (permutation null, Horn parallel-analysis null both tried):
- **dim <= 1: reliably recovered at any cell count** (including the real 5-cell corpus).
- **dim >= 2: systematically UNDER-counted** until ~40-80 control cells exist; with few
  cells the reader returns a LOWER BOUND, not the true dimension.
- Pure-noise input is NOT inflated to high dimension (the gate resists false structure) —
  the failure mode is conservative (under-count), which is the safe direction.

Consequence for the PI's "if it goes up to billions" question: the instrument CAN let
dimension rise (synthetic dim-2 recovered correctly at >=12 cells, dim-3/5 at >=40), but
**reliable counting past ~2 requires a control manifold with many cells** — i.e. the k/N x
policy x N grid, not the current single-lever slice. On the current corpus the only
defensible statement is "intrinsic dimension >= 1, consistent with rank-1 on this slice."

This is recorded as a limitation, not hidden: the branch reports its own confidence tier
and labels low-cell results as lower bounds.

---

## Dynamical layer added (response to Zeta geometry-saturation finding)

`dynamical_extractor.py` adds a SEPARATE trajectory-level signal layer (autocorrelation
times, Fano burstiness, inter-birth-interval CV, birth↔occupancy lagged cross-correlation,
clean-star autocorrelation). Per the review's strict constraint, it is NOT fed into the
static exponent pipeline — it is its own layer with its own null-gated rank test, so
dynamics are never recompressed into static rank artifacts.

### The key test (review's success criterion): does dynamical rank exceed static rank?
On the existing single-lever corpus (N=480–1440, k/N=1/15, bound_symmetric):
- STATIC layer:     null-gated intrinsic dim = 1 (leading var 90.5%)
- DYNAMICAL layer:  null-gated intrinsic dim = 1 (leading var 92.6%)

**Dynamical rank does NOT exceed static rank here** — no extra temporal degree of freedom
surfaces. BUT two strong caveats keep this from being a resolution:
1. Both layers are control-rank-capped at 1 (single lever); this is a lower-bound
   consistency check, not a dimension resolution. F3 (observable projection collapse)
   is neither confirmed nor refuted — it cannot be, on one lever.
2. The dynamical leading direction is WEAK and nearly single-feature: it is dominated by
   inter-birth-interval CV (slope +0.39, R² 0.81); the other dynamical features are
   flat-to-weak (autocorr times ~0.48 nearly N-independent, R² < 0.6). The leading
   singular value (0.449) barely clears its null ceiling (0.432). So even the dim-1
   dynamical signal is mostly one clustering statistic, not a rich temporal manifold.

### Interpretation [BRANCH/NUM diagnostic] — CORRECTED (review)
The earlier phrasing ("dynamical observables are also near-saturated; weakly argues against
F3") was an INFERENCE ERROR and is retracted. On a rank-1 control manifold BOTH layers are
forced to return rank <= 1 regardless of the true underlying dimension (1, 5, or infinite) —
the hidden directions cannot be EXCITED, so observing static-dim = dynamical-dim = 1 is
guaranteed by the experimental geometry and can conclude NOTHING about F3 or about the
absence of higher-dimensional structure. The correct statement:

  > Both static and dynamical observable layers collapse to a rank-1 response under a
  > rank-1 control manifold. This is a statement about EXCITATION INSUFFICIENCY, not about
  > the absence of higher-dimensional structure in the underlying process.

Second limitation (review): the dynamical features here (CV, Fano, autocorrelation times)
are COMPRESSED many-to-one statistics of path space, not trajectory embeddings. So the
layer tests rank(feature_summary), NOT rank(trajectory_manifold). Even on a richer control
manifold, a non-injective feature map could under-resolve the true dynamical dimension.
Injectivity of the dynamical feature map is itself unverified and is now a branch caveat.

### What this result actually is (tight form)
- A CONSISTENCY result, not a structural one: no observable distinction between static and
  dynamic projections appears under 1D excitation. Expected under the geometry; not a discovery.
- It does NOT rule out hidden dynamical structure (single lever cannot, by construction).
- The one NON-dimensional finding that DOES survive: inter-birth-interval CV carries genuine
  N-dependence (slope +0.39, R²0.81) while autocorrelation times are flat (R²<0.6). This is a
  statement about WHICH trajectory features respond to N under the applied excitation — not a
  dimension claim — so it stands. CV is the highest-value dynamical observable for the grid.
- Build discipline confirmed: dynamical layer runs, null-gates correctly, firewalled from the
  static pipeline.

### Two open instrument questions for the grid stage
1. Excitation: only k/N + policy variation can break the static/dynamic projection
   degeneracy. A "minimum excitation set" guaranteeing identifiability of dynamic-vs-static
   projection kernels is the next design target (not analysis — design).
2. Injectivity: whether the compressed dynamical features resolve path-space rank, or need
   to be replaced by genuine trajectory embeddings (e.g. delay-coordinate / covariance-of-
   increments), must be settled before trusting any grid-stage dynamical rank > 1.

---

## Feature-map injectivity test (review-directed, executed on existing data — NO grid needed)

The review argued that the scalar dynamical summaries (CV, Fano, autocorr) are compressive
many-to-one maps, so a richer trajectory embedding might extract structure they lose — and
that this is testable WITHOUT expanding the control manifold (it is an intra-run question).
Correct, and tested:

**Three embeddings, per-run, N=840:**
- Cross-channel INCREMENT covariance (births,occ,cs,ms): **rank 1** in all 30 runs — the
  four channels' increments move along one shared mode.
- Cross-channel LEVEL covariance: **rank 1** in all 30 runs — the standing state is
  one-dimensional across channels.
- Single-channel DELAY embedding (Takens, dim=8): initially "rank ~8" on births — but this
  was an ARTIFACT: births are rare in the late window (median 11 events / ~4000 steps), so
  the embedding of a near-zero sparse series fills its dimension trivially. Caught by the
  null test; do not trust delay rank on sparse channels.

**Null-tested memory (occupancy channel, real variation, delay dim=8, vs shuffled):**
- real effective rank 7.63 vs shuffled 7.99; gap 0.37 (below the 0.5 threshold).
- => only MARGINAL memory structure beyond the marginals; the scalar autocorrelation
  summary already captures essentially all of it.

### Conclusion [BRANCH/NUM diagnostic]
On this corpus the feature-map non-injectivity, while real in principle, does **not** hide
extractable structure: richer trajectory embeddings (increment covariance, level covariance,
null-tested delay coordinates) recover no temporal degrees of freedom the scalar summaries
miss. The trajectory process is genuinely low-complexity here — one shared cross-channel
mode, near-white memory beyond marginals. This was resolvable WITHOUT the grid, and it
removes "improve feature injectivity" from the list of available no-grid levers: it was
tried and the corpus does not reward it.

Methodological note: the initial births delay-rank of 8 would have been a false "structure"
finding had it not been null-tested against a shuffle — the same discipline (null-gate
everything) that the Zeta study and the response-tensor branch both rely on. Recorded as a
caught near-miss.
