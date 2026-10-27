# Number Genesis self-check against the Reference-Transport Audit (30 Sep 2026)

**Doc ID:** `NG_SELFCHECK_REFERENCE_TRANSPORT_v1` · **Class:** noncanonical review; no owner file changed.
**Base:** Number Genesis v1.20.6 (`2a51c4b1…48c5`), C7C-M2 preregistration (`248f128c…8987`) and census artifacts.

## 1. Audit findings that touch this stream
| audit key | touches Number Genesis? | status here |
|---|---|---|
| RF-06 phase-only / token-origin gauge | **yes** — L68 §1.1 row-1a `[DEF]` import: "physical states are quotiented by global phase shift, and relational phase differences are primary" | wording needs a scope note (§3); DISC route itself is sound (§2) |
| RF-08 stale consumer snapshots | yes, as coordination | already handled: v1.20.5 recorded RECOG v0.3.5 repin; Dyadic consumer rows left to the Dyadic stream |
| RF-07 reference-transport contract | indirectly — C7C-M2 uses comparison-context transports | consistent: M2 witnesses align comparison contexts only (G-bridge); no gauge or physical-transport claim is made |
| RF-01…05 (RECOG, GEN, TRIAD, OPEN M formulas) | no live import of the affected formulas | none |

The audit itself lists Number Genesis as preserving the residue (logarithmic defect, non-fixed re-blocking, GAP-LOCK, SG-NG-24) with only the RF-06 shorthand outstanding. The self-check below confirms that at the level of the live text.

## 2. RF-06 on the DISC route — spot check (finite sample, not a proof)
The owner rule's star blow-up sets `delta[center] = -old_d` (v18 L684): not equivariant under a common token shift, matching OFN `STAR-TOKEN-SHIFT`. DISC, however, runs on the 3-node BIND3 route, whose operations are phase advance, SWAP (a permutation, L639), P3 path-cycle (a permutation, L664–667) and path orientation by token **differences** (L622). Test with the pinned owner code (`ng_rf06_token_shift_spotcheck_v1.py`): k = 0..3, 2,500 random states each, every common shift `c = 1..23` — **230,000 shifted steps, 0 reduced-key mismatches, all absolute tokens shifted by exactly `c`, 0 star/birth steps.**

Consequence: the DISC cycle key — the gauge-reduced 4-tuple of phase and token **differences** — is a legitimate state key on that route, and the `δ_A = 0` lift used in the P2 exposure audits is harmless there. The token-origin non-gauge of RF-06 bites on star/birth steps, which the DISC route does not reach. This also backs the TDR-G gauge entry of the frozen M2 `κ_b` registry ("global-phase quotient; cycle key in the gauge-reduced 4-tuple").

## 3. Self-check of the live text against the audit's five criteria
| criterion | finding in Number Genesis v1.20.6 |
|---|---|
| 1 linear vs nonlinear closure | clean — the only "exact return" (L920–929) is explicitly conditional and shows that an exact return would retain distinguishing memory |
| 2 `T^6` is grouping, not reset | clean — no reset / heal / repair of dynamics (the three "repair" hits are methodological) |
| 3 gauge quotient needs well-defined dynamics | clean — SG-NG-17 demands dynamical equivariance; `G_adm` is an invertible groupoid; **except the L68 shorthand (RF-06)** |
| 4 raw vs odd vs NF vs averaging | clean — SG-NG-18 separates `37/40` (raw ray burst with the `−(5/24)Q^(5/2)` term) from `47/54` (raw fixed-radius uniform-angle mean); the cyclic-average theorem (L1484) declares its operation; L2109 already corrected the `O(Q²)` hypothesis to the quartic `Q^(3/2)` angular term |
| 5 event ≠ residual ≠ reference | clean — N-1 repeats an event type; SG-NG-24 forbids discarding the certified discrepancy |
| RF-03 scalar laws | clean — L-BACKBONE (L2113) and L1 (L2785) state `q' = q − q² + O(q^(5/2))` for the typed `Q_true`, uniformly in phase; this matches the raw half-power term the audit computes, and makes no `Q³`-order autonomous-closure claim |

## 4. Recommended repair (for a future owner patch, not applied)
Row 1a (L68) is a verbatim `[DEF]` import of Discrete Genesis §6.1, and the defect originates at the source (audit RF-06 → TDR-G L523). Under K4 the import keeps the source's text, so the repair is a **scope note**, not a rewrite:

> *Scope (RF-06):* the global-phase quotient is the only unrestricted gauge. The TDR-G transition state also carries tokens / relative advances; state completeness follows OFN SG-OFN-STATE. A common token-origin shift is **not** a gauge of the star rule (OFN `STAR-TOKEN-SHIFT`). On the 3-node SWAP/P3 route used by DISC, the rule is equivariant under every common token shift (finite spot check), so the DISC phase-and-token-difference key is a legitimate state key there.

The source-side correction belongs to the Discrete Genesis owner.
