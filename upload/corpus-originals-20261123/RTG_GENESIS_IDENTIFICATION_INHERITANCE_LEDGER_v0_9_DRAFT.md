# RTG Genesis Identification & Inheritance Ledger v0.9 — DRAFT

**Date:** 28 September 2026  
**Status:** WORKING DRAFT — noncanonical; no owner adoption; no Genesis RID regraded or replaced.  
**Study:** GUP-08 / GUP-09 — physical birth residual + identification/inheritance contract.  
**Current scope:** continuous \(\Phi_{2\to3}\) branch plus the separately typed TDR-G clean-star comparator. v0.9 imports the RRF v0.6 representation lock as a working discipline, separates the registered dyad relabel candidate \(S_h\) from network bookkeeping/Jacobi sign reversal, corrects the relabel interpretation of raw versus odd residuals, and makes OPEN-A together with the OPEN-B/E1 bridge explicit dependencies of the Genesis residual/identity question. No physical birth law, fracture predicate, child functional, physical pole-relabel action, information principle, network bridge, or post-birth dynamics is selected.  
**Owner baseline:** `RTG_GENESIS_GEOMETRY_DSN_v2.8.4` (retained owner baseline, under the frozen noncanonical Genesis correction ledger).  

## 0. Source discipline

This draft uses the following sources as distinct authorities:

- `RTG_GENESIS_GEOMETRY_DSN_v2.8.4` — historical owner formulation of \(\Phi_{2\to3}\).
- `GENESIS_CORRECTION_LEDGER_v0_1_FROZEN.md` — frozen noncanonical correction record; not owner adoption.
- `RTG_DYADIC_OSCILLATOR_DSN_v6.4.10` — raw / odd-projected / polynomial-conjugacy object separation.
- `RTG_TRIADIC_BIRTH_LIFT_DSN_v1.5` — diagnostic birth-angle / \(J_Q\) route record.
- `RTG_PRIMORDIAL_RELATIONAL_REPRESENTATION_WRAPUP_v0.3` — noncanonical representation/identity framework and proposed inheritance-ledger fields.
- `RTG_RRF_REPRESENTATION_REGISTRY_v0.6` — noncanonical candidate working representation standard used here as the profile/transport discipline; it does not amend owner science. RRF §7 explicitly leaves Genesis inheritance fields unregistered pending this ledger.
- `BIRTH_CONTRACT_REVIEW.md` — receiving-side source audit and review; noncanonical, no owner adoption.
- `contract_field_audit.json` — machine-readable eleven-field source-status audit used in §11.
- `TDRG_CLEAN_STAR_SOURCE_CONTRACT.md` — source-level extraction of the literal TDR-G clean-star event; comparison branch only.
- `V0_3_RECEIVING_REVIEW (1).md` — receiving-side v0.3 verification and interpretation correction; noncanonical.
- `CONDITIONAL_SNAPSHOT_TEST (1).md` — explicitly conditional common-completion event-snapshot test; noncanonical diagnostic.
- `RTG_RELATIONAL_RECOGNITION_DSN_v0.3.4` — current inspected recognition owner: R8/R9 theorem closures; pole-swap covariance remains unresolved under R1/representation typing; its header still carries stale NUMGEN/OFN companion pointers.
- `V0_4_RECEIVING_REVIEW.md` — receiving-side verification and scope corrections for v0.4; noncanonical.
- `CHILD_FUNCTIONAL_RESULTS.md` — conditional child-functional survival/erasure calculations; noncanonical working deductions.
- `Pasted markdown(20260928-151204).md` — receiving summary of the child-functional audit; noncanonical.
- `V0_6_RECEIVING_REVIEW.md` — receiving-side verification and scope/access review of v0.6; noncanonical.
- `PROPOSED_SCOPE_PATCHES.md` — unapplied narrow wording/typing patches proposed by the v0.6 review; noncanonical.
- `Pasted text.txt` — concise receiving summary of the same v0.6 access/scope audit; noncanonical.
- `RTG_NUMBER_GENESIS_DSN_v1.20.2` — inspected for synchronization only; its banner reports scientific-state-identical methodology successor v1.20.3, which is not present in the project. No new Genesis birth-contract import is taken from it.

Tags used here:
- `[SOURCE]` — directly reported by an inspected owner/source.
- `[ALG]` — direct mathematical deduction from explicitly stated definitions.
- `[AUDIT]` — source-comparison finding.
- `[HEUR]` — proposed research convention.
- `[OPEN]` — missing physical/model selection or missing bridge.

No `[THM]` or owner-level `[RESULT]` is created by this draft.

## 0.1 Representation annotation discipline

This revision adopts the RRF v0.6 equation-suffix discipline as a **working representation safety rule**:

```text
<equation>   (rep: <PROFILE-ID>; <scope/exactness>)
<equation>   (transport: <SRC> → <DST>; <arrow/bridge>; <scope>)
```

Registered profiles used here are:

- `RRF-DYAD-W` — lifted dyad \(W\)-frame; registered relabel candidate \(S_h=h_6(-I)h_6^{-1}\);
- `RRF-DYAD-NF` — normal-form \(z\)-frame; registered profile involution \(z\mapsto-z\);
- `RRF-NET-W-RAW` — provisional network raw-edge profile; \(\mathscr O_e\) is bookkeeping reorientation, **not** a pole-relabel candidate.

RRF v0.6 explicitly does **not** yet register:

- Genesis inheritance fields;
- a TDR-G discrete profile;
- the bridge `RRF-DYAD-W → RRF-NET-W-RAW`.

Accordingly, this ledger uses explicit sentinels rather than inventing profiles:

- `(rep: [UNREGISTERED-GENESIS]; ...)`;
- `(rep: [UNREGISTERED-TDRG]; ...)`;
- `(rep: [ABSTRACT]; ...)`.

These are **not new RRF profile IDs**. They mark exactly where registration/bridge work is still open.

No equation may use the sign action of one profile as the relabel law of another without an explicit registered transport or an `[OPEN]` bridge.

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
\mathcal A_{\rm access},
\mathcal C_{\rm child},
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
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)

Here:

- \(\mathcal D_{\rm event}\) is the event/admissibility domain, including timing/detection convention;
- \(\mathcal R_{\rm res}\) is the residual/projection operation when the model has one; for a model such as the literal TDR-G star event it may be **not applicable**, not a missing continuous parameter;
- \(\mathcal A_{\rm access}\) is itself structured:
  \[
  \mathcal A_{\rm access}
  =
  (\mathcal X_{\rm full},\mathcal M_{\rm fixed},a,\Omega_{\rm allow}),
  \]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)
  where \(\mathcal X_{\rm full}\) contains the complete independently variable event input, \(\mathcal M_{\rm fixed}\) is fixed/known model structure, \(a:\mathcal X_{\rm full}\to\mathcal Y_{\rm read}\) is the permitted readout, and \(\Omega_{\rm allow}\) lists permitted evaluations/reconstructions. This distinguishes independent data from values computable from already known state/model information;
- \(\mathcal C_{\rm child}\) is the typed residual/parent-to-child constitutive functional, including its domain, regularity, magnitude semantics and whether it is linear, nonlinear, normalizing or residual-independent;
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
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)

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
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)

where \(V_{\rm role}\) is the carrier, \(B_{\rm role}\) its declared bilinear/Gram form when one is used, and \(\jmath_{\rm role}\) its embedding into any common post-event carrier. Provenance is one of **SUPPLIED / INHERITED / EVENT-GENERATED / OPEN**. Using the parent \(B\) on a new role is therefore a modelling choice unless its inheritance is established.

The post-state is initially an **admissible set**

\[
\mathcal S_{\rm post}^{\rm adm}
=
\{x:\mathcal C_{\rm post}(x)=0,\ldots\},
\]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)

not assumed to be a regular manifold at the event.

For child-functional comparisons, record at least these independent axes:

1. **data access** — parent-only / pointwise residual / paired residual / field / history;
2. **residual dependence** — none / linear / nonlinear;
3. **magnitude semantics** — preserve / project / normalize / impose from parent data;
4. **regularity and domain** — including any excluded zero-projection or alignment locus;
5. **identity/gauge covariance** — relative to the declared pre/post role actions;
6. **cubic-target compatibility** — whether the documented \(C_3^\kappa=\kappa QJ_Qs\) is retained;
7. **information retention** — which residual distinctions are discarded by construction.

These axes are part of the physical contract. Algebraic convenience does not select them.

At the ordinary set-map level, a child rule uses only the declared readout \(a\) iff it factors through that readout:

\[
\boxed{
\mathcal C(x)=\widetilde{\mathcal C}(a(x)).
}
\]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)

Equivalently,

\[
\boxed{
a(x)=a(y)
\Longrightarrow
\mathcal C(x)=\mathcal C(y).
}
\]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)

This is a determinacy/fibre test only. Regularity, locality, causal availability and permitted computation are additional conditions on the factorization.

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
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

`[OPEN]` The inspected \(\Phi_{2\to3}\) block names the fracture state but does not, by itself, provide a complete standalone event-admissibility predicate \(\mathcal D_{\rm event}\).

## 2.2 Historical residual declaration

`[SOURCE]` Genesis v2.8.4 writes

\[
E_*=F_6(s_*)-s_*,
\]
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

and gives the cubic pieces

\[
E_{\parallel,*}=-\frac12Q_s s_*,
\qquad
E_{\perp,*}=-\tau Q_sJ_Qs_*.
\]
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

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
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

`[AUDIT]` These remainder orders are **owner-source wording, not yet contract-invariant facts**. They hold if the residual-to-child functional removes the quartic raw contribution (as in an odd/NF-type fifth-order remainder) or otherwise annihilates it. If a quartic term reaches \(c_0\), the generic orders weaken to

\[
c_0=\kappa Q_sJ_Qs_*+O(|s_*|^4),
\]
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

\[
\frac{W(c_0)}{W(s_*)}
=i\kappa Q_s+O(Q_s^{3/2}),
\]
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

\[
\arg\frac{W(c_0)}{W(s_*)}
=
-\frac{\pi}{2}+O(Q_s^{1/2})
\quad(\kappa<0),
\]
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

and

\[
Q_c=\kappa^2Q_s^3+O(Q_s^{7/2}).
\]
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

Which order applies is controlled by the still-OPEN full residual-to-\(c_0\) functional.

Reference policies:

\[
\kappa_{\rm shear}=-\frac{2\sqrt3}{3},
\qquad
\kappa_{\rm recoil}=-\frac12.
\]
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

