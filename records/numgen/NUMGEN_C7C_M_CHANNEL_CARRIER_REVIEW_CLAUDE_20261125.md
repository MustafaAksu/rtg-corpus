# NUMGEN C7C-M three-channel carrier — co-owner review (Claude)

**Date:** 25 November 2026.
**Status:** [SESSION] co-owner review. It is not an owner claim, an adoption, a preregistration or a campaign authorization. No DSN, RID or frozen-evidence change.

**Reviewed:** `records/numgen/NUMGEN_C7C_M_CHANNEL_CARRIER_20261125.md` and its exact check, PR #386, head `8194c75`.
- Script `c5a729ae…f84d`.
- Output `a556a8f7…84c7`.

**Sources:** `numgen-v1.22` (`36b31755…d40b`):
- the primitive map;
- SG-NG-20 and SG-NG-26;
- L-MONO, L-PHASE, INF-1/2, N5-PHYS-1 and WD-CLOSE;
- the frozen `NG_C7C_M2_PREREG_DRAFT_v4.md`, §§2 and 10.

## 1. Verdicts

| Part | Verdict |
|---|---|
| §2 same-instance outer self-collision | **ACCEPT** (conditional THM). A useful negative control. |
| §3 six directed predicates: counts, cofinality, "occurs alone" | **ACCEPT** (conditional). The h-strip argument checks. |
| §4 no global fixed-step translate | **ACCEPT as stated**, i.e. as an identity of predicates on a whole local neighbourhood. The jet table was reproduced by an independent route. See §3 below for its weight. |
| §5–6 conditional WD-DOM PASS on the channel-typed domain | **Correct, but not informative as a test.** The domain is saturated by construction (§4 below). |
| A*: physical admission of M_± and H_± as independent event types | **Not supported by this review; I recommend against it in this form.** On a real orbit the channels are almost exactly fixed-step translates of P (§3). |
| Campaign | none. M4 HOLD; Census-1 INCONCLUSIVE / INCONCLUSIVE; DISC-3 DEFER; full-interface WD-DOM OPEN. |

## 2. What was checked

**Replay.** `python3 -I channel_carrier_exact_check.py` (Python 3.13.18) reproduced the author's output byte-identically: `author_check_replay_output.txt`, `a556a8f7…84c7`.

**Independent jet route.** `jet_sympy.py` uses SymPy 1.14.0, truncates at `t⁴` after every primitive step, and asserts that each source point lies on its own zero curve.
- It reproduces all 30 leading terms of the §4 table exactly: `jet_sympy_output.txt`, `f1a00b58…7c9a`.
- The cubic-coefficient argument for `m = k + 6ℓ` holds. F = T⁶ has no quadratic term, and its cubic term `W|W|²` commutes with the rotation. So the ℓ-fold correction adds `±(2/√3)·τ·ℓ = ±4ℓ/3` to a leading cubic coefficient. Every tabulated cubic coefficient has `0 < |c| < 4/3`.

**Channel identities.**
- `h = e^ρ − 1 − sin η` equals `(2/√3) r cos(Θ + π/6) + O(r)`, giving zero rays at `π/3` and `4π/3`.
- The six rays are 0, π/3, …, 5π/3 in the order (P₊, H₋, M₋, P₋, H₊, M₊). Verified.

**Strip argument (§3).**
- Strip width `2ε = π/24 < π/6`, so at most one state lies in a strip on any passage.
- The certain-sign arcs have length `π − 2ε > π/2`, so no step skips one.
- Checked case by case for an intermediate state that is positive, zero or negative: there is exactly one directed token per passage.

**§2 self-collision.** Correct. An equivalence that forgets the crossing direction, on a domain that admits same-channel outer pairs, produces `(B₋, B₋)`. That pair is excluded by SG-NG-20, as the owner already uses it at WD-CLOSE.

## 3. Main finding: the three channels are one observable read at consecutive primitive steps

**Linear-order identities.** The exact map gives:
- `η(Tx) = ρ(x) + ρ²/2 + O(3)`;
- `h(x) = ρ(Tx) + (e^ρ − 1 − ρ) = ρ(Tx) + ρ²/2 + O(3)`.

To linear order, therefore:
- the M observable is the P observable one step later;
- the H observable is the M observable one step later.

The six rays are spaced by exactly π/3, which is the rotation angle of T's order-6 elliptic linearization. The six directed predicates are thus, to linear order, the six phase offsets of the single section B₊ under T. They differ only by the nonlinear corrections that §4 tabulates.

