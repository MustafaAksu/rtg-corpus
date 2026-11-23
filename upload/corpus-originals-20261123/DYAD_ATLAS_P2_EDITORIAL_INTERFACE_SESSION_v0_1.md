# DYAD ATLAS P2 — Editorial and Interface Pass — Session Record v0.1

**Date:** 21 October 2026 · **Owner:** Dyadic DSN (Claude) · **Status:** `[SESSION]` owner record. The draft it documents is **not adopted and not released**.

- **Authority:** `ATLAS P1 — SCIENTIFIC REVIEW ACCEPTED` (reviewer, 21 Oct 2026), which authorizes P2.
- **Output:** a single draft, `RTG_DYADIC_OSCILLATOR_DSN_v6_4_20_DRAFT_r1.md`, SHA-256 `a5c70f5b1468ab01ba1cdf932fb9205c4bf00976a2b6523e8b90210e5e457c4a` (2375 lines).
- **What comes next is separate:** external review of r1, then an explicit PI adoption decision.
- **Official state unchanged:** DYAD v6.4.19 (`40c9e63f14baef581db9ef4a362ea8f8ac1f124c9f29a63f6b1c3f8931686ec9`) is the adopted ledger. OPEN 20 is PARTIAL; B-an and B-6 are OPEN.
- **Not done here:** nothing is adopted or released, and no notice is sent or prepared. N16–N20 come only after a release, with its verified hash.

## 1. Base and inputs

| Input | SHA-256 | Role |
|---|---|---|
| `RTG_DYADIC_OSCILLATOR_DSN_v6_4_20_P1_WORKING.md` | `6f30f347b4f896a512cc7f1018d57721e33889d70e039fbb69377770fdc2c905` | base (verified P1 working file) |
| `RTG_DYADIC_OSCILLATOR_DSN_v6_4_19.md` | `40c9e63f14baef581db9ef4a362ea8f8ac1f124c9f29a63f6b1c3f8931686ec9` | census and section-map reference; unchanged |
| RECOG v0.3.20 | `fdb8c9a72cbea67bae339a890f440b7d67c608979f7886279e2cd00bdabfb8df` | frozen; historical pins |
| RECOG v0.3.21 | `a3459522c8f58204f83f5e65e3d1a99912f9651d1c17cc4fb0c090196f670ae3` | superseded adopted edition |
| RECOG v0.3.22 | `0dcce9e44d48fbedbcd5af083283fce12560cc17a3951a7632ff0e50db44bcd9` | current; receipts §7.2 |
| NUMGEN v1.20.8 | `835a56f82b2641343a0e2fa116b049a167c62efd4d13fe41236966c117f4817e` | I1–I5 targets; receipts §9.1; GAP-LOCK lemmas |

All six hashes are checked by `p2_source_checks.py` S1.

## 2. What the draft does

The draft is built mechanically from the P1 working file by `build_dyad_v6_4_20_r1.py`, in three stages:

1. **Anchored edits P01–P36.** Each anchor must occur exactly once. Twelve passages are relocated, and each one is quoted verbatim in Appendix A as H-P2-1…H-P2-12.
2. **Global transforms.** These are:
   - tag normalization (§3 below);
   - P1 markers become `[v6.4.20` markers;
   - §6 headings carry their entry grades;
   - the one-tag RID rule (§4 below);
   - repair of double escapes;
   - "breaker primes" becomes "exceptional orders".
3. **Inserted blocks.** These are:
   - a compact header;
   - the tag tables;
   - the rebuilt §7: §7.0 editions with the historical-pin note, §7.0a, the L-PHASE I1–I5 export table and the notice-state table;
   - new appendices C (notation), D (OPEN 9 definitions), E (claim-to-evidence matrix), F (DZT/AZ crosswalk) and G (old→new section map);
   - a single footer;
   - the draft record in Appendix A.

**Disposition items covered:** FB-DYAD-09, 10, 11, 14, 16, 17, 18, 20, 22, 23, 24, 26, 27, 28, 29, 30, plus the section map. Tier-C items FC-31 and FC-32 are outside the draft.

