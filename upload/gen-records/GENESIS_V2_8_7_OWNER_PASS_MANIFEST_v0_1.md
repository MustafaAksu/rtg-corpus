# Genesis v2.8.7 — Owner-Pass Scope Manifest and Occurrence Map v0.1

**Date:** 18 October 2026
**State:** Stage B preparation manifest only. It is authorized by the Genesis disposition "K3-6S v0.3: ACCEPT FOR OWNER REVIEW" (18 Oct 2026). Nothing here is an owner edit, a draft, a finalized RID or an adoption. Adopted Genesis v2.8.6, DYAD v6.4.12.1, RRF v0.8.2, OFN v0.9 and the frozen GCL are unchanged.
**Target:** `RTG_GENESIS_GEOMETRY_DSN_v2_8_7_DRAFT`, built deterministically on the exact adopted v2.8.6 bytes.
**Principle:** the draft carries only content proved in the accepted proof record (K3-6S v0.3). Notation may change; content may not. §3 maps one onto the other.

## 0. Pinned inputs

| Input | Role | SHA-256 |
|---|---|---|
| `RTG_GENESIS_GEOMETRY_DSN_v2.8.6` (adopted 16 Oct) | owner baseline; every line number below refers to this file (1457 lines) | `294c6fc26482d7deae42900cb50b3029ac81e96d66e239bfe8b797e95fdaa269` |
| `K3_KAPPA_SIX_STEP_CLOCK_NOTE_v0_3.md` | accepted proof record (6S-core, Lemma S, 6S-κ) | `049e313e4f07ffe5e576018426a5776aab9b602b0c5c55ef286c71d750babc9e` |
| `kappa_pq_symbolic.py` | p, q as identities in ℚ(κ)(i√3) — **load-bearing** | `091a42105cff7965127c55a4a5adffa281021cd71957ed789409de320c5d42b2` |
| `lemmaS_hand_identities.py` | audit of Lemma S identities I1–I5 | `af8e79c36f2312c78150c808e5a7a57fc6aeccba9de5355263f5b9c012989674` |
| `kappa_pq_independent.py` | 5-point exact cross-check (own ψ₂, ψ₃, both components) | `7056b077e30ff498b17cf96737a32366305995283de3e332d38654bbfe4aef97` |
| `lemmaS_burnside_check.py` | M₄(ℝ) corroboration, q = 0 control | `2429212d0c8d38c240a03bac66b8157c687697348c9187f596a0dbc71cb6ea9d` |
| `exact_q.py` / `exact_q_output.txt` | independent q(κ) derivation (ChatGPT; PI rerun) | `44105683…6001` / `951a6f24…dddc` |
| `k3_six_step_factor_check.py` | Lemma S p = 0 branch (Gröbner) — **HISTORICAL / CONFIRMATORY / NOT REPLAYED** | `7d761090378781c5c74ec64abc1f215cc951cec21f139a231ee1bd8ed18ad4ff` *(as recorded in FMS v0.5.1 §10; Genesis holds no copy and has not verified it)* |
| `K3_CUBIC_FACTOR_OBSTRUCTION_SESSION_RECORD_v0_1_2.md` | source of the existing §6.3a (unchanged) | `9f95d48d23a340738146271d4bcf1a483b04252e9210c9f403a7f23172dd083a` |

**Independent execution status (18 Oct disposition).** All four Claude scripts were rerun unmodified: exit 0, empty stderr. The v0.3 bytes and the ZIP manifest match.

**Context only, not imported:** FMS Ledger v0.5.1 SESSION. It is cited for terminology checks only; its SESSION results (R3, R4, R4′, R8) are **not** Genesis content.

## 1. Scope

**In:**
- **G7-01** Lemma S (chiral cubic factor lemma).
- **G7-02** 6S-core: the six-step clock on the raw projected K₃ (κ = 1, 𝒞).
- **G7-03** The mean-feedback family `[DEF]`, its exact cubic data `[ALG]`, and the conditional 6S theorem `[THM]` on ℝ⁶ under (H_spec).
- **G7-04** SG-16 scope guard.
- **G7-05** RRF G2-CLOCK export line (six-step).
- **G7-06** Provenance.

**Out:**
- physical γ (= κ in the source notes) selection;
- OPEN-B/E1;
- alternative additive carrier;
- DYAD OPEN 19 and OPEN 20 imports;
- FMS model-selection verdicts (A1/A2/B/C) and FMS SESSION results R3, R4, R4′, R8;
- the primitive-clock C¹ extension to the family (not in v0.3);
- `Q-SUCC-UV-01`;
- V20-O1–O5 and Candidates A–C;
- M2c (stays an open, non-blocking provenance item);
- any GCL edit;
- the Dyadic repin unless D5 = include.

