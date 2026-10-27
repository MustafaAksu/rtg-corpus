# N-5 Discrimination Criterion v2 — Corrections Applied, and What DISC-1D Can Deliver

**Memo ID:** `NG_N5_DISCRIMINATION_CRITERION_v2` · supersedes `_v1`
**Base:** `RTG_NUMBER_GENESIS_DSN_v1.15` (sha256 `d56440c6…3375`, verified)
**Date:** 2026-08-31 · **Auditor:** Claude
**Artifacts:** `ng_n5_discrimination_criterion_cert_v2.py` / `.log` (7 families, no hard-coded assertions, exit 0)

---

## 1. Corrections accepted and applied

**T1's biconditional needs its premise.** From `N_A = m_A L + O(1)`, `N_B = m_B L + O(1)` we get `Δ_{p:q} = (q m_A − p m_B) L + O(1)`; the `⟹` direction requires `L` **prefix-cofinally unbounded**, since a bounded `L` would give a bounded defect at a nonzero coefficient. Premise now in the statement (natural from SG-NG-25). T1b, the cancellation direction, correctly carries no extra premise.

**P1a was a sampled window presented as an interval.** Repaired by replacing sampling with a mechanism: the locked class corresponds to a **hyperbolic attracting period-2 lift orbit**, and hyperbolic periodic orbits persist under small perturbation. Certified multipliers: `0.360000` at `Ω = 0.50` (orbit `{0, 1/2}`) and `0.634807` at `Ω = 0.48`. Stability is therefore `[ALG]` given `[NUM]`-certified multipliers, not an interval inferred from five points. Contingency (P1b) remains `[NUM]` — but that is appropriate, since contingency is an *existence* claim for which sampled witnesses suffice, while stability is a *universal* claim over a neighbourhood and needed the mechanism.

`[COR]` on my own v1 work: the root scan missed the attracting orbit at `Ω = 0.50` because it sits exactly at the scan boundary with zero sign change, which is why v1's multiplier check appeared to contradict the observed locking. Fixed in v2.

**P2 universality is now derived, not sampled.** For any generator with monotone lifted section angle and per-step increment `< π`, each coincidence ray is crossed once per lap, so `N_{B±} = L + O(1)` and T1b gives `|Δ_{1:1}| = O(1)` for *every* such generator. The `ε` sweep is redundant evidence, not the ground of the claim — exactly as the review indicated.

**Branch-neutral language adopted.** Stability = persistence under an elementary move in a pre-declared admissible deformation structure; "open interval" is the continuous-branch realization, not the definition. **`Q^dyn` kept mechanism-neutral**; mode locking demoted to `[INTERP]` reference mechanism. I over-specified in v1 and withdraw the definitional form.

## 2. New result: what a finite-state branch can and cannot deliver

**T3 (proved, corollary of T2).** A deterministic map on a finite state space is eventually periodic on every orbit. By T2, **every co-realized event pair in a finite-state branch lies in `Q^bd`, and unbounded defect is impossible there.** Two consequences bear directly on the DISC-1 redesign:

1. **DISC-1B has no falsification content.** The `Q^bd` census is guaranteed non-empty and cannot fail; it is purely descriptive — a list of which labels exist and are worth testing. That matches the reviewer's reframing, and T3 is the reason it must be so.
2. **Contingency in TDR-G can only mean change of reduced class, never loss of boundedness.** The C6-style contrast — bounded in the control, unbounded in the real system — is structurally unavailable in a finite-state branch. DISC-1D-C should therefore be stated as *class-change under `k`-deformation*, and the pass criterion written accordingly before data.

This is not a weakening: if `r` changes with `k` while predicates, substrate, state-space cardinality and conventions are held fixed, then `r` is a function of the dynamics rather than of predicate multiplicity, which is exactly the content `Q^dyn` is meant to capture.

## 3. Two design notes on DISC-1D, offered before the artifact is inspected

**Compare spectra, not single ratios.** Per-cycle labels `r_{x,k}` vary across seeds at fixed `k`, so `r` is an invariant of a cycle, not of the system. A single seed changing label under `k` is weak evidence — it could reflect the seed landing in a different cycle. The stronger, and I think intended, comparison is between the **label spectra** `{r_{x,1}}` and `{r_{x,2}}` over the frozen panel, together with the per-seed map `x ↦ (r_{x,1}, r_{x,2})`. Recommend pre-registering which of these is the pass criterion.

**A degenerate-pass risk worth fencing now.** If a label changes under `k` merely because a cycle's *length* changes while per-period SWAP and P3 counts scale together, the reduced class is unchanged and no discrimination occurs; conversely if the counts change only because the cycle acquires or loses dual-activity, the comparison is between different sectors rather than the same pair under deformation. Suggest requiring, as part of DISC-1D-S, that the compared cycles be **dual-active at both `k` values for the same seed**, so that the pair being deformed is genuinely the same pair.

The `k`-axis choice at fixed `N = 24` is otherwise well-founded, and freezing the raw seed panel rather than the "retrigger-entry" label is the right call — the label does not survive the deformation even though the states do.

## 4. Ledger position (unchanged from the reviewer's proposal)

C1–C4 CLOSED; C5-SYN-13 mathematical periodic control; **T2/T3** as periodicity-triviality identities; C6 unchanged and discriminating; N5-PHYS-1 = first **physical positive control**, `1 ∈ Q^bd`; C7A unchanged; **`Q^dyn` empty**; DISC-1 → `Q^bd` census; DISC-1D → dynamic gate; C7C downstream of `Q^dyn`, not `Q^bd`.

## 5. Residual question

T3 says the discrete branch cannot exhibit unbounded defect. The canonical continuous pair's unbounded `6:1` discrepancy is thus a structurally *continuous-branch* phenomenon. If `Q^dyn` is ultimately populated only from finite-state sectors, every admitted class will rest on class-change contingency alone. Whether that is sufficient for genesis-grade status, or whether the programme should also require at least one continuous-branch `Q^dyn` witness, is an interpretive call and PI-blocked.
