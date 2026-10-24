# Atlas v0.4 — internal-consistency audit, round 1 (atlas owner)

**Date:** 24 October 2026. **By:** Claude (atlas owner). **Object:** accepted atlas v0.3 (`atlas-v0.3`, `71310e8c…dc5b`, 1,560 lines) read against the governing tags of 24 October 2026; the only source that moved since v0.3 is Programme (`programme-v1.3`, `1b8358b3…aea06`). **Status:** findings record; no atlas edit. ChatGPT's independent round is on `chatgpt/atlas-v0.4-independent-audit` (PR #31); I had seen only the PI's six-line summary of its headings (A04-01…06) before writing this, not the record.

**Method.** (1) `tools/atlas_check.py` on v0.3 with the v0.3 manifest and data files. (2) Scripted structure checks: H1–H12 ↔ L5 key references; retired keys; "high" L5 rows without an H. (3) Targeted greps for facts that recur across domains (S_h, |G| and its windows, 403/250, 15/2, K₀, 0.04654, 1.61112) and for phrases the v0.3 cycle showed to go stale (RID unavailable, 14 homes, Programme v1.2, offered/transferred). (4) Reading of every D1 PROG node and every PROG.* diagnostic against Programme v1.3. (5) Owner texts consulted where a provenance question arose (OFN v0.10 §11.4, RRF v0.8.4 §6.2a).

## 1. Findings

**C04-01 — sources (checker FAIL).** `sources · PROG baseline — BASELINE row hash+tag differ`: the SOURCES row still says PROG v1.2 / `programme-v1.2`; `BASELINE.md` has v1.3 / `1b8358b3…aea06`. The only checker FAIL; everything else is as at v0.3 (7 UNVERIFIED, 11 DOCUMENTED-UNRESOLVED, 16 wording WARN, carried). Fix: SOURCES row and manifest → `programme-v1.3`.

**C04-02 — H10 and the PROG.* diagnostics against Programme v1.3.**
- PROG.G1 (stale 14-home table and status reports), PROG.G2 (RRF/RER/FMS/ER-2B missing), PROG.G4 (IF14/IF16/IF17 to check): resolved by v1.3 §§6.1–7.2 → retire.
- PROG.G5 (P2B criterion home): v1.3 §5 now cites OFN OPEN-OFN-3B as the criterion home → the PROG part is resolved; the PREL part (old row-agreement form) stays under PREL.P1 → reword or fold into PREL.P1.
- PROG.G6 (Pre-Legacy pass not executed): still true, and v1.3 §9.2 now records it → retain, reworded as an owner-recorded fact (D-STALE on PREL, not on PROG).
- PROG.G7 (κ_RTG in the κ family, HYP): v1.3 §8.2 carries κ_RTG as hypothesis-grade in the κ table → retire; the collision itself stays H8.
- H10: rebuild from what remains — OPENM.U1 (chart-dependent OPEN-M-6 audit) and PREL.P1/PROG.G6 (Pre-Legacy pointers); the "corpus map out of date" headline is gone.
- AZ.A3 ("programme-patch request satisfied by Programme v1.2 but still listed open" in AZ): AZ-side, unchanged; fine as is, edition reference may say v1.2/v1.3.

