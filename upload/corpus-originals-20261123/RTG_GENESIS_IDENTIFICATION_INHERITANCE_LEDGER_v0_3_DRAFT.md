# RTG Genesis Identification & Inheritance Ledger v0.3 — DRAFT

**Date:** 28 September 2026  
**Status:** WORKING DRAFT — noncanonical; no owner adoption; no Genesis RID regraded or replaced.  
**Study:** GUP-08 / GUP-09 — physical birth residual + identification/inheritance contract.  
**Current scope:** continuous \(\Phi_{2\to3}\) branch plus a separately typed TDR-G clean-star comparison branch. v0.3 makes the contract schema arity-neutral, integrates the eleven-field receiving-side source audit, completes the no-splitting/no-merging and whole-contract-equivalence guards, and records the literal TDR-G clean-star as a \(4\to5\) event rather than a discrete \(2\to3\) analogue.  
**Owner baseline:** `RTG_GENESIS_GEOMETRY_DSN_v2.8.4` (retained owner baseline, under the frozen noncanonical Genesis correction ledger).  

## 0. Source discipline

This draft uses the following sources as distinct authorities:

- `RTG_GENESIS_GEOMETRY_DSN_v2.8.4` — historical owner formulation of \(\Phi_{2\to3}\).
- `GENESIS_CORRECTION_LEDGER_v0_1_FROZEN.md` — frozen noncanonical correction record; not owner adoption.
- `RTG_DYADIC_OSCILLATOR_DSN_v6.4.10` — raw / odd-projected / polynomial-conjugacy object separation.
- `RTG_TRIADIC_BIRTH_LIFT_DSN_v1.5` — diagnostic birth-angle / \(J_Q\) route record.
- `RTG_PRIMORDIAL_RELATIONAL_REPRESENTATION_WRAPUP_v0.3` — noncanonical representation/identity framework and proposed inheritance-ledger fields.
- `BIRTH_CONTRACT_REVIEW.md` — receiving-side source audit and review; noncanonical, no owner adoption.
- `contract_field_audit.json` — machine-readable eleven-field source-status audit used in §11.
- `TDRG_CLEAN_STAR_SOURCE_CONTRACT.md` — source-level extraction of the literal TDR-G clean-star event; comparison branch only.

Tags used here:
- `[SOURCE]` — directly reported by an inspected owner/source.
- `[ALG]` — direct mathematical deduction from explicitly stated definitions.
- `[AUDIT]` — source-comparison finding.
- `[HEUR]` — proposed research convention.
- `[OPEN]` — missing physical/model selection or missing bridge.

No `[THM]` or owner-level `[RESULT]` is created by this draft.

---

# 1. Arity-neutral birth/event contract

The common schema must not force every event into \(2\to3\) notation. Use

\[
\mathfrak B
=
\bigl(
\mathcal S_{\rm pre},
\mathcal D_{\rm event},
\mathcal I_{\rm roles},
\mathcal K_{\rm role},
\mathcal R_{\rm res},
\Phi,
\mathcal S_{\rm post}^{\rm adm},
\mathcal C_{\rm post},
\mathcal G_{\rm pre},
\mathcal G_{\rm post},
\mathcal A_{\rm attach},
\Pi_{\rm ret},
T_{\rm pre},T_{\rm post},
\mathcal O,
\mathcal Q_{\rm phys}
\bigr).
\]

Here:

- \(\mathcal D_{\rm event}\) is the event/admissibility domain, including timing/detection convention;
- \(\mathcal R_{\rm res}\) is the residual/projection operation when the model has one; for a model such as the literal TDR-G star event it may be **not applicable**, not a missing continuous parameter;
- \(\Phi\) is the event map;
- \(\Pi_{\rm ret}\) is the explicitly declared retained-parent readout/component of the post-state;
- \(T_{\rm pre},T_{\rm post}\) are the pre/post evolution maps or flows together with their time convention;
- \(\mathcal O\) is the declared observable/trace family used for comparisons;
- \(\mathcal Q_{\rm phys}\) is the declared physical/gauge quotient on which recoverability or no-erasure is tested.

This replaces the unexplained final \(\mathcal L\) slot in v0.2.

The identification slot is

\[
\mathcal I_{\rm roles}
=
\bigl(
\mathcal P,\sim_I,
\mathcal T_{\rm transport},
\mathcal L_{\rm continuation},
\mathcal A_{\rm lineage}
\bigr),
\]

