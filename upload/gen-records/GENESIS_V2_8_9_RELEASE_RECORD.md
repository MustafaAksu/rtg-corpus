# Genesis Geometry v2.8.9 — Release Record (scientific)

**Date:** 19 October 2026

**Owner decision:** Adopted by Genesis stream owner decision, 19 October 2026, following the independent Genesis v2.8.9 receiving review (11/11 PASS in --final --cert mode, 0 SKIP); scientific payload unchanged from the reviewed draft.

**Status:** v2.8.9 becomes the adopted Genesis owner file from this release, after R1–R8 PASS on the real bytes (§2). v2.8.8 is superseded and kept unchanged as history.

## 1. Identities

| Object | SHA-256 |
|---|---|
| Baseline: adopted v2.8.8 | `9abd36169a4bf6056318605c0399ff1f91c53f157b9181bdbfdb9faed3000f37` |
| Reviewed draft `RTG_GENESIS_GEOMETRY_DSN_v2_8_9_DRAFT.md` | `b2cc5c5cb637459b3e2aded30b1c48ad859f2591a93684f463f89fbab503f62a` |
| **Adopted release `RTG_GENESIS_GEOMETRY_DSN_v2_8_9.md` (1649 lines)** | **`d143673e9596abc900f54f269582299c87c9146504d6c9e1fd08ac294ba8c6fc`** |
| Draft package (receiving review) | `a3ceb92e66d7cd2caf4d96d5e65f6d17607b5b7e50f2f88a6f0582335573e973` |
| Adoption kit (owner-verified) | `5dfa9fbcf6f5771ff18d43bdc9da447e91a9d46e48576f77cff776e12688df52` |
| `release_v2_8_9.py` / `check_release_v2_8_9.py` | `09ab48f6…adfc` / `2145216a…34ec` |
| Release checker output | `e446311a122279ca4bd802ec0284d769acdb4073b3a616de41c7e6a902aae8dd` |
| `d4_transported_cubic_cert.py` | `f4c382855b130249ce290d3ca939b283aadd27d6ea9a1af551599f4cd9533f6d` |
| Draft build / draft checker / negative controls (original / fast) | `21388c8b…ac2e` / `1ac4dd5c…463c` / `956383f4…b113` / `dc882360…7f22` |
| Occurrence disposition v0.1 / plan v0.1 / owner-pass manifest v0.1 / D-4 v0.1.1 | `2e128a2b…275c` / `aee218c0…1ee3` / `53782f85…0570` / `1a5f7f56…cee3` |

## 2. Chain

1. **v2.8.8 → draft.** 11 edits authorized by rules.
   - Draft checker `--final --cert`: 11/11 PASS, 0 SKIP (independent receiving review).
   - Certificate: 6/6 PASS.
   - Package manifest: 12/12.
2. **Negative controls.**
   - The package record shows 8/8 caught.
   - The reviewer's full replay with the original script did not complete within the time limit. This is recorded in Appendix A as an execution-coverage limitation.
   - The reviewer later completed an independent replay with `negative_controls_v2_8_9_fast.py`: 8/8, exit 0. That replay is the same set of controls with the certificate rerun removed from NC1–NC7.
   - The owner decided that the Appendix A wording stays as issued. It remains historically accurate, because the original slow script was never replayed in full.
3. **Draft → release.** 7 metadata edits. Release checker R1–R8: **8/8 PASS**, exit 0.
   - §6.3a–§6.3c are byte-identical.
   - The RID set is unchanged and includes the new RID.
   - Claim-tag counts are identical.
   - The certificate pin is intact.

## 3. In force from this release