**C04-03 — D1 nodes stale against Programme v1.3** (not diagnostics; the nodes themselves):
- `PROG-TIERS` (L1): "14 document homes ≠ 14 branches … @PROG§6.1" → v1.3: 15 canonical homes in `dsn/`, 3 noncanonical, 1 derived map; class column; RRF in Tier 5.
- `PROG-INTERFACE-TYPES` (L1): v1.3 §7.1 adds *standard reference*, *noncanonical record*, *derived map*, *mutual citation*; *transfer-proposal* has no live instance (IF17 retired).
- `*PROG:IF-register` (L2): IF01–IF25 at v1.2 wording; v1.3 retires IF17 as a transfer proposal and adds IF26–IF36 (RECOG → DYAD R9 assumption; NUMGEN's consumer record of RECOG; RECOG → OFN; RRF as standard; owner imports into RRF; OFN ↔ RRF class-C contract; feedback imports into OFN; RER/FMS/ER-2B records; atlas).
- D1 header line "⊥ κ … — programme-wide node in header" and H8's advice "one cross-stream κ table": the table now exists (Programme v1.3 §8.2); the atlas should point to it rather than advise it.
- `*PROG:custody`, `*PROG:TDRG-launch-gate`, `*PROG:provenance`, `*PROG:firewall`: unchanged in v1.3; no edit.

**C04-04 — H-list ↔ L5 referencing is inconsistent.** H lines cite L5 rows by key, but three H lines cite *source keys* that are not L5 row ids: H7 (ER2B.Z1, FMS.M5, RER.E1), H8 (RER.E5, RRF.F6), H11 (PREL.P2, PREL.P3). In D4a the L5 rows are numbered F1–F29 and carry the source keys in parentheses ("F2 ~ D-LINK (RER.E1; high)"); in D1/D6 some rows are combined ("OFN.O8 + RRF.F6", "LEGACY.Y2 + PREL.P2"). RER.E5 occurs nowhere but H8 — a dangling reference. Conversely five "high" L5 rows are cited by no H under their own id (OFN.O1, F1, F2, F3, F5), although their content is in H1, H7, H8. Fix: one convention — every H cites L5 row ids; every high L5 row names its H; the D4a F-rows either become OWNER.X keys or the H list cites F-ids. The checker's `keys` check should then cover H → L5.

**C04-05 — κ ≡ γ is an owner statement, not an atlas reading.** Atlas H8 and the D1 κ line write "class-C coupling κ ≡ GEN γ" without `~`; RRF.F5 writes it with `~`. I checked the owners: OFN v0.10 §11.4 states "`GEN-THM-MEANFEEDBACK-SIXSTEP-NOGO` (γ ≡ κ ∈ ℝ∖{0,2}, under (H_spec))" and RRF v0.8.4 §6.2a states "(`γ≡κ` in the OFN class-C parameter convention)". Genesis itself writes γ and never κ ≡ γ. So H8 and D1 are right; RRF.F5 can drop the `~` and cite OFN §11.4 / RRF §6.2a; and the identification is OFN/RRF's convention, not GEN's. **Consequence outside the atlas:** Programme v1.3 §8.2, first row, says the relation "is an atlas reading, not an owner statement" — that sentence is wrong (my error as v1.3 editor). Registered as Programme erratum E-P13-1 (`records/programme/RTG_PROGRAMME_OVERVIEW_v1_3_POST_RELEASE_NOTE.md`), to be corrected in the next Programme edition; v1.3 is not reopened.

**C04-06 — consumer pins (no finding).** `*DYAD:leading-decay` and `*DYAD:cubic-rate-across-p` cite "RECOG v0.3.22": Dyadic's pins, written at the edge per Method §4. Correct.

**C04-07 — recurring numbers (no finding).** |G| = √481897/90720 ≈ 0.0076520 (2 sites, consistent); incompleteness windows ≈1.4800743×10⁻⁵ / ≈4.6944689×10⁻⁵ and partial-budget threshold 3.83×10⁻⁵ each at one site; 403/250 (6), 15/2 (6), K₀ = 1101/1000 (2), ε ≤ 0.04654 (2), 1.61112 (3): same value wherever repeated. S_h: "exact involution; commutation certified through degree 6; j⁶S_h = j⁶R₀" consistent in D1 (RRF-DYAD-LIFT), D3 (two nodes), RRF.F7, H12.

**C04-08 — retired keys.** None of the 10 keys retired at v0.3 is referenced anywhere in the live text. ✓

**C04-09 — carried checker limitations.** 4 link UNVERIFIED (AZ-OPEN-PROMO, AZ-OPEN-SCOPE-ARITH, AZ-OPEN-SCOPE-ZETA, NUMGEN-ART-ROTNUM-OBSTRUCTION: present but not in a recognized declaration form), 3 artifact UNVERIFIED (cm.py, fit.py, prove_core_equiv.py named outside their owner line), 11 DOCUMENTED-UNRESOLVED, 16 wording WARN, v0.1 input-equality unknowns for 13 sources. Unchanged since v0.2; owners' to fix or the checker's declaration grammar to widen. Carried.

## 2. Proposed v0.4 scope

Rebase PROG to v1.3 (C04-01, C04-03); H10 rebuilt and PROG.G1/G2/G4/G7 retired, G5 reworded, G6 retained (C04-02); one H ↔ L5 referencing convention, RER.E5 resolved (C04-04); RRF.F5 upgraded with owner citations (C04-05). No other source moved, so no other domain is re-extracted. Dispositions recorded with before/after hashes as in v0.3; checker and controls rerun; shared tool unchanged.

Round 2 is ChatGPT's independent record; the two are reconciled into one v0.4 build. Where the two rounds disagree on a fact, the owner text decides (C04-05 is the first such case: the κ ≡ γ provenance).