`[ALG]` With

\[
\mu_6=-\frac12-i\frac{2\sqrt3}{3},
\]
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

the two reference coefficients are exactly its real and imaginary parts:

\[
\boxed{
\kappa_{\rm recoil}=\Re\mu_6,
\qquad
\kappa_{\rm shear}=\Im\mu_6.
}
\]
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

For the shared cubic residual decomposition

\[
E^{[3]}_*
=
E^{[3]}_{\parallel,*}
+
E^{[3]}_{\perp,*},
\]
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

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
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

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
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

This is an algebraic identification of the documented cubic pieces, not a derivation that these projections are the complete physical birth functionals.

`[SOURCE]` Physical \(\kappa\) is not selected by the existing capacity-matching route.

## 2.4 Longitudinal branch

`[SOURCE]` Genesis leaves

\[
\lambda_\parallel
\]
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

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
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

This is a source-completeness finding, not a rejection of the historical model.

---

# 3. Residual register — keep the three objects visible

## 3.1 Raw residual `(rep: RRF-DYAD-W)`

\[
E_{\rm raw}(w)=F_W(w)-w.
\]
(rep: RRF-DYAD-W; lifted local unless explicitly specialised)

`[SOURCE]` Dyadic v6.4.10 records a nonzero quartic part \(F_4\), with channels \((4,0),(3,1),(2,2),(1,3)\), and gives the positive-real-ray value

\[
F_4(t)
=
-\frac{5+25i\sqrt3}{48}t^4
\ne0.
\]
(rep: RRF-DYAD-W; lifted local unless explicitly specialised)

`[ALG — reconstruction from the sourced primitive \(T\)]` Exact degree-four composition of the declared primitive map through six steps and conversion through

\[
W=\mathcal L(\rho,\eta)
=
\rho-\frac{\eta}{2}
+i\frac{\sqrt3}{2}\eta
\]
(rep: RRF-DYAD-W; lifted local unless explicitly specialised)

gives

\[
\boxed{
\begin{aligned}
F_4(W,\bar W)=&
\left(-\frac1{16}+\frac{7i\sqrt3}{144}\right)W^4\\
&+\left(-\frac16-\frac{2i\sqrt3}{9}\right)W^3\bar W\\
&+\left(-\frac5{24}-\frac{11i\sqrt3}{24}\right)W^2\bar W^2\\
&+\left(\frac13+\frac{i\sqrt3}{9}\right)W\bar W^3.
\end{aligned}
}
\]
(rep: RRF-DYAD-W; lifted local unless explicitly specialised)

The coefficient sum on \(W=\bar W=t\) reproduces the owner ray value exactly. Since every monomial has total degree four,

\[
\boxed{
F_4(-W,-\bar W)=F_4(W,\bar W).
}
\]
(rep: RRF-DYAD-W; lifted local unless explicitly specialised)

Thus the leading raw-minus-odd difference is swap-even under the naive sign action.

**Status in this ledger:** historical Genesis raw-residual reference plus an independent exact reconstruction of its degree-four coefficient polynomial.  
**Physical selection:** `[OPEN]`.

## 3.2 Odd-projected residual `(rep: RRF-DYAD-W; parity operation defined with naive \(-I\), not thereby the registered pole relabel)`

\[
E_{\rm odd}(w)
=
\frac{F_W(w)-F_W(-w)}2-w.
\]
(rep: RRF-DYAD-W; lifted local unless explicitly specialised)

`[SOURCE]`

\[
E_{\rm odd}(w)
=
\mu|w|^2w+O(|w|^5),
\]
(rep: RRF-DYAD-W; lifted local unless explicitly specialised)

and

\[
E_{\rm raw}(w)-E_{\rm odd}(w)
=
F_4(w)+O(|w|^6).
\]
(rep: RRF-DYAD-W; lifted local unless explicitly specialised)

The \(F_4+O(|w|^6)\) statement is source-backed by the Dyadic six-step return/parity ledger; it is not inferred here from a generic near-identity map. In particular, the owner return has identity linear part, certified cubic leading defect and the stated quartic even part, so there is no unrecorded quadratic even term being silently dropped.

**Status:** mathematically defined projection/diagnostic.  
**Physical selection as Genesis birth input:** `[OPEN]`.

## 3.3 NF-native residual `(rep: RRF-DYAD-NF; transport to W only through T-h)`

Let

\[
\widehat F=h^{-1}\circ F_W\circ h.
\]
(transport: RRF-DYAD-NF → RRF-DYAD-W; T-h; certified local domain)

Then

\[
E_{\rm NF}(z)=\widehat F(z)-z
=
\mu|z|^2z+O(|z|^5).
\]
(transport: RRF-DYAD-NF → RRF-DYAD-W; T-h; certified local domain)

`[ALG]` On the domain of the conjugacy,

\[
\boxed{
E_{\rm raw}(h(z))
=
h\!\left(z+E_{\rm NF}(z)\right)-h(z).
}
\]
(transport: RRF-DYAD-NF → RRF-DYAD-W; T-h; certified local domain)

Thus raw and NF residuals describe the same isolated-dyad pre/post return states when **the complete map is transported**. A finite displacement does not transform exactly as a tangent vector:

\[
E_{\rm raw}(h(z))
\ne
Dh(z)E_{\rm NF}(z)
\quad\text{in general}.
\]
(transport: RRF-DYAD-NF → RRF-DYAD-W; T-h; certified local domain)

**Status:** chart-native residual.  
**Use as Genesis birth input without full contract transport:** `[OPEN]`.

---

# 3.4 Actual \(h_2\): child-field covariance defect versus finite-displacement transport

`[import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.10]` The Dyadic Birkhoff frame is

\[
\mathcal L(\rho,\eta)
=
\rho-\frac{\eta}{2}
+i\frac{\sqrt3}{2}\eta,
\]
(transport: RRF-DYAD-NF → RRF-DYAD-W; T-h; certified local domain)

which is the same complex \(W\)-coordinate used for the Genesis/Dyadic local birth comparison. The adopted quadratic normalizer is

\[
h(z,\bar z)
=
z+h_2(z,\bar z)+O(|z|^3),
\]
(transport: RRF-DYAD-NF → RRF-DYAD-W; T-h; certified local domain)

\[
h_2
=
-\frac{1+i\sqrt3}{12}z^2
-\frac13z\bar z
+\frac{1-i\sqrt3}{24}\bar z^2.
\]
(transport: RRF-DYAD-NF → RRF-DYAD-W; T-h; certified local domain)

The owner records \(h_2\) as the unique quadratic change that removes the raw quartic return \(F_4\). Thus raw/odd/NF do not contain independent unrelated quartic effects:

- \(E_{\rm raw}\) retains the even quartic \(F_4\);
- \(E_{\rm odd}\) removes that even quartic by projection in the raw \(W\)-frame;
- \(E_{\rm NF}\) absorbs the same raw quartic into the chart through \(h_2\).

This does **not** mean that a child rule may be copied between charts unchanged.

Let the cubic child field in complex form be

\[
C_3(z,\bar z)=i\kappa z^2\bar z.
\]
(transport: RRF-DYAD-NF → RRF-DYAD-W; T-h; certified local domain)

`[ALG]` If the same coordinate formula is naively reused after changing chart, the degree-four covariance defect is

\[
[C_3(h)-Dh\,C_3]_4
=
DC_3(z)h_2(z)-Dh_2(z)C_3(z).
\]
(transport: RRF-DYAD-NF → RRF-DYAD-W; T-h; certified local domain)

On the real ray \(z=\bar z=t\),

\[
\boxed{
[C_3(h)-Dh\,C_3]_4
=
\frac{\kappa(\sqrt3-21i)}{24}t^4\ne0
}
\]
(transport: RRF-DYAD-NF → RRF-DYAD-W; T-h; certified local domain)

for \(\kappa t\ne0\).

This is a **child-field covariance defect under the fixed chart change**. It is not the finite-displacement/secant error.

For a cubic displacement \(v=C_3(z)=O(|z|^3)\), define

\[
\delta_h(z;v)=h(z+v)-h(z).
\]
(transport: RRF-DYAD-NF → RRF-DYAD-W; T-h; certified local domain)

Then

\[
\delta_h(z;C_3(z))-Dh(z)C_3(z)
=
h_2(C_3(z))+O(|z|^7)
=
O(|z|^6).
\]
(transport: RRF-DYAD-NF → RRF-DYAD-W; T-h; certified local domain)

For the actual \(h_2\) and \(z=t\in\mathbb R\),

\[
\boxed{
\delta_h(t;C_3(t))-Dh(t)C_3(t)
=
\frac{\kappa^2(-7+3i\sqrt3)}{24}t^6+O(t^7).
}
\]
(transport: RRF-DYAD-NF → RRF-DYAD-W; T-h; certified local domain)

Accordingly, two different order statements coexist:

| Question | First discrepancy here |
|---|---:|
| Reuse the cubic child field across the chart: \(C_3(h)\) vs \(Dh\,C_3\) | degree 4 |
| Replace finite displacement by tangent transport: \(h(z+C_3)-h(z)\) vs \(Dh\,C_3\) | degree 6 |

The exact isolated residual transport remains

\[
E_{\rm raw}(h(z))
=
h(z+E_{\rm NF}(z))-h(z),
\]
(transport: RRF-DYAD-NF → RRF-DYAD-W; T-h; certified local domain)

so

\[
E_{\rm raw}(h(z))-Dh(z)E_{\rm NF}(z)=O(|z|^6).
\]
(transport: RRF-DYAD-NF → RRF-DYAD-W; T-h; certified local domain)

Therefore the quartic covariance defect is relevant to a **hybrid or naively reused child prescription**; it is not evidence that two fully and consistently transported physical contracts already differ at quartic order.


# 3.5 Relabel actions are profile-typed

The word “pole swap” is not used untyped in this ledger.

## 3.5.1 Registered dyad actions

In the normal-form profile the registered representation-level involution is

\[
z\mapsto-z.
\]
(rep: RRF-DYAD-NF; registered profile involution)

Transport through the certified normalizer gives the exact local involution

\[
\boxed{
S_h
=
h_6\circ(-I)\circ h_6^{-1}
}
\]
(rep: RRF-DYAD-W; exact involution on the certified local domain)

with leading expansion

\[
\boxed{
S_h(W)
=
-W+2h_2(W,\bar W)+O(|W|^3).
}
\]
(rep: RRF-DYAD-W; local expansion)