## 3. Tag normalization map

Legacy compound tags are rewritten into canonical tag sequences. No grade changes. The alias table in "Local Tag Aliases" is excluded from the rewrite.

| Legacy | Canonical |
|---|---|
| `[ALG, exact]` | `[ALG]` |
| `[ALG, exact under OPEN-P0 representation-phase convention]` | `[ALG]` `[assuming: OPEN-P0 representation-phase convention]` |
| `[ALG structure]` | `[ALG]` `[scope: structure]` |
| `[ALG structure / NUM strong]` | `[ALG]` `[scope: structure]` `[NUM]` `[scope: strong numerical evidence]` |
| `[ALG candidate]` | `[CAND]` `[target: ALG]` |
| `[ALG finite sweep]`, `[ALG validation]` | `[ALG]` `[scope: finite sweep]`, `[ALG]` `[scope: validation]` |
| `[ALG — formal]`, `[ALG — formal second order; remainder not certified]` | `[ALG]` `[scope: …]` |
| `[ALG / ENG]`, `[ENG / NUM strong]`, `[NUM strong]` | `[ENG]` `[ALG]`; `[ENG]` `[NUM]` `[scope: strong numerical evidence]`; `[NUM]` `[scope: strong numerical evidence]` |
| `[CAND/conditional]`, `[HYP inherited]` | `[CAND]` `[scope: conditional]`; `[HYP]` `[scope: inherited]` |
| `[THM — analytic]` | `[THM]` `[scope: analytic]` |
| `[THM — conditional on RECOG-THM-R9-MEMORY]`, `[THM — conditional on R9]` | `[THM]` `[assuming: RECOG-THM-R9-MEMORY]` |
| `[THM — conditional on T1]`, `[THM — conditional]` | `[THM]` `[assuming: T1]`; `[THM]` `[assuming: hypotheses stated in the entry]` |
| `[THM/ALG]`, `[THM/ALG, all-$p$]`, `**[CLOSED v6.4.9, THM/ALG]**` | `[THM]` `[proof: exact algebraic identity]` (plus scope or the CLOSED label) |
| `[COR v6.4.10]`, `[COR v6.4.11]`, `[COR v6.4.11: …]`, `[P1 COR]` | `[COR]` followed by a version span |

Mixed tags that appear only in §6 headings (for example `[ALG / mixed]`) are replaced by "— entry grades: …", computed from the tagged entries under each heading. §6.13 has no tagged entries, so its heading keeps `[ENG]`. The draft prints the full map after the Local Tag Aliases, with occurrence counts in `p2_edit_log.json`.

## 4. RID census

**Two census rules.** These explain the "136" of the P1 record.

- **Census A** counts identifiers inside `[RID: …]` tags.
- **Census B** counts every RID-shaped string `DYAD-(ALG|THM|DEF|OPEN|ART|CAND|NUM|CF)-…`.

| File | Census A | Census B |
|---|---|---|
| v6.4.19 (adopted) | 135 | 136 |
| P1 working file | 137 | 138 |
| v6.4.20 DRAFT r1 | 148 | 159 |

- The "136" in the P1 record is Census B; the P1 checker's G1 regex counted 131.
- Three strings appear in v6.4.19 Census B without a tag: `DYAD-ART-B5-LIMIT-CERT`, `DYAD-CAND-PHISTAR-ENTRY-PHASE` and `DYAD-OPEN-B5-ALLP`.
- r1 Census B is larger mainly because Appendix F quotes DZT/AZ strings.
- **Gate G2 result.** Every P1 tagged identifier is still tagged. The new tagged set is exactly the eleven P2 proposals. Every v6.4.19 Census-B string is present. The FA-07 candidate (`DYAD-ALG-KP-FRAME-SCALE`) and the FB-13 candidate (`DYAD-THM-SMOOTH-EQUIVARIANT-CHART`) are still tagged.

**Eleven proposed RIDs (P2), registered only at adoption:**

