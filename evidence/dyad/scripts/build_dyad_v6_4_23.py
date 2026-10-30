#!/usr/bin/env python3
"""DYAD v6.4.23 (maintenance candidate): single-stage, assertion-gated build from adopted v6.4.22.

Scope: the joint owner/co-owner reconciliation of the inbox round (records/dyad/DYAD_INBOX_20261030_RECONCILIATION.md,
accepted by the co-owner, PR #130 comment 6522082716), items D1-D6, plus the OFN v0.12 notice (D7, owner disposition in
the reconciliation addendum; needs co-owner confirmation):
  D1  successor RID DYAD-THM-OPEN18-STEP-MONOTONE (step-indexed monotonicity; q_{3/4} isolated in G); the adopted
      DYAD-THM-OPEN18 keeps its text and grade with a [scope:] note (historical first-footprint formulation); summary
      lines cite the successor; Section 8 / Appendix E rows
  D2  new RID DYAD-THM-NF-REM-C7-SHARP (C_7 <= 85.1 / 27.7); [COR] of the displayed certificate values at the NF-REM table
  D3  new RID DYAD-THM-LPHASE-ROWA-BRIDGE (exact decomposition; c_Q = 0.79246, c'_Q = 0.36916); [COR] of the displayed
      decimal chain at the L-PHASE proof outline (0.36915 / 1.51632 / 1.06252 / 1.61112 -> 0.36916 / 1.51633 / 1.06253 /
      1.61115); the "certificate value 1.61112" displays (Section 2 table, Section 7.0a)
  D4-D7  consumer register: Section 7.0 rows (NUMGEN v1.21, RECOG v0.3.26, OFN v0.12, Genesis v2.9, Programme v1.3,
      Methodology v1.4), Section 7 context and consumer lines, notice-receipt rows N4/N6/N14 (OFN) and N15 (NUMGEN)
  ED  edition lines (title, date, status, supersedes, release record, Appendix A entry, Appendix G note, footer)
No compaction. No existing RID, grade or OPEN status changed; three result RIDs and one artifact RID added. Appendix A history is not edited (one
entry is added). Every edit asserts exactly one occurrence of its old text in the current working text.
usage: build_dyad_v6_4_23.py BASE OUT EDITLOG_JSON
"""
import hashlib, json, sys

BASE_SHA = "2363ca409c08bc571378125771f27239b6426d3e7cdbe75e0306a2a728778c29"
REC = "records/dyad/RTG_DYADIC_v6_4_23_RELEASE_RECORD.md"
RECON = "`records/dyad/DYAD_INBOX_20261030_RECONCILIATION.md`"
OWN = "`evidence/dyad/scripts/dyad_inbox_20261030_owner_checks.py`"
CHAIN = "`evidence/dyad/scripts/dyad_inbox_20261030_l902_chain.py`"
OPEN18_SHA = "a9acb69f532a8535c6e18a1da3658a33587737874436ff7020734fba01d36ae4"
QINT = r"[1.260214202563477114872438560955,\ 1.260214202563477114872438560958]"

SUCC = (
    "`[THM-ALG via IA]` [RID: DYAD-THM-OPEN18-STEP-MONOTONE] `[v6.4.23]` `[scope: canonical family $(\\rho_0,\\eta_0)=(0,q)$; "
    "step-indexed; the labels $\\Gamma_3:=(0,q_{3/4}]$, $\\Gamma_4:=[q_{3/4},2]$ are a presentation convention, not a footprint-branch claim]` "
    "**OPEN 18, step-indexed form.** With $Q_n=\\rho_n^2-\\rho_n\\eta_n+\\eta_n^2$ and $\\Theta_n=\\operatorname{Arg}(\\rho_n+\\omega\\eta_n)$, "
    "$\\omega=e^{2\\pi i/3}$, along the orbit of $(0,q)$ (unwrapped $\\eta$, as in the certificate; this is the §6.8 angle wherever $|\\eta_n|<\\pi$): $dQ_3/dq>0$ and $d\\Theta_3/dq<0$ for $q\\in(0,\\,1.26021520256]$; $dQ_4/dq>0$ and $d\\Theta_4/dq<0$ for "
    "$q\\in[1.26021320256,\\,2]$. In $G=[1.26021320256,\\,1.26021520256]$, $\\rho_4$ has exactly one zero $q_{3/4}\\in" + QINT + "$, "
    "and $\\Theta_4(q_{3/4})=-\\pi/3$ (the ISP-funnel edge). Uniqueness is stated in $G$ only. *Evidence:* DYAD-ART-OPEN18 "
    "(macro sweeps $n=3$ on $[0.001,\\inf G]$ and $n=4$ on $[\\sup G,2]$, micro strip on $(0,0.001]$; the program exits 0 "
    "unconditionally, so its result is read from its printed lines) and DYAD-ART-INBOX-20261030 checks O1 (isolation) and "
    "O3 (both steps on all of $G$). $q_{3/4}$ is not NUMGEN's $q_*$ (a root of $\\eta_6(q)-q$): $\\eta_6(q_{3/4})-q_{3/4}\\approx-0.5537$ (O2).")