where \(\mathcal P\) is the set of pole/endpoint occurrences and \(\sim_I\) is occurrence identity. Equal labels, equal numerical values, common ancestry and physical identity are not interchangeable.

The role-carrier slot is

\[
\mathcal K_{\rm role}
=
\bigl(
V_{\rm role},
B_{\rm role},
\jmath_{\rm role},
{\rm provenance}
\bigr),
\]

where \(V_{\rm role}\) is the carrier, \(B_{\rm role}\) its declared bilinear/Gram form when one is used, and \(\jmath_{\rm role}\) its embedding into any common post-event carrier. Provenance is one of **SUPPLIED / INHERITED / EVENT-GENERATED / OPEN**. Using the parent \(B\) on a new role is therefore a modelling choice unless its inheritance is established.

The post-state is initially an **admissible set**

\[
\mathcal S_{\rm post}^{\rm adm}
=
\{x:\mathcal C_{\rm post}(x)=0,\ldots\},
\]

not assumed to be a regular manifold at the event.

For the continuous branch, specialize \(\Phi=\Phi_{2\to3}\). For the literal TDR-G clean-star comparator, \(\Phi=\Phi_\star\) is a marked \(4\to5\) local event.

---
# 2. Historical Genesis reference contract — source extraction

## 2.1 Pre-event state

`[SOURCE]` Genesis §6.3 evaluates the event at a fracture state

\[
s_*\in\mathbb R^2,
\qquad
Q_s=s_*^\top B s_*,
\qquad
B=
\begin{pmatrix}
1&-\tfrac12\\
-\tfrac12&1
\end{pmatrix}.
\]

`[OPEN]` The inspected \(\Phi_{2\to3}\) block names the fracture state but does not, by itself, provide a complete standalone event-admissibility predicate \(\mathcal D_{\rm event}\).

## 2.2 Historical residual declaration

`[SOURCE]` Genesis v2.8.4 writes

\[
E_*=F_6(s_*)-s_*,
\]

and gives the cubic pieces

\[
E_{\parallel,*}=-\frac12Q_s s_*,
\qquad
E_{\perp,*}=-\tau Q_sJ_Qs_*.
\]

`[AUDIT]` Under Dyadic v6.4.10 / GCL-06, these component formulas are retained as **cubic truncations** shared by the raw, odd-projected and NF residual objects. The displayed \(O(|s_*|^5)\) remainder is not valid for the named raw residual because the raw return contains a nonzero quartic term.

## 2.3 Leading child family

`[SOURCE]` Genesis gives the one-dimensional transverse family

\[
c_0
=
\kappa Q_sJ_Qs_*+O(|s_*|^5),
\qquad
Q_c
=
\kappa^2Q_s^3+O(Q_s^4).
\]

`[AUDIT]` These remainder orders are **owner-source wording, not yet contract-invariant facts**. They hold if the residual-to-child functional removes the quartic raw contribution (as in an odd/NF-type fifth-order remainder) or otherwise annihilates it. If a quartic term reaches \(c_0\), the generic orders weaken to

\[
c_0=\kappa Q_sJ_Qs_*+O(|s_*|^4),
\]

\[
\frac{W(c_0)}{W(s_*)}
=i\kappa Q_s+O(Q_s^{3/2}),
\]

\[
\arg\frac{W(c_0)}{W(s_*)}
=
-\frac{\pi}{2}+O(Q_s^{1/2})
\quad(\kappa<0),
\]

and

\[
Q_c=\kappa^2Q_s^3+O(Q_s^{7/2}).
\]

Which order applies is controlled by the still-OPEN full residual-to-\(c_0\) functional.

Reference policies:

\[
\kappa_{\rm shear}=-\frac{2\sqrt3}{3},
\qquad
\kappa_{\rm recoil}=-\frac12.
\]

`[ALG]` With

\[
\mu_6=-\frac12-i\frac{2\sqrt3}{3},
\]

the two reference coefficients are exactly its real and imaginary parts:

\[
\boxed{
\kappa_{\rm recoil}=\Re\mu_6,
\qquad
\kappa_{\rm shear}=\Im\mu_6.
}
\]

For the shared cubic residual decomposition

\[
E^{[3]}_*
=
E^{[3]}_{\parallel,*}
+
E^{[3]}_{\perp,*},
\]

this gives

\[
\boxed{
c_{\rm shear}^{[3]}
=
E^{[3]}_{\perp,*},
\qquad
c_{\rm recoil}^{[3]}
=
J_QE^{[3]}_{\parallel,*}.
}
\]

