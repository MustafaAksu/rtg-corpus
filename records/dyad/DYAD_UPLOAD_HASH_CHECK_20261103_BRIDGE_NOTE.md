# DYAD upload hash check — bridge note v1.1 (`DYAD-ART-BRIDGE-NOTE`)

**Date:** 3 November 2026. **By:** Claude, Dyadic owner/editor and Triadic co-owner.
**Object:** branch `miss1`, commit `47f807c` ("upload: dyad_triad_antisymmetric_bridge_v1_1.md (DYAD-ART-BRIDGE-NOTE), unchanged"), pushed by the PI. One file was added: `upload/dyad-bridge-note/dyad_triad_antisymmetric_bridge_v1_1.md`.

**Evidence:**
- `EV-HASH` for the file.
- `EV-RUN` for the exact replay of its claims (§3).
- The file was not changed, renamed or moved. It stays under `upload/dyad-bridge-note/`, the intake placement used for `upload/dyad-sources/` on 30 October.

**Branch name.** CONVENTIONS asks for `upload/<topic>`. This upload came on a branch named `miss1`, but the folder in the commit is the agreed one. The content is unaffected and no action is needed. The working branch `claude/dyad-bridge-note-intake` builds on `47f807c`, so merging it brings in the upload commit unchanged.

## 1. Hash check

| File | Bytes | Lines | SHA-256 |
|---|---|---|---|
| `upload/dyad-bridge-note/dyad_triad_antisymmetric_bridge_v1_1.md` | 10 099 | 232 | `5ddebfe46b5572761a5154a05712fbcfe4e675f912430ee7d6bfcf0d93f4e875` |

- UTF-8, LF line endings, no CR. The repository's `* -text` attribute applies, so git stores the bytes as committed.
- The committed blob is byte-identical (`cmp`) to the copy the PI attached in the Dyadic session on 3 November 2026.
- The Dyadic DSN records no hash for this file (§8, `DYAD-ART-BRIDGE-NOTE`). Triadic does not record one either (§7.1 cites the note by name). Under the recovery-list rule it is accepted as **PI-supplied**, identified by name and content.

## 2. Identification

| Check | Result |
|---|---|
| File name | equal to the name cited in Dyadic §2 (downstream handoff), §8 (`DYAD-ART-BRIDGE-NOTE`) and Triadic §7.1 |
| Version and date in the file | "v1.1", footer "2026-05-05". The revision note names the v1.1 corrections (area/Jacobian statement §6, Genesis lift formula §10) |
| Content against the §8 description ("antisymmetric odd-channel identity, μ_p = p λ̄ ν₃^(1,p), protection matrix, Genesis lift obstruction") | all four present (§1, §4, §6, §7) |
| Content against `DYAD-DEF-BRIDGE-EXPORT-CONTRACT` (§6.12) | the frame W = ρ + ωη and v_⊥, μ = −½ − iτ, τ = 2√3/3, the ratio 4√3/3, 𝒫_dyad(R²) and the bridge lemma are all stated, with the same values |
| Primitive map | the note's T at K = 1 is the map of `DYAD-DEF-PRIMITIVE-MAP` (§1) |

**Identified** as the cited `DYAD-ART-BRIDGE-NOTE`.

## 3. Exact replay (`EV-RUN`)

- **Script:** `evidence/dyad/scripts/dyad_bridge_note_v1_1_check.py` (sympy 1.14.0, exact algebra).
- **Run:** `evidence/dyad/bridge-note-v1-1/run.sh` from the repository root, with outputs and `SHA256SUMS.txt` in the same folder.
- **Inputs:** the uploaded note, and the Dyadic DSN read from the tag `dyad-v6.4.23`. Gate G0 checks the note's hash and three DSN text anchors: the registry line, the primitive map, and the ν₃(λ) closed form.
- **Result:** positive run exit 0, all 51 gates PASS. The five negative controls each exit 1, at the gates named below.