**Existing theorem untouched.** The statement, proof (a)–(e), evidence and OPEN lines of `GEN-THM-K3-PLANAR-FACTOR-NOGO` (the whole §6.3a, lines 725–764) and SG-15 (line 563) stay byte-identical (gate M7). RRF pins to that RID therefore keep their meaning.

## 2. Work packages and occurrence map (v2.8.6 line numbers)

### G7-01 / G7-02 — Lemma S and 6S-core (inside §6.3a)

| Location | Action |
|---|---|
| §6.3a, after line 764 (`[INTERP]`), before §6.4 (line 766) | Insert sub-block **"Six-step clock (v2.8.7)"**. |
| (a) | `[THM]` Lemma S, proposed RID `GEN-THM-CHIRAL-CUBIC-FACTOR-LEMMA`. Statement in the §6.3a chiral form u(f) = c\,u\|u\|² − iβNu (§3). Proof = v0.3 §2.1–§2.2 (invariant kernel; A(π/2)⁻¹A(π/6) = ½Rot(π/3); mixed terms). Branch hypothesis: c − iβ ≠ 0 and β ≠ 0. The p = 0 / Gröbner branch is **not** stated as an owner result; it is mentioned only as historical confirmation. |
| (b) | `[THM]` 6S-core, proposed RID `GEN-THM-K3-SIXSTEP-FACTOR-NOGO`, `[scope: named projected-K3 model on 𝒞; six-step contract E∘F₁⁶ = T′∘E; local germs at 0; C³, d ∈ {1,2,3}]`. The statement says explicitly: no hypothesis on T′ beyond C³. Proof = v0.3 §3.1, steps 1–4. It reuses §6.3a(b) (leading-term lemma) and (d) (c₀, β*) by pointer. |
| (c) | One `[ALG]` sentence: primitive factors induce six-step factors, so 6S-core re-excludes them at C³. The adopted C¹ statement for d = 1, 3 is stronger and stays separate. |

### G7-03 — Mean-feedback family (new §6.3b)

| Location | Action |
|---|---|
| new §6.3b, after the G7-01 block, before §6.4 | **`[DEF]`** `GEN-DEF-MEANFEEDBACK-FAMILY`: F_γ(w)_e = T(w_e) − γ·mean_e T(w), on ℝ⁶. Includes the carrier 𝒞 = {Σw_e = 0} and the mean mode 𝒟 = {w₁ = w₂ = w₃}. DF_γ(0) = λ on 𝒞 and (1−γ)λ on 𝒟. At γ = 1, F₁ restricted to 𝒞 is the §6.3a model. |
| | **`[ALG]`** `GEN-ALG-MEANFEEDBACK-CUBIC`. Centre manifold M^c_γ = {mean = ψ_γ(u)}, **tangent to 𝒞**, for γ ∈ ℝ ∖ {0, 2}. The real zeros of the denominators are exactly {0, 2}. The six-step cubic has chiral form with (c_γ, β_γ) (§3), as exact rational-function identities. c_{γ=1} = c₀, β_{γ=1} = β*, Re β_γ > 0, and Im(c_γ − iβ_γ) ≠ 0. |
| | **`[THM]`** `GEN-THM-MEANFEEDBACK-SIXSTEP-NOGO` `[scope: conditional on (H_spec)]`. Hypothesis (H_spec): (1−γ)⁶ ∉ spec DT′(E(0)). Proof = v0.3 §3.2. Sufficient forms of (H_spec) are listed. The γ = 1 counterexample E = Σw_e, T′ ≡ 0 is recorded as showing that a hypothesis is necessary (v0.3 §3.3). |
| | **`[ALG]`** Primitive-clock corollary on ℝ⁶ at C³, from v0.3 §3.4, with its own spectral condition. |
| | **`[OPEN]`** `GEN-OPEN-MEANMODE-FACTOR`: factors whose target spectrum meets the 𝒟-spectrum, for γ ≠ 1. **`[OPEN]`** γ = 2 (quadratic resonance λ⁴ = (1−γ)λ) and γ = 0. **`[OPEN]`** d = 2 at C¹/C² at both clocks. |

### G7-04 — SG-16 (§3 Scope Guards)

