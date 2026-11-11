# AZ Action 1 — Token Resonance and Basin Selection: preregistration and test package

**[SESSION] NONCANONICAL. Draft r2 (amended before any confirmatory data, in answer to the independent review `5855522171`; accepted, scoped, by the readback `5857601141`; log in §12); nothing here is adopted and no campaign is authorised by a review.** Prepared by the AZ co-owner (Claude) on 11 November 2026 on the PI's message of that day (10:00 +03:00), which relayed the task "Proceed with AZ Action 1 — Token Resonance and Basin Selection, as selected by the PI" together with the co-owner review (ChatGPT) of the BOOTSTRAP 4 advisory. Branch `claude/az-token-resonance-prereg`. It edits no DSN, closes no pipe item, claims no TDR-G result and authorises no campaign: the PI decides on the confirmatory run after the independent review.

Governing sources: AZ `az-v0.7` (file SHA-256 `2294d2a3…fc94`), TDR-G `tdrg-v2.12.14` (file SHA-256 `3be72923…2392`, §§6.1–6.3, §6.5, §6.12, SG-11–SG-14). Every statement about TDR-G dynamics below is a proposal to the TDR-G owner; `TDRG-OPEN-SPECCONS-STAR` and `TDRG-OPEN-LOCKING-FAIL` (TDR-26) stay open and stay TDR-G's (SG-AZ-6).

## 0. What is registered, in one paragraph

On the pinned TDR-G engine with the adopted orientation rule, at `N = 120`, `k = 8`, policy `bound_symmetric`, the outcome `Y = 1{max_{t≤800} M_t ≥ 100}` is compared between runs whose initial state differs in **one token only**: a resonant value (`2x ≡ 0`, or `2x ≡ N/2`) against its neighbour `x ± 1`, with the same initial phases and the same other three tokens. Two contrasts form the only confirmatory family (order 1 and order 2, tested separately). The cell `N = 122` (where no order-2 token exists) is a separate, supportive replication family. A node-label permutation, a sham perturbation and the detuned comparator are control contrasts with a declared neutrality margin; they qualify every reading. The pooled `4x ≡ 0` contrast, the native-ensemble association, the superseded orientation rule and the TDR-26 birth-anchored rule are descriptive outputs. The registered minimal effect is a risk difference of `0.05`. Sample size is fixed in advance (1,500 base draws per cell); there is no interim look. The analysis is fail-closed: it prints no estimate and no reading unless identity, custody, initial states, record consistency, completeness and two gates have passed. What a supported contrast would establish is the causal effect of the token replacement at this engine, profile and horizon — not a mechanism.

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

**Corollary 1.1 (birth injection).** *One birth in the tick.* The multiset of tokens after a birth with centre token `x` is the multiset before it plus one `−x`. Hence the multiset of absolute pairwise advances gains exactly `{ |x + y|_c : y in the pre-event token multiset }` (`M_pre` elements, among them `|2x|_c`). *Several births in one tick*, centre tokens `x_1, …, x_m` (all read from the pre-update snapshot): the token multiset gains `{−x_1, …, −x_m}`, and the pairwise multiset gains the pairs between the new tokens and the pre-event multiset **and** the pairs among the new tokens: `{ |x_a + y|_c : 1 ≤ a ≤ m, y pre-event } ∪ { |x_a − x_b|_c : a < b }`, that is `m·M_pre + m(m−1)/2` elements. Applying the one-birth formula `m` times against the unchanged pre-event multiset would miss the second set. In every case all pairwise advances lie in `S₀ − S₀`, and the token sum changes by `−Σ x_a` (as TDR-G SG-3 and OFN already state for one birth).

**Corollary 1.2 (birth-free segments, any number of nodes).** Along any stretch of a trajectory without a star event the multiset of tokens, hence the multiset `{|d_ij|_c}` of absolute pairwise advances, is conserved. For three nodes this is the statement of `TDRG-ALG-LEM-SPECCONS`; TDR-G records the `n`-node statement as conjectured. Under (E) it is immediate; whether (E) is the complete event inventory of the adopted rule set is for the TDR-G owner to confirm.

**Proposition 2 (free parent–child phase law).** `[SESSION]` proposal, `[ALG]` in form. Let a star event at tick `t₀` have a centre `A` with pre-event token `x`, and child `E`. Suppose that at each of the next `j` advances `A` carries `−x` and `E` carries `x` (no event at ticks `t₀+1, …, t₀+j−1` changes either token). Then after the advance of tick `t₀ + j`
$$\theta_E-\theta_A\equiv \tfrac N2+2jx \pmod N .$$
*Proof.* Immediately after the event `θ_E − θ_A = N/2`; each advance adds `δ_E − δ_A = 2x`. ∎ The pair is a defect edge at tick `t₀ + j` iff `|2jx|_c ≤ k`, and exactly antipodal iff `ord(2x)` divides `j`. Events that leave both tokens in place do not break the hypothesis — in particular the swap between `A` and `E` when `2x ≡ 0`, since then `−x = x`.

**Proposition 3 (order classification).** `ord(2x) = 1` iff `2x ≡ 0` iff `x ∈ {0, N/2}`: the separation is `N/2` at every tick, the relative advance is zero. `ord(2x) = 2` iff `2x ≡ N/2` iff `4 | N` and `x ∈ {N/4, 3N/4}`: the separation alternates between `N/2` (even `j`) and `0` (odd `j`). Hence `4x ≡ 0 (mod N)` iff `ord(2x) ≤ 2`, and these are the only tokens for which the free parent–child separation takes values in `{N/2, 0}` only. For `N ≡ 2 (mod 4)` no token has order 2. ∎

