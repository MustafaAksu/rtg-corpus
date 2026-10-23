# Atlas v0.2 — L5 dispositions

**Date:** 23 October 2026. **Atlas owner:** Claude. **Scope:** every L5 item of atlas v0.1 (HEADLINE H1–H12, D-WRONG and D1–D6 L5), dispositioned against the v0.2 source snapshot (`evidence/atlas/source_manifest_v0_2.json`) and the v0.2 diagnostic semantics (Method v0.2 §6: D-PIN, D-GRADE, D-PROOF). This record holds the reasons; the atlas holds only the current state (Method v0.2 §4.1, §7). Rows marked **[AV02]** apply the receiving review `records/atlas/ATLAS_V0_2_RECEIVING_REVIEW.md` (AV02-02–04).

L5 dispositions (195 items): deleted 16, moved 7, new 1, retained 105, reworded 66. Further rows record non-L5 edits made under the same rules (two process-only L3 lines deleted, edge replacements, process-wording removals, evidence-record typing).

- **retained** — the item's sources, its dependencies and the diagnostic rule applied to it are unchanged; text carried forward.
- **reworded** — still holds, restated against the current sources or semantics (reason given).
- **deleted** — no longer holds at the snapshot, or is process state; the key is retired and never reused (`evidence/atlas/retired_l5_keys_v0_2.json`, checked by `tools/atlas_check.py` check `keys`).
- **moved** — PASS lists leave L5 (Method v0.2 §6, last paragraph).
- **new** — finding from the v0.2 re-extraction.

Retained items were not re-derived; scientific certificates were not rerun (Method v0.2 §7).