| Location | Action |
|---|---|
| after SG-15 (line 563), before §4 (line 568) | **[SG-16] Six-step and mean-feedback scope guard (v2.8.7).** |

SG-16 states:
- `GEN-THM-MEANFEEDBACK-SIXSTEP-NOGO` may be cited only together with (H_spec).
- No physical γ is selected.
- γ ∈ {0, 2} is not covered.
- The centre manifold is tangent to 𝒞, not to 𝒟.
- The six-step results do not exclude C¹ factors.
- ER-2B shape-sphere integrals (κ = 1, Re q = 0) do not transport to γ ≠ 1.
- SG-15 applies to all v2.8.7 statements.

### Summary, ledger and registry entries

| Line | Action |
|---|---|
| 11 (status summary) | Append one sentence: **v2.8.7 addition.** It covers 6S-core (any C³ target), the conditional family theorem under (H_spec), and the non-selection clause. Items (i)–(x) and the v2.8.6 sentence are unchanged. |
| after 51 (§1) | Two `[THM]` one-liners: 6S-core and the conditional family theorem, each with a §6.3a/§6.3b pointer and SG-16. |
| after 615 (§5 high-risk) | Two rows. **Valid:** "no local C³ submersive factor of the raw projected K₃ under the six-step contract, d = 1–3, any C³ target" / "same for F_γ, γ ∉ {0, 2}, under (H_spec)". **Forbidden:** "six-step d = 1, 3 at C¹"; "family theorem without (H_spec)"; "γ = 2 excluded"; "physical γ / closure selected"; "centre manifold tangent to the mean mode". |
| after 1058 (§7 export) | `[DEF]` **(v2.8.7) RRF G2-CLOCK six-step export**, with exactly the wording of v0.3 §5. No admissibility condition is selected. |
| after 1095 (§8 registry) | Four RID entries plus OPEN RIDs, with the §0 hashes and execution statuses. `k3_six_step_factor_check.py` is marked HISTORICAL / CONFIRMATORY / NOT REPLAYED. |
| Appendix A (before line 1110) | v2.8.7 DRAFT entry: G7-01–06, decisions D1–D7, "no v2.8.6 claim corrected, regraded or retracted". |
| 1–5, 7, footer 1454–1456 | Mechanical: title, date, status (DRAFT), supersedes on adoption, draft footer. |

## 3. Notation concordance (source v0.3 → Genesis draft)

**Collisions found in v2.8.6.**
- **κ.** κ occurs 73 times. It is the physical child W-ratio κ (line 11, §6.3), with κ < 0 and κ_phys / κ_RTG in the §7 export rules. Writing the family parameter as κ would collide head-on with a live physical symbol, and with the "may not export a physical κ_phys" rule.
- **p.** p is the fixed point E(0) in §6.3a(a), and also the p-step index (p = 5, 6, 7).
- **"Closure plane"** is ambiguous across sources:
  - FMS v0.5.1 §1 uses it for {h = 0} = 𝒞;
  - v0.3 §1.1 uses it for the mean mode Σ;
  - this was the disposition's second FMS point.

| v0.3 | Draft (proposed) | Relation |
|---|---|---|
| κ | **γ** (unused in v2.8.6) | identical parameter |
| F_κ | F_γ, "mean-feedback family" | identical map |
| closure plane Σ = {w₁ = w₂ = w₃} | **mean mode 𝒟** | same subspace; the phrase "closure plane" is not used |
| W^c_κ | **M^c_γ** (W is the eigenframe symbol) | same manifold, tangent to 𝒞 |
| p(κ), q(κ) | **c_γ = p − q, β_γ = i q** | u(f) = c_γ u\|u\|² − iβ_γ N u (§6.3a form) |
| μ_cl = (1−κ)⁶ | (1−γ)⁶ | — |
| (H_spec) | (H_spec) | unused in v2.8.6 |

**Exact forms (verified by sympy from the v0.3 closed forms).** Write n = γ² − γ + 1.

- c_γ = (3γ³ − 7γ² + 5γ − 2) / (6(γ − 2)n) + i (√3/9)(2γ² − 3γ + 2)/n
- β_γ = (2√3/9)(2γ² − 3γ + 2)/n − i (2/3)(γ − 1)³ / ((γ − 2)n)

At γ = 1: c₁ = 1/6 + i√3/9 = c₀ and β₁ = 2√3/9 = β*.

