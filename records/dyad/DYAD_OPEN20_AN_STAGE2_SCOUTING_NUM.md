# DYAD OPEN 20 analytic branch — sectorial pilot, stage 2: limited `[NUM]` scouting

**Date:** 24 October 2026 (runs 23/24 October; revised the same day after the co-owner review `ACCEPT SCOPED — LABEL CORRECTION REQUIRED`: label narrowed, Padé anomaly recorded, exact cross-check of $a_5$–$a_8$ added, doublet test added). **From:** Dyadic DSN owner (Claude). **Status:** working record (SESSION), evidence level **OWNER-RUN**. **Result label:** `INCONCLUSIVE — NUM (Borel singularity scale)`; coefficient generation `ACCEPT — NUM`; Gevrey-1/3 growth indication `RETAIN — NUM`. Everything below is `[NUM]`: a reproducible numerical observation with provenance. It is not a theorem, not a certificate, and not evidence for a DSN statement. It establishes no analytic continuation, no Stokes phenomenon, no divergence or convergence, and no certified radius.

**Authorization.** `records/dyad/DYAD_LH2012_STAGE1_J1_CLOSEOUT_REVIEW.md` (`J1 CLOSED`, `STAGE-1 EXACT PREPARATION ACCEPTED`, `LIMITED STAGE-2 NUM SCOUTING MAY PROCEED`, `STAGE 3 NOT AUTHORIZED`) and the PI's decision of 23 October 2026: continue from commit `ae78387` (PR #21, branch `claude/dyad-open20-lh2012`); stage 3 stays closed. Baseline: DYAD v6.4.22, Methodology v1.4; B-an and B-6 ACTIVE.

**Design reference:** `records/dyad/DYAD_OPEN20_AN_SECTORIAL_PILOT_DESIGN.md` §5 item 2 (scouting), D6 (singular directions), D7 (sectors and overlaps). Stage-1 input: `evidence/dyad/open20-an/stage1_prep.json` (SHA-256 `2c9ae6376e0c482f2ba520a7ea8e2b38606a6821f7ac3bfa259d4d6020d04739`).

## 0. Outcome in one paragraph

The coefficients $a_2,\dots,a_{216}$ of the pilot branch $w=\hat\phi_+(z)=\sum a_kz^k$ ($a_{\rm pil}$, $\operatorname{Im}a>0$) were computed from the full map $F=T^6$ (no jet truncation) in ball arithmetic, order by order, at five (N, precision) settings; the stored 80-digit midpoints are identical across all settings, and the rigorous ball radii are below $10^{-114}$. The sequence decays until $k=39$ and then grows factorially: within each residue class $k=3n+r$ the two-step ratio $|a_{3n+6+r}/a_{3n+r}|/n^2$ is $0.0036$–$0.0040$ for $45\le n\le70$, the signature of level-3 (Gevrey-1/3 in $z$) growth predicted by the design. The Borel singularity scale is **`INCONCLUSIVE — NUM`**: Borel–Padé branch-point estimates at $|\zeta_z|\approx17.1$ (still drifting upward with the Padé order), quadratic ratio fits at $|\zeta_z|\approx19.0$–$21.4$ (moving by $10\%$ between $N=144$ and $216$), model value $2\pi/(3|\ell|)=21.34$; the range $17.1$–$21.4$ is a method-dependent observation window, not a mathematical lower–upper bound. The singular directions are consistent with the design's D6 to within $0.03$–$0.06\pi$. A secondary oscillation in the ratios (period about $4.6$ in $n$, relative size a few per cent) is unresolved. Candidate comparison points $z_*$ on $\arg\xi=\pi/6$ are listed with least-term sizes; none is known to lie in $\Delta_0\cap\Delta_1$ because no admissible radius is certified. The coefficients themselves are exact-checked through $a_8$ (§3). **Classification** (co-owner review of 24 October 2026, adopted here): coefficient generation and its numerical stability `ACCEPT — NUM`; level-3 growth indication `RETAIN — NUM`; Borel singularity scale `INCONCLUSIVE — NUM`; no Stokes jump computed; stage 3 not authorized; no DSN change. The owner's first label (`SCALE BRACKETED, NOT CONVERGED`) is withdrawn as the scientific label and kept only as the descriptive observation of §4; the candidate-point choice does not depend on it beyond the $|\zeta|^{1/3}$ sensitivity noted in §5.

