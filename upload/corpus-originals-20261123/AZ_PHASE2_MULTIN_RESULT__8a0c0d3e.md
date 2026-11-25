# Phase 2 multi-N result — the 4|q angular rule is STATIC antipodal-Z_N geometry

**RID:** TDRG-AZ-PHASE2-MULTIN-NULL1
**Tag:** `[NUM diagnostic]`
**Scope:** N in {120,180,240}, k/N=1/15, bound_symmetric, Core(G_T), Null1 + theta-geometry null.
**Branch-local. SG-AZ-3 / SG-AZ-7 / SG-PROG-1/4 forbid any Dyadic/OPEN-P1 use.**

## IMPORTANT CORRECTION (this supersedes the first draft of this file)

The first draft tagged the 4|q rule `[NUM diagnostic strong]` and called it an
arithmetic selection rule that "tracks N." A further null — the theta-geometry null
(random theta on Z_N, SAME antipodal defect rule) — shows the 4|q ENHANCEMENT is a
STATIC property of the antipodal defect geometry on Z_N, NOT a TDR-G dynamical effect.
The corrected, honest finding is below.

---

## What is real, and what it is

**Finding 1 — the 4|q enhancement is static antipodal-Z_N geometry (NOT TDR-G dynamics).**
A theta-geometry null — random distinct theta values on Z_N with the identical antipodal
defect rule |theta_a - theta_b - N/2| <= k, no TDR-G dynamics at all — ALREADY reproduces
the 4|q rule almost exactly:

| q | real TDR-G core (seed2) | theta-geometry null | 4\|q |
|---|---|---|---|
| 4 | 0.950 | 0.924 | * |
| 8 | 0.923 | 0.863 | * |
| 12 | 0.941 | 0.821 | * |
| 20 | 0.972 | 0.807 | * |
| 24 | 0.955 | 0.813 | * |
| 3,5,15 | ~0 | ~0 | |

For 4|q the real core and the pure-geometry null agree within ~0.03-0.16, with the null if
anything slightly LOWER. So "R_q elevated iff 4|q" is explained entirely by the antipodal
defect rule on Z_N; TDR-G dynamics are not needed to produce it. The fact that the signal
set tracks the 2-adic divisors of N (q=16 only at N=240, etc.) is consistent with this:
it is a fact about which roots of unity the antipode-N/2 band rule admits, i.e. about Z_N
arithmetic, not about the trajectory.

**Finding 2 — TDR-G dynamics leave a weaker, less certain signature in the SUPPRESSION.**
For even-non-4|q values (q in {2,6,10}), the real TDR-G core sits BELOW the theta-geometry
null (real suppresses these components). But this holds in only 4/5 seeds (seed 4 reverses),
so it is suggestive, not clean. This is the only place TDR-G dynamics appear to add anything
beyond the static geometry, and it is not yet a robust effect.

---

## Honest status

```
[NUM diagnostic] [scope: N in {120,180,240}, bound_symmetric, Core(G_T)]
The Core(G_T) non-backtracking angular spectrum concentrates at q-th roots of unity iff
4 | q. This rule is a STATIC property of the antipodal defect rule on Z_N (reproduced by a
random-theta geometry null with no TDR-G dynamics) and tracks the 2-adic divisor structure
of N. It is NOT a TDR-G dynamical signature.

[NUM weak/unstable] A complementary suppression of even-non-4|q angular components (q in
{2,6,10}) appears in the real TDR-G core relative to the theta-geometry null in 4/5 seeds.
This is the only candidate TDR-G-dynamical angular effect and is not yet robust.
```

## What the null ladder established (in order of strength)

- **Null0 (degree-only):** R_max excess — but inflated by the bidirected export symmetry. [superseded]
- **Null1 (reciprocal-pair):** 4|q signal survives, even-q artifact removed. Looked like a
  TDR-G arithmetic rule. [refined by theta null]
- **Theta-geometry null (Z_N antipodal rule, random theta):** 4|q rule REPRODUCED with no
  dynamics. => the rule is static Z_N geometry, not TDR-G. [decisive]

The theta null is the one that mattered: it is the control Null1 was missing, because Null1
preserves the bidirected pairing but not the Z_N antipodal-band geometry, whereas the
theta null isolates exactly the geometry.

## Consequences

- The earlier G_cumulative lead is RETRACTED (no signal under Null1).
- The 4|q "arithmetic selection rule" is REAL but is a geometric fact about the antipodal
  defect rule on Z_N, not a dynamical TDR-G phenomenon. It is still a legitimate
  branch-local diagnostic — and arguably a cleaner one, because it is now mechanistically
  understood (see below) rather than mysterious.