| RID | Grade | Where | Evidence |
|---|---|---|---|
| `DYAD-ALG-B5-ALLP-NONVANISHING` | ALG | §6.11 | existing §8 certificates; not rerun in P2 |
| `DYAD-ALG-RAW-ANGULAR-MEAN` | ALG | §6.5 | M8 |
| `DYAD-ALG-ONE-BLOCK-BURST` | ALG | §6.5 | M7 |
| `DYAD-ALG-P5-RADIAL` | ALG | §6.14 (new entry) | M6 |
| `DYAD-ALG-SIXSTEP-CUBIC-JET` | ALG | §6.7 | M5 |
| `DYAD-ALG-Q3-DEG2-CANCEL` | ALG | §6.11 | existing record; AZ `DYAD-ALG-Q3-CANCEL` stays unmatched, with no alias |
| `DYAD-DEF-CRITICAL-CURVE` | DEF | §6.1 (new entry) | definition |
| `DYAD-ALG-QC-CRITICAL-AMPLITUDE` | ALG | §6.4 | M3 |
| `DYAD-ALG-ISP-MAPS` | ALG | §6.4 | M4 |
| `DYAD-ART-ATLAS-P1` | ENG | §8 | artifact |
| `DYAD-ART-ATLAS-P2` | ENG | §8 | artifact |

**One-tag rule.** Each identifier keeps one canonical `[RID: …]` tag in live text:
- OPEN items: at the §2 registry header;
- artifacts: in §8;
- everything else: at its first §6 occurrence, otherwise the first §2 occurrence, otherwise the first occurrence anywhere.

Thirty other occurrences became code spans. In total, 146 identifiers carry a canonical tag in live text and Appendix B. Appendix A is history and is not rewritten (only double escapes are repaired there).

## 5. Owner decisions taken in this pass

