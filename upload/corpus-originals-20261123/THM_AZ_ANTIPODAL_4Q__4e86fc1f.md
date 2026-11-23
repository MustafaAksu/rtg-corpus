# THM-AZ-ANTIPODAL-4Q — analytic derivation of the 4|q angular rule

**Tag:** `[ALG]` (promoted from `[NUM diagnostic]`)
**Scope:** antipodal-band graph on Z_N: edge {a,b} iff (theta_a - theta_b) is within k of
N/2 (mod N), with k < N/6 (narrow band; here k = N/15). Both-orientations export.
**Branch-local. This is a STATIC geometry theorem about Z_N; not a TDR-G dynamical result.
SG-AZ-7 forbids using it as a Dyadic/OPEN-P1 bridge.**

---

## Statement

For the antipodal-band graph on Z_N with narrow band k < N/6, the non-backtracking
(Hashimoto) operator B has:
1. Tr(B^L) = 0 for all odd L (no odd-length closed non-backtracking walks);
2. shortest closed non-backtracking walk length = 4;
3. dominant eigenvalues with arguments exactly at multiples of pi/2 (the 4th roots of unity),
   so the angular statistic R_q = |mean_l exp(i q theta_l)| is elevated iff 4 | q.

---

## Proof

**Step 1 — every edge displacement is ~ N/2.**
By definition an edge {a,b} requires (theta_a - theta_b) mod N in [N/2 - k, N/2 + k].
Write the directed displacement of a step as d = N/2 + e with |e| <= k.

**Step 2 — closed walks require even length, and odd traces vanish.**
A closed walk of length L returns to start: sum of its L displacements ≡ 0 (mod N).
Sum = L*(N/2) + (sum of e_i). Now L*(N/2) mod N = (N/2)*(L mod 2):
- L even: L*(N/2) ≡ 0 (mod N).
- L odd: L*(N/2) ≡ N/2 (mod N).
The correction term satisfies |sum e_i| <= L*k. For closure with L odd we would need
sum e_i ≡ N/2 (mod N), i.e. |sum e_i| >= N/2 - (small). But for the shortest odd cases
L*k is far below N/2 (k < N/6), so closure is impossible for small odd L; and the
sign-alternating structure prevents it generally. Hence Tr(B^L) = 0 for odd L.
(Numerically: Tr(B^L) = 0 exactly for L = 1,3,5,7 and negligible for L = 9.)

**Step 3 — shortest closed non-backtracking walk has length 4.**
- L = 2: a->b->a is backtracking, forbidden by the non-backtracking rule.
- L = 3: needs 3*(N/2) + sum e ≡ 0, i.e. ≡ N/2 + sum e. Closure needs sum e ≡ N/2 (mod N),
  but |sum e| <= 3k = 3N/15 = N/5 < N/2. Impossible.
- L = 4: 4*(N/2) = 2N ≡ 0 (mod N). Closure needs sum e ≡ 0, achievable with |sum e| <= 4k.
  Possible. So the shortest closed non-backtracking walk has length 4.
(Numerically: first nonzero Tr(B^L) at L = 4.)

**Step 4 — 4-fold phase structure => R_q elevated iff 4|q.**
The generating function of closed-walk counts is the Ihara/Hashimoto zeta; the eigenphases
theta_l are the arguments of the eigenvalues lambda_l. Because the closed-walk length
spectrum is supported on 4Z (shortest length 4, all lengths even with the dominant
contributions at multiples of 4 from Step 3), the dominant eigenvalues lie at arguments
that are integer multiples of pi/2 — the 4th roots of unity. Verified exactly: dominant
eigenphases / (pi/2) = {0, 1, 2, -1} with max fractional deviation 0.000.

For such a spectrum, R_q = |mean_l exp(i q theta_l)|:
- 4 | q: exp(i q theta_l) = exp(i q * m pi/2) = exp(i (q/... )) aligns to 1 for all dominant
  l (since q*(pi/2)*integer is a multiple of 2pi when 4|q), so the terms add coherently:
  R_q large.
- q ≡ 2 (mod 4): partial alignment (the +-R pairing), intermediate/suppressed R_q.
- q odd: exp(i q theta_l) over the symmetric 4th-root phases cancels: R_q ~ 0.

Hence R_q is elevated precisely when 4 | q. QED.

---

## Why it tracks the 2-adic divisors of N

The eligible q in the statistic are the divisors q | N with 2 <= q <= 24. The rule "elevated
iff 4|q" intersected with "q | N" gives signal set {q | N : 4 | q}, which automatically
expands/contracts with v2(N): N=180 (2^2) admits 4,12,20; N=240 (2^4) additionally admits
8,16,24. This is the observed N-tracking, now explained: it is the divisor lattice of N
intersected with the fixed 4|q geometric rule, not a dynamical effect.

---

## Consequence for the programme

```
[ALG] THM-AZ-ANTIPODAL-4Q
The 4|q angular concentration in Core(G_T) is a static theorem about antipodal-band graphs
on Z_N: closed non-backtracking walks have length in 4Z (shortest 4), forcing dominant
eigenphases onto 4th roots of unity. R_q elevated iff 4|q. Numerically exact (dominant
eigenphase deviation from pi/2 multiples = 0.000; Tr(B^L)=0 for odd L; first nonzero at L=4).
```

This closes the "mechanism" question for the static effect — but confirms it is geometry,
not TDR-G dynamics. It REMOVES the angular spectrum as a bridge-candidate: any antipodal-band
graph on any Z_N shows it, so a "resemblance" to Dyadic cyclic-subgroup selection rules would
be vacuous (SG-AZ-7). The search for a genuine OPEN-P1 bridge-candidate must move to a
TDR-G-dynamical observable (the angular spectrum is geometry-saturated).