RRF v0.6 registers

\[
\mathcal J_{\le6}(f\circ S_h-S_h\circ f)=0
\]
(rep: RRF-DYAD-W; one-step delivered map; finite-jet statement with RRF provenance)

but keeps **OPEN-A** for the physical interpretation:

\[
\boxed{
\text{registered representation involution}
\;\not\equiv_{\rm established}\;
\text{physical pole relabel}.
}
\]
(rep: [ABSTRACT]; RRF OPEN-A)

The primitive/lifted naive sign map

\[
(\rho,\eta)\mapsto(-\rho,-\eta)
\]
(rep: RRF-DYAD-LIFT; diagnostic sign action, not registered relabel candidate)

is not the transported \(S_h\) action; indeed

\[
T(-\rho,-\eta)+T(\rho,\eta)
=
\left(0,2(\cosh\rho-1)\right).
\]
(rep: RRF-DYAD-LIFT; exact identity)

That identity therefore diagnoses failure of the **naive sign action**, not failure of the registered \(S_h\) relabel candidate.

## 3.5.2 Network/Jacobi action is a different profile

In the node-mediated sequential Jacobi bookkeeping,

\[
s=(1,-1,0,0),\qquad
c=\left(\frac12,\frac12,-1,0\right),\qquad
d=\left(\frac13,\frac13,\frac13,-1\right).
\]
(rep: RRF-NET-W-RAW; node-mediated Jacobi branch, provisional)

The label exchange \(A\leftrightarrow B\) gives

\[
\boxed{
s\mapsto-s,\qquad c\mapsto c,\qquad d\mapsto d.
}
\]
(rep: RRF-NET-W-RAW; node-label/Jacobi action)

RRF's native network reorientation is

\[
\mathscr O_e:
\quad
W_e^{\rm net}\mapsto-W_e^{\rm net},
\qquad
\epsilon_{\gamma e}\mapsto-\epsilon_{\gamma e}.
\]
(rep: RRF-NET-W-RAW; bookkeeping reorientation)

RRF explicitly states that \(\mathscr O_e\) is **not** the dyad pole-relabel candidate \(S_h\). The bridge

\[
RRF\text{-}DYAD\text{-}W
\;\dashrightarrow\;
RRF\text{-}NET\text{-}W\text{-}RAW
\]
(transport: RRF-DYAD-W → RRF-NET-W-RAW; `[OPEN]`; OPEN-B/E1)

is not registered. Therefore the Jacobi sign action may not be substituted for \(S_h\) inside the isolated-dyad return.

## 3.5.3 Raw versus odd: the covariance verdict reverses with the action

Define the odd-projected six-step return

\[
F_{\rm odd}(W)
:=
\frac{F_W(W)-F_W(-W)}{2}.
\]
(rep: RRF-DYAD-W; diagnostic projection defined by naive \(-I\))

Let

\[
D_S(F):=F\circ S-S\circ F.
\]
(rep: [ABSTRACT]; covariance-defect notation)

Using the exact quartic \(F_4\) of §3.1 and the published \(h_2\), an independent degree-four calculation gives

\[
\boxed{
D_{-I}(F_W)
=
2F_4+O(|W|^6),
\qquad
D_{-I}(F_{\rm odd})=0.
}
\]
(rep: RRF-DYAD-W; naive-\(-I\) diagnostic action, not the registered W-profile relabel)

For the registered \(W\)-profile involution,

\[
\boxed{
D_{S_h}(F_W)
=
0
\quad\text{through degree }4,
}
\]
(rep: RRF-DYAD-W; independent degree-4 check; RRF source registers stronger one-step finite-jet commutation)

whereas

\[
\boxed{
D_{S_h}(F_{\rm odd})
=
-2F_4+O(|W|^5).
}
\]
(rep: RRF-DYAD-W; independent degree-4 check)

Thus:

\[
\boxed{
\begin{array}{c|cc}
&F_W&F_{\rm odd}\\ \hline
\text{naive }-I&\text{quartic defect }2F_4&\text{covariant by construction}\\
S_h&\text{covariant through checked order}&\text{quartic defect }-2F_4
\end{array}
}
\]
(rep: RRF-DYAD-W; action-dependent covariance summary)

The earlier statement “\(E_{\rm odd}\) is the relabel-covariant residual” is therefore withdrawn as an **untyped** statement. The correct statement is:

\[
\boxed{
\text{residual covariance is a property of }
(\text{residual operation},\text{profile},\text{relabel action}).
}
\]
(rep: [ABSTRACT]; representation-safety rule)

Consequently GUP-08 residual selection depends not only on the consumer birth law but also on **OPEN-A**: which registered/physical involution, if any, represents pole relabeling.

## 3.5.4 What remains of the cubic Genesis obstruction

The Genesis/Jacobi cubic target is

\[
C_3^\kappa(s)=\kappa Q(s)J_Qs.
\]
(rep: [UNREGISTERED-GENESIS]; inheritance/profile assignment pending RRF §7)

Under the node-mediated Jacobi action,

\[
C_3^\kappa(-s)=-C_3^\kappa(s),
\qquad
c\mapsto c.
\]
(rep: RRF-NET-W-RAW; leading node-mediated parity statement)

The registered dyad involution has the same **linear** part,

\[
S_h(W)=-W+O(|W|^2).
\]
(rep: RRF-DYAD-W; local linearisation)

Hence the previously derived cubic parity obstruction survives only in the following scoped sense:

> `[ALG / bridge-conditional]` If a future `RRF-DYAD-W → Genesis/network` bridge transports the linearized dyad relabel to the standard Jacobi \(A\leftrightarrow B\) action, while \(\kappa\) is fixed and the child role remains swap-even, the nonzero cubic target cannot descend to that simple quotient.

This is **not** a currently registered cross-profile covariance theorem. OPEN-B/E1 is precisely the missing bridge.

## 3.5.5 Owner-pass consequence for GCL-06

The frozen correction ledger remains unchanged. For a future Genesis owner claim-status pass, the GCL-06 route should record:

\[
\boxed{
\text{physical residual selection}
\;\text{ depends on }\;
\text{consumer birth contract}
+\text{ RRF OPEN-A}
+\text{ OPEN-B/E1 profile bridge}.
}
\]
(rep: [ABSTRACT]; proposed owner-pass dependency, not owner adoption)

Selecting \(E_{\rm raw}\), \(E_{\rm odd}\), or \(E_{\rm NF}\) without those dependencies would again conflate mathematical projection, representation transport, and physical relabeling.

---

# 4. Complete-contract classification

The three residual formulas do **not** automatically define three inequivalent physical models.

| Contract candidate | Definition | Current classification |
|---|---|---|
| `B-RAW-HIST` | Historical Genesis contract retaining \(E_{\rm raw}\) as the named residual | **Reference contract, incomplete; compatible with registered \(S_h\) covariance through the checked quartic order, but physical relabel remains OPEN-A** |
| `B-ODD-PROJ` | Apply the naive-\(-I\) odd projection in `RRF-DYAD-W` before the birth rule | **Additional same-frame operation; covariance depends on relabel action; physical role OPEN-A / consumer bridge OPEN** |
| `B-NF-TRANSPORT` | Transport the entire birth contract through valid pre/post chart maps \(H_{\rm pre},H_{\rm post}\) | **Potentially REP-EQUIV; isolated residual transport is exactly the raw finite displacement, but the post-event/network transport remains missing** |
| `B-NF-HYBRID` | Insert \(E_{\rm NF}\), \(Dh\,E_{\rm NF}\), or an unchanged NF child formula into an otherwise raw contract | **Same cubic leading data; chart-covariance defects can appear from quartic order; not justified as a coordinate change** |

The verdict vocabulary is

\[
\texttt{REP-EQUIV},
\qquad
\texttt{PHYS-DISTINCT},
\qquad
\texttt{UNDECIDED-MISSING-BRIDGE}.
\]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)

Guard:

\[
\boxed{
\text{failure to prove REP-EQUIV does not imply PHYS-DISTINCT}.
}
\]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)

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
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)

\[
\boxed{
\widehat\Phi
=
H_{\rm post}^{-1}\circ
\Phi\circ
H_{\rm pre},
}
\]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)

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
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)

The comparison must also transport consistently:

- gauge actions and physical quotient;
- retained-parent update \(R_{\rm ret}\) and readout \(\Pi_{\rm ret}\), with \(\Pi_{\rm ret}\circ\Phi=R_{\rm ret}\) when that retention is held fixed;
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
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)

This is separate from dynamical reduction. Given an embedding \(\iota\), the reduction question is

\[
\boxed{
T_{\rm post}\circ\iota
=
\iota\circ T_{\rm pre}.
}
\]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)

Failure for one proposed \((\iota,T_{\rm pre})\) does not rule out every admissible reduction. Conversely, the differential-rank bound of §9 does not establish this intertwining identity.

---
# 6. Identification / inheritance test

Let \(\mathcal P\) be pole occurrences and let

\[
\mathcal V=\mathcal P/\!\sim_I
\]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)

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
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)

must preserve identity classes:

\[
p\sim_{I_t}q
\Longrightarrow
\ell_t(p)\sim_{I_{t+1}}\ell_t(q).
\]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)

That implication alone permits two distinct source classes to merge. In a sector declared to have **neither splitting nor merging**, require reflection as well:

\[
\boxed{
p\sim_{I_t}q
\Longleftrightarrow
\ell_t(p)\sim_{I_{t+1}}\ell_t(q)
}
\]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)

on the retained domain, equivalently injectivity of the induced continuation on retained role classes.

Continuation and ancestry are distinct:

\[
\boxed{
\text{generated from }A
\ne
\text{identical to }A.
}
\]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)

---

# 7. Leading trial map — what it proves and what it does not

For diagnostic purposes only, take

\[
s^+=s,
\qquad
c=\kappa Q(s)J_Qs,
\]
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

and define

\[
\iota(s)=\bigl(s,\kappa Q(s)J_Qs\bigr).
\]
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

With

\[
J_Q=
\frac1{\sqrt3}
\begin{pmatrix}
1&-2\\
2&-1
\end{pmatrix},
\]
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

the companion checker verifies:

\[
J_Q^\top BJ_Q=B,
\qquad
s^\top BJ_Qs=0,
\]
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

and

\[
\operatorname{Gram}_B(s,c)
=
\begin{pmatrix}
Q&0\\
0&\kappa^2Q^3
\end{pmatrix}.
\]
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

