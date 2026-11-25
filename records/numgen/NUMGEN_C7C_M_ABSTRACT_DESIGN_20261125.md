# NUMGEN C7C-M — abstract three-stream carrier design

**Date:** 25 November 2026.  
**Status:** [SESSION], DESIGN ONLY, proposed for co-owner review. No new owner claim, RID, preregistration freeze, campaign, numerical trajectory, or DSN change. M4 remains HOLD.  
**Governing source:** `numgen-v1.22`, DSN SHA-256 `36b31755c1bd73f1d5f69117c63b1556afacc18c2505e1b865b7a3adf512d40b`, tagged commit `c5acda99de18598108e9b5e368ad15fa74f5488d`.  
**Research target:** a certified nondegenerate composable three-stream witness and interface-typed WD-DOM, not an expanded list of rational labels.

## 1. Read scope and inherited constraints

- NUMGEN v1.22 §§2, 3 (SG-NG-20, 25, 26), 6.6 (N5-C1–C4, C6, N5-PHYS-1, C7A, C7C-WD/0/M, primitive lift, L-BACKBONE, L-MONO, L-PHASE, INF-1/2), 8 and 9.1: targeted source reading; not a new proof audit of unchanged claims.
- Frozen `upload/numgen-records/NG_C7C_M2_PREREG_DRAFT_v4.md` §§1–11 (Git blob `91c99d890ec6aeb1ca21de1389070597fa2d0e6a`), and `NG_C7C_M2_ANALYSIS_LOG.md` E0–E6 including E4-COR-1, E5-COR-1 and E6-D (blob `1f3cde0f1d27e8614c6d8daf949194d3bb516c02`): read the frozen instrument and the relevant analysis/correction sections. `NG_C7C_M2_CENSUS_PROTOCOL_v1.md` (blob `92e08cb958e07cd0e631fc85348a376145fcdd93`), targeted universe/field/replay requirements.
- TDR-G `tdrg-v2.13` §§3, 6.2–6.3, 6.12–6.13 (blob `77b11fdb6f88ad2609968f658e89e231a43bb689`): targeted rule, recurrence, orientation, event inventory and custody passages. No general new import or producer-policy decision.
- The M2 instrument is used as a design reference, not silently edited or repinned. Any extension is a separate preregistration with its own exact source/semantic keys. Census-1 remains 160 records, 120 admitted, INCONCLUSIVE / INCONCLUSIVE; no retrospective admission. S1 resolved P2 sensitivity on the registered witness panel, not the missing chain.

[OWNER: NUMGEN v1.22 §6.6] The required shape is `x=(A,B) ∈ R_bd`, `y=(B',C) ∈ R_bd`, a certified middle-interface germ `[φ]`, and independent outer-pair provenance `Π(x,[φ],y)`. An algebraic count identity is not physical co-realization. M2-1 is adopted algebra; M2-0 and M2-2 are instrument lemmas, not adopted owner results. The definitions of the interface and its witness are label-independent; Π is outside the equivalence. N1 and N2 prevent a vacuous PASS.

## 2. Existing-stream obstruction

[SESSION][ALG] On the common small certified dyad sector, the primitive transition count T and the phase-coincidence pair B_+, B_- do not already yield a new admitted three-type chain.

By N5-C6 and INF-2, on the block prefixes H_M,

    N_T(H_M) = 6M,
    N_+(H_M) = M - (τ/(2π)) log M + O(1).

N5-PHYS-1 gives |N_+ - N_-| ≤ 1. Thus the same asymptotic holds for N_-. For either sign, qN_T - pN_± = (6q-p)M + (pτ/(2π))log M + O(1), unbounded for every p,q>0: the linear term is nonzero unless p=6q, in which case the logarithm diverges. Swapping the order does not change boundedness. Consequently no pair involving T and one of B_± has a positive bounded label on these prefixes. The only existing bounded leg among these three types is the B_+/B_- pair and its reciprocal; their composite repeats the outer type, excluded by SG-NG-20. This is a deduction on the three named types, not a no-go theorem for all dyad observables. Adding more records of these types cannot remove that obstruction.

## 3. Preferred route: an analytic radial-zero crossing candidate

[SESSION][DEF proposal] Work on a sufficiently small common punctured, one-chart certified tube on which the owner L-MONO, L-PHASE, L-BACKBONE, INF-1/2 and N5-PHYS-1 hypotheses hold, shrinking where needed. No explicit-radius or U_NG = U_D claim. Use the same primitive map T, common prefix order, orientation and lift as NUMGEN-DEF-N5AS1-PRIMITIVE-LIFT. Write

    W_n = ρ_n + ω η_wrap,n,    ω = exp(2πi/3),
    W_n = |W_n| exp(i φ̂_n),
    π/6 < φ̂_(n+1) - φ̂_n < π/2.

Take B_+, B_- from the owner (positive and negative phase-coincidence rays, angles 0 and π). Propose one new candidate predicate, C_r, fixed here before any trajectory search:

    C_r at x -> Tx iff ρ(x) > 0 ≥ ρ(Tx).

