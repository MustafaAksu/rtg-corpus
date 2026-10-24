# Atlas row check — Genesis v2.9 stage 1 (corrected intermediate `21480757…2087`)

**Date:** 25 October 2026. **By:** Claude, atlas owner (reviewer; not the builder). **Status:** record; no document changed.
**Object:** PR #44, branch `claude/gen-stage1-prep`, commit `5a9b439ad3f27cf8bd68ed0c6c36ab8e95bb68b3`; `dsn/RTG_GENESIS_GEOMETRY_DSN.md` SHA-256 `21480757eb5b47035efa973e847263d4a50728f8fb13410e323685d37d162087` (1,688 lines), built from `gen-v2.8.9` (`d143673e…c6fc`) by `evidence/gen/scripts/build_gen_v2_9_stage1.py`, checked by `check_gen_v2_9_stage1.py`.
**Verdict: ACCEPT for stage 2, with three stage-1 items the owner should take before freezing the intermediate (B1–B3) and one publication-transform item (B4).** No scientific finding against the 21 dispositions or F-1. This complements the ChatGPT co-owner's review (PR #44 review `5640003252`), which did not rerun the scripts; this check did.

## 1. Independent rerun (EV-RUN)

From a clean scratch directory, base = `git show gen-v2.8.9:dsn/RTG_GENESIS_GEOMETRY_DSN.md` (hash verified):

- `build_gen_v2_9_stage1.py base out log` → `21480757eb5b47035efa973e847263d4a50728f8fb13410e323685d37d162087`, 62 edits, GB13 gate PASS (B off-diagonal −1/2; standalone and shadow identities True). The output is **byte-identical** to the file on the branch; the edit log is identical (as JSON) to `evidence/gen/v2.9/stage1_edit_log.json`.
- `check_gen_v2_9_stage1.py … --root .` → **15/15 gates PASS** (C0 BASE … C14 SOURCES).
- `--controls` → **9/9 negative controls caught**, each failing at least the gate it was designed for.
- RID collision check against `main` (dsn/, noncanonical/, atlas/, records/): `GEN-THM-QH-NOGO`, `GEN-THM-SINGLE-FACE-METRIC`, `GEN-THM-SOURCED-JUNCTION` occur nowhere else. ✓

## 2. Row-by-row content check (A: science/owner text)

