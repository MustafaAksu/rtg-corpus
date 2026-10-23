# RECOG G2 — Dyadic Source-Fidelity Run and Proposed Final Dispositions v0.1.1

**v0.1.1:** identical to v0.1 (`8cb01193…15ecb`, the reviewed record) in §§1–6; adds §7, the receiving disposition of 20 October 2026.

**Date:** 20 October 2026
**Status:** `[SESSION]` execution record, supplementing `RECOG_G2_DYADIC_CLAIM_AUDIT_v0_1_2.md` (`99fce74b…20aa`).
- It proposes final CLAIM_EQUIVALENT dispositions for A1–A18. They become final only on the reviewer's acceptance.
- No DSN is edited, and RECOG v0.3.20 (FROZEN) remains authoritative.
- No Dyadic v6.4.17 claim is accepted into RECOG.

## 1. Inputs (hashes recomputed in session)

| File | SHA-256 | Expected | Match |
|---|---|---|---|
| `RTG_DYADIC_OSCILLATOR_DSN_v6_4_10.md` (PI upload, 1,024 lines) | `7455811928606076b3bc3075632275dc2a24e37fdbf0ae20036db5529a1b56b7` | RECOG §8 pin | **yes** |
| `RTG_DYADIC_OSCILLATOR_DSN_v6_4_17.md` (PI upload, 1,502 lines) | `e07cf2b93b532554d9e1d05d2bfef3be34829b7cb892627c0bb03d1d182d4bfc` | v6.4.17 release record / N13 | **yes** |
| `recog_g2_dyad_passage_diff.py` v0.3 | `8af2a00d…a364` | audit v0.1.2 | yes |

**What this run covers.**
- The run compares the **pinned** edition (v6.4.10) directly with the **reported current** edition (v6.4.17); that is the comparison a consumer import verdict needs.
- The reviewer's v6.4.16 self-runs (18/18 anchors) establish anchor presence in the verified intermediate edition.
- A v6.4.16 ↔ v6.4.17 comparison would serve Dyadic's own release verification. It is not needed for the consumer verdicts and is not claimed here.

**Qualification adopted.** Per the review, `BYTE_IDENTICAL` means exact equality of the selected lines. It does not mean literal equality of raw byte spans, because blank-line separators and line endings are not compared. The script text is left unchanged so that the hash of the executed version stays stable; the qualification is recorded here.

## 2. Reports (run in session; files attached)

| Run | Mode | Exit | IDENTICAL | DIFFERS | Report SHA-256 |
|---|---|---|---|---|---|
| default | whitespace-normalized, `--extend 0` | 1 | 15 | 3 (C21, BRIDGE-LEMMA, NU5-1-6) | `44731941…21a6` |
| `--bytes` | exact selected lines | 1 | 15 | 3 (the same) | `21f556cb…454b` |
| `--extend 1` | normalized | 1 | 13 | 5 (+ CONST-6.3, OPEN12) | `98e760a2…a079` |
| `--extend 2` | normalized | 1 | 11 | 7 (+ NF-REM, LIEGAUGE-NORM) | `bc6268ba…0a66` |

All 18 anchor groups were found in both editions in every run (no exit 2).

## 3. Coverage check from the printed line ranges

- **The operative statement block is selected for every passage**, in the same order in both editions. Examples: NF6 at v6.4.10 L633–638 and v6.4.17 L735–740; NF-REM at L652 + table L654–657 and at L754 + L756–759.
- **One coverage gap appeared at `--extend 0`.** For **OPEN12** only the heading line was selected; the status block sits in the next paragraph. `--extend 1` captures it (L197–198 and L229–230), and the difference it then shows is the expected status change (§4). For **NF-REM**, the constants-and-ingredients paragraph after the table is captured from `--extend 1` (L659 and L761) and is identical.
- **The `--extend 2` runs mostly pick up neighbouring paragraphs** that are not part of the imported claims. The new differences they show are insertions next to the claims, not edits to them (§4).

## 4. Disposition of every differing block (reviewer to confirm)

