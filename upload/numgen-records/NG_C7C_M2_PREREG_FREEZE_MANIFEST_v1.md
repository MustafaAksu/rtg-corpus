# C7C-M2 Preregistration — Freeze Manifest

**Manifest ID:** `NG_C7C_M2_PREREG_FREEZE_MANIFEST_v1` · **Date:** 2026-09-30
**Ruling:** co-owner — M2-0 germ calculus, M2-1 transported identity, M2-2 value descent, `κ_b` registry, anti-circularity and P2 evidence guards APPROVED. **`NG_C7C_M2_PREREG_DRAFT_v4` FROZEN as the C7C-M2 preregistration.**
**Owner base:** Number Genesis v1.20.6 (`2a51c4b1a8037105d75e68ea7f24c721a970ab5ec32c27e810139020ccb948c5`).

## Canonical preregistration pin
```
248f128c906de337370915014e618b67c207307114cbedd9a2a4ac764d928987  NG_C7C_M2_PREREG_DRAFT_v4.md
```
Superseded drafts, each bannered with its content hash: v1 `e654abd3…794b`, v2 `1abeced0…c390`, v3 `7f8ee6ec…c2f4`.

## Provenance statement
**No C7C-M2 case or realization was examined before the definitions, germ calculus, `κ_b` keys, WD-DOM quantifiers, N1/N2 conditions and evidential guards were frozen.**

## What the audit rounds fixed
- v1 → v2: Π removed from the interface (it was making the primary test true by construction).
- v2 → v3: witness-typed domain; transported identity M2-1 (the middle condition is bounded, not exact); frozen level-b key `κ_b` with registry.
- v3 → v4: witnesses as cofinal germs (canonical transport independent of tail choice); T-inv; corrected M2-2 right-end witness `[φ′]⁻¹∘[ψ^R_y]∘[φ]`; G-bridge.
- **Co-owner closing check:** for fixed `(x,y)` and two middle germs `[φ₁]`, `[φ₂]`, the automorphism `[β] = [φ₂][φ₁]⁻¹` of `𝔍^L(y)` is itself an admissible witness choice (`x′ = x`, `y′ = y`, source identity, `ψ^L_y = β`), giving `[φ′] = [φ₂]`. Because WD-DOM(b) quantifies over every witness choice, PASS(b) already excludes Π depending on the middle germ; at level a only the identity germ is admissible. The PASS/PASS reading is therefore not silently too strong.
- **Noted, not a blocker:** the continuous-dyad sector key `DYAD-THM-PRIM-CTR U_T` is broader than the shrunken tube N5-PHYS-1's certification may use; `κ_b` only classifies event types, and G-sufficiency still requires each realization's own provenance, so the broad key admits no uncertified realization.

## Next step — evidence-sufficiency census (definitions untouched)
Scope: determine which existing records — N5-PHYS-1 / continuous dyad, and P2-unexposed DISC records — carry enough frozen provenance to reconstruct `𝔍`, `κ_b`, a representative of `[φ]`, and the provenance on which `Π` would be decided. **Output: admissible / not admissible for analysis — never PASS or FAIL.**

Census guard (from the frozen G-sufficiency, stated here so the census cannot drift into evaluation): the census records whether Π is **decidable** from a record's provenance, **not its truth value**. N1/N2 and every evaluation of Π belong to the analysis phase, because N2 itself requires an instance with Π true.
