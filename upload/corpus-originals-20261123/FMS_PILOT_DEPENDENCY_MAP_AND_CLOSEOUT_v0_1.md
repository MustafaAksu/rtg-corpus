# RTG Foundations & Model Selection — Pilot Dependency Map / Closeout v0.1

**Status:** Noncanonical audit finding, proposed pilot closeout; not an owner decision, DSN replacement, or selection of physical geometry. **Date:** 2026-10-12. **Evidence:** OFN v0.8, Programme Overview v1.2, RRF v0.7, NUMGEN v1.20.7, ER-2B v0.2 research and earlier FMS-01/02/06 review record. Source RID spelling is pinned below.

## 1. Principal finding: carrier choice precedes additive holonomy

In a specified additive edge carrier \((V,+)\), the cycle observable is \(h_+=\sum_e\epsilon_e r_e\in V\). Thus the expression and the flat condition \(h_+=0\) are typed **relative to the chosen operation and orientation**. For the ER-2B oriented triangle, \(V=\mathbb R^2\) and \(h_+\) has **two real components**. \(\Omega_G\) (oriented area) is a different observable and may be nonzero when \(h_+=0\).

For a nonlinear, invertible local rechart \(r=H(z)\), *passively transported* closure is \(\sum_eH(z_e)=0\), equivalently \(z_1\oplus_H\cdots\oplus_H z_n=0_H\) for \(x\oplus_Hy=H^{-1}(H(x)+H(y))\). This retains the original flat/holonomic classification, because the transported holonomy is \(H^{-1}(\sum_e H(z_e))\), or equivalently its old-carrier image \(\sum H(z_e)\). Conversely, **re-imposing native addition** \(\sum z_e=0\) selects a *different model/additive law*. The original-normalizer example \((z_1,z_2,z_3)=(t,t,-2t)\) has \(\sum z_e=0\) but \(\sum H(z_e)=-(9+3i\sqrt3)t^2/4+O(t^3)\). This is a **comparison of two additive-carrier contracts**, not a passive coordinate transformation turning the same physical state from flat to holonomic.

**Consequences:** (i) ER-2B results belong to the raw \((\rho,\eta)\)-additively-flat K3 sector; (ii) any proposed holonomy-to-curvature dictionary must name the carrier, orientation, admissible rechartings, and transport of its operation; (iii) NG-7A gauge, orientation and cycle-basis invariance is **within a fixed typed carrier** and does not itself establish invariance under arbitrary nonlinear replacement of addition.

## 2. Finite model-class matrix (not an exhaustive ontology theorem)

| Model class | Additive cycle result | Additive carrier status | Scope / physical gap |
|---|---|---|---|
| Pure node differences \(r_{ij}=u_j-u_i\) | \(h=0\) theorem | Canonical **relative to an already selected affine node carrier** | Cannot supply a *required nonzero additive edge holonomy* without extra content; physical curvature need not require this particular holonomy |
| Node-first plus connection | Nonzero \(h\) possible | Node-difference part follows selected node carrier; connection's value space and operation separately typed | Connection source/update and curvature dictionary OPEN |
| Independent raw edge/dyad | Nonzero \(h\) possible | Operation/carrier is a model selection | ER-2B C19 gives a formal six-real-parameter **quadratic-chart** freedom for the specific projected-family comparison; does not certify physical admissibility |
| ER-2B projected K3 | \(h=0\) by \(P_{\mathcal C}\) every primitive step | Raw \((\rho,\eta)\) additive closure **postulated** | \(\chi,\Omega_G\), quartic norm response and C20 sign thresholds are phenomena *inside that sector*, not nonintegrable geometry |

**Conditional exclusion:** only **if** a selected physical curvature dictionary demands nonzero \(h\) in a particular typed additive carrier, the pure node-difference-only model fails that necessary condition. This does not exclude general node-first plus connection models and does not establish that physical curvature requires \(h\ne0\).

## 3. OPEN dependencies and exact source identifiers

