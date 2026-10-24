# Genesis v2.8.9 — Occurrence Map and Owner-Pass Revision Plan v0.1 (D-4)

**Date:** 19 October 2026
**Status:** `[SESSION]` owner-pass preparation, authorized by the Genesis owner decision of 19 Oct 2026 ("v2.8.9: OWNER-PASS PREPARATION AUTHORIZED").
- **No draft is produced.** No owner file is modified.
- Adopted Genesis v2.8.8 (`9abd36169a4bf6056318605c0399ff1f91c53f157b9181bdbfdb9faed3000f37`, 1581 lines) stays in force. Line numbers below refer to that file.

**Controls**
- Owner-pass manifest v0.1: `53782f8509949c2ae989bbf8fe3a9a64207b7157831988a727c7ba4dde910570`.
- D-4 SESSION v0.1.1: `1a5f7f56…cee3`.
- Certificate: `d4_transported_cubic_cert.py` `f4c38285…3f6d`.
- Owner decisions of 19 Oct:
  - **D1:** a new independent `[THM]` RID, `GEN-THM-TRANSPORTED-CHIRAL-FACTOR-NOGO` (six-step); existing RIDs are not widened.
  - **D2:** the primitive-clock transfer stays `[ALG]`.
  - **D3:** C1, C2, C3 and T-D4(iii) go into one theorem, separated by their existence conditions. C3 is the main statement, with explicit hypotheses.
  - **D4:** the result is recorded with an explicit C³ hypothesis, without waiting for OFN's Q6-REG decision.
  - **D5:** OFN notice is SESSION only until adoption.

---

## 1. Scope of v2.8.9

| Package | Content |
|---|---|
| **G9-01** | New §6.3c: the transported chiral factor obstruction. It contains one new `[THM]` RID, one primitive `[ALG]` companion without a RID, a non-RID `[DEF]` model block, an `[ALG]` μ-invariance remark, `[DEF]` evidence, `[OPEN]`, and the guards G-JET, G-20, G-SEL and G-OFN at the point of use. |
| **G9-02** | Entries for the new RID: §1 canonical state, §5 high-risk row, §7 export line, §8 RID line. |
| **G9-03** | Metadata: header, status-summary sentence, Appendix A DRAFT record, footer. |

**Explicitly not in v2.8.9**
- Any byte change to §6.3a, §6.3a.1, §6.3b, SG-15 or SG-16.
- Any change to the five existing K3/6S/mean-feedback RID lines.
- A new scope guard: per the owner, the guards sit inside §6.3c.
- Any import of J, Lemma F, F1–F3, OFN verdicts or FMS classifications.
- Physical γ, closure, carrier or model-C selection.
- Dyadic repin to v6.4.14 (see decision R-1).

---

## 2. Occurrence map (v2.8.8 → planned v2.8.9 edits)

| ID | v2.8.8 site (line / anchor) | Action | Authorization rule for the checker (S3) |
|---|---|---|---|
| H1 | line 1, title | `v2.8.8` → `v2.8.9_DRAFT` | exact title |
| H2 | lines 4–5, date and status | DRAFT owner successor, scientific (G9-01…03); **not adopted**; adopted owner stays v2.8.8 | prefix; "Not adopted"; no claim tag |
| H3 | line 7, Supersedes | prefix insertion of v2.8.8 ("on adoption") | exact prefix |
| P11 | line 11, status summary (end) | append one sentence: "**v2.8.9 draft addition:** … `GEN-THM-TRANSPORTED-CHIRAL-FACTOR-NOGO` (§6.3c) … mathematical semiconjugacy exclusion for the stated real C³ class; no physical model, carrier or γ is selected." | append only; required phrases; exactly one new RID mention |
| C1 | §1, after the `GEN-THM-MEANFEEDBACK-SIXSTEP-NOGO` paragraph (line 55, anchor = full line) | insert one `[THM]` summary paragraph for the new RID: six-step, C³, the 3-jet class, (H_spec), μ ≠ 0; "Mathematical exclusion only; see §6.3c" | insertion after an anchor; one RID; tag `[THM]` once |
| R5 | §5 table, after the "Mean-feedback six-step factor" row (line 624) | new row "Transported chiral factor": certified `[THM]` conditional (class, C³, d = 1–3, (H_spec), μ ≠ 0; primitive `[ALG]` under (H_prim)) · forbidden: physical model C selection, existence of the exact transported class, sub-C³ or non-planar decouplings, γ ∈ {0,2} · pointer: §6.3c | insertion after an anchor; forbidden-column phrases required |
| S6 | between line 848 (§6.3b Evidence) and line 850 (`### §6.3c…` placed before `### §6.4`) | **new §6.3c block** (proposed text in §4) | block inserted after an anchor; contents checked by rules M5′ and S2′ (§5) |
| X7 | §7 Export protocol, after line 1145 | new `[DEF]` export line: `GEN-THM-TRANSPORTED-CHIRAL-FACTOR-NOGO` exported with its hypotheses. The primitive companion is `[ALG]` and is **not** exported as a theorem. Q6 use requires OFN's own contract (G-OFN). | insertion after an anchor; required phrases |
| R8 | §8, after line 1186 | new RID line: `[THM]` `[scope: §6.3c; six-step; conditional on (H_spec) and μ ≠ 0]`, proof §6.3c / D-4 v0.1.1 (`1a5f7f56…cee3`), certificate `d4_transported_cubic_cert.py` (`f4c38285…3f6d`, load-bearing for the cubic data), dependency `GEN-THM-CHIRAL-CUBIC-FACTOR-LEMMA` | insertion after an anchor |
| APPA | Appendix A, before line 1201 | v2.8.9 DRAFT record: G9-01…03, the owner decisions, "No v2.8.8 claim corrected, regraded or retracted", and the not-in-draft list | append only; no backticked claim tag; exactly one new GEN RID mention |
| FOOT | lines 1577–1578 | draft footer plus the inherited v2.8.8 footer | prefix plus inherited tail |

