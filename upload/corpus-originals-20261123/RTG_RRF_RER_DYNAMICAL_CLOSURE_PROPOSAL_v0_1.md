---
title: "RRF / RER — Proposed Dynamical Closure Evaluation Contract"
version: "v0.1"
date: "16 October 2026"
status: "NONCANONICAL PROPOSAL — RER v0.2 source pending; not adopted as registry/profile requirements"
origin: "Extracted without claim upgrading from adopted RRF v0.8 §6.4"
---

# Proposal record (not a scientific owner DSN)

This proposal was carried as non-normative §6.4 of adopted RRF v0.8, and is separated here to preserve the RRF theorem-source policy. The RER v0.2 document, F3/age-family proofs and the N=7/8 Stage-2 global certificate have **not** been supplied for independent inspection. Nothing here constitutes adopted physical realization, mandatory RRF profile fields, or a claim of globally controlled closure.

### 6.4 OPTIONAL / PROPOSED dynamical-closure evaluation contract — RER source pending

`[DEF] [scope: RER-PLAN-ONLY; source document not mounted; NON-NORMATIVE proposal]` A *claim record* about the sufficiency of a proposed representation may carry

\[
\mathcal K_{\rm closure}=(S,F,O,\pi,D,p,\mathcal E;\ \text{clock},\text{source/adoption}).
\]

`S`: full specified state and carrier; `F`: exact named update/projection cadence; `O`: preserved observable family; `\pi`: proposed factor map with admissible regularity class (`NOT_PROPOSED` if none); `D`: source and invariance domain; `p`: jet order or `exact`; `\mathcal E`: norm/domain/constants/remainder **and horizon** if approximation claimed. `clock` is not inferred from dyad degree; `source/adoption` separates a local calculation, source report and scientific owner/adoption status.

| Closure outcome | Required meaning; never automatic physical interpretation |
|---|---|
| `STATIC_COMPLETE` | present-state quotient completeness under specified symmetry; not dynamic closure |
| `EXACT_CLOSURE` | `\pi F=F_{eff}\pi` plus `O=O_{eff}\pi` if observables must be retained |
| `FINITE_ORDER_CLOSURE` | equality of finite Taylor jets under explicit degree/weight convention; not exact analytic closure |
| `CONTROLLED_APPROXIMATE_CLOSURE` | explicit domain, norm, remainder bound and finite-time error propagation horizon (unless globally proved) |
| `NONCLOSURE_WITNESS` | same reduced state but different next `O` **for same named full map** |
| `FORMAL_ONLY` | formal power series or finite jet; no convergence or physical selection |
| `OPEN` | missing map/attachment/realization/proof/validated global error, itemized |

**[ALG] [scope: explanatory standard mathematics; not an imported RER theorem] Observable-rank necessary condition:** if a smooth factor preserves named `F` and `O`, then locally `rank D(O,O\circ F,\ldots,O\circ F^m)\le\dim S_{eff}`. Any rank-four deduction from the signed-Gram/harmonic study remains **session-grade pending RER owner review**; this note does not import it as a verified RER theorem. A rank lower than four alone does not construct a factor.

**[DEF] [scope: RER-PLAN-ONLY; communicated source status, NON-NORMATIVE]** The user-communicated RER v0.2 plan proposes T02/T03 source synchronization, F3/age-family and `w_13` entries, plus N=7/8 finite-jet vs Stage-2 certificate separation. No full v0.2 registry, F3, age-family or Stage-2 current proof artifact was supplied. Accordingly **do not mark Stage-2 as globally certified** or register bounds `\|\mathcal E_7\|_B\le K_{7,2}R^8` / `\|\mathcal E_8\|_B\le K_{8,2}R^9` as `CONTROLLED_APPROXIMATE_CLOSURE`. The communicated status is `FINITE_JET_FORMAL_VERIFIED / LOCAL_CERTIFICATE_REPORTED / GLOBAL_CERTIFICATE_PENDING`, **only as RER plan/source report**.

**Adoption guard for §6.4:** source pending does not block review of v0.8 as a scoped working-standard revision, but this optional block must not be turned into a mandatory RRF profile field or an accepted physical representation before RER source/adoption evidence is available.

