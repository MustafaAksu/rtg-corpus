# Genesis consumer impact — Dyadic v6.4.13 — v0.1

**Date:** 19 October 2026
**State:** `[SESSION]` noncanonical consumer record.
- Adopted Genesis v2.8.7 (`d5d1e57c…e361`) is not reopened.
- No owner file, RID or OPEN status is changed here.

**Upstream:** `RTG_DYADIC_OSCILLATOR_DSN_v6.4.13`, adopted 18 Oct 2026.
- SHA-256 `5958f7fe8a3e0ec94546cb7e915c5f690d09827a3d680d13a17c9d880b968542`, as reported by the Genesis-side review of 19 Oct.
- This record was written from the project copy. Byte identity is gate D2 of the checker in §6.

**Input review:** Genesis-side assessment of 19 Oct (ChatGPT). Its proposed actions G-D13-01…05 are adopted below with three refinements: §2.3, §4 and §5.

## 1. Summary

| Item | Genesis disposition |
|---|---|
| M2c (ν₅⁽⁵⁾) | **RESOLVED upstream + Genesis replay PASS.** Point-of-use convention tag is pending for the next Genesis successor (§2). |
| Formal ℤ₆ generator J | No import. No Genesis claim depends on it (§4). |
| Lemma F, F1–F3 | No import. They concern existing smooth objects of the isolated dyad (§4). |
| OPEN 20 B-6 | Tracked as a Dyadic OPEN. No Genesis OPEN is created (§4). |
| Dyadic pins (D5) | Repin-ready v6.4.11 → v6.4.13 by manual audit; mechanical checker supplied (§3). |
| Genesis K3 / 6S theorems | **Unaffected.** No revision needed (§5). |
| Dyadic notices | N8 → RECEIVED. N7 status unchanged (ACKNOWLEDGED, no import). N1/N2 already answered. |

## 2. M2c — ν₅⁽⁵⁾ provenance

### 2.1 Source located

Dyadic v6.4.13 §6.11 registers `DYAD-ALG-NU5-P5` `[ALG]`:

  ν₅⁽⁵⁾ = (355 − 159√5)/48 + i (1106√5 − 2473)√(10+2√5)/48,

with certificate `dyad_m2c_nu5_p5_exact.py` (`5fcccb9d…d464`):
- exact arithmetic in ℚ(ζ₅);
- p = 6 calibration against `DYAD-ALG-NF6`;
- a negative control.

**Comparison with Genesis.** Genesis v2.8.7 §6.2 prints the same numerals; only the TeX spelling differs. Its value is ≈ −0.0111418421 + 0.0072266913 i.

### 2.2 Genesis-side independent replay `[NUM high-precision]`

`genesis_nu5_p5_replay.py` (`34bab140…61cb`) is Genesis's own implementation and uses no Dyadic code. It computes in mpmath at 60 digits. Setup:
- the declared K_p family;
- frame W_p = ρ + ((λ−1)/K_p)η;
- one-step normal form f∘h = h∘n through degree 5, with every resonant h-coefficient set to zero.

Result: 4/4 PASS, exit 0, under 1 s.

| Gate | Result |
|---|---|
| C1 calibration | p = 6 reproduces n₂₁, n₃₂, n₀₅ of `DYAD-ALG-NF6` to 10⁻⁵⁰ |
| C2 | p = 5: n₃₂ equals the printed closed form to 10⁻⁵⁰ |
| C3 negative control | the conjugated value is rejected |
| C4 convention sensitivity | a resonant normalizer coefficient h₂₁ = i/10 shifts Im n₃₂ by **0.01127**, larger than \|Im ν₅⁽⁵⁾\| = 0.00723 |

The resonant p = 5 slots through degree 5 come out as (2,1), (0,4), (3,2). This matches the Dyadic lattice-channel structure.

This replay is not an exact certificate. It confirms the value independently of the Dyadic certificate code, in the declared convention.

### 2.3 Refinement: a convention tag is required at the point of use

Gate C4 shows that the value belongs to its normalization convention.
- This agrees with Dyadic SG-10: Im ν₅ is not gauge-invariant.
- The Dyadic r1 review note says the same: the p = 6 calibration fixes the declared convention and does not prove equivalence of other conventions.

Genesis §6.2 lists ν₅⁽⁵⁾ under "OPEN 9 imports" without a convention tag. Its own projection warning (§6.2 `[DEF]`) requires each imported dyadic quantity to be tagged.

**Disposition:** M2c → `RESOLVED — source located (DYAD-ALG-NU5-P5), Genesis replay PASS`. The point-of-use edit belongs to the next Genesis successor:
- add `[RID: DYAD-ALG-NU5-P5]`;
- add `[conv: one-step normal form, declared K_5 family, frame W_p, resonant normalizer coefficients zero (DYAD-ALG-NF6 convention)]`.

The formula itself does not change. Until that successor, v2.8.7 is correct but under-tagged at this line. This is not a scientific error.

## 3. Repin audit (D5 revisited)

**Manual read of v6.4.13 against the 12 DYAD RIDs Genesis cites:**
- every RID is present with its v6.4.11 content;
- the 8 values Genesis cites are printed verbatim (559√15/4860, 86775991, 1/(1−iτ), 119√3/648, 2√3/3, e^{iF_f/2}, G₀₄(10), −13+15√3/2).