| # | key | disposition | reason |
|---|---|---|---|
| 1 | H1 | reworded | DYAD v6.4.22 registers SMOOTH-EQUIVARIANT-CHART (Bochner step now owner-stated); RER now imports SMOOTH-EMBEDDING, so RER and RRF are removed from the stale list; edition chronology removed |
| 2 | H2 | retained | sources, dependencies and diagnostic semantics unchanged |
| 3 | H3 | reworded | DYAD v6.4.22 App F now classifies every DZT/AZ string; restated as consumer-side defect only |
| 4 | H4 | retained | sources, dependencies and diagnostic semantics unchanged |
| 5 | H5 | retained | DYAD inputs (LPHASE-ROWA, PRIM-CTR) unchanged in content at v6.4.22; RECOG/NUMGEN unchanged |
| 6 | H6 | reworded | ν₃ frame clause deleted: DYAD-ALG-KP-FRAME-SCALE and the frame-named BRIDGE-LEMMA settle the factor-3 frame issue at the owner (RECOG.R-C3 deleted) |
| 7 | H7 | retained | RER v0.2 adopted text still does not cite OFN v0.10 / A1 / class C (slice check) |
| 8 | H8 | retained | sources, dependencies and diagnostic semantics unchanged |
| 9 | H9 | reworded | process wording (new at merge) removed |
| 10 | H10 | reworded | D-PIN v0.2 semantics: edition age alone dropped; RECOG.R-P1 clause removed (no demonstrated mismatch) |
| 11 | H11 | retained | sources, dependencies and diagnostic semantics unchanged |
| 12 | H12 | reworded | degree-6 agreement S_h=R₀ is owner-stated in DYAD; 'to verify' part removed |
| 13 | AZ.A1 (D-WRONG) | retained | sources, dependencies and diagnostic semantics unchanged |
| 14 | OFN.O7 ≡ TDRG.G4 (D-WRONG) | retained | sources, dependencies and diagnostic semantics unchanged |
| 15 | OFN.O1 + RRF.F1 | reworded | DYAD now owns the Bochner chart step; RRF part (F1) is not stale (RRF records it), key RRF.F1 retired; chronology removed |
| 16 | OFN.O2 | deleted | D-PIN v0.2: edition age alone is not a defect; the IMP-O10-04 'DYAD-CAND-…' identifiers still exist in DYAD v6.4.22 (no mismatch); content mismatch is carried by OFN.O1 |
| 17 | OFN.O3 | reworded | edition reference and process wording removed |
| 18 | OFN.O4 | retained | sources, dependencies and diagnostic semantics unchanged |
| 19 | OFN.O5 | retained | sources, dependencies and diagnostic semantics unchanged |
| 20 | OFN.O6 | retained | sources, dependencies and diagnostic semantics unchanged |
| 21 | OFN.O7 | retained | sources, dependencies and diagnostic semantics unchanged |
| 22 | OFN.O8 + RRF.F6 | reworded | process wording ('advised') normalized |
| 23 | OFN.O9 | retained | sources, dependencies and diagnostic semantics unchanged |
| 24 | OFN.O10 | reworded | D-PROOF state named per Method v0.2 §6 |
| 25 | OFN.O11 | retained | sources, dependencies and diagnostic semantics unchanged |
| 26 | OFN.O12 | retained | sources, dependencies and diagnostic semantics unchanged |
| 27 | OFN.O13 | retained | sources, dependencies and diagnostic semantics unchanged |
| 28 | RRF.F2 | reworded | D-PIN v0.2: age-only pins dropped; the internal convention/row contradiction is kept as D-STALE |
| 29 | RRF.F3 | retained | sources, dependencies and diagnostic semantics unchanged |
| 30 | RRF.F4 | retained | sources, dependencies and diagnostic semantics unchanged |
| 31 | RRF.F5 | retained | sources, dependencies and diagnostic semantics unchanged |
| 32 | RRF.F7 | reworded | DYAD statement exists; 'needs DYAD statement' clause removed |
| 33 | PROG.G1 | reworded | current-edition comparison list dropped (D-PIN v0.2); stale status statements kept |
| 34 | PROG.G2 | retained | RER v0.2 adopted; still absent from the Programme inventory |
| 35 | PROG.G4 | reworded | DYAD edition updated to the snapshot |
| 36 | PROG.G5 | retained | sources, dependencies and diagnostic semantics unchanged |
| 37 | PROG.G6 | retained | sources, dependencies and diagnostic semantics unchanged |
| 38 | PROG.G7 | retained | sources, dependencies and diagnostic semantics unchanged |
| 39 | METH.M1 | reworded | Methodology reference updated to v1.4 (rule unchanged) |
| 40 | METH.M2 | reworded | process wording (Advisory Note pass) removed |
| 41 | DYAD.X1 | reworded | Bochner step is now an owner RID, so the link is no longer atlas-derived (~ removed); chronology removed |
| 42 | DZT.Q1 | reworded | owner classification (App F) and new RID Q3-DEG2-CANCEL in DYAD v6.4.22; restated as consumer-side defect |
| 43 | NUMGEN.N-S1 | retained | NUMGEN unchanged; DYAD keeps U and U_T distinct (App C) |
| 44 | NUMGEN.N-A + DYAD.X10 | reworded | notice-receipt wording removed; content unchanged |
| 45 | NUMGEN.N-D + DYAD.X3(part) | reworded | DYAD side resolved (DYAD v6.4.22 removes φ* and states the string is not a Dyadic identifier); DYAD.X3 part retired |
| 46 | NUMGEN.N-B | retained | sources, dependencies and diagnostic semantics unchanged |
| 47 | NUMGEN.N-E | retained | sources, dependencies and diagnostic semantics unchanged |
| 48 | NUMGEN.N-L6 | retained | sources, dependencies and diagnostic semantics unchanged |
| 49 | DYAD.X8 | reworded | owner RID of the conversion added; otherwise unchanged |
| 50 | DYAD.X2 | retained | symbol overloads unchanged in DYAD v6.4.22 (ℓ reserved for winding) |
| 51 | NUMGEN.N-S2 | retained | sources, dependencies and diagnostic semantics unchanged |
| 52 | DZT.Q2 | deleted | DYAD v6.4.22 §2 cites DZT-ALG-P12-NORM at the near-cancellation item and restores the sign |
| 53 | NUMGEN.N-L1 | retained | sources, dependencies and diagnostic semantics unchanged |
| 54 | NUMGEN.N-L2 | retained | sources, dependencies and diagnostic semantics unchanged |
| 55 | NUMGEN.N-L3 | retained | sources, dependencies and diagnostic semantics unchanged |
| 56 | NUMGEN.N-L4 | retained | sources, dependencies and diagnostic semantics unchanged |
| 57 | NUMGEN.N-L5 | retained | sources, dependencies and diagnostic semantics unchanged |
| 58 | NUMGEN.N-L7 | retained | sources, dependencies and diagnostic semantics unchanged |
| 59 | NUMGEN.N-SC1 | retained | sources, dependencies and diagnostic semantics unchanged |
| 60 | NUMGEN.N-R1 | retained | sources, dependencies and diagnostic semantics unchanged |
| 61 | NUMGEN.N-R2 | retained | sources, dependencies and diagnostic semantics unchanged |
| 62 | DYAD.X4 | reworded | [AV02] prefix–grade difference of immutable CAND identifiers removed (DYAD gives a current-grade lookup; the prefix is not the grade); classification-by-p DEF dropped; only results without RID remain |
| 63 | DYAD.X5 | deleted | DYAD-ALG-B5-ALLP-NONVANISHING registered; OPEN RID kept only as closed lifecycle item |
| 64 | DYAD.X11 | reworded | statement now located in DYAD (§6.11); remaining issue is identity with the historical proposition |
| 65 | DYAD.X6 | reworded | not a grade defect under D-GRADE v0.2; reclassified; notice wording removed |
| 66 | DYAD.X9 | deleted | [AV02] DYAD v6.4.22 §6.12 export table records the 16/3=(4√3/3)² bookkeeping cross-reference (FC-DYAD-34); the identity stays at its content home (DYAD-DEF-BRIDGE-EXPORT-CONTRACT node) |
| 67 | AZ.A2 (D2 copy) | retained | AZ unchanged; Q403-PHASELAW closure and GEN v2.8.9 current |
| 68 | DYAD.X3 | deleted | DYAD v6.4.22: N2 Triadic ANSWERED; §7.0 one current-edition table (RECOG v0.3.22, NUMGEN v1.20.8, OFN v0.10) |
| 69 | DYAD.X7 | deleted | DYAD v6.4.22 internal frontier lists only open items; edition tags inside entries are owner provenance, not a contradiction |
| 70 | NUMGEN.N-F | reworded | D-PIN v0.2: deliberate valid pins (DYAD v6.4.18 etc.) are not defects; reverse DYAD pointer now v1.20.8; RECOG part is RECOG.R-P2 |
| 71 | NUMGEN.N-C1 | retained | sources, dependencies and diagnostic semantics unchanged |
| 72 | NUMGEN.N-C2 | deleted | [AV02] DYAD-THM-Q403-PHASELAW is [THM] [proof: exact algebraic identity]; NUMGEN imports it as [RESULT] [from: THM] — consistent; NUMGEN's "not graded here" for N-3C+ is an explicit scope statement, not a conflict |
| 73 | NUMGEN.N-D1 | reworded | D-PROOF state named |
| 74 | NUMGEN.N-G1 | retained | sources, dependencies and diagnostic semantics unchanged |
| 75 | NUMGEN.N-T1 | retained | sources, dependencies and diagnostic semantics unchanged |
| 76 | NUMGEN.N-T2 | retained | sources, dependencies and diagnostic semantics unchanged |
| 77 | NUMGEN.N-T3 | reworded | DYAD v6.4.22 no longer cites the bound (load-bearing clause removed) |
| 78 | DZT.Q3 | deleted | D-PIN v0.2: edition age alone; DZT's demonstrated consumer defect is DZT.Q1 |
| 79 | DZT.Q4 | reworded | [OBS] is a METH v1.4 §8.1 tag; that clause removed |
| 80 | DZT.Q5 | retained | sources, dependencies and diagnostic semantics unchanged |
| 81 | AZ.A5 (D2 copy) | retained | sources, dependencies and diagnostic semantics unchanged |
| 82 | AZ.A3(part) | deleted | D-PIN v0.2: edition age alone; AZ consumer defects are AZ.A2/A7 and DZT.Q1 |
| 83 | NUMGEN/DYAD q* merge note | retained | DYAD v6.4.22 OPEN18 still names q_* without NUMGEN citation |
| 84 | RECOG.R-L1 | reworded | edition chronology removed; content checked against DYAD v6.4.22 (LPHASE-ROWA unchanged) |
| 85 | RECOG.R-L1b | reworded | restated with the owner statement |
| 86 | RECOG.R-L2 | retained | sources, dependencies and diagnostic semantics unchanged |
| 87 | RECOG.R-L3 | retained | sources, dependencies and diagnostic semantics unchanged |
| 88 | RECOG.R-L4 | reworded | reclassified (not a grade defect); notice wording removed |
| 89 | RECOG.R-L5 | reworded | degree-6 agreement is owner-stated in DYAD; 'presumably/to verify' removed |
| 90 | RECOG.R-L6 | retained | sources, dependencies and diagnostic semantics unchanged |
| 91 | RECOG.R-L7 | reworded | DYAD notice table now records N10–N13 receipts; notice clause removed; D-GRADE v0.2 reading stated |
| 92 | RECOG.R-L8 | retained | sources, dependencies and diagnostic semantics unchanged |
| 93 | RECOG.R-L9 | deleted | DYAD v6.4.22 §1 lists the winding fixed points and states agreement with RECOG §6.3 |
| 94 | RECOG.R-C3 | deleted | DYAD-ALG-KP-FRAME-SCALE and the frame-named DYAD-ALG-BRIDGE-LEMMA settle the frame (ν₃^Z=cot²(π/p)ν₃^{W_p}; exported μ_p/ν₃ name their frame) |
| 95 | RECOG.R-S2 | retained | sources, dependencies and diagnostic semantics unchanged |
| 96 | RECOG.R-G1 | retained | sources, dependencies and diagnostic semantics unchanged |
| 97 | RECOG.R-R2 | retained | sources, dependencies and diagnostic semantics unchanged |
| 98 | RECOG.R-R3 | retained | sources, dependencies and diagnostic semantics unchanged |
| 99 | RECOG.R-P1 | deleted | D-PIN v0.2: RECOG's DYAD pins are deliberate and valid (DYAD reports the consumed passages unchanged); no demonstrated mismatch |
| 100 | RECOG.R-P2 | reworded | reclassified: the 'RID unavailable' statement contradicts the owner; age-only pins dropped |
| 101 | RECOG.R-P3 | reworded | age-only pins dropped (D-PIN v0.2); internal contradictions kept |
| 102 | RECOG.R-T1 | retained | sources, dependencies and diagnostic semantics unchanged |
| 103 | RECOG.R-T2 | retained | sources, dependencies and diagnostic semantics unchanged |
| 104 | RECOG.R-T3 | deleted | notice handling is process state (Method v0.2 §4.1); RER v0.2 records receipt of the RECOG G3 notice |
| 105 | RECOG.R-Y1 | retained | sources, dependencies and diagnostic semantics unchanged |
| 106 | RECOG.R-Y2 | retained | sources, dependencies and diagnostic semantics unchanged |
| 107 | RECOG.R-D1 | reworded | D-PROOF states named |
| 108 | F1 | reworded | RER separates κ/γ internally (notation block); cross-stream collision kept |
| 109 | F2 | reworded | restated against adopted RER v0.2 (γ=1 statement present, OFN class statement absent) |
| 110 | F3 | retained | ER-2B, FMS, GEN, RER cubic data unchanged |
| 111 | F4 | reworded | restated against adopted RER v0.2 (block retained, archive search negative) |
| 112 | F5 | reworded | RER now imports SMOOTH-EMBEDDING (RER.E2 retired); remaining stale sites FMS, ER-2B; chronology removed |
| 113 | F6 | retained | sources, dependencies and diagnostic semantics unchanged |
| 114 | F7 | retained | sources, dependencies and diagnostic semantics unchanged |
| 115 | F8 | reworded | D-PIN v0.2: age-only pin inventory removed (deliberate valid pins); demonstrated identity issue and RER internal contradiction kept |
| 116 | F9 | retained | sources, dependencies and diagnostic semantics unchanged |
| 117 | F10 | retained | sources, dependencies and diagnostic semantics unchanged |
| 118 | F11 | retained | sources, dependencies and diagnostic semantics unchanged |
| 119 | F12 | retained | sources, dependencies and diagnostic semantics unchanged |
| 120 | F13 | reworded | RER acceptance scope updated to adopted v0.2 |
| 121 | F14 | reworded | D-PROOF states named |
| 122 | F15 | retained | sources, dependencies and diagnostic semantics unchanged |
| 123 | F16 | retained | sources, dependencies and diagnostic semantics unchanged |
| 124 | F17 | retained | sources, dependencies and diagnostic semantics unchanged |
| 125 | F18 | reworded | record now receiver ACCEPT SCOPED in adopted RER; 'unreviewed' replaced by its current scope |
| 126 | F19 | retained | sources, dependencies and diagnostic semantics unchanged |
| 127 | F20 | retained | sources, dependencies and diagnostic semantics unchanged |
| 128 | F21 | deleted | DYAD v6.4.22 notice table: N2 Triadic ANSWERED |
| 129 | F22 | retained | RER G7/CND01 content unchanged apart from RRF v0.8.4 reference lines; OFN import pin still v0.9 |
| 130 | F23 | retained | RER G6 still OPEN; DYAD chain unchanged; triad has no smooth-embedding analogue |
| 131 | F24 | retained | sources, dependencies and diagnostic semantics unchanged |
| 132 | F25 | retained | sources, dependencies and diagnostic semantics unchanged |
| 133 | F26 | reworded | DYAD edition reference removed |
| 134 | F27 | reworded | restated against adopted RER v0.2 |
| 135 | F28 | reworded | 'now' removed |
| 136 | F29 | new | new: DYAD v6.4.22 owner RID relevant to an RER record |
| 137 | GEN.D1 | retained | sources, dependencies and diagnostic semantics unchanged |
| 138 | GEN.D2 | retained | sources, dependencies and diagnostic semantics unchanged |
| 139 | GEN.D3 | reworded | D-PROOF state named |
| 140 | GEN.D4 | retained | sources, dependencies and diagnostic semantics unchanged |
| 141 | GEN.D5 | retained | sources, dependencies and diagnostic semantics unchanged |
| 142 | GEN.D6 | retained | sources, dependencies and diagnostic semantics unchanged |
| 143 | GEN.D7 | retained | sources, dependencies and diagnostic semantics unchanged |
| 144 | GEN.D8 | deleted | D-PIN v0.2: GEN's DYAD v6.4.13 pin is deliberate (repin deferred, DYAD §7.0) and no mismatch is demonstrated; class-C content mismatch is DYAD.X1/GEN.D15 |
| 145 | GEN.D14 | retained | sources, dependencies and diagnostic semantics unchanged |
| 146 | OPENM.U1 | reworded | age-only pins dropped (D-PIN v0.2); the content link is kept |
| 147 | OPENM.U2 | reworded | process wording removed |
| 148 | OPENM.U3 | retained | sources, dependencies and diagnostic semantics unchanged |
| 149 | OPENM.U4 | reworded | process wording normalized |
| 150 | OPENM.U5 | retained | sources, dependencies and diagnostic semantics unchanged |
| 151 | OPENM.U6 | retained | sources, dependencies and diagnostic semantics unchanged |
| 152 | OPENM.U7 | reworded | 'now' removed |
| 153 | OPENM.U8 | reworded | audit status is review metadata, not a proof state; reclassified |
| 154 | OPENM.U9 | reworded | process wording removed |
| 155 | OPENM.U10 | retained | sources, dependencies and diagnostic semantics unchanged |
| 156 | OPENM.U11 | retained | sources, dependencies and diagnostic semantics unchanged |
| 157 | TDRG.G1 | reworded | process wording normalized |
| 158 | TDRG.G2 | retained | sources, dependencies and diagnostic semantics unchanged |
| 159 | TDRG.G3 | reworded | age-only pin clause dropped (D-PIN v0.2) |
| 160 | TDRG.G4 (D-WRONG) | retained | sources, dependencies and diagnostic semantics unchanged |
| 161 | TDRG.G5 | retained | sources, dependencies and diagnostic semantics unchanged |
| 162 | TDRG.G6 | retained | sources, dependencies and diagnostic semantics unchanged |
| 163 | TDRG.G7 | reworded | process wording normalized |
| 164 | TDRG.G8 | retained | sources, dependencies and diagnostic semantics unchanged |
| 165 | TDRG.G9 | retained | sources, dependencies and diagnostic semantics unchanged |
| 166 | AZ.A1 | reworded | process wording removed |
| 167 | AZ.A2 | retained | sources, dependencies and diagnostic semantics unchanged |
| 168 | AZ.A3 | reworded | age-only pins dropped (D-PIN v0.2) |
| 169 | AZ.A5 | retained | sources, dependencies and diagnostic semantics unchanged |
| 170 | AZ.A7 | retained | sources, dependencies and diagnostic semantics unchanged |
| 171 | D5.X1 | reworded | process wording removed |
| 172 | D5.X3 | retained | sources, dependencies and diagnostic semantics unchanged |
| 173 | NUMGEN.N-R1 (DISC part) | retained | sources, dependencies and diagnostic semantics unchanged |
| 174 | NUMGEN.N-S2 (DISC part) | retained | sources, dependencies and diagnostic semantics unchanged |
| 175 | NUMGEN.N-F (DISC part) | deleted | a pin check, not a diagnostic or a scientific fact |
| 176 | PREL.P1 + LEGACY.Y1 + PROG.G6 | reworded | age-only pins dropped (D-PIN v0.2); stale pointers kept |
| 177 | LEGACY.Y2 + PREL.P2 | reworded | process wording removed |
| 178 | LEGACY.Y3 + PREL.P3 | retained | sources, dependencies and diagnostic semantics unchanged |
| 179 | PREL.P4 | retained | sources, dependencies and diagnostic semantics unchanged |
| 180 | LEGACY.Y5 + PREL | retained | sources, dependencies and diagnostic semantics unchanged |
| 181 | PREL.P5 | retained | sources, dependencies and diagnostic semantics unchanged |
| 182 | PREL.P6 + LEGACY.Y4 | retained | sources, dependencies and diagnostic semantics unchanged |
| 183 | PREL.P7 | retained | sources, dependencies and diagnostic semantics unchanged |
| 184 | LEGACY.Y6 | retained | sources, dependencies and diagnostic semantics unchanged |
| 185 | PREL.P8 | reworded | PASS-with-note restated as a scope note with atlas-checked value |
| 186 | D6.X1 | reworded | stable key assigned; process wording removed |
| 187 | D6.X2 | reworded | stable key assigned; class corrected (internal conflict, not a link) |
| 188 | PASS block D6 | moved | PASS list removed from D6.L5 (Method v0.2 §6: atlas-checked facts at content layer); placed as evidence record *ATLAS:checked-D6 at the end of D6.L2; per-node distribution deferred to the compression pass |
| 189 | PASS block D5 | moved | PASS list removed from D5.L5 (Method v0.2 §6: atlas-checked facts at content layer); placed as evidence record *ATLAS:checked-D5 at the end of D5.L2; per-node distribution deferred to the compression pass |
| 190 | PASS block D4b | moved | PASS list removed from D4b.L5 (Method v0.2 §6: atlas-checked facts at content layer); placed as evidence record *ATLAS:checked-D4b at the end of D4b.L2; per-node distribution deferred to the compression pass |
| 191 | PASS block D4a | moved | PASS list removed from D4a.L5 (Method v0.2 §6: atlas-checked facts at content layer); placed as evidence record *ATLAS:checked-D4a at the end of D4a.L2; per-node distribution deferred to the compression pass |
| 192 | PASS block D3 | moved | PASS list removed from D3.L5 (Method v0.2 §6: atlas-checked facts at content layer); placed as evidence record *ATLAS:checked-D3 at the end of D3.L2; per-node distribution deferred to the compression pass |
| 193 | PASS block D2 | moved | PASS list removed from D2.L5 (Method v0.2 §6: atlas-checked facts at content layer); placed as evidence record *ATLAS:checked-D2 at the end of D2.L2; per-node distribution deferred to the compression pass |
| 194 | PASS block D1 | moved | PASS list removed from D1.L5 (Method v0.2 §6: atlas-checked facts at content layer); placed as evidence record *ATLAS:checked-D1 at the end of D1.L2; per-node distribution deferred to the compression pass |
| 195 | NUMGEN.N-C | reworded | PASS wording replaced by atlas-checked scope note |
| 196 | D3.L3 governance line | deleted (non-L5) | process state (repin requests, notice/receipt status, ownership offers); scientific residue kept in RECOG.R-P2 and RECOG.R-L4 |
| 197 | D4a.L3 governance line | deleted (non-L5) | process state (RID requests, disposition records, Programme pass); RID gaps kept in D4a.L5 F13 |
| 198 | D3.L1 K_p family; *RECOG:Kp-frame | edge replaced | [AV02] dangling pointer to retired RECOG.R-C3 replaced by the content edge ≡ DYAD-ALG-KP-FRAME-SCALE |
| 199 | D1 owners line; D2.L3 p-resonance, phase constants | process wording removed | [AV02] "pass one done / pass two pending", advisory tier/key "Tier-C target FC-DYAD-31", "(governance only)", "NUMGEN-side not started" removed; open target, available owner result and missing obligation kept |
| 200 | *ATLAS:checked-D1…D6 | typed | [AV02] each evidence record split into exact / numerical / source with execution context (atlas v0.1 build, carried forward, EV-NOT-RERUN); rounded evaluations written ≈ (e.g. 517·(256/225)²=33882112/50625≈669.276; 1.51632·1.06252=1.6111203264≈1.61112); diagnostic-key labels [PROG.G3]/[PROG.G8]/[METH.M3] dropped |
| 201 | *RECOG:fixed-points; *GEN WPHASE line; D2 b5/cascade lines | edge/marker corrected | [AV02] retired RECOG.R-L9 pointer replaced by the DYAD §1 content edge; abbreviated TRIAD-ALG-T6M replaced by the owner RID TRIAD-ALG-T6M-REFERENCE-QUARTER-TURN (found by the stricter link check); owner-classified strings marked as not owner RIDs |

## Retired keys

Never reused: OFN.O2, RRF.F1 (merged into OFN.O1, RRF side not stale), DZT.Q2, DZT.Q3, DYAD.X3, DYAD.X5, DYAD.X7, DYAD.X9, NUMGEN.N-C2, RECOG.R-L9, RECOG.R-C3, RECOG.R-P1, RECOG.R-T3, GEN.D8, D5.X2 (PASS content moved into `*ATLAS:checked-D5`), F21. The RER slice key RER.E2 is no longer cited in F5 (RER imports SMOOTH-EMBEDDING).