| Gate | Claim of the note | Result |
|---|---|---|
| B1 | odd-channel identity Δ_cT = T(x+cv) − T(x−cv), any x, v, K; only odd powers of c | PASS (general K: Δ_cT_η = 2cb + 2K e^ρ sinh(ca) − 2K cos η sin(cb)) |
| B1k | the printed Δ_cT_η | the **K = 1 form** (finding F1) |
| B2 | det ∇T = 1 + K cos η (e^ρ − 1); 1 at the origin; not identically 1 | PASS (at (1, 0): 1 + K(e − 1)) |
| B3 | λ = 1 + ω = e^{iπ/3}; the linear part in W is λW; the inverse map; v_⊥ = (1/√3, 2/√3); W = i√3 Z | PASS. Z is the DSN raw frame η = Z + Z̄, ρ = uZ + ūZ̄, u = 1/(1−λ) = ½ + i√3/2. This agrees with `DYAD-ALG-KP-FRAME-SCALE` at p = 6 |
| B4 | §3 series at P₁ = (0,0) along v_⊥, and Δ_cW′ = 2λic + (7√3/54 + i/2)c³ + O(c⁵) | PASS |
| B5 | ν₃^(1,6) = 1/8 − i·7√3/72 (W frame) | PASS, **computed independently**: one-step Birkhoff normal form of T (K = 1) in the W frame, with the quadratic terms removed. It equals the DSN closed form ν₃(ζ₆) = 3/8 − i·7√3/24 (Z frame, §6) divided by cot²(π/6) = 3 |
| B6 | μ₆ = 6λ̄ν₃ = −½ − i·2√3/3 = μ | PASS; this is `DYAD-THM-C21`'s μ |
| B7 | bridge lemma μ_p = pλ̄ν₃ | PASS for p = 5, 6, 7: symbolic ν, p-fold composition truncated at cubic order |
| B8 | F(s+ic) − F(s−ic) = 2ic(1 + μR²), and its real form | PASS |
| B9 | det 𝒫_dyad = 1 − R² + 19R⁴/12 = \|1 + μR²\|²; det ∇F = 1 − 2R² + 19R⁴/4 (exact for W ↦ W + μ\|W\|²W); the two differ | PASS |
| B10 | −Im μ / (−Re μ) = 2τ = 4√3/3 | PASS |
| B11 | the lift W = βe^{iχ}w gives w′ = w + μβ²\|w\|²w; χ cancels; the ratio is unchanged in 𝒫_Genesis | PASS |
| T | each checked formula is printed in the note as checked | 16/16 PASS |

| Control | Change | Fails at |
|---|---|---|
| TAMPER | every `\tfrac{19}{12}` in the note replaced by `\tfrac{19}{11}` | G0 hash, T_detP |
| KFORM | the printed Δ_cT_η asserted for K = 2 | B1k |
| NUSIGN | ν₃ with the imaginary sign flipped | B5, B6 |
| ZFRAME | the Z-frame ν₃ used in the W-frame lemma without cot² | B6 (gives 3μ) |
| DETMIX | det ∇F asserted equal to det 𝒫_dyad | B9 |

What this replay covers:
- It checks the note's algebra and its agreement with the adopted DSN. Nothing in the DSN changes because of it.
- B5 checks the one-step coefficient ν₃ against a fresh normal-form computation. It is not a replay of the certifying instances the note names ("exact cyclotomic engine" and the mpmath 60–100 dps checks). Those scripts are not in the note and are not recovered. The note's "residual < 6×10⁻⁶¹" is therefore cited, not reproduced.
- The note's prerequisite `OPEN9_full_onestep_normalization_table_v2.md` is still missing (recovery list, Tier 3).

## 4. Findings

- **F1 (editorial; the note's result is unaffected).** The note's §1 prints Δ_cT_η without K, which is the K = 1 form. It then states that the identity holds "for arbitrary K". That scope claim is true for the odd-channel corollary (B1). The printed component formula needs the factor K on the sinh and sin terms. The note is a frozen source and is not edited. Any DSN text that quotes the component formula should use the general-K form.
- **F2 (grade, for the v6.4.24 X4 decision).** The note grades "primitive dyad not globally area-preserving" `[ALG]`: it is a direct Jacobian computation (B2). Dyadic §1 (L63) and §6 (L447) at `dyad-v6.4.23` mark the same statement `[THM]`. X4 proposes a Dyadic RID for this statement. The grade is decided there and recorded in `records/dyad/DYAD_v6_4_24_BACKLOG.md` §B. Owner proposal: `[ALG]`, with the note as its source.
- **F3 (pin).** At the next Dyadic release, the §8 `DYAD-ART-BRIDGE-NOTE` entry can carry the hash above and the path `upload/dyad-bridge-note/`, with the availability note "PI-supplied 3 Nov 2026, identified by content".

## 5. Updates made with this record

- `records/dyad/DYAD_SOURCE_RECOVERY_LIST.md`: Tier 3 row marked placed; added to a "Placed (3 November 2026)" table.
- `records/triad/TRIAD_SOURCE_RECOVERY_LIST.md` (Triadic co-owner): the note moves from S to P.
- `pipes/TRIAD/20261103-DYAD-bridge-note-recovered.md`: notice to the Triadic owner. Triadic §7.1's availability sentence ("the intermediary bridge note is still not in this package") can be updated at its next release.
- The v6.4.24 backlog items (F2, F3) go on the backlog branch `claude/dyad-v6.4.24-backlog-update`.