Thus the two historical policies can be written as **cubic-order residual functionals**:

\[
\mathcal C_{\rm shear}^{[3]}
=
P_\perp^{(s_*)},
\qquad
\mathcal C_{\rm recoil}^{[3]}
=
J_QP_\parallel^{(s_*)}.
\]

This is an algebraic identification of the documented cubic pieces, not a derivation that these projections are the complete physical birth functionals.

`[SOURCE]` Physical \(\kappa\) is not selected by the existing capacity-matching route.

## 2.4 Longitudinal branch

`[SOURCE]` Genesis leaves

\[
\lambda_\parallel
\]

OPEN: the birth map may retain, subtract or redistribute the longitudinal residual.

Therefore the full post-birth longitudinal state \(s^+\) is not fixed by the displayed leading child formula alone.

## 2.5 Identification and attachment

`[SOURCE/AUDIT]` The continuous reference construction is **not topology-free**: Triadic §6.1 names a primitive \(K_3\) target, and Genesis downstream Jacobi sections use already-labelled node/mode structure.

What is missing is the **complete event-level realization**:

- the pole-occurrence set \(\mathcal P\) and the precise event-stage identity quotient;
- whether each shared role identity is supplied, inherited or event-generated;
- the endpoint gluing / state assignment that realizes the declared \(K_3\);
- a post-event incidence representation tied to \(\Phi_{2\to3}\);
- a continuation rule for retained roles.

Accordingly, the historical branch is treated as a **node-mediated reference branch with supplied labels/partial identity**, not as evidence that the birth law itself derives persistent node identity.

## 2.6 First contract verdict

`[AUDIT]`

\[
\boxed{
\text{Genesis v2.8.4 supplies a leading birth family, but not yet a complete }\mathfrak B_{2\to3}.
}
\]

This is a source-completeness finding, not a rejection of the historical model.

---

# 3. Residual register — keep the three objects visible

## 3.1 Raw residual

\[
E_{\rm raw}(w)=F_W(w)-w.
\]

`[SOURCE]` Dyadic v6.4.10 records a nonzero quartic part \(F_4\); on the positive real ray,

\[
F_4(t)
=
-\frac{5+25i\sqrt3}{48}t^4
\ne0.
\]

**Status in this ledger:** historical Genesis reference definition.  
**Physical selection:** `[OPEN]`.

## 3.2 Odd-projected residual

\[
E_{\rm odd}(w)
=
\frac{F_W(w)-F_W(-w)}2-w.
\]

`[SOURCE]`

\[
E_{\rm odd}(w)
=
\mu|w|^2w+O(|w|^5),
\]

and

\[
E_{\rm raw}(w)-E_{\rm odd}(w)
=
F_4(w)+O(|w|^6).
\]

The \(F_4+O(|w|^6)\) statement is source-backed by the Dyadic six-step return/parity ledger; it is not inferred here from a generic near-identity map. In particular, the owner return has identity linear part, certified cubic leading defect and the stated quartic even part, so there is no unrecorded quadratic even term being silently dropped.

**Status:** mathematically defined projection/diagnostic.  
**Physical selection as Genesis birth input:** `[OPEN]`.

## 3.3 NF-native residual

Let

\[
\widehat F=h^{-1}\circ F_W\circ h.
\]

Then

\[
E_{\rm NF}(z)=\widehat F(z)-z
=
\mu|z|^2z+O(|z|^5).
\]

`[ALG]` On the domain of the conjugacy,

\[
\boxed{
E_{\rm raw}(h(z))
=
h\!\left(z+E_{\rm NF}(z)\right)-h(z).
}
\]

Thus raw and NF residuals describe the same isolated-dyad pre/post return states when **the complete map is transported**. A finite displacement does not transform exactly as a tangent vector:

\[
E_{\rm raw}(h(z))
\ne
Dh(z)E_{\rm NF}(z)
\quad\text{in general}.
\]

**Status:** chart-native residual.  
**Use as Genesis birth input without full contract transport:** `[OPEN]`.

---

# 3.4 Actual \(h_2\) test: the quartic contract split is nonzero

The generic order count can be checked in the **published Dyadic quadratic normalizer**, not only in an abstract chart. Write

\[
h(z,\bar z)
=
z+h_2(z,\bar z)+O(|z|^3),
\]

with

\[
h_2
=
-\frac{1+i\sqrt3}{12}z^2
-\frac13z\bar z
+\frac{1-i\sqrt3}{24}\bar z^2.
\]