## 1. Package

Directory `evidence/dyad/open20-an/stage2/`; `SHA256SUMS.txt` lists every file. Scripts:

| File | SHA-256 | Role |
|---|---|---|
| `evidence/dyad/scripts/dyad_open20_an_stage2_scout.py` | `2961e6383eb9b0e5fb58c0fcb892aa6b05dc2be0faf4c766a3f85be1346008ad` | coefficient generator, gates C0–C4, ratio fits, candidate points; python-flint 0.9.0 ball arithmetic |
| `evidence/dyad/scripts/dyad_open20_an_stage2_summary.py` | `e69be8ab0fcf86dd47ae24366ae2dabda5ee9abd04a73771fde68e5ece06b307` | cross-run comparison, Borel–Padé scouting with Froissart-doublet test, jump-scale table; mpmath (first version `daff7b74…6ddc` had no doublet test) |
| `evidence/dyad/scripts/dyad_open20_an_stage2_exact_crosscheck.py` | `f282f81bc1b5d2cb6badfa4819b5229a80f478b012b0481eb7c6e228fd039620` | exact $a_3$–$a_8$ in $E$ by the stage-1 route (jets to degree 11), compared with the stage-2 values; gates X1, X2; control W |
| `evidence/dyad/open20-an/stage2/run_all.sh` | in `SHA256SUMS.txt` | the exact commands |

Commands (from `evidence/dyad/open20-an/stage2/`, input copied from `../stage1_prep.json`):

```
python3 -I -B ../../scripts/dyad_open20_an_stage2_scout.py --N 72  --dps 330 --stage1 stage1_prep.json --out scout_N72_dps330.json
python3 -I -B ../../scripts/dyad_open20_an_stage2_scout.py --N 72  --dps 400 --stage1 stage1_prep.json --out scout_N72_dps400.json
python3 -I -B ../../scripts/dyad_open20_an_stage2_scout.py --N 144 --dps 600 --stage1 stage1_prep.json --out scout_N144_dps600.json
python3 -I -B ../../scripts/dyad_open20_an_stage2_scout.py --N 144 --dps 700 --stage1 stage1_prep.json --out scout_N144_dps700.json
python3 -I -B ../../scripts/dyad_open20_an_stage2_scout.py --N 36  --dps 60  --stage1 stage1_prep.json --out control_N36_dps60.json   # negative control, exit 1
python3 -I -B ../../scripts/dyad_open20_an_stage2_scout.py --N 216 --dps 840 --stage1 stage1_prep.json --out scout_N216_dps840.json
python3 -I -B ../../scripts/dyad_open20_an_stage2_exact_crosscheck.py --scout scout_N216_dps840.json --out exact_crosscheck.json
python3 -I -B ../../scripts/dyad_open20_an_stage2_exact_crosscheck.py --scout scout_N216_dps840.json --out exact_crosscheck_control_W.json --control W   # expected exit 1
python3 -I -B ../../scripts/dyad_open20_an_stage2_summary.py . > summary_output.txt
```

Owner timings (Linux container, Python 3.13): 4.6 s, 5.3 s, 66 s, 82 s, 0.3 s, 322 s. Output JSON files are byte-deterministic for fixed arguments (verified by a second run of the N=72 and control cases: identical SHA-256). Platform: the owner's container, not the PI's machine; nothing here was run on Windows.

## 2. Method (what the numbers are)

