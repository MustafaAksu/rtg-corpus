# RRF response to OFN coincident-node disposition — v0.2

**Date:** 14 October 2026  
**Class:** Noncanonical RRF owner-side review / proposed interface wording; not an amendment of adopted RRF v0.7 or OFN v0.9.  
**Status:** ACCEPT SCOPED. All scientific/physical owner decisions remain separate.  
**Sources inspected in this turn:** `Pasted text.txt` (OFN handoff message); `OFN_RESPONSE_TO_RRF_COINCIDENCE_v0_1.md` (full 217-line response); `RTG_ONTOLOGICAL_FOUNDATIONS_v0_9.md` (relevant adopted definitions, OPENs and RF-O09-03); `RTG_RRF_COINCIDENCE_ADMISSIBILITY_REVIEW_v0_1.md` (previous RRF review). The adopted RRF v0.7 Markdown itself is not mounted in this turn; previously cited policy from it is source-reported, not freshly checked against its exact bytes.

## 1. Accepted correction: the fixed-set implication requires no new ontology axiom

[THM] [scope: deterministic complete-state exchange; standard fixed-set lemma]

For a declared complete configuration space `X`, an admitted exchange involution `sigma` and deterministic update `F` on an invariant domain, if `F sigma = sigma F`, then

\[
 F(\operatorname{Fix}\sigma)\subseteq\operatorname{Fix}\sigma.
\]

For `sigma X=X`, `sigma F(X)=F(sigma X)=F(X)`. Invertibility, a metric, conservation or a primordial coincidence postulate is not needed. This is a mathematical implication conditional on the **same fixed-model exchange action** being a symmetry of the complete update. Permutation covariance of a parameterized family is weaker than symmetry of any fixed member; structural data must transform consistently and be fixed for a fixed-point argument.

[OPEN] Equality of intrinsic node quantities, zero edge difference, full exchange-fixed configuration and actual node merging are **four distinct interpretations**. The theorem governs complete exchange-fixed configurations. A merge/deletion needs a separate lower-cardinality compatibility map. OFN already owns `RTG-OFN-DEF-PRESENTATION-COVARIANCE` and `RTG-OFN-DEF-STATE-COMPLETENESS`; this response does not amend them.

## 2. Exact obstruction and its physical scope

[ALG] [scope: named conditional projected K3 model]

\[
 \mathcal C=\{(a,b,c)\in(\mathbb R^2)^3:a+b+c=0\},\quad
 \mathcal N=P_{\mathcal C}T^{\times3}|_{\mathcal C},\quad
 F_6=\mathcal N^6.
\]

Projection is reapplied after **every primitive step**. Exchange `B<->C` acts on ordered edges `(AB,BC,CA)` by

\[
 R(a,b,c)=(-c,-b,-a),\qquad
 \operatorname{Fix}(R)|_{\mathcal C}=\mathcal D_{BC}=\{(a,0,-a)\},
 \quad P_{\mathcal C}R=RP_{\mathcal C}.
\]

On `a=(rho,eta)`, primitive coincidence defect:

\[
 b^{(1)}=\left(0,-\tfrac23(\cosh\rho-1)\right),
\]

nonzero for `rho!=0`. Six-step defect:

\[
 b^{(6)}=\frac1{36}\binom{3\rho^4+\eta^4}{\rho^4+12\rho^3\eta-12\rho^2\eta^2+12\rho\eta^3-2\eta^4}
 +O(\|a\|^5).
\]

The degree-2 and degree-3 homogeneous contributions vanish. Moreover

\[
 \frac{3\rho^4+\eta^4}{36}-\frac{(\rho^2+\eta^2)^2}{48}
 =\frac{(3\rho^2-\eta^2)^2}{144}\ge0.
\]

Analyticity implies a sufficiently small punctured neighborhood where the **first component** of `b^(6)` is positive. No explicit certified numeric radius is imported. The named coincidence embedding `iota(a)=(a,0,-a)` is therefore noninvariant for `N` and `N^6`, and cannot be an invariant reduction on a full neighborhood. This does not decide all candidate embeddings or physical triads.

**Conditional exclusion:** If a proposed complete node-mediated model has a genuinely `sigma`-fixed physical state mapped to one of these witnessed configurations and supplies an encoding `E` satisfying `E sigma=R E` and `E F_phys=K E`, with `F_phys sigma=sigma F_phys` for the chosen physical clock `K=N` or `K=N^6`, then the three identities are inconsistent with the observed defect. No assertion about realizability of *every* point in `D_BC` is required. Conversely, `b=0` alone does not establish a `sigma`-fixed full state.

