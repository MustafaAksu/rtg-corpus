# RRF — coincident-node admissibility review v0.1

**Date:** 14 October 2026  
**Status:** discussion-level / proposed interface decision; **not** a modification or adoption of RRF v0.7, OFN or Genesis owner documents.  
**Source:** `ER2B_COINCIDENCE_SIXSTEP_AUDIT_v0_1.zip`, `RTG_ER2B_CONSOLIDATED_STUDY_v0_2.md`, OFN v0.8. This review does not select the physical K3 carrier, coupling or clock.

## [ALG] Precisely tested model

With real two-component edge variables `a=r_AB`, `b=r_BC`, `c=-a-b=r_CA`, set

\[
 \mathcal C=\{(a,b,c):a+b+c=0\},\qquad
 \mathcal N=P_{\mathcal C}T^{\times3}|_{\mathcal C},\qquad
 F_6=\mathcal N^6.
\]

The projection is reapplied **after each** primitive step. It is part of this conditional model; no physical healing or selected birth operator is inferred. The coincident-node subspace being tested is `B=C`, hence `b=0`, `c=-a`. Its preservation criterion is

\[
 \mathcal N(\mathcal D_{BC})\subseteq\mathcal D_{BC},\qquad
 \text{or for a six-block clock}\quad F_6(\mathcal D_{BC})\subseteq\mathcal D_{BC},
 \quad\mathcal D_{BC}=\{(a,0,-a)\}.
\]

For `a=(rho,eta)`, the primitive first-step value is exactly

\[
 b^{(1)}= -\frac{T(a)+T(-a)}{3}
 =\begin{pmatrix}0\\-\frac23(\cosh\rho-1)\end{pmatrix}
 =\begin{pmatrix}0\\-\frac13\rho^2+O(\rho^4)\end{pmatrix}.
\]

Thus primitive-step coincidence preservation fails (already quadratic as a polynomial, for rho ≠ 0). For the six-step strobe, a separate exact calculation gives

\[
 \boxed{b^{(6)}=\frac1{36}
 \begin{pmatrix}
  3\rho^4+\eta^4\\
  \rho^4+12\rho^3\eta-12\rho^2\eta^2+12\rho\eta^3-2\eta^4
 \end{pmatrix}+O(\|a\|^5).}
\]

The degree-two and degree-three homogeneous parts of `b^(6)` vanish. The first component is positive for all sufficiently small nonzero real `a`, since `(3 rho^4+eta^4)/36 >= (rho²+eta²)²/48`. Analyticity supplies a uniform local remainder, so the six-step collision manifold is not invariant on any punctured neighborhood of the origin.

### Reproduction scope

- The uploaded ZIP passed integrity check and contains `check_iterate_family.py` and `verify_restricted.py` together.
- Running `check_iterate_family.py` in a normal extraction with its expected `../evidence` directory passes its asserted finite-clock tests, including zero quadratic six-step jet.
- Running `verify_restricted.py` prints exactly the expected degree-2/3 zeros and two quartic components. **It prints rather than asserts the quartic coefficient equality**, so its exit 0 is not by itself a coefficient-level acceptance gate.
- A separate fresh **SymPy two-variable implementation** of the projected map, truncated to degree four after every primitive step, ran for six steps and asserted both full quartic polynomial equalities exactly. PASS. This review did not rerun the older independent owner's original source script.

## [HEUR] RRF admissibility classification

**Proposed contract: `RRF-CND-01 — Node-coincidence preservation`** (not an adopted RID). If a candidate realization declares `B=C` to mean equality of the *complete physical node state*, and assigns both nodes identical deterministic, permutation-equivariant local laws, their equality must remain invariant under the admitted physical clock. If it is merely equality of a selected coordinate/observable while other unrepresented node data differ, the preservation requirement does not automatically follow.

| Candidate model contract | Consequence of the exact witness |
|---|---|
| Complete-node identification `B=C`, node-indistinguishability and primitive update `N` | **Excluded** for this named projected K3 map: quadratic violation |
| Same complete-node identification, admitted six-step update `F6` only | **Excluded** for this named projected K3 map: quartic violation |
| Primitive dyad/edge model where `b=0` is not stipulated to be a physical node-identity stratum | **No exclusion** from this criterion |
| A model with additional node labels, roles, or histories for which `b=0` is not equality of complete node state | **No exclusion** without specifying the expanded state and identification semantics |
| A different carrier / redefined closure / transported passive chart / different strobe | **Not tested** by this polynomial |

This is **conditional model exclusion**, not a derivation that node-primitive ontology is false, nor selection of a physical dyad-primitive ontology. `OPEN-B/E1` must determine the carrier, attachment/identification semantics and physical clock before declaring this acceptance predicate mandatory.

## [OPEN] Decision requested of RRF and OFN

1. Is equality of **full node state** a physical identity/indistinguishability stratum in the candidate realization? If yes, is it required to persist under a deterministic node-equivariant evolution?
2. Is `B=C` correctly represented by `r_BC=0` in the declared carrier, or is `r_BC=0` merely an observable-level coincidence?
3. Which map and strobe are being admitted: primitive `N`, six-step `F6`, or neither? What is its model source and physical status?
4. Are pole identification, orientation, incidence and all non-edge node variables transported under the proposed equality relation?

Until these are answered: **retain the exact quartic result as a conditional obstruction and freeze extra jet optimization**. No B6 extension or alternative-carrier sweep is required merely to establish this obstruction. If later asked to compare alternative physical carriers, register those alternatives and their closure operations before running them.

## Interface notice for the registry

The existing RRF **provisional raw-edge safety lock** remains in force: the `P_C` projection / linear edge closure of this conditional model is neither a selected physical birth mechanism nor a theorem about every RRF network realization. The source archive should be recorded with its separate two-method verification and the packaging/acceptance-gate caveat. No owner DSN or adopted RRF status is changed by this note.
