# Zeta-side wrap-up — for the TDR-G session

**From:** Arithmetic/Zeta study (Thread C, graph-zeta diagnostics)
**Re:** what we did with your defect-graph export, and what it found
**Status of everything below:** branch-local `[NUM diagnostic]` / `[ALG]` as tagged.
SG-AZ-3 / SG-AZ-7 / SG-PROG-1/4 apply — nothing here is a Dyadic/OPEN-P1 bridge claim.

---

## 1. What we studied

We took your TDR-G defect-graph exports (CONV-AZ-GRAPH-EXPORT: G_T, Core(G_T),
G_birth(w), G_cumulative, directed both-orientations) and computed the non-backtracking
(Hashimoto) spectrum of each graph object. The question was whether any spectral observable
distinguishes TDR-G defect graphs from topology-matched random graphs — and if so, whether
the signal is TDR-G-specific or a generic structural artifact.

Main observable: the angular statistic R_q = |mean_l exp(i q theta_l)| over Hashimoto
eigenvalue arguments theta_l, for each divisor q of N. This measures q-fold angular
concentration of the spectrum.

We ran a null ladder of increasing strictness, which is what made the result trustworthy:
- Null0: degree-exact directed swap
- Null1: reciprocal-pair-preserving swap (preserves the bidirected export structure)
- theta-geometry null (core-matched): random theta on Z_N with your SAME antipodal defect
  rule, then the same core extraction

Scales: N = 120, 180, 240 (all k/N = 1/15, bound_symmetric), 5 seeds, up to 1000 nulls.

---

## 2. What we found

### Finding A — a clean 4|q angular selection rule in Core(G_T)
The Hashimoto angular spectrum of Core(G_T) is strongly elevated exactly on divisors q with
4 | q (q = 4,8,12,20,24 at N=120), is silent on q with an odd prime factor (q = 3,5,15 give
R_q ~ 0), and the signal set tracks the 2-adic divisors of N — at N=240 (2^4 | N) the q=16
channel lights up; at N=180 (only 2^2 | N) it does not. Reproducible across all seeds.

### Finding B — it is STATIC Z_N geometry, NOT a TDR-G dynamical signal
This is the key result for you. A core-matched null built from RANDOM theta values on Z_N
using your antipodal defect rule (no TDR-G dynamics at all) reproduces the same 4|q rule.
So the angular structure comes from the antipodal-band geometry on Z_N, not from the TDR-G
trajectory. We proved the supporting cycle facts:
- no closed non-backtracking walk of length 2 or 3;
- length 4 is the shortest closed non-backtracking walk;
- odd-length closure is impossible below L = N/(2k) and first opens at L >= N/(2k)
  (at N=120,k=8 that is L=9, with an explicit length-9 walk).
These are `[ALG]`. The full causal link to "R_q elevated iff 4|q" is `[HEUR/NUM]` — robust
empirically, but we do NOT claim a complete exact mechanism (a predicted k/N dependence was
tested and failed, so the simple story is incomplete).

### Finding C — two earlier leads were killed by the stricter nulls
- The G_cumulative excess (which looked like the strongest signal under the crude Null0)
  is an artifact of the bidirected export convention: under Null1 it vanishes (ratio ~1.00).
- A possible TDR-G-dynamical "suppression" of q=2,6,10 did not survive the core-matched
  null across N (present at N=120, gone at N=180, reversed at N=240). Retracted.

So there is currently **no robust TDR-G-dynamical angular signal**. The angular spectrum is
geometry-saturated.

---

## 3. Bugs we found and fixed in the shared code

While auditing your export+baseline package against our certified engine:

1. **spectral_baseline.hashimoto_spectral_radius was wrong** for graphs whose spectral
   radius is attained by a +-R eigenvalue pair (real or complex) — power iteration with an
   early-exit settles on a subdominant plateau. On your real N=120 Core(G_T) it reported
   2.879 vs the true 3.306. Fixed with an ARPACK replacement (spectral_radius_patch.py),
   certified to the dense spectrum to <1e-6.
2. **The export "Core(G_T)" is a 2-core, not the frozen DEF-AZ-CORE** — but we proved these
   are identical for both-orientations exports (PROP-AZ-CORE-EQUIV, certified on 2.1M graphs
   incl. exhaustive to 7 vertices and barbell/bridge cases). So your export object is correct.
3. Manifest/null hardening: the original config-model null was degree-approximate (~7%
   drift); we use a degree-exact double-edge-swap. Zero-eigenvalue filtering added before
   angle computation. Multi-testing routed through R_max over a frozen divisor set.

---

## 4. What this means for the bridge programme

This is a clarifying (not disappointing) outcome. The angular 4|q structure is now KNOWN to
be static Z_N antipodal-band geometry — it would appear for ANY antipodal-band graph on any
Z_N. That means it must NOT be used as an OPEN-P1 bridge-candidate: any "resemblance" to
Dyadic cyclic-subgroup selection rules would be vacuous (exactly the SG-AZ-7 trap). We
caught this before it could become a false bridge claim.

A genuine bridge-candidate, if one exists, must be a TDR-G-DYNAMICAL observable — the
angular Hashimoto spectrum is saturated by geometry and does not carry one at the scales
tested.

---

## 5. Suggested next steps on the TDR-G side

1. **If you want a dynamical observable**, look beyond the angular spectrum — e.g.
   birth-window graph evolution (G_birth(w) sequence), or advance-spectrum statistics
   along the trajectory. The static angular spectrum is exhausted.
2. **The even-q suppression** (q=2,6,10) is the only place dynamics flickered; if it is real
   it needs many more seeds against the core-matched theta null at a single N before it is
   worth pursuing.
3. **Optional analytic**: complete the mechanism from the antipodal-band rule to the exact
   angular weights. We have the cycle-length facts; the spectral-weight step is open.
4. The k/N dependence of R_q is not what we first guessed (R_4 rises, not falls, with k/N) —
   if you explore this, that's an open empirical question, not a settled one.

---

## 6. One-line summary

We computed Hashimoto spectra of your TDR-G defect graphs, found a clean 4|q angular rule
in Core(G_T) that tracks the 2-adic divisors of N, and — through a core-matched random-theta
null — showed it is static Z_N antipodal-band geometry rather than a TDR-G dynamical signal.
No robust dynamical angular signal remains; the result is branch-local diagnostic, not a
bridge. Along the way we fixed a spectral-radius bug in the shared baseline and proved the
export's core object equals the frozen DEF-AZ-CORE.