**On a real orbit** (`lag_stats.py`, `fd250c7e…05be`; output `e896df95…31ff`):
- Run: mpmath 1.3.0 at 30 digits, 120,000 primitive steps from the canonical seed `(1/100, 1/250)` in `U_D,base`.
- `[NUM]`, not a proof input. No seed or ray was selected.

| Predicate | Exact fixed-lag translate of the P₊ token |
|---|---|
| H₋ at `n+1` | 19999/19999 (100 %) |
| M₋ at `n+2` | 19948/19999; lag 1 in 51 cases |
| P₋ at `n+3` | 19948/19999; lag 2 in 51 cases |
| H₊ at `n+4` | 19948/19999; lag 3 in 51 cases |
| M₊ at `n+5` | 19999/19999 (100 %) |

On this prefix:
- **H₋ is exactly the one-step translate of P₊ (= B₊)** on every occurrence.
- M₊ is exactly the five-step translate of P₊. Equivalently, P₊ is the one-step translate of M₊.
- The other channels deviate only at the sparse slips that §4 and #383 P2 describe.

§4's predicate-level result is true: the zero curves differ at O(t³). But the mismatch wedges have angular width O(q), and the orbit enters them only rarely. The record itself says that §4 is not an orbit-by-orbit theorem.

**Consequence for A*.**
- SG-NG-20 excludes "blockings or re-indexings of the one certified generator T". Along orbits, the M and H channels are such re-indexings except at a sparse set of steps.
- The owner admitted B₊ and B₋ as distinct (N5-PHYS-1). That precedent rests on two opposite relational-coincidence sections, not on reading one section at a later step.
- I do not think the count, noncoincidence and fixed-translation results carry A* for M_± or H_±.
- A positive case would need an argument that the channels are independent *as physical event types*, despite being one observable at consecutive steps. I do not see such an argument in the record.
- This also bears on #383's C_r = M₋ (the two-step translate, 99.74 %). It strengthens the SG-NG-26 reading in my #384 review: these are multiplicity / phase controls at most.

## 4. The §6 WD-DOM PASS is saturated by construction

The typed domain admits a chain only when the three native channels are pairwise distinct. Channel is a key component, and A* admits **every** cross-channel pair to `R_cross`. So, for any equivalent replacement:
- the outer pair is cross-channel by key;
- it is therefore in `R_cross` by A*;
- Π is determined by key data.

WD-DOM then cannot fail on this domain. The PASS is a property of the definitions, not evidence about physical composition. The frozen instrument keeps Π outside every equivalence and requires independent `R_pair` provenance (prereg §2, G-bridge). The record correctly presents §6 as a new instrument, not a retuning of M2. Even so, it should state plainly that its WD-DOM PASS is definitional, given A* and the key.

The non-unit control `2 × ½ = 1` uses both-direction readouts. It is a readout-multiplicity identity under SG-NG-26, as the record itself says.

## 5. Recommendation

- Keep §2 (the self-collision lemma) and the §3–4 mathematics as conditional [SESSION] results. They are correct.
- **Do not take A* (M_±, H_±) to the PI as an admission candidate in this form.** The orbit-level translate structure (§3) is the decisive obstacle under SG-NG-20.
- If the channel route continues, the next step is analytic: either an argument for physical independence that addresses near-translate structure, or a decision that channel composition is only a machinery control, with no WD-DOM evidential weight.
- No campaign is needed. M4 stays HOLD.

**Files**, in `evidence/numgen/c7c_m_channel_review_20261125/`:
- `jet_sympy.py`: `4ac1f409…db34`;
- `lag_stats.py`: `fd250c7e…05be`;
- `author_check_replay_output.txt`: `a556a8f7…84c7`;
- `jet_sympy_output.txt`: `f1a00b58…7c9a`;
- `lag_stats_output.txt`: `e896df95…31ff`.

## 6. Addendum (25 Nov 2026, evening) — review of #386 §9 (head `636e415`)

**Reviewed:** #386 §9, record file `36daca8f…d9e6`.