| Source decision (open) | What it controls | Depends on / feeds | Scope / evidence |
|---|---|---|---|
| **RRF OPEN-B → OPEN-E1 → OPEN-E2** (RRF v0.7 §6; these are local OPEN labels, not invented owner RIDs) | Physical identity of node/pole role → canonical network state → joint constrained normal form | Feeds admissible additive carrier and geometry sources | RRF §2.5 `RRF-NET-W-RAW` prohibits silent identification of \(W_e^{net}\) with isolated-dyad \(W\). ER-2B C15/C19/C20 quantifies the consequence of changing the carrier. |
| **`RTG-OFN-OPEN-PRIMACY`** (OFN v0.8 §9 OPEN-OFN-3) | Node-first, dyad-first, or network-first physical primitive | Constraint from FRUSTRATION and RRF OPEN-B, not settled by either | Genesis Jacobi incidence is representation-only and ER-2B linear closure is a postulate. |
| **`RTG-OFN-OPEN-FRUSTRATION`** (OFN §9) | Native physical source of nonintegrable content | Needs source and a typed geometry dictionary; feeds `RTG-OPEN-REGGE-BRIDGE` | Pure node-potential differences give the established flat/null case. Source not selected. |
| **`RTG-OFN-OPEN-HOLONOMY-RANK-DIAGNOSTIC`** (OFN §9) | Typed operator/content distinction by branch | NG-7A additive operator half done; NG-7B physical source remains | Do not reopen the algebraic null theorem as missing. |
| **NG-7A, `NUMGEN-OPEN-REC-HOL-OPERATOR`** (NUMGEN v1.20.7 §6.8; RRF §5 calls this a sub-RID of closed NG-7A) | \(CD^T=0\), integrable/holonomic classification in a specified abelian coefficient carrier | Feeds OFN holonomy diagnostic; **not** full geometry | Invariance established for orientation, gauge and fundamental cycle-basis changes; nonlinear carrier replacement not an established invariance. |
| **NG-7B** (NUMGEN v1.20.7 §6.8, OPEN module; no new RID asserted here) | Physical nonintegrable source / non-Abelian extension | Feeds `RTG-OFN-OPEN-FRUSTRATION`, `RTG-OPEN-REGGE-BRIDGE` | Candidate connection, history/birth, spin/quaternionic, OPEN-M sources remain unselected. |
| **`RTG-OPEN-REGGE-BRIDGE`** (Programme v1.2 OPEN-P3) | Nondegenerate metric, network compatibility and typed curvature/coupling dictionary | Requires source/carrier/transport/observable matching where applicable | P3 does **not** require additive holonomy as its exclusive curvature source. Any dictionary *using* \(h\) must identify its carrier and transformation law. |
| **`RTG-OFN-OPEN-REF-CLOSURE`** (OFN §9) | Is edge closure mathematically equivalent to reference consumption? | Related to primacy, distinct from choosing curvature source | Counting equality or a chosen K3 closure does not settle the quotient/reference equivalence. |

**Dependency sketch (not a claim that all are strictly sequential):**

`RRF OPEN-B → OPEN-E1 → OPEN-E2` controls an admissible network/edge model. `RTG-OFN-OPEN-PRIMACY` constrains, but is not solved by, this selection. Typed additive carriers make NG-7A cycle operators meaningful. A physical nonintegrable source remains `NG-7B` / `RTG-OFN-OPEN-FRUSTRATION`. A further physical metric/curvature/coupling identification remains `RTG-OPEN-REGGE-BRIDGE`. There is **no** established theorem that this entire chain is the only route to geometry.

## 4. Pilot decisions, two independent axes, stop

**FMS audit dispositions** (four fixed outcomes, not scientific truth tags):

- **FMS-01:** `COVERED`. Existing OFN/RRF carrier and transport obligations suffice. Physical bridge and canonical network variables are `ROUTED TO RRF OPEN-B/E1`. No new OFN field adopted.
- **FMS-02:** `ROUTED TO RTG-OFN-OPEN-PRIMACY`. Primitive-object selection not made; the carrier-versus-nonintegrability trade-off above is an *explicit conditional dependency*.
- **FMS-06:** `ROUTED TO RTG-OPEN-REGGE-BRIDGE` for physical curvature/dictionary, and to `RTG-OFN-OPEN-FRUSTRATION` / NG-7B for sources. P3's **source neutrality** is an untagged audit finding, not a misuse of `COVERED`.
- **FMS-04/FMS-05:** **not opened**; only instantiate if an owner supplies a defined discrepancy or precise question. No compulsory second Mathematical Structure Audit.

**Model assessment** is a separate axis: `NECESSARY`, `SUFFICIENT`, `EXCLUDED UNDER ASSUMPTIONS`, `UNRESOLVED`. The preceding conditional exclusion is not a global ontology ruling.

**Pilot stop achieved (proposed):** no demonstrated contract gap in three investigated subjects; one useful dependency map and targeted evidence-to-RID links. The audit should **stop here**, with OFN owner invited to import the map as a *noncanonical second-pass evidence input*. No permanent new audit DSN, mandatory philosophy stream or scientific promotion follows. The remaining OPENs stay with their owners. **No owner has approved this closure merely because this proposal was written.**