## 3. Mandatory correction to earlier RRF table: passive transport is not a model escape

[ALG] Under an invertible chart change `H`, transport **the map, coincidence set and exchange action**:

\[
 \widehat K=H^{-1}KH,\qquad \widehat D=H^{-1}D,\qquad
 \widehat R=H^{-1}RH.
\]

Then

\[
 \widehat K(\widehat D)\subseteq\widehat D
 \iff K(D)\subseteq D.
\]

Thus any correctly transported passive chart **inherits** this obstruction. It is wrong to list it alongside entirely new carriers, modified closure, changed model laws or untested strobes as simply “not tested.” Retaining a freshly imposed linear coincidence equation after a nonlinear chart change defines a **different identity condition**, not passive transport.

| Candidate change | Disposition |
|---|---|
| Same model, invertible passive transport of map / action / fixed set | Invariance failure persists exactly |
| Redefined physical carrier, update, action or coincidence set | Not settled by this counterexample |
| Projection once per block rather than after each primitive step | Different map, not settled |
| Strobe other than `N` or `N^6` | Not settled |
| Different invariant embedding or extra physical state fields | Not settled without an explicit contract |

## 4. Replacement text proposed for `RRF-CND-01`

[HEUR] [scope: proposed interface/admissibility text; not adopted RRF theorem]

> For any deterministic node-mediated candidate, specify the exchange action on the **complete** relational configuration, including incidence, pole/role identification, connection, fixed structural parameters, history and other transition inputs. If an admitted complete configuration is fixed by that exchange and the physical clock map is equivariant under the same fixed-model action, its exchange-fixed status is preserved. A carrier-level coincidence stratum tests that consequence only with an explicit encoding intertwining the full-state action and evolution. Equality of one coordinate/comparator alone does not establish full-state symmetry, and a subsequent merge/deletion requires an additional quotient and dynamics contract. This is not a new universal primordial coincidence axiom.

## 5. Three owner questions, now concrete

| Contract item | Required owner declaration | Current decision |
|---|---|---|
| **Identity/action** | Complete `X`, `sigma_BC`, fixed-model symmetry, actual exchange-fixed states; distinguish exchange from merge | OPEN-B / OFN 3B/3C |
| **Carrier** | `E:X->C`, `R`, `E sigma=R E`; whether `b=0` encodes full fixed-state identity or a weaker observable equality | OPEN-B then E1 |
| **Clock/model** | `F_phys`, declared clock `K`, `E F_phys=K E`, and exact projection cadence | No selected physical projected K3 law |

[OPEN] No new normalizer, B6 bound, alternative-carrier search or simulation is necessary to establish this particular obstruction. A different model must first be specified. The RRF work is to get the **identity/action, carrier and clock contract** from the relevant owner and to route the conditional failure, not re-own the polynomial theorem. Relevant OFN targets: `RTG-OFN-OPEN-PRIMACY-3B`, `RTG-OFN-OPEN-PRIMACY-3C`, feedback `RF-O09-03`. Existing RRF OPEN-B -> E1 -> E2 remains OPEN.

## 6. Review and evidence boundary

- The OFN response reports executing both supplied ER2B scripts unchanged, rebuilding the quartic restriction in a new SymPy implementation, and passing 38 grouped checks. **Those are OFN's recorded executions**, not new checks run in this turn.
- `verify_restricted.py` prints rather than asserts the quartic component; the separately reported OFN audit supplies the coefficient assertions. No higher-order B6 bound, different closure family or physical selected law is thereby proved.
- The complete owner `RTG_ONTOLOGICAL_FOUNDATIONS_v0_9.md` confirms its covariance/completeness definitions, the two target OPENs and RF-O09-03 remain in the current owner. Its adoption predates the current response, which is noncanonical.
- The particular *conditional* ER2B model must be pinned to its technical owner's evidence before an adopted scientific result import. No official status, adoption or owner custody is changed here.

## 7. Disposition and next work

**RRF disposition: ACCEPT SCOPED; replace the ambiguous earlier CND-01 proposal with the full-configuration version above as a proposed, not yet adopted, interface contract.** Treat passive recharting as an **invariance-preserving transformation**, not a possible escape. Require the three owner declarations before proposing physical exclusion.

**Technical task next:** owner-facing one-page `Identity–Action / Carrier–Encoding / Clock–Model` contract for the particular projected K3 candidate. Until then, do not infer that `b=0` is physical merging or identity, and do not run another jet/simulation simply to repeat an already established conditional obstruction.