**§9.1 delay-coordinate identities: ACCEPT.** Each identity follows in one line from the map, and the logarithm's argument is `e^ρ > 0`. The record itself limits the scope correctly. For NUMGEN's map the two-sample observation `(η(x), η(Tx))` is injective on the tube, and every local observable is a function of it. (Erratum, 26 Nov 2026: I first wrote that this holds for every invertible planar map. It does not: the identity map is a counterexample, and injectivity of the delay map is required. #386 comment `7174411169`.) So the identity alone does not discriminate between event types; the near-translate structure is what matters.

**§9.2 bound `J_k = O_x(√N)`, and `O_x(log N)` for k = 1, 5: ACCEPT** (conditional on the common tube). Steps checked:
1. **Linear part.** `g_k = η + O(|W|²)` with unit linear coefficient. For example, for k = 1: `h(Tx) ≈ −η`, normalised to `η`.
2. **Strip width.** A mismatch needs an endpoint in `{sign g_k ≠ sign η}`. This set has width `O(|W|²)` in η, i.e. angular width `O(r)`.
3. **Cubic case.** For k = 1, 5 the reviewed table has cubic entries on both rays (`±t³/6`, `∓7t³/6`). The width therefore drops to `O(|ρ|³)` in η, i.e. angular `O(r²) = O(q)`.
4. **Residues.** Using each residue's own `D_(m,s)` with increments `τ/m + O(m^(−3/2))` is consistent with L-BACKBONE, L-PHASE and INF-1.
5. **Dyadic count.** On a dyadic block `[J, 2J)`, D advances a bounded amount and so meets O(1) strips. Visits per strip are `O(1 + J^(1−α))`. Summing gives `O(√N)` for α = 1/2 and `O(log N)` for α = 1.

The proof is correct as written.

`[NUM]` consistency check (`jk.py` `266cef1b…0d42`, output `a9524b4f…2602`): same canonical seed, mpmath at 30 digits, no selection.

| N | J₁ | J₂ | J₃ | J₄ | J₅ |
|---|---|---|---|---|---|
| 75,000 | 0 | 102 | 102 | 102 | 0 |
| 150,000 | 0 | 102 | 102 | 102 | 0 |
| 300,000 | 0 | 262 | 262 | 262 | 2 |
| 600,000 | 0 | 262 | 262 | 262 | 2 |

- Growth is intermittent: it happens once per passage of D through a strip.
- `J/√N` stays bounded (≈ 0.37 at 75,000; ≈ 0.48 at 300,000).
- J₅ shows its first, logarithmically rare mismatches.

**Correction to my §3 (owned).** I wrote that the B_± precedent "rests on two opposite relational-coincidence sections, not on reading one section at a later step". That overstated the contrast. To linear order, `P₋` is `P₊` read three steps later (rotation by π), and `J₃` grows like `J₂` and `J₄` in the table. So B₋ is itself a near-translate of B₊ in the §9.2 sense.

The difference from M and H is only the owner's adopted relational semantics for B_±: opposite radial sign at phase coincidence. That pair is used as a positive control (SG-NG-26), not as dynamic breadth. #386 §9.2 states this correctly. My conclusion is unchanged: withhold A*. The §3 contrast should be read as "no owner semantics has been adopted for M and H", not as a structural difference.

**§9.3 static P4 fixture: verified with the pinned engine** (`p4_fixture.py` `7e78b790…c14e`, output `c7653184…137a`).
- The v18 engine (`9d787b43…`) with the `tdrg-v2.13` reference orientation (`ca59e9b9…`) was run from pre-advance θ = (0,12,23,9), δ = (0,1,3,6), N = 24, k = 1.
- Under both `bound_symmetric` and `bound_path_tie` it gives post-advance θ = (0,13,2,15) and δ′ = (6,0,1,3), with one path interaction, no tie and no birth.
- The signed defect errors are −1, −1, −1 along 0–1–2–3; the remaining errors are 10, 10 and −3. This matches the record.

As the record says, this is one step only: no invariant sector, no recurrence, no co-realization.

**§9.3 direction: AGREE.** Move to owner-native support-distinguished TDR-G events (SWAP / P3 / P4), with the four gates (i)–(iv) set *before* any search.
- Gate (i) needs TDR-G owner confirmation of support-sensitive event predicates. That request belongs in `pipes/TDRG/`, and it should be filed before NUMGEN designs further.
- The four-node sector inherits TDR-G's own questions: births are possible for K₁,₃ / star configurations, and multistar policies apply. A birth-free invariant sector has to be proved, not assumed.

M4 HOLD; DISC-3 DEFER; Census-1 INCONCLUSIVE / INCONCLUSIVE; full-interface WD-DOM OPEN.

*END OF RECORD.*