Because the first output slot is \(s\),

\[
\pi_s\circ\iota=\mathrm{id},
\qquad
\operatorname{rank}D\iota=2.
\]
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

Hence, for this trial family,

\[
\boxed{
\text{new geometric direction}
\ne
\text{new independently supplied birth datum}.
}
\]
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

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
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

is the unit quarter-turn **direction identity**.

For the homogeneous leading child,

\[
\boxed{
\frac{W(c)}{W(s)}
=
i\kappa Q(s).
}
\]
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

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
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

If a quartic residual/chart contribution reaches the child,

\[
\boxed{
\frac{W(c_0)}{W(s_*)}
=
i\kappa Q_s+O(Q_s^{3/2}),
}
\]
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

and only

\[
\boxed{
\arg\frac{W(c_0)}{W(s_*)}
=
-\frac{\pi}{2}+O(Q_s^{1/2})
}
\]
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

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
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)

so

\[
\operatorname{rank}D(T_{\rm post}^n\circ\iota)
\le
\operatorname{rank}D\iota.
\]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)

This is an information-parameter bound, not a theorem of dynamical reducibility.

---

# 10. First GUP-08/09 findings

### BIRTH-AUDIT-01 `[AUDIT]`
The current owner formulation does not yet provide a complete continuous \(2\to3\) birth contract.

### BIRTH-AUDIT-02 `[ALG]`
Raw and NF residuals are related by finite map transport, not by naive tangent-vector substitution.

### BIRTH-AUDIT-03 `[AUDIT]`
Odd projection is an additional same-\(W\)-frame operation defined using the naive sign action. It is covariant under that diagnostic \(-I\) by construction, but it is **not** covariant under the registered `RRF-DYAD-W` involution \(S_h\) at quartic order: \(D_{S_h}(F_{\rm odd})=-2F_4+O(5)\). The raw return shows the opposite degree-four covariance pattern. Physical meaning therefore depends on RRF OPEN-A.

### BIRTH-AUDIT-04 `[ALG / conditional diagnostic]`
Under the leading trial family, the new \(J_Qs\) direction is not a new independently supplied birth datum.

### BIRTH-AUDIT-05 `[OPEN]`
No inspected source currently justifies privileging \(E_{\rm raw}\), \(E_{\rm odd}\), or \(E_{\rm NF}\) as the physical \(\Phi_{2\to3}\) input. The selection depends on the complete consumer birth contract, on RRF OPEN-A (physical relabel action), and on the unregistered DYAD-W → Genesis/network inheritance bridge under OPEN-B/E1.

### BIRTH-AUDIT-06 `[OPEN]`
The provenance of shared-role identity and the exact attachment semantics of the continuous birth remain to be specified before node/pole persistence can be classified.

### BIRTH-AUDIT-07 `[ALG]`
The shear and recoil reference coefficients are exactly \(\Im\mu_6\) and \(\Re\mu_6\). At cubic order the shear policy selects \(E_\perp^{[3]}\), while the recoil policy applies \(J_Q\) to \(E_\parallel^{[3]}\). This partially fills the residual-to-\(c_0\) field **at cubic order only**.

### BIRTH-AUDIT-08 `[ALG]`
Using the actual published Dyadic \(h_2\), a cubic child formula copied unchanged between charts has a nonzero degree-four covariance defect, while the true finite-displacement/secant correction begins at degree six. The degree-four defect diagnoses a hybrid child prescription, not failure of exact raw/NF finite transport.

### BIRTH-AUDIT-09 `[AUDIT]`
All registered residual contracts share the same documented cubic child under the two reference policies. Raw-versus-odd separation begins in the swap-even quartic \(F_4\); whether its leading \(Q_c\) consequence is physically discriminating depends on whether \(W\) and \(-W\) are distinct oriented states or identified by the event quotient.

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


### BIRTH-AUDIT-15 `[ALG]`
The full primitive-frame quartic \(F_4(W,\bar W)\) is reconstructed exactly from the sourced \(T^6\) and is even under \(W\mapsto-W\). The positive-real-ray coefficient is only one directional specialization.

### BIRTH-AUDIT-16 `[AUDIT]`
The earlier use of the Jacobi \(A\leftrightarrow B\) sign action as the isolated-dyad relabel was profile-mistyped. `RRF-NET-W-RAW` bookkeeping/Jacobi sign reversal and the `RRF-DYAD-W` involution \(S_h\) are distinct objects with no registered bridge. Any cross-profile parity conclusion is conditional on OPEN-B/E1.

### BIRTH-AUDIT-17 `[ALG / conditional completion]`
For residual-linear child maps with projector \(P(-s)=P(s)\), the raw/odd \(Q_c\) difference has an antipodally odd degree-seven cross term and an antipodally even degree-eight norm term. Event-domain orientation/quotient semantics therefore determine which term is an admissible discriminator.


### BIRTH-AUDIT-18 `[ALG]`
For any child functional differentiable in its residual argument,
\[
\Delta c(s)
=
\int_0^1
D_R\mathcal C\!\left(s,R_{\rm odd}(s)+uD(s)\right)[D(s)]\,du,
\qquad
D=R_{\rm raw}-R_{\rm odd}.
\]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)
A nonzero residual difference therefore does not by itself imply a nonzero child difference.

### BIRTH-AUDIT-19 `[ALG / class-specific]`
No family of residual-linear maps \(L_s:V\to V\) can, on **every** nonzero parent direction in a punctured neighborhood, both preserve the nonzero cubic Genesis target \(L_sE_3(s)=\kappa QJ_Qs\) and annihilate \(F_4(s)\). The obstruction is an alignment ray on which \(F_4(s)=\gamma E_3(s)\), \(\gamma\ne0\). This does not apply to nonlinear functionals or event domains excluding that ray.

### BIRTH-AUDIT-20 `[ALG / conditional completion]`
A same-point nonlinear amplitude-setting rule can make raw and odd child outputs exactly equal on a common small-amplitude sign sector while preserving the cubic target. It does so by discarding projected residual magnitude and imposing the child magnitude from \(Q\). This is an additional constitutive choice, not a source result.

### BIRTH-AUDIT-21 `[ALG / identity-conditioned]`
Fix nonzero scalar \(\kappa\). In the node-mediated Genesis/network branch, the cubic target is odd under the Jacobi \(s\mapsto-s\) action while the standard \(c\)-role is even. This is an exact leading-order obstruction **inside that branch**. Because Genesis inheritance from `RRF-DYAD-W` is not registered, carrying the obstruction back to the isolated-dyad physical relabel is bridge-conditional. The fact that \(S_h(W)=-W+O(W^2)\) means the cubic parity calculation is unchanged at linearized order if that bridge later identifies the actions.

### BIRTH-AUDIT-22 `[ALG / bridge guard]`
Under the phase-linear bridge ansatz
\[
b_m(e^{i\phi})=e^{i(m\phi+\vartheta_0)},
\qquad m\in\mathbb Z,
\]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)
the quarter-turn-to-half-turn condition \(m\equiv2\pmod4\) implies \(b_m(-u)=b_m(u)\). The phase map alone is therefore many-to-one and cannot be the invertible chart map required by `REP-EQUIV` without additional sheet data, a justified quotient, a local restriction, or a larger information-carrying bridge.


### BIRTH-AUDIT-23 `[SCOPE]`
The calibrated constant mixture of §15.2 cancels the raw/odd quartic difference only on the positive-real \(W\)-ray used to solve its two coefficients. It is not a phase-uniform delay mechanism; off that ray the quartic child difference generally reappears.

### BIRTH-AUDIT-24 `[ALG / bridge condition]`
For a phase-linear cross-branch bridge with \(m\equiv2\pmod4\), the phase component identifies antipodes. In the node-mediated oriented Genesis branch this loses the sign/orientation used by the cubic child. Calling that sign the **dyad pole-order datum** is conditional on the missing RRF-DYAD-W → network/Genesis bridge; the bridge requirement is therefore profile-typed, not an established physical pole-swap result.

### BIRTH-AUDIT-25 `[HEUR separation]`
A realized-data principle constrains **what may be read**, not **what may be discarded**. It excludes counterfactual/whole-field readers when those data are not realized at or before the event, but it does not by itself force raw/odd survival: the pointwise amplitude-setting rule is a counterexample. Any claim that the child must retain the residual distinction needs an additional constitutive-faithfulness premise.


### BIRTH-AUDIT-26 `[ALG / access typing]`
For fixed known \(T\), fixed residual definition and complete parent \(s\), the tuples
\[
s,\qquad (s,R(s)),\qquad (s,R(s),R(-s))
\]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)
carry the same independently variable parent datum: each enriched tuple is determined by \(s\), and projection recovers \(s\). Additional evaluation can still be forbidden by the allowed-operation contract. Computable value \(\ne\) independent datum.

### BIRTH-AUDIT-27 `[ALG / variable-input counterexample]`
If the residual field itself is independently variable, pointwise and two-point readouts need not have the same fibres. There exist two fields with the same cubic part and the same value at a realized \(s_0\), but different values at \(-s_0\), hence different odd-extracted outputs. Access semantics therefore depend on what is included in the complete variable input.

### BIRTH-AUDIT-28 `[AUDIT]`
Child-channel erasure is not automatically whole-event information loss. In a parent-retaining snapshot \((s,c)\), projection \((s,c)\mapsto s\) can preserve all parent information even when the child constitutive rule discards a residual magnitude already computable from \(s\). Independently variable field/history data require their own retention analysis.


### BIRTH-AUDIT-29 `[AUDIT / RRF lock]`
`RRF-DYAD-W`, `RRF-DYAD-NF`, and `RRF-NET-W-RAW` are distinct profiles. No closure, comparator, holonomy, relabel, or incidence law is imported across them without a registered arrow. Genesis inheritance fields and the DYAD-W → NET bridge remain unregistered.

### BIRTH-AUDIT-30 `[ALG / independent degree-4 check]`
With \(D_S(F)=F\circ S-S\circ F\),
\[
D_{-I}(F_W)=2F_4+O(6),\qquad D_{-I}(F_{\rm odd})=0,
\]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)
while
\[
D_{S_h}(F_W)=0\ \text{through degree }4,\qquad
D_{S_h}(F_{\rm odd})=-2F_4+O(5).
\]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)
Thus raw/odd covariance reverses when the action changes from naive \(-I\) to registered \(S_h\).

