# Triadic / Genesis — F3 finite-jet N=7/8 receiving review

**Status:** noncanonical receiving audit, 2026-10-10. **Sources:** the exact four uploaded files reproduced under `source/`; no adopted Genesis, Triadic, RRF or RER owner document modified. 

## 1. Model and independent replay

The script explicitly builds the Genesis→RER *conditional analytic modal* map by applying `T_e(r,e)=(r-sin(e),e+expm1(r)-sin(e))` to the three incidence edges with projection after each of six primitive steps. It does **not** represent a physically selected standalone K3 birth event. Its series dependency `c09_independent_series_check_rev2.py` has SHA-256 `67b2e0e785dd30a1bd637c79db2a7210d93516b79f5a00d5fb8233da04f6799b`, and the supplied finite-jet script has SHA-256 `de3675953013d3a1e83227a46565708b16068314974bf81ad142a3f42034d9a3`.

In a separate source layout, the finite-jet script reproduced `age_family_polynomials_kt1.json` **byte-identically**, SHA-256 `03042f84016aa2128ca7ac425a0782d84a617e4b74c490d4f0c7b912c300d83c`. Its 4 visible PASS checks and its empirical grid match the uploaded log. The `--negative` mode exits 1 as intended at the N=7 leading-defect control, rather than at a missing dependency. Run logs are preserved under `evidence/`. The script's 4 PASS lines are bookkeeping/model checks, not four independent mathematical proofs.

The exact interpolated homogeneous polynomials verify, in the binomial-age basis at `kt=1`,

\[
[\binom{\tau}{1}]\mathcal C_5=-\tfrac12 Q_s^2s,\qquad
[\binom{\tau}{2}]\mathcal C_7=\tfrac14 Q_s^3s,\qquad
[\binom{\tau}{3}]\mathcal C_9=-\tfrac3{16}Q_s^4s.
\]

These three identities hold as full polynomials in `(r,e)`. Extrapolating them to a general coefficient family remains `[CAND]`; they do not establish convergence or a finite radius.

## 2. [ALG, formal] Correct leading compatibility defect

With `C_N` the age-family truncation and `E_N=F_c(s,C_N(s,tau))-C_N(F_s(s,C_N(s,tau)),tau+1)`, the full formal invariance and `F=id+O(3)` imply for bounded fixed `tau`:

\[
\mathcal E_7=\Delta_\tau\mathcal C_8+\Delta_\tau\mathcal C_9+O(\|s\|^{10}),\qquad
\mathcal E_8=\Delta_\tau\mathcal C_9+O(\|s\|^{10}),
\]

where `Delta_tau f=f(tau+1)-f(tau)`. The omitted coefficient contributes at both the domain and codomain ends; replacing this by `-C_(N+1)(tau+1)` is incorrect. The `O(...)` statements have no explicit numerical constant and are **not** yet certified uniform error bounds.

## 3. [COR] The stated Q_s ranges use an incorrect Euclidean-radius bound

The script samples `s=R(cos(theta),sin(theta))` and computes `Q_s=r^2-re+e^2`. Therefore, **exactly**:

\[
Q_s=R^2\left(1-\tfrac12\sin(2\theta)\right),\qquad
\boxed{\tfrac12R^2\le Q_s\le\tfrac32R^2.}
\]

Both extrema occur on the stated 24-angle grid. The script's printed `Q_s~[0.75R^2,R^2]` is **not** the sampled range. At `R=0.12` the actual range is `[0.0072,0.0216]`; at `R=0.25` it is `[0.03125,0.09375]`. The reports' downstream `Q_s`-threshold language must not be treated as certified or read from the incorrect column.

## 4. [COR] Proper pointwise age-resolution normalization

The code's printed age-resolution ratio `sup|E_N|/(R^5/2)` is **not** `sup |E_N|/|D_5(s)|`, since the exact age-sheet drift is `D_5(s)=-(1/2)Q_s^2s`. Consequently `|D_5(s)|=(1/2)Q_s^2R`, which varies with direction.

An independent grid evaluation against the same *untruncated* analytic map, using the same 24 angles, five ages and radii, gives the following **empirical (not upper-certified)** values:

