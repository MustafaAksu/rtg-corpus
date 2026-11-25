# N5-C6 Canonical-Pair Falsifier Certificate v1

**Certificate ID:** `NG_N5C6_CANONICAL_PAIR_FALSIFIER_v1`  
**RID:** `NUMGEN-OPEN-N5-COMM-BD / N5-C6`  
**Base:** `RTG_NUMBER_GENESIS_DSN_v1.14`  
**Date:** 2026-08-28  
**Artifact:** `ng_n5c6_canonical_pair_falsifier_v1.py` / `.log`  
**Verdict:** **N5-C6 CLOSED `[RESULT][from: ALG]` conditional on the adopted N-5-COMM-BD bounded-defect candidate definition. N-5 remains OPEN.**

## 1. Certified inputs

On the sufficiently small certified primitive-dyad tube, let `A` be the primitive `T` event stream and `B` the canonical positive phase-coincidence stream. For the common-order prefix `H_M` containing the first `6M` primitive A-events, the closed N-5A/GAP-LOCK package gives

\[
N_A(H_M)=6M,
\]
\[
N_B(H_M)
=
M-\frac{\tau}{2\pi}\log M+O(1),
\qquad
\tau=\frac{2\sqrt3}{3}>0.
\]

Equivalently, the physical seven-gap count satisfies

\[
s(M)=\frac{3\tau}{\pi}\log M+O(1),
\qquad
E_B(M)=s(M)+O(1).
\]

The prefixes `H_M` are admissible common-order prefixes: their order is inherited from the already-certified N-2-ORD reachability relation. No external time or real-valued frequency is introduced.

## 2. Candidate bounded synchronization defect

For fixed positive integers `p,q`, v1.14 defines

\[
\Delta_{p:q}(H)
=
qN_A(H)-pN_B(H).
\]

Substituting the certified canonical-prefix counts gives

\[
\boxed{
\Delta_{p:q}(H_M)
=
(6q-p)M
+
\frac{p\tau}{2\pi}\log M
+
O(1).
}
\]

For each fixed `(p,q)` the `O(1)` term remains bounded.

## 3. Dichotomy

### Case I — `p != 6q`

Because `6q-p` is a nonzero integer,

\[
\frac{\Delta_{p:q}(H_M)}{M}
=
(6q-p)
+
\frac{p\tau}{2\pi}\frac{\log M}{M}
+
O(M^{-1})
\longrightarrow
6q-p\neq0.
\]

Therefore

\[
\boxed{
|\Delta_{p:q}(H_M)|\to\infty
}
\]

linearly.

### Case II — `p = 6q`

The linear term cancels. Since `p,q>0` and `tau>0`,

\[
\Delta_{6q:q}(H_M)
=
\frac{6q\tau}{2\pi}\log M+O(1)
=
\frac{3q\tau}{\pi}\log M+O(1)
\longrightarrow+\infty.
\]

Equivalently, using the physical GAP-LOCK count law,

\[
\Delta_{6:1}(H_M)
=
N_A(H_M)-6N_B(H_M)
=
E_B(M)
=
s(M)+O(1)
\to+\infty.
\]

Thus the unique positive rational slope compatible with the limiting density also fails the bounded-defect criterion.

## 4. Falsifier theorem

For every fixed pair of positive integers `(p,q)`,

\[
\boxed{
\sup_M |\Delta_{p:q}(H_M)|=\infty.
}
\]

Bounded synchronization commensurability requires one uniform finite bound over **all** sufficiently long admissible common-order prefixes. An unbounded admissible prefix subsequence is therefore sufficient to falsify the class. Consequently:

\[
\boxed{
\forall p,q\in\mathbb N_{>0},
\qquad
A\not\sim_{\rm comm}^{p:q}B
}
\]

under the N-5-COMM-BD candidate definition.

**Important routing point:** this negative theorem does **not** require N5-C2 prefix-origin invariance. C2 is needed to make a positive bounded class presentation-independent. For a falsifier, one admissible prefix family with unbounded defect already defeats the universal boundedness requirement. Finite endpoint/tie-convention changes can only alter the displayed defect by `O(1)` and cannot remove either the linear or logarithmic divergence.

## 5. Density-resonance separation

Nevertheless,

\[
\frac{N_A(H_M)}{N_B(H_M)}
=
\frac{6M}{M-\frac{\tau}{2\pi}\log M+O(1)}
\longrightarrow6.
\]

Hence the canonical pair certifies the strict separation

\[
\boxed{
\text{rational limiting density }6
\quad\not\Rightarrow\quad
\text{bounded physical commensurability }6:1.
}
\]

This is the theorem-level canonical witness motivating SG-NG-24.

A useful terminology split is therefore:

- **density-resonant at 6**: `N_A/N_B -> 6`;
- **boundedly commensurate at 6:1**: `N_A-6N_B=O(1)`.

The canonical pair has the first property and fails the second.

## 6. Scope and guards

1. `[RESULT][from: ALG]` is local to the sufficiently small selected continuous primitive-dyad tube and inherits OPEN-P0.
2. The theorem is conditional on using the v1.14 **bounded-defect candidate definition** as the N-5 commensurability criterion; it does not yet prove that this definition is the unique or final RTG notion of commensurability.
3. N5-C1–C5 and N5-C7 remain OPEN. In particular, no positive Q-like physical class has yet been realized.
4. The result does not promote the chart-derived constant `tau`, the logarithmic coefficient, or the limiting density to a genesis-grade number object (SG-NG-19/23/24).
5. GAP-LOCK Lemma 3 is irrelevant to the falsifier: the theorem needs only the closed physical count law `s(M)=(3tau/pi)log M+O(1)`, not convergence of consecutive physical slip ratios.

## 7. Verdict

\[
\boxed{\text{N5-C6 CLOSED}}
\]

and the canonical A/B pair is:

\[
\boxed{
\text{rational-density resonant at }6
\quad\text{but not boundedly commensurate at any positive rational }p:q.
}
\]

**N-5 remains OPEN.** The next proof work should test the candidate definition itself (C1–C5) and seek a positive RTG realization before C7 can supply a Q-like representation.