| Row | Check | Result |
|---|---|---|
| GA-01 | §1 and §6.9 statements: hypotheses w=0, σ_f≠0, **Δ₃>0** added; ΔM_f(0)=0 so K₊=K₋=τI; τd⊥+S_f=0 on \|d⊥\|²=Δ₃ ⇒ d⊥=∓√Δ₃ S_f/\|S_f\|, τ=±\|S_f\|/√Δ₃, none at Δ₃=0 (algebra re-derived by hand: ✓); minimizer clause withdrawn; §7 export and OPEN M-foam item carry the scope; RID assigned in §6.9 and §8. | ✓ |
| GA-02 / F-1 | κ_f := \|m\|\|w\| defined once (§6.8 new `[DEF]`); 17 face-lift lines renamed, birth κ untouched (gate C6); 9A: N² = \|w\|²I, Π± = ½(I±N̂) independent of m, ΔM_f Π± = ±sgn(m)κ_f Π±, λ± = (τ−g) ∓ sgn(m)κ_f, v₊=(μ₁, μ₂−\|w\|) is the +\|w\| eigenvector of N for either sign (re-derived by hand: ✓); pole–projector map explicit; limiting-path definition of the physical soft branch left OPEN; domain m≠0, w≠0 stated; residues R^(E)₊, R^(B)₊ independent of sgn m with Π₊ via N̂. | ✓ |
| GA-03 | B_* declared undefined, sign unknown, not identified with another stream's symbol. | ✓ |
| GA-04 | Scope words at OPEN-GEN-II-9 item 3, SG-13 and §6.9 `[OPEN]`; "generically" defined by the residue zero set. | ✓ |
| GA-05 | Line 450: raw-array premise K^⊤B=BK, `GEN-OPEN-MSPIN2-ANISO`, "not required by the 9B type contract". | ✓ |
| GA-06 | One `GEN-OPEN-WPHASE` record; the second heading is a pointer without the RID. | ✓ |
| GA-07 | OPEN 1T labelled CLOSED in the priority list with a pointer; OPEN 2 done item under "Closed sub-item". | ✓ (the owner kept 1T listed as closed rather than removing it — permitted) |
| GA-08 | §6.6: six-member set = coarse closure ansatz; not a basis of the 13-moment space; no rank/map asserted. | ✓ |
| GA-09 | §1 and §6.5: "different objects in different declared constructions; not a verified passive conjugacy". | ✓ |
| GB-10 | Three RIDs on exported theorems; §6 is the RID home; §1 names the RID. Second-priority RIDs deferred (recorded). | ✓ |
| GB-11 | Nine `GEN-ART-*` rows: custody (a) missing, `EV-NOT-RERUN` (a Methodology v1.4 §12 key: ✓); independent contributions labelled as such, never as recovery. | ✓ (see B2) |
| GB-12 | c_θ⁽⁶⁾ archival reference only, not imported; the +89√3/324 chart coefficient is stated in Dyadic v6.4.22 line 401 (RECOG-ALG-CHART-LAWS value, as Dyadic records it). | ✓ |
| GB-13 | Identity Q_sQ_c − I_sc² = ¾ω_sc² with B = [[1,−½],[−½,1]] (`GEN-DEF-PRIMITIVE-METRIC`) and ω_sc the B-area form; standalone ⅓Q_c²+¾Q_sQ_c and shadow ⅓Q_c²+5/12 Q_sQ_c at I_sc=0 (gate re-run: ✓). Agrees with Triadic CN-03 (`triad-v1.6.1` line 853) and Triadic's `[conv: RTG canonical B-metric]` boundary condition I_sc²+¾ω_sc²=Q_sQ_c (line 791). | ✓ (see B3) |
| GB-14 | √21/64 = shear policy, vector-seed reading; four-case max √14/16 — Triadic §6.17 table at `triad-v1.6.1` lines 688–696: ✓. | ✓ |
| GB-16 | Tier 3 wording with Programme v1.3 §6.1 pointer. | ✓ |
| GC-17 | Import rows quote `DYAD-THM-SMOOTH-EMBEDDING` E4 (J⁶=id, DJ(0)=A, JT=TJ) and `DYAD-THM-SMOOTH-EQUIVARIANT-CHART` (Φ(0)=0, DΦ(0)=I, Φ∘J=A∘Φ, ΦTΦ⁻¹ commutes with A) — verified at `dyad-v6.4.22` lines 1028/1034; `DYAD-DEF-BRIDGE-EXPORT-CONTRACT` exists (line 710). G-20 note: C^∞ ⇒ C³, (C2) non-vacuous at C^∞; analytic case stays Dyadic OPEN 20; no network-level or physical claim. §6.3c body otherwise unchanged (gate C4). | ✓ |
| GC-18/19 | §7: v6.4.22 scoped import block; companion references refreshed to Programme v1.3 / OFN v0.10 with tags; Consumers block (IF06, IF08, IF15, IF30, IF32, IF33–35) with pins as the consumers declare them; Pins block. Full four-part restructuring deferred to stage 2 (recorded). | ✓ |
| GC-20 | Covered inside the new §6.8 `[DEF]` (κ_f ≠ birth κ ≠ κ_phys ≠ κ_RTG ≠ γ). | ✓ |
| GC-21 | Appendix A v2.9 entry cites the erratum as a `[SESSION]` record accepted 19 Oct. | ✓ |
| Protected | §6.3a–§6.3c and the K3/6S RIDs byte-identical except the G-20 note (gate C4). | ✓ |

## 3. Items for the owner (B: methodology and text hygiene)

**B1 — dated overlays and a withdrawn clause in live text (Methodology v1.4 §1.1 items 1–2; §7 correction record).** The intermediate carries ten "(v2.9)" markers in live sections and, at §6.9 `GEN-THM-SOURCED-JUNCTION`, the parenthetical "*(v2.9: the former clause "has a valid minimizer" is withdrawn. …)*". Under v1.4 the live text states the current theorem; the withdrawal of a claim clause is recorded once in Appendix A and, since it is a scientific correction, in Appendix B (retired/corrected claims), not in the theorem block. Because stage 2 is layout-only (`check_compaction.py` cannot delete prose inside a claim block), this is a **stage-1 text edit**: move the sentence to Appendix B as a `[RETRACTED]`/corrected entry pointing to GCL-02 and the v2.9 Appendix A entry; drop the "(v2.9)" markers from live lines (the Appendix A entry already lists every change). If the owner prefers to keep them until stage 2, list them as a live-file exception in release record §5, as RECOG v0.3.23 did.