| Euclidean `R` | `max_grid |E_7|/|D_5|` | `max_grid |E_8|/|D_5|` | `max_grid |E_8|/max_grid |E_7|` (separate maxima) |
|---:|---:|---:|---:|
| 0.03 | 0.0000972 | 0.0000429 | 0.441 |
| 0.08 | 0.00309 | 0.00225 | 0.729 |
| 0.12 | 0.0137 | 0.0118 | 0.863 |
| 0.18 | 0.0621 | 0.0631 | 1.016 |
| 0.25 | 0.216 | 0.252 | 1.168 |

The last column is the ratio of the separate maximal absolute defects, not a pointwise defect ratio. Thus at R=0.12 the true *grid-pointwise* normalisation is about 1.4% and 1.2%, compatible with a rough 1% description but different from the reported nominal 3.1% and 2.7% based on the fixed `R^5/2` divisor. At `R=0.25`, the correct grid-pointwise maxima are about 22% and 25%, not 49% and 57%. The eighth-degree jet improves the measured **absolute** child defect for radii through approximately 0.12, loses its advantage near 0.18, and is worse at 0.25. None of these grid maxima are certified `K_(N,T)` over the full compact domain.

## 5. [COR] Q_s-error zero is a constructed one-step comparison

For the two states compared in the script, the parent `s+ = F_s(s,C_N)` is identical on both sides; only the target child is replaced by `C_N(s+,tau+1)`. Hence the printed `Q_s` difference is **exactly zero by design**. This establishes no direct one-step error for the parent observable only in that particular projected comparison. It is **not** an accuracy result for a reduced parent-only evolution or a multi-step physical trajectory.

Writing `E=F_c(s,C_N)-C_N(s+,tau+1)`, the *true one-step observable differences* in the script satisfy exactly

\[
\Delta I=B(s^+,E),\qquad
\Delta\Omega_G=\frac{\sqrt3}{2}(s^+_\eta E_\rho-s^+_\rho E_\eta),\qquad \Delta Q_s=0.
\]

For the primitive `B=[[1,-1/2],[-1/2,1]]`, this gives `|Delta I| <= (3/2)|s+||E|` and `|Delta Omega_G| <= (sqrt(3)/2)|s+||E|`. Parent prediction errors can emerge after subsequent steps through backreaction; they require a true iterative comparison and separate bounds.

## 6. Statements not certified

- The numeric suprema are grid maxima over `kt=1`, 24 angles, 5 ages in `[0,2]` and 8 Euclidean radii, evaluated with 50-digit `mpmath`. No interval enclosure or analytic majorant over the continuous region was used. 
- `~25x` growth in empirical coefficient sizes is a heuristic diagnostic; two degrees do not establish any positive, zero or finite radius of convergence. A radius `<=0.04` cannot be certified from this evidence.
- There is no uniform bound as the age horizon increases, no proof of model/physical selection, no long-time observable factor certificate and no memory/physical clock selection.

## 7. Recommended next gate

1. Select an explicit compact `R_min<=|s|<=R_max`, `tau in [0,T]`, including the `tau+1` evaluation and all six intermediate primitive states. Keep `kt=1` for the initial certificate and label the parameter scope.
2. Establish **certified** upper bounds on the polynomial contributions `Delta_tau C_8`, `Delta_tau C_9` and on analytic remainders of `sin` and `expm1` in the full six-step map; derive explicit `K_7(T,R)` and `K_8(T,R)`, not only sample maxima.
3. Separately bound the transverse (relative to the B-metric `D_5` direction) component of `C_8`, and distinguish this from the earlier age-fibre `w_13` curvature invariant.
4. Prove an invariance/retention condition on the chosen region before iterating the standard Lipschitz recurrence; track real true-vs-approximate `Q_s,I,Omega_G` errors over steps.
5. Keep the `[THM — formal]` age-family result, C09 geometry and empirical defect study in distinct RER evidence records. No modification to Genesis v2.8.5 or Triadic v1.6.

**Receiving disposition:** `[ALG]` coefficient and asymptotic-defect mathematics ACCEPT; numeric comparison ACCEPT at **sampled-grid** scope; **Q range and age-resolution table NEED CORRECTION**; explicit constant / multi-step / convergence / physical interpretation OPEN.