1. **Generator.** The curve $(z,\hat\phi(z))$ is written in the real chart $\rho=z-\omega\eta$, $\eta=(z-w)/(\omega-\bar\omega)$, the primitive map $T(\rho,\eta)=(\rho-\sin\eta,\ \eta+(e^{\rho}-1)-\sin\eta)$ is applied six times as one-variable power series in $z$ (exponential and sine by the standard series recurrences; products by `acb_poly`), and the image is mapped back to $(Z,W)$. The residual $W-\hat\phi(Z)$ (P1-c convention $F_w(z,\phi)-\phi(F_z(z,\phi))$) is formed with $\hat\phi(Z)$ computed as a Taylor perturbation $\sum_m\hat\phi^{(m)}(z)(Z-z)^m/m!$, valid because $Z=z+O(z^4)$ on the curve (gate C0). At order $z^{k+3}$ the residual is affine in $a_k$ with the exact coefficient $L_k=\ell(k^*-k)$ (stage-1 S2); $a_k=-R_k/L_k$ with $a_j$, $j<k$, already fixed. No jet is truncated: the only truncation is the series length, and $a_k$ for $k\le N$ does not depend on $N$ (confirmed in §3).
2. **Gates.** C0 $F_z=z+O(z^4)$ on the curve (and $[F_z]_4=\ell$); C1, C2 $a_3,a_4$ equal the exact stage-1 $b_1,b_2$ at $a_{\rm pil}$ (agreement $<10^{-20}$; actual $\sim10^{-300}$ at dps 840); C3 all ball radii $<10^{-30}$; C4 the coefficient of $a_k$ in the order-$(k+3)$ residual equals $L_k$ for $k=3,\dots,8$ (finite difference, relative deviation $<10^{-20}$). The recursion's residual through order $N+3$ is small by construction and is reported only as a sanity figure. **Exact cross-check of $a_5$–$a_8$** (added after the co-owner review; `dyad_open20_an_stage2_exact_crosscheck.py`): the stage-1 route — $F=T^6$ composed to total degree 11 in exact rationals in the real chart, converted to $(z,w)$, graph equation solved order by order in $E=\mathbb Q(i\sqrt3)[a]/(P)$ — gives $a_3,\dots,a_8$ exactly (gate X1: orders $z^0$–$z^5$ vanish, $L_k=\ell(k^*-k)$ exactly for $k=3,\dots,8$, residual zero through $z^{11}$); evaluated at $a_{\rm pil}$ with 60 digits they agree with the stage-2 values to $\le3.4\times10^{-63}$ (gate X2, threshold $10^{-40}$). Control W (evaluation at the other root of $P$) fails X2, exit 1. The two routes share only the definition of $T$ and the frame change; the stage-2 generator never forms a bivariate jet. Exact values, e.g. $a_5=\bigl(-\tfrac{162839}{65297988}+\tfrac{9383197}{1958939640}i\sqrt3\bigr)+\bigl(-\tfrac{202}{19845}-\tfrac{5393}{119070}i\sqrt3\bigr)a$, are in `exact_crosscheck.json`. Beyond $a_8$ there is no exact cross-check.
3. **Ball note (why dps is large).** The balls are rigorous for rounding but pessimistic: the radius of $a_k$ feeds back through $W$ and $\hat\phi(Z)$, whose contributions cancel in value but add in radius, so the recorded radii grow by about $3.5\times10^3$ per order (six $T$-steps, radius matrix eigenvalue $(3+\sqrt5)/2$ per step, compounded). The midpoints are not affected; the required precision is roughly $\mathrm{dps}>3.6N+40$. The first owner attempt at dps 30 produced exploding coefficients from $k=11$; that run is reproduced as the negative control (`--N 36 --dps 60`: C3 fails, $|a_{36}|\sim10^{52}$ with radius $\ge$ value). No number from an under-precise run is used.
4. **Borel scale.** For $c_n=a_{3n+r}$ and the design model $c_n\sim K\,\Gamma(n+\beta)\zeta^{-n}$ with two singularities $\pm\zeta_z$ of equal modulus (D6: $\zeta_z=\pm(2\pi i/3)/(-\ell)$, $|\zeta_z|=2\pi/(3|\ell|)=21.344$, $\arg\zeta_z/\pi\equiv-0.4357\pmod 1$), the two-step ratio $s_n=c_{n+2}/c_n\sim(n+\beta)(n+\beta+1)/\zeta^2$ is fitted by a quadratic in $n$ on the last third of each class; $\zeta$ is read mod sign. Independently, the diagonal Padé approximants of $B_r(t)=\sum_nc_nt^n/n!$ are computed from the stored 80-digit coefficients at orders $[14/14]$–$[34/34]$ and their nearest poles listed: a string of poles marks a branch cut, and the first pole of a string estimates the branch point. Both are `[NUM]` heuristics.
5. **Candidates.** $\xi_*$ on $\arg\xi=\pi/6$ (centre of the overlap $S_0\cap S_1$, D7), $|\xi_*|$ fixed by $\exp(-(2\pi/3)/|\xi_*|^3)=$ target; $z_*=\xi_*/c_+$. The least term of $\sum a_kz_*^k$ is reported, and the jump scale is re-evaluated with the bracketing $|\zeta_z|$ values.