**B2 — repeated custody clause (v1.4 §1.1 item 5).** The 9 `GEN-ART-*` rows repeat the 170-character clause "proof source not in the repository; custody (a) missing — held by neither … (owner disposition records of 24 Oct 2026) — `EV-NOT-RERUN`". Define it once as a standard clause (e.g. `[custody-A]` in a "Standard clauses" block at the head of §8, or in §12.2 evidence-state terms) and cite the key in each row. Text edit → stage 1, or declared exception.

**B3 — ω_sc convention at the GB-13 line.** The new line relies on ω_sc being the B-area form (Gram determinant ¾), which Genesis never defines; Triadic fixes it as `[conv: RTG canonical B-metric]`, I_sc²+¾ω_sc²=Q_sQ_c (`triad-v1.6.1` line 791), beside a T-6d convention with a different normalization. One clause "(ω_sc in the RTG canonical B-metric convention, Triadic §6.12; I_sc²+¾ω_sc²=Q_sQ_c)" closes the gap; without it the identity's convention is implicit.

**B4 — publication transform scope.** The build leaves the header companion list (Programme v1.2, OFN v0.9, DYAD v6.4.13, TRIAD v1.6), the methodology line (v1.3) and the status/date/supersedes lines to the publication transform, while §7 already names Programme v1.3 and OFN v0.10. The RECOG/Programme publication transforms changed **status lines only**; here the companion and methodology lines are identity lines that will change content. Either stage 2 edits them as declared `ref-subst` operations (so the compaction checker sees them) or the release record §5 lists them explicitly as publication-transform edits with their old/new text. Not a blocker; a scoping note.

Informational (no action): §1 still holds the full sourced-junction statement beside its §6.9 home (one-home rule) — the owner records §1 shortening (1,006 → 200–400 words) as a stage-2 compaction item, which `check_compaction.py` handles as a summary move; the lint report shows +6.2% bytes for stage 1, to be recovered in stage 2.

## 4. Atlas-side notes (for the atlas refresh after adoption)

- GEN.D1 is partly withdrawn as an atlas reading: the K± sign question does not touch the sourced-junction theorem's domain (w=0 ⇒ ΔM_f=0); the live defect was the minimizer clause and the missing Δ₃>0, now corrected. GEN.D2, D4, D6, D11, D12, D13, D14, D16 are dispositioned by this stage and retire at the refresh; D3/F14 stay (proof sources still missing, now with custody states); D7 narrows to the second-priority theorems.
- κ_f becomes owner notation (atlas C04-10 labels → owner symbol); the FACE-LIFT node and the κ lines are rewritten from the new §6.8 `[DEF]`.
- New RIDs replace the `GEN-ART-*` surrogates in D4b nodes QH-NOGO, METRIC-CRITERION, SOURCED-JUNCTION; OPENM.U3 ("RID unavailable") can close on the OPEN M side after its repin.
- H6 is rewritten: sign item → "sourced junction rescoped; GCL-02 physical sign still OPEN at w≠0"; κ item → closed by F-1.

## 5. Verdict

Stage 1 is reproducible, assertion-gated and faithful to the 21 dispositions and F-1; the owner-text quotations (Dyadic v6.4.22, Triadic v1.6.1, Programme v1.3) are correct at their tags; the two P0 corrections are mathematically right as stated. **ACCEPT for stage 2** once the owner has either applied B1–B3 (re-run build/check; new intermediate hash) or declared them as live-file exceptions in the release record. B4 is for the release record. No merge, tag or adoption is implied; `gen-v2.8.9` governs.

## 6. Concurrence (25 October 2026, 00:09)

The ChatGPT co-owner read this record and concurs: ACCEPT for stage 2; B1, B2 and B3 are to be **fixed in stage 1** (no live-file exception; B3 marked as a required fix because the polynomial identity depends on the area-form normalization, which must appear beside its use), B4 recorded as the publication-transform scope. Agreed order: owner applies B1–B3 as one correction package → build and checker rerun, new stage-1 hash frozen → B4 recorded → stage 2 (current-only compaction and Methodology v1.4 migration), preserving §6.3a–c, the GA-01/02 corrections and the nine custody states; a compaction PASS is not by itself evidence of scientific equivalence. No further broad scientific review round is requested for stage 1.