This is the decreasing radial-zero crossing; at the corresponding ray ρ=0, η_wrap>0, the angle is β=2π/3. It uses the two endpoint states of the primitive transition, not interpolation, an external clock, or a ratio. The orientation/frame, gauge and physical independence of C_r still require owner review. The declaration alone is not a certified RTG event type.

### 3.1 Conditional count and recurrence lemma

[SESSION][THM, conditional on the named local-map hypotheses] Since

    ρ = Re W + Im W / √3
      = (2/√3) |W| cos(Θ - π/6),

the positive-to-nonpositive sign change crosses exactly one β+2πℓ threshold (the other radial-zero ray is negative-to-positive). Strictly positive increments <π/2 cannot cross both radial-zero rays in one step. For the half-open crossing convention (φ̂_j, φ̂_(j+1)], the exact C_r count over n transitions is therefore

    N_C(n) = floor((φ̂_n - β)/(2π)) - floor((φ̂_0 - β)/(2π)).

Owner L-MONO identifies B_+ with the positive-ray lap count (same half-open convention). For any real a and shift 0≤s<1, floor(a)-floor(a-s)∈{0,1}. Applied at both endpoints this gives |N_C(n)-N_+(n)|≤1. N5-PHYS-1 then gives |N_C(n)-N_-(n)|≤2; no change of the owner's B_- boundary convention is needed. Both bounds are uniform in finite prefixes on the declared one-orbit architecture. Since the lift is unbounded, C_r is prefix-cofinally repeatable. On block prefixes the INF-2 count also yields

    N_C(6M) = M - (τ/(2π)) log M + O(1).

As in C6, this excludes an eventual fixed blocking of the primitive T as C_r. These are count/recurrence statements, **not** R_pair or physical-admission statements.

### 3.2 Noncoincidence of transition tokens

[SESSION][THM, same hypotheses] The stronger claim that C_r is not just an identical token predicate to either B_± can be checked analytically. From L-PHASE and INF-1,

    D_(M+1)-D_M = τ q_M - r_M,    |r_M| ≤ C q_M^(3/2),
    q_M → 0,    D_M → ∞.

Thus D_M eventually increases with increments tending to zero. For every open arc of the angle circle, D_M modulo 2π enters that arc infinitely often: choose a smaller interval in the arc and the successive first passage across its lifted lower endpoints; eventually each overshoot is smaller than its width. The block-start angles φ̂_(6M)=φ̂_0+2πM-D_M therefore visit every fixed open arc infinitely often. Also δ_T(T^(6M)x)→π/3 by L-MONO.

Use the three arcs of half-width π/24 centered at π/2, 5π/6, 11π/6. For sufficiently late block starts, |δ_T-π/3|<π/24. The respective transition angle intervals then cross only β, only π, or only 2π among the three specified thresholds (with the expected local ρ signs at B_± crossings). Hence each candidate event predicate occurs without the other two infinitely often on each orbit under these hypotheses. This is a discrete-transition distinction; it does not assume that no transition can ever contain two different ray crossings.

**Limit:** distinct tokens, cofinality and non-fixed-T-blocking are not enough by themselves to certify independent *physical* event types. The radial-zero predicate needs a gauge/relational interpretation audit (including permitted orientation changes), and all three pairs need independent R_pair certification. The choice of a common phase cycle may still be a common-parent multiplicity control under SG-NG-26. No claim of a new dynamic label or a physically primitive third clock is made. The proposed bounded labels are all 1; a useful positive carrier control is the aim, not dynamic breadth. If the owner judges C_r a representation-only re-indexing, reject this route rather than weaken SG-NG-20.

## 4. Conditional C7C-M construction and WD-DOM(b) obstruction

[SESSION][THM, conditional implication, not an evaluated M2 verdict]

Assume the following prerequisites, none inferred from a rational label:

- H1. The owner certifies C_r as an independently typed physical recurrence stream, and certifies the pairs (B_-,C_r) and (B_+,C_r) in R_pair, in the same one-orbit prefix context as the existing N5-PHYS-1 pair, with the common-domain and gauge hypotheses of §3.
- H2. The analysis universe includes the already-certified B_+/B_- pair on two physically distinct comparison instances ω and ω', with one-orbit co-realization semantics. Distinctness is independently certified (not simply two distinct seeds, two re-indexed histories, or nonidentified forward starts). A cross-instance outer pair in this specified architecture cannot be co-realized. E4-L2 and E4-COR-1 supply the design precedent; applicability at the actual new source pins and chosen instances is reviewed before freeze.
- H3. The level-b key registry preserves the M2 distinction: same owner-native event schema/sector/gauge/order semantics across ω and ω', no orbit ID or label inserted into κ_b. Interface equivalence is the bounded single-stream witness relation from M2; Π retains independently certified outer-pair co-realization.

Then on ω choose

    x = (B_+^ω, B_-^ω),    y = (B_-^ω, C_r^ω),    [φ] = [id_ω].

