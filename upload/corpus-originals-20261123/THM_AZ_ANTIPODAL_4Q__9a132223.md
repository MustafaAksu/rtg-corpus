# Antipodal-band low-order cycle structure — CORRECTED (v2)

**Tag:** `[ALG]` for the low-order claims (1-3 below); `[HEUR/NUM strong]` for the
angular-concentration consequence. The earlier exact spectral theorem is RETRACTED.
**Scope:** antipodal-band graph on Z_N, edge iff displacement within k of N/2 (mod N),
narrow band k < N/6. Both-orientations export. Branch-local; SG-AZ-7 forbids bridge use.

---

## RETRACTION of the v1 claim

v1 (THM-AZ-ANTIPODAL-4Q) claimed:
- "Tr(B^L) = 0 for all odd L" — **FALSE**, and
- "dominant eigenvalues with arguments EXACTLY at multiples of pi/2" — **overclaimed**.

Refuted by an explicit odd closed non-backtracking walk at N=120, k=8, length 9:
`0->68->16->84->32->99->46->113->60->0`, every step in the antipodal band [52,68],
non-backtracking, closed. Independently verified. This matches the v1 numerics, where
Tr(B^9) = 4212 (nonzero) was wrongly dismissed as "negligible." The auditor is correct.

The error: I generalized a SMALL-L exclusion to ALL odd L. The exclusion has a threshold.

---

## CORRECTED statement (the part that is actually true)

Let displacements be d = N/2 + e with |e| <= k. A closed walk of length L needs
sum of displacements ≡ 0 (mod N): L*(N/2) + sum(e_i) ≡ 0, with |sum e_i| <= L*k.

**Claim 1 [ALG]. No closed non-backtracking walk of length 2 or 3.**
- L=2: a->b->a is backtracking, forbidden.
- L=3: L*(N/2) = 3N/2 ≡ N/2 (mod N); closure needs sum e ≡ N/2, but |sum e| <= 3k < N/2
  whenever k < N/6. So impossible. (Verified by search at N=120,k=8: none found.)

**Claim 2 [ALG]. Length 4 is the shortest closed non-backtracking walk.**
4*(N/2) = 2N ≡ 0 (mod N); closure achievable with |sum e| <= 4k. (Verified: first nonzero
Tr(B^L) at L=4.)

**Claim 3 [ALG]. Odd-length closure has an exact threshold L >= N/(2k).**
For odd L, L*(N/2) ≡ N/2 (mod N), so closure needs sum e ≡ N/2 (mod N), i.e.
|sum e| >= N/2 - (correction). Since |sum e| <= L*k, odd closure is IMPOSSIBLE for
L*k < N/2, i.e. L < N/(2k), and first becomes possible at L >= N/(2k).
At N=120, k=8: N/(2k) = 7.5, so the smallest odd closed walk is L=9 — exactly the
counterexample. (Verified: Tr(B^L)=0 for odd L=1,3,5,7; Tr(B^9)=4212 != 0.)

**Claim 4 [HEUR/NUM strong]. Length-2/3 exclusion + length-4 shortest cycle co-occur with
4|q angular enhancement (finite-N), mechanism incompletely understood.**
For k/N = 1/15 the leading short cycles are length-4-dominated (L=2,3 excluded; first odd
closure at L=9). Empirically the dominant eigenphases concentrate near 4th roots of unity
and R_q is elevated for 4|q. The L=2,3 exclusion and L=4 shortest-cycle facts are [ALG];
the full causal link to "R_q elevated iff 4|q" is [HEUR/NUM] and INCOMPLETE — a tested
prediction that the rule should weaken with larger k/N was FALSIFIED (see below), showing
the low-order-domination story does not fully capture the k-dependence. What is solid: the
4|q enhancement is empirically robust and is reproduced by the core-matched random-theta
null, so it is static Z_N antipodal geometry, not TDR-G dynamics.

---

## Note on the odd-cycle perturbation

The odd cycles enter only at order L >= N/(2k) (here L=9), with small amplitude
(Tr(B^9)=4212 vs Tr(B^8)~1.17e6, ~0.4%). So they are a small perturbation to the even,
4-led low-order structure. This is why R_q remains strongly concentrated at 4|q despite
odd cycles existing. It does NOT, however, imply the k-dependence runs as first guessed
(see falsified prediction below).

---

## Corrected DSN status

```
[ALG] Antipodal-band low-order cycle structure on Z_N (k<N/6):
  - no closed NB walk of length 2 or 3;
  - length 4 is the shortest closed NB walk;
  - odd closure impossible for L < N/(2k); first odd closure at L >= N/(2k).
  Verified: N=120,k=8 -> first odd closure L=9 (explicit walk + Tr(B^9)!=0).

[HEUR/NUM strong] [RID: TDRG-AZ-STATIC-ZN-4Q]
[scope: N in {120,180,240}, k/N=1/15, bound_symmetric, Core(G_T), core-matched theta null]
  The 4|q angular enhancement follows from low-order 4-domination of the closed-walk
  spectrum. It is a finite-regime dominant-moment effect, not an exact spectral theorem.
  A core-matched random-theta antipodal null reproduces it => static Z_N geometry, not
  TDR-G dynamics.

[RETRACTED] v1 "[ALG] THM-AZ-ANTIPODAL-4Q" with "Tr(B^L)=0 all odd L" and "exact 4th-root
  eigenphases." Refuted by explicit N=120,k=8 length-9 odd closed NB walk.
```

## Tested prediction — FALSIFIED, recorded honestly

I predicted the 4|q rule should WEAKEN as k/N rises (odd threshold N/(2k) drops). Tested at
N=120, k in {4,8,12,16,19}: R_4 does NOT decline — it slightly rises (0.75 -> 0.97), and
R_2, R_6 rise too. So the prediction is FALSE. The odd-closure threshold correctly explains
why SMALL odd L are excluded, but it does NOT govern the k-dependence of the angular
concentration. That k-dependence runs the other way (denser bands -> all R_q rise, sharper
peaks). The "4|q weakens with k/N" mechanism is therefore RETRACTED as well.

Honest residual: Claims 1-3 (no L=2,3 closure; shortest L=4; odd threshold L>=N/(2k)) are
verified [ALG] facts. The CONNECTION from those to "R_q elevated iff 4|q" is [HEUR/NUM] only
and is NOT fully explained — the low-order-domination story is incomplete, since increasing
k (more odd cycles, lower threshold) does not weaken the rule. The 4|q angular concentration
is empirically robust and reproduced by the core-matched theta null (so: static Z_N
geometry), but its exact mechanism beyond the L=2,3 exclusion + L=4 shortest-cycle facts
remains OPEN.