## 3. Stability (PI condition 2)

| Comparison | Result |
|---|---|
| Truncation: $a_k$, $k\le72$, across $N=72,144,216$; $k\le144$ across $N=144,216$ | identical to all 80 stored digits (max relative difference 0) |
| Precision: $N=72$, dps 330 vs 400; $N=144$, dps 600 vs 700 | identical to all 80 stored digits; max ball radii $4.0\times10^{-115}$ / $5.8\times10^{-185}$ and $3.6\times10^{-199}$ / $2.1\times10^{-299}$; $N=216$, dps 840: $\max\operatorname{rad}a_k=$ `$1.5\times10^{-269}$` |
| Residual through order $N+3$ (midpoint) | $2.9\times10^{-124}$ ($N=72$, dps 330) … `$2.1\times10^{-278}$` ($N=216$, dps 840) |
| Negative control $N=36$, dps 60 | exit 1; C3 FAIL; coefficients explode from $k\approx11$; $|a_{36}|=1.5\times10^{52}$, radius $3.0\times10^{52}$ |
| Exact cross-check $a_3$–$a_8$ (stage-1 route, degree-11 jets) | X1, X2 PASS; agreement $\le3.4\times10^{-63}$; control W fails X2 |

The coefficients are therefore a well-defined object of this generator; what is *not* stable is the asymptotic scale extracted from them (§4).

## 4. Growth and Borel scale (PI condition 4)

**Magnitudes** ($N=216$): $|a_2|=0.1507$, $|a_{20}|=8.7\times10^{-5}$, minimum $|a_{39}|=3.1\times10^{-7}$, then $|a_{74}|=2.1\times10^{-5}$, $|a_{110}|=0.072$, $|a_{146}|=7.6\times10^3$, $|a_{182}|=1.2\times10^{10}$, $|a_{216}|=6.1\times10^{16}$.

**Two-step ratios.** $|s_n|/n^2$ in the three classes: $0.0051$–$0.0065$ at $n\approx20$; $0.0037$–$0.0042$ at $n\approx45$; $0.0035$–$0.0036$ at $n\approx69$. A plateau has not been reached; a slow decrease with a few-per-cent oscillation (period about $4.6$ in $n$) persists. Geometric growth would send this quantity to $0$ like $1/n^2$; it does not.

**Quadratic fits** ($\zeta^2=1/p_2$, $2\beta+1=p_1/p_2$):

| Run (fit range) | class | $|\zeta_z|$ | ratio to model | $\arg\zeta_z/\pi$ mod 1 (model $-0.4357$) | $\beta$ |
|---|---|---|---|---|---|
| $N=144$ ($n=31$–$46$) | 0 / 1 / 2 | 14.85 / 16.48 / 18.09 | 0.70 / 0.77 / 0.85 | $-0.483$ / $+0.486$ / $+0.455$ | $-13.8-17.2i$ / $-13.1-25.8i$ / $-13.0-37.4i$ |
| $N=216$ ($n=47$–$70$) | 0 / 1 / 2 | 21.38 / 19.26 / 19.01 | 1.00 / 0.90 / 0.89 | $-0.396$ / $-0.418$ / $-0.379$ | $+29.0+0.7i$ / $+12.6-9.8i$ / $+10.7+8.1i$ |

The fitted $\beta$ swings between the two windows: the quadratic model with a single $\beta$ is not adequate at these orders, and the $|\zeta|$ values from this method should be read as $19$–$21$ with a method error of order $10\%$.