Let the cubic child functional in the complex frame be

\[
C(z,\bar z)=i\kappa z^2\bar z
=i\kappa |z|^2z.
\]

`[ALG]` The degree-four part generated by evaluating the child functional on the transported state is

\[
[C(h)-C]_{4}
=
\kappa\left[
\left(-\frac{\sqrt3}{24}+\frac{i}{24}\right)z^4
+
\left(\frac{\sqrt3}{6}-\frac{i}{2}\right)z^3\bar z
+
\left(-\frac{\sqrt3}{12}-\frac{3i}{4}\right)z^2\bar z^2
+
\left(\frac{\sqrt3}{12}+\frac{i}{12}\right)z\bar z^3
\right],
\]

which is not identically zero.

For real-ray \(z=\bar z=t\),

\[
\boxed{
[C(h)-C]_{4}
=
\frac{\kappa(\sqrt3-9i)}8\,t^4\ne0
\qquad(\kappa\ne0,t\ne0).
}
\]

The tangent push-forward also differs. With the real-analytic derivative \(Dh\),

\[
[Dh\,C-C]_{4}\big|_{z=\bar z=t}
=
\frac{\kappa(\sqrt3-3i)}{12}\,t^4,
\]

and therefore

\[
\boxed{
[C(h)-Dh\,C]_{4}\big|_{z=\bar z=t}
=
\frac{\kappa(\sqrt3-21i)}{24}\,t^4\ne0.
}
\]

So the published normalizer confirms the generic conclusion:

\[
\boxed{
\text{the historical/raw, odd-projected and chart-transport questions are indistinguishable at cubic order but can separate at quartic order.}
}
\]

This does **not** by itself classify any two complete birth contracts as `PHYS-DISTINCT`; an admissible \(H_3\), attachment transport and declared observables are still required.


# 4. Complete-contract classification

The three residual formulas do **not** automatically define three inequivalent physical models.

| Contract candidate | Definition | Current classification |
|---|---|---|
| `B-RAW-HIST` | Historical Genesis contract retaining \(E_{\rm raw}\) as the named residual | **Reference contract, incomplete** |
| `B-ODD-PROJ` | Apply odd projection before the birth rule | **Additional operation; physical role OPEN** |
| `B-NF-TRANSPORT` | Transport the entire birth contract through valid pre/post chart maps \(H_2,H_3\) | **Potentially REP-EQUIV; same cubic child, actual \(h_2\) produces nonzero quartic transport terms; \(H_3\)/network transport missing** |
| `B-NF-HYBRID` | Insert \(E_{\rm NF}\) into the historical birth formula while leaving the other ingredients unchanged | **Same leading cubic child; potential divergence from quartic order; not justified as a coordinate change** |

The verdict vocabulary is

\[
\texttt{REP-EQUIV},
\qquad
\texttt{PHYS-DISTINCT},
\qquad
\texttt{UNDECIDED-MISSING-BRIDGE}.
\]

Guard:

\[
\boxed{
\text{failure to prove REP-EQUIV does not imply PHYS-DISTINCT}.
}
\]

`PHYS-DISTINCT` requires an actual difference in declared admissible states, observables, attachments or dynamics.

---

# 5. Whole-contract representation equivalence test

A genuine change of representation requires more than a conjugacy of the event map.

Let \(H_{\rm pre}\) and \(H_{\rm post}\) be invertible, domain-specified representation maps. At minimum require

\[
\widehat{\mathcal D}_{\rm event}
=
H_{\rm pre}^{-1}(\mathcal D_{\rm event}),
\]

\[
\boxed{
\widehat\Phi
=
H_{\rm post}^{-1}\circ
\Phi\circ
H_{\rm pre},
}
\]

and, on the corresponding evolution domains,

\[
\widehat T_{\rm pre}
=
H_{\rm pre}^{-1}T_{\rm pre}H_{\rm pre},
\qquad
\widehat T_{\rm post}
=
H_{\rm post}^{-1}T_{\rm post}H_{\rm post}.
\]

The comparison must also transport consistently:

- gauge actions and physical quotient;
- retained-parent readout \(\Pi_{\rm ret}\);
- role identity, continuation and lineage data;
- attachment/incidence structure;
- admissible post-state constraints;
- declared observables and comparison precision;
- any map/flow reblocking or time correspondence.