**Lemma S branch conditions in this notation:**
- β ≠ 0, which holds because Re β_γ > 0;
- c − iβ ≠ 0, which holds because Im(c_γ − iβ_γ) = −(√3/9)(2γ² − 3γ + 2)/n ≠ 0.

## 4. Gates (checker for the draft)

| # | Gate |
|---|---|
| M1a–d | Baseline v2.8.6 SHA. Deterministic build. Reverse-applying the edit list recovers v2.8.6 byte-exactly. No undeclared change. |
| M2 | Dyadic pins unchanged: same 12 DYAD RIDs, all present in v6.4.11. If D5 = include, all must also be present in v6.4.12.1 with the cited values verbatim. |
| M7 | Lines 725–764 (the whole adopted §6.3a: model, statement, proof, reading, evidence, OPEN, INTERP of `GEN-THM-K3-PLANAR-FACTOR-NOGO`) and SG-15 are byte-identical in the draft. Its §1, §5, §7 and §8 entries are unchanged. |
| M8 | New RIDs do not occur in v2.8.6; each new RID is defined exactly once. |
| S1a | New text carries: the (H_spec) formula; c_γ and β_γ (verbatim from §3); the γ = 1 reduction to (c₀, β*); and every §0 hash. |
| S1b | `kappa_pq_symbolic.py` and `lemmaS_hand_identities.py` match their hashes and exit 0 (sympy needed; SKIP rather than PASS if absent). `kappa_pq_independent.py` exits 0. |
| S1c | Concordance check: the printed c_γ and β_γ equal p − q and iq of the v0.3 closed forms, identically in γ (sympy). |
| S2 | No forbidden overclaim in added text. Negated guard sentences are allowed. Patterns: family theorem without "(H_spec)" in the same paragraph; "C^1" together with six-step d = 1, 3 exclusion; "γ = 2" excluded or covered; physical γ / closure / carrier selection; "tangent to 𝒟" / "tangent to the mean mode"; "κ" as the family parameter. Includes a negative control. |
| S3a–c | Tag audit vs v2.8.6. No tag is removed. Tags are added only in G7 edits. No `[COR]` or `[RETRACTED]`. Whole-document deltas are reported. |
| S4 | `[SESSION]` boundary: FMS R3, R4, R4′, R8, A1/A2/B/C verdicts and OPEN 20 content are absent. FMS appears at most as a context pointer. |
| S5 | Provenance status: `k3_six_step_factor_check.py` appears only with "HISTORICAL / CONFIRMATORY / NOT REPLAYED". It is never cited as proof of a stated owner result. |

## 5. Owner decisions needed before drafting

- **D1 — RID strategy.** Recommended: new RIDs (§2), with the existing `GEN-THM-K3-PLANAR-FACTOR-NOGO` byte-frozen. Alternative: widen the existing RID's scope to both clocks. Not recommended: it changes the meaning of a RID that RRF already cites.
- **D2 — Family parameter symbol.** Recommended: γ. κ is excluded by the collision in §3.
- **D3 — Coefficient notation.** Recommended: (c_γ, β_γ), continuous with (c₀, β*). The alternative (p_γ, q_γ) collides with p = E(0).
- **D4 — Placement.** Recommended: Lemma S and 6S-core inside §6.3a; the family in a new §6.3b.
- **D5 — Dyadic repin v6.4.11 → v6.4.12.1.** Mechanical; every cited RID and value is present (consumer-impact note, 17 Oct). Recommended: **defer** to keep v2.8.7 narrowly scientific. The alternative is to include it, with gate M2 extended.
- **D6 — Primitive-clock family corollary (v0.3 §3.4).** Recommended: include it as `[ALG]` at C³ with its own spectral condition. No C¹ family statement: it is not in the proof record.
- **D7 — Gröbner script status.** Recommended: "HISTORICAL / CONFIRMATORY / NOT REPLAYED". Record the hash as FMS-reported and not Genesis-verified. This is not release-blocking, since the p = 0 branch is not a proof dependency.

## 6. Out-of-band notes (not Genesis edits)

**FMS v0.5.1.** The disposition's two scope guards are confirmed against the file:
- §8 "Within the κ family …" needs the κ ∉ {0, 2} and (H_spec) qualifiers.
- §1 C′ "tangent to the closure plane" should read "tangent to 𝒞 (h = 0)".

FMS v0.5.1 §10 also supplies the full Gröbner-script hash used in §0.

**K3 note v0.3.** "Closure plane Σ" (§1.1) is superseded by "mean mode 𝒟" through the §3 concordance. No v0.3.1 is needed, since the content is unchanged.