H1 and §3.1 give x,y∈R_bd at 1:1, independently of Π's boundedness. The outer pair (B_+^ω,C_r^ω) lies in R_pair by H1, so Π is true. M-1A/M-1B give the output label; it is not used to define the operation.

Choose x'=(B_+^ω',B_-^ω'), y'=y. For primitive prefixes n=6M+r, 0≤r≤5, the universal INF-2 leading and logarithmic coefficients cancel across ω and ω'; the bounded residual and the finite number of events in the last r steps give a bounded single-stream discrepancy for the positive ray. Strict alternation gives the same conclusion for the negative ray. Thus both ends of x and x' have bounded index-preserving witnesses (zero translation on primitive-prefix indices), with the same type keys by H3. They have equal reduced labels by N5-PHYS-1, hence x≈_b x'. Use the identity witnesses for y. M2's canonical transported middle germ

    [φ'] = [ψ_y^L] ∘ [φ] ∘ [ψ_x^R]^{-1}

aligns the two primitive-prefix contexts; it cannot supply co-realization. Its outer pair is (B_+^ω', C_r^ω). Under H2 it is not an admissible same-instance R_pair. Therefore Π(x',[φ'],y') is false. This is a conditional counterexample to WD-DOM(b) in the declared one-orbit architecture: once H1–H3 are certified, N1 and N2 have explicit witnesses (x,x' and the admitted source chain with that replacement). Failure is due to independent instance replacement, not a ratio or a choice of witness after inspection.

**No verdict is issued here.** This implication is not a claim that H1–H3 are already satisfied, nor a theorem about all physical carriers. In particular missing evidence for an outer pair is UNVERIFIED, not by itself certified ¬Π. A level-a result needs its own N1/N2 analysis; no PASS is inferred merely from literal-instance typing. If a richer κ_b includes common-instance data, that is a different, prospectively defined equivalence problem, not a repair of an outcome already inspected. No associativity-transfer, unit, inverse, addition, or dynamic-spectrum extension follows.

## 5. Alternative discrete route (deferred design option)

[OWNER: TDR-G v2.13 §§6.2, 6.3, 6.12, 6.13] The owner-native balanced path-tie predicate is S=0, 2E≡0 mod N for a path; under bound_symmetric it is an inert bound state. SWAP and active P3 are different native rule applications. TDRG-ALG-EVENT-INVENTORY distinguishes permutations, identity and star events; a tie is not a third token-changing event by fiat.

[SESSION][HEUR] If the analytic route fails H1, the fixed three-node N=24, k=1, birth-free reference rule could be studied with the tie predicate as a proposed third event. This requires separate physical event certification, not merely a nonzero diagnostic counter. No generic null/free-step complement or different k values are declared independent physical streams. Within a certified eventually periodic sector, three distinct admissible event types with positive cycle counts a,b,c and common-prefix provenance yield bounded pairs by the existing periodic-count identity C7B-ALG-T2; their output labels are then derived by M2-1. This says nothing about whether such a native cycle exists or whether the quotient domain is saturated. A capped birth stream cannot be a prefix-cofinally repeatable third stream when each birth strictly increases node number and the cap is fixed.

Retain the distinction E4-COR-1: equal-density candidates from different seeds are not certified physically distinct until orbit merging/re-indexing is excluded. New rule and old v18 convention require distinct evidence keys; S1 is not a certificate for a new three-stream carrier. A new discrete census must freeze the universe, predicate and event order, owner rule, gauge and orbit/instance identification, positive control, negative fixtures, F1–F7 availability rules and the WD-DOM decision protocol before inspecting outcomes. No seed, orbit, tie frequency or new policy was searched here.

## 6. Proposed review/launch gates

The recommended next work is **analytic review of the radial-zero route**, not DISC-3 or a broad Census-2.

| Gate | Required evidence / decision | Status |
|---|---|---|
| A1 | Independently audit §§2–3.2: exact local hypotheses, boundary/anchor rules, count bounds, log deficit and arc-visit argument. | Proposed |
| A2 | Owner decision whether C_r is independently physical under SG-NG-20, 25, 26; gauge and event distinction; separately certify both outer and middle R_pair relations. Reject if only a representation/re-indexing. | OPEN |
| A3 | Freeze the common-domain and one-orbit comparison architecture, exact source pins, admissible physical distinctness proof, and prospective κ_b with no outcome/label/instance key at level b. Validate §4's conditional obstruction against the actual carrier, including N1/N2 and the certified ¬Π basis. | OPEN |
| A4 | Co-owner review, followed by PI decision on any new preregistration, certificate or campaign. Only a separately approved design can change M4 HOLD. If A2 fails, return to the alternative route; do not select another ray after results are seen to rescue admission. | PI pending |

This record is the abstract design work only. No M2 PASS/FAIL, new result adoption, model selection, numerical campaign, DSN/RID allocation, Census-1 change, DISC-3 launch or Atlas refresh. A1–A3 can be addressed analytically first; no expensive server campaign is presently justified. 

*END OF RECORD.*
