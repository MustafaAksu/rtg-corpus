#!/usr/bin/env python3
"""DYAD v6.4.24 (maintenance candidate): single-stage, assertion-gated build from adopted v6.4.23.

Scope (records/dyad/DYAD_v6_4_24_BACKLOG.md, sections A, B, B2, C, C3; PI decision of 11 Nov 2026 to start the candidate):
  S1   new result DYAD-THM-OPEN21-SHARP-ROWS [assuming: RECOG-THM-R9-SHARPENED-ROWS] (Section 6.14; accepted by the
       co-owner, PR #150); pointers in the header summary and the OPEN 21 registry entry; Section 8 and Appendix E rows.
       DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER is not edited.
  X4   three RID registrations for existing statements (Atlas DYAD.X4): DYAD-ALG-NOT-AREA-PRESERVING (Section 6.1; the
       displayed tag is retagged [THM] -> [ALG], content unchanged; Section 1 readout follows), DYAD-ALG-P6-LINEAR-ORDER
       and DYAD-ALG-HOMOLOGICAL-RESONANCE (Section 6.6); Appendix E rows. No RID for the cubic radial rate across p.
  B2   DYAD-DEF-PRIMITIVE-MAP: the bare "provisional" replaced by a [scope:] note (definition, RID, imports unchanged);
       DYAD-ART-BRIDGE-NOTE: path, hash and availability note; DYAD-ART-BRIDGE-NOTE-CHECK.
  S3   OPEN 20: one [SESSION] paragraph on the state of the analytic-branch pilot (no result claimed; B-an, B-6 ACTIVE);
       Section 8 DYAD-ART-OPEN20-AN-PILOT.
  REG  consumer register: Section 7.0 rows and Section 7 lines to RECOG v0.3.27, Genesis v2.10, Triadic v1.7,
       Programme v1.4, AZ v0.7; notice-table and Appendix F state sentences (N16-N21 filed through pipes/).
  ED   edition lines (title, date, status, supersedes, release record, Appendix A entry, Appendix G note, footer).
No compaction. No statement, constant or OPEN status changed; one displayed grade tag changed (X4, retag); four result RIDs
and three artifact RIDs added. Every edit asserts exactly one occurrence of its old text in the current working text.
usage: build_dyad_v6_4_24.py BASE OUT EDITLOG_JSON
"""
import hashlib, json, sys

BASE_SHA = "9f874ccc1cd684482f26a27fca13b37102977cba2a80a75e762ecd7b300425cb"
REC = "records/dyad/RTG_DYADIC_v6_4_24_RELEASE_RECORD.md"
SUMMARY = ("S1 result on RECOG's sharpened R9 rows, three RID registrations, consumer register, bridge-note source, "
           "state of the OPEN 20 analytic-branch pilot")

S1 = (
    "`[THM]` `[assuming: RECOG-THM-R9-SHARPENED-ROWS]` [RID: DYAD-THM-OPEN21-SHARP-ROWS] `[v6.4.24]` `[proof: proof of "
    "DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER with the R9 constant replaced + exact-rational certificate]` `[scope: as "
    "DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER — rows A, B of NF-REM, not mixed; primitive start $W_0$]` `[import: "
    "RTG_RELATIONAL_RECOGNITION_DSN v0.3.26 §6.13a | RECOG-THM-R9-SHARPENED-ROWS; the entry is byte-identical at v0.3.27]` "
    "**Primitive-variable phase remainder, sharpened R9 rows.** With $\\mathcal P_2$, $M_W$ and $w_j$ as in "
    "DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER, for $0<|W_0|\\le w_j$:\n"
    "$$|M_W-\\mathcal P_2(W_0)|\\le K'_jQ_0^{3/2}+C'_{2,j}\\bigl(\\tfrac{256}{225}\\bigr)^2Q_0^2\\qquad\\text{(primary)},"
    "\\qquad |M_W-\\mathcal P_2(W_0)|\\le S_jQ_0^{3/2}\\qquad\\text{(secondary)},$$\n\n"
    "| Row | Chart disk | Primitive domain $w_j$ | $K'_j$ (unchanged) | $C'_{2,j}$ (sharpened R9) | $C'_{2,j}(256/225)^2$ | $S_j$ | adopted $K_j$ |\n"
    "|---|---|---|---|---|---|---|---|\n"
    "| A | $\\lvert z\\rvert\\le\\tfrac1{20}$ | $\\tfrac3{64}$ | $\\tfrac{3951}{1000}$ | $259.2$ | $\\tfrac{1048576}{3125}$ | $\\tfrac{492}{25}$ | $\\tfrac{8831}{250}$ |\n"
    "| B | $\\lvert z\\rvert\\le\\tfrac1{40}$ | $\\tfrac3{128}$ | $\\tfrac{971}{250}$ | $81.49$ | $\\tfrac{133513216}{1265625}$ | $\\tfrac{6357}{1000}$ | $\\tfrac{883}{100}$ |\n\n"
    "$S_j$ is the three-decimal ceiling of $K'_j+C'_{2,j}(256/225)^2w_j$ (exact values $19.67964$ and $6.356466963\\ldots$). "
    "*Proof.* In the proof outline of DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER, R9 enters only through the error $E$ of the "
    "chart-variable memory law, $|E|\\le C_2q_0^2+K_2q_0^{3/2}$; $K_2$ and the $T$-terms are Dyadic's own, so the bound is affine "
    "in $C_2$ through $C_2q_0^2\\le C_2(256/225)^2Q_0^2$. By RECOG-THM-R9-SHARPENED-ROWS the statement of RECOG-THM-R9-MEMORY "
    "holds with $C'_2=259.2$ ($q_0\\le\\tfrac1{400}$) and $C'_2=81.49$ ($q_0\\le\\tfrac1{1600}$) on the same rows. Hence, inside "
    "this proof, the memory law holds with $|E|\\le C'_{2,j}q_0^2+K_2q_0^{3/2}$ on the matching row, and every other step is "
    "unchanged. *Certificate:* DYAD-ART-OPEN21-SHARP-ROWS (exact rationals; gates G0–G5; five negative controls).\n\n"
    "`[DEF]` `[v6.4.24]` **Recorded distinctions.** (i) DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER keeps its statement, rows and "
    "`[assuming: RECOG-THM-R9-MEMORY]`; this entry is a separate result. (ii) It is conditional on RECOG-THM-R9-SHARPENED-ROWS at "
    "statement level and is not unconditional in R9; RECOG's certificate is not rerun here. (iii) The $-$C7 rows "
    "(RECOG-THM-R9-SHARPENED-ROWS-C7) are not used. (iv) $K'_j$ is used at statement level, as the adopted published ceiling; the P5 "
    "certificate is not in the repository (`records/dyad/DYAD_SOURCE_RECOVERY_LIST.md`). (v) The R9 term is still the larger part "
    "of $S_A$ ($15.729$ of $19.680$). No optimality is claimed.\n\n")

