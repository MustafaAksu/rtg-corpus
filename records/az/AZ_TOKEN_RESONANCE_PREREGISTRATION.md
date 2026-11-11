# AZ Action 1 — Token Resonance and Basin Selection: preregistration and test package

**[SESSION] NONCANONICAL. Draft r1 for independent review; nothing here is adopted.** Prepared by the AZ co-owner (Claude) on 11 November 2026 on the PI's message of that day (10:00 +03:00), which relayed the task "Proceed with AZ Action 1 — Token Resonance and Basin Selection, as selected by the PI" together with the co-owner review (ChatGPT) of the BOOTSTRAP 4 advisory. Branch `claude/az-token-resonance-prereg`. It edits no DSN, closes no pipe item, claims no TDR-G result and authorises no campaign: the PI decides on the confirmatory run after the independent review.

Governing sources: AZ `az-v0.7` (file SHA-256 `2294d2a3…fc94`), TDR-G `tdrg-v2.12.14` (file SHA-256 `3be72923…2392`, §§6.1–6.3, §6.5, §6.12, SG-11–SG-14). Every statement about TDR-G dynamics below is a proposal to the TDR-G owner; `TDRG-OPEN-SPECCONS-STAR` and `TDRG-OPEN-LOCKING-FAIL` (TDR-26) stay open and stay TDR-G's (SG-AZ-6).

## 0. What is registered, in one paragraph

On the pinned TDR-G engine with the adopted orientation rule, at `N = 120`, `k = 8`, policy `bound_symmetric`, the outcome `Y = 1{max_{t≤800} M_t ≥ 100}` is compared between runs whose initial state differs in **one token only**: a resonant value (`2x ≡ 0`, or `2x ≡ N/2`) against its neighbour `x ± 1`, with the same initial phases and the same other three tokens. Two contrasts are primary (order 1 and order 2, tested separately); the pooled `4x ≡ 0` contrast, the native-ensemble association, a sham perturbation, a node-label permutation, the cell `N = 122` (where no order-2 token exists), the superseded orientation rule and the TDR-26 birth-anchored rule are registered secondary outputs. The registered minimal effect is a risk difference of `0.05`. Sample size is fixed in advance (1,500 base draws per cell); there is no interim look.

## 1. Sources and pins

| Object | Path | SHA-256 | State |
|---|---|---|---|
| TDR-G engine (header "v15.3"; the engine of the v17 corpus) | `upload/tdrg-records/genesis_mode_b_mc.py` | `4c94d8741dc43780394cc563d04be9b2ee5c9767a43a048878fc67640dafa608` | `EV-HASH`, `EV-CODE`; equals TDR-G §8 `TDRG-ART-GENESIS-MC`; not modified |
| Reference `orient_path` for `TDRG-DEF-ORIENT` (v2.12.14) | `evidence/tdrg/scripts/tdrg_orient_v2_12_14.py` | `ca59e9b9a1bb260a6600f3f793adea488ba40c416879673219dc30f21f77d59c` | `EV-HASH`, `EV-CODE`; not modified |
| v18 engine | `upload/tdrg-records/genesis_mode_b_mc_v18.py` | `9d787b435c42fd2024c81e614e3c6e3e076dc2bd30ad1e7e286ada8e6dfe675e` | read only: differs from the engine above in motif-logging options only (36 changed lines after line-ending normalisation; `orient_path`, the event functions and `step_universe` are identical); not used |
| TDR-26 classifier | `upload/tdrg-session-scripts/tdr26_early_basin_classifier.py` | `17e634bfd8267038d9732a0f7f3dc7171b57319f857edd53557c83ca520dce1c` | read only: source of the birth-anchored metric definitions (§6.4) |

**Profiles.** `P1` (primary): the engine above with the module attribute `orient_path` rebound to `make_orient(engine)` of the reference file, i.e. the adopted `TDRG-DEF-ORIENT`. `P2` (sensitivity only): the engine with its built-in `orient_path`, the superseded "v18 path orientation". The engine file is never written. The reference file states that "the engine itself is not patched in v2.12.14", and TDR-G §6.3 keeps its historical numbers under `[conv: v18 path orientation]`, i.e. `P2`; whether `P1` is the profile TDR-G wants for new campaigns is a TDR-G decision (§11).

## 2. Exact statements

Notation: `|y|_c` is the cyclic absolute value on `ℤ_N`; `ord(y)` the additive order of `y` in `ℤ_N`; `A₀` the set of initial tokens; `S₀ = A₀ ∪ (−A₀)`; `c_t(y)` the number of nodes with token `y` after tick `t`; `M_t = Σ_y c_t(y)`.

