# C7C-M — Multiplication Design Under C7C-WD

**Memo ID:** `NG_C7C_M_DESIGN_v1` · **RID:** `NUMGEN-C7C-M` · **Date:** 2026-09-19 · **Auditor:** Claude
**Base:** `RTG_NUMBER_GENESIS_DSN_v1.18` (frozen `908786bb…5fcad`), `NG_C7C_WD_C7C0_DESIGN_v1.md`, `NG_C7C0_RECIPROCAL_CERT_v2.md`
**Status:** DESIGN ONLY. One symbolic identity verified. **No campaign data, no realization search, no trajectory computed.** Nothing here enters `Q_RTG^bd` or `Q_RTG^dyn`.

---

## 1. The candidate — chain composition through a shared stream

The only owner-native binary composition available from certified objects alone is Eudoxus transitivity: two comparisons that share a stream compose to a comparison between their outer streams.

```
x = (A, B) ∈ R_bd at reduced class p:q,   y = (B, C) ∈ R_bd at reduced class u:v,
B the SAME certified stream in both, all three streams co-realized in one admissible
sector under one common-order prefix structure (SG-NG-20, SG-NG-25).

Φ(x, y) := (A, C).
```

Typed signature: `Φ_B : R_{(·,B)} × R_{(B,·)} ⇀ R_pair`, indexed by the shared stream `B`. The output is not manufactured — `(A, C)` is a pair of streams that already existed in the sector. **WD-PHYS discharged**: `Φ` consults streams and co-realization only; it cannot see `p, q, u, v`.

## 2. WD-CLOSE — exact, and the label emerges

With `q N_A − p N_B = e₁ = O(1)` and `v N_B − u N_C = e₂ = O(1)` on every common prefix `H`, substituting gives

```
qv·N_A − pu·N_C  =  v·e₁ + p·e₂  =  O(1).
```

Verified symbolically; `N_B` cancels identically. So `(A, C) ∈ R_bd` at class `red(pu, qv)`, and

```
ρ_Q(Φ(x,y)) = ρ_Q(x) · ρ_Q(y)                                  (WD-REP, derived)
```

is a **representation theorem** produced by the closure computation, exactly as the framework requires. The bounded-defect structure of C1–C4 already contained multiplication; it was never imported.

## 3. WD-DOM — where it fails, and what survives

**Untyped, WD-DOM fails.** Admissibility of `(x, y)` requires *literal stream identity*: `y`'s first stream must be `x`'s second stream. Take `x' = (A', B') ≡_Q x` with `B' ≠ B`. Then `(x, y)` is admissible and `(x', y)` is not. So `(x,y) ∈ D_Φ ⇎ (x',y) ∈ D_Φ` — admissibility is **not** a function of labels. This is the failure C7C-WD was built to detect, and the reason the "whenever all four compositions are admissible" wording was one condition short: chain composition passes WD-VAL trivially wherever it is defined and still is not an operation on classes.

**Typed by shared stream, WD-DOM holds.** Within the fibre `τ = B` — realizations whose relevant stream *is* `B` — two `≡_Q`-equivalent inputs `x = (A,B)`, `x' = (A',B)` are both composable with any `y = (B, C)`. So `Φ_B` is domain-congruent on its own fibre, and by §2 both outputs `(A,C)`, `(A',C)` carry `red(pu,qv)`: **WD-VAL holds fibrewise.** WD-DESCENT therefore gives, for each shared stream `B`, a well-defined partial operation on the fibre's classes.

**What descends globally is weaker than a total operation.** Across fibres the *output label* is always `rs` (§2), so the label-level rule is consistent — but the domain is existential over realizations:

```
r ⊙ s  is defined  ⟺  ∃ x carrying r, y carrying s, with a shared co-realized middle stream,
r ⊙ s  = rs  whenever defined.
```

This is a **witness relation** `W_× = {(r, s, x, y, B)}` with `r ⊙ s` its label projection — the same architecture as `Q^dyn`, and for the same reason: the physical content lives in the realizations. Whether `r ⊙ s` is defined for *every* pair of currently established labels is a **realization question**, not a design question, and is deferred.

## 4. Laws — what the realization level gives for free, and what it refuses

| law | realization level | label level |
|---|---|---|
| associativity | **free**: `((A,B)(B,C))(C,D) = (A,D) = (A,B)((B,C)(C,D))` as pairs | inherited |
| commutativity | **fails**: `(B,C)·(A,B)` is admissible only if `C = A` | `rs = sr` holds, but only as WD-REP, not as a physical law |
| identity | `(B,B)` is **not in `R_pair`**: one stream compared with itself is not two independent event types (SG-NG-20) | label `1` exists (N5-PHYS-1, DISC-2), but not as `(B,B)` |
| inverse | `(A,B)·(B,A) = (A,A)`, excluded for the same reason; C7C-0 gives `ρ_Q(Sx) = ρ_Q(x)⁻¹` but the *composite* is not a realization | `r · r⁻¹ = 1` is not physically closed by this construction |

So the chain product yields a **partial associative composition on realizations** with a derived multiplicative representation — not a group and not a semigroup with identity. The label-level structure looks like `(ℚ₊, ·)`; the physical structure that produces it does not. That gap is the finding, and it is the correct outcome for a WD analysis: the framework was supposed to expose exactly where numeral-arithmetic outruns the physics.

## 5. Two guards worth stating now

1. **Ray-multiplicity chains are controls, not evidence.** In the continuous dyad, `(B₊∪B₋, C₊)` at `2:1` and `(C₊, B₊)` at `1:1` chain to `(B₊∪B₋, B₊)` at `2:1` — consistent with §2 and useful as an operator control (like C5-SYN-13), but SG-NG-26 applies: it verifies the mechanism, not a dynamically contentful product. Any C7C-M realization campaign must state what would make a chained triple *non-trivial*, before looking.
2. **No composability across the branch firewall.** `1` has realizations in both the continuous dyad and TDR-G; those cannot share a stream, so their labels are never composable with each other through `Φ`. The label `1` is one thing; its realizations are not interchangeable inputs. This is WD-DOM biting in exactly the case Appendix B now rejects.

## 6. Proposed obligations for C7C-M closure (to be frozen before any search)

- **M-1** `[ALG]` closure and label emergence: §2, ready to certify now.
- **M-2** `[ALG]` fibrewise WD-DOM/WD-VAL/WD-DESCENT: §3, ready to certify now.
- **M-3** `[DEF]` register `W_×` and the partial label operation `⊙` with existential domain.
- **M-4** `[OPEN, realization]` exhibit at least one chained triple `(A,B,C)` of co-realized certified streams in one sector with **both** legs non-trivially bounded — i.e. not a common-source multiplicity artifact of a single lift (SG-NG-26 discharge required per leg). Pre-register what counts before any enumeration.
- **M-5** `[OPEN]` laws: state explicitly that identity and inverse do **not** close under `Φ` at the realization level; if a physical identity is wanted, it must come from a *separate* certified `1:1` pair sharing streams with the operands, not from `(B,B)`.

## 7. Non-claims

No claim that `Q_RTG^bd` is closed under multiplication — only that a partial, fibrewise well-defined composition exists whose label representation is multiplicative wherever defined. No claim about `Q_RTG^dyn`. No claim of a group, monoid, or field structure. No realization is exhibited.
