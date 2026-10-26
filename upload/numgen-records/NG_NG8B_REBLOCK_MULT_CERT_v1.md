# NG-8B Certificate — Multiplication by Physical Re-blocking

**Certificate ID:** `NG_NG8B_REBLOCK_MULT_CERT_v1`  
**Parent RID:** `NUMGEN-OPEN-TWO-FIVES`  
**Sub-RID:** `NUMGEN-OPEN-TWO-FIVES-REBLOCK`  
**Target document:** `RTG_NUMBER_GENESIS_DSN_v1.3`  
**Date:** 2026-08-27  
**Status:** `[ALG]` certificate candidate for NG-8B closure  
**Scope:** sufficiently small forward-invariant primitive-dyad tube \(\mathcal U_T\) on which N-1 is certified  
**Ownership:** Number Genesis

---

## 1. Certified inputs

The N-1 primitive-dyad realization supplies:

1. **Primitive generator and counting token.**  
   One primitive event is one application of
   \[
   T:\mathcal U_T\to\mathcal U_T.
   \]

2. **Forward invariance.**
   \[
   T(\mathcal U_T)\subseteq \mathcal U_T.
   \]
   Hence, for every \(m\in\mathbb N_{>0}\),
   \[
   T^m(\mathcal U_T)\subseteq\mathcal U_T.
   \]

3. **Primitive-orbit non-collision.**  
   For every \(x\in\mathcal U_T\) and distinct \(r,s\in\mathbb N_0\),
   \[
   T^r x\neq T^s x.
   \]

4. **Free-monogenic history algebra.**
   \[
   \mathsf M_T=\{\mathrm{id},T,T^2,\ldots\}
   \]
   is free on the distinguished generator \(T\).

The theorem below introduces no new primitive event type. A block is a derived grouping of already-certified primitive \(T\)-events.

---

## 2. Derived block transformation

Fix a positive block size
\[
m\in\mathbb N_{>0}.
\]

Define the derived block transformation
\[
\boxed{
B_m:=T^m.
}
\]

One occurrence of \(B_m\) means the ordered composition of exactly \(m\) consecutive primitive \(T\)-events.

Define the block submonoid
\[
\boxed{
\mathsf M_{B_m}
=
\langle B_m\rangle
=
\{\mathrm{id},B_m,B_m^2,\ldots\}
=
\{\mathrm{id},T^m,T^{2m},\ldots\}.
}
\]

Because \(\mathcal U_T\) is forward invariant under \(T\), every block iterate remains in \(\mathcal U_T\).

---

## 3. Inherited freeness of the block submonoid

Let \(r,s\in\mathbb N_0\) and suppose
\[
B_m^r x=B_m^s x
\]
for some \(x\in\mathcal U_T\).

Since \(B_m=T^m\),
\[
T^{mr}x=T^{ms}x.
\]

N-1 primitive-orbit non-collision implies
\[
mr=ms.
\]

Since \(m>0\),
\[
r=s.
\]

Therefore distinct powers of \(B_m\) never collide on \(\mathcal U_T\), and
\[
\boxed{
\mathsf M_{B_m}\ \text{is free monogenic on }B_m=T^m.
}
\]

This is inherited freeness, not a new independent counting generator.

---

## 4. Re-blocking identity

For every \(k\in\mathbb N_0\),
\[
B_m^k
=
(T^m)^k.
\]

Expanding the composition gives
\[
(T^m)^k
=
\underbrace{T^m\circ T^m\circ\cdots\circ T^m}_{k\ \text{blocks}}
=
T^{\underbrace{m+\cdots+m}_{k\ \text{summands}}}.
\]

In the ordinary mathematical representation of repeated addition,
\[
\underbrace{m+\cdots+m}_{k\ \text{summands}}=mk.
\]

Hence
\[
\boxed{
(T^m)^k=T^{mk}.
}
\]

For \(k=0\),
\[
(T^m)^0=\mathrm{id}=T^0,
\]
so the zero-block case is included.

---

## 5. Physical content of the identity

The equality
\[
(T^m)^k=T^{mk}
\]
is stronger than equality of final states.

Both sides denote the **same ordered primitive history**:

- left description: \(k\) consecutive blocks, each containing \(m\) primitive \(T\)-events;
- right description: one unblocked history containing \(mk\) primitive \(T\)-events.

Re-blocking changes only the partition/parenthesization of the already-realized primitive event word. It does not change:

- the primitive event tokens;
- their order;
- the intermediate states;
- the final state.

Thus the physical operation is **repeated concatenation of a finite primitive-event block**. Multiplication appears only after representing the repeated-addition count in the mathematical metalanguage.

---

## 6. Theorem — multiplication compatibility by re-blocking

For every admissible \(x\in\mathcal U_T\), every positive block size \(m\in\mathbb N_{>0}\), and every block count \(k\in\mathbb N_0\),

\[
\boxed{
B_m^k x=T^{mk}x.
}
\]

The submonoid \(\langle T^m\rangle\) is free monogenic, and the inclusion
\[
\langle T^m\rangle\hookrightarrow\mathsf M_T
\]
implements the map
\[
k\longmapsto mk
\]
in the standard \(\mathbb N\)-representation.

Equivalently, counting \(k\) physically realized blocks of \(m\) primitive events is compatible with counting the underlying \(mk\) primitive events.

