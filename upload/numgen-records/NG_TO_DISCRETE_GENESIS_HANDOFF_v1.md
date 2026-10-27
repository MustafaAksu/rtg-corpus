# Number Genesis → Discrete Genesis — Owner Handoff

**Memo ID:** `NG_TO_DISCRETE_GENESIS_HANDOFF_v1` · **Date:** 2026-10-01
**From:** Number Genesis owner stream · **To:** Discrete Genesis (TDR-G) owner
**Pins:** Number Genesis v1.20.7 `c4637e7a…fab28` (freeze manifest `b06fd02b…dbef`) · Discrete Genesis DSN v2.12.13 `aa232643…053f` · TDR-G owner code `genesis_mode_b_mc_v18.py` `9d787b43…675e`
**Related:** `NG_TO_TDRG_REPRODUCIBILITY_GAP_v2.md` (`6c7865c2…`) covers the BIND3 reproduction-contract gaps and is not repeated here.

---

## 1. Required owner rulings

### 1.1 P2 — antipodal-endpoint orientation policy
In the two-defect path rule, orientation uses `endpoint_d = signed_centered(δ[path_end] − δ[path_start], N)` (v18 L622), with `signed_centered` returning a value in `(−N/2, N/2]`. At the antipodal value `|endpoint_d| = N/2`, both presentations of the same path yield `+N/2`, so the orientation is **not presentation-covariant** there.

**Requested ruling:** the canonical owner semantics at the antipodal endpoint. The options considered so far are: v18 as is; reverse; inert. The ruling may also choose another option, or state that presentation covariance is not required. A ruling of any kind unblocks Number Genesis.

### 1.2 RF-06 — state/gauge statement in §6.1
§6.1 defines a state that carries phases `θ_i` **and** velocity tokens `δ_i` (L521) and a relative advance `d_ij` (L525), but L523 states *"Only `Δ_ij = (θ_i − θ_j) mod N` are physical."* Read literally, that sentence makes the physical state phase-only.

**Requested ruling:** reconcile L523 with the defined state. The facts on record:
- the global-phase quotient is the only unrestricted gauge;
- the transition state also carries tokens / relative advances (OFN v0.8 SG-OFN-STATE);
- a common token shift is not a gauge of the star rule (OFN v0.8 `RTG-OFN-ALG-STAR-TOKEN-SHIFT`: fixed-star covariance iff `2c = 0`);
- on the no-birth SWAP/P3 route the rule is equivariant under every common token shift.

This is a **source-text correction only**. Number Genesis v1.20.7 already carries a scope note at its import of §6.1 (L72); the source wording belongs to this owner.

## 2. Why Number Genesis is waiting

- **M-4 is on HOLD pending §1.1.** The first realization search for the composition programme (C7C-M, M-4) runs on the SWAP/P3 implementation, whose orientation at the antipodal endpoint is exactly the open point (NG v1.20.7 L2030).
- **Frozen DISC and M2 results are not changed retroactively.**
  - DISC-1: 0/22 witnesses touch the antipodal condition.
  - DISC-2: 40/136 are exposed; every admitted label keeps at least one unexposed witness, and the label set is unchanged under the reverse and inert alternatives.
  - The C7C-M2 Census-1 excluded the 40 exposed records by a preregistered quarantine. Its outcome is INCONCLUSIVE / INCONCLUSIVE, decided on unexposed or continuous-dyad evidence.

  A P2 ruling therefore governs **future** campaigns. Any change to past records would be a new owner patch on the Number Genesis side, not a reinterpretation.
- **RF-06 does not affect the DISC route.** DISC runs on the no-birth SWAP/P3 route, where the phase-and-token-difference key is legitimate. This follows from reading the pinned v18 transition and is corroborated by a finite spot check (`NG_SELFCHECK_REFERENCE_TRANSPORT_v1`). The request in §1.2 concerns the general statement, not any Number Genesis result.

## 3. Forward-looking request — a ruling, not a campaign

Number Genesis's open composition question needs, in one certified sector, **three** independently certified, co-realized event predicates. Currently only SWAP and P3 are registered for TDR-G in the frozen M2 key registry (`κ_b`). The frozen enumerators also label two further tick classes:
- **`tie`** (DISC-1 `'tie'`, DISC-2 `'T'`): a balanced two-defect tie under `bound_symmetric`; the tick is inert (no state change);
- **`triangle`** (DISC-1 `'k3'`, DISC-2 `'K'`): a three-edge defect component; the tick is inert.

These are **enumerator-level telemetry only**. They are not owner-certified event predicates and not certified interface types in `κ_b`.

**Requested ruling:** whether any event predicate beyond SWAP and P3 — including, but not limited to, these tick classes — **can** be promoted to an owner-grade event predicate in the same TDR-G sector (`N = 24`, three-node Mode-B, `k = 1`, v18 conventions). If so, under what exact owner definition: event semantics, independence from SWAP and P3, and presentation covariance. Number Genesis requests no particular outcome. A negative ruling is equally informative, and nothing here opens a campaign; M-4 stays on HOLD until §1.1 is ruled.