**Event inventory (E).** Read from `tdrg-v2.12.14` §6.3. In one tick (`TDRG-DEF-CONV-TICK`) phases advance by the current tokens, the defect components are formed, and the token update is applied synchronously against the pre-update snapshot, component by component. Each component's update is one of:
- (a) a permutation of the tokens of its nodes: `TDRG-DEF-SWAP` (transposition); `TDRG-DEF-CONV-P3CYC` (successor shift along the orientation chosen by `TDRG-DEF-ORIENT`, for `P_n`);
- (b) the identity: balanced path-tie, `TDRG-DEF-CYCLE-BOUND`, a multistar under the bound or trap policies, an isolated node;
- (c) the star map of `TDRG-DEF-STAR` at one centre (clean star; `largest_center`) or at several distinct centres of one component (`all_centers`): `δ_A ← −δ_A`, and a new node `E` with `θ_E = θ_A + N/2`, `δ_E = δ_A^{pre}`.

Engine fact (`EV-CODE`, static reading of `4c94d874…`): tokens are written at four places only — line 561 (initial draw), 639 (swap), 667 (successor shift), 683–684 (star map). Components the engine labels `ambiguous_*` or `triangle_forbidden_or_wideband` change no token. The engine treats `K_{1,m}`, `m ≥ 3`, as a star; the owner text defines the star for `K_{1,3}`.

**Proposition 1 (signed token alphabet; class counts).** `[SESSION]` proposal, `[ALG]` in form. Under (E), for every policy of §6.3 and either orientation rule:
1. `δ_i(t) ∈ S₀` for every node and tick. At most `2|A₀| ≤ 2m₀` distinct tokens ever occur (eight for the engine's `m₀ = 4`).
2. Updates of type (a) and (b) leave `c` unchanged. A star event whose centre has pre-event token `x` changes `c` by exactly `c(−x) ← c(−x) + 1` (for `2x ≡ 0` this is `c(x) ← c(x) + 1`). Hence `c_t` is coordinatewise non-decreasing, and for the signed class `[x] = {x, −x}` the number of nodes in the class at time `t` equals its initial number plus the number of births so far whose centre token lay in `[x]`.

*Proof.* (a) and (b) do not change the multiset of tokens. In (c) the centre contributes one `x` before the event; after it the centre carries `−x` and the child `x`: the multiset has gained one `−x` and lost nothing. Distinct centres of one tick are distinct nodes, and components are disjoint, so the single-event statements compose. Part 1 follows by induction on `t`, since `−x ∈ S₀` whenever `x ∈ S₀`. ∎

**Corollary 1.1 (birth injection).** The multiset of tokens after a birth with centre token `x` is the multiset before it plus one `−x`. Hence the multiset of absolute pairwise advances gains exactly `{ |x + y|_c : y in the pre-event token multiset }` (`M_pre` elements, among them `|2x|_c`), all pairwise advances lie in `S₀ − S₀`, and the token sum changes by `−x` (as TDR-G SG-3 and OFN already state).

**Corollary 1.2 (birth-free segments, any number of nodes).** Along any stretch of a trajectory without a star event the multiset of tokens, hence the multiset `{|d_ij|_c}` of absolute pairwise advances, is conserved. For three nodes this is the statement of `TDRG-ALG-LEM-SPECCONS`; TDR-G records the `n`-node statement as conjectured. Under (E) it is immediate; whether (E) is the complete event inventory of the adopted rule set is for the TDR-G owner to confirm.

**Proposition 2 (free parent–child phase law).** `[SESSION]` proposal, `[ALG]` in form. Let a star event at tick `t₀` have a centre `A` with pre-event token `x`, and child `E`. Suppose that at each of the next `j` advances `A` carries `−x` and `E` carries `x` (no event at ticks `t₀+1, …, t₀+j−1` changes either token). Then after the advance of tick `t₀ + j`
$$\theta_E-\theta_A\equiv \tfrac N2+2jx \pmod N .$$
*Proof.* Immediately after the event `θ_E − θ_A = N/2`; each advance adds `δ_E − δ_A = 2x`. ∎ The pair is a defect edge at tick `t₀ + j` iff `|2jx|_c ≤ k`, and exactly antipodal iff `ord(2x)` divides `j`. Events that leave both tokens in place do not break the hypothesis — in particular the swap between `A` and `E` when `2x ≡ 0`, since then `−x = x`.

**Proposition 3 (order classification).** `ord(2x) = 1` iff `2x ≡ 0` iff `x ∈ {0, N/2}`: the separation is `N/2` at every tick, the relative advance is zero. `ord(2x) = 2` iff `2x ≡ N/2` iff `4 | N` and `x ∈ {N/4, 3N/4}`: the separation alternates between `N/2` (even `j`) and `0` (odd `j`). Hence `4x ≡ 0 (mod N)` iff `ord(2x) ≤ 2`, and these are the only tokens for which the free parent–child separation takes values in `{N/2, 0}` only. For `N ≡ 2 (mod 4)` no token has order 2. ∎

**Why none of this closes `TDRG-OPEN-SPECCONS-STAR`.**
1. *Ownership.* The OPEN, `LEM-SPECCONS` and the event definitions are TDR-G's. Only a TDR-G edition changes their status; this note is `[SESSION]`.
2. *Content.* The OPEN asks whether star blow-up "conserves, controllably extends, or breaks" the relational advance spectrum. Proposition 1 answers one kinematic part: the spectrum is not conserved, its growth at each birth is the explicit injection of Corollary 1.1, and its support is fixed at `t = 0`. It does not give an invariant of the full dynamics built from the spectrum's multiplicities; it does not say **which** centre tokens fire — that sequence depends on the phases and is the dynamical question this campaign samples; and it carries no reading of "what births physically inject" (`[INTERP]`, the owner's).
3. *Conditionality.* Both propositions rest on (E). Proposition 2 is a two-body statement under a token-persistence hypothesis; in a multi-node universe the centre of an order-1 pair is in a defect component at every tick, so further events are the rule, not the exception. Fixture T7 shows that an isolated hub whose four nodes share one token gives births for **every** token (N = 120, 60 ticks: 60 births for `x ∈ {0, 60}`, 31 for `x = 30`, between 3 and 44 for the others): hub maintenance alone does not single out `4x ≡ 0`.