1. The planned `DYAD-DEF-ISP-MAPS` is registered as **`DYAD-ALG-ISP-MAPS`**, because the entry is an `[ALG]` statement (exact inverse maps), not a definition.
2. The §6.13 heading keeps `[ENG]`, because there are no tagged entries to compute grades from.
3. The Local Tag Aliases table is left untouched; it documents the legacy forms.
4. `DYAD-OPEN-BREAKOUT-PHASE` (OPEN 2B) is recorded as an **alias of OPEN 5**. The identifier is kept and not renamed, and it is not counted as a separate open item.
5. $\phi_*$ is removed from the §4 layer-routing table, following NUMGEN's N3 answer (pin removed, `[CAND]` cap kept, historical source not identified).
6. "remain ontological ground truth" becomes "remain the reference mathematical model." This is one of the two declared §6 substitutions. The other removes the GAP-LOCK phrase from the "still not established anywhere" sentence and adds a scoped pointer to NUMGEN v1.20.8 GAP-LOCK Lemmas 1–3 (whether GAP-LOCK is discharged is NUMGEN's decision).
7. The historical `[import: RECOG v0.3.20 §…]` pins are kept. S2 shows that the cited passages are byte-identical in v0.3.22.
8. N16–N20 are **not prepared**. They follow the release.

## 6. Kept distinctions

- **FA-08.** The formula of `DYAD-THM-RAW-CUBIC` is independently verified. Its match with the historical source is **not**, because the source file is outside the review package. These are two different evidence levels.
- **FA-04.** `degree_b_vanishing_cert_v2.py` is **not available**. Every live line naming it says so (gate G14). It is not presented as recreated.
- **FB-13.** `DYAD-THM-SMOOTH-EQUIVARIANT-CHART` is a proposed `[THM]` RID (a corollary of E3–E4 by finite-group averaging). Analyticity stays OPEN. B-an and B-6 are unchanged.
- **FC-32** (HNG R9-free) is a SESSION record only. It is not imported into the draft.

## 7. Evidence levels (kept separate)

| Level | Content in this session |
|---|---|
| `OWNER-RUN` | Draft checker G0–G18 ALL PASS with two independent clean rebuilds, byte-identical. Owner math checks M1–M11 PASS. Source checks S1–S4 PASS. Checker negative controls N0–N16 plus K1–K3 and C1–C2, all as expected (`p2_checker_controls.json`). Records check R1–R4 PASS, with controls D1–D2 exit 1 |
| `REVIEWER-REPLAYED` | For r1: nothing yet. For the inputs: the P1 review accepted the P1 working file (`6f30f347…c905`), including its reviewer checks for FA-07 and FB-13 |
| `REVIEWER FULL REPLAY NOT COMPLETED` | Everything in r1. Carried from v6.4.19: the combined G14–G15 run and the separate-process M1–M4 exit codes |

The matrix in Appendix E applies the same three levels to each of the 58 live result and definition identifiers (E.2). Where a cell says "not recorded", it means that no record was found in the material read for this draft. It does not mean the claim failed.

## 8. Owner math checks (`dyad_p2_math_checks.py`)

All checks use exact rational arithmetic on the degree-6 jets of $T^6$, with SymPy for the closed forms.

| Check | Content |
|---|---|
| M1 | $R_*=\lambda_{\rm DSI}^{1/2}$, $e^{\pi/(3\tau)}=\lambda_{\rm DSI}^{1/6}$ |
| M2 | $DT\,(\cos\eta,1)^{\mathsf T}=(0,\det DT)^{\mathsf T}$ (critical curve) |
| M3 | $Q_c\approx0.5865$ |
| M4 | ISP inverse maps |
| M5 | six-step cubic jet; $M+M^{\mathsf T}=-I$ |
| M6 | $P_5$ radial term |
| M7 | $-\tfrac5{24}$ and $\tfrac{37}{40}$ (one-block burst) |
| M8 | $\tfrac{47}{54}=[W^3\bar W^3]\Delta Q_6$ |
| M9 | winding fixed points $(\log(1+2\pi k),0)$, $(\log(1+2\pi k),\pi)$ |
| M10 | $\vert\eta\vert<0.0543$ |
| M11 | $K_{\rm extra}$ admissibility |

Negative controls: K1 changes $37/40$ to $36/40$; K2 uses the exponent $1/3$; K3 changes $43$ to $42$. Each exits 1.

## 9. Checker gates (`check_dyad_v6_4_20_r1.py`) and controls

The result is G0–G18 **ALL PASS**:
- census A 137 → 148, with nothing missing and nothing extra;
- G8: 58/58/58;
- G18: 12/12 relocations quoted verbatim;
- rebuild hash equals the draft hash.

| Control | Mutation | Expected gate | Result |
|---|---|---|---|
| P0 | none | pass | exit 0 |
| N0 | one byte changed (full rebuild) | G0 | exit 1, G0 |
| N1 | second live RID tag in §6 | G3 | exit 1, G3 |
| N2 | FA-07 RID renamed | G2 | exit 1, G2 (and G4) |
| N3 | §6.1 order-6 → order-7 | G4 | exit 1, G4 |
| N4 | two recipients in one notice row | G6 | exit 1, G6 |
| N5 | "ontological ground truth" back in §6 | G4 | exit 1, G4 and G12 |
| N6 | second footer | G11 | exit 1, G11 |
| N7 | double escape | G9 | exit 1, G9 |
| N8 | E.1 row deleted | G8 | exit 1, G8 |
| N9 | §6 heading removed from the section map | G7 | exit 1, G7 |
| N10 | `[ALG, exact]` back in live text | G16 | exit 1, G16 |
| N11 | $\phi_*$ back in §4 | G13 | exit 1, G13 |
| N12 | missing script named without a custody note | G14 | exit 1, G14 |
| N13 | second AI_CONTEXT_CORE_END | G10 | exit 1, G10 |
| N14 | "breaker primes" back | G12 | exit 1, G12 |
| N15 | quoted relocated line altered | G18 | exit 1, G18 |
| N16 | not-adopted marker removed | G17 | exit 1, G17 |
| K1–K3 | math controls | — | exit 1 each |
| C1–C2 | source controls (wrong hash; altered v0.3.20 paragraph) | — | exit 1 each |

These controls are fail-closed engineering probes. Several gates overlap, so they are not independent proofs.

**Verified diffs.**
- **Appendix A**, outside the new v6.4.20 DRAFT r1 entry, differs from the P1 file's Appendix A only by the repair of double escapes on 38 lines.
- **Appendix B** differs only by the marker mapping `[P1]` → `[v6.4.20]`.
- **§6** passes the protection gate G4: after normalization it equals the P1 §6 up to the two declared substitutions. Normalization means the tag map, version markers, heading grades, new entry lines, RID tags and code spans, and `[v6.4.20: …]` spans.

## 10. Release-record addenda (FB-DYAD-17)

`DYAD_v6_4_17_v6_4_18_RELEASE_RECORD_ADDENDA_v0_1.md` does the following:
- attaches the reviewer verification identities to the v6.4.17 and v6.4.18 release records, which themselves are not edited;
- separates frozen RECOG v0.3.20 from adopted v0.3.21 and v0.3.22;
- records the RECOG v0.3.22 §7.2 receipts for N10–N13.

`check_p2_records.py` checks these identities against the source files, and checks the figures in this record against the result JSON files. Result: R1–R4 PASS. Its negative controls D1 (one RECOG hash altered in the addenda) and D2 (the draft hash altered in this record) each exit 1.

## 11. Known residual issues

1. Some tables inherited from P1 have `|` inside math in a table cell, for example the L-PHASE row in §5. The text is correct, but some Markdown renderers split those cells. New P2 tables use `\vert` / `\Vert`; inherited P1 tables were not changed in this pass.
2. Hashes are not recorded in this ledger for Triadic v1.6.1, OPEN-M v0.7.1, the Programme Overview, the Methodology, DZT and AZ. The §7.0 table says "not recorded in this ledger" rather than giving a value.
3. The full hashes of the v6.4.17 and v6.4.18 release records are not available in this session (addenda §6).
4. In the matrix, "not recorded" cells mark missing records, not failures. Filling them needs the historical review packages.

## 12. Carried open (unchanged)

- Row B.
- Reviewer full replay of G14–G15 (v6.4.19).
- FC-31 (large-$p$ behaviour of $|Q_p|$).
- O20-an (López-Hernanz source).
- The missing `degree_b_vanishing_cert_v2.py`.
- N16–N20, which follow a release.
- B-an and B-6 (OPEN 20).

## 13. Package

- **Files:**
  - the draft;
  - `p2_edit_log.json`;
  - `build_dyad_v6_4_20_r1.py`;
  - `p2_content.py`;
  - `check_dyad_v6_4_20_r1.py` and its JSON;
  - `dyad_p2_math_checks.py` and its JSON;
  - `p2_source_checks.py` and its JSON;
  - `p2_checker_controls.py` and its JSON;
  - `check_p2_records.py` and its JSON;
  - the addenda;
  - this record;
  - `SHA256SUMS.txt`.
- **Packages:** `DYAD_ATLAS_P2_PACKAGE.zip` holds these files. The source files are not in the ZIP; they are identified by hash in §1.
- **Reproduction** (from the package directory, with `p1_working.md` and `sources/` present):
  - `python -B build_dyad_v6_4_20_r1.py p1_working.md sources/base_v6_4_19.md RTG_DYADIC_OSCILLATOR_DSN_v6_4_20_DRAFT_r1.md`
  - `python -B dyad_p2_math_checks.py`
  - `python -B p2_source_checks.py sources`
  - `python -B check_dyad_v6_4_20_r1.py --draft RTG_DYADIC_OSCILLATOR_DSN_v6_4_20_DRAFT_r1.md --p1 p1_working.md --base sources/base_v6_4_19.md --math dyad_p2_math_checks.json --src p2_source_checks.json`
  - `python -B p2_checker_controls.py`
  - `python -B check_p2_records.py sources`
