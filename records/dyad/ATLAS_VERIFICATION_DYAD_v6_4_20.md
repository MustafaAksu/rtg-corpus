# Atlas Verification — Dyadic Oscillator DSN v6.4.20 against the FINAL Advisory v1.0

**From:** the atlas owner (Claude). **To:** the Dyadic stream owner and the PI. **Date:** 21 October 2026.
**Status:** noncanonical verification note. It is not an amendment and not a review verdict. The owner DSN governs.

**Checked object:** `RTG_DYADIC_OSCILLATOR_DSN_v6_4_20.md`, 2793 lines, 411,765 bytes, adopted 21 Oct 2026.
- SHA-256 **`0b2d5a44eb818598bb330464dfa4f2e9d75521715f577a7c2e589e165f1a4852`**, recomputed by the atlas owner on the delivered file. It matches the release record (§1).
- Package `SHA256SUMS.txt`: 12/12 OK in a clean directory.
- The PI decides whether this independent recomputation counts as the "external verification of the final SHA-256" that the release record leaves pending. The algorithm is the same; the session is a different one.

**References:**
- `ATLAS_ADVISORY_DYAD_v6_4_19_FINAL_v1_0.md` (34 rows);
- `ATLAS_DISPOSITION_DYAD_v6_4_19_SESSION_v0_1.md` (owner decisions);
- `RTG_DYADIC_v6_4_20_RELEASE_RECORD.md`;
- base `RTG_DYADIC_OSCILLATOR_DSN_v6_4_19.md` (from the package, `base_v6_4_19.md`).

**Method:**
- Each advisory row was located in v6.4.20 by RID, phrase and section.
- Every leftover string from v6.4.19 was located by line number.
- A leftover is counted as residual only when it is in live text (§§0–9, App. B–G). Quotations inside Appendix A are history by design and are not counted.
- Atlas re-derivations are listed in §4.

---

## 1. Result in one line

All 34 advisory rows are dispositioned:
- **28 are implemented** in the adopted text: 22 fully, 6 with a small residual. FB-11 went beyond scope by recovering OPEN 9 definitions that the disposition had deferred.
- 3 are deferred or routed with a stated target, as the advisory allowed (FC-31, FC-32, FC-33).
- 2 are notices to be sent after hash verification (FB-19, FB-21).
- **1 accepted row was neither implemented nor recorded as deferred (FC-34).**

Residuals:
- **Seven live-text residuals (R1–R7).** One (R1) can mislead a reader; the others are minor.
- **One structural regression (R8).** Appendix A grew by about 92k characters of draft-round records.

No new scientific error was found.

## 2. Row-by-row status

Legend: ✅ implemented · ◐ implemented with a residual (see §3) · ⏸ deferred or routed, target stated · ✉ notice planned after hash verification · ✗ accepted but not implemented.

