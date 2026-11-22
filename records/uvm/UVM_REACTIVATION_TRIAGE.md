# OPEN M (UVM) — Reactivation Triage

**Status:** [SESSION] / NONCANONICAL. **Preparer's draft for the second co-owner's independent review**; Deliverable B of `records/atlas/ATLAS_ADVISORY_UVM_REACTIVATION_20261121.md` §5 and BOOTSTRAP 2 of `records/uvm/UVM_COOWNER_SESSION_ORIENTATION.md`. Every class and action below is a proposal by the triage owner. Nothing here edits the DSN, changes a pipe state, moves a pin, adopts or re-grades a result. The PI decides the successor edition's scope.
**By:** Claude, UVM co-owner (preparer and triage owner, PI assignment of 21 November 2026).
**Date:** 22 November 2026. `main` `a79e420c7ea0e1fde189e2ca0caeb67747e9d97b`. Governing edition: `uvm-v0.7.1`, SHA-256 `0a51644de0a15035797ab03945207cf319fd6d7514a04b8cae441d9d6e93f53e`. Line numbers are lines of that file.

**Built on:** the two entry reading reports (PR #357 `4413d65`, PR #358 `efe8723`), the reconciled discrepancy list (PR #359 `40b0c1c`, with the second co-owner's review `6013063697`), and — opened for the first time for this triage, after both reports and the reconciliation were filed — §3 and §4 of the 21 November advisory and the Atlas L5 rows `OPENM.U1–U11` (`atlas/RTG_STATE_ATLAS.md` at `atlas-v0.15`, SHA-256 `483e6003…02df`). The Atlas is advisory; where it and the owner text differ, the owner text is followed and the difference is listed in §8.

**Classes** (exactly those of BOOTSTRAP 2): **(i)** scientifically changed claim, or grade/scope issue; **(ii)** identifier, pin or editorial correction only; **(iii)** unaffected, or intentional pin, with an owner reason; **(iv)** source-unverified or blocking.

**Check state** used in the tables: *both* = verified by both co-owners (reference in the discrepancy list); *C* = Claude only; *G* = ChatGPT only; *A* = also stated by the Atlas row named.

---

## 1. PI decisions of 22 November 2026 (19:12 +03:00, project conversation with this session)

Recorded by the preparer from the PI's numbered reply to five numbered questions. They are quoted so that later readers do not have to trust a paraphrase.

| # | Question put to the PI | PI's reply | What it settles | What it does not settle |
|---|---|---|---|---|
| 1 | Start Deliverable B (open §3, draft the triage)? | "triyaja başlayalım" | this document | — |
| 2 | Does the hash-matched reconstruction of Genesis v2.8.5 count as the comparison source for the UVM pin; should it be placed in the repository or kept as a recipe? | "kaynak sayılsın" | the derived copy (SHA-256 `41ed7660…75cf`) **is the comparison source** for UVM's Genesis v2.8.5 pin | placement: not answered, so the copy is **not placed**; it stays a reproducible recipe (Claude report §(a).4) |
| 3 | Where are the UVM originals; can they come in on `upload/…`? | "dosya isimlerini veriren arayıp uploada koyabilirim" (verbatim) | the PI will search by file name and bring what he finds in on an upload branch | which files exist; until they arrive the S0 rows stay (iv) |
| 4 | Does the 10 November `0.403` decision also cover line 107 and the neighbouring "Legacy" attributions (lines 271, 273, 293)? | "kapsıyor" | all of them are corrected with the rework | the wording of each correction (row U9) |
| 5 | Is OPEN-M-6 approved as the first bounded science question? | "Onaylıyorum" | OPEN-M-6 is the first science item; its scope statement is prepared after this triage (row U1) | model class, hypotheses and falsifier: to be drafted and reviewed; no campaign is running |

---

## 2. S0 — source custody

| ID | Item | Class | Evidence / check state | Proposed owner action | Acceptance criterion | Affects |
|---|---|---|---|---|---|---|
| S0-1 | v0.7.1 adoption, release record, change record, release validation (4 files) | (iv) | absent from tree and zips (*both*; history not searched) | PI searches (decision 3); files arrive unchanged on `upload/uvm-originals`; hash-check; then a release record for v0.7.1 can cite them | each file present, SHA-256 recorded; the adoption JSON names the bytes `0a51644d…f53e` | adoption provenance of the governing edition |
| S0-2 | v0.7 governance files (6), v0.7 edition (`fea80656…7540`), v0.7.1 Draft 2 (`ebbf23ea…db95`) | (iv) | absent (*both*) | as S0-1 | hashes equal those in the v0.7.1 header | revision chain v0.7 → v0.7.1 |
| S0-3 | 18 certificate scripts, one wiring note, all outputs, ESM packs and growth series | (iv), blocking for I-3, I-4 and any rerun | absent (*both*) | as S0-1; list in §9 | per script: bytes, hash, and the output it produced; packs for RUN05/RUN10/RUN11/T80–T120 | every `[ALG]`/`[NUM]` certificate statement in §6/§8 stays `EV-SRC-REPORTED` until then |
| S0-4 | Genesis v2.8.5 bytes | settled by PI decision 2 | reconstructed independently by both sessions, same hash (*both*, D1) | none; do not place | — | rows P-GEN-* |
| S0-5 | Dyadic v6.4.10 (`74558119…56b7`), Triadic v1.6 (`c768687c…5b36`), OFN v0.8 (`56bc991d…a514`) | (iv) for old → new comparison only | absent (*both*); hashes recorded in RER v0.2 §7 | PI searches his archive (§9); otherwise the comparisons stay UNVERIFIED and are not replaced by current-owner statements | file hash equals the recorded value | rows P-DYAD, P-TRIAD, P-OFN |

---

## 3. Pins, at statement scope

| ID | Pin and use | Class | Evidence / check state | Proposed owner action | Acceptance criterion |
|---|---|---|---|---|---|
| P-GEN-a | Genesis v2.8.5: frame `[DEF]`, block-diagonal no-go, 9B / 9B-tau / 9C, norm typing, the 7B target, SG-6, dependency lines, GCL readings | (iii) | every imported owner line is byte-identical in `gen-v2.10` except `κ → κ_f` (*C*, Claude report §(b).2; bytes *both*) | owner reason for leaving the wording alone: nothing imported changed. Whether the successor names `gen-v2.10` as the pin is then a (ii) restatement; proposed yes, statement by statement, not as a blanket move | second co-owner repeats the line comparison, or accepts it on inspection of the table |
| P-GEN-b | "RID unavailable" on the six Genesis imports | (ii) | `GEN-THM-QH-NOGO` exists since v2.9 (*C*, *A* U3); the other five lines still carry no RID in `gen-v2.10` | attach `GEN-THM-QH-NOGO` to the no-go import; for the rest keep "RID unavailable" and send one RID request to Genesis through `pipes/GEN/`; UVM mints no Genesis RID | import lines cite only RIDs that exist at the pinned tag |
| P-GEN-c | The no-go's proof source is "not in the repository" (Genesis v2.9+) | (iv), non-blocking | `gen-v2.10` line 1006 (*C*; O9, not yet checked by the second co-owner) | carry the producer's custody limit in the import entry; do not restate the no-go as stronger than its custody allows | import entry names the limit; Genesis remains owner of the proof |
| P-DYAD | Dyadic v6.4.10: `B`, `J_Q`, `μ_6`, `τ`, `λ=e^{iF_f/2}`, archival `h_3=0` vs adopted `h_3≠0`, `DYAD-CAND-P0-DYADIC` | (iv) old side; current side consistent | no v6.4.10 bytes; `dyad-v6.4.24` lines 81, 778, SG-15 agree with UVM's reading (*both*) | none until bytes arrive, except U1 (new producer theorem since the pin) | S0-5 |
| P-TRIAD | Triadic v1.6: T-6s/t/u, SG-17, CN-01–05 | (iii) for v1.6.1 → v1.7; (iv) for v1.6 → v1.6.1 | T-6s/t/u and SG-17 lines identical v1.6.1 → v1.7 (*C*); v1.6 bytes absent | cite the Triadic RIDs that exist (`TRIAD-ALG-T6S-…`, `-T6T-…`, `-T6U-…`) in the Import Ledger (ii) | S0-5 for the remaining delta |
| P-OFN | OFN v0.8: OPA relevance for OPEN-M-7 | (iv) old side; low impact | reference-only use; `ofn-v0.12` keeps OPA OPEN and calls `UVM-OPEN-OPA-LINK` a hypothesis (*both*) | none | S0-5 |
| P-PROG | Programme v1.2: SG-PROG-1/2/4, tiering | (iii) | SG-PROG-1–4 lines identical v1.2 → v1.4 (*C*) | restating the pin as v1.4 is editorial (ii) | tag-to-tag check repeated by the second co-owner |
| P-METH | Methodology v1.3 | (iii) for grammar; layout in §7 | §3.3, §3.4, §4.3, §8.1, §8.4 identical v1.3 → v1.4 (*C*) | see M rows | — |
| P-PREL | Pre-Legacy v0.8 | (iii) pin; citations in U9 | same edition governs (*both*) | see U9, I-6 | — |

---

## 4. The eleven Atlas diagnostics

"Owner check" is what the tagged bytes say, read by this session; it is not the Atlas's wording.

| Row | Atlas diagnostic | Owner check | Class | Proposed owner action | Acceptance criterion / falsifier | Affects |
|---|---|---|---|---|---|---|
| U1 | OPEN-M-6 does not consider Dyadic's smooth equivariant chart | Correct as a fact and unavoidable: `DYAD-THM-SMOOTH-EQUIVARIANT-CHART` is "new in v6.4.20" (`dyad-v6.4.24` line 1056), after UVM's pin. It gives a `C^∞` local chart `Φ` with `Φ∘J = A∘Φ` and `ΦTΦ⁻¹` commuting with `A`. It says nothing about how the UV source coupling transforms | (i) | this is the PI-approved first science item (decision 5). Its scope statement must name three charts separately — archival return-log (`h_3=0`), adopted one-step polynomial conjugacy (`h_3≠0`), `C^∞` equivariant chart — and define the action on the typed source `jΛz̄` and on one named observable | outcome is one of: invariant / renormalized by a stated factor / mixed / undecided at stated order, with regularity and clock stated. Falsifier of "invariant": a nonzero change of the leading coupling under the one-step conjugacy at the order the old `O(Q^{3/2})` envelope claimed | R9, OPEN-M-6; Genesis GCL-07; Dyadic SG-15 |
| U2 | `0.024` → `4/125` → `ρ ≥ 16/5` → R15 `0.007–0.008` → RESULT-M-3B are one chain with different assumption domains | Agreed (*both*, A8–A10). Two conditions are missing from the chain as written in v0.7.1 **and** in the Atlas node: the single-jet hypothesis (I-1) and the state domain (I-5); the R15 quotient needs `gC_mh ≠ 0` (I-8) | (i) | one dependency table in the successor: object and norm, state/window, 9C premise, single-jet, finite `g`, `K_vac ↔ g`, source bridge; keep "no certified deficit factor" | every occurrence of `0.024`, `4/125`, `16/5` points to the table; no new number | Dyadic `DYAD-CAND-P0-DYADIC`, AZ §6, OFN RF-O08-08, Programme |
| U3 | `UVM-OPEN-2F` labels both the registry entry and R14; some Genesis imports are "RID unavailable" | Confirmed: lines 115 and 277 (*C*, *A*). In addition R1–R11 have no result RIDs and consumers cite them by label (O7, *C*) | (ii) | give R14 its own result RID and keep `UVM-OPEN-2F` on the OPEN entry; decide whether R1–R11 receive result RIDs (a consumer-visible change: Dyadic writes "OPEN-M R11"); Genesis side in P-GEN-b | RID census has no identifier on two objects; an alias table maps old labels | Dyadic, AZ, OFN citations |
| U4 | Genesis HYP-B keeps "sole viable cascade mechanism"; UVM retires "σ_f sole channel" | UVM line 295 is explicit: `σ_f` "remains an unresolved reduced-model UV source datum/route, not the sole certified remaining physical channel". Genesis `gen-v2.10` line 326 says "sole viable cascade mechanism" after HYP-A/HYP-C fail, with "reduced birth-race wrapper" attached to the threshold, not to "sole" | (iii) for UVM | none in UVM. Owner reason: the UVM text already carries the qualifier. The wording is Genesis's; a notice to `pipes/GEN/` asking for a cross-reference is optional and a separate owner decision | — | Genesis (owner of HYP-B) |
| U5 | `κ`, `μ`, `σ` have several meanings (advisory adds `h`, `H`, `g`) | Confirmed by census of the DSN: `κ` (birth coefficient `κQ_s`, `κ_phys`, proto-gravity `κ=−0.175` at line 81, `κ_3`); `μ` (BCH sector name, `μ_6`, `μ_1=ℜw`); `σ` (`σ_f`, `σ_int`, `σ_{h,int}`, Pauli `σ_1`/`σ_3`, `σ(z)`, `σ_harm`). Owner additions: the sign of `m` (I-2) and `Q_s` against `Q_{s,0}` (I-5) | (ii); the `m` and `Q_s` parts are (i), see I-2, I-5 | a local symbol dictionary: category, type, norm, units for each load-bearing symbol | no equality in §6 joins two symbols from different models without a named bridge | readers; no consumer change |
| U6 | `θ_f = 2π/3` equals Dyadic `F_f`, the OFN 120° angle and the ISP funnel angle as numbers only | Agreed (*both*, A13). UVM already grades the angle `[ALG]` inside the assembly and `[INTERP]` across domains "pending a bridge theorem" (R11). Dyadic line 467 words it more strongly ("equals the face flux `F_f` exactly") | (iii) | none required in UVM. Owner reason: the grade split is already in the text. Before any physical use: state the bridge hypothesis (named transport between the two-face BCH frame and the ESM holonomy) and its falsifier | — | Dyadic wording is Dyadic's |
| U7 | §9 item 8 says Programme/OFN synchronization "not performed"; OFN consumes v0.7.1 | Line 363: "not performed by this release" — true of the release, stale as a current status. At the governing tags the consumers do reference v0.7.1: OFN v0.12 (RF-O08-08, RF-O08-11), Dyadic v6.4.24, AZ, Programme v1.4 (lines 239, 305) | (ii) | replace the item by a consumer table with four separate columns: notice sent / received / statement accepted / adopted use, filled only from the consumers' own tagged text | each cell cites a consumer line at a tag; no cell is inferred | OFN, Dyadic, AZ, Programme |
| U8 | §6 header says R1–R6 are "pending PI audit"; later records show audits for some items only | Line 235 carries the June 2026 banner. Appendix A mentions PI audits for the R11 non-claims (line 393), the BCH probe and the exit-code gates (397), a failed R3 patch caught at freeze (400) and the R10 audit artifact, "PI-run confirmed" (402). No audit statement for R1, R2, R5, R6 was found (*C*) | (iv) for the audit facts; (ii) for the banner | **PI question:** were R1–R6 (the June 2026 equivariance package) PI-audited? Then: per-result line "certificate id / audit status", banner removed | every R-row states its own audit status or "not recorded" | export of R1–R6 to Genesis |
| U9 | R12 "Legacy 0.403" is a Pre-Legacy value | Confirmed against bytes (*both*, A5): Pre-Legacy v0.8 §1.9, grown `N=175`, `[NUM strong]`; absent from Legacy v0.7. **PI decisions of 10 and 22 November cover lines 107 and 271, and the "Legacy" attributions at 271, 273, 293** | (ii), decided | lines 107, 271: "Pre-Legacy v0.8 §1.9". Lines 271, 273, 293: the phrase "no β₁ → no vacuum" is literal in neither file; cite the nearest Pre-Legacy §1.9 statements with their own grades (`β₁` as topological matter; `[HEUR]` "void fails"), or mark the phrase as UVM's paraphrase — do not present it as a quotation | number `0.403` unchanged; finite-simulation context kept; no sentence credits Legacy v0.7 with a statement it does not contain | Atlas H11, LEGACY.Y2, PREL.P2 |
| U10 | RESULT-M-3A carries a compound grade | The exact text is `[RESULT]` `[from: ALG/typing audit]` (line 285), as the advisory says; the Atlas row misquotes it. It is nevertheless not clean: Methodology §3.4 (identical in v1.3 and v1.4) pairs `[RESULT]` "with exactly one canonical status", and "ALG/typing audit" and "DEF/RESULT registry" (line 79) are not canonical statuses. So: **not a false positive in substance; wrong rule and wrong quotation in the Atlas row** | (ii) for the form; (i) through I-3 | write the companion as one canonical status and move "typing audit" into a provenance clause; the status chosen for RESULT-M-3A depends on what THM-3G is (I-3). §8 provenance strings sorted under §8.4. Genesis-owned tags are Genesis's | each `[RESULT]` has one registry status; no grade is raised by the rewrite | Atlas D4; Genesis for its own tags |
| U11 | `E_full/E_half = 4` does not select `h ↦ 2h` or `4h` in the OPEN-M source norm | Agreed (*G*, source line confirmed by *C*: Pre-Legacy line 282, an energy-normalization convention). R16 already withdraws "legal ×2" and conditions the branch on two unproved premises | (iii) | none. Owner reason: v0.7.1 already holds ×2 / ×4 / neither open; nothing to repair numerically without a typed map (owner priority 2) | — | Dyadic SG-15, AZ §6 |

---

## 5. The four inbox items

Proposed receiving position only. No `pipes/UVM/` file is edited; "received", "statement accepted", "adopted use" and "closed" stay distinct, and adopted use exists only once a UVM Import Ledger or release record says so.

| Item | Part | Class | Statement accepted? | Proposed adopted use | Proposed state |
|---|---|---|---|---|---|
| `20261026-GEN-kappa-f-b-star-sourced-junction` | `κ_f` notation | (iii) — UVM never writes `κ` for the face-lift magnitude | yes | none needed | — |
| | `B_*` undefined, sign unknown | (i) — reaches six UVM places (I-2) | yes (*both*, D3) | successor states the sign hypothesis at each place | open until the successor |
| | sourced-junction rescoping | (iii) — UVM does not import the theorem (*both*, D2) | yes | none | — |
| | RIDs now available | (ii) — P-GEN-b | yes | cite `GEN-THM-QH-NOGO` | — |
| `20261103-GEN-v2-10-adopted` | "changes nothing UVM imports" | (iii) | yes on the imported lines (*C*); the two informational results were not read | pin restatement per P-GEN-a | can close with the successor |
| `20261103-DYAD-notices-n16-n21` | "OPEN-M R11" / "RECOG R11" | (ii) | yes | none in UVM; feeds the RID decision in U3 | can close once U3 is decided |
| `20261103-TRIAD-v1-7-adopted` | T-6s/t/u unchanged; CN-02 remainder | (iii) for the T-6 lines; (iv) for the v1.6 → v1.6.1 delta | yes for v1.6.1 → v1.7 | Import Ledger cites the Triadic RIDs; UVM line 76 already carries the GCL-06 dependence | open until S0-5 or an owner decision to accept the delta as source-reported |

---

## 6. Findings not in the Atlas rows

| ID | Finding | Class | Check state | Proposed owner action | Acceptance criterion / falsifier |
|---|---|---|---|---|---|
| I-1 | The `0.024` target is derived with `α_f = c_0|w|` (single-jet) in Genesis; UVM's condition lists at lines 68, 101, 163, 215, 267, 289 omit it | (i) | *both* (O1) | add single-jet to the target's conditions; keep the second co-owner's distinction: stipulated diagnostic number versus derived threshold | no line uses `0.024` or `4/125` as a derived threshold without naming single-jet |
| I-2 | Sign of `m`: `B_*` undefined in Genesis; UVM assumes `m ≥ 0` at lines 136, 239, 265, 289, 299, 301 | (i), no number changes | *both* (D3) | sign-safe forms (`g_soft = 2|m||ℜw|`); declare the hypothesis where a sign is needed; say which branch `g_soft` denotes; note that R11 forces `m ≥ 0` only inside its own assembly | each formula holds for both signs or states its sign hypothesis. Falsifier of the sign-safe form: a 2×2 evaluation at `m<0` disagreeing with `g ± 2mℜw` |
| I-3 | `THM-3G`: no claim block, status, RID, hypotheses or §8 row; certificate named only in §7 | (i) grade undeclared; (iv) certificate absent | *both* (O3) | after S0-3: write the statement with its domain ("tested topology class") and the grade its evidence supports; until then say "grade not declared in the governing text" wherever it is used (R15, RESULT-M-3A) | a §6 block with one registry status, hypotheses, and a §8 row. This shows a record gap, not that the assertion is false |
| I-4 | `T100`: `nm=2` at line 110, `nm=0` at line 277, same `σ_{h,int}=0.252` | (iv), blocking for one R14 sentence | *both* (O4); the Atlas node repeats `nm=0` | after S0-3: read the panel output. Do not choose a value or delete a result before that | the two lines agree, or are shown to describe different packs |
| I-5 | Genesis records control-loss values for `Q_{s,0} ≤ 5×10⁻²`; the assembler evaluates at `Q_s = 0.1` | (i) scope | *C* (O5) | part of the U2 dependency table; input to OPEN-M-3C | the table names the state at which each number was obtained |
| I-6 | Locators `§RG` (actual: §6.2) and `§1.12` (step 4 is in §1.9); `[from: HYP]` over a chain Pre-Legacy grades `[HEUR]` (line 81) | (ii) locators; (i) for the companion tag | *C* (O8) | correct locators; split line 81 so each import carries its source's own grade | each import's grade equals the source's at the cited line |
| I-7 | R14: `n=9` stages of one growth series; `r=+0.654` is `p≈0.06`; `+0.654` vs `+0.326` not resolved | (i) wording scope | *C* | drop "weaker correlate" as a comparative claim or state it as descriptive of this series only | no sentence ranks the two correlations |
| I-8 | R15 quotient valid only where `gC_mh ≠ 0` | (i) scope note | *G*; algebra agreed by *C* | one clause in R15 | — |
| I-9 | The preserved R12 sentence "the harmonic component … is the physical source" is corrected only by the adjacent `[COR]` | (ii), layout | *G*, consistent with *C* | resolved by M-1 | the current-use text contains no superseded assertion |

---

## 7. Methodology v1.4 normalization (stage 2)

All class (ii). The advisory asks that structural migration be done "only when warranted" and separately from the scientific corrections; whether it is in the successor's scope is the PI's decision.

| ID | Item | Evidence | Proposed action |
|---|---|---|---|
| M-1 | Live-file rule: dated overlays beside preserved v0.6 bodies (R12, R14); Appendix A (12,570 characters, 8 editions); Appendix B verbatim archive | `dsn_lint`, informational | current-state text only; history stays in the tag and the release record |
| M-2 | §1 is 973 words | `dsn_lint` | shorten or use a header profile exception |
| M-3 | §7 Import Ledger is prose per source, not the §4.3 entry format | DSN §7; header declares a bounded migration | rewrite as §4.3 entries with `Source status / Depends on / Verification / Synchronization` |
| M-4 | No Local Tag Aliases block while `[INTERP]`, `[INTERP/HYP]`, `[NUM diagnostic]`, `[CAND]` are used; `[source: …]` instead of `[import: …]` on three lines | DSN lines 81, 83, 85, 258 and others | declare aliases or use registry tags; unify the import form |
| M-5 | §1 says it "asserts nothing on its own authority" but holds two native `[COR]` guards and one native inference | DSN §1.3, §1.4 | move native statements to §3 / §6, or amend the sentence |

---

## 8. Where this triage differs from the Atlas and the advisory

For the Atlas owner's information. Nothing is filed to `pipes/ATLAS/` by this draft; whether to send it is an owner decision after review.

1. **U10:** the advisory proposes marking the UVM part a "false-positive candidate". Owner reading: the row misquotes the tag and cites §8.4, but §3.4's "exactly one canonical status" is not met. Not a false positive in substance.
2. **U7:** the row cites OFN v0.11 and "Programme v1.2 does not"; at `ofn-v0.12` and `programme-v1.4` both reference v0.7.1.
3. **U2 / node `*UVM:deficit-chain`:** the node's condition list ("reduced-wrapper + conditional-9C + large-g + state/window") omits single-jet, as the UVM text does (I-1).
4. **Node `UVM-NUM-2F-TRAJ`:** repeats "clean T100 (…, nm=0, …)" without the §2 value `nm=2` (I-4).
5. **No Atlas row** for the reach of `sgn(m)` in UVM (I-2) or for THM-3G (I-3).
6. Rows U1, U3, U4, U5, U6, U8, U9, U11: the owner check agrees with the diagnostic; U3 and U5 are extended.

---

## 9. Files the PI is asked to look for (decision 3)

Bring whatever exists, unchanged, on branch `upload/uvm-originals`, folder `upload/uvm-originals/`, with a `SHA256SUMS.txt`. "Not found" is a valid answer and is recorded as such.

- **v0.7.1 governance:** `RTG_OPEN_M_v0_7_1_OWNER_ADOPTION.json`, `RTG_OPEN_M_v0_7_1_RELEASE_RECORD.md`, `RTG_OPEN_M_DSN_v0_7_1_CHANGE_RECORD.md`, `RTG_OPEN_M_v0_7_1_RELEASE_VALIDATION.txt`
- **v0.7 governance:** `RTG_OPEN_M_v0_7_OWNER_ADOPTION.json`, `RTG_OPEN_M_v0_7_RELEASE_RECORD.md`, `RTG_OPEN_M_v0_7_DRAFT2_VALIDATION.txt`, `RTG_OPEN_M_v0_7_DRAFT3_VALIDATION.txt`, `RTG_OPEN_M_v0_7_DRAFT3_1_VALIDATION.txt`, `RTG_OPEN_M_DSN_v0_7_DRAFT3_1_CHANGE_RECORD.md`
- **Editions:** OPEN M v0.7 (SHA-256 `fea80656…7540`), `…v0_7_1_DRAFT2.md` (`ebbf23ea…db95`); Dyadic v6.4.10 (`74558119…56b7`), Triadic v1.6 (`c768687c…5b36`), OFN v0.8 (`56bc991d…a514`)
- **Scripts (§8):** `uvjet_equivariant_classification.py`, `open_m_constraint_scope.py`, `open1_liegauge_candidate.py`, `thm_m_lock_certificate.py`, `bch_two_face_word_probe.py`, `bch_minimal_jet_assembly.py`, `open_m_doc_consistency_check.py`, `hodge_decomposition_audit.py`, `harmonic_localization_invariant.py`, `open_m_2e_panel.py`, `open_m_2f_trajectory.py`, `open_m_2f_zh2_weighted.py`, `open_m_2f_staircase.py`, `open_m_2f_rho_assembler.py`, `esm_harmonic_report.py`, `t103_defect_carrier_test.py`, `single_sandwich_dichotomy_certificate.py`, and the note `EDIT_A_wiring_instructions.txt`
- **Script (§7 only):** `open_m_3g_mini_protocol.py`
- **Data, first priority:** the OPEN-M-2E panel output and the T80→T120 trajectory output that contain `T100` (I-4); the output of `open_m_3g_mini_protocol.py` (I-3). Then the ESM packs for RUN05, RUN10, RUN11, T100, T103.

---

## 10. What the PI is asked to decide after the second co-owner's review

1. **Successor edition, stage 1 (scientific and scope corrections).** Proposed content: U2 with I-1, I-5, I-8 (one dependency table); I-2 (sign of `m`); U9 (citations, already decided); U3 and P-GEN-b (identifiers); U7 (consumer table); U10 and I-6 (status companions); I-7 (wording). None changes a number. I-3 and I-4 enter stage 1 only if S0-3 delivers their originals; otherwise they are stated as open evidence gaps.
2. **Stage 2 (M-1 to M-5):** in the same edition, a later one, or not now.
3. **U8:** were R1–R6 PI-audited?
4. **Pins:** restate Genesis as `gen-v2.10` and Programme as v1.4 (P-GEN-a, P-PROG), leaving Dyadic, Triadic and OFN at their stated editions until S0-5.
5. **Notices out:** RID request to Genesis (P-GEN-b); optional cross-reference request on HYP-B (U4); feedback to the Atlas owner (§8).

OPEN-M-6 (decision 5) proceeds independently of the edition work: its scope statement is the next deliverable.

*End of triage draft. No UVM statement, pin, grade, pipe state or evidence file is changed by it.*