- For OPEN-P1 / bridge purposes this is actually clarifying: any future bridge-candidate
  must be sought in a TDR-G-DYNAMICAL observable (e.g. the weak even-q suppression, or a
  non-angular statistic), because the angular 4|q structure is explained by Z_N geometry
  alone and would be present in ANY antipodal-band graph on Z_N. SG-AZ-7 still forbids
  Dyadic comparison regardless.

## Mechanism (now largely understood, branch-local)

The antipodal defect rule links theta_a, theta_b when theta_a - theta_b is within k of N/2.
On Z_N the edge "displacements" cluster around N/2. The non-backtracking cycle lengths and
hence the eigenphase concentration are governed by how N/2-centered displacements compose
mod N, which is controlled by the 2-adic structure of N (N/2 is the order-2 element). This
is why 4|q (the 2-adic divisors) is selected and odd-factor q is silent. A full derivation
is a clean branch-local [ALG] target and would close the "mechanism" question for the
static effect — but it would also confirm the effect is geometric, not dynamical.

## Next native steps (revised priorities)

1. **Derive the static 4|q rule analytically** from the antipodal-band rule on Z_N (clean
   [ALG] target; would convert Finding 1 from [NUM] to [ALG] and explain the 2-adic selection).
2. **Test the even-q suppression (Finding 2) properly**: more seeds, against the theta-geometry
   null specifically, to see if it is a real TDR-G-dynamical effect or seed noise. This is now
   the only candidate dynamical angular signal.
3. **If a dynamical signal is wanted**, look beyond the angular spectrum — the static geometry
   dominates it. Candidates: birth-window graph evolution, advance-spectrum statistics.
4. Dyadic/OPEN-P1 comparison remains forbidden (SG-AZ-7); doubly so now, since the angular
   structure is Z_N-geometric and would trivially "resemble" any cyclic-group selection rule.

---
---

## CORE-MATCHED UPDATE (per audit): conclusion confirmed, dynamical residue dissolves

The audit required the theta null be core-matched: compare Core(G_T) against
Core(random-theta antipodal graph), not against the raw theta graph. Done. Two results:

**(a) The 4|q enhancement is confirmed static geometry.** Core-matched, the theta null
reproduces the 4|q elevation at all three N (diffs for 4|q small, mostly positive:
+0.01 to +0.11). The qualitative rule survives the matched comparison. Static-Z_N-geometry
classification stands.

**(b) The "weak dynamical residue" (even-non-4|q suppression) DISSOLVES under core-matching.**
The q in {2,6,10} suppression flagged as a possible TDR-G-dynamical effect is N-dependent
once the null is core-matched:
- N=120: suppression present (diffs -0.17, -0.18, -0.24)
- N=180: gone (diffs ~0)
- N=240: slightly reversed (diffs +0.01 to +0.07)

It does not survive as a consistent effect across N. The [NUM weak/unstable] dynamical
residue is RETRACTED: it was an artifact of the unmatched (raw-theta) comparison at N=120.
There is currently NO robust TDR-G-dynamical angular signal.

## Naming correction (per audit)

The decisive control is NOT "Null3" (reserved for a TDR-G trajectory-preserving / phase-
shuffled dynamical null). The control used here is:
- `[NULL-GEO-RAW]` random-theta antipodal-band null (raw)
- `[NULL-GEO-CORE]` core-matched random-theta antipodal-band null (the DSN-clean one)

## Final corrected status

```
[NUM diagnostic] [RID: TDRG-AZ-STATIC-ZN-4Q]
[scope: N in {120,180,240}, k/N=1/15, bound_symmetric, Core(G_T), core-matched theta null]
The Core(G_T) Hashimoto angular spectrum shows elevated R_q precisely on divisors q with
4|q. A CORE-MATCHED random-theta antipodal-band null reproduces this, so the 4|q rule is
static Z_N antipodal-band geometry, not TDR-G dynamics. Tracks the 2-adic divisors of N
(q=16 only at N=240). Per-q tables: AZ_THETA_CORE_MATCHED.json.

[RETRACTED] "[NUM weak/unstable] even-non-4|q suppression as dynamical residue."
Reason: under the core-matched theta null the q in {2,6,10} suppression is N-dependent
(present at N=120, gone at N=180, reversed at N=240) — not a consistent dynamical effect.

[OPEN] analytic derivation of the 4|q rule from the antipodal-band rule on Z_N ([ALG] target);
a genuine TDR-G-dynamical observable (the angular spectrum is geometry-saturated, so look
elsewhere: birth-window evolution, advance-spectrum statistics).
```

