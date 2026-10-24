# Genesis Geometry v2.8.7 — Release Record

**Date:** 18 October 2026
**Owner decision:** Adopted by Genesis stream owner decision, 18 October 2026, following the independent Genesis v2.8.7 receiving review (17/17 PASS in --final mode, 0 SKIP); scientific payload unchanged from the reviewed draft.
**Status:** v2.8.7 is the adopted Genesis owner file from this release. v2.8.6 is superseded but kept unchanged as history.

The gate counts (17/17 draft, 8/8 release) certify source integrity, determinism and scope. The theorems rest on their proofs: §6.3a.1 and §6.3b, from proof record K3-6S v0.3.

## Identities

| Object | SHA-256 |
|---|---|
| Baseline: adopted v2.8.6 | `294c6fc26482d7deae42900cb50b3029ac81e96d66e239bfe8b797e95fdaa269` |
| Reviewed draft `RTG_GENESIS_GEOMETRY_DSN_v2_8_7_DRAFT.md` | `81a9bd9c954f6e71d47e2cb28a9417f6dd27b51fe6132b2efe72134bf3ea7a22` |
| **Adopted release `RTG_GENESIS_GEOMETRY_DSN_v2_8_7.md`** (1564 lines) | **`d5d1e57c6eea0800cf8bf3e3f6b5905873e719df0969d15144ca55197cd2e361`** |
| Draft package (receiving review) | `114ff19b27a121ab15f5d0714651cf738027998fe6e9b06f8692d4386646d4c7` |
| Adoption kit (owner-verified) | `6490922e049a42d97bf4107518b4fedfadef6cf00fef32860d57e8a588a306d6` |
| Release transform `release_v2_8_7.py` | `eecc8eb0d2bdf61d71453eb16c7c7e9c423b7c540daad891a2b42302606aa2aa` |
| Release checker `check_release_v2_8_7.py` | `d28ee2df5b2f5c5ade6c77b1c36df382a8a9bd0d080549a8c395e28f43d903fc` |
| Release checker output | `c2b626674f03d4cc0cc98bc4db59d7f2b9335d5a822c3005239a920ed05aaa2e` |
| Manifest v0.1 / occurrence disposition v0.1 | `7519e14f…135a` / `e5f27795…b07e` |
| Draft build / draft checker / draft checker output | `8e623c62…e3f2` / `f6af52b3…d802` / `614ec28a…df7` |
| Proof record K3-6S v0.3 | `049e313e4f07ffe5e576018426a5776aab9b602b0c5c55ef286c71d750babc9e` |

## Chain

1. **v2.8.6 → draft.** 13 declared edits. The draft checker passed 17/17 in `--final` mode with 0 SKIP, here and in the independent receiving review; the stdout is byte-identical in both.
2. **Draft → release.** 19 metadata edits; release checker **R1–R8: 8/8 PASS**, exit 0.
   - The reverse transform recovers the draft byte-exactly.
   - Claim-tag counts are identical.
   - Every changed live line is metadata (34 lines).
   - No draft marker remains in live text.
   - The RID set is unchanged.
   - The Gröbner script status is unchanged.
   - The adoption text is the owner's exact wording.
3. **Cross-check against v2.8.6.**
   - §6.3a and SG-15 are byte-identical.
   - New GEN RIDs are exactly the four authorized.
   - No κ appears in added text.

## Scope (unchanged from the reviewed draft)

**Adopted:**

| RID | Grade | Scope |
|---|---|---|
| `GEN-THM-CHIRAL-CUBIC-FACTOR-LEMMA` | `[THM]` | real-linear factors of the chiral cubic, branch c−iβ ≠ 0, β ≠ 0 (§6.3a.1) |
| `GEN-THM-K3-SIXSTEP-FACTOR-NOGO` | `[THM]` | raw projected K₃ on 𝒞; E∘F₁⁶ = T′∘E; C³; d = 1, 2, 3; **no hypothesis on T′** |
| `GEN-DEF-MEANFEEDBACK-FAMILY` | `[DEF]` | F_γ on ℝ⁶; carrier 𝒞, mean mode 𝒟 (§6.3b) |
| `GEN-THM-MEANFEEDBACK-SIXSTEP-NOGO` | `[THM]` conditional | γ ∈ ℝ∖{0,2}; C³; d = 1, 2, 3; **only under (H_spec)**: (1−γ)⁶ ∉ spec DT′(E(0)) |

