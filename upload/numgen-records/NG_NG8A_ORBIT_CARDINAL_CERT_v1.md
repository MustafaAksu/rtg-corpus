# NG-8A Certificate — Ordinal-to-Cardinal Orbit-State Compatibility

**Certificate ID:** `NG_NG8A_ORBIT_CARDINAL_CERT_v1`  
**Parent RID:** `NUMGEN-OPEN-TWO-FIVES`  
**Sub-RID:** `NUMGEN-OPEN-TWO-FIVES-ORBIT-CARDINAL`  
**Target document:** `RTG_NUMBER_GENESIS_DSN_v1.3`  
**Date:** 2026-08-27  
**Status:** `[ALG]` certificate candidate for NG-8A closure  
**Scope:** sufficiently small forward-invariant primitive-dyad tube `U_T` on which N-1 is already certified  
**Ownership:** Number Genesis

---

## 1. Certified inputs

The N-1 primitive-dyad realization supplies the following already-certified facts on `U_T`:

1. **Primitive counting token.** For each `x in U_T`, one occurrence of the scoped counting type is the directed transition `e_x : x -> T(x)`.
2. **Forward invariance.** `T(U_T) subset U_T`.
3. **Primitive-orbit non-collision.** For every `x in U_T` and all distinct `r,s in N_0`,
   `T^r x != T^s x`.
4. **Free-monogenic history algebra.** `M_T={id,T,T^2,...}` has no relation between distinct finite powers.

No cardinality statement is used as a physical premise in these inputs.

---

## 2. Physical finite-event history

Fix `x in U_T` and a finite history of `m >= 0` primitive `T`-events.

For `m >= 1`, the event-token history is

`e_x, e_Tx, e_T^2x, ..., e_T^(m-1)x`

with successive post-event states

`Tx, T^2x, ..., T^m x`.

Define the **post-event visited-state collection**

`S_m^+(x) := {T^k x : 1 <= k <= m}`,

and `S_0^+(x) := emptyset`.

This convention aligns one physical event occurrence with one newly visited post-event state.

If the initial state is included as a trajectory position, then an `m`-event trajectory has `m+1` positions; that is a different counting convention and is not used for the theorem below.

---

## 3. Physical evaluation map

For `m >= 1`, define

`Phi_(x,m) : {1,...,m} -> S_m^+(x)`

by

`Phi_(x,m)(k) = T^k x`.

The map is physically implemented by the orbit itself. The finite index set is used only in the mathematical metalanguage to state the certificate; it is not the physical cause of distinctness.

---

## 4. Injectivity

If `Phi_(x,m)(r)=Phi_(x,m)(s)`, then `T^r x=T^s x`. By certified N-1 primitive-orbit non-collision, `r=s`.

Hence `Phi_(x,m)` is injective, and the `m` post-event states are pairwise physically distinguishable by the present reduced relational state itself.

---

## 5. Surjectivity

By definition, every element of `S_m^+(x)` equals `T^k x` for some `1 <= k <= m`.

Hence `Phi_(x,m)` is surjective.

---

## 6. Theorem — physical equinumerosity

Therefore

`Phi_(x,m) : {1,...,m} -> S_m^+(x)`

is a bijection.

In the ordinary mathematical representation,

`|S_m^+(x)| = m`.

The RTG-native content is stronger than a bare set-theoretic isomorphism: the comparison map is the realized primitive orbit itself, and its injectivity is forced by the already-certified physical non-collision theorem.

For `m=0`, `S_0^+(x)=emptyset`, so `|S_0^+(x)|=0`.

---

## 7. Equivalent orbit-position formulation

If instead one counts the first `m` **orbit positions**, including the initial state, define

`S_m^pos(x) = {x,Tx,...,T^(m-1)x}`.

The same non-collision proof gives `|S_m^pos(x)|=m`.

But the semantics differ:

- `m` orbit positions contain only `m-1` transitions between them;
- `m` primitive event occurrences produce `m` post-event states, or `m+1` trajectory positions if the initial state is included.

The DSN should keep these conventions explicit.

---

## 8. Interpretation

`[RESULT][from: ALG]` **Ordinal-to-cardinal seed compatibility.**

Within the scoped local primitive-dyad realization, a finite Track-A history of `m` primitive events produces `m` pairwise distinguishable post-event relational states.

Thus the same numeral that represents the finite repetition history also represents the multiplicity of its physically realized post-event state collection, and the correspondence is implemented by the orbit map rather than assumed through an abstract cardinal identification.

This supplies the first certified Track-A -> finite-state Track-B compatibility arrow for the NG-8 “two fives” programme.

---

## 9. Scope guards

1. **Local-tube scope.** Holds only on `U_T`, where primitive non-collision is certified.
2. **Generator-selection ceiling.** Inherits OPEN-P0 / SG-PROG-2 because the result is conditional on the selected continuous generator `T`.
3. **No network-cardinality claim.** Does not identify this multiplicity with TDR-G node count, graph-component count, birth count, or any other cross-branch cardinal object.
4. **No Track-C identification.** Does not identify event count with eta-winding, harmonic exponent, character label, or cyclic residue class.
5. **No bare-isomorphism closure.** Physical content is the orbit-implemented evaluation map plus N-1 non-collision.
6. **No completed-infinity claim.** Each theorem instance is finite; successor extensibility gives potential indefinite extension only.

---

## 10. Closure verdict

**NG-8A CLOSED**

Recommended DSN status:

`[RESULT][from: ALG] [scope: local primitive-dyad tube U_T]`

Closed statement:

For every admissible `x in U_T` and every finite `m in N_0`, the `m`-event primitive history has a post-event visited-state collection

`S_m^+(x)={Tx,...,T^m x}`

physically equinumerous with its `m` event occurrences via the orbit-evaluation map `k -> T^k x`.

Full Track-B/network cardinal compatibility, Track-C compatibility, and a universal counting object remain OPEN.

---

## 11. DSN insertion text

> **NG-8A — Ordinal-to-cardinal orbit-state compatibility**  
> **Sub-RID:** `NUMGEN-OPEN-TWO-FIVES-ORBIT-CARDINAL`  
> **Status:** CLOSED `[RESULT][from: ALG]` `[scope: local primitive-dyad tube U_T]`
>
> For every admissible initial state `x in U_T` and every finite `m >= 0`, let
> `S_m^+(x)={T^k x : 1 <= k <= m}`, with `S_0^+(x)=emptyset`.
> N-1 primitive-orbit non-collision implies that the orbit-evaluation map
> `Phi_(x,m)(k)=T^k x`
> is injective on the `m` physical event occurrences, while surjectivity holds by construction. Hence the orbit itself implements a bijection between the finite Track-A event history and the collection of its post-event relational states. In the mathematical representation, `|S_m^+(x)|=m`.
>
> This is **physical equinumerosity**, not a bare abstract set isomorphism: the comparison map is the realized `T`-orbit and its injectivity is supplied by the certified N-1 non-collision theorem.
>
> `[GUARD]` If one instead counts orbit positions including the initial state, `{x,Tx,...,T^(m-1)x}` contains `m` positions but represents only `m-1` transitions between them. Event-count and state-position conventions must not be mixed.
>
> `[GUARD]` NG-8A closes only the local Track-A -> finite-state multiplicity seed. It does not identify this count with TDR-G/network cardinality or Track-C winding/harmonic labels and inherits OPEN-P0.

**Certificate:** `NG_NG8A_ORBIT_CARDINAL_CERT_v1.md`