OLD18_NOTE = (
    " `[scope: historical first-footprint formulation; the footprint predicate and branch legality are not substantiated by the "
    "recovered archive and are not available for a new downstream claim (evidence obligation open; "
    "records/dyad/DYAD_SOURCE_RECOVERY_LIST.md). The separately certified step-indexed content is DYAD-THM-OPEN18-STEP-MONOTONE. "
    "The isolation of the $\\rho_4$ zero in $G$ does not establish equivalence with the missing footprint audit.]`")

C7SHARP = (
    "`[THM]` [RID: DYAD-THM-NF-REM-C7-SHARP] `[v6.4.23]` `[proof: exact-rational certificate]` `[scope: chart and norm of "
    "DYAD-THM-NF-REM; rows not mixed]` **Sharper $C_7$ rows.** $|\\widehat F(z)-J(z)|\\le C_7|z|^7$ with $C_7=85.1$ on "
    "$|z|\\le\\tfrac1{20}$ and $C_7=27.7$ on $|z|\\le\\tfrac1{40}$. *Evidence:* DYAD-ART-RE-P2B2 `outputs/certificate.json`, "
    "`profiles.enlarged`/`profiles.small`.`value_rational_upper` (exact bounds $85.0731933471\\ldots$, $27.6022209836\\ldots$; "
    "DYAD-ART-INBOX-20261030 check O5). The constants of DYAD-THM-NF-REM ($C_7=100/30$, $C_D=1000/250$) are unchanged and remain "
    "the inputs of every proof that cites them; the certificate's $C_D$ bounds were computed with $C_7=100/30$ and are not "
    "re-derived here.")

BRIDGE = (
    "`[THM]` [RID: DYAD-THM-LPHASE-ROWA-BRIDGE] `[v6.4.23]` `[proof: exact identity + exact-rational certificate]` `[scope: "
    "row-A disk $|z|\\le\\tfrac1{20}$ of the chart of DYAD-THM-NF-INV, used at block base points in $U$; branch control (B) on "
    "$U_T$]` **Row-A bridge lemma.** (i) `[ALG]` Under (B), $r=\\Lambda_3(z)+[S_\\Theta-L_\\Theta]+\\tau[D_Q-D_3]+"
    "[\\operatorname{Arg}(J/z)+\\tau q]+\\operatorname{Arg}(\\widehat F/J)$ exactly, $\\Lambda_3=L_\\Theta+\\tau D_3$, with $D_Q$, $D_3$ "
    "as defined in this section. (ii) $|D_Q|\\le c_Qq^{3/2}$ with $c_Q=0.79246$, and $|D_Q-D_3|\\le c'_Qq^2$ with $c'_Q=0.36916$. "
    "*Evidence:* DYAD-ART-LPHASE-ROWA gates P-a1, P-a2 (certified exact values $0.7924576152\\ldots$, $0.3691523046\\ldots$; "
    "DYAD-ART-INBOX-20261030 check O6).")

COR902 = (
    "`[COR]` `[v6.4.23]` The decimals of the proof outline above are outward ceilings: $c'_Q=0.36916$ (the certified majorant is "
    "$0.3691523\\ldots$), $1.51633$, $1.06253$ and $1.61115$ replace displays that were nearest-rounded and below the quantities "
    "they bound ($0.36915$, $1.51632$, $1.06252$, $1.61112$). The certificate works with exact rationals; its FIN value is "
    "$1.6111210\\ldots$, and $\\tfrac{403}{250}$ is unchanged (" + CHAIN + "; DYAD-ART-INBOX-20261030 check O7).")