**Borel–Padé** ($N=216$, $B_r(t)$): the nearest poles form two strings in every class, at $\arg t/\pi\approx+0.59$ and $\approx-0.47$ (model $+0.564$ and $-0.436$; the two observed strings are $1.06\pi$ apart, the model pair $\pi$). Branch-point estimates (first pole of the strings): $[22/22]$ $15.8$–$16.0$; $[30/30]$ $16.2$–$16.8$; $[34/34]$ $17.0$–$17.2$ (classes agree to $1\%$ at each order). The estimate still moves upward with the order; it is a lower-side estimate. In the $\xi^3$ Borel variable ($|t_u|=|t_z|\,|\ell|$): observed $1.67$–$1.68$ at $[34/34]$ against the model $2\pi/3=2.094$.

**Padé anomaly and doublet test** (co-owner review check 2). Class 0 at $[30/30]$ shows an isolated pole at $|t|=11.339$, $\arg t/\pi=-0.536$, and another at $14.919$, neither on a string and neither present at $[22/22]$ or $[34/34]$; class 1 at $[22/22]$ has one at $16.43$, $\arg/\pi=0.358$. The summary script now pairs every pole with the nearest zero of the numerator: each of these poles has a numerator zero within $5\%$ of $|t|$ (Froissart doublet, the usual artefact of noise at the limit of the stored precision) and is excluded. The $5\%$ criterion also tags some poles *on* the strings, where poles and zeros interleave along a cut, so it is a conservative exclusion, not a certified cancellation test; with it, the nearest non-doublet pole per class is $14.5$–$14.7$ $[14/14]$, $15.8$–$16.2$ $[22/22]$, $16.6$–$16.8$ $[30/30]$, $17.0$–$17.1$ $[34/34]$, the same picture as the string heads. The $11.339$ pole is therefore recorded as an artefact at this scope, not as a candidate singularity; nothing here certifies its absence.

**Observation window (not a bound).** The methods give $|\zeta_z|$ between $17.1$ (Padé, rising with order) and $21.4$ (fits, moving with $N$), model $21.34$; in $\xi^3$: $1.68$–$2.1$, model $2.094$. This is a method-dependent window; it is not a mathematical lower–upper bound, and the scale is classified `INCONCLUSIVE — NUM`. Directions: Padé strings at $0.59\pi$ and $-0.47\pi$, fits at $-0.38$ to $-0.42\pi$ (mod $\pi$), model $0.564\pi$ and $-0.436\pi$: consistent to $0.03$–$0.06\pi$. In $\xi$ the estimated singular directions are then $\arg\xi\approx0.15\pi$ and $0.51\pi$ (and their $2\pi/3$ rotations), i.e. $0.01$–$0.015\pi$ off the design's $\pi/6+j\pi/3$; both remain inside the $\pi/12$-wide overlap windows of D7.

**Unresolved.** (i) The scale has not converged with $N$: the Padé estimate rises $15.9\to17.1$ from order 22 to 34 and the fits move by $10\%$ between $N=144$ and $N=216$. (ii) The few-per-cent oscillation in $s_n$ with period $\approx4.6$ in $n$ indicates at least one further singular contribution of comparable modulus; its position is not identified. (iii) The large and unstable fitted $\beta$ means the Gamma-shift (the local exponent at the branch point) is not determined. None of these is a defect of the coefficients; they are limits of $N=216$ and of the two heuristics.

## 5. Candidate comparison points (PI condition 3)

Direction $\arg\xi_*=\pi/6$, the centre of $S_0\cap S_1$ (D7), so $z_*$ lies on the common raw-$z$ overlap of two sums of the same branch — **as a candidate**: no admissible radius $\delta_0$ is certified (E1–E6 not done), hence no point is known to lie in $\Delta_0\cap\Delta_1$. $\arg z_*/\pi=-0.14522$. The model jump scale is $\exp(-(2\pi/3)/|\xi_*|^3)=\exp(-21.34/|z_*|^3)$; the bracketed scale uses $|\zeta_z|=17.1$.

