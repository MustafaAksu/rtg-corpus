# RECOG A1a — E2 receiving source check against Dyadic v6.4.18

**Date:** 20 October 2026  
**Status:** `[SESSION]` independent **SOURCE-STATEMENT VERIFICATION PASS on adopted Dyadic v6.4.18** for A1a block (c). Not a rerun of the Dyadic P5 proof certificate, not an adoption/release decision, and not a byte comparison against v6.4.17.  
**Input draft:** `RECOG_A1A_CELL_DRAFT_v0_3.md`, SHA-256 `febed7f985f6e19b35b572c0ac329777e342ebe3d15388cc7c04d6e934009562`, 202 lines.  
**Inspected owner:** `RTG_DYADIC_OSCILLATOR_DSN_v6_4_18.md`, SHA-256 `f70308f19f5955c0597c03a27b572abfd4c8746aef6922c959675eb0d56e458d`, 256,933 bytes, 1,539 lines; the adopted owner source itself was present and rehashed.  
**Other owner context:** RECOG adopted v0.3.21 §6.13a / RECOG-THM-R9-MEMORY (`a3459522…0ae3`). This source check does not rerun R9's Arb certificate.

## Statement-level verification

1. **Primitive formal form** — DYAD v6.4.18 §6.14, lines 806–809 (`DYAD-ALG-OPEN3-PHASE-OFFSET`): source explicitly grades the primitive second-order expression `[ALG — formal second order; remainder not certified]`, and states `P_{W2}=-Δ_2+DΔ_1[h_2]`. The A1a draft gives the same Δ₁ and P_{W2} harmonic expressions, and keeps the certification separate. PASS. Independently computed in exact symbolic Laurent arithmetic from Dyadic's $h_2$, Δ₁ and Δ₂: `P_{W2}+Δ₂-DΔ₁[h₂]=0` identically. PASS.
2. **OPEN 21 owner theorem** — v6.4.18 §6.14, lines 843–850, RID `DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER`, explicitly attributed in the owner text to v6.4.17 and graded `[THM — conditional on RECOG-THM-R9-MEMORY]`. Exact statement is `|M_W-𝒫₂(W₀)|≤K'_j Q₀^(3/2)+C_{2,j}(256/225)^2 Q₀^2`; A1a block (c) transcribes this without promoting the owner theorem's grade. PASS.
3. **Certified rows** — owner v6.4.18 §6.14 lines 846–849: A `|W₀|≤3/64`, chart disk `|z|≤1/20`, `K'_A=3951/1000`, `C_{2,A}=517`; B `|W₀|≤3/128`, chart disk `|z|≤1/40`, `K'_B=971/250`, `C_{2,B}=163`. All equal the draft. Secondary constants A `8831/250`, B `883/100` are in the source but are not asserted by the draft. PASS. The owner makes the A/B profiles separate, as does the draft.
4. **Exact auxiliary arithmetic** — `517*(256/225)^2=33882112/50625`, `163*(256/225)^2=10682368/50625`. Secondary-bound checks: `8831/250 - (3951/1000 + 517*(256/225)^2*(3/64))=91/135000>0`, `883/100-(971/250+163*(256/225)^2*(3/128))=31/67500>0`. PASS.
5. **A1a domain transfer** — on the separately proved A1a local start domain, `16/15 * 1/25 = 16/375 < 1/20`, and `16/15 * 3/128 = 1/40`; hence the clipped A row and B row in the draft do not widen the owner's theorem. PASS.
6. **Dependency and scope** — v6.4.18 explicitly keeps the theorem conditional on R9, its $C_2$ contribution separate, and forbids transferring it to comparator `C_W^(h)` or to NUMGEN L1/ISP-angle coefficients. A1a invokes adopted R9 at statement-level to discharge that condition for its own mathematical block (c); it makes no assertion about the comparator. PASS.

## Evidence limits and decision

- **E2, interpreted as checking block (c) directly against the current adopted Dyadic owner edition v6.4.18: PASS.** Independent evidence for the exact exported theorem statement, its coefficients, frame, rows and assumptions is now available.
- **Historical edition equivalence:** the complete v6.4.17 file was **not available** in this runtime. The owner says §6.14 is byte-identical between v6.4.17 and v6.4.18; this claim is **owner-reported, not independently checked here**. Therefore do **not** describe the v6.4.17 line-837 source pin as independently verified.
- To use this E2 result in a future A1a revision, **repin block (c) and its import to adopted `RTG_DYADIC_OSCILLATOR_DSN_v6.4.18.md`**, §6.14, lines 806–809 and 843–850, owner theorem RID preserved, SHA-256 above. Historical v6.4.17 attribution may remain as a provenance note clearly labelled owner-reported. The precise draft change has not been made here.
- The Dyadic P5 28-gate certificate and RECOG R9 Arb proof were not independently rerun here; the check is an **owner-source fidelity check**, not a new mathematical certification. E2 does not register an A1a RID, determine release readiness or change any owner status.
- G1 NUMGEN missing-RID disposition and G2 primitive-form provenance annotation remain routine publication-preparation edits. Adopted RECOG v0.3.21 and R6 ACTIVE remain unchanged; G3 OFN/RRF/RER dispatch is separate.
