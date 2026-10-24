# Genesis v2.8.7 DRAFT — Occurrence Disposition v0.1

**Date:** 18 October 2026 · **State:** draft companion; no adoption. Adopted Genesis v2.8.6 stays the owner file.
**Baseline:** adopted v2.8.6 `294c6fc26482d7deae42900cb50b3029ac81e96d66e239bfe8b797e95fdaa269`. Line numbers below refer to the baseline.
**Draft:** `RTG_GENESIS_GEOMETRY_DSN_v2_8_7_DRAFT.md` `81a9bd9c954f6e71d47e2cb28a9417f6dd27b51fe6132b2efe72134bf3ea7a22` (1560 lines).
**Control:** manifest v0.1 `7519e14f…135a` + owner decisions D1–D7 (18 Oct 2026) with two record corrections:
- (A) four new RIDs only — no `GEN-ALG-MEANFEEDBACK-CUBIC`, no OPEN RIDs;
- (B) the primitive-clock family statement uses the direct condition (1−γ)λ ∉ spec B, not the six-step (H_spec).

**Build:** `build_v2_8_7_draft.py` applies 13 exact-once edits. `check_v2_8_7_draft.py` proves that reversing them recovers v2.8.6 byte-exactly (M1c). The table in §1 is therefore the complete change list.

## 1. Edit-by-edit disposition

| ID | v2.8.6 line | Package | Change | Claim effect |
|---|---|---|---|---|
| H1 | 1 | mech | title → v2.8.7_DRAFT | none |
| H2 | 4–5 | mech | date 18 Oct; status DRAFT, not adopted; adopted owner stays v2.8.6 | none |
| H3 | 7 | mech | "Supersedes (on adoption)" adds v2.8.6 | none |
| H4 | 11 (opening) | mech | status-summary scope note → "v2.8.7 draft on the adopted v2.8.6 base" | none |
| H5 | 11 (end) | G7-02/03 | one appended sentence: six-step K3 exclusion; family result under (H_spec); non-selection clause | summary of §6.3a.1 / §6.3b |
| K1 | after 51 | G7-02/03 | two §1 `[THM]` one-liners (6S-core; family theorem with (H_spec)) | new claims (authorized) |
| SG16 | after 564 | G7-04 | new SG-16 + Violation line | guard |
| HR | before 616 | G7-02/03 | two §5 rows (valid form / forbidden overclaims) | guard |
| K63 | after 764, before 766 | G7-01/02/03/06 | new §6.3a.1 (Lemma S `[THM]`, 6S-core `[THM]`, `[ALG]` primitive relation, `[DEF]` evidence); new §6.3b (`[DEF]` model, `[ALG]` exact cubic, `[THM]` family theorem, three `[ALG]` notes incl. primitive clock under (H_prim), `[OPEN]`, `[DEF]` evidence) | new claims (authorized) |
| EXP | after 1058 | G7-05 | §7 RRF G2-CLOCK six-step export; family export only with (H_spec) | export statement |
| ART | after 1095 | G7-06 | four §8 RID entries with provenance and execution status | registry |
| APPA | 1108–1110 | log | Appendix A: v2.8.7 DRAFT record | history |
| FOOT | 1454–1455 | mech | draft footer; inherited v2.8.6 footer kept | none |

**Not edited, by design:**
- §6.3a, lines 725–764: model, statement, proof (a)–(e), reading, evidence, OPEN and INTERP;
- SG-15, lines 563–564;
- the existing `GEN-THM-K3-PLANAR-FACTOR-NOGO` lines in §1 (51), §5 (615), §7 (1058), §8 (1095) and Appendix A (1118);
- every Dyadic pointer and the companion header (D5 deferred);
- §2, §4, §6.1–§6.3 and §6.4 onward.

**Tag deltas (whole document):** +11 `[THM]`, +6 `[DEF]`, +5 `[ALG]`, +1 `[OPEN]`; no `[COR]`, no `[RETRACTED]`, no tag removed.

The 11 `[THM]` tags are counted as follows:
- 2 in §1;
- 2 in §5;
- 1 in the §6.3a.1 heading;
- 3 in the block (Lemma S, 6S-core, family theorem);
- 3 in §8 (lemma, 6S-core, family theorem; the family `[DEF]` entry is counted under `[DEF]`).

The 6 `[DEF]` tags are: the §6.3b heading, the model, two evidence blocks, the §7 export and the §8 family entry.

## 2. Claim-by-claim source map (content ⊆ K3-6S v0.3)

| Draft statement | RID / tag | v0.3 source |
|---|---|---|
| Lemma S (branch c−iβ ≠ 0, β ≠ 0), proof (i)–(iv) | `GEN-THM-CHIRAL-CUBIC-FACTOR-LEMMA` `[THM]` | §2.1–§2.2 (p ≠ 0 branch; p = c−iβ, q = −iβ) |
| Sharpness at β = 0 | (in lemma text) | §2.2 final line |
| 6S-core, proof (a)–(d) | `GEN-THM-K3-SIXSTEP-FACTOR-NOGO` `[THM]` | §3.1 steps 1–4 |
| Primitive factors induce six-step factors; adopted C¹ statement stays separate | `[ALG]` | §3.4 first item |
| F_γ model; 𝒞, 𝒟; spectra; γ = 1 reduction | `GEN-DEF-MEANFEEDBACK-FAMILY` `[DEF]` | §1.1 |
| Centre manifold; denominators zero only at {0, 2}; exact (c_γ, β_γ); non-vanishing | `[ALG]` (no RID, decision A) | §1.2–§1.3 |
| Family theorem under (H_spec), proof (a)–(c) | `GEN-THM-MEANFEEDBACK-SIXSTEP-NOGO` `[THM]` | §3.2 |
| Sufficient forms of (H_spec) | `[ALG]` | §3.2 "Sufficient forms" |
| (H_spec) cannot be dropped (γ = 1, E = Σw_e, T′ ≡ 0) | `[ALG]` | §3.3 |
| Primitive clock at C³ under (H_prim) | `[ALG]` (decision D6 + correction B) | §3.4 second item: "needs only (1−κ)λ ∉ spec DT′(E0)". Steps (i)–(iii) spell out that remark. B⁶ = I follows from the intertwining on 𝒞. (H_spec) is explicitly not used. |
| OPEN list | `[OPEN]` | §3.3, §4, §5 |
| SG-16 content | guard | §5 + owner decision text |