### BIRTH-AUDIT-31 `[OPEN / physical relabel]`
RRF OPEN-A remains upstream of a physical residual-covariance interpretation. The registered representation involution \(S_h\) is not yet identified with physical pole relabeling; neither is naive \(W\mapsto-W\).

### BIRTH-AUDIT-32 `[OWNER-PASS REQUIREMENT / noncanonical]`
A future Genesis v2.8.5 claim-status pass should add RRF OPEN-A and OPEN-B/E1 as dependencies at the GCL-06 residual-choice route. The present ledger does not enact that owner edit.

---

# 11. Eleven-field continuous source audit

The receiving-side source audit has now assessed all eleven original fields. “Missing” below means not supplied by the inspected formulation, not that no historical unpublished artifact ever existed.

| # | Field | Current continuous status | Next obligation |
|---:|---|---|---|
| 1 | Event/admissibility predicate | **MISSING COMPLETE PREDICATE** — fracture state and leading family named; no complete trigger/first-event rule | Specify predicate, timing, crossing/detection convention and ambient context |
| 2 | Retained-parent update \(s^+\) | **EXPLICITLY OPEN** — longitudinal retention unresolved | Declare retained-output map/readout and approximation order |
| 3 | Residual-to-child functional | **LEADING FAMILY ONLY** — cubic pieces and leading \(c_0\) supplied | Define complete functional of selected residual/event state |
| 4 | Physical \(\kappa\) | **REFERENCE POLICIES PRESENT; SELECTION OPEN** | Keep shear/recoil as reference policies; require independent selection criterion |
| 5 | Role identity / continuation | **SUPPLIED LABELS PARTIAL; NO EVENT DERIVATION; RRF PROFILE BRIDGE OPEN** | Separate supplied/inherited/event-generated identity from lineage; record OPEN-A and OPEN-B/E1 when interpreting relabeling across dyad/network profiles |
| 6 | Attachment / incidence | **TARGET TOPOLOGY PRESENT; FULL GLUING MISSING** — Triadic declares \(K_3\) | Specify endpoint/state realization and event-level incidence |
| 7 | Pre/post gauge/relabel actions | **PROFILE-SPECIFIC ACTIONS PRESENT; PHYSICAL IDENTIFICATION OPEN** — \(S_h\) in DYAD-W, \(-I\) in NF, bookkeeping \(\mathscr O_e\) in NET | State which action is physical (OPEN-A) and transport it through the event/profile bridge rather than substituting signs across profiles |
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
(rep: [UNREGISTERED-TDRG]; discrete profile not registered in RRF v0.6 §7)

whose entire local defect graph is the isolated \(K_{1,3}\) centred at \(A\).

Thus

\[
\boxed{
\Phi_\star:\;4\to5
}
\]
(rep: [UNREGISTERED-TDRG]; discrete profile not registered in RRF v0.6 §7)

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
(rep: [UNREGISTERED-TDRG]; discrete profile not registered in RRF v0.6 §7)

Old phases are retained through the event and leaf tokens are unchanged. \(E\) is a fresh label. The child copies the **pre-event** centre token; it is not advanced again during the same tick.

The output lies on a constrained image, including

\[
\theta_E^+-\theta_A^+=\frac N2,
\qquad
\delta_E^++\delta_A^+=0\pmod N.
\]
(rep: [UNREGISTERED-TDRG]; discrete profile not registered in RRF v0.6 §7)

## 12.3 Identity and attachment

Initial node identity is **SUPPLIED** by the indexed model. Old labels continue and a fresh child label is appended. Hence

\[
\text{generated from }A\ne\text{identical to }A.
\]
(rep: [UNREGISTERED-TDRG]; discrete profile not registered in RRF v0.6 §7)

Defect adjacency is reconstructed from node phases; it is an observable of the node state, not an independently glued permanent edge field.

For the stated isolated narrow-band \(K_{1,3}\) input, the newborn is defect-related to the centre and not to the three leaves, so the immediate local output defect graph is \(K_{1,4}\). This is instantaneous and local; later evolution or outside nodes can change the graph.

## 12.4 Gauge and marked recoverability

The declared gauge is common phase shift,

\[
g_a(\theta_i,\delta_i)
=
(\theta_i+a,\delta_i)\pmod N.
\]
(rep: [UNREGISTERED-TDRG]; discrete profile not registered in RRF v0.6 §7)

The local star event is covariant under this action. A common token shift is **not** silently added as another gauge action.

With centre \(A\), newborn \(E\), and event type known, delete \(E\) and recover

\[
\theta_i^-=\theta_i^+,
\qquad
\delta_A^-=-\delta_A^+=\delta_E^+,
\qquad
\delta_i^-=\delta_i^+\quad(i\ne A).
\]
(rep: [UNREGISTERED-TDRG]; discrete profile not registered in RRF v0.6 §7)

Thus the marked local event has a left inverse and is injective on the corresponding marked phase-gauge quotient. This does not establish recoverability from an unmarked final state, unknown simultaneous events, or an arbitrary history.

## 12.5 Concrete source example

For \(N=24,\;k=1\),

\[
\theta^-=(0,11,12,13),
\qquad
\delta^-=(2,1,5,7)
\]
(rep: [UNREGISTERED-TDRG]; discrete profile not registered in RRF v0.6 §7)

maps to

\[
\theta^+=(0,11,12,13,12),
\qquad
\delta^+=(22,1,5,7,2).
\]
(rep: [UNREGISTERED-TDRG]; discrete profile not registered in RRF v0.6 §7)

The child copies \(2\), not the updated centre token \(22\), and its phase is \(12\), not \(14\).

## 12.6 Algebraic update symmetries versus physical gauge

The source-declared comparison gauge remains the common phase shift. The local marked **update rule itself** has a broader algebraic covariance:

- phase affine dihedral actions \(\theta\mapsto \varepsilon\theta+a\), \(\varepsilon=\pm1\), commute with the half-turn child rule;
- token multiplication \(\delta\mapsto u\delta\) commutes with the update, and is invertible when \(u\in(\mathbb Z/N)^\times\);
- a token translation \(\delta\mapsto\delta+a\) commutes with the centre sign flip only when
  \[
  2a=0\pmod N.
  \]
(rep: [UNREGISTERED-TDRG]; discrete profile not registered in RRF v0.6 §7)
  Hence arbitrary token shifts are not a symmetry; for even \(N\), the special half-period shift is an algebraic exception.

These are symmetries of the scoped local update formula, not automatically physical gauges of the TDR-G model. The event-domain classifier, \(T_{\rm pre}\), \(T_{\rm post}\), observables and quotient must also be covariant. Therefore the physical gauge candidate is the **intersection** of the admitted event/update symmetries with those of the actual dynamics and observables.

## 12.7 A conditional phase-linear bridge constraint `[HEUR]`

The continuous leading child with fixed \(\kappa<0\) is a quarter-turn,

\[
\Delta\arg W=-\frac{\pi}{2},
\]
(rep: [UNREGISTERED-TDRG]; discrete profile not registered in RRF v0.6 §7)

whereas the TDR-G newborn phase is antipodal to the centre,

\[
\Delta\theta=\pi.
\]
(rep: [UNREGISTERED-TDRG]; discrete profile not registered in RRF v0.6 §7)

If a future circle-valued bridge is assumed to have the phase-linear form

\[
\theta=m\,\arg W+\theta_0\pmod{2\pi}
\]
(rep: [UNREGISTERED-TDRG]; discrete profile not registered in RRF v0.6 §7)

and is required to map the birth rotations directly, then

\[
-m\frac{\pi}{2}\equiv\pi\pmod{2\pi}
\]
(rep: [UNREGISTERED-TDRG]; discrete profile not registered in RRF v0.6 §7)

implies

\[
\boxed{m\equiv2\pmod4.}
\]
(rep: [UNREGISTERED-TDRG]; discrete profile not registered in RRF v0.6 §7)

This is only a necessary condition **under that bridge ansatz**. It neither identifies TDR-G phase with \(W\)-phase nor constructs the bridge. The parent-update correspondence is independently unresolved: the conditional continuous snapshot below retains \(s\), while the star event flips the centre token.


For a globally well-defined circle map write

\[
b_m(e^{i\phi})
=
e^{i(m\phi+\vartheta_0)},
\qquad
m\in\mathbb Z.
\]
(rep: [UNREGISTERED-TDRG]; discrete profile not registered in RRF v0.6 §7)

The integer condition comes from \(\phi\sim\phi+2\pi\). The required congruence \(m=4k+2\) is even, so

\[
\boxed{
b_m(-u)=b_m(u).
}
\]
(rep: [UNREGISTERED-TDRG]; discrete profile not registered in RRF v0.6 §7)

Hence this phase component is not globally invertible for \(|m|\ge2\). It cannot by itself be an \(H_{\rm pre}\) or \(H_{\rm post}\) of a `REP-EQUIV` claim.

Moreover, because the ordered continuous cubic birth distinguishes \(u\) from \(-u\) while every such even-degree phase map identifies them, the missing bridge information is not arbitrary:

\[
\boxed{
\text{an injective bridge must carry at least the lost antipodal/pole-order sheet datum outside the phase component.}
}
\]
(rep: [UNREGISTERED-TDRG]; discrete profile not registered in RRF v0.6 §7)

For the minimal \(m=\pm2\) cover this is a \(\mathbb Z_2\)-type sheet/orientation label. For \(|m|>2\), the covering has more sheets, so that orientation bit is necessary but may not be sufficient for full inversion.

The TDR-G source phase is an index in \(\mathbb Z_N\). Any comparison with a continuous circle phase must separately declare the radian embedding \(2\pi\theta/N\), the allowed discrete image, and any branch/sheet information. The congruence does not supply that bridge.

## 12.8 Cross-branch comparison status


The common schema now supports the question

> How does each event realize a new represented role, retain prior structure, constrain its output, and permit or prevent recovery?

But it does **not** identify the two events:

\[
\text{continuous }\Phi_{2\to3}
\quad\not\equiv_{\rm supplied}\quad
\text{literal modular }K_{1,3}\text{ birth}.
\]
(rep: [UNREGISTERED-TDRG]; discrete profile not registered in RRF v0.6 §7)

A direct representation-equivalence claim requires an additional grouping, embedding or coarse-graining contract plus aligned observables.

Therefore the present cross-branch verdict is

\[
\boxed{
\texttt{UNDECIDED-MISSING-BRIDGE}.
}
\]
(rep: [UNREGISTERED-TDRG]; discrete profile not registered in RRF v0.6 §7)

---
# 13. Conditional-completion programme