S3 = (
    "(B-an, analytic branch — state of work) `[SESSION]` `[v6.4.24]` **Sectorial pilot; no result is claimed.** Records: "
    "`records/dyad/DYAD_OPEN20_AN_LH2012_OWNER_ASSESSMENT.md`, `records/dyad/DYAD_OPEN20_AN_SECTORIAL_PILOT_DESIGN.md` and the "
    "stage records (§8 DYAD-ART-OPEN20-AN-PILOT). In the complexified raw frame, $F=T^6$ has two formal invariant curves "
    "$\\Gamma_\\pm$ ($w=a_\\pm z^2+\\cdots$), exchanged by $T$. By the pilot's decision rule, a certified nonzero sectorial jump of "
    "one branch would give divergence of $\\Gamma_\\pm$ and of $\\log F$; it would not decide B-an or B-6. "
    "(i) Stage 1, exact (OWNER-RUN): normalized data $k=3$, $m=2$, $\\alpha=-\\tfrac{102}{19}-\\tfrac{16\\sqrt3}{19}i$ on both "
    "branches; `[ALG]` the ratio is the same on both because $P'(u)=\\alpha\\,(c_{40}+\\mu u)$ identically, with $P$ the quadratic "
    "whose roots are $a_\\pm$ and $c_{40}=[z^4]F_z$. "
    "(ii) Literature basis, SESSION scope, through LIT: 3-summability of $\\Gamma_\\pm$ "
    "(`lopezhernanz2012-summable-curves@vor`, with LIT INF-005 to INF-008); local orbit structure of the complexified germ along "
    "$\\Gamma_\\pm$ (`lopezhernanz2025-flower@vor:Theorem 1.3`; `lopezhernanz2021-stable-manifolds@arxiv-v1:Theorem 5.1`, "
    "`:Theorem 7.1`; LIT INF-014, INF-015). The orbit statements are conditional and carry open source questions (FL-Q1, IMRN-Q1, "
    "an arXiv-v1 reading) and a separate identification step with the 3-sums; they are not `[THM]` imports. They concern the "
    "complexified germ only: on the real slice $w=\\bar z$, $|w/z^2|=1/|z|\\to\\infty$, so no real-orbit statement follows. "
    "(iii) Stage 2, `[NUM]`: the coefficients $a_2,\\dots,a_{216}$ of $\\Gamma_+$; the Borel scale read from them was INCONCLUSIVE. "
    "(iv) Stage 3a, owner calculation: the a-priori operator route (LIT INF-009, INF-010) is negative — in the $m=2$ normalized "
    "chart it admits only $|\\xi|<1.76\\cdot10^{-6}$, for every admissible sector opening and every scaling of the transversal "
    "coordinate, far below any radius at which the jump is resolvable. "
    "(v) Stage 2b, `[NUM]` scouting with no proved error bound: on one overlap the jump is numerically nonzero "
    "($|\\Delta_Y|$ from $1.6\\cdot10^{-5}$ at $|\\xi_*|=0.45$ to $7.3\\cdot10^{-50}$ at $|\\xi_*|=0.24$) and decays like "
    "$e^{-2\\pi T}$ in the Fatou time $T$ of the restricted map. "
    "None of (i)–(v) is a theorem about B-an or B-6; both stay ACTIVE, and no certification run is authorized.  \n")