No statement in the draft lacks a v0.3 source. No FMS SESSION result (R3, R4, R4′, R8) is carried, and the checker enforces this (S4).

## 3. Notation concordance (v0.3 → draft)

| v0.3 | Draft | Check |
|---|---|---|
| κ | γ | κ is absent from all added text (S2) |
| F_κ | F_γ, mean-feedback family | — |
| closure plane Σ | mean mode 𝒟 = {w₁ = w₂ = w₃} | the phrase "closure plane" is not used |
| W^c_κ | M^c_γ, tangent to 𝒞 | "tangent to 𝒟" is forbidden (S2) |
| p(κ), q(κ) | c_γ = p − q, β_γ = iq | sympy identity (S1c) |
| p ≠ 0, q ≠ 0 | c − iβ ≠ 0, β ≠ 0 | same conditions |
| μ_cl = (1−κ)⁶ | (1−γ)⁶ in (H_spec) | — |
| "(1−κ)λ ∉ spec DT′" (§3.4) | (H_prim) | — |

The pinned scripts keep their κ / p, q notation. The draft evidence lines say so explicitly.

## 4. Gate results (executed here, `--final` mode)

`check_v2_8_7_draft.py --scripts … --final` reports **ALL EXECUTED GATES PASS (17/17)**, with no SKIP. The full output is in `checker_output.txt`.

| Gate | Content |
|---|---|
| M1a–c | baseline hash; fresh deterministic build equals the draft; reverse edit list recovers v2.8.6 byte-exactly |
| M2 | 12 DYAD RIDs unchanged; pins on v6.4.11; v6.4.12 named only in the "D5 deferred" line |
| M7 | the whole adopted §6.3a (4185 chars), SG-15 and all six existing K3-PLANAR lines byte-identical |
| M8 | new GEN RIDs = exactly the four; one §8 entry each; no `GEN-ALG-MEANFEEDBACK*` / `GEN-OPEN-MEANMODE*` |
| S1a | c_γ, β_γ, n, γ = 1 reduction, (H_spec), (H_prim), A(π/2)⁻¹A(π/6) = ½R_{π/3}, SG-16, all pinned hashes present |
| S1b ×3 | `kappa_pq_symbolic.py`, `lemmaS_hand_identities.py`, `kappa_pq_independent.py`: hash, exit 0, PASS token |
| S1c | sympy: c_γ = p − q and β_γ = iq identically; γ = 1 gives (c₀, β*); printed Im(c_γ − iβ_γ) formula |
| S2 | no forbidden overclaim; no κ; every mention of the family RID carries (H_spec); four built-in negative controls fire |
| S3a–c | tag audit (deltas as in §1) |
| S4 | no FMS SESSION content; OPEN 20 named only in "Not in this draft" |
| S5 | `k3_six_step_factor_check.py` appears only as HISTORICAL / CONFIRMATORY / NOT REPLAYED, not a proof input |

**SKIP policy (owner execution condition, 18 Oct).**
- In development mode, missing scripts or sympy give SKIP with exit 0.
- With `--final`, any SKIP gives exit 1. Verified: `--final` without `--scripts` exits 1.
- `kappa_pq_symbolic.py` is load-bearing, so the adoption review must run with `--final`.

**Negative controls (all exit 1):**

| Tampering | Caught by |
|---|---|
| one undeclared word deleted inside §6.3a | M1b, M1c, M7 |
| (H_spec) removed from the §1 line (edited draft) | M1b, M1c |
| fifth RID `GEN-ALG-MEANFEEDBACK-CUBIC` inserted | M1b, M1c, M8 |
| β_γ typo (γ−2 → γ+2) | M1b, M1c, S1a |
| build that drops (H_spec) from §1 | S2 |
| build that "selects a physical closure" | S2 |
| build that makes M^c tangent to 𝒟 | S2 |

## 5. Outbound notices on adoption (not sent by the draft)

| To | Notice |
|---|---|
| RRF | G2-CLOCK may cite `GEN-THM-K3-SIXSTEP-FACTOR-NOGO` (any C³ target). `GEN-THM-MEANFEEDBACK-SIXSTEP-NOGO` may be cited only with (H_spec). `GEN-THM-K3-PLANAR-FACTOR-NOGO` is unchanged, so existing v0.8.3 wording stays valid. |
| FMS / OFN | R7 (Theorem 6S) gains an owner RID once adopted. FMS rows must adopt γ / 𝒟 terminology or cite the concordance. The two FMS scope guards (γ = 2; tangent to 𝒞) still apply. |
| Dyadic | none. The v6.4.12.1 consumer repin remains a separate maintenance operation (D5). |

## 6. Remaining before adoption

1. An independent receiving review of the draft bytes, this disposition, the build and the checker, run with `--final` and `--scripts`.
2. Owner adoption decision. The new RIDs become citable only then.
3. A release transform (metadata only) with its own checker, as for v2.8.6.