The isolated-dyad normalizer \(h\) can participate in an \(H_{\rm pre}\)-type description on its proved domain. It does **not** by itself provide the post-birth/network \(H_{\rm post}\).

Therefore

\[
\boxed{
B\text{-NF-TRANSPORT is currently }\texttt{UNDECIDED-MISSING-BRIDGE}.
}
\]

This is separate from dynamical reduction. Given an embedding \(\iota\), the reduction question is

\[
\boxed{
T_{\rm post}\circ\iota
=
\iota\circ T_{\rm pre}.
}
\]

Failure for one proposed \((\iota,T_{\rm pre})\) does not rule out every admissible reduction. Conversely, the differential-rank bound of §9 does not establish this intertwining identity.

---
# 6. Identification / inheritance test

Let \(\mathcal P\) be pole occurrences and let

\[
\mathcal V=\mathcal P/\!\sim_I
\]

be represented shared roles.

For every occurrence identification, record its provenance:

1. **SUPPLIED** before the event;
2. **INHERITED** from an earlier identified role;
3. **EVENT-GENERATED** by the birth rule;
4. **OPEN / unspecified**.

A continuation map on retained occurrences,

\[
\ell_t:\mathcal P_t^{\rm retained}\to\mathcal P_{t+1},
\]

must preserve identity classes:

\[
p\sim_{I_t}q
\Longrightarrow
\ell_t(p)\sim_{I_{t+1}}\ell_t(q).
\]

That implication alone permits two distinct source classes to merge. In a sector declared to have **neither splitting nor merging**, require reflection as well:

\[
\boxed{
p\sim_{I_t}q
\Longleftrightarrow
\ell_t(p)\sim_{I_{t+1}}\ell_t(q)
}
\]

on the retained domain, equivalently injectivity of the induced continuation on retained role classes.

Continuation and ancestry are distinct:

\[
\boxed{
\text{generated from }A
\ne
\text{identical to }A.
}
\]

---

# 7. Leading trial map — what it proves and what it does not

For diagnostic purposes only, take

\[
s^+=s,
\qquad
c=\kappa Q(s)J_Qs,
\]

and define

\[
\iota(s)=\bigl(s,\kappa Q(s)J_Qs\bigr).
\]

With

\[
J_Q=
\frac1{\sqrt3}
\begin{pmatrix}
1&-2\\
2&-1
\end{pmatrix},
\]

the companion checker verifies:

\[
J_Q^\top BJ_Q=B,
\qquad
s^\top BJ_Qs=0,
\]

and

\[
\operatorname{Gram}_B(s,c)
=
\begin{pmatrix}
Q&0\\
0&\kappa^2Q^3
\end{pmatrix}.
\]

Because the first output slot is \(s\),

\[
\pi_s\circ\iota=\mathrm{id},
\qquad
\operatorname{rank}D\iota=2.
\]

Hence, for this trial family,

\[
\boxed{
\text{new geometric direction}
\ne
\text{new independently supplied birth datum}.
}
\]

Interpretive nondegeneracy must be stated separately:

- \(\operatorname{rank}D\iota=2\) holds even at \(\kappa=0\), because the retained \(s\)-slot has identity derivative;
- a **nonzero new child direction** requires \(s\ne0\) and \(\kappa\ne0\);
- the ratio \(W(c)/W(s)\) requires \(s\ne0\);
- phase asymptotics require fixed nonzero \(\kappa\), sufficiently small amplitude, and a specified continuous local argument branch.

This does **not** establish the physical Genesis birth law, because \(s^+=s\), fixed \(\kappa\), exact truncation and attachment semantics were imposed only for the diagnostic.

---

# 8. W-direction and full leading child ratio

Let \(W\) be the Genesis eigenframe.

`[ALG]`

\[
\frac{W(J_Qs)}{W(s)}=i
\]

is the unit quarter-turn **direction identity**.

For the homogeneous leading child,

\[
\boxed{
\frac{W(c)}{W(s)}
=
i\kappa Q(s).
}
\]

For the full asymptotic ansatz the remainder depends on the still-OPEN residual-to-child functional.

If the child remainder begins at degree five,

\[
\frac{W(c_0)}{W(s_*)}
=
i\kappa Q_s+O(Q_s^2),
\qquad
\arg\frac{W(c_0)}{W(s_*)}
=
-\frac{\pi}{2}+O(Q_s)
\quad(\kappa<0).
\]

If a quartic residual/chart contribution reaches the child,

\[
\boxed{
\frac{W(c_0)}{W(s_*)}
=
i\kappa Q_s+O(Q_s^{3/2}),
}
\]