The broad source audit is complete enough to stop searching for a fully specified continuous event that the inspected owner texts do not contain.

A completion package must distinguish retained-state **update** from retained-state **readout**:

\[
R_{\rm ret}:\mathcal D_{\rm event}\to\mathcal S_{\rm ret},
\qquad
\Pi_{\rm ret}:\mathcal S_{\rm post}^{\rm adm}\to\mathcal S_{\rm ret},
\]
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

with

\[
\boxed{
\Pi_{\rm ret}\circ\Phi_R=R_{\rm ret}
}
\]
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

when the actual retained state is intentionally held fixed across residual choices.

Use the snapshot-level completion package

\[
\Xi_{\rm snap}
=
\bigl(
\mathcal D_{\rm frac},
R_{\rm ret},
\Pi_{\rm ret},
\mathcal C_{\rm child},
\mathcal A_{K_3},
\mathcal G_{\rm event},
\mathcal O_{\rm cmp}
\bigr),
\]
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

with every unsourced ingredient explicitly `[HYP/CHOICE]`.

“Same completion” means the same **typed physical operation**, not the same coordinate string. Raw and odd residuals already live in the same primitive \(W\)-frame. For an NF-computed input, the same primitive finite-displacement residual is

\[
R_{\rm NF\to W}(h(z))
=
h(z+E_{\rm NF}(z))-h(z)
=
E_{\rm raw}(h(z)).
\]
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

Feeding bare \(E_{\rm NF}(z)\) or \(Dh(z)E_{\rm NF}(z)\) to an otherwise raw child rule is a different hybrid prescription.

An event-snapshot comparison does not supply later dynamics. A whole birth-plus-evolution comparison requires an additional common

\[
T_{\rm post},
\]
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

its domain and time/reblocking correspondence.

---

# 14. First conditional common-completion snapshot test

This section records a **diagnostic construction**, not an extracted physical Genesis law.

## 14.1 Fixed choices

For a marked, sufficiently small nonzero parent \(s\), choose:

\[
R_{\rm ret}(s)=s,
\qquad
\Pi_{\rm ret}(s^+,c)=s^+,
\]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)

a child in the same primitive carrier \(V\) with the same \(B\), and fresh marked role \(C\).

Use the node-mediated \(K_3\) reference **difference realization**

\[
r_{AB}=s,
\qquad
r_{BC}=c-\frac{s}{2},
\qquad
r_{CA}=-c-\frac{s}{2},
\]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)

which satisfies

\[
r_{AB}+r_{BC}+r_{CA}=0
\]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)

**by construction**. This checks internal consistency of the chosen difference parameterization; it is not evidence that the physical birth event establishes that attachment.

This is a computational realization of supplied incidence, not an ontological claim of three independent substances.

For \(Q_s\ne0\), define

\[
P_\parallel(s)
=
\frac{s\,s^\top B}{Q_s},
\qquad
P_\perp(s)
=
I-P_\parallel(s).
\]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)

Define two **separate** all-order diagnostic extensions of the sourced cubic policies:

\[
\mathcal C_{\rm sh}(s,R)
=
P_\perp(s)R,
\]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)

\[
\mathcal C_{\rm re}(s,R)
=
J_QP_\parallel(s)R.
\]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)

The extension of these projectors to the complete residual is `[HYP/CHOICE]`.

For each fixed family \(\alpha\in\{{\rm sh},{\rm re}\}\),

\[
\Phi_R^\alpha(s)
=
\left(
s,
\mathcal C_\alpha(s,R(s))
\right).
\]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)

## 14.2 Raw-versus-odd difference and antipodal parity

Write

\[
R_o(w)=E_{\rm odd}(w),
\qquad
R_e(w)=E_{\rm raw}(w)-E_{\rm odd}(w).
\]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)

Then to the relevant orders,

\[
R_o(-w)=-R_o(w),
\qquad
R_e(-w)=R_e(w),
\qquad
R_e(w)=F_4(w)+O(|w|^6).
\]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)

Let the child rule be linear in the residual and even in the parent direction:

\[
\mathcal C_{-w}=\mathcal C_w.
\]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)

This includes both reference projector extensions of §14.1. Define

\[
c_o(w)=\mathcal C_w(R_o(w)),
\qquad
c_e(w)=\mathcal C_w(R_e(w)).
\]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)

Then

\[
c_o(-w)=-c_o(w),
\qquad
c_e(-w)=c_e(w).
\]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)

For the quadratic child norm,

\[
Q_c(c)=\langle c,c\rangle_B,
\]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)

one has exactly

\[
\boxed{
Q_{c,\rm raw}(w)-Q_{c,\rm raw}(-w)
=
4\,\operatorname{Re}\langle c_o(w),c_e(w)\rangle_B,
}
\]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)

and

\[
\boxed{
\frac{
Q_{c,\rm raw}(w)+Q_{c,\rm raw}(-w)
}{2}
-
Q_{c,\rm odd}(w)
=
\|c_e(w)\|_B^2.
}
\]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)

Since \(c_o=O(|w|^3)\) and \(c_e=O(|w|^4)\), degree seven and degree eight are the **first possible orders** for these general parity mechanisms. The displayed reference-ray coefficients below are nonzero and therefore realize those orders; other child functionals or directions can cancel them.

On \(w=\pm t\), \(t>0\):

| policy | \(\Delta Q_c(+t)\) | \(\Delta Q_c(-t)\) | antipodal average minus \(Q_{c,\rm odd}\) |
|---|---:|---:|---:|
| shear | \(+\frac{25}{12}t^7+O(t^8)\) | \(-\frac{25}{12}t^7+O(t^8)\) | \(\frac{625}{768}t^8+O(t^9)\) |
| recoil | \(+\frac5{48}t^7+O(t^8)\) | \(-\frac5{48}t^7+O(t^8)\) | \(\frac{25}{2304}t^8+O(t^9)\) |

Therefore

\[
\boxed{
\text{the degree-seven discriminator is admissible only for an oriented event domain that distinguishes }w\text{ from }-w.
}
\]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)

The antipodal average is a **sign-invariant scalar diagnostic**. It does not make the complete birth event descend to the simple swap quotient. Under the standard Jacobi \(c\)-even action, §15.6 obstructs that event descent already at cubic order. Physical use of the averaged scalar therefore requires a separately completed quotient/event/observable contract.

### 14.2.1 Angularly resolved quartic response

Put

\[
w=re^{i\theta},
\qquad
F_4(w,\bar w)=r^4 f_4(\theta).
\]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)

Define relative parallel/transverse components

\[
p(\theta)=\operatorname{Re}(e^{-i\theta}f_4(\theta)),
\qquad
q(\theta)=\operatorname{Im}(e^{-i\theta}f_4(\theta)).
\]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)

The exact reconstructed quartic gives

\[
\boxed{
p(\theta)
=
-\frac{17\sqrt3}{72}\sin\theta
+\frac{\sqrt3}{16}\sin3\theta
-\frac38\cos\theta
+\frac{13}{48}\cos3\theta,
}
\]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)

\[
\boxed{
q(\theta)
=
\frac1{24}\sin\theta
-\frac{19}{48}\sin3\theta
-\frac{49\sqrt3}{72}\cos\theta
+\frac{23\sqrt3}{144}\cos3\theta.
}
\]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)

Thus the quartic even-child contributions of the two chosen extensions are

\[
\boxed{
c_{e,\rm re}
=
i\,r^4e^{i\theta}p(\theta),
\qquad
c_{e,\rm sh}
=
i\,r^4e^{i\theta}q(\theta).
}
\]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)

At \(\theta=0\),

\[
p(0)=-\frac5{48},
\qquad
q(0)=-\frac{25\sqrt3}{48},
\]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)

so neither reference projector annihilates \(F_4\) in every direction.

More generally, a residual-linear child functional eliminates the raw/odd quartic difference for every admissible parent only if

\[
\boxed{
\mathcal C_w(F_4(w))=0
\quad\text{for every admissible }w.
}
\]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)

The full reconstructed \(F_4\), not a single ray, is therefore the correct input for the next functional-class audit.

## 14.3 Phase does not discriminate this oriented completion

On either fixed oriented ray, both projectors force the child into the \(B\)-transverse \(J_Qs\) direction. With their negative common cubic coefficients, raw and odd have the same child/parent phase

\[
-\frac{\pi}{2}
\]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)

on a sufficiently small nonzero interval, even though \(Q_c\) differs.

Thus

\[
\boxed{
\text{same child phase}\quad\not\Rightarrow\quad\text{same child output}.
}
\]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)

A phase-only observable misses this conditional raw/odd distinction.

## 14.4 NF control

To compare the **same primitive residual operation** using NF coordinates, use

\[
s=\mathcal L^{-1}h(z),
\]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)

and

\[
R_{\rm NF\to W}(z)
=
h(z+E_{\rm NF}(z))-h(z)
=
E_{\rm raw}(h(z)).
\]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)

With all other primitive operations fixed, this reproduces the raw snapshot input exactly. Using bare \(E_{\rm NF}\), tangent transport \(Dh\,E_{\rm NF}\), or a bare normalized observable instead defines another typed prescription.

## 14.5 Current verdict

This test proves only:

\[
\boxed{
\text{under two explicit common snapshot completions, the raw/odd quartic difference survives to }Q_c.
}
\]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)

It does **not** establish:

- that either completion is the physical birth law;
- that every admissible child functional distinguishes raw and odd;
- a global `PHYS-DISTINCT` verdict;
- any post-birth evolution difference;
- network representation equivalence or inequivalence.

The immediate next task is **identity-conditioned**:

1. keep the present ordered/oriented reference branch, where \(w\) and \(-w\) remain distinct;
2. separately define a hypothetical swap-gauged branch, including output action and attachment transport;
3. within each branch classify child functionals that annihilate or retain the full \(F_4(W,\bar W)\);
4. append one explicit common \(T_{\rm post}\) only after the event-level identity/gauge choice is fixed.

The two branches must not be mixed when assigning physical meaning to the odd projection.

---



# 15. Child-functional admissibility audit

This section varies only the explicitly conditional child functional while holding the v0.5 snapshot carrier, retention, marked roles, \(K_3\) difference realization and \(Q_c\) readout fixed. No fracture predicate or \(T_{\rm post}\) is introduced.

Let

\[
D(s)=R_{\rm raw}(s)-R_{\rm odd}(s).
\]
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

The exact return is analytic, with

