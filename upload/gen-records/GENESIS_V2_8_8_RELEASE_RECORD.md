# Genesis Geometry v2.8.8 — Release Record (maintenance)

**Date:** 19 October 2026
**Owner decision:** Adopted by Genesis stream owner decision, 19 October 2026, following the independent Genesis v2.8.8 receiving review (11/11 PASS in --final mode, 0 SKIP); scientific payload unchanged from the reviewed draft.
**Status:** v2.8.8 is the adopted Genesis owner file from this release. v2.8.7 is superseded and kept unchanged as history.

## Identities

| Object | SHA-256 |
|---|---|
| Baseline: adopted v2.8.7 | `d5d1e57c6eea0800cf8bf3e3f6b5905873e719df0969d15144ca55197cd2e361` |
| Reviewed draft `RTG_GENESIS_GEOMETRY_DSN_v2_8_8_DRAFT.md` | `4dcf0185ab14815e34e06eb35dd52616d74cbf91726ff96e62f616c84923f884` |
| **Adopted release `RTG_GENESIS_GEOMETRY_DSN_v2_8_8.md`** (1581 lines) | **`9abd36169a4bf6056318605c0399ff1f91c53f157b9181bdbfdb9faed3000f37`** |
| Upstream: adopted Dyadic v6.4.13 | `5958f7fe8a3e0ec94546cb7e915c5f690d09827a3d680d13a17c9d880b968542` |
| Draft package (receiving review) | `bea4cd5034be39055266f9da2a7a2cfeaf71e67c57014b0b150f2df7c0cd9ba0` |
| Adoption kit (owner-verified) | `295462360dc8c7284e5153803d577b2987a83ecc0954513fe9a36353c4d68f68` |
| `release_v2_8_8.py` / `check_release_v2_8_8.py` | `c374f3cc…843d` / `5e9e8876…f48f` |
| Release checker output | `71b579be323b5c8f040a8802ba6243dc6177e8475e00074404f6c7dc54282b85` |
| Manifest v0.1 / occurrence disposition v0.1 | `81939e5f…f542` / `72bd4e46…` |
| Draft build / draft checker | `0b2270bb…c352` / `eb1f3bb4…8435` |
| Consumer record / consumer checker / ν₅ replay | `1e412c43…38d1` / `db9000ce…bfad` / `34bab140…61cb` |

## Chain

1. **v2.8.7 → draft.** 18 rule-authorised edits. Draft checker with `--final --dyad --replay`: 11/11 PASS, 0 SKIP, on the adopted Dyadic v6.4.13 bytes (independent receiving review).
2. **Draft → release.** 7 metadata edits. Release checker R1–R8: **8/8 PASS**, exit 0.
3. **Cross-check against v2.8.7.**
   - §6.3a–§6.3b, SG-15 and SG-16 are byte-identical.
   - Claim-tag counts and the GEN RID set are identical.
   - The only added DYAD RID is `DYAD-ALG-NU5-P5`.
   - No live v6.4.11 or v6.4.12 pointer remains outside the historical anchors.

## In force from this release

- **D5:** live Dyadic source pins name adopted v6.4.13. Statements dated to v2.8.6 that name v6.4.11 are retained as history.
- **M2c: CLOSED.** The §6.2 ν₅⁽⁵⁾ closed form is unchanged. It now carries `DYAD-ALG-NU5-P5` and `[conv: one-step NF, declared K_5 family, frame W_p, resonant h=0]`.
  - The exact certificate is Dyadic-owned (`dyad_m2c_nu5_p5_exact.py`).
  - The Genesis replay (`genesis_nu5_p5_replay.py`) remains [NUM] only.
- **Unchanged:**
  - `GEN-THM-K3-PLANAR-FACTOR-NOGO`, `GEN-THM-K3-SIXSTEP-FACTOR-NOGO`, `GEN-THM-MEANFEEDBACK-SIXSTEP-NOGO`, `GEN-THM-CHIRAL-CUBIC-FACTOR-LEMMA`, `GEN-DEF-MEANFEEDBACK-FAMILY`;
  - SG-15 and SG-16.
- **Not imported:** the formal ℤ₆ generator, Lemma F and F1–F3.
- **Open:** physical G2, OPEN-B/E1, γ selection.

## Outbound notices (issued now, citing the adopted hash `9abd3616…0f37`)

**→ Dyadic (N8) — Genesis consumer acknowledgement**
- **Status:** RECEIVED.
- **Consumer:** Genesis Geometry v2.8.8, adopted (`9abd36169a4bf6056318605c0399ff1f91c53f157b9181bdbfdb9faed3000f37`).
- **Upstream:** Dyadic Oscillator v6.4.13, adopted (`5958f7fe…8542`).
- **Checks:**
  - consumer checker on the adopted v6.4.13 bytes: 8/8 PASS;
  - Genesis independent numerical replay of ν₅⁽⁵⁾: 4/4 PASS [NUM];
  - draft checker `--final --dyad`: 11/11 PASS.
- **M2c: CLOSED.** `DYAD-ALG-NU5-P5` is cited at the point of use with its normalization convention.
- **N1/N2 and D5:** the repin to v6.4.13 is executed for all live Genesis pointers. All 13 cited DYAD RIDs and the cited values were verified upstream.
- **Scope:** the formal ℤ₆ generator, Lemma F and F1–F3 are not imported into the Genesis network maps. Edgewise J^{×3} and R₀^{×3} do not preserve 𝒞 beyond linear order (consumer record v0.1 §4). Physical G2, OPEN-B/E1 and carrier selection remain open.
- **Dyadic-side housekeeping (Dyadic owner's action):** the "Consumer editions inspected" line may now pin Genesis v2.8.8, and N8 may be marked ANSWERED.

**→ RRF (G2-CLOCK).** Informational.
- Genesis v2.8.8 (`9abd3616…0f37`) is a maintenance release.
- `GEN-THM-K3-PLANAR-FACTOR-NOGO`, `GEN-THM-K3-SIXSTEP-FACTOR-NOGO` and `GEN-THM-MEANFEEDBACK-SIXSTEP-NOGO` (the last only with (H_spec)) are byte-identical to v2.8.7, and their exports are unchanged.
- Citations of v2.8.7 remain valid; they may be repinned to v2.8.8 at RRF's convenience.

**→ FMS / OFN.** Informational.
- The K3/6S owner results and SG-16 terminology (γ, 𝒟, tangent to 𝒞) are unchanged.
- M2c is closed.
- The Dyadic v6.4.13 results (J, Lemma F, F1–F3) are not imported by Genesis. They remain Dyadic-owned, at the scope set in Dyadic notice N9.