**Not edited, by design**
- §2 OPEN registry. The factor OPENs live in the §6.3a/§6.3b `[OPEN]` lines, and the new ones go in §6.3c.
- §6.3b `[OPEN]` line 846 ("other network dynamics"). It stays byte-identical. §6.3c states which part of it the new theorem covers.
- §7 import ledger. No new import: μ₆ is recomputed in the certificate from `DYAD-DEF-PRIMITIVE-MAP`, which is already imported.
- The Dyadic pin (R-1).

---

## 3. Expected deltas (input to the checker)

| Quantity | Expected change v2.8.8 → v2.8.9 |
|---|---|
| GEN RID set | + `GEN-THM-TRANSPORTED-CHIRAL-FACTOR-NOGO` only |
| DYAD RID set | none |
| Claim tags (backticked, live text) | `[THM]` +2 (§1 summary, §6.3c theorem); `[ALG]` +3 (primitive companion, μ-invariance remark, the C1/C2 instances block); `[DEF]` +4 (§6.3c model, §6.3c evidence, §7 export line, R8 line); `[OPEN]` +1 (§6.3c). Final counts are fixed when the text is frozen; the checker compares against the declared delta, not "≤". |
| Byte-identical blocks | §6.3a through §6.3b (lines 734–848), SG-15, SG-16, and every line carrying the five existing K3/6S RIDs |

---

## 4. Proposed mathematical content of §6.3c (for owner review; not draft text)

> **### §6.3c Transported Chiral Factor Obstruction `[DEF / ALG / THM]` (v2.8.9)**
> **[SG-15 applies] [SG-16 applies]** *(source: D-4 SESSION v0.1.1; owner-pass manifest v0.1; Genesis receiving review of 19 Oct 2026)*

**`[DEF]` Model class** (no RID).
- Let 𝒩₃ be the real C³ germs N: (ℂ,0) → (ℂ,0) with N(0) = 0, DN(0) = A (multiplication by λ = e^{iπ/3} in the eigenframe of §6.3a), and **zero quadratic part with cubic part n z²z̄**, i.e. j³N(0)(z) = λz + n z²z̄.
- Put μ(N) := 6λ̄n. Then N⁶(z) = z + μ(N) z²z̄ + o(|z|³).
- For γ ∈ ℝ, write G^N_γ for the family of §6.3b with T replaced by N: (G^N_γ w)_e = N(w_e) − (γ/3) Σ_j N(w_j).
- The reference jet map is G^{(n)}_γ := G^{N₃}_γ, with N₃(z) = λz + n z²z̄. It is a real polynomial map.

**`[THM]` `[RID: GEN-THM-TRANSPORTED-CHIRAL-FACTOR-NOGO]`** `[scope: real C³ germs on ℝ⁶ in the class below; six-step contract; local at 0; C³, d = 1,2,3; conditional on (H_spec) and μ ≠ 0]`

