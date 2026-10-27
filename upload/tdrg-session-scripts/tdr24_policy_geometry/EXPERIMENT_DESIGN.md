# TDR-24 Policy / k-N Separation — Minimal Experimental Design Matrix

**[RID: TDRG-OPEN-POLICY-GEOMETRY]   Status: [DEF — design; runs not yet executed]**

Goal: determine whether the TDR-24 observable map **factorizes** over a 2-D continuous
control manifold (N, k/N) and a discrete operator (multistar policy):
$$\mathcal{O}(N, k/N, \pi) \stackrel{?}{=} f(N, k/N)\cdot g(\pi),\quad \pi\in\{\text{bound\_symmetric},\text{largest\_center},\text{all\_centers}\}.$$
This replaces the earlier "Layer A vs Layer B" language, which presupposed independence;
the **operator formulation explicitly permits policy↔geometry coupling** and makes it the
object of test rather than an assumption. Supersedes the information-saturated rank-1 fits
on the single k/N=1/15, bound_symmetric slice.

Two decisive sub-experiments, each minimal (no over-simulation). All runs use the
canonical `genesis_mode_b_mc.py`; observables read with `tdr24b_field_structure.py`
and classified with `tdr24_policy_geometry_classify.py`.

---

## Experiment 0 — Cross-N scaling anchor (ALREADY IN CORPUS — no new runs)

The normalization anchor (fixed k/N=1/15, fixed policy=bound_symmetric, vary N) is
required to separate genuine exponent drift from amplitude renormalization leaking into
slope fits. **This data already exists** as the canonical scan and need not be
re-simulated:

| run | N | k | k/N | policy | source file |
|---|---|---|---|---|---|
| 0A | 480 | 32 | 1/15 | bound_symmetric | motif_N480_k32_T5000_b20_v17.csv |
| 0B | 720 | 48 | 1/15 | bound_symmetric | motif_N720_k48_T5000_b100_v17.csv |
| 0C | 840 | 56 | 1/15 | bound_symmetric | motif_N840_k56_T5000_b100_v17.csv |
| 0D | 1200 | 80 | 1/15 | bound_symmetric | motif_N1200_k80_T5000_b50_v17.csv |
| 0E | 1440 | 96 | 1/15 | bound_symmetric | motif_N1440_k96_T5000_b50_v17.csv |

These five cells fix the N-exponent of every observable at the reference k/N, against
which Experiment 2's per-k/N exponents are compared. (A reviewer proposed adding a
480/720/840 anchor trio as "the only missing column"; it is in fact the existing
canonical scan, so no new simulation is incurred.)

## Experiment 1 — Policy factorization test (operator isolation)

**Fix N and k/N; vary policy only.** Tests whether policy enters multiplicatively —
i.e. whether $\mathcal{O}(N,k/N,\pi)=f(N,k/N)\cdot g(\pi)$ holds at this slice (amplitude
shift only). It does NOT by itself establish policy as an "independent operator" — that
requires Experiment 2's exponent-invariance check across k/N. Outcomes:
- **Case A (multiplicative separability):** policies shift amplitude only → policy is a
  discrete symmetry-breaking selector, not a scaling field (cleanest world).
- **Case B (partial entanglement):** amplitude shifts + weak exponent drift → policy
  renormalizes the k/N response (most likely in discrete systems; only detectable with
  Experiment 2).
- **Case C (full entanglement):** exponent changes with policy → the control-manifold /
  operator split is incomplete.

Design (single N anchor, all three policies):

| run | N | k | k/N | policy | T | batch |
|---|---|---|---|---|---|---|
| 1A | 840 | 56 | 1/15 | bound_symmetric | 5000 | 100 |
| 1B | 840 | 56 | 1/15 | largest_center  | 5000 | 100 |
| 1C | 840 | 56 | 1/15 | all_centers     | 5000 | 100 |

(N=840 chosen: factor-rich clean control, batch-100 already standard there, no tail
contamination in the existing bound_symmetric cell.)

Outputs per run: C_birth, χ, B/step, O/step (late-window bulk; for inflationary
policies "bulk" = non-cap-limited runs, guard in classifier).

**This experiment alone cannot give exponents** (single N). It establishes the
*amplitude* gaps between policies at one (N, k/N), needed to normalize Experiment 2.

---

## Experiment 2 — k/N sweep at fixed policy (Layer A geometry)

**Fix policy = bound_symmetric; fix N; sweep k/N.** Tests whether k/N changes only
amplitudes (pure smooth control) or also the *exponent geometry*.

Design (5 k/N points, single N to isolate k/N; note CLI cap k/N < 1/6):

| run | N | k | k/N | policy | T | batch |
|---|---|---|---|---|---|---|
| 2A | 840 | 28 | 1/30  | bound_symmetric | 5000 | 100 |
| 2B | 840 | 42 | 1/20  | bound_symmetric | 5000 | 100 |
| 2C | 840 | 56 | 1/15  | bound_symmetric | 5000 | 100 |
| 2D | 840 | 84 | 1/10  | bound_symmetric | 5000 | 100 |
| 2E | 840 | 105| 1/8   | bound_symmetric | 5000 | 100 |

