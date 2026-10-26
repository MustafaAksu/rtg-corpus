# N-5 Discrimination v3 — T3 Retracted and Corrected, DISC-1D Strengthened

**Memo ID:** `NG_N5_DISCRIMINATION_CRITERION_v3` · supersedes `_v2`
**Base:** `RTG_NUMBER_GENESIS_DSN_v1.15` (sha256 `d56440c6…3375`, verified)
**Date:** 2026-08-31 · **Auditor:** Claude
**Artifact:** `ng_n5_discrimination_identity_cert_v3.py` / `.log` — an **identity certificate supporting memo proofs**; its exit code certifies the algebraic identities and nothing else.

---

## 1. `[RETRACTED]` — v2's T3

**Retracted claim:** "in a finite-state branch, unbounded defect is impossible."

**Why it is wrong, and why I should have caught it.** For an eventual cycle with per-cycle counts `(a,b)`, the defect at an arbitrary fixed class is

```
Δ_{p:q} = (qa − pb)·m + (q r_A − p r_B),
```

whose `m`-coefficient is nonzero for **every** `p:q ≠ a:b`. So all other classes diverge linearly. I conflated *"some class is bounded"* with *"every class is bounded"*. This contradicted **my own T2**, which displays exactly this identity, and it also contradicted C6, where I had already certified linear divergence at every non-`6:1` class. A self-inconsistency against material in the same certificate is a worse error than a missing premise, and the two downstream conclusions I drew from it were both wrong.

**`[COR]` Corrected T3 — finite-state eventual-cycle classification.** For a deterministic map on a **closed finite invariant sector**, with predicates determined by the finite state/transition data, every orbit is eventually periodic. If its eventual cycle is dual-active with `a, b > 0`, it realizes **exactly one** reduced bounded class `a:b`; every other `p:q` diverges linearly as `(qa − pb)m + O(1)`. If `a = 0` or `b = 0`, that cycle supplies no positive dual-active bounded class.

**Scope qualifier accepted.** This applies to a closed finite invariant sector — the `N = 24`, three-node no-birth BIND3 sector — not to TDR-G globally, whose state space `⊔_{M≥2} ℤ_N^{2M}` grows under star blow-up and is not a single finite state space.

## 2. Both downstream reversals accepted

**DISC-1B remains falsifiable.** T2 gives boundedness only *conditional on a dual-active cycle*; it does not supply a non-`1` class. The frozen falsifier — all dual-active cycles reduce to `1:1` ⟹ the SWAP/P3 non-`1` search fails — is logically valid exactly as pre-registered in v1.15. My "no falsification content" claim was a consequence of the retracted T3 and falls with it. What is structurally automatic is *boundedness*, not *non-triviality*.

**The C6-style contrast is available in finite state.** `[RESULT]` **T4 (proved):** evaluating the old class `a:b` on a deformed cycle `(a',b')` gives `m`-coefficient `(b a' − a b')`, vanishing iff `a:b = a':b'`. So **class-change under deformation and linear loss of boundedness of the fixed original class are equivalent.** DISC-1D-C can therefore keep the strong bounded→unbounded form rather than weakening to "ratio changed." The minimal witness makes it vivid: cycle `A⁶B` gives `Δ_{6:1} = O(1)`; cycle `A⁵B` gives `Δ_{6:1} = −m + O(1)`. Both finite, both exactly periodic, same fixed class, opposite verdicts.

Consequently I withdraw the residual question of v2. Requiring a continuous-branch `Q^dyn` witness would make branch membership definitional, which conflicts with the branch-neutral architecture — the argument against it is sound and I accept it. The two mechanisms are epistemically parallel: continuous C6 destroys `6:1` by nonlinear slip accumulation; discrete DISC-1D destroys the old `p:q` by deformation of the exact cycle ratio.

## 3. P1a now fully `[ALG]`

The exact route is better than my numerical one. At `Ω = 1/2` the sine terms vanish identically, so `0 ↦ 1/2 ↦ 1` is an exact period-2 lift orbit with multiplier

```
f'(0)·f'(1/2) = (1+K)(1−K) = 1 − K²,
```

hyperbolic attracting for `0 < K < 1`. Hyperbolic persistence gives an open parameter neighbourhood with no numerics at all. The `Ω = 0.48` multiplier `0.634807` is retained as supplementary `[NUM]`. The awkward "`[ALG]` given `[NUM]` multipliers" wording is gone.

## 4. Certificate-description discipline

Accepted: the artifact is re-described as an **identity certificate supporting memo proofs**. Its exit code certifies the algebraic identities only. Eventual periodicity, the monotone-lift ray-crossing theorem, and sector closure are premises argued in this memo, not established by the script. v1 and v2 both described their exit codes too broadly; that is now stated in the file header rather than left to the reader.

## 5. New pre-data finding — DISC-1D needs at least three admissible `k` values

`[RESULT]` **D1 (design constraint).** By T4, for dual-active cycles a class under an elementary move either **persists** or **changes**, exhaustively and exclusively. So a single move `k₀ → k₁` can establish stability or contingency but never both: whichever verdict it returns, it forecloses the other. **DISC-1D therefore requires at least two distinct admissible moves from the same base — that is, at least three admissible `k` values.**

At `N = 24` the constraint `k < N/6` gives `k ∈ {0,1,2,3}`. If `k = 0` is degenerate (zero defect band), the usable set is `{1,2,3}`: exactly enough, with **no margin**. A viable pre-registration therefore looks like — candidate `r` at `k = 1`, persists at `k = 2` (DISC-1D-S), destroyed at `k = 3` (DISC-1D-C) — and if `k = 3` turns out inadmissible for the frozen sector, the design has no room and needs a second deformation axis declared in advance. I would settle that before inspecting the artifact, since discovering it afterwards would force a post-hoc axis choice.

## 6. Ledger position

C1–C4 CLOSED; C5-SYN-13 mathematical periodic control; T2 periodicity triviality; **T3 corrected**, **T4 new**; C6 unchanged and discriminating; N5-PHYS-1 = first physical positive control, `1 ∈ Q^bd`; C7A unchanged; `Q^dyn` empty; DISC-1B = falsifiable non-`1` census; DISC-1D = dynamic gate with the strong bounded→unbounded contingency form; C7C downstream of `Q^dyn`.