and only

\[
\boxed{
\arg\frac{W(c_0)}{W(s_*)}
=
-\frac{\pi}{2}+O(Q_s^{1/2})
}
\]

is justified without an additional cancellation theorem.

The child direction may be distinct while its leading value remains fully parent-determined.

---

# 9. Emergence classification — four independent axes

Do not collapse emergence into one ordered hierarchy. Record four answers:

| Axis | Question |
|---|---|
| Description | Is the post-state only another representation of the same admissible states? |
| Operational access | Which new comparisons become readable/executable? |
| Dynamics | Is post-birth evolution reducible to an admissible parent evolution? |
| Independent data | Is anything independently specifiable beyond complete parent state + declared event inputs? |

A deterministic birth family can leave its initial embedded image under \(T_{\rm post}\) without gaining independent initial information.

For smooth deterministic maps,

\[
D(T_{\rm post}^n\circ\iota)
=
DT_{\rm post}^n(\iota(s))D\iota(s),
\]

so

\[
\operatorname{rank}D(T_{\rm post}^n\circ\iota)
\le
\operatorname{rank}D\iota.
\]

This is an information-parameter bound, not a theorem of dynamical reducibility.

---

# 10. First GUP-08/09 findings

### BIRTH-AUDIT-01 `[AUDIT]`
The current owner formulation does not yet provide a complete continuous \(2\to3\) birth contract.

### BIRTH-AUDIT-02 `[ALG]`
Raw and NF residuals are related by finite map transport, not by naive tangent-vector substitution.

### BIRTH-AUDIT-03 `[AUDIT]`
Odd projection is an additional operation at fourth order relative to the raw residual; its physical Genesis role is not selected by Dyadic.

### BIRTH-AUDIT-04 `[ALG / conditional diagnostic]`
Under the leading trial family, the new \(J_Qs\) direction is not a new independently supplied birth datum.

### BIRTH-AUDIT-05 `[OPEN]`
No inspected source currently justifies privileging \(E_{\rm raw}\), \(E_{\rm odd}\), or \(E_{\rm NF}\) as the physical \(\Phi_{2\to3}\) input.

### BIRTH-AUDIT-06 `[OPEN]`
The provenance of shared-role identity and the exact attachment semantics of the continuous birth remain to be specified before node/pole persistence can be classified.

### BIRTH-AUDIT-07 `[ALG]`
The shear and recoil reference coefficients are exactly \(\Im\mu_6\) and \(\Re\mu_6\). At cubic order the shear policy selects \(E_\perp^{[3]}\), while the recoil policy applies \(J_Q\) to \(E_\parallel^{[3]}\). This partially fills the residual-to-\(c_0\) field **at cubic order only**.

### BIRTH-AUDIT-08 `[ALG]`
Using the actual published Dyadic \(h_2\), the cubic child functional is not equivariant under naive finite substitution or tangent push-forward at degree four. The first contract-sensitive terms are therefore genuinely nonzero at quartic order in the adopted chart.

### BIRTH-AUDIT-09 `[AUDIT]`
All four registered residual contracts share the same documented cubic child under the two reference policies. Leading-order birth data cannot discriminate them. A discriminating observable must be sensitive to quartic-order contract differences (relative order \(O(Q_s^{1/2})\)) or to attachment/evolution differences.

### BIRTH-AUDIT-10 `[OPEN]`
Triadic's \(Q_{s,*}^{\rm escape}\), \(Q_s^{\rm turn}\), and diagnostic ODE guards are not fracture-event predicates. They may not be imported to fill \(\mathcal D_{\rm event}\). The continuous event predicate remains OPEN unless a separate Genesis/Triadic source supplies it.

### BIRTH-AUDIT-11 `[AUDIT]`
The eleven contract fields are not uniformly absent. The source audit classifies them as a mixture of explicit OPENs, partial structures and missing bridges. In particular, a \(K_3\) target topology is supplied, while full event-level gluing is not.

### BIRTH-AUDIT-12 `[AUDIT]`
The literal TDR-G clean-star birth is \(K_{1,3}:4\to5\) (or \(M\to M+1\) in a larger state), not a supplied discrete \(\Phi_{2\to3}\). It is a structural comparator, not evidence that the discrete and continuous events are the same law.

### BIRTH-AUDIT-13 `[ALG / comparator scope]`
For the marked isolated TDR-G star event, the newborn is deterministically specified from the pre-event centre, old labels persist, and marked deletion plus centre-token reversal gives a left inverse on the stated local event image. This does not establish unmarked-history recoverability.