**Why none of this closes `TDRG-OPEN-SPECCONS-STAR`.**
1. *Ownership.* The OPEN, `LEM-SPECCONS` and the event definitions are TDR-G's. Only a TDR-G edition changes their status; this note is `[SESSION]`.
2. *Content.* The OPEN asks whether star blow-up "conserves, controllably extends, or breaks" the relational advance spectrum. Proposition 1 answers one kinematic part: the spectrum is not conserved, its growth at each birth is the explicit injection of Corollary 1.1, and its support is fixed at `t = 0`. It does not give an invariant of the full dynamics built from the spectrum's multiplicities; it does not say **which** centre tokens fire — that sequence depends on the phases and is the dynamical question this campaign samples; and it carries no reading of "what births physically inject" (`[INTERP]`, the owner's).
3. *Conditionality.* Both propositions rest on (E). Proposition 2 is a two-body statement under a token-persistence hypothesis; in a multi-node universe the centre of an order-1 pair is in a defect component at every tick, so further events are the rule, not the exception. Fixture T7 shows that an isolated hub whose four nodes share one token gives births for **every** token (N = 120, 60 ticks: 60 births for `x ∈ {0, 60}`, 31 for `x = 30`, between 3 and 44 for the others): hub maintenance alone does not single out `4x ≡ 0`.

Proposition 3 names a precise free-kinematic mechanism candidate. That it explains basin selection in the interacting universe is **not shown**, and the campaign of §§4–6 does not test the mechanism either: it estimates the effect of a token replacement (§6.6).

**What the machine checks cover, and what they do not.** The runner checks at every tick of every run: (i) all tokens lie in `S₀`; (ii) the exact class update — the census after the tick equals the census before it plus one count at `−x` for every node born in the tick, `x` being the newborn's token; (iii) for every newborn a node at its antipode carries `−x` (the centre). (ii) is the per-birth statement of Proposition 1, not only "no count decreases and the total grows by the births"; fixture T5b shows a corrupted birth that passes the weaker checks and is caught by (ii). These checks are `[NUM]`-type evidence about the pinned engine on the states actually run (§7); they are not a proof, they are conditional on the engine implementing (E), and they do not establish the multi-birth pairwise formula of Corollary 1.1 separately (it follows from the census update by counting).

**Engine symmetry used below (owner statement, checked on the engine).** TDR-G SG-14 (importing `RTG-OFN-ALG-STAR-TOKEN-SHIFT`) states that the common token shift `δ_i ↦ δ_i + c` commutes with swaps, path shifts and ties and with the star map iff `2c ≡ 0`; it is "not a gauge". For `c = N/2` fixture T8 confirms on the engine that `(M_t)` is unchanged. Consequently, under the native law of the other coordinates, the tokens `0` and `N/2` are exchangeable, and so are `N/4` and `3N/4`: they are pooled within an order class. No other common shift is used anywhere in this design, and no result is averaged over shifts. The mirror `(θ, δ) ↦ (−θ, −δ)` is not a step symmetry (TDR-G SG-14 (ii)); `x` and `−x` are not pooled on that ground, the sign of the detuning is randomised.

## 3. The exploratory pilot (frozen, separate)

Code, data, original standard output and chronology: `evidence/az/token_resonance/pilot/` with `PROVENANCE.md`. Summary: the hypothesis was formed on a 252-run timing sample (five covariates fixed in advance were not significant; the dominant token class of its 8 tail runs was `0` or `N/4`) and tested once, with a script written before the data were complete, on an independent 2,123-run sample: tails `61/258` with a seed token satisfying `4x ≡ 0` against `11/1865` without (risk ratio 40.1, Katz 95 % 21.4–75.2; one-sided Fisher `p = 1.6·10⁻⁴⁷`). Its limits are listed in `PROVENANCE.md`; the detuned-neighbour table (`1/462`) is post hoc. The pilot is exploratory evidence for one cell and is not pooled with confirmatory data. Master seeds 5551 and 20261111 are spent.

## 4. Hypotheses