To get k/N-EXPONENTS (not just one N's response) the sweep must be repeated at a
second N so a 2-D (N, k/N) Jacobian can be formed. Minimal augmentation:

| run | N | k | k/N | policy | T | batch |
|---|---|---|---|---|---|---|
| 2A' | 480 | 16 | 1/30 | bound_symmetric | 5000 | 100 |
| 2C' | 480 | 32 | 1/15 | bound_symmetric | 5000 | 100 |
| 2E' | 480 | 60 | 1/8  | bound_symmetric | 5000 | 100 |

Total Experiment 2: 8 runs (5 at N=840 + 3 at N=480). With Experiment 1's 3 runs
(1A == 2C already), the whole matrix is **10 distinct runs**.

---

## Pre-registered decision thresholds

Run `tdr24_policy_geometry_classify.py` on the resulting motif logs. Decisions:

### Experiment 1 (policy):
- **DISCRETE-CLEAN** if, between policies at fixed (N,k/N), amplitudes differ by
  >2x on >=2 of {C_birth, χ, B/step, O/step} AND the policies remain individually
  well-defined (no exponent comparison here — that is Experiment 2). This is the
  expected outcome (DSN already shows bound_symmetric→crystallization vs
  largest_center→inflation as categorical).

### Experiment 2 (k/N geometry), the decisive classification:
- **Case 1 — pure smooth control:** k/N-exponents of all observables constant across
  the sweep within +/-0.05 (CI overlap); only amplitudes shift. → current DSN model
  correct; k/N is an amplitude coordinate.
- **Case 2 — structural bending:** any observable's k/N-exponent drifts monotonically
  by >0.10 across the sweep (CI non-overlap end-to-end). → k/N is a geometry modifier,
  not a pure coordinate.
- **Case 3 — regime crossover:** a sharp kink (piecewise-linear fit beats single
  power law by >2x in residual at some k/N) or bimodality in any observable. → hidden
  phase structure on the k/N axis (would partially vindicate the phase-boundary view,
  though §6.7's smooth rN_T peak argues against it).

### Rank readout (combines both):
- Run `tdr24_observable_rank.py` on the full 10-run matrix. control_rank should now
  be 2 (N and k/N both vary at fixed policy). Resolvable scaling directions:
  - **1** → single latent flow confirmed across the 2-D control (strong result);
  - **2** → two genuinely independent scaling fields (the field-count question, finally
    answered affirmatively).

---

## What NOT to do (per review; recorded as scope guard)
- No further exponent fitting on the existing k/N=1/15 bound_symmetric corpus
  (information-saturated; reproduces rank-1 artifacts).
- No further basis-reduction attempts before Experiment 2 data exists.
- Do not exceed the matrix: 10 runs is sufficient for a decisive classification.

All outputs branch-local TDR-G diagnostics [NUM]; SG-PROG firewall applies.

---

## Exact run commands (verified runnable against genesis_mode_b_mc.py)

PowerShell (Mustafa's local env; backtick line continuation). Each writes a motif log.

```powershell
# --- Experiment 1: policy slice at N=840, k/N=1/15 ---
foreach ($pol in "bound_symmetric","largest_center","all_centers") {
  python genesis_mode_b_mc.py --policy $pol --N 840 --k 56 --T 5000 --batch 100 `
    --max-nodes 10000 --motif-log "motif_N840_k56_$($pol)_b100_v17.csv" --motif-stride 1 --seed 1
}

# --- Experiment 2: k/N sweep at N=840, bound_symmetric ---
python genesis_mode_b_mc.py --policy bound_symmetric --N 840 `
  --ratios 0.0333 0.05 0.0667 0.10 0.125 --T 5000 --batch 100 --max-nodes 10000 `
  --motif-log motif_N840_sweep_b100_v17.csv --motif-stride 1 --seed 1

# --- Experiment 2 augmentation: second N for cross-N exponents (N=480) ---
python genesis_mode_b_mc.py --policy bound_symmetric --N 480 `
  --ratios 0.0333 0.0667 0.125 --T 5000 --batch 100 --max-nodes 10000 `
  --motif-log motif_N480_sweep_b100_v17.csv --motif-stride 1 --seed 1
```

Note: `--ratios` filters to k/N < 1/6, so 0.125 (1/8) is the highest admissible point.
If a single combined sweep CSV is produced per N, the classifier reads all cells from it.

## Analysis (one command after runs complete)

```powershell
python tdr24_policy_geometry_classify.py `
  motif_N480_k32_T5000_b20_v17.csv `        # Exp0 anchor (existing)
  motif_N720_k48_T5000_b100_v17.csv `       # Exp0 anchor (existing)
  motif_N840_k56_T5000_b100_v17.csv `       # Exp0 anchor (existing) == Exp1 bound_symmetric
  motif_N1200_k80_T5000_b50_v17.csv `       # Exp0 anchor (existing)
  motif_N1440_k96_T5000_b50_v17.csv `       # Exp0 anchor (existing)
  motif_N840_k56_largest_center_b100_v17.csv `   # Exp1 (new)
  motif_N840_k56_all_centers_b100_v17.csv `      # Exp1 (new)
  motif_N840_sweep_b100_v17.csv `                # Exp2 (new)
  motif_N480_sweep_b100_v17.csv                  # Exp2 (new)

python tdr24_observable_rank.py motif_N840_sweep_b100_v17.csv motif_N480_sweep_b100_v17.csv `
  motif_N480_k32_T5000_b20_v17.csv motif_N840_k56_T5000_b100_v17.csv
```

The classifier prints the Experiment-1 verdict (DISCRETE-CLEAN vs ENTANGLED) and the
Experiment-2 Case (1/2/3); the rank tool prints control_rank=2 and the resolvable
scaling-direction count (1 = single latent flow; 2 = independent fields).

## Estimated cost
**Only 4 NEW motif logs** at T=5000 (Exp0 anchor reuses 5 existing canonical-scan files):
2 new policy runs (largest_center, all_centers at N=840) + 2 new k/N sweeps (N=840, N=480). Inflationary policies (largest_center, all_centers) may hit
the node cap; that is expected and the classifier guards bulk pooling. Total compute is
modest (comparable to the existing per-cell campaign), and the design is deliberately
capped at the minimum for a decisive 3-way Case classification — do not extend it.