### BIRTH-AUDIT-14 `[AUDIT]`
The cross-branch continuous-versus-clean-star disposition is \(\texttt{UNDECIDED-MISSING-BRIDGE}\). Different arity and carrier prevent direct representation-equivalence claims without an explicit grouping/embedding/coarse-graining contract.

---

# 11. Eleven-field continuous source audit

The receiving-side source audit has now assessed all eleven original fields. “Missing” below means not supplied by the inspected formulation, not that no historical unpublished artifact ever existed.

| # | Field | Current continuous status | Next obligation |
|---:|---|---|---|
| 1 | Event/admissibility predicate | **MISSING COMPLETE PREDICATE** — fracture state and leading family named; no complete trigger/first-event rule | Specify predicate, timing, crossing/detection convention and ambient context |
| 2 | Retained-parent update \(s^+\) | **EXPLICITLY OPEN** — longitudinal retention unresolved | Declare retained-output map/readout and approximation order |
| 3 | Residual-to-child functional | **LEADING FAMILY ONLY** — cubic pieces and leading \(c_0\) supplied | Define complete functional of selected residual/event state |
| 4 | Physical \(\kappa\) | **REFERENCE POLICIES PRESENT; SELECTION OPEN** | Keep shear/recoil as reference policies; require independent selection criterion |
| 5 | Role identity / continuation | **SUPPLIED LABELS PARTIAL; NO EVENT DERIVATION** | Separate supplied/inherited/event-generated identity from lineage |
| 6 | Attachment / incidence | **TARGET TOPOLOGY PRESENT; FULL GLUING MISSING** — Triadic declares \(K_3\) | Specify endpoint/state realization and event-level incidence |
| 7 | Pre/post gauge actions | **LOCAL CHART DATA PRESENT; FULL CONTRACT ACTIONS MISSING** | State actions and covariance on event domain/output/attachment |
| 8 | Post-event representation map | **MISSING BRIDGE** | Construct \(H_{\rm post}\) only if representation equivalence is claimed |
| 9 | Post-event dynamics | **PARTIAL DIAGNOSTIC MODELS PRESENT** | Name exact map/flow/reduction and time correspondence |
| 10 | Comparison observables | **NATURAL OBSERVABLES PRESENT; ALIGNED COMPARISON MISSING** | Specify matched initial states, observables, continuations and precision |
| 11 | Recoverability quotient | **TRIAL LEFT INVERSE ONLY; FULL EVENT OPEN** | Declare marks, gauge quotient, retained data and event information available to inverse |

Two source guards are now explicit:

1. Triadic diagnostic conditions such as \(Q_s=0\), \(Q_c=0\), \(r=0\), and \(Q_sQ_c-I_{sc}^2=0\) are integration/event guards of the diagnostic dynamics, not automatically the fracture trigger for \(\Phi_{2\to3}\).
2. A reduced escape or sign-turn threshold is not a birth predicate unless a separate bridge states so.

Physical residual selection remains OPEN.

---

# 12. TDR-G clean-star comparison contract

## 12.1 Arity and event domain

The literal TDR-G comparison event is not \(2\to3\). Fix even \(N\) and integer \(k\) with \(0\le k\) and \(6k<N\). The local input is an already-labelled **four-node post-advance, pre-event snapshot**

\[
(A,L_1,L_2,L_3)
\]

whose entire local defect graph is the isolated \(K_{1,3}\) centred at \(A\).

Thus

\[
\boxed{
\Phi_\star:\;4\to5
}
\]

for this local adapter, or \(M\to M+1\) in a larger state.

The continuous residual slot \(\mathcal R_{\rm res}\) and continuous \(\kappa\) are **not applicable** here. Importing them would be a new cross-branch model input.

## 12.2 Literal source event

For one selected isolated star, modulo \(N\),

\[
\boxed{
\theta_E^+=\theta_A^-+\frac N2,\qquad
\delta_E^+=\delta_A^-,
\qquad
\delta_A^+=-\delta_A^-.
}
\]

Old phases are retained through the event and leaf tokens are unchanged. \(E\) is a fresh label. The child copies the **pre-event** centre token; it is not advanced again during the same tick.

The output lies on a constrained image, including

\[
\theta_E^+-\theta_A^+=\frac N2,
\qquad
\delta_E^++\delta_A^+=0\pmod N.
\]