| Row | Status | Where in v6.4.20 | Note |
|---|---|---|---|
| FA-01 R9 dependency | ✅ | §7 "Dependency structure" + claim-level imports (R9 with rows; A1A reciprocal amplitude) | acyclic chain stated; custody unchanged |
| FA-02 one status per module | ◐ | §2 OPEN 3/20/21 cleaned, queue rebuilt (§2 L153–158), §6.9 R11 sentence turned into a guard, App. B L2509 corrected | **R1, R2** |
| FA-03 summaries mirror hypotheses | ◐ | §5 rows (DG(0)=I restored; "not implied by … alone"); SG-16 violation clause (L397) | **R3** |
| FA-04 VANISH-B2 explanation | ✅ | §6.11 L694 (a+b−1 bound, COR) + certificate audit block | `degree_b_vanishing_cert_v2.py` recorded as unavailable |
| FA-05 field labels | ◐ | §6.2, §6.9, §6.11 L685 (ℚ(ζ₅)) | **R4** |
| FA-06 §6.6 tiers | ✅ | §6.6 L575–583: [ALG] linear order; resonance condition; [DEF] classification; RECOG-scoped radial rate (p≥5, Z frame, with tan² note); harmonic count [OPEN] | owner corrected the atlas's p=7 value (−1.3178, not 1.316) |
| FA-07 frame typing | ✅ | §6.9 `DYAD-ALG-KP-FRAME-SCALE` [ALG], proved; §6.11 L729 typo fixed | atlas PASS, §4 |
| FA-08 RAW-CUBIC | ✅ | §2 OPEN 9: statement recovered (raw one-step z²z̄ coefficient, Z_p frame, v5.x table source) | match with the historical source stays open, as recorded |
| FB-09 crosswalk | ✅ | Appendix F | every DZT/AZ string classified |
| FB-10 result RIDs | ✅ | 13 new RIDs (B5-ALLP-NONVANISHING, RAW-ANGULAR-MEAN, ONE-BLOCK-BURST, P5-RADIAL, SIXSTEP-CUBIC-JET, Q3-DEG2-CANCEL, CRITICAL-CURVE, QC, ISP-MAPS, …) | 135 → 148, none renamed |
| FB-11 OPEN 9 definitions | ✅ | Appendix D | done although the disposition had deferred it |
| FB-12 leading decay vs fit | ✅ | §6.5 L549 [THM] import, L551 [DEF] historical ansatz, κ_bb | — |
| FB-13 smooth equivariant chart | ✅ | §6.17 `DYAD-THM-SMOOTH-EQUIVARIANT-CHART` with proof, scope and GEN C2 interface | notice N16 pending |
| FB-14 L-PHASE export | ✅ | §7.0a I1–I5 table; domain asymmetry; GAP-LOCK pointer (§6.14 L951, §7.0a) | — |
| FB-15 sign + DZT | ✅ | §2 L252 | asymptotic part → FC-31 |
| FB-16 editions table | ✅ | §7.0 | hashes given where held; otherwise "not recorded" |
| FB-17 RECOG promises | ✅ | §7.0 (v0.3.20 frozen / v0.3.21 / v0.3.22); addenda record (p2r2) | — |
| FB-18 notice states | ✅ | §7 notice table, one recipient per row | N12→RRF and N14→FMS/OFN "NOT RECORDED" |
| FB-19 N16–N20 | ✉ | release record §7 | after hash verification |
| FB-20 threshold citations | ◐ | §1 L140, §6.12 L773 | **R5** |
| FB-21 S_h routing | ✉ | N19 | — |
| FB-22 orientation | ◐ | header now about 8k (was about 20.7k); single live footer | **R8 (Appendix A growth)** |
| FB-23 notation | ◐ | Appendix C | **R6** |
| FB-24 grammar/format | ✅ | tag normalization map; 0 double-escaped LaTeX; setext bug fixed (L298); CAND lookup; "exceptional orders"; one context marker | — |
| FB-25 c_θ cell | ✅ | §5 row | Genesis via N16 |
| FB-26 SG-PROG-2 | ✅ | SG-14 L390; export protocol | — |
| FB-27 registry hygiene | ✅ | OPEN 2B alias; OPEN 4b label qualified; SG-17/18 line | — |
| FB-28 fixed-point scope | ✅ | §1 L84–92 table | atlas PASS, §4 |
| FB-29 evidence matrix | ✅ | Appendix E | — |
| FB-30 constant identities | ✅ | §6.3 L516; App. C | — |
| FC-31 large-p cascade | ⏸ | §2 L252 names it as a Tier-C target | deferral is valid; premise is PHASELAW only |
| FC-32 R9-free existence | ⏸ | Appendix A, P1 record (SESSION) | offered to RECOG/NUMGEN via N18/N19; the optional DYAD-side lemma Σ\|r_m\|<∞ is not registered |
| FC-33 lag sign | ⏸ ✉ | not in the DSN; N18 | acceptable as notice-only |
| FC-34 16/3 cross-reference | ✗ | not found anywhere in v6.4.20 | **R7** |

## 3. Residuals in live text

**R1 | FA-02 | misleading | §1 L128.** The OPEN 3 summary line still ends "OPEN 3 is PARTIAL: asymptotic-phase transfer (P4) OPEN." §2 L178 and the closed list say OPEN 3 is CLOSED (v6.4.16) within its scope. *Fix:* "OPEN 3 is CLOSED within its defined scope (§2); the primitive-variable remainder is OPEN 21 (CLOSED, v6.4.17)."

**R2 | FA-02 | minor | §2 OPEN 9.**
- The "Active sub-items" list still contains two CLOSED entries: the q=4,(0,3) cascade formula, and "Channel boundary all-p … CLOSED [ALG]".
- "Next required artifacts" keeps a struck-through DONE line.

*Fix:* move both entries to "Closed sub-items" as pointers, and drop the struck line.

**R3 | FA-03 | minor.**
- §2 closed-OPEN list, OPEN 19 line: "formal centralizer of T⁶ is {exp(sX)}" lacks DG(0)=I. §5 and §1 L124 are correct.
- §1 L126 ends the F1–F3 summary with "No existence is asserted." without the pointer that §5 now carries.

*Fix:* add "(tangent to the identity)" to the OPEN 19 line, and add "existence: DYAD-THM-SMOOTH-EMBEDDING (L134)" at L126.

**R4 | FA-05 | verify | §1 L112.** "Archival Lie-gauge 6-step object: h₄ exact over ℚ(√3)". If the archival h₄ coefficients are complex, which is likely in the W frame, the label should read ℚ(i√3), or say that the components lie in ℚ(√3). The owner should check this against `normalize_p6_liegauge_exact.py`.