\[
R_{\rm odd}=E_3+F_5+F_7+\cdots,
\qquad
D=F_4+F_6+F_8+\cdots.
\]
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

The documented cubic target remains

\[
C_3^\kappa(s)=\kappa QJ_Qs,
\qquad
\kappa\ne0.
\]
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

## 15.1 General survival identity

If \(\mathcal C(s,R)\) is \(C^1\) in \(R\) on a neighborhood of the segment joining \(R_{\rm odd}(s)\) and \(R_{\rm raw}(s)\) (or satisfies another explicit hypothesis sufficient for the fundamental theorem of calculus along that segment), then

\[
\boxed{
\Delta c(s)
=
\int_0^1
D_R\mathcal C
\!\left(
s,
R_{\rm odd}(s)+uD(s)
\right)
[D(s)]\,du.
}
\]
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

This is differentiation in the **residual argument with parent state fixed**. It is unrelated to the chart secant/tangent distinction of §3.4.

For a residual-linear family

\[
\mathcal C(s,R)=L_sR,
\]
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

\[
\Delta c=L_sD.
\]
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

If \(L_{tu}=L_u\) on a parent ray \(s=tu\),

\[
\Delta c(tu)
=
t^4L_uF_4(u)
+t^6L_uF_6(u)
+O(t^8).
\]
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

Thus quartic residual difference is merely the first **available input** difference. Its first output order is selected by \(\mathcal C_{\rm child}\).

## 15.2 Cubic-preserving constant mixture: one-ray delay, not erasure

Consider

\[
\mathcal C_{a,b}(s,R)
=
aP_\perp(s)R
+
bJ_QP_\parallel(s)R.
\]
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

Its cubic output is

\[
\mathcal C_{a,b}(s,E_3(s))
=
\left(-\tau a-\frac b2\right)QJ_Qs.
\]
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

On the **positive real \(W\)-ray only**, preserving a fixed nonzero \(\kappa\) and cancelling the quartic raw/odd difference gives

\[
-\tau a-\frac b2=\kappa,
\qquad
25\sqrt3\,a+5b=0,
\]
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

hence

\[
\boxed{
a_*=\frac{2\sqrt3\,\kappa}{11},
\qquad
b_*=-\frac{30\kappa}{11}.
}
\]
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

For the two negative reference values of \(\kappa\), \(a_*<0<b_*\); this is not a nonnegative mixture of the original reference policies.

Exact one-ray reconstruction through degree six gives

\[
F_6^W(t)
=
\frac{-1163+817i\sqrt3}{1440}t^6.
\]
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

Therefore

\[
\boxed{
c_{\rm raw}^W-c_{\rm odd}^W
=
\frac{829i\kappa}{330}t^6
+O(t^8),
}
\]
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

and

\[
\boxed{
Q_{c,\rm raw}-Q_{c,\rm odd}
=
\frac{829\kappa^2}{165}t^9
+O(t^{11}).
}
\]
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

So this child functional delays the first distinction **on that calibrated ray** without eliminating it.

For \(\kappa=1\), at \(\theta=\pi/6\) the quartic child difference is already

\[
\boxed{
\Delta c_4
=
-\frac{9\sqrt3}{44}
+
i\frac{27}{44},
}
\]
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

so the degree-four difference returns immediately away from the calibration ray.

The cancellation is not phase-uniform. Comparing \(W=1\) and \(W=i\), the quartic cancellation rows have determinant

\[
\boxed{
\frac{295}{576}\ne0.
}
\]
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

A constant mixture cancelling both rays would require \(a=b=0\), incompatible with nonzero cubic target.

## 15.3 All-direction residual-linear obstruction

In real primitive coordinates,

\[
F_{4,\rho}
=
-\frac{
25\eta^4-48\eta^3\rho+48\eta^2\rho^2-32\eta\rho^3+15\rho^4
}{24},
\]
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

\[
F_{4,\eta}
=
-\frac{
10\eta^4-20\eta^3\rho+36\eta^2\rho^2-20\eta\rho^3+25\rho^4
}{24}.
\]
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

Direct algebra gives

\[
\boxed{
\det[E_3(s),F_4(s)]
=
\frac{Q^2}{144}
\left(
55\rho^3
-14\eta\rho^2
-73\eta^2\rho
-55\eta^3
\right).
}
\]
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

At \(\rho=1\), the cubic factor is \(55\) at \(\eta=0\) and \(-87\) at \(\eta=1\). Hence a ray \(\eta=\xi\rho\) exists with \(0<\xi<1\) on which \(E_3\) and \(F_4\) are collinear. Numerically,

\[
\xi\approx0.6497374908
\]
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

for orientation only; the theorem uses the exact sign change and continuity.

Neither vector vanishes there. In particular,

\[
\det M=\frac{19}{12}\ne0,
\]
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

and

\[
-24F_{4,\eta}
=
10\eta^2(\eta-\rho)^2
+
26\rho^2\left(\eta-\frac{5\rho}{13}\right)^2
+
\frac{275}{13}\rho^4
>0
\]
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

for nonzero \(s\).

Therefore on that ray

\[
F_4(s)=\gamma(s)E_3(s),
\qquad
\gamma(s)\ne0.
\]
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

Any linear \(L_s\) preserving

\[
L_sE_3(s)
=
\kappa QJ_Qs
\ne0
\]
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

must also satisfy

\[
L_sF_4(s)
=
\gamma(s)\kappa QJ_Qs
\ne0.
\]
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

Hence:

\[
\boxed{
\text{No residual-linear child functional can preserve the nonzero cubic target and annihilate }F_4
\text{ on every nonzero parent direction.}
}
\]
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

This is class-specific. A physical event domain could exclude the alignment ray, and nonlinear functionals are not covered.

Where \(E_3\) and \(F_4\) are independent, a local linear annihilator exists:

\[
L_sR
=
C_3^\kappa(s)
\frac{\det[F_4(s),R]}{\det[F_4(s),E_3(s)]},
\]
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

but it is singular on the alignment locus.

## 15.4 Same-point nonlinear amplitude rule: exact erasure on a sign sector

Choose one reference projection

\[
V_s=P_\perp(s)
\quad\text{or}\quad
V_s=J_QP_\parallel(s),
\]
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

with its corresponding fixed negative reference \(\kappa\).

For \(V_sR\ne0\), define

\[
\boxed{
\mathcal C_{\rm amp}(s,R)
=
|\kappa|Q^{3/2}
\frac{V_sR}
{\sqrt{(V_sR)^\top B(V_sR)}}.
}
\]
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

Since the image of \(V_s\) is \(\operatorname{span}(J_Qs)\), write

\[
V_sR=\beta J_Qs.
\]
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

Then

\[
\mathcal C_{\rm amp}(s,R)
=
|\kappa|Q\,\operatorname{sgn}(\beta)\,J_Qs.
\]
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

For raw and odd residuals,

\[
\beta=\kappa Q+O(\|s\|^3).
\]
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

On a common sufficiently small sector where both projected coefficients retain the negative sign of the reference \(\kappa\),

\[
\boxed{
\mathcal C_{\rm amp}(s,R_{\rm raw}(s))
=
\mathcal C_{\rm amp}(s,R_{\rm odd}(s))
=
\kappa QJ_Qs.
}
\]
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

The equality is exact on that sector, not merely finite-order.

The cost is explicit at the **child channel**: the projected residual contributes direction/sign, while its magnitude is discarded and the child amplitude is imposed from \(Q\). The map is undefined where \(V_sR=0\). Physical admissibility is OPEN.

This child-channel discard is not automatically whole-event information loss. In the parent-retaining snapshot used here, \((s,c)\mapsto s\) is a left inverse for the retained parent. If the discarded residual magnitude is already a deterministic function of fixed known \(T\) and retained \(s\), the complete snapshot can still determine it. Independently variable residual/history data require a separate retention test.

## 15.5 Other exact erasure mechanisms and access semantics

A parent-only prescription

\[
\mathcal C(s,R)=\kappa QJ_Qs
\]
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

erases raw/odd differences trivially because it ignores the residual. Here **parent-only must mean complete oriented \(s\)** (or another readout carrying equivalent orientation information). A magnitude-only readout \(Q\) cannot determine the existing cubic target because

\[
Q(-s)=Q(s),
\qquad
C_3^\kappa(-s)=-C_3^\kappa(s).
\]
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

A two-point field-level rule

\[
\widetilde{\mathcal C}_V[R](s)
=
V_s\frac{R(s)-R(-s)}2
\]
(rep: [UNREGISTERED-GENESIS]; inheritance/profile bridge pending RRF v0.6 §7 / OPEN-B-E1)

also gives exact raw/odd equality by idempotence of odd projection.

The information meaning of that rule depends on the complete input class.

### Fixed known model

If \(T\), its parameters, the residual definition and the complete parent \(s\) are fixed/known, then

\[
a_0(s)=s,
\qquad
a_1(s)=(s,R(s)),
\qquad
a_2(s)=(s,R(s),R(-s))
\]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)

have the same independently variable parent datum. Each enriched tuple is computable from \(s\), and projecting it recovers \(s\).

Thus

\[
\boxed{
\text{another residual evaluation}
\ne
\text{another independent datum}.
}
\]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)

Nevertheless, \(R(-s)\) may require an additional **allowed counterfactual evaluation**. Independent-data content and permitted computation are different contract fields.

### Independently variable residual field

If the residual field itself belongs to the variable event/environment input, pointwise and two-point access can differ.

As an illustrative algebraic counterexample, fix

\[
a=\frac1{100},
\qquad
s_0=(a,0),
\]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)

and a nonzero fixed vector \(v\). Let

\[
R_0(s)=E_3(s),
\qquad
R_1(s)=E_3(s)+\rho^4(\rho-a)v.
\]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)

Then

\[
R_1(s_0)=R_0(s_0),
\]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)

but

\[
R_1(-s_0)-R_0(-s_0)
=
-2a^5v.
\]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)

Their odd-extracted values at \(s_0\) differ by

\[
\boxed{a^5v}.
\]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)

The example does not assert a new RTG residual candidate. It shows that the fibres of the pointwise and two-point readouts differ when the field itself is allowed to vary independently.

These constructions cannot be compared physically until \(\mathcal X_{\rm full}\), \(\mathcal M_{\rm fixed}\), the permitted readout \(a\), and the allowed-operation set \(\Omega_{\rm allow}\) are fixed.

## 15.6 Interaction with the identity branch: network/Jacobi cubic obstruction