## 12.3 Identity and attachment

Initial node identity is **SUPPLIED** by the indexed model. Old labels continue and a fresh child label is appended. Hence

\[
\text{generated from }A\ne\text{identical to }A.
\]

Defect adjacency is reconstructed from node phases; it is an observable of the node state, not an independently glued permanent edge field.

For the stated isolated narrow-band \(K_{1,3}\) input, the newborn is defect-related to the centre and not to the three leaves, so the immediate local output defect graph is \(K_{1,4}\). This is instantaneous and local; later evolution or outside nodes can change the graph.

## 12.4 Gauge and marked recoverability

The declared gauge is common phase shift,

\[
g_a(\theta_i,\delta_i)
=
(\theta_i+a,\delta_i)\pmod N.
\]

The local star event is covariant under this action. A common token shift is **not** silently added as another gauge action.

With centre \(A\), newborn \(E\), and event type known, delete \(E\) and recover

\[
\theta_i^-=\theta_i^+,
\qquad
\delta_A^-=-\delta_A^+=\delta_E^+,
\qquad
\delta_i^-=\delta_i^+\quad(i\ne A).
\]

Thus the marked local event has a left inverse and is injective on the corresponding marked phase-gauge quotient. This does not establish recoverability from an unmarked final state, unknown simultaneous events, or an arbitrary history.

## 12.5 Concrete source example

For \(N=24,\;k=1\),

\[
\theta^-=(0,11,12,13),
\qquad
\delta^-=(2,1,5,7)
\]

maps to

\[
\theta^+=(0,11,12,13,12),
\qquad
\delta^+=(22,1,5,7,2).
\]

The child copies \(2\), not the updated centre token \(22\), and its phase is \(12\), not \(14\).

## 12.6 Cross-branch comparison status

The common schema now supports the question

> How does each event realize a new represented role, retain prior structure, constrain its output, and permit or prevent recovery?

But it does **not** identify the two events:

\[
\text{continuous }\Phi_{2\to3}
\quad\not\equiv_{\rm supplied}\quad
\text{literal modular }K_{1,3}\text{ birth}.
\]

A direct representation-equivalence claim requires an additional grouping, embedding or coarse-graining contract plus aligned observables.

Therefore the present cross-branch verdict is

\[
\boxed{
\texttt{UNDECIDED-MISSING-BRIDGE}.
}
\]

---
# 13. Next executable step — minimal conditional continuous completion

The broad source audit is complete enough to stop searching for a fully specified event that the inspected owner texts do not contain.

The next calculation is to define a **minimal conditional completion** of the continuous branch without promoting the added premises to owner facts.

Introduce a completion package

\[
\Xi
=
\bigl(
\mathcal D_{\rm frac},
\Pi_{\rm ret},
\mathcal C_{\rm child},
\mathcal A_{K_3},
\mathcal G_{\rm event},
\mathcal O_{\rm cmp}
\bigr),
\]

where each slot is explicitly marked `[HYP/CHOICE]` unless sourced:

- \(\mathcal D_{\rm frac}\): a fracture/event domain and timing rule;
- \(\Pi_{\rm ret}\): the retained-parent update \(s\mapsto s^+\);
- \(\mathcal C_{\rm child}\): the **complete** residual-to-child functional, reducing at cubic order to the documented shear/recoil policies where appropriate;
- \(\mathcal A_{K_3}\): an event-level state/endpoint realization of the declared \(K_3\) target;
- \(\mathcal G_{\rm event}\): pre/post gauge actions and covariance;
- \(\mathcal O_{\rm cmp}\): aligned observables/continuations capable of seeing the first quartic contract differences or later attachment/evolution differences.

For each residual branch \(R\in\{E_{\rm raw},E_{\rm odd},E_{\rm NF}\}\), construct

\[
\mathfrak B_R[\Xi]
\]

with the **same** completion package wherever the typing permits. This prevents a residual comparison from being contaminated by changing attachment, retention or observables at the same time.

Only then compare complete same-branch contracts under the whole-contract equivalence test of §5.

The TDR-G clean-star remains a structural comparator for identification, deterministic child data and marked recoverability. It does not choose \(\Xi\), a continuous residual, or a continuous network chart.

---

**Draft boundary:** this document changes no owner source, does not adopt a birth residual or continuous fracture predicate, does not identify the TDR-G star with \(\Phi_{2\to3}\), and does not turn the PRR dyad-first interpretation into an established Genesis ontology.
