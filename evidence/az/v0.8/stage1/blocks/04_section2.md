## §2. Active Frontier / OPEN Registry

This is an infrastructure document. The registry covers scope and infrastructure questions; the scientific open items of Thread C are in §4.3.6. No experiment or artifact is requested by this section.

**OPEN 1 — Is a graph/transfer-zeta observable dynamical or substrate?** [RID: AZ-OPEN-SCOPE-ZETA]

Status: PARTIAL  
Owner study: this DSN  
Question: Determine whether a graph/transfer-zeta observable of the TDR-G defect graph is a branch-discriminating *dynamical* observable or merely an aggregate/substrate diagnostic.  
Closure criterion: no separate criterion is registered. The conditions that apply are the success criterion of §1.1 and the two null gates of §4.3.6 (a degree/reciprocal null and the $\mathbb{Z}_N$ geometry null), with the declarations SG-AZ-5 requires.  
Dependencies: the Thread C engine (§4.3.1) and its artifacts (§9).  
Closed sub-items:
- the first angular observable (the Core(G_T) `4|q` rule) is a substrate-geometry diagnostic, not dynamical :: `[NUM diagnostic]` :: [RID: TDRG-AZ-STATIC-ZN-4Q] :: §4.3.3, §4.3.4

Active sub-items:
- a dynamical (non-substrate) graph observable :: `[OPEN]` :: §4.3.6

Required before any Level B promotion.

**OPEN 2 — Are the $\mathbb{Z}_N$ arithmetic objects bridge-candidate observables?** [RID: AZ-OPEN-SCOPE-ARITH]

Status: ACTIVE  
Owner study: this DSN  
Question: Determine whether the $\mathbb{Z}_N$ cyclic memory length and divisibility structure of TDR-G are bridge-candidate observables for OPEN-P1, or purely internal to the TDR-G DSN. The full question, with the objects it concerns, is stated in §4.2.  
Closure criterion: as stated in §4.2 — OPEN-P1 at minimum formally opened, a candidate bridge observable defined, and SG-AZ-7 satisfied.  
Dependencies: OPEN-P1 (Programme); the TDR-G objects cited in §8.  

Required before any Level B promotion.

**OPEN 3 — Promotion conditions** [RID: AZ-OPEN-PROMO]

Status: ACTIVE  
Owner study: this DSN  
Question: State the exact conditions under which this document would be promoted to a full Level B active scientific DSN, including required artifact and transcript provenance.  
Closure criterion: those conditions registered in an adopted edition of this DSN. The success criterion of §1.1 is the current statement; it does not yet name the artifact and transcript provenance.  
Dependencies: none.  

Required before any Level B promotion.

**Closed modules.**

- **AZ-OPEN-ENG** [RID: AZ-OPEN-ENG-BLOCKERS] — CLOSED. All five `[ENG-blocker]` items fixed and all three `[ENG-open]` items closed; engine certified by an exit-code-gated suite. Per-item closure record in §4.3.1; artifacts and their availability in §9. The guard that depended on this module (SG-AZ-5) is a provenance guard (§3).
- **AZ-OPEN-EDGE** [RID: AZ-OPEN-EDGE-EXPORT] — CLOSED. Decision: **directed, both orientations.** Each symmetric defect pair $\{a,b\}$ is exported as the two directed edges $(a,b)$ and $(b,a)$. One-edge-per-pair makes `extract_recurrent_core` silently empty and the Hashimoto operator ill-defined; both orientations give a well-defined $2|E|\times2|E|$ Hashimoto operator. Registered in §4.3.1.1 and in the frozen conventions artifact. A consequence of this decision is PROP-AZ-CORE-EQUIV (§4.3.2).

---