This subsection is explicitly **not** a statement about the isolated-dyad \(S_h\) action.

In the node-mediated Jacobi branch,

\[
s\mapsto-s,\qquad c\mapsto c.
\]
(rep: RRF-NET-W-RAW; Jacobi/node-label action)

Suppose this network/Jacobi action is promoted to the event quotient and the child retains the standard swap-even meaning.

Fix a nonzero scalar \(\kappa\) unchanged by that action. Assume the local event domain contains nonzero antipodal pairs approaching the origin along some fixed direction \(u\ne0\), and that

\[
c(s)=C_3^\kappa(s)+r(s),
\qquad
C_3^\kappa(s)=\kappa Q(s)J_Qs,
\qquad
r(s)=o(\|s\|^3).
\]
(rep: [UNREGISTERED-GENESIS]; node-mediated birth branch)

Whole-event covariance under this **network/Jacobi** quotient would require

\[
c(-s)=c(s).
\]
(rep: RRF-NET-W-RAW; proposed quotient condition)

But

\[
\frac{c(-tu)-c(tu)}{t^3}
\longrightarrow
-2\kappa Q(u)J_Qu
\ne0.
\]
(rep: [UNREGISTERED-GENESIS]; leading node-mediated asymptotic)

At cubic order,

\[
\boxed{
\|C_3^\kappa(-s)-C_3^\kappa(s)\|_B^2
=
4\kappa^2Q(s)^3
>0
\quad(s\ne0).
}
\]
(rep: [UNREGISTERED-GENESIS]; exact cubic identity)

Thus the standard cubic Genesis child cannot descend to that simple **network/Jacobi** quotient under the stated hypotheses.

This does not prove incompatibility with the registered dyad involution \(S_h\), because the bridge from `RRF-DYAD-W` to the Genesis/network child role is OPEN. Since

\[
S_h(W)=-W+O(|W|^2),
\]
(rep: RRF-DYAD-W; local linearisation)

the cubic parity obstruction would survive at leading order **if** a future bridge transports the linearized \(S_h\) action to the standard Jacobi sign action. That statement is bridge-conditional.

The existing cubic-preserving candidate functionals therefore belong naturally to the oriented/node-mediated Genesis branch under its current role action. This is not a theorem that every possible \(S_h\)-covariant or swap-gauged Genesis completion is impossible.

## 15.7 Result matrix

| Conditional child functional | Access class | Cubic target | Raw/odd outcome | Main added choice / restriction |
|---|---|---|---|---|
| Full shear/recoil projections | pointwise \(R(s)\) | retained | child degree 4; \(Q_c\) degree 7 on oriented ray | extend cubic projector to full residual |
| Calibrated linear mixture | pointwise \(R(s)\) | retained | **positive-real ray only:** child degree 6; \(Q_c\) degree 9; quartic difference returns off-axis | negative weight for reference \(\kappa<0\); not phase-uniform |
| Alignment-aware linear map | pointwise \(R(s)\) | retained | quartic killed on nonsingular angular patch | excludes \(\det[E_3,F_4]=0\) |
| Fixed-amplitude projected-direction map | pointwise \(R(s)\) | retained | exact child equality on common sign sector | discards residual magnitude; excludes zero projection |
| Parent-only rule | parent only | retained by definition | exact equality | residual ignored |
| Two-point odd functional | \(R(s),R(-s)\) or residual field | retained | exact equality | counterfactual/field access |
| Simple swap-gauged standard \(c\) role | quotient requirement | **incompatible when \(\kappa\ne0\)** | — | cubic parity obstruction |

---

# 16. Next research decision — complete input, readout, operations, constitutive law

The next stage remains model-level, but the access question is now precise enough to test without selecting the physical answer.

## 16.1 Four objects must be declared separately

For each candidate event family, specify:

1. **Complete variable input**
   \[
   x\in\mathcal X_{\rm full},
   \]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)
   including any independently variable field/environment, law parameters, branch identifiers or retained history.

2. **Fixed known model structure**
   \[
   \mathcal M_{\rm fixed},
   \]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)
   such as a declared \(T\), residual definition and constants that are not independently varying in the comparison.

3. **Permitted readout**
   \[
   a(x)\in\mathcal Y_{\rm read}.
   \]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)

4. **Allowed operations**
   \[
   \Omega_{\rm allow},
   \]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)
   including whether the rule may evaluate the known model at counterfactual states, normalize magnitudes, reconstruct hidden variables, consult history, or query a field away from the realized point.

At the set-map level, a child law depends only on the declared readout iff

\[
\boxed{
a(x)=a(y)
\Longrightarrow
\mathcal C(x)=\mathcal C(y).
}
\]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)

Equivalently, \(\mathcal C=\widetilde{\mathcal C}\circ a\). This is a fibre/determinacy condition. Regularity, causality, locality and permitted computation remain separate.

## 16.2 Candidate realized-data principle `[HEUR]`

One possible restriction is:

> A birth functional may directly read only data realized at the event or causally retained from the declared pre-event history.

This is a restriction on allowed readout/operations, not a statement about independent-state dimension.

For a fixed known \(T\) and complete oriented \(s\), \(R(-s)\) is mathematically determined by \(s\), so evaluating it adds no independent datum. The candidate principle could still forbid that counterfactual evaluation as a local physical operation.

If the residual field itself varies independently, the conclusion changes and the full field/environment must be included in \(\mathcal X_{\rm full}\).

No realized-data principle is adopted here.

## 16.3 Candidate residual-faithfulness principle `[HEUR]`

A separate possible constitutive rule is:

> If a residual channel \(V_sR\) is declared to source a child amplitude, the child constitutive law must respond nontrivially to that declared channel unless an explicit saturation, normalization, quotient or coarse-graining rule is part of the model.

This is **channel faithfulness**, not automatically a whole-event no-erasure law.

It may exclude a fixed-amplitude normalization as a faithful residual-amplitude law, while the complete parent-retaining event can still preserve enough information to reconstruct the discarded channel when the model is fixed.

No residual-faithfulness principle is adopted here.

## 16.4 Parent-only is not the same as \(Q\)-only

If the readout is complete oriented \(s\), the parent-only rule can reproduce the existing cubic target.

If the readout is only

\[
Q(s),
\]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)

then it cannot determine

\[
C_3^\kappa(s)=\kappa QJ_Qs
\]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)

because

\[
Q(-s)=Q(s)
\]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)

while the target changes sign. Therefore the orientation required by the existing cubic target must reside somewhere in the complete readable contract.

## 16.5 Alignment-ray exclusion is not a free repair

The residual-linear obstruction uses an entire ray

\[
\eta=\xi\rho,
\qquad
\xi\approx0.6497374908,
\]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)

through the origin. Excluding that ray can evade the universal quantifier only if the exclusion follows from an independently stated event predicate, accessible sector, symmetry condition or other physical/model rule.

It may not be introduced merely to rescue a preferred functional.

## 16.6 Bridge orientation requirement

The phase-linear bridge condition and the cubic swap obstruction remain:

\[
C_3^\kappa(-s)=-C_3^\kappa(s),
\qquad
b_m(-u)=b_m(u)
\quad(m\equiv2\!\!\!\pmod4).
\]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)

Thus the phase readout alone loses a pole-order distinction used by the ordered continuous birth. An injective bridge must carry that distinction elsewhere, justify a quotient that removes it physically, or abandon the phase-linear ansatz.

For \(m=\pm2\), a \(\mathbb Z_2\) sheet/orientation variable is the minimal phase-covering repair. For larger even degree, more sheet information may be needed.

## 16.7 Conditional \(T_{\rm post}\) work need not wait for a final physical access choice

It is not necessary to settle the uniquely physical access class before all further calculations.

One may choose a **declared conditional family**

\[
(\mathcal X_{\rm full},
\mathcal M_{\rm fixed},
a,
\Omega_{\rm allow},
\mathcal C_{\rm child})
\]
(rep: [ABSTRACT]; carrier-neutral contract or audit statement)

and then attach the same explicitly scoped \(T_{\rm post}\), retention, quotient and observables to raw/odd/NF variants where well typed.

The resulting evolution comparison remains conditional on that access/constitutive package; it is not promoted to the physical Genesis law.

## 16.8 Work sequence

1. retain the node-mediated oriented Genesis branch as the computational baseline, not a statement about the `RRF-DYAD-W` physical relabel;
2. instantiate a small number of explicit access/readout families using the fibre test;
3. keep constitutive faithfulness as a separate axis;
4. do not infer independent information merely from additional computable residual evaluations;
5. state event-domain exclusions independently;
6. attach a common conditional \(T_{\rm post}\) to one fixed family and test whether snapshot distinctions persist, disappear or become unreadable.

---


# 17. Synchronization and future owner-pass requirements

## 17.1 Genesis owner

Genesis remains `RTG_GENESIS_GEOMETRY_DSN_v2.8.4`; no successor is adopted here.

For a future v2.8.5 claim-status pass, the GCL-06 route should state explicitly:

- raw/odd/NF residual selection remains OPEN;
- covariance interpretation depends on RRF OPEN-A;
- any use of Jacobi/network sign reversal as the dyad relabel requires the OPEN-B/E1 bridge;
- `E_odd` is a naive-\(-I\) parity projection in `RRF-DYAD-W`, not automatically the relabel-covariant physical residual.

This is a required **claim-status dependency patch**, not a selection of the raw residual.

## 17.2 Recognition

The inspected current owner is `RTG_RELATIONAL_RECOGNITION_DSN_v0.3.4`. R8 and R9 are theorem-grade closures. The current Genesis birth-contract study does not import those theorems into the event law.

Maintenance only:

- RECOG v0.3.4 still carries stale companion pointers to NUMGEN v1.15 and OFN v0.7 in its header;
- Programme Overview v1.2 still selects RECOG v0.3.

These are synchronization items, not Genesis scientific dependencies.

## 17.3 Number Genesis

The inspected `RTG_NUMBER_GENESIS_DSN_v1.20.2` records its own scientific-sync corrections and says it is superseded by v1.20.3 with identical scientific state and methodology-only migration. v1.20.3 is not present in the project.

No new Number-Genesis result is imported into GUP-08/09 from this maintenance difference.

---

**Draft boundary:** this document changes no owner source, does not adopt a birth residual, fracture predicate, all-order child functional, physical gauge, or post-birth dynamics; does not identify the TDR-G star with \(\Phi_{2\to3}\); and does not turn the PRR dyad-first interpretation into an established Genesis ontology.