**R5 | FB-20 | minor | §6.11 L704 (DYAD-ALG-P6-FACEFLUX block).** It still names only "OPEN-GEN-II-7B [HYP]" as the source of the 0.024 threshold. §1 L140 and §6.12 L773 now give GEN-OPEN-UVJET-SCOPE, OPEN-M R16 and the five inherited conditions. *Fix:* add the same pointer at L704.

**R6 | FB-23 | minor | Appendix C.** Three overloads named in the advisory are missing from the table:
- ISP U=(√3/2)ρ (§6.4 L539) versus the tube U (§6.14);
- the OPEN-M source amplitude h (SG-15, §6.11–6.12) versus the normalizer h;
- the NF-INV contraction constant κ=M′(R) versus κ_bb.

*Fix:* three table rows.

**R7 | FC-34 | accepted, not done.** The disposition (§4, FC-34: "ACCEPT (reference note only)", P2) planned an optional cross-reference: (4√3/3)² = 16/3 = Genesis's (4/3)/(1/4). It is not in v6.4.20, and neither the release record nor Appendix A lists it as deferred. *Fix:* add one line in §6.12, or record a dated deferral.

**R8 | FB-22 | structural regression.** The header shrank as intended (20.7k → 8.0k), but Appendix A grew from about 58.8k to about 150.7k characters:
- adoption record: 21.6k;
- DRAFT r2 record: 13.2k;
- DRAFT r1 record: 44.1k;
- P1 working record: 13.2k.

The file grew overall from 276k to 412k. The live body is roughly unchanged at about 217k, with useful new content including Appendices C–G (39k). The draft-round records are already preserved as separate session files in the project (`claude/atlas/p1`, `p2`, `p2r2`). *Suggestion:* in the next edition, keep in Appendix A only the adoption record, with pointers and hashes to the draft and session files. The 55 verbatim-quoted lines can stay as an old→new map in the release record. This affects AI readability and token cost, not correctness.

## 4. Atlas checks re-run on v6.4.20 (PASS)

- **SHA-256 of the delivered file:** matches the release record (`0b2d5a44…4852`). Package `SHA256SUMS.txt`: 12/12 OK.
- **DYAD-ALG-KP-FRAME-SCALE:**
  - u = 1/(1−λ) = ½ + (i/2)cot(π/p).
  - K_p = (1−λ)(1−λ̄), so (λ−1)/K_p = −ū and W_p = (u−ū)Z = i·cot(π/p)·Z.
  - Hence μ^{W_p} = μ^Z·tan²(π/p). At p=6, cot²(π/6)=3, consistent with μ^Z = 3μ^W and with [G]'s check W = i√3 Z.
- **Fixed-point table (§1):**
  - sin η = 0 and e^ρ = 1 give (0, mπ) on the lift.
  - On the cylinder, e^ρ − 1 = 2πk gives (log(1+2πk), 0 or π), k ≥ 1.
- **§6.6 resonance claim:** a−b−1 ≡ 0 (mod 6) forces a+b to be odd, and (a,b) = ((d+1)/2, (d−1)/2) gives a resonant monomial at every odd degree d.
- **§6.5 leading decay:** the statement as written follows from the RECOG lemma. No proof dependency on R9 or on A1a results.
- **§6.11 VANISH-B2 correction:** (x+x²)∘(x+x²) = x+2x²+2x³+x⁴. The conclusion holds.
- **No 136-RID loss:** the release record reports 135 tagged RIDs (v6.4.19) → 148. Every advisory-requested RID that the atlas looked for is present.
- **Atlas self-correction:** at p=7, −p sin²(π/p) = −1.31779. The FINAL advisory printed 1.316. The owner's value is right.

## 5. Operational items (PI)

1. **Installation.** The adopted v6.4.20 is **not** in the project: the write was refused at the project size limit (release record §5). The project currently holds several full-size working copies, including `claude/atlas/p1/RTG_DYADIC_OSCILLATOR_DSN_v6_4_20_P1_WORKING.md`, `claude/atlas/p2/…DRAFT_r1.md` and `claude/atlas/p2r2/…DRAFT_r2.md`, each about 400k. They are hash-pinned in the release record and kept in the package, so they are candidates to remove to make room. The PI decides.
2. **External hash verification and notices.** If the PI accepts §4's recomputation as the external check, notices N16–N20 can be prepared, citing `0b2d5a44…4852`.
3. **Residuals R1–R8.** None blocks the adopted release. They can go into the next DYAD edition, for example a small v6.4.21 metadata/editorial release together with the notice receipts. R1 is the only one that can mislead a reader and should come first.
4. **Atlas refresh.** On installation, the atlas DYAD slice is regenerated from v6.4.20. The five atlas corrections of the FINAL advisory §5 and the p=7 value are applied at the same time.

*End of verification note. No DSN was edited; no notice was sent.*