A_ENTRY = (
    "### v6.4.24 — 11 November 2026 — Draft candidate\n\n"
    "- **S1 result:** `DYAD-THM-OPEN21-SHARP-ROWS` `[assuming: RECOG-THM-R9-SHARPENED-ROWS]`, §6.14: $S_A=\\tfrac{492}{25}$, "
    "$S_B=\\tfrac{6357}{1000}$ (adopted $K_A=\\tfrac{8831}{250}$, $K_B=\\tfrac{883}{100}$). `DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER` "
    "is unchanged.\n"
    "- **RID registrations (Atlas DYAD.X4):** `DYAD-ALG-NOT-AREA-PRESERVING` (§6.1; displayed tag retagged `[THM]`→`[ALG]`, a direct "
    "Jacobian computation, content unchanged), `DYAD-ALG-P6-LINEAR-ORDER`, `DYAD-ALG-HOMOLOGICAL-RESONANCE` (§6.6). The cubic radial "
    "rate across $p$ stays a statement-level import of `RECOG-ALG-NU3-CLOSED-FORM` without a Dyadic RID.\n"
    "- **`DYAD-DEF-PRIMITIVE-MAP`:** the bare \"provisional\" is replaced by a `[scope:]` note (the Programme's reference map; "
    "generator selection open). Definition, RID and imports unchanged.\n"
    "- **Sources:** `DYAD-ART-BRIDGE-NOTE` recovered (PI-supplied 3 Nov 2026; path and hash in §8) with its exact replay "
    "`DYAD-ART-BRIDGE-NOTE-CHECK`.\n"
    "- **OPEN 20:** one `[SESSION]` paragraph on the state of the analytic-branch sectorial pilot (stages 1, 2, 3a, 2b; literature "
    "basis through LIT); `DYAD-ART-OPEN20-AN-PILOT`. B-an and B-6 stay ACTIVE; no result is claimed.\n"
    "- **Consumer register:** §7.0 and §7 to RECOG v0.3.27, Genesis v2.10, Triadic v1.7, Programme v1.4, AZ v0.7; N16–N21 filed "
    "through `pipes/` (Genesis and AZ answered). NUMGEN and OFN had not answered the v6.4.23 notice.\n"
    "- No statement, constant or OPEN status changed; four result RIDs and three artifact RIDs added. Backlog "
    "`records/dyad/DYAD_v6_4_24_BACKLOG.md`; release record `" + REC + "`; predecessor tag `dyad-v6.4.23`.\n\n")