This is the Track-A **multiplication-by-re-blocking compatibility theorem**.

---

## 7. Relation to the existing \(F=T^6\) construction

The already-certified six-step block
\[
F=T^6
\]
is the realization-specific example \(m=6\).

NG-8B does not use the L1 contraction theorem to prove the general algebraic re-blocking identity. L1 was needed upstream to certify primitive-orbit non-collision and the N-1 tube. Once N-1 is closed, inherited freeness proves the statement for every positive block size \(m\).

---

## 8. Epistemic interpretation

`[RESULT][from: ALG]` **Multiplication compatibility, not multiplication ex nihilo.**

The theorem does **not** claim that RTG has reconstructed the standard mathematical definition of multiplication without mathematical metalanguage.

The RTG-native physical operation is:

\[
\text{repeat a block of }m\text{ primitive events }k\text{ times}.
\]

The representation theorem identifies the total primitive-event count with repeated addition,
\[
m+\cdots+m,
\]
and therefore with the standard product \(mk\).

So the certified claim is:

\[
\boxed{
\text{physical block repetition}
\longleftrightarrow
\text{multiplicative compatibility in the }\mathbb N\text{ representation}.
}
\]

---

## 9. Scope guards

1. **Local-tube scope.**  
   The theorem is scoped to the N-1 tube \(\mathcal U_T\) and the selected continuous generator \(T\).

2. **OPEN-P0 ceiling.**  
   The result inherits SG-PROG-2 / OPEN-P0. It does not establish universal physical primitiveness of this arithmetic realization.

3. **Derived block ≠ independent event type.**  
   \(B_m=T^m\) is a coarse-graining/re-blocking of the same primitive Track-A stream. It is **not** a second independently certified event type and cannot discharge N-5A or SG-NG-20.

4. **No use as a fake rational generator.**  
   Ratios of \(T^m\) and \(T^n\) remain single-generator constructions. NG-8B does not provide the independent co-realized recurrence streams required for N-5.

5. **No full Track-B multiplication theorem.**  
   NG-8B concerns multiplication compatibility of history repetition. It does not yet prove that cardinal collections, network multiplicities, winding classes, or harmonic labels implement the same multiplication law.

6. **Positive block-size guard.**  
   \(m=0\) is excluded as a block generator: \(T^0=\mathrm{id}\) contains no primitive event and \(\langle\mathrm{id}\rangle\) is not a free monogenic event stream. The zero **block-count** case \(k=0\) is valid.

7. **No commutativity claim from grouping alone.**  
   The theorem certifies repeated block concatenation and its standard product representation. Any claim that a physical binary multiplication operation is independently commutative across distinct counting realizations belongs to later NG-8 compatibility work.

---

## 10. Closure verdict

\[
\boxed{
\text{NG-8B CLOSED}
}
\]

**Recommended DSN status:**

`[RESULT][from: ALG] [scope: local primitive-dyad tube \(\mathcal U_T\)]`

**Closed statement:**  
For every \(m\ge1\) and \(k\ge0\), the derived block submonoid \(\langle T^m\rangle\) is free, and \(k\) repetitions of an \(m\)-primitive-event block are exactly the same primitive history as \(mk\) applications of \(T\):
\[
(T^m)^k=T^{mk}.
\]
The physical operation is re-blocked concatenation; multiplication is the mathematical representation of repeated addition.

**Remaining NG-8 scope:**  
Cross-track multiplication compatibility, network/cardinal multiplication, Track-C multiplication, and a universal counting object remain OPEN.

---

## 11. DSN insertion text

> **NG-8B — Multiplication by physical re-blocking**  
> **Sub-RID:** `NUMGEN-OPEN-TWO-FIVES-REBLOCK`  
> **Status:** CLOSED `[RESULT][from: ALG]` `[scope: local primitive-dyad tube \(\mathcal U_T\)]`
>
> Fix \(m\ge1\) and define the derived block transformation \(B_m:=T^m\). Since the N-1 tube is forward invariant, \(B_m\) acts on the same tube. N-1 non-collision implies that if
> \[
> B_m^r x=B_m^s x,
> \]
> then \(T^{mr}x=T^{ms}x\), hence \(r=s\). Therefore \(\langle T^m\rangle\) is free monogenic.
>
> For every \(k\ge0\),
> \[
> (T^m)^k
> =
> T^{m+\cdots+m}
> =
> T^{mk}.
> \]
> Thus \(k\) repetitions of a block containing \(m\) primitive \(T\)-events are physically the same ordered primitive history as \(mk\) consecutive primitive events. Re-blocking changes only the grouping of the event word; it changes neither the event tokens nor their order or intermediate states.
>
> `[RESULT][from: ALG]` This realizes **multiplication compatibility by physical re-blocking**: the RTG-native operation is repeated concatenation of an \(m\)-event block, while \(mk\) is the standard mathematical representation of the resulting repeated-addition count.
>
> `[GUARD]` \(T^m\) is a derived block/coarse-graining of the same Track-A stream, not an independently certified second event type; NG-8B therefore does not discharge N-5A/SG-NG-20 and cannot be used to manufacture physical rational ratios from one generator.
>
> `[GUARD]` NG-8B closes only the Track-A multiplication seed. Full Track-B/network and Track-C multiplication compatibility remains OPEN.

**Certificate:** `NG_NG8B_REBLOCK_MULT_CERT_v1.md`
