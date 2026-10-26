# N-5 Discrimination Criterion — Correction, Two Theorems, and a Positive Template

**Memo ID:** `NG_N5_DISCRIMINATION_CRITERION_v1` · **Supersedes items A3/A6 of** `NG_N5PHYS1_DISCRIMINATION_AUDIT_v1`
**Base:** `RTG_NUMBER_GENESIS_DSN_v1.15` (sha256 `d56440c6…3375`, verified)
**Date:** 2026-08-31 · **Auditor:** Claude
**Artifacts:** `ng_n5_discrimination_criterion_cert_v1.py` / `.log` (6 assertion families, all genuinely gated, exit 0)

---

## 1. `[COR]` — my own certificate defect

The reviewer is right: A3 and A6 were asserted as `True` inside an exit-code-gated script. That is a real methodological failure, not a presentational one — a hard-coded `True` makes the exit code vacuous for those items while inheriting the authority of a passing certificate. It is exactly the kind of thing this programme's certificate discipline exists to prevent, and I should not have written it.

Remedy applied: A6 is now **proved symbolically** (T1 below), A3 is demoted to a memo-level admissibility argument with no certificate status, and the new certificate contains no placeholder assertions. A4/A5 remain finite-checkpoint numerics and are labelled as such; their conceptual weight now rests on T1 rather than on the samples.

## 2. Accepted without reservation

The `Q^bd` / `Q^dyn` split is better architecture than my single-tier proposal: it keeps C1–C4 and C7A intact as theorems about bounded pairs, requires no reopening, and localises the correction to the *semantics of the spectrum symbol* rather than to any proof. The generalized SG-NG-26 (common-source finite-multiplicity, stated via a parent stream `L` rather than via rays) is strictly better than my version — rays were an instance, not the principle. And reserving `Q_RTG^real` for the strong object with an explicit `[COR]` on the v1.15 definition, rather than silently re-pointing the symbol, is the right ledger hygiene.

**T1 (proved).** With `N_A = m_A L + O(1)` and `N_B = m_B L + O(1)`, the parent-count coefficient of `q N_A − p N_B` is exactly `(m_A q − m_B p)`. So the defect is bounded **iff** `q m_A = p m_B`: the reduced class is forced to `m_A : m_B` independently of whatever dynamics generates `L`. This is the generalized SG-NG-26 as an algebraic identity.

## 3. The DISC-1 point is stronger than stated — it is structural

**T2 (proved).** For an exactly periodic co-realized word with `a` A-events and `b` B-events per period, `b N_A − a N_B = b r_A − a r_B`, where `r` are partial-period remainders. **The period count cancels identically.** Every exactly periodic co-realized pair is boundedly commensurate at `a:b` by construction.

The consequence for C7B-DISC-1: because the `N=24, k=1` family is an *exact-cycle* family, DISC-1 **cannot fail on the boundedness axis**. Its stated falsification rule tests only whether the ratio is non-`1`, which is a combinatorial question about how many SWAP and P3 events a cycle happens to contain — not whether the class is dynamically contentful. So DISC-1 as currently designed has no falsification power for the dynamic spectrum, and the pre-data DISC-1D amendment is not merely prudent but load-bearing.

This also unifies two things the ledger currently treats separately: C5-SYN-13 and DISC-1 are the *same phenomenon* under T2. C5 is correctly fenced as an abstract control; DISC-1 needs the identical fence.

## 4. Proposed criterion — two-sided, and a worked template

A discrimination certificate should require **both** properties, because each alone admits a degenerate case:

- **Stability.** The class persists under small admissible perturbation of the generator. (Rules out knife-edge coincidences that no physical realization could hold.)
- **Contingency.** There exist admissible dynamics on the same domain, with the same predicates and comparison semantics, under which the class *changes or becomes unbounded*. (Rules out universality — a class that holds for every dynamics is a fact about the predicates.)

Ray-multiplicity classes fail contingency. Exact-cycle classes fail contingency for the same reason (T2 holds for every periodic system). The reviewer's "matched null control" is the contingency half; I am proposing that stability be required alongside it.

**Positive template — mode locking.** In the standard circle map at `K = 0.8`, with `A` = primitive steps and `B` = section crossings, `Δ_{2:1}` is bounded with oscillation **1** across `Ω ∈ {0.480, 0.490, 0.500, 0.510, 0.520}` — an interval, so **stable** — and linearly unbounded at `Ω ∈ {0.440, 0.460, 0.470, 0.475, 0.525, 0.530, 0.540, 0.560}` — so **contingent**. That is what a dynamically contentful `2:1` looks like: boundedness is a fact about the dynamics, holding on an open set and failing off it.

By contrast, `max|Δ_{1:1}(B_+, B_-)| ≤ 1` for every perturbation `ε ∈ [−1, 2]` of the dyad generator. Universal, hence uninformative.

**Structural reading.** Elements of `Q^dyn` are **mode-locked classes**: pairs whose *aperiodicity* is shared, so that the slips of one stream track the slips of the other. That is a genuine physical phenomenon and a real target. It also explains why the canonical A/B pair fails — its slips are tracked by nothing — and why C6 is the model example of correct epistemics: the null control gives bounded `6:1` exactly where the nonlinear dyad gives `6:1` unbounded by `(3τ/π) log M`. C6 is contingent; that is precisely what N5-PHYS-1 lacks.

Note this is the *right* place for classical rotation-number theory. Earlier I flagged that Sturmian/three-distance machinery does not apply to our drifting rotation number — that remains true for the canonical pair. Arnold-tongue mode locking applies here instead, to the question of which bounded classes are structurally stable, which is a different question about a different object.

## 5. Recommended state change (PI-blocked; stated for ruling, not applied)

1. `[COR]` on the v1.15 `Q_RTG^real` definition; split into `Q^bd` and `Q^dyn` per the reviewer's architecture.
2. N5-PHYS-1 → **first physical positive control**; `1 ∈ Q^bd`, with `Q^dyn` currently **empty**.
3. Adopt generalized SG-NG-26; add T1 and T2 as its supporting identities.
4. Amend C7B-DISC-1 pre-data with the DISC-1D gate, and record under T2 that an exact-cycle pass is necessarily a positive control.
5. Register the two-sided criterion (stability + contingency) as the standard for admission to `Q^dyn`, with the mode-locking template as the reference example.

## 6. Open question I cannot resolve, and would put to the owners

If `Q^dyn` requires contingency, then admission depends on a declared class of *admissible comparison dynamics* — what may be varied, and how far. In the continuous branch this is natural (perturb the generator). In the native-discrete branch, where the dynamics is combinatorially rigid, it is not obvious what "small admissible perturbation" means: varying `N` or `k` changes the system rather than perturbing it. Without an answer, the contingency half of the criterion may be inapplicable exactly where the programme most needs it, which would make `Q^dyn` unreachable from TDR-G by construction. This is an interpretive/physics-input call and therefore PI-blocked; I flag it as a possible structural obstruction to the current C7B routing rather than a defect in it.