Proposition 3 names a precise free-kinematic mechanism candidate. That it explains basin selection in the interacting universe is **not shown**; it is what §4 tests.

**Engine symmetry used below (owner statement, checked on the engine).** TDR-G SG-14 (importing `RTG-OFN-ALG-STAR-TOKEN-SHIFT`) states that the common token shift `δ_i ↦ δ_i + c` commutes with swaps, path shifts and ties and with the star map iff `2c ≡ 0`; it is "not a gauge". For `c = N/2` fixture T8 confirms on the engine that `(M_t)` is unchanged. Consequently, under the native law of the other coordinates, the tokens `0` and `N/2` are exchangeable, and so are `N/4` and `3N/4`: they are pooled within an order class. No other common shift is used anywhere in this design, and no result is averaged over shifts. The mirror `(θ, δ) ↦ (−θ, −δ)` is not a step symmetry (TDR-G SG-14 (ii)); `x` and `−x` are not pooled on that ground, the sign of the detuning is randomised.

## 3. The exploratory pilot (frozen, separate)

Code, data, original standard output and chronology: `evidence/az/token_resonance/pilot/` with `PROVENANCE.md`. Summary: the hypothesis was formed on a 252-run timing sample (five covariates fixed in advance were not significant; the dominant token class of its 8 tail runs was `0` or `N/4`) and tested once, with a script written before the data were complete, on an independent 2,123-run sample: tails `61/258` with a seed token satisfying `4x ≡ 0` against `11/1865` without (risk ratio 40.1, Katz 95 % 21.4–75.2; one-sided Fisher `p = 1.6·10⁻⁴⁷`). Its limits are listed in `PROVENANCE.md`; the detuned-neighbour table (`1/462`) is post hoc. The pilot is exploratory evidence for one cell and is not pooled with confirmatory data. Master seeds 5551 and 20261111 are spent.

## 4. Hypotheses