| Passage | Where the difference is | Content | Effect on the imported claim |
|---|---|---|---|
| C21 | closed-OPEN list (v6.4.10 L228–232 → v6.4.17 L288–295) | three lines **added**: OPEN 3 closed, OPEN 21 closed, OPEN 19 closed | none. The operative lines L40 and L365–367 (v6.4.10) equal L55 and L441–443 (v6.4.17); c₂₁ and its `[THM]` grade are unchanged. |
| BRIDGE-LEMMA | one line **added** after the statement (v6.4.17 L598) | the v6.4.11 cross-reference to RECOG §6.12 as general-p proof provenance; "Dyadic RID and statement retained" | none on the statement. This is exactly the A7 mutual-citation finding, and its guard stands. |
| NU5-1-6 | the p = 5 line of the finite-ledger block | DYAD-ALG-NU5-P5 closed form **appended** (v6.4.13) | none. RECOG imports only the p = 6 line c₀₅^(1,6) = 43/17280 − i·227√3/155520, which is unchanged. NU5-P5 is new upstream (N), not used by RECOG. |
| CONST-6.3 (`--extend 1`) | the block after the constants display | v6.4.10: next heading (§6.4); v6.4.17: the inserted "Definition-ledger identities (v6.4.11)" paragraph | none. The constants display (L379–380 → L455–456) is identical. The inserted paragraph carries the A14 RIDs (N / dual-registration finding). |
| OPEN12 (`--extend 1`) | status block | ACTIVE / `[OPEN]` → PARTIAL (v6.4.11, by consumer theorems), importing RECOG-THM-P2-HET and RECOG-THM-P2-C0-FIRST; remaining: global W^s(P₂), later C₀ re-intersections, large amplitude | as recorded in A18: owner status changed (**CS**), consistent with RECOG R3; R3 owns only the first residual item |
| NF-REM (`--extend 2`) | the block after the ingredients paragraph | v6.4.10: the "Not established by this section" paragraph; v6.4.17: the inserted DYAD-ALG-NF6-DEG10 block | none. The theorem paragraph, the table and the ingredients paragraph are identical. DEG10 is new upstream (N), already respected by SG-R13. |
| LIEGAUGE-NORM (`--extend 2`) | the bridge-lemma block reached by extension | the same added cross-reference line as BRIDGE-LEMMA | none |

**Additional checks.**
- A4: ΣQ_m² ≤ 2Q₀ is present in v6.4.10 as well (one occurrence in each edition). A4's open sub-question is therefore settled: **U**.
- The NF-REM certificate values 85.07 / 812.89 / 27.60 / 216.77 are present in v6.4.10 L656–657.

## 5. Proposed final dispositions A1–A18

| Row | Final verdict (proposed) | Basis |
|---|---|---|
| A1 C21 | **U** | operative lines identical; only list additions |
| A2 NF6 | **U** (statement); **S** (evidence, v6.4.16 provenance, outside the compared block) | identical |
| A3 NF6-OBS | **U** | identical |
| A4 PRIM-CTR | **U** | identical, including ΣQ² ≤ 2Q₀ |
| A5 NF-INV | **U** | identical |
| A6 NF-REM | **U** | theorem, table and ingredients identical through `--extend 1` |
| A7 BRIDGE-LEMMA | **U**, with the mutual-citation guard | statement identical; provenance line added |
| A8 P6-FACEFLUX | **U** | identical |
| A9 ALIAS-PHASE | **U** | identical |
| A10 LIEGAUGE-NORM | **U** | identical through `--extend 1` |
| A11 §6.1 block | **U** content; **ID** (DYAD-DEF-PRIMITIVE-MAP is absent in v6.4.10 and present in v6.4.17) | MAP-6.1 identical |
| A12 §6.4 block | **U** | identical |
| A13 §6.7–6.8 block | **U** | identical |
| A14 §6.3 constants | **U**; N for the inserted definition-ledger RIDs | display identical |
| A15 h₂ | **U** | identical |
| A16 ν₅^(1,6) | **U**; N for NU5-P5 | p = 6 line identical |
| A17 47/54 | **U** | identical |
| A18 OPEN 12 | **CS** (owner status), consistent with R3 | status block differs exactly as recorded |

**Conclusion (proposed).**
- No load-bearing import changed its statement, hypotheses, domain, rows, chart, constants or grade between the pinned v6.4.10 and v6.4.17.
- Every differing block is an addition next to an imported claim, or the anticipated OPEN 12 status change.
- The six findings and the N10–N13 receipt semantics of v0.1.2 are unchanged. N13 stays a conditional receipt, because source verification ≠ release verification ≠ consumer acceptance.

## 6. Attached reports

- `g2_dyad_passage_diff_v6_4_10_vs_v6_4_17.txt` (default)
- `g2_dyad_passage_diff_v6_4_10_vs_v6_4_17_bytes.txt`
- `g2_dyad_passage_diff_v6_4_10_vs_v6_4_17_extend1.txt`
- `g2_dyad_passage_diff_v6_4_10_vs_v6_4_17_extend2.txt`

The reviewer can reproduce any of them with the two uploaded files and script v0.3.

## 7. Receiving disposition (20 October 2026)

> **G2-DYADIC — CLOSED at source-fidelity/claim-equivalence scope.** The 18 consumer rows A1–A18 have been reviewed against the supplied v6.4.10→v6.4.17 comparison evidence. No scientific import statement, domain, normalization, constant or grade change requiring a RECOG regrade was identified. A2 carries stronger evidence, A11 an identifier registration, and A18 the documented owner-status transition. N13 remains conditional pending separate release verification and consumer acceptance.

**Evidence boundary (reviewer).** The reviewer accepted the reported comparison results and checked the hashes of all four reports. The source editions were not mounted in the reviewer's workspace, so the reviewer did not run a second comparison against them.

**Still in force:**
- N11 remains eligible for the narrowly scoped SG-R14 reference, with its row-specific bounds and its dependence on R9.
- The mutual-citation guard (A7) is maintained.
- This disposition does not authorize v0.3.21 publication. RECOG v0.3.20 remains the frozen authority.