- **`GEN-THM-TRANSPORTED-CHIRAL-FACTOR-NOGO`** (§6.3c), `[THM]`, conditional. Its scope:
  - six-step contract;
  - real C³ germs on ℝ⁶ with the stated third jet (linear part λ on 𝒞 and (1−γ)λ on 𝒟; zero quadratic part; cubic part n w_e²w̄_e minus the γ-mean);
  - γ ∈ ℝ∖{0,2}, μ = 6λ̄n ≠ 0, and (H_spec);
  - closed under C³ conjugacy.
  - Algebraic dependency: `GEN-THM-CHIRAL-CUBIC-FACTOR-LEMMA` (adopted branch, with c = p − q and β = iq).
- **Primitive-clock companion.** `[ALG]`, no RID, under (H_prim). It is proved by the direct primitive argument. It is not a corollary of the six-step theorem, and it is not exported as a theorem.
- **Instances.**
  - C1, polynomial and existing: n_T = 1/8 − 7i√3/72, μ₆ = −1/2 − 2i√3/3.
  - C2, conditional on a C³ chart Φ with ΦTΦ⁻¹ commuting with A. Its existence is not asserted.
  - C3, the theorem itself.
- **Unchanged.**
  - The five K3/6S RIDs, SG-15 and SG-16.
  - The Dyadic pins at v6.4.13 (repin to v6.4.14/v6.4.15 deferred, R-1).
- **Not imported.** No Dyadic generator, centralizer or realization result, and no OFN or FMS verdict.
- **Open.**
  - OFN Q6-REG.
  - Physical selection of model C (OFN/FMS).
  - DYAD OPEN 20.
  - γ ∈ {0,2}; C¹/C² planar factors; 𝒟-spectrum targets; non-planar decouplings.

## 4. Outbound notices (issued now, citing the adopted hash `d143673e…c6fc`)

**→ OFN. Informational; supersedes the SESSION-level D-4 notification.**
- Genesis v2.8.9 is adopted (`d143673e9596abc900f54f269582299c87c9146504d6c9e1fd08ac294ba8c6fc`). It adds `GEN-THM-TRANSPORTED-CHIRAL-FACTOR-NOGO` (§6.3c).
- **What it states:** no local C³ submersive six-step factor (d = 1–3) exists for real C³ network germs with the stated linear structure, zero quadratic part and chiral cubic invariant μ ≠ 0, under (H_spec), for γ ∉ {0,2}.
- **Primitive clock:** the companion statement under (H_prim) is `[ALG]` without RID, at the same grade as the adopted §6.3b primitive statement.
- **Use for Q6.** The narrow Q6 planar-decoupling forms of OFN v0.7.2 §3.1 are covered at the primitive clock **only at the `[ALG]` grade**, and only if passive transformations are local C³ conjugacies.
- **Still OFN's decision:** Q6-REG, and whether the narrow planar-product reading is the governing contract.
- **Not established:**
  - existence of an analytic Dyadic J or of an exactly transported realization;
  - any physical realization;
  - selection of model C. The obstruction does not even distinguish model C from its third-jet equivalents.
- **Citation:** cite the RID together with its hypotheses. Do not cite the primitive companion as a theorem.

**→ RRF (G2-CLOCK). Informational.**
- New exportable RID `GEN-THM-TRANSPORTED-CHIRAL-FACTOR-NOGO`, six-step contract, with the hypotheses of §6.3c.
- The primitive and six-step contracts remain distinct, consistent with RRF v0.8.3.
- No carrier, encoding or G2 realization is selected.
- Existing exports are byte-identical.

**→ FMS. Informational.**
- The transported-family Q6 entry can now cite an adopted six-step Genesis RID. The primitive entry remains `[ALG]`.
- No class verdict is made by Genesis; physical selection stays with FMS/OFN.
- Suggested ledger housekeeping: register the Standard C route, and refresh R7 to the adopted Genesis RIDs.

**→ Dyadic. Informational; no action required.**
- Genesis v2.8.9 imports no new Dyadic RID.
- μ₆ is recomputed in the certificate from `DYAD-DEF-PRIMITIVE-MAP`.
- Pins remain v6.4.13. The repin to v6.4.14/v6.4.15 is deferred; N10/N11 report no change to any imported RID.