Native law `L_N`: four nodes, `θ_i(0)` and `δ_i(0)` independent and uniform on `ℤ_N` (the engine's `init_universe`, `exclude_zero_delta = False`). For a value `v`, `p(v) := P(Y = 1)` when one uniformly chosen node's token is set to `v` and everything else is native.

- **H1 (order 1).** `RD₁ := mean_{r∈{0,N/2}} p(r) − mean_{r, s=±1} p(r+s) ≥ δ*`.
- **H2 (order 2, `4 | N`).** `RD₂ := mean_{r∈{N/4,3N/4}} p(r) − mean_{r, s=±1} p(r+s) ≥ δ*`.
- **H3 (cross-cell arithmetic, `N = 122`).** H1 holds at `N = 122`; and setting a token to one of the four values nearest `N/4`, `3N/4` (`30, 31, 91, 92`; none has order 2) leaves the risk within `±δ*` of the native risk.
- `δ* = 0.05` (about one fifth of the pilot's risk difference and about eight times the pilot's non-resonant risk).

Alternatives the design separates from H1/H2: a smooth dependence on the distance to a resonant value (detuned arms); an effect of perturbing a token as such (sham arm); dependence on node labels (permutation arms); an artefact of the orientation completion (profile `P2`); a purely kinematic shift of the first contact (first-birth times and the birth-anchored output, §6.4).

## 5. Design

**Cells and sizes (Stage 1; all fixed before any run).**

| Cell | N | k | Profile | Base draws | Arms | Runs |
|---|---|---|---|---|---|---|
| C1 (primary) | 120 | 8 | P1 | 0–1499 | BASE, O1R, O1D, O2R, O2D, SHAM; BASE_P and O1R_P for base draws 0–199 | 9,400 |
| C2 (cross-cell) | 122 | 8 | P1 | 0–1499 | BASE, O1R, O1D, Q2R, SHAM | 7,500 |
| C3 (sensitivity) | 120 | 8 | P2 | 0–499, the same states as C1 | BASE, O1R, O1D, O2R, O2D, SHAM | 3,000 |

Common: policy `bound_symmetric`; `T = 800` ticks; stop at `M ≥ 300` (the engine's `max_nodes`, checked before and after each tick as in `run_one`); four initial nodes.

**Base draw and arms.** Base draw `b` is the engine's native draw from the run seed `sha256("AZ-TOKRES-S1|N<N>|k<k>|base|<b>")[0:8] mod 10¹²`. A second stream, seeded from `…|arm|<b>`, chooses the slot `j ∈ {0,1,2,3}`, `r₁ ∈ {0, N/2}`, `r₂ ∈ {N/4, 3N/4}` (C2: one of the four near-quarter values), the signs `s₁, s₂, s₃ ∈ {+1, −1}` and a permutation of the four labels. Arms: `BASE` native; `O1R`: `δ_j := r₁`; `O1D`: `δ_j := r₁ + s₁`; `O2R`: `δ_j := r₂`; `O2D`: `δ_j := r₂ + s₂`; `Q2R`: `δ_j := r₂` (near-quarter); `SHAM`: `δ_j := δ_j + s₃`; `BASE_P`, `O1R_P`: the same states with permuted node labels. Every arm of a base draw has the same `θ(0)` and the same three other tokens. Each resonant arm is a draw from the native law conditioned on the slot's value, so the design oversamples the rare exposure without leaving the native ensemble: C1 and C2 have equal power although a native draw contains a `4x ≡ 0` token with probability 12.68 % at `N = 120` and 6.40 % at `N = 122`.

**Exposure categories.** Slot class: `O1` (`2x ≡ 0`), `O2` (`2x ≡ N/2`), `NR`. Alphabet class of a run: by the four initial tokens, `NR`, `O1`, `O2`, `O1+O2`. The other three tokens are native and may be resonant by chance; the registered contrasts keep such pairs (they are part of the estimand); S5 repeats the contrasts without them.

**Sample size.** 1,500 pairs per contrast. If the resonant risk is at least 0.15 and the detuned risk at most 0.02, the 97.5 % interval has half-width about 0.022 and the registered support criterion is met with near certainty; if the two risks are equal near the pilot's non-resonant level, the half-width is about 0.007 and the registered refutation criterion is met. A true difference between about 0.035 and 0.065 would probably end as inconclusive, and will be reported so.

**Stopping, censoring, exclusions.** The campaign stops when every registered `(base, arm)` record exists; the runner prints only counts and seconds, and the analysis script refuses an incomplete set. `Y` is defined for every run (a run stopped at 300 nodes has `Y = 1`); there is no censoring of the primary endpoint. No run is excluded on its outcome. A run that raises an error is rerun from the same seed; if the error is deterministic the base draw is removed from all arms with `--exclude-base` and reported. The birth-anchored output has its own explicit states (§6.4).

**Seeds not to be reused.** Spent: 5551, 20261111 (pilot); tags `FIXTURE`, `SMOKE` (this package) and `PROBE` (a 40-base-draw scratch probe of the runner, not kept). The tag `AZ-TOKRES-S1` has not been run: the runner refuses registered tags without `--confirmatory`.

**Amendments.** Any change to §§4–6 before data exist is made in this file by a commit and listed in §12. A change after confirmatory data exist is a deviation and is labelled as such in the report.

## 6. Analysis plan

Implemented by `evidence/az/scripts/az_tokres_analyse.py`; its output is reported verbatim.

### 6.1 Primary endpoint and contrasts (cell C1)

`Y = 1{M ≥ 100}` with `M` the node count when the run stops (`M_t` never decreases, so this is `1{max_{t≤800} M_t ≥ 100}`, the pilot's tail).

- **PC1** `O1R` against `O1D`; **PC2** `O2R` against `O2D`; paired on the base draw.
- Test: exact two-sided McNemar test on the discordant pairs; Holm adjustment over {PC1, PC2} at family level 0.05.
- Estimate: `RD = (b − c)/n`; interval: Agresti–Min adjusted Wald interval for matched proportions at 97.5 % two-sided (simultaneous 95 % for the two contrasts).
- **Registered reading, per contrast.** *Supported*: Holm `p < 0.05` and lower limit `> δ*`. *Not supported at the registered size*: upper limit `< δ*`. Otherwise *inconclusive* — which is not a refutation and is reported as insufficient resolution.

### 6.2 Cross-cell family (cell C2)

- **PC3** `O1R` against `O1D` at `N = 122`: same test, interval and reading as PC1.
- **PC4** `Q2R` against `BASE`: *equivalent* if the 97.5 % interval lies inside `(−δ*, +δ*)`; otherwise *not shown equivalent*.

### 6.3 Secondary outputs (nominal 95 %, descriptive; no confirmatory reading)

S1 pooled `4x ≡ 0` contrast (mean of the two resonant arms minus mean of the two detuned arms; bootstrap over base draws, fixed seed). S2 native association in the `BASE` arm by alphabet class, with the risk ratio "any `4x ≡ 0` seed against none" (Katz interval) — the pilot's quantity. S3 detuned and resonant arms against `BASE`; `SHAM` against `BASE` on base draws whose native and sham alphabets are non-resonant. S4 resonant arms by value (`0` vs `N/2`; `N/4` vs `3N/4`; the four near-quarter values). S5 the contrasts on pairs whose other three tokens are non-resonant. S6 thresholds `M ≥ 60, 80, 150, 200, 300`. S7 share of the largest signed token class at the end, by arm and outcome. S9 label-permutation control. S10 first-birth step by arm. Sensitivity: C3 against C1 run by run, and the contrasts recomputed under `P2`.

### 6.4 TDR-26 birth-anchored rule — separate, source-scoped output (S8)

Definitions taken from the classifier script: over the ticks `fb ≤ t < fb + 200` (`fb` = first tick with a birth), `b/step = Σ births / (number of ticks)`, `ms_abs = Σ occ_clean_pairs_in_multistar / Σ occ_clean_pairs`; rule positive iff `b/step ≥ 0.30` and `ms_abs ≤ 0.25`. Each run is reported in exactly one state: *not applicable* (no birth), *censored* (the run stopped before the 200-tick window was complete), *rule positive* or *rule negative*, cross-tabulated with `Y` and arm. The thresholds were chosen by TDR-G at `N = 720`, `k = 48`, `T = 5000` on two runs; at `N = 120` the output is descriptive and validates nothing. Validation in the source's own scope is Stage 3 (§10) and needs TDR-G.

### 6.5 Integrity gates (reported first)

G1 the fixtures pass on the machine that runs the campaign (same hashes as §9). G2 the summed law-violation counter of Proposition 1 is zero over all runs; a non-zero value falsifies Proposition 1 for this engine and stops the interpretation. G3 the label-permutation control shows no difference under `P1`; a difference is reported to TDR-G as a covariance defect of the profile and the contrasts are then read as conditional on the labelling. G4 the sham interval contains zero; otherwise the detuned arm is not a neutral comparator and PC1/PC2 are read as effects of a token replacement, not of the resonant value. G5 the detuned arms' intervals against `BASE` contain zero; otherwise the resonance is not sharp at distance 1 and the report says so.

### 6.6 What a result would and would not mean

A supported H1/H2 is a `[NUM]` statement about this engine, profile, cells, horizon and threshold. It is not a statement about the TDR-26 defective basin, about `N`-scaling, about other policies, or about any continuous-branch quantity; it is not a bridge observable (OPEN-P1 untouched) and has no relation to AZ's Hashimoto `4 | q` rule or to Dyadic/DZT `q = 4` beyond the numeral (SG-AZ-7, SG-DZT-1). Whether it counts towards AZ-2, and at what grade it enters any DSN, is decided later by the owners and the PI.

## 7. Instrument validation — what was executed, and what was not

Executed on 11 Nov 2026 (Linux container, Python 3.13.18), outputs in `evidence/az/token_resonance/fixtures/`:

| Test | Content | Result |
|---|---|---|
| T1 | pins of engine and orientation reference; two orientation bindings on one unmodified module | pass |
| T2 | the runner's loop reproduces the engine's `run_one` (final θ, δ, births, steps, cap flag): 24 runs, both profiles, two policies | 0 differ |
| T3 | constructed `P₃` state with `S = 0`, `E = N/2`: built-in orientation rotates the tokens, `TDRG-DEF-ORIENT` returns the balanced tie | pass |
| T4 | collecting the motif row (needed for §6.4) does not change the dynamics: 30 runs | 0 differ |
| T5 | Proposition 1 on 120 fixture runs (two policies), 15,965 births; negative control: an injected foreign token is detected | 0 violations; control fires |
| T6 | Propositions 2–3 on the engine: post-birth pair, all tokens, `(N,k)` = (24,1), (24,3), (120,8), (122,8): separation `N/2 + 2jx` until the first band return, first swap at `τ(x)` | 290 tokens, pass |
| T7 | isolated same-token hub, births in 60 ticks for every token, `N = 120, 122`; equals the golden file | pass |
| T8 | `δ ↦ δ + N/2` on all nodes leaves `(M, births, steps, fb, M_at)` unchanged: 30 runs | 0 differ |
| T9 | permuting the four initial labels leaves the same summary unchanged under `P1`: 20 runs | 0 differ |
| T10 | seed derivation, native draws and 12 run summaries equal the golden file (cross-platform determinism check) | pass |
| T11 | exhaustive: all four-node initial states with `θ₀ = 0`, `N = 6`, `k = 0`, 16 ticks, cap 24 | 279,936 states, 22,752 with a birth, 112,264 births, 0 violations |
| T11b | exhaustive: `N = 8`, `k = 1`, same horizon (separate run, about 16 minutes) | 2,097,152 states, 1,860,288 with a birth, 7,829,856 births, 0 violations |
| analysis | `--selftest`: counts, risk difference, Agresti–Min interval, exact McNemar, Holm, Wilson, Katz and the three registered readings on synthetic input | pass |
| smoke | tag `SMOKE`: 24 base draws at C1 settings, 12 at C2, 12 under `P2`; analysis run with the output marked as not confirmatory where partial | ran; timing below |

One instrument defect was found and fixed from the smoke output: the plain Wald interval has zero width when there is no discordant pair; it was replaced by the Agresti–Min interval before registration. The smoke files contain outcome data of 288 runs with other seeds; they were seen. No hypothesis, endpoint, arm, threshold or sample size was changed after seeing them.

**Not executed:** any run with tag `AZ-TOKRES-S1`; any run at `N ≥ 240`; any TDR-26-scope run; the reconstruction of r43/r31; the fixtures and the PowerShell block on Windows.

Earlier machine checks of Proposition 1 that are part of the frozen pilot, not of this package: 3,000 runs, five policies, both orientation bindings, 463,193 births, no violation.

## 8. Exact commands

From the repository root. `E`, `O`, `R`, `X`, `A` are the engine, orientation reference, runner, fixtures and analysis scripts.

**Verification of this package (reviewer; about 3 minutes, plus T11b):**
```bash
E=upload/tdrg-records/genesis_mode_b_mc.py; O=evidence/tdrg/scripts/tdrg_orient_v2_12_14.py
R=evidence/az/scripts/az_tokres_run.py; X=evidence/az/scripts/az_tokres_fixtures.py; A=evidence/az/scripts/az_tokres_analyse.py
F=evidence/az/token_resonance/fixtures
(cd evidence/az/token_resonance && sha256sum -c SHA256SUMS)
python3 -I $A --selftest
python3 -I $X --engine $E --orient $O --runner $R --golden $F/golden.json --exhaustive N6k0
python3 -I $X --engine $E --orient $O --runner $R --golden $F/golden.json --exhaustive N8k1     # optional, long
python3 -I $R --engine $E --orient $O --out /tmp/smoke.jsonl --tag SMOKE --N 120 --k 8 --stop 24 --n-perm 6
python3 -I $A --cell N120k8 --profile P1 --n-base 24 --n-perm 6 /tmp/smoke.jsonl   # compare with $F/smoke_analysis_N120k8.txt (first block)
```
The smoke records are reproducible in every field except `secs`.

**Stage 1 campaign (PI's Windows machine, PowerShell; only after the PI's authorisation).** Four parallel shards per cell; adjust `$S` to the number of cores.
```powershell
$E="upload\tdrg-records\genesis_mode_b_mc.py"; $O="evidence\tdrg\scripts\tdrg_orient_v2_12_14.py"
$R="evidence\az\scripts\az_tokres_run.py"; $X="evidence\az\scripts\az_tokres_fixtures.py"; $A="evidence\az\scripts\az_tokres_analyse.py"
$D="az_tokres_stage1"; New-Item -ItemType Directory -Force $D | Out-Null
python -I $X --engine $E --orient $O --runner $R --golden evidence\az\token_resonance\fixtures\golden.json   # must end: FIXTURES PASS
function Run-Cell($name,$N,$prof,$stop,$nperm,$S) {
  $step=[int]($stop/$S); $p=@()
  0..($S-1) | ForEach-Object { $a=$_*$step; $b=$a+$step
    $p += Start-Process python -NoNewWindow -PassThru -ArgumentList @("-I",$R,"--engine",$E,"--orient",$O,"--out","$D\${name}_$a.jsonl","--tag","AZ-TOKRES-S1","--N",$N,"--k","8","--profile",$prof,"--start",$a,"--stop",$b,"--n-perm",$nperm,"--confirmatory") }
  $p | Wait-Process }
Run-Cell "C1_N120k8_P1" 120 "P1" 1500 200 4
Run-Cell "C2_N122k8_P1" 122 "P1" 1500 0 4
Run-Cell "C3_N120k8_P2" 120 "P2" 500 0 4
Get-FileHash $D\* -Algorithm SHA256 | Format-Table -AutoSize | Out-File $D\HASHES.txt -Width 300
python -I $A --cell N120k8 --profile P1 --n-base 1500 --n-perm 200 --compare-profile P2 (Get-ChildItem $D\C1_*.jsonl,$D\C3_*.jsonl).FullName | Out-File -Encoding utf8 $D\analysis_C1.txt
python -I $A --cell N122k8 --profile P1 --n-base 1500 (Get-ChildItem $D\C2_*.jsonl).FullName | Out-File -Encoding utf8 $D\analysis_C2.txt
```
An interrupted shard is continued with the same command plus `--resume`. The directory `az_tokres_stage1` comes back unchanged on a branch `upload/az-token-resonance-stage1` and is hash-checked before placement (CONVENTIONS §6); the analysis is then rerun from the placed files by the co-owner and, independently, by the reviewer.

## 9. Evidence manifest

`evidence/az/token_resonance/SHA256SUMS` lists every file of the package (scripts by relative path). Key hashes at this draft:

| File | Path | SHA-256 |
|---|---|---|
| runner | `evidence/az/scripts/az_tokres_run.py` | `ad52a20d7cb8d94b1e0786a67702f8320eb7f9ac92ed7a2bfe74907ffc2372af` |
| fixtures script | `evidence/az/scripts/az_tokres_fixtures.py` | `ddbbf1eeaff71124e97c9c0e1eb999846284465a766a781898492884e94220a8` |
| analysis script | `evidence/az/scripts/az_tokres_analyse.py` | `7fc9ecd7b516cfabdae6de9ef0844eb7b53b15801e0971290685e43a806449b0` |
| golden file | `evidence/az/token_resonance/fixtures/golden.json` | `40eba43073fba138130244f75cc0790ef20bffcbeda7599ff4e372b95427c134` |
| fixtures output (with T11, N=6) | `evidence/az/token_resonance/fixtures/fixtures_output.txt` | `d5201a6629b55d361cb3eda7c69f6b5f2203413f2afc46209ef23c2282f9c57a` |
| fixtures output (with T11b, N=8) | `evidence/az/token_resonance/fixtures/fixtures_output_exhaustive_N8k1.txt` | `0c25e603bd932e0413e99f123d9456d9e7e3fb404bcfdd7eac042729f75ed78c` |
| smoke records C1 settings | `evidence/az/token_resonance/fixtures/smoke_N120k8_P1.jsonl` | `b52591213bc047d38b6de5b02d88bd62bc8f8bf911b217424f634ea84993a9de` |
| smoke records C2 settings | `evidence/az/token_resonance/fixtures/smoke_N122k8_P1.jsonl` | `7563ec9a33badeb7a10566129dce0efebba8ef5bbd02431ef4ce7caf3a6c625d` |
| smoke records P2 | `evidence/az/token_resonance/fixtures/smoke_N120k8_P2.jsonl` | `cda6cb95f0d21b78d78ecf6c98993ad71535160894c13947f9460ffd931079d3` |
| pilot data, 252 runs | `evidence/az/token_resonance/pilot/pilot_time.jsonl` | `8b11130b321ce021110beadfd9ce15cbfd1430ce440ab6af4ce1c3afab36d043` |
| pilot data, 2,123 runs | `evidence/az/token_resonance/pilot/pilot_N120.jsonl` | `d2bba5abb07988dfc2ee72107bf99f22a8e2b64a65cff7c477862a04dc2c5dda` |
| pilot script | `evidence/az/token_resonance/pilot/pilot.py` | `c7e317584723e6841c0aeb83870bd5f86607a8126a3531d2db27c664f5708d77` |
| pilot test script | `evidence/az/token_resonance/pilot/analyse3.py` | `54302092f3d7802a585c700d919e3def5ed60139338f9ac6e7b8edb2eec93701` |
| pilot provenance | `evidence/az/token_resonance/pilot/PROVENANCE.md` | `c0cc703fe739e21a279e59b6f5782b922e38fcc616bed594c34fe19dc428e2d6` |

`SHA256SUMS` covers 32 files: the three scripts, 11 fixture files and the frozen pilot (11 original files, 6 regenerated or reconstructed, `PROVENANCE.md`). Check: `cd evidence/az/token_resonance && sha256sum -c SHA256SUMS`.

Fields of a run record: `schema`, `tag`, `cell`, `N`, `k`, `T`, `cap`, `profile`, `policy`, `base`, `arm`, `seed`, `slot`, `choices`, `th0`, `d0` (state actually run), `d0_base` (native tokens), `alphabet_class`, `slot_class`, `M`, `births`, `steps`, `hit_cap`, `fb`, `fe`, `t100`, `M_at`, `census`, `top_class`, `top_share`, `law_viol`, `swaps`, `paths`, `path_ties`, `ms_seen`, `ms_bound`, `ambiguous`, `tdr26`, `secs`.

## 10. Proposed campaign and run counts

| Stage | Content | Runs | Cost | State |
|---|---|---|---|---|
| 1 | C1, C2, C3 as registered in §5 | 19,900 | smoke timing here: 0.39 s (C1), 0.21 s (C2), 0.27 s (C3) per run on one core of a two-core container, with a second job running: about 1.7 core-hours; to be confirmed by the fixtures' and first shard's timing on the PI's machine | registered; waits for the PI's authorisation |
| 2 | `N ∈ {240, 242, 480}` at `k/N ≈ 1/15` (`k = 16, 16, 32`), same arms, 1,000 base draws per cell | 6,000 / 5,000 / 6,000, plus calibration | unknown; a timing probe of 20 base draws per cell comes first | **proposal only.** `T` and the threshold of `Y` are not known for these cells and are not frozen. Proposed: `T = 800`; threshold `⌈2.5 × median M⌉` of 500 native runs with a separate tag (exposure-blind; at `N = 120` this gives 103 against the registered 100). To be fixed by an amendment after Stage 1 is reviewed. |
| 3 | TDR-26 in its own scope: `N = 720`, `k = 48` and `N = 722`, `k = 48`, `T = 5000`, arms O1R, O1D (and O2R, O2D at 720), birth-anchored rule as the endpoint, 200 base draws per cell | 800 + 400 | unknown, large; timing probe first | **proposal only; needs the TDR-G owner** (engine profile, node cap, rule thresholds, relation to TDR-G's own campaign specification of batch ≥ 500) |
| — | r43 (`N = 720`) and r31 (`N = 722`): do their initial tokens contain a `4x ≡ 0` value? | 0 new runs | negligible | **not executable now.** The v17 `N = 720/722` files are held outside the repository and their command line and master seed are not recorded in TDR-G §8. If the PI supplies the exact command (engine, `--seed`, grid arguments, batch), the run seeds follow from the engine's `monte_carlo` and the initial tokens from `init_universe`, without running the dynamics. Under independence the chance that both runs contain such a token is about `0.022 × 0.011 ≈ 2.4·10⁻⁴`. |

## 11. Dependencies, firewalls, and a proposed pipe item (not filed)

- **TDR-G** owns the rules, the OPENs and the engine. Needed from TDR-G before any use beyond AZ's own diagnostic: its verdict on Propositions 1–3 and on (E); whether `P1` is its profile for new campaigns; Stage 3. This note does not ask TDR-G to change anything.
- **OFN**: no decision needed. The design uses the residual `2c ≡ 0` case of `RTG-OFN-ALG-STAR-TOKEN-SHIFT` as TDR-G imports it.
- **PI**: authorisation of Stage 1; the v17 command line for r43/r31; whether the item below is filed.
- **Dyadic, DZT, Genesis, NUMGEN, LIT**: none.
- Methodology: AZ v0.7 declares v1.2; this note uses the v1.4 evidence keys of CONVENTIONS §5 for its own files. It is not a DSN edition.

Proposed text for `pipes/TDRG/` — **not filed in this PR**:
> `from: AZ · to: TDRG · kind: offer · object: TDRG-OPEN-SPECCONS-STAR; TDRG-ALG-LEM-SPECCONS (n-node conjecture); TDRG-OPEN-LOCKING-FAIL · tags: [tdrg-v2.12.14, az-v0.7]`
> AZ offers, as a `[SESSION]` proposal, a signed-token-alphabet law and class-count update under the §6.3 event inventory, with a birth-injection corollary and the birth-free `n`-node corollary (`records/az/AZ_TOKEN_RESONANCE_PREREGISTRATION.md` §2; fixtures `evidence/az/token_resonance/fixtures/`). It does not close the OPEN. AZ has registered a campaign on the placed engine with `TDRG-DEF-ORIENT` that reports the TDR-26 birth-anchored rule as a separate output. Needed from TDR-G: a verdict on the statement and on the completeness of the event inventory; nothing blocks.

## 12. Review request and amendment log

Requested from the independent reviewer (ChatGPT): (1) the proofs of §2 and the list of what they do not close; (2) the estimand, arms and the conditional-sampling argument of §5; (3) the registered readings of §6, the choice `δ* = 0.05` and the interval; (4) the fixtures and commands, by rerunning §8; (5) whether the pilot is adequately separated; (6) anything in §§4–6 that should change **before** data exist.

Decision points: this PR → independent review → PI decision on Stage 1. No merge, tag or adoption is implied by the PR.

Amendments: none yet (draft r1).