Let γ ∈ ℝ∖{0,2} and n ∈ ℂ, and let G be a real C³ germ on ℝ⁶ with G(0) = 0. Assume:
- **(H-JET)** In some C³ coordinates fixing 0, j³G(0) = j³G^{(n)}_γ(0). Written out, this means:
  - **(i)** DG(0) is multiplication by λ on 𝒞 and by (1−γ)λ on 𝒟;
  - **(ii)** G has no quadratic part;
  - **(iii)** the cubic part of G is (w ↦ n w_e²w̄_e − (γ/3) Σ_j n w_j²w̄_j)_e.
- **(H-μ)** μ := 6λ̄n ≠ 0.

Let E be a C³ submersion from a neighbourhood of 0 ∈ ℝ⁶ onto a manifold of dimension d ∈ {1,2,3}, and T′ a C³ map with E∘G⁶ = T′∘E near 0. If (H_spec) holds, i.e. (1−γ)⁶ ∉ spec DT′(E(0)), then no such pair exists.

The class is closed under C³ conjugacy fixing 0 (part (iii) of T-D4).

*Proof outline.*
- (a)–(b) as in the proof of §6.3b. They use only (i) and the existence of a C³ centre manifold M^c tangent to 𝒞, which needs |1−γ| ≠ 1.
- The 3-jet of M^c is fixed by the homological equation. Its denominators λ^m − (1−γ)λ (degrees 2 and 3) do not vanish for γ ∉ {0,2}. By (ii), ψ₂ = 0.
- On M^c, G⁶ = id + f + o(|x|³). In the chiral coordinates of §6.3a:
  - u(f) = (μ/3) u|u|² + (2μ/3)|v|²u,
  - v(f) = (μ/3) v|v|² + (2μ/3)|u|²v,

  with no other cubic monomials (certificate G3, exact and identically in γ and n).
- Steps (a)–(c) of §6.3a.1 then give ℓ∘f = t₃∘ℓ.
- `GEN-THM-CHIRAL-CUBIC-FACTOR-LEMMA` applies with c = p − q = −μ/3 and β = iq = 2iμ/3: c − iβ = μ/3 ≠ 0 and β ≠ 0 by (H-μ). This is the adopted branch, with no extension.
- Conjugacy closure: if E is a factor of Ψ⁻¹GΨ, then E∘Ψ⁻¹ is a factor of G with the same T′. ∎

**`[ALG]` Primitive clock (C³ only; no RID; same grade as the §6.3b primitive statement).** Under the same hypotheses, no C³ submersive E∘G = T′∘E with d ∈ {1,2,3} exists under (H_prim): (1−γ)λ ∉ spec DT′(E(0)). The proof is that of §6.3b, primitive clock (i)–(iii), followed by the theorem above. (H_spec) is not used.

**`[ALG]` Instances, by existence condition.**
- **(C1, exists)** G^{(n_T)}_γ, where n_T = 1/8 − (7/72)i√3 is the Birkhoff cubic of T, with μ = μ₆ = −1/2 − (2/3)i√3. This is a real polynomial map (certificate G1, G2).
- **(C2, conditional)** Let Φ be a real C³ diffeomorphism with Φ(0) = 0, DΦ(0) = I, such that N_Φ := ΦTΦ⁻¹ commutes with A. Then N_Φ ∈ 𝒩₃ and μ(N_Φ) = μ₆, because ΦT⁶Φ⁻¹ = id + f₃ + o(|z|³) with f₃ unchanged. Hence (Φ⁻¹)^{×3}∘G^{N_Φ}_γ∘Φ^{×3} satisfies the theorem.
  - **The existence of such Φ is not asserted.** A C³ realization of the Dyadic generator J would supply one (DYAD OPEN 20). Neither J nor any DYAD §6.16–§6.17 result is imported here.
- **(C3)** The theorem itself: every real C³ germ with the stated 3-jet, whether or not it is exactly transported.

**Guards at the point of use** (manifest v0.1 §4; not a new SG)
- **G-JET.** Real statements only. Formal and polynomial computations enter as exact 3-jet data. No statement is made about the formal series F^N_κ.
- **G-20.** The theorem neither needs nor supplies the existence of the exact transported class. C2 is vacuous if no such Φ exists.
- **G-SEL.** No physical model, carrier, γ or closure condition is selected. In particular, the obstruction does not imply that model C is unique; it does not even distinguish C from its 3-jet equivalents (C3).
- **G-OFN.** Any use for OFN Q6 is subject to OFN's own contract (passive = local C³ conjugacy, primitive clock, planar targets). Wider readings need separate proof.