ART = (
    "\n- [RID: DYAD-ART-OPEN21-SHARP-ROWS] `[v6.4.24]` :: `evidence/dyad/scripts/dyad_s1_open21_sharp_rows_cert.py` (SHA-256 "
    "`325c2a8a787a5660d5acc243e5b27fcfc91fc225460b0ada9d4b52464c0130ef`); outputs `evidence/dyad/s1-open21-sharp/`; design and review "
    "record `records/dyad/DYAD_S1_OPEN21_SHARP_ROWS_DESIGN.md` :: exact-rational certificate of $S_A$, $S_B$: inputs read from the tags "
    "`dyad-v6.4.23` and `recog-v0.3.26` (G0), adopted table reproduced (G1), windows (G2), constant used (G3), outward minimal ceilings "
    "(G4), $S_j<K_j$ (G5); controls C7, MIX, FLOOR, NOFACTOR, W2 exit 1 :: evidence for DYAD-THM-OPEN21-SHARP-ROWS at constant level; "
    "OWNER-RUN\n"
    "- [RID: DYAD-ART-BRIDGE-NOTE-CHECK] `[v6.4.24]` :: `evidence/dyad/scripts/dyad_bridge_note_v1_1_check.py` (SHA-256 "
    "`a0382ceaab5c4a40c09dd2623e7c76d3f89adaa9ed1ec6713648646d75e24734`); outputs `evidence/dyad/bridge-note-v1-1/`; record "
    "`records/dyad/DYAD_UPLOAD_HASH_CHECK_20261103_BRIDGE_NOTE.md` :: exact replay (sympy) of DYAD-ART-BRIDGE-NOTE against the note text "
    "and `dyad-v6.4.23`: odd-channel identity for general $K$, $\\det\\nabla T$ (gate B2), the $p=6$ frame (B3), one-step $\\nu_3$ by an "
    "independent normal-form computation (B5), $\\mu_6$, bridge lemma for $p=5,6,7$, protection matrix, Genesis lift; five negative "
    "controls exit 1 :: evidence for DYAD-ALG-NOT-AREA-PRESERVING (B2); OWNER-RUN\n"
    "- [RID: DYAD-ART-OPEN20-AN-PILOT] `[v6.4.24]` :: stage 1 `evidence/dyad/scripts/dyad_open20_an_stage1_prep.py` "
    "(`5c22ff7aab5d9dabdf243bfc6e279616b4fdbc5ea9d8429fa513c3b2584d8568`), output `evidence/dyad/open20-an/stage1_prep.json` "
    "(`2c9ae6376e0c482f2ba520a7ea8e2b38606a6821f7ac3bfa259d4d6020d04739`); stage 2 `dyad_open20_an_stage2_scout.py` "
    "(`2961e6383eb9b0e5fb58c0fcb892aa6b05dc2be0faf4c766a3f85be1346008ad`), outputs `evidence/dyad/open20-an/stage2/`; stage 3a "
    "`dyad_open20_an_stage3_apriori_route_check.py` (`692dd395584eabdd880f37c1e5cbabe26ca00bcdae14dbca6827392fe31f4430`), outputs "
    "`evidence/dyad/open20-an/stage3-route/`; LIT hypothesis check `dyad_open20_lit_inf014_inf015_hypothesis_check.py` "
    "(`517be03623da791a9759856d18491f676175d399c62c3ace7fbf8e887531b4d4`), outputs `evidence/dyad/open20-an/lit-inf014-inf015/`; stage 2b "
    "`dyad_open20_an_stage2b_jump_scout.py` (`2d125640243d255971a0284cac2613607791b47390ae0079d87a3488f31f96c8`) and "
    "`dyad_open20_an_stage2b_law.py` (`0cfe90f884a7ce69f9670202978ffabd1473233e7c7b174e28dab61f5ce3c623`), outputs "
    "`evidence/dyad/open20-an/stage2b/`; records `records/dyad/DYAD_OPEN20_AN_SECTORIAL_PILOT_DESIGN.md`, "
    "`DYAD_OPEN20_AN_LH2012_OWNER_ASSESSMENT.md`, `DYAD_OPEN20_AN_STAGE2_SCOUTING_NUM.md`, `DYAD_OPEN20_AN_STAGE2B_JUMP_SCOUTING_NUM.md` "
    ":: the analytic-branch sectorial pilot of OPEN 20 (§2); exact stage 1, `[NUM]` stages 2 and 2b, design calculation 3a :: "
    "SESSION working evidence; no theorem rests on it; OWNER-RUN")

E1 = (
    "\n| `DYAD-THM-OPEN21-SHARP-ROWS` | THM `[assuming: RECOG-THM-R9-SHARPENED-ROWS]` — new in v6.4.24 | as "
    "DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER; rows not mixed | §6.14 | DYAD-ART-OPEN21-SHARP-ROWS | `325c2a8a…30ef` | exact rational "
    "| constants $S_A$, $S_B$ only; $K'_j$ and R9 at statement level |\n"
    "| `DYAD-ALG-NOT-AREA-PRESERVING` | ALG — RID new in v6.4.24 (tag retagged from THM) | the map $T$, globally | §6.1 | "
    "DYAD-ART-BRIDGE-NOTE-CHECK (gate B2) | `a0382cea…4734` | exact symbolic (sympy) | Jacobian determinant identity |\n"
    "| `DYAD-ALG-P6-LINEAR-ORDER` | ALG — RID new in v6.4.24 | linear part at $P_1$ | §6.6 | elementary; DYAD-ART-BRIDGE-NOTE-CHECK "
    "(gate B3: $\\lambda^6=1$, $\\lambda^3=-1$) | `a0382cea…4734` | exact symbolic (sympy) | order of $\\lambda$ only |\n"
    "| `DYAD-ALG-HOMOLOGICAL-RESONANCE` | ALG — RID new in v6.4.24 | one-step normal form at $P_1$ | §6.6 | `dyad_p1_math_checks.py` "
    "P1-3 | not recorded | exact | resonance condition and divisor moduli |")

E2 = (
    "\n| `DYAD-THM-OPEN21-SHARP-ROWS` | 3 Nov 2026 (certificate; gates G0–G5, five controls) | not recorded (co-owner source review, "
    "PR #150 reviews `5748327144`, `5748500129`) | not recorded | co-owner rational pre-check ($19.679640$, $6.356467$) | $K'_j$ at "
    "statement level (P5 certificate not in the repository); RECOG's certificate not rerun |\n"
    "| `DYAD-ALG-NOT-AREA-PRESERVING` | 3 Nov 2026 (bridge-note check, gate B2) | not recorded | not recorded | — | — |\n"
    "| `DYAD-ALG-P6-LINEAR-ORDER` | 3 Nov 2026 (bridge-note check, gate B3) | not recorded | not recorded | — | — |\n"
    "| `DYAD-ALG-HOMOLOGICAL-RESONANCE` | P1 (`dyad_p1_math_checks.py` P1-3) | not recorded | not recorded | — | script hash not "
    "recorded in this ledger |")

