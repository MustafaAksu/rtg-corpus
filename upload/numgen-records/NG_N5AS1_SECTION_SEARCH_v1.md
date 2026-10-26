# N-5A-S1 Search Report — Second-Stream Section-Crossing Candidate

**Report ID:** `NG_N5AS1_SECTION_SEARCH_v1` · **RID:** `NUMGEN-FAIL-N5AS1-SECTION`
**Module:** N-5A-S1 under the N-4 umbrella (PI directive 2026-08-28)
**Date:** 2026-08-28 · **Author/auditor:** Claude · **Target document:** `RTG_NUMBER_GENESIS_DSN_v1.7`
**Artifacts:** `ng_n5a_s1_section_search_v1.py` / `.log` (exit 0)
**Verdict:** candidate **FALSIFIED at gate 5**; positive byproduct registered.

---

## 1. Pre-registration (stated before the run)

**Candidate.** `B` = oriented crossing of the declared relational section `Σ = {Θ = 0 mod 2π}`, with `Θ = atan2(√3 η_wrap, 2ρ − η_wrap)` (ISP angle; imported observable, ownership remains Dyadic).

**Gate order.** Gate 5 (independence / non-relabeling) is the cheapest falsifier, so it was run **first**, before gates 1–4 (relational definition, repeatability, co-realization, common order). Per falsification-first discipline.

**HYP-N5AS1-GAP (pre-registered).** Because the `P₁` linearization is the order-6 elliptic rotation `λ = exp(±iπ/3)` and L1 contracts `Q_true → 0`, the rotation per primitive step tends to exactly `π/3`. **Prediction:** the return-gap word converges to the constant word `6`, i.e. `B → T⁶ = F`, so the candidate fails gate 5 inside the certified tube. **Falsifier:** a persistent non-constant gap word inside the certified small-amplitude regime.

## 2. Result — gate 5 failed, prediction confirmed

Inside the certified small-amplitude tube (5 seeds, `Q₀ ≈ 10⁻⁴`, 240 steps, dps=50), the return-gap word is the **constant word 6** in every case. `B` therefore coincides with `F = T⁶` there: this is re-blocking of the single Track-A stream (NG-8B), not a second independently certified event type. **SG-NG-20 is not discharged.**

**The failure is section-independent.** Sweeping 12 sections `Θ₀ = 2πk/12` across 3 seeds yields distinct gap set `{6}` — every transverse section gives the same constant word. So the obstruction is not an artifact of choosing `Θ = 0`.

## 3. Byproduct — the rational-rotation-number obstruction (positive finding)

Measured mean rotation per primitive step, with the corresponding rotation number:

| `Q₀` | mean rotation | rotation number |
|---|---|---|
| 7.6e-5 | 1.047183 | 0.1666643 |
| 0.0079 | 1.045524 | 0.1664003 |
| 0.1575 | 1.006054 | 0.1601185 |
| 1.29 | 0.564716 | 0.0898773 |

As `Q_true → 0` the rotation number → **exactly 1/6**, pinned by the `p = 6` elliptic linearization. A map whose rotation number is exactly rational `p/q` gives *every* transverse section a constant return gap `q`. This identifies the mechanism:

> `[NUM]` `[mechanism: ALG]` **Rational-rotation obstruction.** The very structure that makes N-1 work — the order-6 elliptic fixed point with `Q_true` contraction into it — forces the limiting rotation number to the rational value `1/6`, and therefore forces every section-crossing stream on the contracting local tube to be a relabeling of `T⁶`. No second independent recurrence can be constructed from the angular geometry of the same contracting orbit.

**Transient non-constancy exists but decays.** At large amplitude (outside the certified tube) the gap word is genuinely non-constant — `{6, 7, 11}` — reflecting the Birkhoff twist, i.e. amplitude-dependent rotation. But as contraction proceeds the word relaxes toward constant 6 (tails at `Q ≈ 6×10⁻³` still show `{6,7}` for two seeds, and the small-tube regime shows `{6}` uniformly). Non-constancy is a **transient of the large-amplitude regime**, not a property of the certified sector.

## 4. Consequences for the programme

1. **N-4 and N-5A are now coupled for a concrete reason, not merely by adjacency.** The only regime in which a section-crossing stream is not a relabeling of `T⁶` is the twist regime where the rotation number actually varies — which lies outside the certified L1 domain. A second stream of this type requires N-4 domain extension *first*.
2. **N-5A candidate sources should be re-partitioned.** Type (a): same orbit, angular geometry — **closed negative on the contracting tube** by this report. Type (b): domain extension into the twist/critical-curve regime — N-4 territory, and it must contend with the critical curve `C₀` (`ρ ≥ ln 2`) and the loss of the certified L1 contraction. Type (c): a structurally different source not derived from the same orbit's angular geometry — e.g. boundary/topology-changing content, birth/history records, or frame data. Only (b) and (c) remain live.
3. **A deeper connection to N-5/N-6.** Commensurability classification needs a rotation-number-like invariant that is not already pinned rational. Here it is pinned at `1/6` by the selected generator. This puts a sharp new question under the OPEN-P0 generator-selection ceiling: whether the rationality of the limiting rotation number is a property of *this* generator choice or of RTG's relational dynamics generally. That is a PI-blocked physics-input question, registered not answered.

## 5. Guards

1. This is a **falsification of one candidate**, not of N-5A itself. Types (b) and (c) are untouched.
2. The large-amplitude observations are **exploratory only** — outside the certified tube, with no claim status; they may not be used as N-5A evidence without N-4 domain certification.
3. The rotation number is an imported Dyadic-sector diagnostic; no new dyadic claim is made and ownership stays Dyadic.
4. The obstruction is `[NUM]`-certified with an `[ALG]` mechanism sketch; the general theorem ("exactly rational limiting rotation number ⟹ every transverse section is a relabeling") is registered as `[HYP]` pending a proof that handles the approach-from-below behavior seen in the intermediate regime.
5. Scope: local certified tube, selected generator `T`, OPEN-P0 ceiling retained.

## 6. Verdict

**N-5A-S1 (section-crossing candidate on the contracting tube): FALSIFIED at gate 5**, `[FAIL]`, RID `NUMGEN-FAIL-N5AS1-SECTION`. Gates 1–4 were not reached and remain untested for this candidate. **Positive byproduct registered:** `NUMGEN-ART-ROTNUM-OBSTRUCTION`, the rational-rotation obstruction, which converts the N-4/N-5A coupling from a scheduling note into a structural requirement and re-partitions the remaining N-5A search space into types (b) and (c).
