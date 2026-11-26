# NUMGEN C7C-M abstract design — co-owner review (Claude)

**Date:** 25 November 2026.
**Status:** [SESSION] co-owner review. This is not an owner claim, an adoption, a preregistration or a campaign authorization. No DSN change, no RID, and no frozen evidence change.

**Reviewed:**
- `records/numgen/NUMGEN_C7C_M_ABSTRACT_DESIGN_20261125.md` (PR #383, head `467dc8a`, file `ab49bc76…ce7c`);
- the author-side supplement P1–P3 (PR #383, comment `7156326127`).

**Sources read:**
- `numgen-v1.22` (`36b31755…d40b`):
  - §3: SG-NG-20, 25, 26;
  - §6.3a: P3, and the one-chart shrinking theorem;
  - §6.6: the primitive map, the canonical section and B predicate, NUMGEN-DEF-N5AS1-PRIMITIVE-LIFT, L-MONO, L-PHASE, NUMGEN-DEF-N5AS1-DEFECT, INF-1, INF-2, N5-PHYS-1, and WD-CLOSE.
- Frozen `NG_C7C_M2_PREREG_DRAFT_v4.md`: §§2, 9, 10.
- `NG_C7C_M2_ANALYSIS_LOG.md`: E4-L2, E4.4, E4-COR-1, and the level-b table.

## 1. Verdicts

| Gate | Verdict |
|---|---|
| A1 — §§2–3.2 analytic statements | **ACCEPT as conditional [SESSION] deductions.** All steps were checked (§2 below). One precision note, R-a. |
| P1 — relational form of C_r | **ACCEPT (algebra).** Physical pole-exchange covariance stays OPEN. |
| P2 — non-constant lag from B_+ to C_r | **ACCEPT (conditional ALG).** The expansions check. Eventually the lag takes only the values 1 and 2, and both occur infinitely often. |
| P3 — existence of non-merging orbits | **ACCEPT (THM-level argument, conditional on the tube).** It supplies the existence of distinct instances that E4-L2 uses. |
| A2 — physical event typing of C_r | **OPEN, owner decision.** My reading is in §3: at most a relational *positive-control* stream under SG-NG-26; no dynamic content. |
| A3 — instance and outer-pair semantics | **OPEN.** The §4 counterexample is correct but generic (§4 below). The informative question is level a, or a prospectively defined κ_b. |
| Campaign | **none.** M4 HOLD; Census-1 INCONCLUSIVE / INCONCLUSIVE; DISC-3 DEFER; full-interface WD-DOM OPEN. |

## 2. A1 and P1–P3: what was checked

**Coordinates.**
- The primitive map is `T(ρ,η) = (ρ − sin η, η + e^ρ − 1 − sin η)` (§6.6), with `W = ρ + ω η_wrap`, `ω = e^{2πi/3}`, and `Θ = arg W = atan2(√3 η, 2ρ − η)`.
- `Re W + Im W/√3 = ρ` and `= (2/√3)|W| cos(Θ − π/6)`. Hence `ρ = 0` exactly on the rays `Θ = 2π/3` and `Θ = −π/3`, with `ρ > 0` on `(−π/3, 2π/3)`.
- On `ρ = 0, η > 0` the angle is `2π/3 = β`. Verified.

**§3.1 count.**
- By L-MONO, `π/6 < δ_T < π/2 < π`, so one step crosses at most one ρ-zero ray.
- Conversely, if the lift crosses `β + 2πℓ` in a step, then `Θ(x) ∈ (π/6, 2π/3)` gives `ρ(x) > 0`, and `Θ(Tx) ∈ [2π/3, 7π/6)` gives `ρ(Tx) ≤ 0`. So C_r ⇔ crossing of `β` in `(φ̂_j, φ̂_{j+1}]`.
- The floor formula follows. B_+ uses the same half-open convention: L-MONO, `η⁻ < 0 ≤ η⁺`.
- With `s = 1/3`, `N_C − N_+ = [⌊A−s⌋ − ⌊A⌋] − [⌊A_0−s⌋ − ⌊A_0⌋] ∈ {−1, 0, 1}`. The bound `|N_C − N_−| ≤ 2` follows from N5-PHYS-1. The INF-2 form of `N_C(6M)` follows. Verified.

**§2 obstruction.** `q·6M − p(M − (τ/2π) log M) = (6q−p)M + (pτ/2π) log M + O(1)` is unbounded for all `p, q > 0`. Unboundedness on the block subsequence suffices. Verified.
- Excluding the B_+/B_− composite `(B_+, B_+)` by SG-NG-20 matches the owner's own use at WD-CLOSE (§6.6).

**§3.2 arcs.**
- `D_{M+1} − D_M = τ q_M − r_M` follows from L-PHASE and the definition of `D_M`. It is eventually positive and tends to 0, while `D_M → ∞`. So the block-start angles `φ̂_0 − D_M` (mod 2π) visit every open arc infinitely often.
- With `|δ_T − π/3| < π/24`, the three arcs give transition intervals contained in `(3π/4, 11π/12)`, `(13π/12, 5π/4)` and `(25π/12, 9π/4)`. They contain only `β`, only `π`, and only `2π` respectively, and none of them meets the other ρ-zero ray `5π/3`.
- The ρ signs at the π crossing are negative on both sides, as B_− requires. Verified.

**P1.** `ρ(Tx) = ρ − sin η`, so C_r ⇔ `0 < ρ ≤ sin η`, and with `m = e^ρ`, C_r ⇔ `m > 1 ≥ m′`. Verified as algebra. That `m = |ζ|` in the RRF wrapped representation was taken from the comment; I did not re-read RRF for this review.

**P2.**
- At the first block start strictly below `2πℓ`: `Θ ∈ (−c q_M, 0)`, so `η = O(t³) < 0` with `t ≈ |W| ≈ ρ`.
- One step: `ρ₁ = t + O(t³)` and `η₁ = e^t − 1 + O(t³) = t + t²/2 + O(t³)`. This is a B_+ token (`η < 0 ≤ η₁`, `ρ, ρ₁ > 0`).
- Second step: `ρ₂ = ρ₁ − sin η₁ = −t²/2 + O(t³) < 0`. This is a C_r token. So the lag is 1.
- Near `−π/6`, the endpoints at `≈ π/6, π/2, 5π/6` give lag 2. Verified.
- Since `δ_T → π/3` and the rays are `2π/3` apart, the lag is eventually in `{1, 2}`.

**P3.**
- For each `(m, n)`, injectivity of `T^m` gives at most one `y` with `T^m y = T^n x`. So `E(x)` is countable, while the tube is uncountable.
- The argument needs every forward iterate to stay inside the P3 injectivity box. The one-chart shrinking theorem (§6.3a, "lifted tube is forward invariant") provides this, and so does the v1.20 corollary placing `U_D,tube` inside the box. Verified.

**R-a (precision note, not a defect).** State the "common tube" as one forward-invariant set. The cited lemmas are each "on a sufficiently small tube", and L-PHASE and INF-1/2 are on the existential `U_NG`.
- Suggested wording: take a forward-invariant one-chart tube from the shrinking theorem, inside the P3 box, on which all of L-MONO, L-PHASE, L-BACKBONE, INF-1/2 and N5-PHYS-1 hold.
- Alternatively: every orbit has a tail inside any such neighbourhood, because `q_M → 0`. All the claims are tail statements, and restricting to a tail changes counts by `O(1)`.
- The explicit `U_D,tube` carries only the imported L-PHASE constant and the RECOG consumer counterparts. It is not a substitute for `U_NG` here.

## 3. A2 — physical event typing (my reading, for the owner decision)

1. **Relational content.** P1 shows that C_r is the unit-modulus section `|ζ| = 1`, crossed downwards. B_± are the phase-coincidence sections. Both kinds are relational conditions of the dyad, not observer-chosen Θ levels. This is relevant to the owner's canonical-section result, which admits Θ = 0 and π because they are relational, and treats other Θ levels as coordinate probes.
2. **SG-NG-20.** C_r is not a ratio, power or blocking of T. P2 shows that it is not a constant-lag copy of B_+. The literal clause of SG-NG-20 does not exclude it.
3. **SG-NG-26 decides the status.** B_+, B_− and C_r are each one crossing per revolution of the same lift φ̂: `N = L + O(1)` for the common revolution count L. So every bounded class among them is `1:1`, forced by multiplicity. This is the same status the owner already gives the N5-PHYS-1 pair (a positive control). Even if admitted, C_r adds **no** dynamic label and no evidence of breadth. At most it completes a three-stream *positive-control* carrier for testing the composition machinery. That is the design's stated aim, and I agree it is the only claim available.
4. **Orientation.** Exchanging the two poles maps the decreasing crossing at `β` to the increasing crossing at `−π/3`. C_r is therefore an oriented predicate, like B_+ and B_−. Admission should fix it in the same oriented, fixed-support, reduced model as B_± and claim nothing about spectators (SG-NG-13).
5. **R_pair.** The pairs (B_±, C_r) need their own certified `R_pair` provenance. The token distinction of §3.2 and the lag result P2 are necessary for that, but not sufficient.

## 4. A3 — the conditional WD-DOM(b) counterexample is generic

The §4 implication is correct under H1–H3. It uses three things:
- the cross-orbit equivalence of the left end (E4-L2);
- an instance-blind level-b key (H3);
- the impossibility of cross-instance co-realization (H2).

It uses no property of C_r beyond `y ∈ R_bd` and `(B_+, C_r) ∈ R_pair`. Hence, under H2 and H3, **every** admitted same-instance chain whose end is cross-orbit equivalent yields `¬WD-DOM(b)`. The frozen reading matrix (prereg §10) already anticipates exactly this case: "outer admissibility does not descend across instances".

**Consequences:**
- A level-b FAIL obtained this way would report a property of the instance-blind key together with the one-orbit Π. It would not report a property of the physical carrier.
- The informative datum is **level a**: same instance, with its own N1/N2 analysis. Alternatively, a κ_b that carries common-instance data could be defined *before* any outcome is seen. The design already says this; I recommend making it the primary question of any future preregistration.
- Under H2, ¬Π for a cross-instance outer pair holds by the declared architecture, not by missing evidence. The design's UNVERIFIED-vs-¬Π distinction is right, and the future preregistration should state which basis it uses.

P3 supplies the existence of the distinct instances ω ≠ ω′ that E4-L2 and E4-COR-1 use (two non-merging orbits). It does not settle physical distinctness under an enlarged gauge. The supplement says this too.

## 5. Numerical sanity check (`[NUM]`, not a proof input)

- **What was run:** `evidence/numgen/c7c_m_review_20261125/a1_sanity.py` (`f63c0834…c674`, mpmath 1.4.1, 40 digits) iterates T for 120,000 steps from the canonical seed `(1/100, 1/250)` in `U_D,base`. No seed or ray was searched or selected.
- **Output:** `a1_sanity_output.txt` (`d765d507…feb1`).
  - `N_C = 20000`, `N_+ = 19999`, `N_− = 20000`.
  - `max|N_C − N_+| = 1`.
  - The §3.1 floor formula matched `N_C` at every step.
  - `δ_T ∈ [1.04358, 1.05080]`, inside `(π/6, π/2)`.
  - The lag B_+ → C_r was 2 in 19,948 cases and 1 in 51 cases.
  - No transition carried two of the three predicates (C_r 20000, B_+ 19999, B_− 20000, none 60001).

This agrees with A1 and P2 on one orbit and one finite prefix only.

## 6. Recommendation

- The analytic preparation (A1, P1–P3) is sound as conditional [SESSION] work. Nothing needs recomputation.
- A2 (physical typing of C_r) and the choice between level a and a prospective κ_b for A3 are owner decisions. They should be settled before any preregistration is drafted.
- No campaign is justified now. M4 stays HOLD.

*END OF RECORD.*