EDITS = [
# ---- ED ----
("ED-1", "title", "# RTG_DYADIC_OSCILLATOR_DSN_v6.4.22\n", "# RTG_DYADIC_OSCILLATOR_DSN_v6.4.23\n"),
("ED-2", "header date", "**Date:** 23 October 2026  \n", "**Date:** 30 October 2026  \n"),
("ED-3", "header status",
 "**Document status:** ADOPTED — PI, 23 October 2026 (owner errata: current-state wording, owner labels for RECOG R11 and OPEN-M R11, three wordings, second-route $h_4$ evidence). Adoption record: `records/dyad/RTG_DYADIC_v6_4_22_RELEASE_RECORD.md`.",
 "**Document status:** DRAFT — v6.4.23 candidate (inbox round D1–D7: OPEN 18 step-indexed successor RID, two registrations for RECOG, displayed-decimal corrections, consumer register); not adopted."),
("ED-4", "header supersedes",
 "**Supersedes:** `RTG_DYADIC_OSCILLATOR_DSN_v6.4.21` (SHA-256 `a412f34d4db6a6fa92705a5c33334127b3efc3a30a903fecb3c91bd0cf1cdc7d`; tag `dyad-v6.4.21`).",
 "**Supersedes:** `RTG_DYADIC_OSCILLATOR_DSN_v6.4.22` (SHA-256 `2363ca409c08bc571378125771f27239b6426d3e7cdbe75e0306a2a728778c29`; tag `dyad-v6.4.22`)."),
("ED-5", "header release record",
 "**Release record:** `records/dyad/RTG_DYADIC_v6_4_22_RELEASE_RECORD.md`. Version history: Appendix A.",
 "**Release record:** `" + REC + "`. Version history: Appendix A."),
("ED-6", "Appendix G note",
 "v6.4.21 and v6.4.22 keep every heading anchor of v6.4.20.", "v6.4.21 to v6.4.23 keep every heading anchor of v6.4.20."),
("ED-7", "footer",
 "*END OF DOCUMENT — RTG_DYADIC_OSCILLATOR_DSN_v6.4.22 (ADOPTED, 23 October 2026).*",
 "*END OF DOCUMENT — RTG_DYADIC_OSCILLATOR_DSN_v6.4.23 (DRAFT candidate, 30 October 2026).*"),
("ED-8", "Appendix A entry",
 "### v6.4.22 — 23 October 2026 — Adopted\n",
 "### v6.4.23 — 30 October 2026 — Draft candidate\n\n"
 "- **OPEN 18 [scope] (D1):** successor `DYAD-THM-OPEN18-STEP-MONOTONE` (step-indexed monotonicity; $q_{3/4}$ isolated in $G$); `DYAD-THM-OPEN18` keeps its text and grade with a historical-formulation `[scope:]` note; summary lines cite the successor (§1, §2, §6.8, §8, Appendix E). NUMGEN's $q_*$ is a different number.\n"
 "- **Registrations (D2, D3):** `DYAD-THM-NF-REM-C7-SHARP` ($C_7\\le85.1$ / $27.7$) and `DYAD-THM-LPHASE-ROWA-BRIDGE` ($c_Q=0.79246$, $c'_Q=0.36916$), §6.14.\n"
 "- **[COR] displayed decimals:** NF-REM table certificate values; L-PHASE proof outline $0.36915/1.51632/1.06252/1.61112\\to0.36916/1.51633/1.06253/1.61115$; $\\tfrac{403}{250}$ and all adopted constants unchanged.\n"
 "- **Consumer register (D4–D7):** §7.0, §7 and the NUMGEN import state in §6.14 and §7.0a to NUMGEN v1.21, RECOG v0.3.26, OFN v0.12, Genesis v2.9, Programme v1.3, Methodology v1.4; receipts N4/N6/N14 (OFN), N15 (NUMGEN).\n"
 "- No existing RID, grade or OPEN status changed; three result RIDs and one artifact RID (DYAD-ART-INBOX-20261030) added. Evidence: " + OWN + ", " + CHAIN + " (DYAD-ART-INBOX-20261030). Reconciliation " + RECON + "; release record `" + REC + "`; predecessor tag `dyad-v6.4.22`.\n\n"
 "### v6.4.22 — 23 October 2026 — Adopted\n"),
# ---- D1 ----
("D1-a", "status summary", "local quintic normalization pipeline, OPEN 11, OPEN 18);",
 "local quintic normalization pipeline, OPEN 11, OPEN 18 in its step-indexed form `DYAD-THM-OPEN18-STEP-MONOTONE`);"),
("D1-b", "§1 OPEN 18 line",
 "`[THM-ALG via IA]` **OPEN 18 closed.** First-footprint branch monotonicity: $dQ/dq>0$ and $d\\Theta/dq<0$ on both branches; $q=q_*$ is the branch split. `DYAD-THM-OPEN18`",
 "`[THM-ALG via IA]` **OPEN 18 closed (step-indexed).** On the canonical family $(0,q)$: $dQ_3/dq>0$, $d\\Theta_3/dq<0$ on $(0,q_{3/4}]$ and $dQ_4/dq>0$, $d\\Theta_4/dq<0$ on $[q_{3/4},2]$; $q_{3/4}\\approx1.2602142026$ is the zero of $\\rho_4$ in the certificate gap. `DYAD-THM-OPEN18-STEP-MONOTONE`; the historical first-footprint formulation `DYAD-THM-OPEN18` is kept with a scope note (§6.8)"),
("D1-c", "§2 closed-OPEN line",
 "- **OPEN 18** `DYAD-THM-OPEN18` :: `[THM-ALG via IA]` ✓ CLOSED — first-footprint branch monotonicity.",
 "- **OPEN 18** `DYAD-THM-OPEN18-STEP-MONOTONE` :: `[THM-ALG via IA]` ✓ CLOSED — step-indexed monotonicity on the canonical family; the historical first-footprint formulation `DYAD-THM-OPEN18` keeps its grade with a scope note (§6.8)."),
("D1-d", "§6.8 old entry + successor",
 "$q=q_*$ is the branch split. Certificate: `open18_arb_cert_final.cpp`.\n",
 "$q=q_*$ is the branch split. Certificate: `open18_arb_cert_final.cpp`." + OLD18_NOTE + "\n\n" + SUCC + "\n"),
("D1-e", "§8 DYAD-ART-OPEN18",
 "- [RID: DYAD-ART-OPEN18] :: `open18_arb_cert_final.cpp` :: FLINT/Arb certificate for OPEN 18 footprint monotonicity :: `[THM-ALG via IA]` ✓",
 "- [RID: DYAD-ART-OPEN18] :: `open18_arb_cert_final.cpp` (recovered as `upload/dyad-sources/rtg-engine/open18_arb_cert3.cpp`, identified by its first line; SHA-256 `" + OPEN18_SHA + "`, PI-supplied) :: FLINT/Arb certificate of the step-3 and step-4 derivative signs on the canonical family (sweeps outside the gap $G$) :: `[THM-ALG via IA]` ✓ :: Atlas rerun and owner rerun (g++ 13, FLINT 3.0.1), byte-identical output\n"
 "- [RID: DYAD-ART-INBOX-20261030] `[v6.4.23]` :: " + OWN + " (SHA-256 `21aec87c555b8b68e0ea2e84833b13fae0f1a1a63f3b1c66959805e2791649e1`) and " + CHAIN + " (`aac9996fed172a0784244a1233b0f0b946a6440afb1329a00c09f6f34e477553`); outputs `evidence/dyad/inbox-20261030/` :: O1–O3 (OPEN 18 isolation and gap closure, python-flint 256-bit), O5 ($C_7$ bounds), O6–O7 (row-A constants, FIN with the published ceilings), L1–L3 (displayed chain); controls A–D exit 1 :: evidence for DYAD-THM-OPEN18-STEP-MONOTONE, DYAD-THM-NF-REM-C7-SHARP and DYAD-THM-LPHASE-ROWA-BRIDGE at statement and constant level; OWNER-RUN"),
("D1-f", "Appendix E.1 OPEN18 row",
 "| `DYAD-THM-OPEN18` | THM-ALG via IA | as stated at the entry | §6.8 | `open18_arb_cert_final.cpp` (DYAD-ART-OPEN18) | not recorded | FLINT/Arb (C++) | first footprint, both branches |",
 "| `DYAD-THM-OPEN18` | THM-ALG via IA | historical first-footprint formulation (scope note at the entry) | §6.8 | `open18_arb_cert_final.cpp` (DYAD-ART-OPEN18) | `" + OPEN18_SHA[:8] + "…" + OPEN18_SHA[-4:] + "` (recovered, PI-supplied) | FLINT/Arb (C++) | footprint predicate and branch legality: evidence obligation open |\n"
 "| `DYAD-THM-OPEN18-STEP-MONOTONE` | THM-ALG via IA — new in v6.4.23 | step-indexed; canonical family | §6.8 | DYAD-ART-OPEN18 and DYAD-ART-INBOX-20261030 (O1, O3) | `" + OPEN18_SHA[:8] + "…" + OPEN18_SHA[-4:] + "`; `21aec87c…49e1` | FLINT/Arb (C++); python-flint | $n=3$ on $(0,\\sup G]$, $n=4$ on $[\\inf G,2]$; zero of $\\rho_4$ unique in $G$ |"),
("D1-g", "Appendix E.2 OPEN18 row",
 "| `DYAD-THM-OPEN18` | historical | not recorded | not recorded | not recorded | — |",
 "| `DYAD-THM-OPEN18` | historical; certificate rerun 30 Oct 2026 (Atlas, owner) | not recorded | not recorded | not recorded | footprint audits not recovered |\n"
 "| `DYAD-THM-OPEN18-STEP-MONOTONE` | v6.4.23 (C++ rerun; O1, O3) | not recorded | not recorded | co-owner mpmath sanity check of $q_{3/4}$ (not an interval certificate) | micro-strip MVT step and box logic not re-audited |"),
# ---- D2 ----
("D2-a", "NF-REM table row 1/20",
 "| $\\tfrac1{20}$ | $C_7=100$ (certificate value $85.07$) | $C_D=1000$ (certificate value $812.89$) |",
 "| $\\tfrac1{20}$ | $C_7=100$ (certified bound $85.0732$, rounded up) | $C_D=1000$ (certified bound $812.894$, rounded up) |"),
("D2-b", "NF-REM table row 1/40",
 "| $\\tfrac1{40}$ | $C_7=30$ (certificate value $27.60$) | $C_D=250$ (certificate value $216.77$) |",
 "| $\\tfrac1{40}$ | $C_7=30$ (certified bound $27.6023$, rounded up) | $C_D=250$ (certified bound $216.77$, rounded up) |"),
("D2-c", "new RID after NF-REM",
 "Constants travel with their radius and this chart; profiles are not to be mixed.",
 "`[COR]` `[v6.4.23]` The bracketed values in the table are the certificate's exact upper bounds rounded up; the earlier displays $85.07$, $27.60$ and $812.89$ were nearest-rounded and below the bounds ($216.77$ was already an outward value). Constants travel with their radius and this chart; profiles are not to be mixed."),
("D2-d", "insert C7-SHARP before NF6-DEG10",
 "`[ALG]` [RID: DYAD-ALG-NF6-DEG10] `[v6.4.11]`",
 C7SHARP + "\n\n`[ALG]` [RID: DYAD-ALG-NF6-DEG10] `[v6.4.11]`"),
("D2-e", "Appendix E.1 NF-REM row",
 "| `DYAD-THM-NF-REM` | THM | as stated at the entry | §6.14 | as DYAD-THM-PRIM-CTR | v6.4.10 manifest | exact rational | rows $1/20$, $1/40$ (not mixed) |",
 "| `DYAD-THM-NF-REM` | THM | as stated at the entry | §6.14 | as DYAD-THM-PRIM-CTR | v6.4.10 manifest | exact rational | rows $1/20$, $1/40$ (not mixed) |\n"
 "| `DYAD-THM-NF-REM-C7-SHARP` | THM — new in v6.4.23 | chart and norm of DYAD-THM-NF-REM; rows not mixed | §6.14 | DYAD-ART-RE-P2B2 `certificate.json`; DYAD-ART-INBOX-20261030 (O5) | `e4e2bab0…dbe4` | exact rational | $C_7$ rows only |"),
("D2-f", "Appendix E.2 NF-REM row",
 "| `DYAD-THM-NF-REM` | v6.4.10 | v6.4.10 independent reconstruction | not recorded | yes (referee) | higher derivatives not bounded |",
 "| `DYAD-THM-NF-REM` | v6.4.10 | v6.4.10 independent reconstruction | not recorded | yes (referee) | higher derivatives not bounded |\n"
 "| `DYAD-THM-NF-REM-C7-SHARP` | v6.4.23 (O5; P2-B v2 package rerun by the Atlas, byte-identical) | not recorded | not recorded | — | $C_D$ not sharpened |"),
# ---- D3 ----
("D3-a", "L902 c'_Q", "$c'_Q=0.36915$, from the exact polynomial", "$c'_Q=0.36916$, from the exact polynomial"),
("D3-b", "L902 inner constant", "$|r|\\le1.51632\\,q^{3/2}$", "$|r|\\le1.51633\\,q^{3/2}$"),
("D3-c", "L902 bridge factor", "factor $\\le1.06252$", "factor $\\le1.06253$"),
("D3-d", "L902 product", "$|r_m|\\le1.61112\\,Q_m^{3/2}$", "$|r_m|\\le1.61115\\,Q_m^{3/2}$"),
("D3-e", "COR line + BRIDGE RID before Recorded distinctions",
 "\n`[DEF]` `[v6.4.19]` **Recorded distinctions.**",
 "\n" + COR902 + "\n\n" + BRIDGE + "\n\n`[DEF]` `[v6.4.19]` **Recorded distinctions.**"),
("D3-f", "§2 table certificate value",
 "the constant is the ceiling of a majorant (certificate value $1.61112$;",
 "the constant is the ceiling of a majorant (certificate value $1.6111210\\ldots$;"),
("D3-g", "§7.0a upper bound bullet",
 "(the ceiling of a majorant, certificate value $1.61112$)",
 "(the ceiling of a majorant, certificate value $1.6111210\\ldots$)"),
("D3-h", "Appendix E.1 LPHASE row: insert BRIDGE before REMAINDER",
 "| `DYAD-THM-LPHASE-ROWA-REMAINDER` | THM | scope:",
 "| `DYAD-THM-LPHASE-ROWA-BRIDGE` | THM (part (i) ALG) — new in v6.4.23 | row-A disk of the NF-INV chart; block base points in $U$; (B) on $U_T$ | §6.14 | `dyad_numgen_lphase_rowA_cert.py` (DYAD-ART-LPHASE-ROWA) gates P-a1, P-a2; DYAD-ART-INBOX-20261030 (O6) | `117484ae…9cdb` | exact rational | two chart bounds and the decomposition |\n"
 "| `DYAD-THM-LPHASE-ROWA-REMAINDER` | THM | scope:"),
("D3-i", "Appendix E.2 LPHASE row: insert BRIDGE before REMAINDER",
 "| `DYAD-THM-LPHASE-ROWA-REMAINDER` | combined checker",
 "| `DYAD-THM-LPHASE-ROWA-BRIDGE` | v6.4.23 (O6 executes the certificate unchanged) | NUMGEN receipt replay of the certificate (v1.20.8 review package) | not recorded | co-owner exact check of the FIN chain with the published ceilings | — |\n"
 "| `DYAD-THM-LPHASE-ROWA-REMAINDER` | combined checker"),
# ---- D4-D7: §7.0 ----
("R-1", "§7.0 Dyadic row",
 "| Dyadic (this ledger) | v6.4.22 | this edition; status in the header; its SHA-256 is in its release record | predecessor v6.4.21: `a412f34d4db6a6fa92705a5c33334127b3efc3a30a903fecb3c91bd0cf1cdc7d` | tag `dyad-v6.4.21`; release records in `records/dyad/` |",
 "| Dyadic (this ledger) | v6.4.23 | this edition; status in the header; its SHA-256 is in its release record | predecessor v6.4.22: `2363ca409c08bc571378125771f27239b6426d3e7cdbe75e0306a2a728778c29` | tag `dyad-v6.4.22`; release records in `records/dyad/` |"),
("R-2", "§7.0 RECOG current row",
 "| RECOG | v0.3.22 | ADOPTED 20 Oct 2026 (current) | `0dcce9e44d48fbedbcd5af083283fce12560cc17a3951a7632ff0e50db44bcd9` | project copy hashed by DYAD; RECOG release record | claim-level imports (§7); consumer of §6.14 |",
 "| RECOG | v0.3.26 | ADOPTED 28 Oct 2026 (current) | `45e307f8333c81a344158ada07ad34a1a3afab6e1b93b2aa04ee09f84878dd34` | tag `recog-v0.3.26`; RECOG release record | consumer of §6.14 (NF6, NF-REM, NF-INV, PRIM-CTR; LPHASE (D5) constants under `[assuming:]`) |\n"
 "| RECOG | v0.3.22 | ADOPTED 20 Oct 2026 | `0dcce9e44d48fbedbcd5af083283fce12560cc17a3951a7632ff0e50db44bcd9` | project copy hashed by DYAD; RECOG release record | pin of the claim-level imports (§7) |"),
("R-3", "§7.0 NUMGEN row",
 "| Number Genesis (NUMGEN) | v1.20.8 | ADOPTED 21 Oct 2026 | `835a56f82b2641343a0e2fa116b049a167c62efd4d13fe41236966c117f4817e` | project copy hashed by DYAD | L-PHASE interface (I1–I5); notice receipts N3, N10–N15 |",
 "| Number Genesis (NUMGEN) | v1.21 | ADOPTED 26 Oct 2026 | `4805760d683bb3abddfdaab4737f6bb75beed392906bd4c54d8ae79245f15701` | tag `numgen-v1.21`; NUMGEN release record | imports DYAD-THM-LPHASE-ROWA-REMAINDER (§6.6, §9.1, at `dyad-v6.4.22`); L-PHASE interface (I1–I5, confirmed with v1.20.8); notice receipts |"),
("R-4", "§7.0 OFN row",
 "| Ontological Foundations (OFN) | v0.10 | ADOPTED 19 Oct 2026 | `acb70a8cfc7962abcc047dedffb59e9ceca8f2e9843d6203df6eba54f5ed5dfa` | OFN release record | imports IMP-O10-03/04/05; N9 answered (N-O10-1) |",
 "| Ontological Foundations (OFN) | v0.12 | ADOPTED 30 Oct 2026 | `55ff8ba85d4bb48b52266bdd9a44aa84efcd2cc19903d059266fa406a6bb76aa` | tag `ofn-v0.12`; OFN release record | imports IMP-O08-12, IMP-O08-20, IMP-O10-03/04/05, IMP-O10-06/07; receipts N4, N6, N14; N9 answered |"),
("R-5", "§7.0 Genesis row",
 "| Genesis Geometry | v2.8.9 | ADOPTED 19 Oct 2026 | `d143673e9596abc900f54f269582299c87c9146504d6c9e1fd08ac294ba8c6fc` | Genesis release record; OFN-computed | consumer; live Dyadic pins remain v6.4.13 (repin to v6.4.14+ deferred, R-1); no new Dyadic RID imported |",
 "| Genesis Geometry | v2.9 | ADOPTED 25 Oct 2026 | `9178ca2cd38bea8d55deada78b6adbd8022533c4baad7af101583b1179d300ac` | tag `gen-v2.9`; Genesis release record | consumer; scoped import of DYAD-THM-SMOOTH-EMBEDDING and DYAD-THM-SMOOTH-EQUIVARIANT-CHART at `dyad-v6.4.22` (§6.3c G-20 note); its other Dyadic pins remain v6.4.13 |"),
("R-6", "§7.0 Programme row",
 "| Programme Overview | v1.2 | ADOPTED | not recorded in this ledger | — | SG-PROG-1–4; `RTG-OPEN-GENERATOR-SELECTION` |",
 "| Programme Overview | v1.3 | ADOPTED | `1b8358b3e1d3abb853e226786d21e6559c289b7c85570dac0ff1ebc2dabaea06` | tag `programme-v1.3` | SG-PROG-1–4; `RTG-OPEN-GENERATOR-SELECTION` |"),
("R-7", "§7.0 Methodology row",
 "| DSN Methodology | v1.3 | ADOPTED | not recorded in this ledger | — | tag grammar, lifecycle |",
 "| DSN Methodology | v1.4 | ADOPTED | `cdacab5feb79161cd86313086065ca67313ef354e30ceaf205386cf2f3a0f2df` | tag `methodology-v1.4` | tag grammar, lifecycle |"),
# ---- §7 context and consumer lines ----
("R-8", "§7 Programme context", "- `RTG_PROGRAMME_OVERVIEW_v1.2` — SG-PROG-1", "- `RTG_PROGRAMME_OVERVIEW_v1.3` — SG-PROG-1"),
("R-9", "§7 OFN context",
 "- `RTG_ONTOLOGICAL_FOUNDATIONS_v0.10` — motivational layer for the generator choice; does not derive $T$. OFN imports `DYAD-THM-PRIM-CTR` (IMP-O08-20), `DYAD-THM-FORMAL-Z6-GENERATOR` (IMP-O10-03), Lemma F / F3 (IMP-O10-04) and the OPEN 3 records (IMP-O10-05); CUST-O09-01 is answered by `DYAD-DEF-PRIMITIVE-MAP`.",
 "- `RTG_ONTOLOGICAL_FOUNDATIONS_v0.12` — motivational layer for the generator choice; does not derive $T$. OFN imports `DYAD-THM-PRIM-CTR` (IMP-O08-20), `DYAD-DEF-PRIMITIVE-MAP` (IMP-O08-12), `DYAD-THM-FORMAL-Z6-GENERATOR` (IMP-O10-03), Lemma F / F3 (IMP-O10-04), the OPEN 3 records (IMP-O10-05), `DYAD-THM-SMOOTH-EMBEDDING` (IMP-O10-06) and `DYAD-THM-SMOOTH-EQUIVARIANT-CHART` (IMP-O10-07); CUST-O09-01 is answered by `DYAD-DEF-PRIMITIVE-MAP`. OFN v0.12 uses the exact raw-map identity $T(-x)+T(x)=(0,2(\\cosh\\rho-1))$ (OPEN-OFN-3B frame); it follows directly from `DYAD-DEF-PRIMITIVE-MAP`."),
("R-10", "§7 RECOG context",
 "- `RTG_RELATIONAL_RECOGNITION_DSN` — v0.3.22 (adopted) for claim-level imports;",
 "- `RTG_RELATIONAL_RECOGNITION_DSN` — v0.3.22 (adopted) for the claim-level import pins (current edition v0.3.26, §7.0);"),
("R-11", "§7 Genesis export",
 "- `RTG_GENESIS_GEOMETRY_DSN` (v2.8.9, adopted 19 Oct 2026) —",
 "- `RTG_GENESIS_GEOMETRY_DSN` (v2.9, adopted 25 Oct 2026) —"),
("R-12", "§7 Genesis export tail",
 "Genesis pins Dyadic v6.4.13; its repin to a later edition is deferred (R-1). v2.8.9 imports no new Dyadic RID.",
 "Genesis pins Dyadic v6.4.13 for these rows; its repin is deferred (R-1). v2.9 adds a scoped import of `DYAD-THM-SMOOTH-EMBEDDING` and `DYAD-THM-SMOOTH-EQUIVARIANT-CHART` at `dyad-v6.4.22` for its §6.3c G-20 note only."),
("R-13", "§7 RECOG consumer",
 "acceptance recorded from v0.3.2 and retained through v0.3.22.",
 "acceptance recorded from v0.3.2 and retained through v0.3.26; v0.3.26 also carries the NF-REM certificate values and the (D5) row-A constants of `DYAD-THM-LPHASE-ROWA-REMAINDER` under `[assuming:]` (registered here as `DYAD-THM-NF-REM-C7-SHARP` and `DYAD-THM-LPHASE-ROWA-BRIDGE`; whether RECOG drops the qualifier is RECOG's decision, after its re-check with $c'_Q=0.36916$)."),
("R-14", "§7 NUMGEN consumer",
 "`DYAD-THM-PRIM-CTR` (seed admitted to the tube) and `DYAD-THM-Q403-PHASELAW`; v1.20.8 (adopted 21 Oct 2026).",
 "`DYAD-THM-PRIM-CTR` (seed admitted to the tube), `DYAD-THM-Q403-PHASELAW` and `DYAD-THM-LPHASE-ROWA-REMAINDER` (adopted use at §6.6, §9.1, pin `dyad-v6.4.22`); v1.21 (adopted 26 Oct 2026); `DYAD-ALG-P5-RADIAL` recorded by NUMGEN as the owner name of its $\\Delta Q_5$."),
("R-15", "§7 NUMGEN offered import",
 "- **Offered import: `RTG_NUMBER_GENESIS_DSN`** — `DYAD-THM-LPHASE-ROWA-REMAINDER` (`[THM]`): constant and branch certificate for NUMGEN L-PHASE on row A. NUMGEN v1.20.8 records N15 RECEIVED and defers the import to a later edition (OPEN sub-item \"L-PHASE explicit constant\"). No coefficient transfer (SG-19).",
 "- **NUMGEN L-PHASE import:** `DYAD-THM-LPHASE-ROWA-REMAINDER` (`[THM]`), constant and branch certificate on row A, imported by NUMGEN v1.21 (N15: received, statement accepted, adopted use). No coefficient transfer (SG-19)."),
# ---- notice-receipt rows ----
("E1-a", "§6.14 distinctions (iii) ownership",
 "NUMGEN v1.20.8 keeps an `[OPEN]` sub-item without a value; a later NUMGEN edition may import this RID after DYAD adoption.",
 "NUMGEN v1.21 imports this RID (§6.6, §9.1, at `dyad-v6.4.22`); the NUMGEN v1.20.8 `[OPEN]` sub-item without a value is closed there."),
("E1-b", "§6.14 not-established boundary",
 "whose import NUMGEN defers (§7 L-PHASE interface)",
 "imported by NUMGEN v1.21 (§7 L-PHASE interface)"),
("E1-c", "§7.0a GAP-LOCK bullet",
 "its only input is the explicit row-A constant above, whose import NUMGEN has deferred.",
 "its only input is the explicit row-A constant above, which NUMGEN v1.21 imports."),
("N-4", "notice row N4 OFN",
 "| N4 | v6.4.11 | OFN | CUST-O09-01 answered by DYAD-DEF-PRIMITIVE-MAP | INFORMATIONAL — no OFN receipt recorded | OFN v0.10 §12.3 retains the inherited v0.9 CUST-O09-01 paragraph |",
 "| N4 | v6.4.11 | OFN | CUST-O09-01 answered by DYAD-DEF-PRIMITIVE-MAP | RECEIVED — used (IMP-O08-12) | OFN v0.12 IMP-O08-12, §12.3 |"),
("N-6", "notice row N6 OFN",
 "| N6 | v6.4.12 | OFN | same | INFORMATIONAL — no OFN receipt recorded | — |",
 "| N6 | v6.4.12 | OFN | same | RECEIVED — no OFN import | OFN v0.12 §12.3 |"),
("N-14", "notice row N14 OFN",
 "| N14 | v6.4.18 | OFN | same | NOT RECORDED | OFN v0.10 (19 Oct) predates v6.4.18 |",
 "| N14 | v6.4.18 | OFN | same | RECEIVED — used (IMP-O10-06/07) | OFN v0.12 IMP-O10-06, §12.3 |"),
("N-15", "notice row N15 NUMGEN",
 "| N15 | v6.4.19 | NUMGEN | L-PHASE row A: DYAD-THM-LPHASE-ROWA-REMAINDER | RECEIVED — import deferred | NUMGEN v1.20.8 §6.6 OPEN sub-item, §9.1 |",
 "| N15 | v6.4.19 | NUMGEN | L-PHASE row A: DYAD-THM-LPHASE-ROWA-REMAINDER | RECEIVED — statement accepted; adopted use | NUMGEN v1.21 §6.6, §9.1 (import row at `dyad-v6.4.22`) |"),
]


def main():
    base, out, logp = sys.argv[1:4]
    raw = open(base, 'rb').read()
    assert hashlib.sha256(raw).hexdigest() == BASE_SHA, 'base is not dyad-v6.4.22'
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
