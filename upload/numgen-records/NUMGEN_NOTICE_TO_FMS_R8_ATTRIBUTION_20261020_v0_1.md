# Number Genesis → FMS — Attribution notice on R8

**Date:** 20 October 2026 · **From:** Number Genesis owner side (Claude, DSN editor/auditor). Co-owner GO 20 Oct 2026; the PI dispatches. · **To:** FMS editor
**Status:** `[SESSION]` notice. No owner file is modified. No import and no reply is requested beyond a correction line.

**Item.** `FMS_MODEL_SELECTION_LEDGER_v0_6_4_SESSION.md`, §2 results register, row R8:

> "κ=0 relative holonomy limit `|h_m|/√N_m → L ≥ 0`, with `|h_m| → 0` — conditional local theorem (NUMGEN/DYAD provenance)."

**Finding.** `RTG_NUMBER_GENESIS_DSN_v1.20.7` (`c4637e7a…ab28`) does not contain this statement. The owner text was searched for `h_m`, `N_m`, `relative holonomy` and `κ=0`, with no match.

NUMGEN's nearest holonomy content is different:
- NG-7A is an operator and zero-control result: `C·Dᵀ = 0`, with node-difference `Z_N` data flat.
- NG-7B is an OPEN physical-source layer.

Neither gives a limit law of this form.

**Request.**
- Remove "NUMGEN" from the R8 provenance, or replace it with the actual source if FMS can identify one.
- If the result is FMS's own session derivation that uses NUMGEN or Dyadic inputs, please name those inputs by RID.

NUMGEN does not comment on whether R8 is true. Dyadic has been informed separately, because the same label also names Dyadic (`NUMGEN_REQUESTS_TO_DYAD_20261020_v0_1.md` §4).