| target (model) | $|\xi_*|$ | $|\xi_*|^3$ | $z_*$ | $|z_*|$ | jump scale at $|\zeta_z|=17.1$ | least term of $\sum a_kz_*^k$ ($N=216$) |
|---|---|---|---|---|---|---|
| $10^{-10}$ | 0.4497 | 0.0910 | $0.8753-0.4296i$ | 0.9750 | $9.7\times10^{-9}$ | $k=39$: $1.2\times10^{-7}$ |
| $10^{-15}$ | 0.3929 | 0.0606 | $0.7647-0.3753i$ | 0.8518 | $9.6\times10^{-13}$ | $k=74$: $1.4\times10^{-10}$ |
| $10^{-20}$ | 0.3569 | 0.0455 | $0.6947-0.3409i$ | 0.7739 | $9.5\times10^{-17}$ | $k=104$: $3.6\times10^{-14}$ |
| $10^{-30}$ | 0.3118 | 0.0303 | $0.6069-0.2978i$ | 0.6761 | $9.2\times10^{-25}$ | $k=161$: $9.1\times10^{-22}$ |

Reading: the least terms are $10^2$–$10^8$ above the model scale and $10$–$10^3$ above the bracketed scale, as expected from the prefactor and from $|\zeta_z|<21.34$; they confirm the order of magnitude, not the constant. For stage 3 the owner would propose the $10^{-20}$ row ($|\xi_*|^3=0.0455$) as the first candidate: large enough jump for an interval enclosure, smallest $|\xi_*|$ among the rows that keep the least term inside $N=216$ with margin. It becomes admissible only if stage 3 certifies $\kappa\delta_0>0.0455$ ($\kappa=2\cos(3\pi/8)\approx0.7654$), i.e. $\delta_0\gtrsim0.0595$; nothing here says it will, and the analytic bounds E1–E7 remain the actual obstacle to stage 3, not the Borel scale.

## 6. Decision proposal and boundaries

- **Label (co-owner review, 24 October 2026, adopted by the owner).** Stage-2 delivery `ACCEPT`; coefficient stability `ACCEPT — NUM`; Gevrey-1/3 indication `RETAIN — NUM`; Borel singularity scale `INCONCLUSIVE — NUM`; $N=432$ `DEFER`; stage 3 `NOT AUTHORIZED`; Dyadic DSN change not needed. The owner's earlier proposal `SCALE BRACKETED, NOT CONVERGED` is withdrawn as a label. Under the PI's condition (6) the scale result is explicitly inconclusive; the growth type, the directions and the candidate points stand as `[NUM]` observations.
- **What this record does not do.** No sectorial sum, no jump, no Stokes quantity, no analyticity radius or error bound, no statement about B-an or B-6, no DSN, RID, OPEN-status or notice change, no theorem-level claim. The model $|\zeta_z|=2\pi/(3|\ell|)$ is the design's heuristic and is not endorsed by the data beyond the bracket above.
- **Follow-ups named by the co-owner review:** (1) exact cross-check of $a_5$–$a_8$ — **done** (§2, §3; X1, X2, control W); (2) Froissart-doublet analysis of the Padé poles, in particular the $[30/30]$ anomaly — **done** (§4); (3) a two-singularity model in place of the single-$\beta$ quadratic fit, with a window-stability test — **not done**, open; (4) $N=432$ — **deferred** by the review until (3) defines what the run would discriminate. None of these changes the stage-3 decision, which waits on E1–E7.
- **Design sync.** The three stale phrases named by the J1 closeout review were replaced in place in `DYAD_OPEN20_AN_SECTORIAL_PILOT_DESIGN.md` (§5 item 2: overlap instead of union; `[NUM]`/not theorem-certificate evidence; §6: stage 1 complete, stage 2 cleared and run, stage 3 not authorized; header and §7 closing sentence updated accordingly).

**Co-owner review text.** Received 24 October 2026 as `257404c7-attachment.txt` (SHA-256 `0bd3707dd56c4f327ee744972cb9bacd77b4e520526f958c403913542029f000`); not in the repository (the reviewer made no repository change). It would go unchanged to an `upload/...` branch if the PI wants it kept.

**Unchanged and carried:** N16–N21 unsent; the C-4 read-back branch and PR #21 wait for the PI; B-an and B-6 ACTIVE; RAW-CUBIC, OPEN 9, FC-31/32 and the combined G14–G15 replay as before.