**Bridge-export contract:** unchanged, with the same six items and the statement "None of these items depends on the Lie strict-kernel gauge".

**Also unchanged:**
- primitive map;
- protection matrix;
- NF6 jets (n₂₁, n₃₂, n₀₅).

**Byte-level confirmation.** `check_genesis_dyad_v6_4_13_consumer.py` (`db9000ce…bfad`) checks D1–D7: both hashes, RID presence, cited values, contract strings, the M2c numerals and the N8 notice.
- It has been smoke-tested here on a synthetic upstream file: it passes every content gate and fails only the hash gate, as intended.
- The real v6.4.13 bytes must still be run through it locally:

```
python check_genesis_dyad_v6_4_13_consumer.py --genesis RTG_GENESIS_GEOMETRY_DSN_v2_8_7.md --dyad RTG_DYADIC_OSCILLATOR_DSN_v6_4_13.md
```

**Recommendation.** The deferred repin can go straight from v6.4.11 to v6.4.13, skipping v6.4.12.1. The live pointer lines in v2.8.7 are lines 8, 29, 217, 282, 582, 678, 1083, 1129, 1130 and 1164. History lines stay as they are. A pin does not certify that content is unchanged; that is why gates D3–D5 exist.

## 4. J, Lemma F, F1–F3, OPEN 20 B-6 — import boundary

**Agreed with the input review:**
- formal ℤ₆ generator: proved formally;
- analytic generator: OPEN;
- physical node exchange: OPEN;
- uniqueness does not give existence.

**Refinement — why there is no automatic transfer to the Genesis network maps.** `[ALG]`, elementary.
- J = T∘F^{−1/6}. Because F^{−1/6} = id + O(|w|³), the quadratic part of J is the quadratic part of T, which is nonzero. The same holds for R₀ = J³, whose quadratic part is 2h₂ ≠ 0 (Dyadic §6.16).
- On the carrier 𝒞 = {Σw_e = 0}, take w = (x, −x, 0). Then Σ_e J₂(w_e) = 2J₂(x) ≠ 0.
- So the edgewise maps J^{×3} and R₀^{×3} do not preserve 𝒞 beyond linear order. They are therefore not symmetries of F₁ = P_𝒞T^{×3} or of F_γ without an additional construction.
- The Genesis theorems concern those network maps. The Dyadic results concern the isolated dyad T and F = T⁶.

**Disposition:**
- No Genesis import.
- No new Genesis scope guard. SG-15 (independent of `DYAD-THM-LOCAL-INVOLUTION-GERM`; EF = TE ≠ EF = T⁶E) and SG-16 already cover the misuse risk.
- B-6 stays a Dyadic OPEN. An exactly A-equivariant analytic dyad chart, if it exists, would be a carrier candidate for RRF/OFN. Any Genesis use would need its own transport theorem, as for the h-transported carrier, which is outside v2.8.7.

## 5. Genesis K3 / 6S theorems

**No effect.** `GEN-THM-K3-PLANAR-FACTOR-NOGO`, `GEN-THM-K3-SIXSTEP-FACTOR-NOGO` and `GEN-THM-MEANFEEDBACK-SIXSTEP-NOGO` use:
- the primitive map;
- the projected or mean-feedback network map;
- their own cubic data (§6.3a(d), §6.3b).

None of these changed in v6.4.13. γ remains a model parameter (SG-16).

## 6. Proposed Genesis actions

| ID | Action | Where | Priority |
|---|---|---|---|
| G-D13-01 | M2c status → RESOLVED (source + replay). Convention tag + `DYAD-ALG-NU5-P5` import at §6.2 | this record now; tag in next successor | high |
| G-D13-02/03 | J, Lemma F, F1–F3: consumer note only (§4); no owner text | this record | done |
| G-D13-04 | Dyadic repin v6.4.11 → v6.4.13 (live pointers only) | narrow maintenance successor v2.8.8, after D1–D7 PASS on the real bytes | medium |
| G-D13-05 | K3 / 6S revision | none needed | — |
| N8 reply | "Genesis RECEIVED: M2c answered; independent replay PASS (`34bab140…61cb`); point-of-use tag scheduled" | outbound notice to Dyadic | now |

**Proposed v2.8.8 scope** (owner decision; only mechanical and provenance edits):
1. Repin the live pointers.
2. Add `DYAD-ALG-NU5-P5` to the §7 imports with its convention tag, and make the matching edit at §6.2.
3. Record M2c as closed in the release record.

No scientific claim changes. Physical G2, OPEN-B/E1 and γ selection stay open.

## 7. Artifacts

| File | SHA-256 | Result |
|---|---|---|
| `genesis_nu5_p5_replay.py` | `34bab14033a1f6bdf51f47e5c9694de43b68c2e05e6f410a7d6fa91e27f661cb` | 4/4 PASS |
| `genesis_nu5_p5_replay_output.txt` | `82d594a73933258be265f48577b5f83b87d931384cad3a2719462a7aa2a4352d` | recorded stdout |
| `check_genesis_dyad_v6_4_13_consumer.py` | `db9000ce27e5adb0fd399e1c89762795beece95309e2f3eed0085f6b80c1bfad` | to be run on the real v6.4.13 bytes |