**`[OPEN]`**
- γ ∈ {0,2}, including the neutral 𝒟 mode at γ = 2.
- C¹/C² planar factors.
- Targets whose spectrum meets the 𝒟 spectrum.
- Non-planar or d ≥ 4 decompositions.
- Non-submersive or non-local factors.
- The formal series as such.
- Existence of the exact transported class (DYAD OPEN 20).
- Physical selection (OFN/FMS).

Relation to §6.3b `[OPEN]`: the theorem covers the 3-jet class above within "other network dynamics"; the rest of that item stays open.

**`[DEF]` Evidence.**
- D-4 SESSION v0.1.1 (`1a5f7f56…cee3`), with its receiving review (6/6 PASS, independently rerun).
- `d4_transported_cubic_cert.py` (`f4c382855b130249ce290d3ca939b283aadd27d6ea9a1af551599f4cd9533f6d`), load-bearing for: ψ₂ = 0; p = μ/3 and q = 2μ/3 identically in γ and n; μ₆ and n_T from T; calibration against §6.3b.
- Owner-pass manifest v0.1 (`53782f85…0570`).

---

## 5. Gates for the draft checker (DM1–DM7 made concrete)

| Gate | Check |
|---|---|
| **DM1** (M1a–c) | v2.8.8 baseline hash; a fresh build equals the draft; every anchor occurs once; the reverse edit list recovers v2.8.8 byte-exactly |
| **DM2** (M4) | lines 734–848, SG-15, SG-16 and the five existing K3/6S RID lines are byte-identical |
| **DM3** (M5′) | §6.3c cites `GEN-THM-CHIRAL-CUBIC-FACTOR-LEMMA` with "c = p − q", "β = iq" and the branch condition; μ ≠ 0 is stated as a hypothesis |
| **DM4** (S2′) | the primitive companion carries `[ALG]` with no RID; no `[THM]` sits on a primitive-clock statement; X7 does not export it as a theorem |
| **DM5** (S4) | G-JET, G-20, G-SEL and G-OFN phrases are present in §6.3c; forbidden phrases are absent ("unique physical model", "selects model C", "J exists", "physical realization") |
| **DM6** (S5) | certificate hash, plus a rerun 6/6 PASS; required in `--final` mode |
| **DM7** (S2) | the DYAD RID set is unchanged; no J, Lemma F, F1–F3 or OPEN 19/20 RID is imported; no OFN or FMS RID as a premise |
| S1 | the GEN RID delta and the claim-tag delta equal the declared values (§3) |
| S3 | rule-based authorization of every edit ID in §2, each used once |

Negative controls, planned:
- widen `GEN-THM-MEANFEEDBACK-SIXSTEP-NOGO` (expected to trip DM2 and S1);
- tag the primitive companion `[THM]` (DM4);
- drop the μ ≠ 0 hypothesis (DM3);
- import `DYAD-THM-FORMAL-Z6-GENERATOR` (DM7);
- add "unique physical model" (DM5);
- change a byte of §6.3b (DM2).

---

## 6. Owner decisions before the draft

| # | Question | Recommendation |
|---|---|---|
| R-1 | Repin Dyadic v6.4.13 → v6.4.14 in v2.8.9? (N10: no imported RID or grade changes; repin at the owner's convenience) | **No.** Keep v2.8.9 a single-purpose scientific release; repin later or in a maintenance release. |
| R-2 | Model definitions in §6.3c: non-RID `[DEF]` (D1 authorizes exactly one new RID)? | Yes, non-RID `[DEF]`. |
| R-3 | C2 phrased through "Φ with ΦTΦ⁻¹ commuting with A" rather than through J? | Yes. This keeps DM7 strict and imports nothing from DYAD §6.16–§6.17. |
| R-4 | §1 summary paragraph: the theorem only, or the theorem plus a mention of the primitive `[ALG]`? | The theorem only, with a pointer to §6.3c. |
| R-5 | Should the C1 value n_T appear in the text, or only μ₆? | Both; n_T is certificate-checked (G2). |

**Next step after these decisions:** produce `build_v2_8_9_draft.py`, `check_v2_8_9_draft.py`, the draft and the occurrence disposition, following the v2.8.8 pattern. That step needs a separate authorization ("draft production").