Native law `L_N`: four nodes, `θ_i(0)` and `δ_i(0)` independent and uniform on `ℤ_N` (the engine's `init_universe`, `exclude_zero_delta = False`). For a value `v`, `p(v) := P(Y = 1)` when one uniformly chosen node's token is set to `v` and everything else is native.

- **H1 (order 1).** `RD₁ := mean_{r∈{0,N/2}} p(r) − mean_{r, s=±1} p(r+s) ≥ δ*`.
- **H2 (order 2, `4 | N`).** `RD₂ := mean_{r∈{N/4,3N/4}} p(r) − mean_{r, s=±1} p(r+s) ≥ δ*`.
- **H3 (cross-cell arithmetic, `N = 122`).** H1 holds at `N = 122`; and setting a token to one of the four values nearest `N/4`, `3N/4` (`30, 31, 91, 92`; none has order 2) leaves the risk within `±δ*` of the native risk.
- `δ* = 0.05` (about one fifth of the pilot's risk difference and about eight times the pilot's non-resonant risk).

Alternatives the design addresses, each through a control contrast with a declared margin or an explicit check (§6.5): a smooth dependence on the distance to a resonant value (detuned arms, G5); an effect of perturbing a token as such (sham arm, G4); dependence on node labels (permutation arms, G3); an artefact of the orientation completion (profile `P2`, descriptive). **Not separated by this design:** whether the resonant token acts during growth or through the time and manner of the first contact and first birth. First-birth times (S10) and the birth-anchored output (S8) are descriptive and identify no mediation; the mechanism stays OPEN.

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

**Stopping, censoring, exclusions.** The campaign stops when every registered `(base, arm)` record exists; the runner prints only counts and seconds; the campaign driver (§8) writes its completion marker only if the fixtures, every worker and every analysis exited with code 0, and the analysis script refuses an incomplete, duplicated or foreign set (§6.5). `Y` is defined for every run (a run stopped at 300 nodes has `Y = 1`); there is no censoring of the primary endpoint. No run is excluded on its outcome. A run that raises an error is rerun from the same seed; if the error is deterministic the base draw is removed from all arms with `--exclude-base`, which the analysis prints as a deviation and attaches as a qualifier to every reading. The birth-anchored output has its own explicit states (§6.4).

**Seeds not to be reused.** Spent: 5551, 20261111 (pilot); tags `FIXTURE` and `SMOKE` (this package; `SMOKE` is the tag of the test configuration `TEST-C1…C3` of the analysis registry) and `PROBE` (a 40-base-draw scratch probe of the runner, not kept). The tag `AZ-TOKRES-S1` has not been run: the runner refuses registered tags without `--confirmatory`.

**Amendments.** Any change to §§4–6 before data exist is made in this file by a commit and listed in §12. A change after confirmatory data exist is a deviation and is labelled as such in the report.

## 6. Analysis plan

Implemented by `evidence/az/scripts/az_tokres_analyse.py`; its output is reported verbatim. The registered parameters of every cell (tag, `N`, `k`, `T`, cap, policy, profile, numbers of base draws and permuted draws) are constants of that script (`REGISTRY`), not command-line arguments. The analysis is fail-closed (§6.5).

### 6.1 Primary endpoint and the confirmatory family (cell C1)

`Y = 1{M ≥ 100}` with `M` the node count when the run stops (`M_t` never decreases, so this is `1{max_{t≤800} M_t ≥ 100}`, the pilot's tail).

**Family 1 = {PC1, PC2} is the only confirmatory family of Stage 1.**
- **PC1** `O1R` against `O1D`; **PC2** `O2R` against `O2D`; paired on the base draw.
- Test: exact two-sided McNemar test on the discordant pairs; Holm adjustment over {PC1, PC2} at family level 0.05.
- Estimate: `RD = (b − c)/n`; interval: Agresti–Min adjusted Wald interval for matched proportions at 97.5 % two-sided (simultaneous 95 % for the two contrasts).
- **Registered reading, per contrast.** *Supported*: Holm `p < 0.05` and lower limit `> δ*`. *Not supported at the registered size*: upper limit `< δ*`. Otherwise *inconclusive* — which is not a refutation and is reported as insufficient resolution.
- Every reading is printed with its **qualifiers** (§6.5): *unqualified* only if G3 passes and G4 and the contrast's G5 read *equivalent*.

### 6.2 Supportive replication family (cell C2) — separate from family 1

**Family 2 = {PC3, PC4}** is a supportive replication at a neighbouring `N` with a different arithmetic (`N ≡ 2 mod 4`). It is evaluated on its own, with a Bonferroni correction over its two statements (97.5 % two-sided intervals; PC3's McNemar `p` doubled). It does not enlarge family 1: no confirmatory claim of Stage 1 rests on it, no joint claim over the two cells is registered, and it is reported whatever family 1 gives. If family 1 is supported and PC3 is not, the report says that the effect was not replicated at `N = 122`.
- **PC3** `O1R` against `O1D` at `N = 122`: superiority reading as in §6.1.
- **PC4** `Q2R` against `BASE`: *equivalent* if the interval lies inside `(−δ*, +δ*)`; *different* if it lies entirely beyond `±δ*`; otherwise *inconclusive*.

### 6.3 Descriptive outputs (nominal 95 %; no reading)

S1 pooled `4x ≡ 0` contrast (mean of the two resonant arms minus mean of the two detuned arms; bootstrap over base draws, fixed seed). S2 native association in the `BASE` arm by alphabet class, with the risk ratio "any `4x ≡ 0` seed against none" (Katz interval) — the pilot's quantity. S3 resonant and detuned arms against `BASE` on all base draws (the detuned-against-`BASE` difference on *all* draws is not a neutrality control: the native slot token is itself resonant in about 3 % of the draws; the control is G5). S4 resonant arms by value (`0` vs `N/2`; `N/4` vs `3N/4`; the four near-quarter values). S5 the contrasts on pairs whose other three tokens are non-resonant. S6 thresholds `M ≥ 60, 80, 150, 200, 300`. S7 share of the largest signed token class at the end, by arm and outcome. S10 first-birth step by arm — descriptive, not a mediation analysis. Sensitivity: C3 against C1 run by run, and the contrasts recomputed under `P2`, without readings.

### 6.4 TDR-26 birth-anchored rule — separate, source-scoped output (S8)

Definitions taken from the classifier script: over the ticks `fb ≤ t < fb + 200` (`fb` = first tick with a birth), `b/step = Σ births / (number of ticks)`, `ms_abs = Σ occ_clean_pairs_in_multistar / Σ occ_clean_pairs`; rule positive iff `b/step ≥ 0.30` and `ms_abs ≤ 0.25`. Each run is reported in exactly one state: *not applicable* (no birth), *censored* (the run stopped before the 200-tick window was complete), *rule positive* or *rule negative*, cross-tabulated with `Y` and arm. The thresholds were chosen by TDR-G at `N = 720`, `k = 48`, `T = 5000` on two runs; at `N = 120` the output is descriptive and validates nothing. Validation in the source's own scope is Stage 3 (§10) and needs TDR-G.

### 6.5 Integrity, gates and qualifiers

**Integrity (any failure: the errors are listed, no estimate and no reading is printed, exit code 2).** In this order:
1. *Identity.* The files given as engine, orientation reference and runner hash to the pins. Every manifest line and every record carries the registered tag, `N`, `k`, `T`, cap, policy, profile, the confirmatory flag and the three SHA-256 pins.
2. *Custody.* Every record file has a manifest whose last line states the file's SHA-256 and record count; the shards' ranges are disjoint and tile the registered base draws; shard arguments (permuted draws, arms, birth-anchored collection) are the registered ones in every invocation recorded by the manifest.
3. *States.* Seed, initial phases, initial tokens (as run and native), slot, intervention values and class labels of every record equal a re-derivation from `(tag, N, k, base, arm)` written independently in the analysis script (fixture T12 compares it with the runner and the engine's draw).
4. *Records.* `M = 4 + births`; stop rule and cap flag; `t100` and `fb` against `M` and births; census total `= M`; final census inside `S₀`; monotone checkpoints; a law-violation counter is present; birth-anchored block consistent.
5. *Set.* Every registered `(base, arm)` exactly once and nothing else. A base draw may be missing only if declared with `--exclude-base` (a deviation).

The runner refuses to continue (`--resume`) a record file written under any other identity or other shard arguments.

**Gates (a failed gate: no estimate and no reading, exit code 3).** G1: the fixtures log produced on the campaign machine shows the pinned bytes (engine, orientation reference, runner, fixtures script, golden file), contains no failed test and ends with `FIXTURES PASS`. G2: the law-violation counter (§2, "what the machine checks cover") summed over all runs, including the sensitivity set, is zero; a non-zero value contradicts Proposition 1 for this engine and is reported to TDR-G.

**Qualifiers (computed after the gates, printed before the contrasts, attached to every reading).** Control contrasts use the Agresti–Min interval at 95 % two-sided and the neutrality margin `δ_neutral = 0.025` (half of `δ*`), with the reading *equivalent* (interval inside `±δ_neutral`), *different* (interval entirely beyond the margin) or *inconclusive* (anything else). **An interval that contains zero is never, by itself, read as neutrality or equivalence.**
- **G3 node labels.** *Pass* iff no permuted run differs from its unpermuted run in `(M, births, steps, fb, M_at)`; otherwise *fail*: the readings are conditional on the labelling and the finding is reported to TDR-G as a covariance defect of the profile.
- **G4 sham.** `SHAM` against `BASE` on base draws whose native slot token and perturbed slot token are both non-resonant. *Equivalent*: shifting a non-resonant token by `±1` is neutral within the margin.
- **G5 detuned comparator, per contrast.** `O1D` (resp. `O2D`) against `BASE` on base draws whose native slot token is non-resonant, so that both arms carry a non-resonant slot token and identical other coordinates. *Equivalent*: the `±1` neighbour of a resonant value behaves like a native non-resonant token within the margin.
- A reading is **unqualified** only if G3 passes and G4 and its G5 read *equivalent*. Otherwise it is printed as *qualified by* the failing or inconclusive control, and may then be stated only as "resonant value against its `±1` neighbour", without the generalisation to "resonant against non-resonant tokens". Qualifiers do not turn one registered reading into another.
- Expected resolution if the controls are neutral: about 1,450 eligible pairs, interval half-width about 0.011.

### 6.6 What a result would and would not mean

PC1 and PC2 estimate the **total causal effect on `Y` of replacing one initial token by a resonant value rather than by its `±1` neighbour**, under the native law of all other coordinates, for this engine, profile, cell, horizon and threshold. A supported contrast is a `[NUM]` statement of exactly that. It does not identify a mechanism. In particular it does not show that the resonant token acts beyond a change in the time or manner of the first contact and first birth: S10 and S8 are descriptive and are not a mediation analysis, and Proposition 3's parent–child law remains a candidate. **The first-contact mechanism remains OPEN.**

Nor is a supported contrast a statement about the TDR-26 defective basin, about `N`-scaling, about other policies, or about any continuous-branch quantity; it is not a bridge observable (OPEN-P1 untouched) and has no relation to AZ's Hashimoto `4 | q` rule or to Dyadic/DZT `q = 4` beyond the numeral (SG-AZ-7, SG-DZT-1). Whether it counts towards AZ-2, and at what grade it enters any DSN, is decided later by the owners and the PI.

## 7. Instrument validation — what was executed, and what was not

Executed on 11 Nov 2026 (Linux container, Python 3.13.18), outputs in `evidence/az/token_resonance/fixtures/`:

| Test | Content | Result |
|---|---|---|
| T1 | pins of engine and orientation reference; two orientation bindings on one unmodified module | pass |
| T2 | the runner's loop reproduces the engine's `run_one` (final θ, δ, births, steps, cap flag): 24 runs, both profiles, two policies | 0 differ |
| T3 | constructed `P₃` state with `S = 0`, `E = N/2`: built-in orientation rotates the tokens, `TDRG-DEF-ORIENT` returns the balanced tie | pass |
| T4 | collecting the motif row (needed for §6.4) does not change the dynamics: 30 runs | 0 differ |
| T5 | law check (alphabet, exact class update `c(−x) += 1` per birth, centre witness) on 120 fixture runs, two policies, 15,965 births | 0 violations |
| T5 neg. | an injected foreign token is detected | control fires |
| T5b | a corrupted birth that adds its count at `x` instead of `−x` passes the weak checks (alphabet, no decrease, total) and is caught by the exact class update | control fires |
| T5c, T5d | a child born with `−x` is caught; the same hub without corruption has no violation | pass |
| T6 | Propositions 2–3 on the engine: post-birth pair, all tokens, `(N,k)` = (24,1), (24,3), (120,8), (122,8): separation `N/2 + 2jx` until the first band return, first swap at `τ(x)` | 290 tokens, pass |
| T7 | isolated same-token hub, births in 60 ticks for every token, `N = 120, 122`; equals the golden file | pass |
| T8 | `δ ↦ δ + N/2` on all nodes leaves `(M, births, steps, fb, M_at)` unchanged: 30 runs | 0 differ |
| T9 | permuting the four initial labels leaves the same summary unchanged under `P1`: 20 runs | 0 differ |
| T10 | seed derivation, native draws and 12 run summaries equal the golden file (cross-platform determinism check) | pass |
| T11 | exhaustive, same three checks at every tick: all four-node initial states with `θ₀ = 0`, `N = 6`, `k = 0`, 16 ticks, cap 24 | 279,936 states, 22,752 with a birth, 112,264 births, 0 violations |
| T11b | exhaustive: `N = 8`, `k = 1`, same horizon (separate, long run) | 2,097,152 states, 1,860,288 with a birth, 7,829,856 births, 0 violations |
| T12 | the analysis script's independent re-derivation of seed, phases, tokens, slot, choices and classes equals the runner's (engine draw): 600 states, all arms, `N = 120, 122`; pins and schemas agree | 0 differ |
| analysis | `--selftest`: counts, risk difference, Agresti–Min interval, exact McNemar, Holm, Wilson, Katz, superiority readings, three-way equivalence reading (including "contains zero but wider than the margin → inconclusive"), state derivation, record checks, registry | pass |
| negative controls | `az_tokres_negcontrols.py`, 51 cases on the test configuration: runner refusals (registered tag without flag, flag with other tag, engine not matching the pin, existing output, `--resume` under changed `T`, shard range or permuted draws; cut-off record repaired); analysis rejections with exit 2 (wrong tag, `T`, cap, policy, profile, engine pin, runner pin, confirmatory flag; tampered phases, token, arm label, seed, class label; edited outcome; census outside `S₀`; record removed, duplicated, of an unregistered base draw; file changed after the run; manifest missing or of another identity; shard missing or given twice; runner file not matching the pin); gate failures with exit 3 (law counter > 0; fixtures log with a failed test, of other runner bytes, or missing); no reading in exploratory or sensitivity mode; declared deviation; driver: refusals, completion marker only on success, failure of a worker, of an analysis and of the fixtures | all behave as stated; for every rejected input neither an estimate nor a reading is printed |
| test campaign | `az_tokres_campaign.py --plan test --jobs 2` (tag `SMOKE`: 24, 12 and 12 base draws at the settings of C1, C2, C3; fixtures run by the driver) | completion marker written; 288 records; analyses exit 0 with readings marked "test-configuration reading, no evidential value" |

One instrument defect was found from the first smoke output and fixed before registration (r1): the plain Wald interval has zero width when there is no discordant pair; it was replaced by the Agresti–Min interval. The test-campaign files contain outcome data of 288 runs with other seeds than the registered ones; they were seen. The 156 records at C1 settings are identical, in every dynamical field, to the smoke records of draft r1 (checked field by field before the r1 files were removed): the amended runner changes bookkeeping only. No hypothesis, endpoint, arm, seed, sample size, `δ*`, test or interval of PC1–PC4 was changed after seeing any of these outputs; the changes of draft r2 are listed in §12.

**Not executed:** any run with tag `AZ-TOKRES-S1`; any run at `N ≥ 240`; any TDR-26-scope run; the reconstruction of r43/r31; anything on the PI's Ubuntu server or on Windows (fixtures, driver, the command blocks of §8).

Earlier machine checks of Proposition 1 that are part of the frozen pilot, not of this package: 3,000 runs, five policies, both orientation bindings, 463,193 births, no violation (these used the weaker check: alphabet, no decrease, total).

## 8. Exact commands

From the repository root.

**Verification of this package (reviewer; about 6 minutes on two cores, plus T11b):**
```bash
S=evidence/az/scripts; F=evidence/az/token_resonance/fixtures
E=upload/tdrg-records/genesis_mode_b_mc.py; O=evidence/tdrg/scripts/tdrg_orient_v2_12_14.py
(cd evidence/az/token_resonance && sha256sum -c SHA256SUMS)
python3 -I $S/az_tokres_analyse.py --selftest
python3 -I $S/az_tokres_fixtures.py --engine $E --orient $O --runner $S/az_tokres_run.py --analysis $S/az_tokres_analyse.py --golden $F/golden.json --exhaustive N6k0
python3 -I $S/az_tokres_negcontrols.py --work /tmp/az_negcontrols            # must end: NEGATIVE CONTROLS PASS (51 cases ...)
python3 -I $S/az_tokres_campaign.py --plan test --jobs 2 --out /tmp/az_test_campaign   # must end: CAMPAIGN COMPLETE
diff <(grep -v -e SHA-256 /tmp/az_test_campaign/analysis_TEST-C1.txt) <(grep -v -e SHA-256 $F/test_campaign/analysis_TEST-C1.txt)
python3 -I $S/az_tokres_fixtures.py --engine $E --orient $O --runner $S/az_tokres_run.py --analysis $S/az_tokres_analyse.py --golden $F/golden.json --exhaustive N8k1     # optional, long
```
The test-campaign records are reproducible in every field except `secs`; the analysis output is reproducible except for the SHA-256 lines of the record files (they contain `secs`).

**Stage 1 campaign (only after the PI's authorisation).** One command; the driver runs the fixtures, the three cells as parallel shards and the analyses, checks every exit code and every shard, and writes `CAMPAIGN_COMPLETE.json` only if all of it succeeded. `--jobs` is the number of parallel workers; **it must be the same on `--resume`** (another worker count gives differently named shards and leaves obsolete files in the directory).

*Venue: the PI's Ubuntu server* (PI, 11 Nov 2026, 14:02 +03:00: large computations run on the Ubuntu server). The block writes a small script to the home directory and runs it in a fresh `bash`, so that it stops at the first failure whatever the calling shell is. It runs the reviewed bytes and hands the directory over unchanged on an upload branch:
```bash
cat > ~/az_tokres_stage1.sh <<'AZ_STAGE1'
set -euo pipefail
cd ~/rtg-corpus
test -z "$(git status --porcelain)" || { echo "STOP: working tree not clean"; exit 1; }
trap 'git checkout -q main' EXIT
git fetch -q origin
git checkout -q --detach origin/claude/az-token-resonance-prereg
git log --oneline -1; python3 --version; nproc
( cd evidence/az/token_resonance && sha256sum -c --quiet SHA256SUMS )
echo "package bytes OK"
OUT="$HOME/az_tokres_stage1"; JOBS=4
python3 -I evidence/az/scripts/az_tokres_campaign.py --plan stage1 --jobs "$JOBS" --out "$OUT" --confirmatory ${AZ_RESUME:+--resume}
test -f "$OUT/CAMPAIGN_COMPLETE.json"
( cd "$OUT" && sha256sum -c --quiet HASHES.txt )
echo "campaign hashes OK"
cat "$OUT/CAMPAIGN_COMPLETE.json"
git checkout -q -b upload/az-token-resonance-stage1 origin/main
mkdir -p upload/az-token-resonance-stage1
cp -r "$OUT"/. upload/az-token-resonance-stage1/
git add upload/az-token-resonance-stage1
git commit -q -m "upload: AZ token-resonance Stage 1 campaign output, unchanged"
git push -q -u origin upload/az-token-resonance-stage1
echo "UPLOADED: upload/az-token-resonance-stage1 at $(git rev-parse --short HEAD)"
AZ_STAGE1
bash ~/az_tokres_stage1.sh
```
If the run is interrupted: `AZ_RESUME=1 bash ~/az_tokres_stage1.sh` (same `JOBS`). If the driver ends with `CAMPAIGN FAILED`, nothing is uploaded and `~/az_tokres_stage1/CAMPAIGN_FAILED.txt` names the step. The mechanics of this block (clean-tree stop, package-hash stop, completion, hand-over commit, refusal of a second run into the same directory) were tested in a throwaway clone with the test plan and without the push; the registered plan was not run.

*Alternative venue, not planned: Windows, PowerShell.*
```powershell
$ErrorActionPreference = "Stop"
python -I evidence\az\scripts\az_tokres_campaign.py --plan stage1 --jobs 4 --out az_tokres_stage1 --confirmatory
if ($LASTEXITCODE -ne 0) { throw "AZ-TOKRES Stage 1 FAILED (exit code $LASTEXITCODE): nothing to report; see az_tokres_stage1\CAMPAIGN_FAILED.txt" }
if (-not (Test-Path az_tokres_stage1\CAMPAIGN_COMPLETE.json)) { throw "AZ-TOKRES Stage 1: no completion marker" }
Get-Content az_tokres_stage1\CAMPAIGN_COMPLETE.json
```
On `--resume` workers refuse any record file of another identity or of other shard arguments. A directory without `CAMPAIGN_COMPLETE.json` is not a campaign result and is not reported as one. The directory arrives unchanged under `upload/az-token-resonance-stage1/` on the branch of that name and is hash-checked against its `HASHES.txt` before it is placed under `evidence/az/token_resonance/stage1/` by a follow-up commit (CONVENTIONS §6). The registered analysis is then rerun from the placed files — which repeats every integrity check and both gates — by the co-owner and, independently, by the reviewer:
```bash
D=evidence/az/token_resonance/stage1    # the placed directory
python3 -I $S/az_tokres_analyse.py --registered S1-C1 --engine $E --orient $O --runner $S/az_tokres_run.py --fixtures-log $D/fixtures_output.txt $D/S1-C1_*.jsonl --sensitivity $D/S1-C3_*.jsonl
python3 -I $S/az_tokres_analyse.py --registered S1-C2 --engine $E --orient $O --runner $S/az_tokres_run.py --fixtures-log $D/fixtures_output.txt $D/S1-C2_*.jsonl
```

## 9. Evidence manifest

`evidence/az/token_resonance/SHA256SUMS` lists every file of the package (scripts by relative path). Key hashes at this draft:

| File | Path | SHA-256 |
|---|---|---|
| runner | `evidence/az/scripts/az_tokres_run.py` | `75c5f139a453a4b2595eba76760e34cddc32c990370259ae6e84ec5379408992` |
| analysis script | `evidence/az/scripts/az_tokres_analyse.py` | `490b3d4f06ef52d6d39b217d0821bd8361d0a8ed37941f32f9c154113c91dc80` |
| fixtures script | `evidence/az/scripts/az_tokres_fixtures.py` | `da9256dc01d786355e2fc28938647b1b800d54b1425e2e927af1febff2f9cb86` |
| negative controls | `evidence/az/scripts/az_tokres_negcontrols.py` | `ba572a7a82c7eb05fd630cd5e93147eaaaaa07ba382fe06d86985bceb7747eae` |
| campaign driver | `evidence/az/scripts/az_tokres_campaign.py` | `792c9563960161686bdec10b613f68182dab65e25563dd266c7763eb275306f8` |
| golden file | `evidence/az/token_resonance/fixtures/golden.json` | `40eba43073fba138130244f75cc0790ef20bffcbeda7599ff4e372b95427c134` |
| fixtures output (with T11, N=6) | `evidence/az/token_resonance/fixtures/fixtures_output.txt` | `4e71fb233988a7a7fc2e3899f104aa7d2207ed0906267d35741ae8052aea5365` |
| fixtures output (with T11b, N=8) | `evidence/az/token_resonance/fixtures/fixtures_output_exhaustive_N8k1.txt` | `03d9dab0f37421a3c81be6a1f268c49f8e094da3e1d756306a0f4964fd9929d0` |
| negative-control output | `evidence/az/token_resonance/fixtures/negcontrols_output.txt` | `6c51f14271722769d1920026910db6c8a0b586b7ace6ab81ad31f868df44fd7c` |
| test campaign: completion marker | `evidence/az/token_resonance/fixtures/test_campaign/CAMPAIGN_COMPLETE.json` | `3e0c681da43594d1cc5bfb5e717fa1574d680ad18774f7b4dc415c4a359ec7d3` |
| test campaign: file hashes | `evidence/az/token_resonance/fixtures/test_campaign/HASHES.txt` | `b8fe5c3cca32f6238e7faa2006cea4e5e11927f64e8d47fa39dd518409262d57` |
| test campaign: analysis at C1 settings | `evidence/az/token_resonance/fixtures/test_campaign/analysis_TEST-C1.txt` | `8eeea1d0c632b03ce62340db856e5bc4e6af8d66d59224fbe10eb7da6665f044` |
| pilot data, 252 runs | `evidence/az/token_resonance/pilot/pilot_time.jsonl` | `8b11130b321ce021110beadfd9ce15cbfd1430ce440ab6af4ce1c3afab36d043` |
| pilot data, 2,123 runs | `evidence/az/token_resonance/pilot/pilot_N120.jsonl` | `d2bba5abb07988dfc2ee72107bf99f22a8e2b64a65cff7c477862a04dc2c5dda` |
| pilot script | `evidence/az/token_resonance/pilot/pilot.py` | `c7e317584723e6841c0aeb83870bd5f86607a8126a3531d2db27c664f5708d77` |
| pilot test script | `evidence/az/token_resonance/pilot/analyse3.py` | `54302092f3d7802a585c700d919e3def5ed60139338f9ac6e7b8edb2eec93701` |
| pilot provenance | `evidence/az/token_resonance/pilot/PROVENANCE.md` | `c0cc703fe739e21a279e59b6f5782b922e38fcc616bed594c34fe19dc428e2d6` |

`SHA256SUMS` covers 50 files: the five scripts, 27 fixture files (golden file, fixture and negative-control outputs, the test campaign) and the frozen pilot (18 files, unchanged since draft r1). The analysis script pins the runner, the fixtures script and the golden file (`RUNNER_SHA256`, `FIXTURES_SHA256`, `GOLDEN_SHA256`) besides the engine and the orientation reference. Check: `cd evidence/az/token_resonance && sha256sum -c SHA256SUMS`.

Fields of a run record (schema `az_tokres_run_v2`). Identity: `schema`, `tag`, `cell`, `N`, `k`, `T`, `cap`, `profile`, `policy`, `confirmatory`, `engine_sha256`, `orient_sha256`, `runner_sha256`. State: `base`, `arm`, `seed`, `slot`, `choices`, `th0`, `d0` (state actually run), `d0_base` (native tokens), `alphabet_class`, `slot_class`. Outcome: `M`, `births`, `steps`, `hit_cap`, `fb`, `fe`, `t100`, `M_at`, `census`, `top_class`, `top_share`, `law_viol`, `swaps`, `paths`, `path_ties`, `ms_seen`, `ms_bound`, `ambiguous`, `tdr26`. Machine-dependent: `secs`. A manifest line (schema `az_tokres_manifest_v2`): `identity`, `shard` (`start`, `stop`, `n_perm`, `arms`, `tdr26`), `rows_total`, `file_sha256`, `runs_written`, `runs_present_before`, `seconds`, `python`, `platform`, `finished_utc`.

## 10. Proposed campaign and run counts

| Stage | Content | Runs | Cost | State |
|---|---|---|---|---|
| 1 | C1, C2, C3 as registered in §5 | 19,900 | test-campaign timing here: 0.38 s (C1), 0.20 s (C2), 0.29 s (C3) per run, two workers on a two-core container: about 1.7 core-hours, i.e. roughly half an hour with four workers; to be confirmed on the PI's machine | registered; accepted for submission to the PI by the readback `5857601141`; waits for the PI's authorisation; venue: the PI's Ubuntu server |
| 2 | `N ∈ {240, 242, 480}` at `k/N ≈ 1/15` (`k = 16, 16, 32`), same arms, 1,000 base draws per cell | 6,000 / 5,000 / 6,000, plus calibration | unknown; a timing probe of 20 base draws per cell comes first | **proposal only.** `T` and the threshold of `Y` are not known for these cells and are not frozen. Proposed: `T = 800`; threshold `⌈2.5 × median M⌉` of 500 native runs with a separate tag (exposure-blind; at `N = 120` this gives 103 against the registered 100). To be fixed by an amendment after Stage 1 is reviewed. |
| 3 | TDR-26 in its own scope: `N = 720`, `k = 48` and `N = 722`, `k = 48`, `T = 5000`, arms O1R, O1D (and O2R, O2D at 720), birth-anchored rule as the endpoint, 200 base draws per cell | 800 + 400 | unknown, large; timing probe first | **proposal only; needs the TDR-G owner** (engine profile, node cap, rule thresholds, relation to TDR-G's own campaign specification of batch ≥ 500) |
| — | r43 (`N = 720`) and r31 (`N = 722`): do their initial tokens contain a `4x ≡ 0` value? | 0 new runs | negligible | **not executable now.** The v17 `N = 720/722` files are held outside the repository and their command line and master seed are not recorded in TDR-G §8. If the PI supplies the exact command (engine, `--seed`, grid arguments, batch), the run seeds follow from the engine's `monte_carlo` and the initial tokens from `init_universe`, without running the dynamics. Under independence the chance that both runs contain such a token is about `0.022 × 0.011 ≈ 2.4·10⁻⁴`. |

## 11. Dependencies, firewalls, and a proposed pipe item (not filed)

- **TDR-G** owns the rules, the OPENs and the engine. Needed from TDR-G before any use beyond AZ's own diagnostic: its verdict on Propositions 1–3 and on (E); whether `P1` is its profile for new campaigns; Stage 3. This note does not ask TDR-G to change anything.
- **OFN**: no decision needed. The design uses the residual `2c ≡ 0` case of `RTG-OFN-ALG-STAR-TOKEN-SHIFT` as TDR-G imports it.
- **PI**: authorisation of Stage 1; the v17 command line for r43/r31 (not needed for Stage 1); whether the item below is filed. The reviewer recommends filing it, as a `[SESSION]` proposal independent of the campaign decision (review `5855522171`, relayed 11 Nov); that recommendation is not an authorisation, and the item is not filed.
- **Dyadic, DZT, Genesis, NUMGEN, LIT**: none.
- Methodology: AZ v0.7 declares v1.2; this note uses the v1.4 evidence keys of CONVENTIONS §5 for its own files. It is not a DSN edition.

Proposed text for `pipes/TDRG/` — **not filed in this PR**:
> `from: AZ · to: TDRG · kind: offer · object: TDRG-OPEN-SPECCONS-STAR; TDRG-ALG-LEM-SPECCONS (n-node conjecture); TDRG-OPEN-LOCKING-FAIL · tags: [tdrg-v2.12.14, az-v0.7]`
> AZ offers, as a `[SESSION]` proposal, a signed-token-alphabet law and class-count update under the §6.3 event inventory, with a birth-injection corollary and the birth-free `n`-node corollary (`records/az/AZ_TOKEN_RESONANCE_PREREGISTRATION.md` §2; fixtures `evidence/az/token_resonance/fixtures/`). It does not close the OPEN. AZ has registered a campaign on the placed engine with `TDRG-DEF-ORIENT` that reports the TDR-26 birth-anchored rule as a separate output. Needed from TDR-G: a verdict on the statement and on the completeness of the event inventory; nothing blocks.

## 12. Review record and amendment log

**Draft r1** (`b4106b9`): independent review by the second co-owner (ChatGPT), GitHub review `5855522171`, 11 Nov 2026 — *corrections required before Stage 1*: R1 analysis not fail-closed (blocking), R2 PowerShell block without exit-code enforcement (blocking), R3 statistical and interpretive precision, R4 theorem/fixture scope (non-blocking). The review inspected the stored outputs and did not rerun the fixtures.

**Draft r2 — amendments, all made before any confirmatory data exist** (no run with tag `AZ-TOKRES-S1` has been made):

| # | Review point | Change |
|---|---|---|
| A1 | R1 | The analysis is fail-closed (§6.5): registered parameters are constants of the script; identity, custody, independently re-derived initial states, record consistency and completeness are checked before anything is estimated; any failure exits with code 2 and prints neither estimate nor reading. The `--partial` mode is removed; unvalidated input can only be analysed in an exploratory mode that prints no reading. |
| A2 | R1 | Gates G1 (fixtures log of the campaign machine) and G2 (law counter) stop the analysis with exit code 3. G3–G5 are qualifiers attached to every reading. |
| A3 | R1 | Runner: every record carries the full identity (tag, cell parameters, profile, policy, confirmatory flag, three SHA-256 pins); every invocation appends a manifest line with identity, shard arguments, record count and file SHA-256; `--resume` refuses a file of another identity or other shard arguments; `--confirmatory` is refused with a non-registered tag. Record schema v2. |
| A4 | R1 | Negative controls: `az_tokres_negcontrols.py`, 51 cases (§7). |
| A5 | R2 | Campaign driver `az_tokres_campaign.py`: fixtures, workers and analyses are run with their exit codes checked, shard record counts and manifests verified, completion marker written only on full success. The PowerShell block is reduced to that one command with `$LASTEXITCODE` and marker checks (§8). |
| A6 | R3 | G4 and G5 use a declared neutrality margin `δ_neutral = 0.025` with the readings equivalent / different / inconclusive; "the interval contains zero" is no longer a criterion. Their comparison sets were also corrected: r1 compared the detuned arm with `BASE` on all base draws, which is not neutral by construction (the native slot token is resonant in about 3 % of the draws); r2 restricts G4 and G5 to base draws with a non-resonant native slot token. PC4 has the same three-way reading against `±δ*`. |
| A7 | R3 | Families delimited: family 1 = {PC1, PC2} is the only confirmatory family (Holm); family 2 = {PC3, PC4} is a separate supportive replication (Bonferroni within it); no joint claim (§6.1, §6.2). |
| A8 | R3 | Interpretation restricted to the total causal effect of the token replacement at the given engine, profile, cell, horizon and threshold; the first-contact mechanism is stated as OPEN; S10 and S8 are labelled descriptive, not mediation (§0, §2, §4, §6.6). |
| A9 | R4 | The law check is now exact per tick (census increment `+1` at `−x` for every newborn, centre witness), with negative controls T5b–T5d; the exhaustive fixtures were rerun with it. Corollary 1.1 states the several-births-in-one-tick form with the newborn–newborn pairs. §2 names what the machine checks cover. |
| A10 | — | The r1 smoke files are replaced by the driver's test campaign (same tag, same seeds; the C1 records are identical in every dynamical field). |

Unchanged from r1: hypotheses H1–H3, the endpoint, the arms and their randomisation, the seed derivation and the registered tag, cells and sample sizes, `δ* = 0.05`, the McNemar test and the Agresti–Min interval of PC1–PC4, the pilot and its provenance.

**Readback of draft r2** (`f7fdfac`): GitHub review `5857601141`, 11 Nov 2026 — *accepted (scoped); no remaining Stage-1-blocking finding; PI authorisation still required*. R1–R4 closed. The reviewer recomputed 11 SHA-256 values and compared the 156 test records at C1 settings with the r1 smoke records (19 dynamical fields, all equal); the negative controls, fixtures and test campaign were read from the stored outputs, not rerun by the reviewer. Two non-blocking notes, with their disposition:

| Note | Disposition |
|---|---|
| N1. `superiority()` words its reading "Holm p < 0.05" also when it is called for PC3, whose adjusted `p` is the Bonferroni one printed on the line above. The number and the decision are right; the word is wrong. | **Erratum, declared before data:** in the output of cell C2 the PC3 reading "SUPPORTED (Holm p < 0.05 …)" is to be read "SUPPORTED (Bonferroni-adjusted p < 0.05 …)". The Stage 1 report will carry this erratum next to the verbatim output. The analysis script is **not** changed before Stage 1, so that the bytes the reviewer accepted (`az_tokres_analyse.py`, §9) are the bytes that run and that are named in every stored output. |
| N2. Keep `--jobs` constant on `--resume`. | Stated in §8; the server block fixes `JOBS=4`. |

**After r2, documentation only (no script, fixture, golden or pilot byte changed; `SHA256SUMS` unchanged):** this readback record; the venue of Stage 1 moved from the PI's Windows machine to the PI's Ubuntu server on the PI's instruction of 11 Nov 2026, 14:02 +03:00, with the bash block of §8.

Decision points: PI decision on Stage 1 (the reviews do not authorise it) → run on the server → upload branch → hash check and placement → registered analysis rerun by both co-owners. No merge, tag or adoption is implied by the PR.