Supporting content, each without its own RID:
- `[ALG]` exact cubic data (c_γ, β_γ);
- `[ALG]` primitive-clock family statement at C³ under (H_prim): (1−γ)λ ∉ spec DT′(E(0));
- SG-16.

**Unchanged:** `GEN-THM-K3-PLANAR-FACTOR-NOGO` keeps its scope and grade, and its v2.8.6 RRF export stands.

**Open / excluded:**
- physical γ selection;
- OPEN-B/E1;
- DYAD OPEN 20;
- FMS model-selection verdicts;
- optional v0.20 results;
- γ ∈ {0, 2};
- d = 2 at C¹/C²;
- primitive-clock C¹ family statements;
- targets meeting the 𝒟-spectrum.

**Unchanged provenance items:**
- M2c (ν₅⁽⁵⁾ closed form): open and non-blocking.
- `k3_six_step_factor_check.py` (`7d761090…d4ff`, FMS-reported): HISTORICAL / CONFIRMATORY / NOT REPLAYED.
- Dyadic pins remain on v6.4.11; the v6.4.12.1 repin stays deferred (D5).

## Outbound notices (issued now, citing the adopted hash `d5d1e57c…e361`)

**→ RRF (G2-CLOCK).**
- Genesis v2.8.7 (`d5d1e57c6eea0800cf8bf3e3f6b5905873e719df0969d15144ca55197cd2e361`) adopts `GEN-THM-K3-SIXSTEP-FACTOR-NOGO`. The raw projected-K₃ map has no local C³ submersive factor under the six-step contract E∘F₁⁶ = T′∘E, for target dimension 1–3 and any C³ target.
- `GEN-THM-MEANFEEDBACK-SIXSTEP-NOGO` may be cited **only together with (H_spec)**, and only for γ ∉ {0, 2}. It does not transfer to the primitive clock; the primitive-clock family statement carries its own condition (H_prim).
- `GEN-THM-K3-PLANAR-FACTOR-NOGO` (primitive clock; d = 1, 3 at C¹, d = 2 at C³) is unchanged, so the planned RRF v0.8.3 citation stays valid.
- RRF may now cite both clocks without repeating the proofs.
- Genesis selects no admissibility condition, carrier, closure condition, physical γ or node-exchange action (SG-15, SG-16).

**→ FMS / OFN.**
- FMS R7 ("Theorem 6S") now has owner RIDs: `GEN-THM-K3-SIXSTEP-FACTOR-NOGO` for κ = 1 on 𝒞, and `GEN-THM-MEANFEEDBACK-SIXSTEP-NOGO` for the family under (H_spec). FMS R5 and R6 correspond to the §6.3b `[ALG]` data and `GEN-THM-CHIRAL-CUBIC-FACTOR-LEMMA`. These rows may move from `[SESSION]` to `[OWNER]` at the stated scopes.
- **Terminology.** Genesis writes the family parameter as γ, not κ; κ remains the physical birth parameter in Genesis. The coefficients are c_γ = p − q and β_γ = iq. The mean mode is 𝒟 = {w₁ = w₂ = w₃}, and the centre manifold is tangent to 𝒞 (h = 0), not to 𝒟.
- FMS rows citing the owner results should use this notation or cite the concordance (occurrence disposition v0.1 §3).
- The two earlier FMS scope guards still apply: §8 needs the γ ∉ {0, 2} and (H_spec) qualifiers, and §1 C′ should read "tangent to 𝒞".
- No FMS SESSION result (R3, R4, R4′, R8) and no A1/A2/B/C verdict is adopted by Genesis. The physical choice remains OFN's.

**→ Dyadic.** No action. Genesis keeps its v6.4.11 pins; the v6.4.12.1 consumer repin is a separate maintenance pass (D5).

**→ Triadic.** Informational only; no Triadic import changes.