EDITS = [
# ---- ED: edition lines
("ED-1", "title", "# RTG_DYADIC_OSCILLATOR_DSN_v6.4.23\n", "# RTG_DYADIC_OSCILLATOR_DSN_v6.4.24\n"),
("ED-2", "header date", "**Date:** 30 October 2026  \n", "**Date:** 11 November 2026  \n"),
("ED-3", "header status",
 "**Document status:** ADOPTED — PI, 30 October 2026 (inbox round D1–D7: OPEN 18 step-indexed successor RID, two registrations for RECOG, displayed-decimal corrections, consumer register). Adoption record: `records/dyad/RTG_DYADIC_v6_4_23_RELEASE_RECORD.md`.",
 "**Document status:** DRAFT — v6.4.24 candidate (" + SUMMARY + "); not adopted."),
("ED-4", "header supersedes",
 "**Supersedes:** `RTG_DYADIC_OSCILLATOR_DSN_v6.4.22` (SHA-256 `2363ca409c08bc571378125771f27239b6426d3e7cdbe75e0306a2a728778c29`; tag `dyad-v6.4.22`).",
 "**Supersedes:** `RTG_DYADIC_OSCILLATOR_DSN_v6.4.23` (SHA-256 `" + BASE_SHA + "`; tag `dyad-v6.4.23`)."),
("ED-5", "header release record",
 "**Release record:** `records/dyad/RTG_DYADIC_v6_4_23_RELEASE_RECORD.md`. Version history: Appendix A.",
 "**Release record:** `" + REC + "`. Version history: Appendix A."),
("ED-6", "Appendix G note", "v6.4.21 to v6.4.23 keep every heading anchor of v6.4.20.", "v6.4.21 to v6.4.24 keep every heading anchor of v6.4.20."),
("ED-7", "footer",
 "*END OF DOCUMENT — RTG_DYADIC_OSCILLATOR_DSN_v6.4.23 (ADOPTED, 30 October 2026).*",
 "*END OF DOCUMENT — RTG_DYADIC_OSCILLATOR_DSN_v6.4.24 (DRAFT candidate, 11 November 2026).*"),
("ED-8", "Appendix A entry", "### v6.4.23 — 30 October 2026 — Adopted\n", A_ENTRY + "### v6.4.23 — 30 October 2026 — Adopted\n"),
("ED-9", "Section 7.0 own row",
 "| Dyadic (this ledger) | v6.4.23 | this edition; status in the header; its SHA-256 is in its release record | predecessor v6.4.22: `2363ca409c08bc571378125771f27239b6426d3e7cdbe75e0306a2a728778c29` | tag `dyad-v6.4.22`; release records in `records/dyad/` |",
 "| Dyadic (this ledger) | v6.4.24 | this edition; status in the header; its SHA-256 is in its release record | predecessor v6.4.23: `" + BASE_SHA + "` | tag `dyad-v6.4.23`; release records in `records/dyad/` |"),
# ---- S1
("S1-1", "header summary pointer",
 "(OPEN 21; conditional on `RECOG-THM-R9-MEMORY`)",
 "(OPEN 21; conditional on `RECOG-THM-R9-MEMORY`, with the sharper companion `DYAD-THM-OPEN21-SHARP-ROWS` conditional on `RECOG-THM-R9-SHARPENED-ROWS`)"),
("S1-2", "OPEN 21 registry pointer",
 "Status: **CLOSED (v6.4.17)** by `DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER` (§6.14; `[THM]` `[assuming: RECOG-THM-R9-MEMORY]`), per row, R9 term kept separate.  \n",
 "Status: **CLOSED (v6.4.17)** by `DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER` (§6.14; `[THM]` `[assuming: RECOG-THM-R9-MEMORY]`), per row, R9 term kept separate.  \n"
 "`[v6.4.24]` Companion with smaller constants on RECOG's sharpened R9 rows: `DYAD-THM-OPEN21-SHARP-ROWS` (§6.14; `[THM]` `[assuming: RECOG-THM-R9-SHARPENED-ROWS]`). The closing result and its rows are unchanged.  \n"),
("S1-3", "Section 6.14 new result",
 "`[OPEN]` `[v6.4.17]` **Not established:** an unconditional version (independent of R9);",
 S1 + "`[OPEN]` `[v6.4.17]` **Not established:** an unconditional version (independent of R9);"),
# ---- X4
("X4-1", "Section 1 readout, not area-preserving",
 "`[THM]` The map is not globally area-preserving:\n",
 "`[ALG]` `DYAD-ALG-NOT-AREA-PRESERVING` `[v6.4.24: retagged from [THM]; direct Jacobian computation; content unchanged]` The map is not globally area-preserving:\n"),
("X4-2", "Section 6.1 RID, not area-preserving",
 "`[THM]` Map is not globally area-preserving. The equality",
 "`[ALG]` [RID: DYAD-ALG-NOT-AREA-PRESERVING] `[v6.4.24: RID registered; retagged from [THM]; direct Jacobian computation; content unchanged]` Map is not globally area-preserving. The equality"),
("X4-3", "Section 6.6 RID, p=6 linear order",
 "`[ALG]` `[v6.4.20: retagged from [THM]; content stated exactly]` **$p=6$ linear order.**",
 "`[ALG]` [RID: DYAD-ALG-P6-LINEAR-ORDER] `[v6.4.20: retagged from [THM]; content stated exactly]` `[v6.4.24: RID registered]` **$p=6$ linear order.**"),
("X4-4", "Section 6.6 RID, homological resonance",
 "`[ALG]` `[v6.4.20]` **Homological resonance is a separate condition.**",
 "`[ALG]` [RID: DYAD-ALG-HOMOLOGICAL-RESONANCE] `[v6.4.20]` `[v6.4.24: RID registered]` **Homological resonance is a separate condition.**"),
# ---- B2
("B2-1", "primitive map label",
 "`[DEF]` `DYAD-DEF-PRIMITIVE-MAP` `[v6.4.11, provisional]` **Dyad map.**",
 "`[DEF]` `DYAD-DEF-PRIMITIVE-MAP` `[v6.4.11]` `[scope: the Programme's reference map (Programme Overview v1.4 §5); the selection of the generator is open (`RTG-OPEN-GENERATOR-SELECTION`, OPEN-P0). v6.4.24: this note replaces the bare \"provisional\"; definition, RID and imports unchanged]` **Dyad map.**"),
("B2-2", "bridge note source",
 "- [RID: DYAD-ART-BRIDGE-NOTE] :: `dyad_triad_antisymmetric_bridge_v1_1.md` :: Bridge note v1.1: antisymmetric odd-channel identity, $\\mu_p=p\\bar\\lambda\\nu_3^{(1,p)}$, protection matrix, Genesis lift obstruction :: `[ALG]`",
 "- [RID: DYAD-ART-BRIDGE-NOTE] :: `upload/dyad-bridge-note/dyad_triad_antisymmetric_bridge_v1_1.md` (SHA-256 `5ddebfe46b5572761a5154a05712fbcfe4e675f912430ee7d6bfcf0d93f4e875`; `[v6.4.24]` PI-supplied 3 Nov 2026, no earlier hash on record, identified by name and content) :: Bridge note v1.1: antisymmetric odd-channel identity, $\\mu_p=p\\bar\\lambda\\nu_3^{(1,p)}$, protection matrix, Genesis lift obstruction; its §1 prints $\\Delta_cT_\\eta$ in the $K=1$ form (general $K$: $2cb+2Ke^\\rho\\sinh(ca)-2K\\cos\\eta\\sin(cb)$) :: `[ALG]`; replay DYAD-ART-BRIDGE-NOTE-CHECK"),
# ---- S3
("S3-1", "OPEN 20 pilot paragraph",
 "No conjecture on the analytic or existence outcomes is recorded.",
 S3 + "No conjecture on the analytic or existence outcomes is recorded."),
# ---- artifacts and Appendix E
("ART-1", "Section 8 new artifact entries",
 "evidence for DYAD-THM-OPEN18-STEP-MONOTONE, DYAD-THM-NF-REM-C7-SHARP and DYAD-THM-LPHASE-ROWA-BRIDGE at statement and constant level; OWNER-RUN",
 "evidence for DYAD-THM-OPEN18-STEP-MONOTONE, DYAD-THM-NF-REM-C7-SHARP and DYAD-THM-LPHASE-ROWA-BRIDGE at statement and constant level; OWNER-RUN" + ART),
("E-1", "Appendix E.1 rows",
 "| FLINT/Arb (C++); python-flint | $n=3$ on $(0,\\sup G]$, $n=4$ on $[\\inf G,2]$; zero of $\\rho_4$ unique in $G$ |",
 "| FLINT/Arb (C++); python-flint | $n=3$ on $(0,\\sup G]$, $n=4$ on $[\\inf G,2]$; zero of $\\rho_4$ unique in $G$ |" + E1),
("E-2", "Appendix E.2 rows",
 "| co-owner mpmath sanity check of $q_{3/4}$ (not an interval certificate) | micro-strip MVT step and box logic not re-audited |",
 "| co-owner mpmath sanity check of $q_{3/4}$ (not an interval certificate) | micro-strip MVT step and box logic not re-audited |" + E2),
# ---- REG: Section 7.0 rows
("REG-1", "RECOG current row",
 "| RECOG | v0.3.26 | ADOPTED 28 Oct 2026 (current) | `45e307f8333c81a344158ada07ad34a1a3afab6e1b93b2aa04ee09f84878dd34` | tag `recog-v0.3.26`; RECOG release record | consumer of §6.14 (NF6, NF-REM, NF-INV, PRIM-CTR; LPHASE (D5) constants under `[assuming:]`) |",
 "| RECOG | v0.3.27 | ADOPTED 4 Nov 2026 (current) | `19556f913f51b98599faa6ad88c363dda0a278345677f3bd69f3b892d810e1f1` | tag `recog-v0.3.27`; RECOG release record | consumer of §6.14 (NF6, NF-REM, NF-INV, PRIM-CTR); imports `DYAD-THM-LPHASE-ROWA-BRIDGE`, `DYAD-THM-OPEN3-SPIRAL-REM` and `DYAD-THM-NF-REM-C7-SHARP` (answer to the v6.4.23 notice; $c'_Q=0.36916$ used throughout); source of `RECOG-THM-R9-SHARPENED-ROWS` for `DYAD-THM-OPEN21-SHARP-ROWS` (entry byte-identical to v0.3.26) |\n"
 "| RECOG | v0.3.26 | ADOPTED 28 Oct 2026; superseded by v0.3.27 | `45e307f8333c81a344158ada07ad34a1a3afab6e1b93b2aa04ee09f84878dd34` | tag `recog-v0.3.26`; RECOG release record | pin of the S1 certificate input (DYAD-ART-OPEN21-SHARP-ROWS, gate G0) |"),
("REG-2", "Genesis row",
 "| Genesis Geometry | v2.9 | ADOPTED 25 Oct 2026 | `9178ca2cd38bea8d55deada78b6adbd8022533c4baad7af101583b1179d300ac` | tag `gen-v2.9`; Genesis release record | consumer;",
 "| Genesis Geometry | v2.10 | ADOPTED 3 Nov 2026 | `63c3b020d9c63a43a2e5e9a43c411fad2d07dfcab33995bd928683435bb13d62` | tag `gen-v2.10`; Genesis release record | consumer; `DYAD-ALG-NU5-P5` row with the corrected field label and a claim-level pin `dyad-v6.4.23` §6.11 (answer to the 3 Nov notice);"),
("REG-3", "Triadic row",
 "| Triadic Birth-Lift | v1.6.1 | ADOPTED 19 Oct 2026 | not recorded in this ledger | Triadic release record (not in the project) | consumer; §7.1 repins to Dyadic v6.4.13 (N2 answered) |",
 "| Triadic Birth-Lift | v1.7 | ADOPTED 3 Nov 2026 | `506f3403628ca01d5a904f885df055d9bfbdf1ef5e474e24e83d4797c122e64a` | tag `triad-v1.7`; Triadic release record | consumer; §7.1 repins its five Dyadic imports to `dyad-v6.4.23` after a claim-level re-read; `DYAD-ALG-KP-FRAME-SCALE` and the isolated-dyad results (ℤ₆ generator, Lemma F, OPEN 20) are not imported |"),
("REG-4", "Programme row",
 "| Programme Overview | v1.3 | ADOPTED | `1b8358b3e1d3abb853e226786d21e6559c289b7c85570dac0ff1ebc2dabaea06` | tag `programme-v1.3` | SG-PROG-1–4; `RTG-OPEN-GENERATOR-SELECTION` |",
 "| Programme Overview | v1.4 | ADOPTED 4 Nov 2026 | `37d857d08bb47771ed50fc5829584be74aab120a23e922eba7c84bae097f28c0` | tag `programme-v1.4` | SG-PROG-1–4; `RTG-OPEN-GENERATOR-SELECTION` (both unchanged from v1.3); its Dyadic rows read at `dyad-v6.4.23` |"),
("REG-5", "AZ row",
 "| AZ | v0.6 | June 2026 (project copy) | not recorded in this ledger | — | string crosswalk (Appendix F) |",
 "| AZ | v0.7 | ADOPTED 11 Nov 2026 (corrections only) | `2294d2a3287651802824a77ea22fb8f3896f6837cca1162fd8479ff02839fc94` | tag `az-v0.7`; AZ release record | reference consumer; its `[import-ref]` rows pin `dyad-v6.4.23` and use owner RIDs; string crosswalk of v0.6 in Appendix F |"),
# ---- REG: Section 7 text
("REG-6", "programme context line", "- `RTG_PROGRAMME_OVERVIEW_v1.3` — SG-PROG-1 through SG-PROG-4;", "- `RTG_PROGRAMME_OVERVIEW_v1.4` — SG-PROG-1 through SG-PROG-4;"),
("REG-7", "RECOG context line",
 "for the claim-level import pins (current edition v0.3.26, §7.0)",
 "for the claim-level import pins (current edition v0.3.27, §7.0; `RECOG-THM-R9-SHARPENED-ROWS` is imported at v0.3.26 §6.13a by `DYAD-THM-OPEN21-SHARP-ROWS`)"),
("REG-8", "Triadic export line",
 "- `RTG_TRIADIC_BIRTH_LIFT_DSN` (v1.6.1, adopted 19 Oct 2026) — §7.1 imports `DYAD-THM-C21`, `DYAD-ALG-BRIDGE-LEMMA`, `DYAD-DEF-BRIDGE-EXPORT-CONTRACT` item 1, `DYAD-ALG-PROTECTION-MATRIX` and `DYAD-DEF-PRIMITIVE-MAP`, pinned to Dyadic v6.4.13 (N2 answered).",
 "- `RTG_TRIADIC_BIRTH_LIFT_DSN` (v1.7, adopted 3 Nov 2026) — §7.1 imports `DYAD-THM-C21`, `DYAD-ALG-BRIDGE-LEMMA`, `DYAD-DEF-BRIDGE-EXPORT-CONTRACT` item 1, `DYAD-ALG-PROTECTION-MATRIX` and `DYAD-DEF-PRIMITIVE-MAP`, repinned to Dyadic v6.4.23 after a claim-level re-read (N2 answered at v1.6.1). `DYAD-ALG-KP-FRAME-SCALE` and the isolated-dyad results are not imported."),
("REG-9", "Genesis export line",
 "- `RTG_GENESIS_GEOMETRY_DSN` (v2.9, adopted 25 Oct 2026) — imports",
 "- `RTG_GENESIS_GEOMETRY_DSN` (v2.10, adopted 3 Nov 2026; its `DYAD-ALG-NU5-P5` row is pinned at `dyad-v6.4.23` §6.11) — imports"),
("REG-10", "RECOG consumer line",
 "acceptance recorded from v0.3.2 and retained through v0.3.26; v0.3.26 also carries the NF-REM certificate values and the (D5) row-A constants of `DYAD-THM-LPHASE-ROWA-REMAINDER` under `[assuming:]` (registered here as `DYAD-THM-NF-REM-C7-SHARP` and `DYAD-THM-LPHASE-ROWA-BRIDGE`; whether RECOG drops the qualifier is RECOG's decision, after its re-check with $c'_Q=0.36916$).",
 "acceptance recorded from v0.3.2 and retained through v0.3.27; v0.3.27 imports `DYAD-THM-NF-REM-C7-SHARP`, `DYAD-THM-LPHASE-ROWA-BRIDGE` and `DYAD-THM-OPEN3-SPIRAL-REM` (re-check with $c'_Q=0.36916$ done by RECOG; its known-$a$ chain carries no (D5) `[assuming:]`). RECOG's own `RECOG-ALG-A1C-JET-REMAINDER-BOUNDS` ($c_J\\le0.500819$, $c_7\\le100.231$ on $q\\le\\tfrac{256}{140625}$) is not registered here; the constants of `DYAD-THM-LPHASE-ROWA-REMAINDER` are unchanged."),
# ---- REG: notices and Appendix F state sentences
("REG-11", "notice table sentence",
 "Notices N16–N21 are prepared and not yet sent (`records/dyad/DYAD_NOTICES_N16_N21.md`, routed through the PI); their states per recipient (sent, received, statement accepted, adopted use) are kept there and entered in this table when a state is recorded.",
 "`[v6.4.24]` Notices N16–N21 were filed on 3 November 2026 as items in `pipes/<STREAM>/` (per-recipient disposition in `records/dyad/DYAD_NOTICES_N16_N21.md`); Genesis (v2.10) and AZ (v0.7) have answered. From v6.4.23 on, notices are pipe items: their states are read from `pipes/<STREAM>/INDEX.md` and are not copied into this table."),
("REG-12", "Appendix F state sentence",
 "consumer repins are requested by notice N17 (prepared, not yet sent; `records/dyad/DYAD_NOTICES_N16_N21.md`).",
 "consumer repins were requested by notice N17 (filed through `pipes/` on 3 November 2026; `records/dyad/DYAD_NOTICES_N16_N21.md`). `[v6.4.24]` AZ answered at `az-v0.7`: every Dyadic-pattern string it prints is an owner RID, except the closed lifecycle item `DYAD-OPEN-B5-ALLP` and one occurrence of `DYAD-ALG-Q3-CANCEL` in its Appendix A change entry; the AZ rows below record the v0.6 reading and are kept as history. DZT has not answered."),
]


def main():
    base, out, logp = sys.argv[1:4]
    raw = open(base, 'rb').read()
    assert hashlib.sha256(raw).hexdigest() == BASE_SHA, 'base is not dyad-v6.4.23'
    txt = raw.decode('utf-8')
    log = []
    for eid, what, old, new in EDITS:
        n = txt.count(old)
        assert n == 1, (eid, what, n)
        txt = txt.replace(old, new)
        log.append({'id': eid, 'what': what, 'old_sha256': hashlib.sha256(old.encode()).hexdigest(),
                    'new_sha256': hashlib.sha256(new.encode()).hexdigest()})
    data = txt.encode('utf-8')
    open(out, 'wb').write(data)
    json.dump({'base_sha256': BASE_SHA, 'out_sha256': hashlib.sha256(data).hexdigest(), 'n_edits': len(EDITS), 'edits': log},
              open(logp, 'w', encoding='utf-8', newline='\n'), indent=1, sort_keys=True)
    print('edits', len(EDITS), 'out', hashlib.sha256(data).hexdigest())


if __name__ == '__main__':
    main()
