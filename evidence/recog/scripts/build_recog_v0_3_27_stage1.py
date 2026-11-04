#!/usr/bin/env python3
"""RECOG v0.3.27, stage 1: maintenance intermediate (a build stage, not an edition) -- the inbox round after v0.3.26.

Basis: the two-co-owner reconciliation of 3 Nov 2026 (PR #172 proposal, PR #173 reply, ChatGPT acceptance record), on the Atlas
advisory and owner entry note of PR #168 and the independent dispositions of PR #169 / PR #170. Applies, to the adopted v0.3.26 file
(tag recog-v0.3.26), separately marked groups:
  R1    c'_Q = 0.36916 (DYAD-THM-LPHASE-ROWA-BRIDGE, dyad-v6.4.23): part-1b literal changed, the A1c chain and the corrected grid rerun
        by the owner; the §8 rows of the four affected artifacts re-registered (hashes computed from the working tree at build time).
        The five text sites carry the value through D5B or D5A (exactly one of them is built with R1).
  D5B   R2 option (b): the (D5) qualifier discharged at the five A1c sites -- imports DYAD-THM-LPHASE-ROWA-BRIDGE (exact decomposition,
        c_Q, c'_Q) and DYAD-THM-OPEN3-SPIRAL-REM (K_Theta), and the new source-independent RECOG-ALG-A1C-JET-REMAINDER-BOUNDS
        (c_J <= 0.500819, c_7 <= 100.231 on q <= q*, from DYAD-ALG-NF6 and DYAD-THM-NF-REM only) with its artifact row; §1, §2 R6,
        §7 rows; COMBINED-TAIL cites the lemma and the bridge theorem.
  D5A   R2 fallback (a): the same imports, the qualifier narrowed to c_J = 0.50220, c_7 = 157.58 (Dyadic proof-outline constants).
  C7    R3: RECOG-THM-R9-SHARPENED-ROWS-C7 imports DYAD-THM-NF-REM-C7-SHARP instead of assuming the ceilings; L663, L771, §7.
  DISP  item 7: eight displays printed in the safe direction (ceilings outward, the B1 window inward), each with a [COR] note.
  PIN   R6 (+R5 receipt): live current-use Dyadic citations repinned to dyad-v6.4.23 and NUMGEN to numgen-v1.21 (claim audit
        v0.3.27); GAP-LOCK Lemma 3 by RID with its two consumption grades; companion pins (Genesis gen-v2.10, OFN ofn-v0.12,
        TDR-G v2.12.14 reference only); provenance and historical-audit pins kept.
Rules (as v0.3.26 stage 1): assertion-gated edits (exact-once), Appendix A masked for live edits, modes str / line / sub (sub: a set of
exact-count substitutions inside one line found by a unique prefix), header identity lines, status summary and footer untouched.
Decoupling: R1 requires exactly one of D5B, D5A; every other group builds alone.

usage: build_recog_v0_3_27_stage1.py BASE OUT EDITLOG_JSON [--only R1,D5B,C7,DISP,PIN]
  BASE = `git show recog-v0.3.26:dsn/RTG_RELATIONAL_RECOGNITION_DSN.md`; run from the repository root (R1 reads file hashes)
"""
import hashlib, json, os, subprocess, sys

BASE_SHA = "45e307f8333c81a344158ada07ad34a1a3afab6e1b93b2aa04ee09f84878dd34"
APPA_START = "## Appendix A — Version History"
APPA_END = "## Appendix B —"
PREV_TAG = "recog-v0.3.26"
GROUPS = ["R1", "D5B", "D5A", "C7", "DISP", "PIN"]
DY = "RTG_DYADIC_OSCILLATOR_DSN_v6.4.23"

# ----------------------------------------------------------------------------- R2 texts ---------------------------------------------------------------
Q_OLD = r"`[assuming: Dyadic row-A bridge constants $c_Q=0.79246$, $c'_Q=0.36915$ ($|D_Q|\le c_Qq^{3/2}$, $|D_Q-D_3|\le c'_Qq^2$) and the remainder decomposition $r=\Lambda_3+{\rm rest}$ with its constants, as published in the proof of DYAD-THM-LPHASE-ROWA-REMAINDER (certified by DYAD-ART-LPHASE-ROWA); proof constants, not theorem rows; registration requested (§7)]`"
IMP = r"[import: " + DY + r" §6.14 | DYAD-THM-LPHASE-ROWA-BRIDGE, DYAD-THM-OPEN3-SPIRAL-REM]"
BR = (r"(row-A bridge and remainder constants: the exact decomposition $r=\Lambda_3+[S_\Theta-L_\Theta]+\tau[D_Q-D_3]+[\operatorname{Arg}(J/z)+\tau q]+\operatorname{Arg}(\widehat F/J)$"
      r" under branch (B), $|D_Q|\le c_Qq^{3/2}$, $|D_Q-D_3|\le c'_Qq^2$ with $c_Q=0.79246$, $c'_Q=0.36916$ (`[COR]` v0.3.27: copied before as $0.36915$, a nearest-rounded display"
      r" below the certified majorant $0.3691523\ldots$), $K_\Theta=\tfrac{123}{125}$ on $|z|\le\tfrac1{20}$")
Q_NEW_B = IMP + " " + BR + r"; $c_J\le0.50220$, $c_7\le157.58$ on $q\le q^*$ by RECOG-ALG-A1C-JET-REMAINDER-BOUNDS; the former (D5) qualifier is discharged, v0.3.27)"
Q_NEW_A = IMP + " " + BR + r"; v0.3.27)" + r" `[assuming: $c_J=0.50220$ and $c_7=157.58$ ($|\operatorname{Arg}(J/z)+\tau q|\le c_Jq^2$, $|\operatorname{Arg}(\widehat F/J)|\le c_7q^3$), as published in the proof outline of DYAD-THM-LPHASE-ROWA-REMAINDER (" + DY + r" §6.14); proof-outline constants without a theorem row]`"
QS_OLD = r"`[assuming: the Dyadic (D5) row-A bridge proof constants, as RECOG-THM-A1C-SHARPENED-SCHEDULE]`"
QS_NEW_B = IMP + r" (the row-A remainder constants as RECOG-THM-A1C-SHARPENED-SCHEDULE, with RECOG-ALG-A1C-JET-REMAINDER-BOUNDS; the former (D5) qualifier is discharged, v0.3.27)"
QS_NEW_A = IMP + r" (as RECOG-THM-A1C-SHARPENED-SCHEDULE, v0.3.27) `[assuming: $c_J=0.50220$, $c_7=157.58$, as RECOG-THM-A1C-SHARPENED-SCHEDULE]`"
DEP_B = r"DYAD-THM-LPHASE-ROWA-BRIDGE, DYAD-THM-OPEN3-SPIRAL-REM and RECOG-ALG-A1C-JET-REMAINDER-BOUNDS (the row-A remainder constants; v0.3.27)"
DEP_A = r"DYAD-THM-LPHASE-ROWA-BRIDGE, DYAD-THM-OPEN3-SPIRAL-REM (v0.3.27) and the listed assumption ($c_J$, $c_7$)"
JET_BLOCK = (r"`[ALG]` [RID: RECOG-ALG-A1C-JET-REMAINDER-BOUNDS] [scope: chart of DYAD-ALG-NF6 and DYAD-THM-NF-REM, $0<q=|z|^2\le q^*=\tfrac{256}{140625}$ ($<\tfrac1{400}$: row A); adopted rows only, no RECOG A1c result]"
             r" [proof: certificate RECOG-ART-A1C-JET-REMAINDER-BOUNDS (exact rationals, interval check); the majorants are those computed for RECOG-ALG-A1C-COMBINED-TAIL (v0.3.25), stated source-independently in v0.3.27 (co-owner reconciliation of 3 Nov 2026)]"
             r" **Jet and seventh-order remainder bounds.** With $J(z)/z=1+u$, $u=\mu q+(a_{32}+a_{05}e^{-6i\Theta})q^2$, $\bar u=|\mu|q+A_5q^2$, $A_5=|a_{32}|+|a_{05}|$ (DYAD-ALG-NF6; $\operatorname{Im}\mu=-\tau$):"
             r" $|\operatorname{Arg}(J/z)+\tau q|\le c_J(q)\,q^2$, $c_J(q)=\tfrac{89\sqrt3}{324}+|a_{05}|+|\mu|A_5q+\tfrac12A_5^2q^2+\bar u^3/(3(1-\bar u)q^2)$ ($\tfrac{89\sqrt3}{324}=\operatorname{Im}a_{32}-\tfrac12\operatorname{Im}\mu^2$; the logarithm series),"
             r" and $|\operatorname{Arg}(\widehat F/J)|\le c_7(q)\,q^3$, $c_7(q)=C_7/((1-\bar u)(1-w))$, $w=C_7q^3/(1-\bar u)$, $C_7=100$ (DYAD-THM-NF-REM, $|z|\le\tfrac1{20}$)."
             r" Both majorants increase with $q$, so on $q\le q^*$: $c_J\le0.500819$ and $c_7\le100.231$. Hence the two remainder constants of the proof outline of DYAD-THM-LPHASE-ROWA-REMAINDER that RECOG's closed forms use,"
             r" $c_J=0.50220$ and $c_7=157.58$, are valid ceilings on RECOG's domain. Depends on: DYAD-ALG-NF6 ($\mu$, $a_{32}$, $a_{05}$); DYAD-THM-NF-REM ($C_7=100$)."
             "\n" r"**Not supplied:** the smaller $c_7$ that $C_7\le85.1$ (DYAD-THM-NF-REM-C7-SHARP) would give; any bound outside $q\le q^*$." "\n\n")
LPH_OLD = r"§6.13b A1c sharpened schedule and §6.16e decoder (v0.3.25): the proof constants $c_Q=0.79246$, $c'_Q=0.36915$ of the row-A bridge ($|D_Q|\le c_Qq^{3/2}$, $|D_Q-D_3|\le c'_Qq^2$) and the decomposition $r=\Lambda_3+{\rm rest}$ of the owner's proof (certified by DYAD-ART-LPHASE-ROWA) are used under `[assuming:]` — proof constants, not theorem rows; registration as owner statements requested; the exact decomposition of $r$ under branch (B) is used in RECOG-ALG-A1C-COMBINED-TAIL"
LPH_COMMON = r"§6.13b A1c sharpened schedule and §6.16e decoder (v0.3.25): the row-A bridge constants and the exact decomposition of $r$ are imported from DYAD-THM-LPHASE-ROWA-BRIDGE since v0.3.27 (row below; `[COR]` $c'_Q=0.36916$, the earlier copy $0.36915$ being a nearest-rounded display below the certified majorant $0.3691523\ldots$; the A1c chain rerun with it, release record v0.3.27); $K_\Theta=\tfrac{123}{125}$ from DYAD-THM-OPEN3-SPIRAL-REM (row below)"
LPH_NEW_B = LPH_COMMON + r"; the proof-outline constants $c_J=0.50220$, $c_7=157.58$ are bounded RECOG-side by RECOG-ALG-A1C-JET-REMAINDER-BOUNDS; no `[assuming:]` remains on these uses"
LPH_NEW_A = LPH_COMMON + r"; the proof-outline constants $c_J=0.50220$, $c_7=157.58$ remain under `[assuming: $c_J$, $c_7$]` at the points of use (proof-outline constants without a theorem row)"
NEW7_ROWS = ("\n" r"- [RID: DYAD-THM-LPHASE-ROWA-BRIDGE] :: (i) under branch (B), $r=\Lambda_3(z)+[S_\Theta-L_\Theta]+\tau[D_Q-D_3]+[\operatorname{Arg}(J/z)+\tau q]+\operatorname{Arg}(\widehat F/J)$ exactly; (ii) $|D_Q|\le0.79246\,q^{3/2}$, $|D_Q-D_3|\le0.36916\,q^2$ (certified $0.7924576\ldots$, $0.3691523\ldots$) :: " + DY + r" §6.14 (first published v6.4.23) :: §6.13b A1c (TAIL-HARMONICS, SHARPENED-SCHEDULE, COMBINED-TAIL, LOGFREE-ENVELOPE), §6.16e (START-OFFSET (ii), decoder) (v0.3.27) :: row-A disk $|z|\le\tfrac1{20}$ of the DYAD-THM-NF-INV chart, block base points in $U$, branch (B) on $U_T$"
             "\n" r"- [RID: DYAD-THM-OPEN3-SPIRAL-REM] :: $|S_\Theta-L_\Theta|\le K_\Theta q^2$ with $K_\Theta=\tfrac{123}{125}$ on $|z|\le\tfrac1{20}$ ($\tfrac{909}{1000}$ on $\tfrac1{40}$), rows not mixed :: " + DY + r" §6.14 (first published v6.4.14) :: §6.13b A1c, the constant $K_\Theta$ of the row-A remainder (v0.3.27) :: chart of DYAD-ALG-NF6; NF-REM rows, not mixed")
NEW7_C7 = ("\n" r"- [RID: DYAD-THM-NF-REM-C7-SHARP] :: $|\widehat F(z)-J(z)|\le C_7|z|^7$ with $C_7=85.1$ on $|z|\le\tfrac1{20}$ and $C_7=27.7$ on $|z|\le\tfrac1{40}$ (exact bounds $85.0731933471\ldots$, $27.6022209836\ldots$); the NF-REM constants $100/30$ and $C_D=1000/250$ unchanged :: " + DY + r" §6.14 (first published v6.4.23) :: §6.13a RECOG-THM-R9-SHARPENED-ROWS-C7 (v0.3.27; previously the same ceilings under `[assuming:]`) :: chart and norm of DYAD-THM-NF-REM; rows not mixed; $C_D$ not used by RECOG's B1 certificate")

def jet_s8():
    p = "evidence/recog/scripts/recog_a1c_jet_remainder_bounds_cert.py"; j = "evidence/recog/a1c_jet/a1c_jet_remainder_bounds_cert.json"; o = "evidence/recog/a1c_jet/a1c_jet_remainder_bounds_cert_output.txt"
    h = lambda f: hashlib.sha256(open(f, "rb").read()).hexdigest()
    return ("\n" r"- [RID: RECOG-ART-A1C-JET-REMAINDER-BOUNDS] `[v0.3.27]` :: `recog_a1c_jet_remainder_bounds_cert.py` (sha256 `" + h(p) + r"`) + `evidence/recog/a1c_jet/` (`" + h(j)[:8] + "…" + h(j)[-4:] + "`, `" + h(o)[:8] + "…" + h(o)[-4:] + r"`) :: G1 exact rationals (sufficient enclosures of $\sqrt3$, $|\mu|$, $|a_{32}|$, $|a_{05}|$ by squared comparisons; $c_J(q^*)<0.500819<0.50220$, $c_7(q^*)<100.231<157.58$; $u,w<1$, $q^*<\tfrac1{400}$), G2 interval enclosure inside the rational bounds, G3 monotonicity grid, G4 the identity $\operatorname{Im}a_{32}-\tfrac12\operatorname{Im}\mu^2=\tfrac{89\sqrt3}{324}$ (sympy); NC1 the display $100.23$ refused, NC2 the wrong-sign identity exceeds $0.50220$; ALL PASS. Rational bounds from the co-owner reconciliation script `evidence/recog/inbox_reconciliation_20261103/recog_r2_rational_bounds.py` (PR #172) :: `[ALG]` proof input (certificate)")

# ----------------------------------------------------------------------------- C7 texts ---------------------------------------------------------------
C7_Q_OLD = r"`[assuming: $C_7\le85.1$ on $|z|\le\tfrac1{20}$ and $C_7\le27.7$ on $|z|\le\tfrac1{40}$ — Dyadic's published DYAD-THM-NF-REM certificate values $85.07$ / $27.60$ rounded up; these are not Dyadic theorem statements; registration requested (§7)]`"
C7_Q_NEW = r"[import: " + DY + r" §6.14 | DYAD-THM-NF-REM-C7-SHARP] ($C_7\le85.1$ on $|z|\le\tfrac1{20}$ and $C_7\le27.7$ on $|z|\le\tfrac1{40}$, chart and norm of DYAD-THM-NF-REM, rows not mixed; registered at v6.4.23 — the same ceilings RECOG assumed in v0.3.25–v0.3.26; v0.3.27)"
C7_DEP_OLD = r"Depends on: RECOG-THM-R9-SHARPENED-ROWS and the listed assumption (the certificate refuses any ceiling below the published value $+0.005$, control NC2)."
C7_DEP_NEW = r"Depends on: RECOG-THM-R9-SHARPENED-ROWS and DYAD-THM-NF-REM-C7-SHARP (the certificate's control NC2, written against the earlier displays $85.07$ / $27.60$ $+0.005$, remains conservative against the exact bounds $85.0732\ldots$ / $27.6022\ldots$)."
C7_NS_OLD = r"any claim about $C_7$ beyond Dyadic's published values;"
C7_NS_NEW = r"any claim about $C_7$ beyond DYAD-THM-NF-REM and DYAD-THM-NF-REM-C7-SHARP;"
C7_KE_OLD = r"(a Dyadic bound on $\operatorname{Re}(\rho_7/z)$ along an orbit, or the B1-L2 ceiling $C_7\le85.1$, would lower it)"
C7_KE_NEW = r"(a Dyadic bound on $\operatorname{Re}(\rho_7/z)$ along an orbit would lower it, and so would the registered ceiling $C_7\le85.1$ of DYAD-THM-NF-REM-C7-SHARP — not applied in this edition)"
C7_NFREM_OLD = r"accepted; rows not mixed; certificate values 85.07/27.60; §6.13a sharpened rows (v0.3.25): the one-orbit bound in RECOG-ALG-R9-SUM-LEMMA; the published certificate values $85.07/27.60$ used only as `[assuming:]` ceilings $85.1/27.7$ in RECOG-THM-R9-SHARPENED-ROWS-C7 (registration requested);"
C7_NFREM_NEW = r"accepted; rows not mixed; certified bounds $85.0732/27.6023$ rounded up (displays corrected at v6.4.23 from $85.07/27.60$); §6.13a sharpened rows (v0.3.25): the one-orbit bound in RECOG-ALG-R9-SUM-LEMMA; the ceilings $85.1/27.7$ of RECOG-THM-R9-SHARPENED-ROWS-C7 imported from DYAD-THM-NF-REM-C7-SHARP since v0.3.27 (row below);"

# ----------------------------------------------------------------------------- DISP texts -------------------------------------------------------------
COR7 = r"`[COR]` v0.3.27: outward display of the certified value; the earlier display was nearest-rounded in the unsafe direction, the certificate works with the exact interval"
DISP = [
 ("DISP-KEPS", r"$K_\epsilon=0.7203$, $0.4513$, $0.1860$ at $a=625,1000,2500$", r"$K_\epsilon\le0.7204$, $0.4514$, $0.1861$ at $a=625,1000,2500$ (certified $0.72030407\ldots$, $0.45131291\ldots$, $0.18603976\ldots$; " + COR7 + ")"),
 ("DISP-C7R", r"$c_J^R=0.5008$, $c_7^R=100.23$", r"$c_J^R\le0.5008$, $c_7^R\le100.231$ (certified $0.50079841\ldots$, $100.23001968\ldots$; " + COR7 + ")"),
 ("DISP-G0", r"$\gamma_0=0.17715$, $\gamma_1=205.15$", r"$\gamma_0\le0.17716$, $\gamma_1\le205.15$ (certified $0.17715092\ldots$, $205.1458651\ldots$; " + COR7 + ")"),
 ("DISP-BETA", r"($\beta(625)=0.799$, $\beta\to0.792$)", r"($\beta(625)\le0.800$, $\beta\to0.792$; certified $\beta(625)=0.7993089\ldots$ with $c'_Q=0.36916$; " + COR7 + ")"),
 ("DISP-KPHI", r"($K_\Phi\le220.8471$ / $75.6392$)", r"($K_\Phi\le220.8471$ / $75.6393$; certified $75.63920819\ldots$; " + COR7 + ")"),
 ("DISP-WIN", r"resp. $q_0<1.011\times10^{-4}$", r"resp. $q_0<1.010\times10^{-4}$ (certified window $q_0<|G|/75.69=1.0109637\ldots\times10^{-4}$; `[COR]` v0.3.27: the earlier display $1.011\times10^{-4}$ lay above the certified window; the theorem's formula and its $C_2$ row are unchanged)"),
]

# ----------------------------------------------------------------------------- PIN texts --------------------------------------------------------------
CA = "claim audit v0.3.27"
PIN = [
 ("PIN-HDR", r"Dyadic `dyad-v6.4.22`, Number Genesis `numgen-v1.20.8`, Genesis v2.8.9, OFN v0.10, RRF v0.8.4 (convention and registry reference); Discrete Genesis v2.12.13 (reference only, no import).",
            r"Dyadic `dyad-v6.4.23`, Number Genesis `numgen-v1.21`, Genesis `gen-v2.10`, OFN `ofn-v0.12`, RRF v0.8.4 (convention and registry reference); Discrete Genesis v2.12.14 (reference only, no import)."),
 ("PIN-SYNC", r"Current owner editions: Dyadic `dyad-v6.4.22` (`2363ca40…8c29`), NUMGEN `numgen-v1.20.8` (`835a56f8…7e2f`), Genesis v2.8.9, OFN v0.10, RRF v0.8.4. For v0.3.23, for every load-bearing Dyadic and NUMGEN row,",
             r"Current owner editions: Dyadic `dyad-v6.4.23` (`9f874ccc…25cb`), NUMGEN `numgen-v1.21` (`4805760d…5701`), Genesis `gen-v2.10`, OFN `ofn-v0.12`, RRF v0.8.4. For v0.3.27 (as for v0.3.23), for every load-bearing Dyadic and NUMGEN row,"),
 ("PIN-SYNC2", r"(claim audit `evidence/recog/v0.3.23/claim_audit.json`; table in the v0.3.23 release record). Genesis, OFN and RRF rows are as audited v0.3.21 (§7.2);",
              r"(claim audit `evidence/recog/v0.3.27/claim_audit.json`, delimiter-anchored quotes; v0.3.23: `evidence/recog/v0.3.23/claim_audit.json`). Genesis, OFN and RRF rows are as audited v0.3.21 (§7.2), with the v0.3.27 checks noted at the Genesis and OFN rows;"),
]
# sub-mode edits: (key, unique line prefix, [(old, new, count)])
SUBS = [
 ("PIN-L290", "*Quantified.* [impor", [("RTG_DYADIC_OSCILLATOR_DSN_v6.4.22", DY, 1)]),
 ("PIN-L407", "`[ALG]` [import: Dyadic §6.1] [`[CO", [("v6.4.22 §1", "v6.4.23 §1", 1)]),
 ("PIN-L558", "`[DEF]` **Family.** ", [("Dyadic v6.4.22 §6.9", "Dyadic v6.4.23 §6.9", 1)]),
 ("PIN-L681", "`[THM]` [import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.22 §6.14 | D", [("RTG_DYADIC_OSCILLATOR_DSN_v6.4.22", DY, 1), ("current source v6.4.22 (claim audit v0.3.23)", "current source v6.4.23 (" + CA + ")", 1)]),
 ("PIN-L683", "`[ALG]` [import: RTG", [("RTG_DYADIC_OSCILLATOR_DSN_v6.4.22", DY, 1)]),
 ("PIN-L685", "`[ALG]` `[scope: for", [("RTG_DYADIC_OSCILLATOR_DSN_v6.4.22", DY, 1)]),
 ("PIN-L687", "`[THM]` [import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.22 §6.14 (pr", [("RTG_DYADIC_OSCILLATOR_DSN_v6.4.22", DY, 1)]),
 ("PIN-L689", "`[THM]` `[assuming: RECOG-THM-R9-MEMORY]` [import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.22 §6.14 (pro", [("RTG_DYADIC_OSCILLATOR_DSN_v6.4.22", DY, 1)]),
 ("PIN-L691", "`[THM]` `[assuming: RECOG-THM-R9-MEMORY]` [import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.22 §6.14, OPE", [("RTG_DYADIC_OSCILLATOR_DSN_v6.4.22", DY, 1), ("current source `dyad-v6.4.22` (claim audit v0.3.23)", "current source `dyad-v6.4.23` (" + CA + ")", 1)]),
 ("PIN-L715", "`[THM]` [RID: RECOG-THM-A1A-CD-PRIM", [("current source v6.4.22)", "current source v6.4.23, " + CA + ")", 1)]),
 ("PIN-L723", "Chart inclusions $\\t", [("current source v6.4.22 (claim audit v0.3.23)", "current source v6.4.23 (" + CA + ")", 1)]),
 ("PIN-L731", "with all three serie", [("RTG_DYADIC_OSCILLATOR_DSN_v6.4.22", DY, 1)]),
 ("PIN-L746", "Depends on: RECOG-TH", [("RTG_DYADIC_OSCILLATOR_DSN_v6.4.22", DY, 2)]),
 ("PIN-L783", "`[import: Dyadic v6.", [("current counterpart v6.4.22", "current counterpart v6.4.23", 1), ("claim audit v0.3.23", CA, 1)]),
 ("PIN-L794", "`[ALG]`/`[import: RR", [("Dyadic v6.4.22", "Dyadic v6.4.23", 2)]),
 ("PIN-L858", "> **[Local guard SG-R4]** Diagnostic twin $T_s$ only. *", [("Dyadic v6.4.22 §6.4", "Dyadic v6.4.23 §6.4", 1)]),
 ("PIN-L1144", "- [RID: DYAD-THM-NF-REM] ", [("(present at `dyad-v6.4.22` §6.14; v0.3.24)", "(present at `dyad-v6.4.23` §6.14; v0.3.24, " + CA + ")", 1)]),
 ("PIN-L1150", "- [RID: DYAD-DEF-PRI", [("(v6.4.22;", "(v6.4.23;", 1)]),
 ("PIN-L1151", "- [RID: DYAD-ALG-QC-", [("(v6.4.22;", "(v6.4.23;", 1)]),
 ("PIN-L1152", "- [RID: DYAD-ALG-SIX", [("(v6.4.22;", "(v6.4.23;", 1)]),
 ("PIN-L1153", "- [RID: (none — Genesis §6.1);", [(":: comparator construction, distinction anchoring ::", "(`gen-v2.10`, checked v0.3.27: the two RID declaration lines identical to v2.8.9) :: comparator construction, distinction anchoring ::", 1)]),
 ("PIN-L1155", "- [RID: NUMGEN-RESULT-L1-", [("current owner v1.20.8, `numgen-v1.20.8` §6.2", "current owner v1.21, `numgen-v1.21` §6.2", 1), ("claim audit v0.3.23", CA, 1)]),
 ("PIN-L1156", "- [RID: NUMGEN-OPEN-", [("current owner v1.20.8, `numgen-v1.20.8` §6.2", "current owner v1.21, `numgen-v1.21` §6.2", 1), ("claim audit v0.3.23", CA, 1)]),
 ("PIN-L1163", "- [RID: NUMGEN-THM-N", [("current counterpart `numgen-v1.20.8` §6.6", "current counterpart `numgen-v1.21` §6.6", 1), ("claim audit v0.3.23", CA, 1)]),
 ("PIN-L1169", "- [RID: OFN §6.2a, §", [("§7.3 identical — §7.2)", "§7.3 identical — §7.2; `ofn-v0.12`, checked v0.3.27: the imported statements of §6.2a and §7.3 unchanged; OFN's own import pins and TDR-G RIDs updated, one owner note added in §7.3)", 1)]),
 ("PIN-L1171", "- [RID: NUMGEN-DEF-N", [("RTG_NUMBER_GENESIS_DSN_v1.20.8 §6.6 (`numgen-v1.20.8`, `835a56f8…7e2f`)", "RTG_NUMBER_GENESIS_DSN_v1.21 §6.6 (`numgen-v1.21`, `4805760d…5701`; the earlier abbreviation `835a56f8…7e2f` of the v1.20.8 hash was miscopied, the hash ends `…817e`)", 1)]),
 ("PIN-L1172", "- [RID: NUMGEN-RESULT-N5A", [("RTG_NUMBER_GENESIS_DSN_v1.20.8 §6.6", "RTG_NUMBER_GENESIS_DSN_v1.21 §6.6", 1)]),
 ("PIN-L1173", "- [RID: DYAD-ALG-OPEN3-PHASE-OFFSET; DYA", [("RTG_DYADIC_OSCILLATOR_DSN_v6.4.22", DY, 1)]),
 ("PIN-L1174", "- [RID: DYAD-ALG-OPEN3-PHASE-OFFSET, pri", [("RTG_DYADIC_OSCILLATOR_DSN_v6.4.22", DY, 1)]),
 ("PIN-L1175", "- [RID: DYAD-THM-LPHASE-ROWA-REMAINDER] ", [("RTG_DYADIC_OSCILLATOR_DSN_v6.4.22", DY, 1)]),
 ("PIN-L1176", "- [RID: DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER] ", [("RTG_DYADIC_OSCILLATOR_DSN_v6.4.22", DY, 1), ("present at v6.4.22;", "present at v6.4.23 (" + CA + ");", 1)]),
 ("PIN-L1178", "RIDs marked \"(none)\"", [("checked at `dyad-v6.4.22`", "checked at `dyad-v6.4.23`, " + CA, 1)]),
 ("PIN-L677", "`[DEF]` [import: RTG", [("RTG_NUMBER_GENESIS_DSN_v1.20.8", "RTG_NUMBER_GENESIS_DSN_v1.21", 1)]),
 ("PIN-L679", "`[RESULT]` `[from: ALG]` [impo", [("RTG_NUMBER_GENESIS_DSN_v1.20.8", "RTG_NUMBER_GENESIS_DSN_v1.21", 1)]),
]
GAP_OLD = r"- `[import: RTG_NUMBER_GENESIS_DSN_v1.20.8 §6.6 N-5A-S1-INF / GAP-LOCK Lemma 3]` (pinned at v1.20.7 since v0.3.18; the owner records no theorem-level change in v1.20.8; the Lemma 3 text is present in the current source, claim audit v0.3.23) `[HEUR cross-reference]` Number Genesis proves"
GAP_NEW = r"- `[import: RTG_NUMBER_GENESIS_DSN_v1.21 §6.6 | NUMGEN-RESULT-N5AS1-GAPLOCK-SLIP-RATIO]` (GAP-LOCK Lemma 3; RID assigned by the owner at v1.21; pinned at v1.20.7 from v0.3.18; statement present at the cited RID in the current source, " + CA + r"). Consumed at two grades (NUMGEN inbox finding of 26 Oct 2026, dispositioned 29 Oct): (i) its exact bookkeeping identity $G_{n_j}=C+\tfrac\pi3s_j-o_j$ is used at the owner's grade `[ALG]` inside RECOG-RESULT-BTOKEN-LOG-EQUIVALENCE (§6.16e); (ii) `[HEUR cross-reference]` Number Genesis proves"
GAP2_OLD = r"The parallel defect-threshold theorem is owner-RID `NUMGEN-THM-N5AS1-DEFECT-THRESHOLD-RATIO`; no RID is inferred here for GAP-LOCK Lemma 3."
GAP2_NEW = r"The parallel defect-threshold theorem is owner-RID `NUMGEN-THM-N5AS1-DEFECT-THRESHOLD-RATIO`."

# ----------------------------------------------------------------------------- R1: §8 rows (hashes from the working tree) ------------------------------
S8_ROWS = {"RECOG-ART-A1C-SHARPENED-SCHEDULE": ["recog_a1c_tail_averaging_cert.py", "a1c_1b", "a1c_inblock", "a1c_comb"],
           "RECOG-ART-A1C-DECODER": ["a1c_2", "a1c_so", "a1c_joint"],
           "RECOG-ART-A1C-DRIFT-CENTERING": ["a1c_drift"],
           "RECOG-ART-A1C-CORRECTED-GRID": ["v0.3.26/corrected_grid.json"]}
def git_hashes(paths):
    out = {}
    for p in paths:
        b = subprocess.run(["git", "show", f"{PREV_TAG}:{p}"], capture_output=True).stdout
        out[p] = hashlib.sha256(b).hexdigest()
    return out
def s8_subs():
    """for each affected §8 row: every quoted hash of a file whose content changed since recog-v0.3.26 is replaced by the new hash (same
       full/abbreviated form), and the row is marked `[v0.3.27]` regenerated."""
    files = {"recog_a1c_tail_averaging_cert.py": "evidence/recog/scripts/recog_a1c_tail_averaging_cert.py"}
    for d in ("a1c_1b", "a1c_inblock", "a1c_comb", "a1c_2", "a1c_so", "a1c_joint", "a1c_drift"):
        for f in sorted(os.listdir(os.path.join("evidence/recog", d))):
            if f.endswith((".json", ".txt")): files[f"{d}/{f}"] = f"evidence/recog/{d}/{f}"
    files["v0.3.26/corrected_grid.json"] = "evidence/recog/v0.3.26/corrected_grid.json"
    old = git_hashes(files.values())
    new = {p: hashlib.sha256(open(p, "rb").read()).hexdigest() for p in files.values()}
    subs = []
    for rid in S8_ROWS:
        reps = []
        for p in files.values():
            if old[p] == new[p]: continue
            o, n = old[p], new[p]
            reps.append((f"`{o}`", f"`{n}`", None)); reps.append((f"`{o[:8]}…{o[-4:]}`", f"`{n[:8]}…{n[-4:]}`", None))
        subs.append((f"R1-S8-{rid}", f"- [RID: {rid}] ", reps, "; `[v0.3.27]` outputs regenerated by the owner rerun with $c'_Q=0.36916$ (R1; release record v0.3.27)"))
    return subs

# ----------------------------------------------------------------------------- the edit list ---------------------------------------------------------
TAIL_ANCHOR = r"[RID: RECOG-ALG-A1C-TAIL-HARMONICS] [scope: $x_0\in U$; every $M\ge1$] "
SCHED_ANCHOR = r"[RID: RECOG-THM-A1C-SHARPENED-SCHEDULE] [scope: as RECOG-THM-A1B-SLIP-SCHEDULE-U; $a$ known] "
ENV_ANCHOR = r"enclosed (RECOG-ALG-A1C-START-OFFSET); $a$ known] "
SO_ANCHOR = r"(ii) *Signed start offset* "
ADM_ANCHOR = r"[RID: RECOG-ALG-A1C-ADMISSIBLE-REGION] [scope: as RECOG-THM-A1C-SHARPENED-SCHEDULE, $a$ unknown] "
JC_ANCHOR = r"the true $a$ is never an input — in every box $a$, $L$, $b$, $\Theta_0$ and $\omega=a-b$ are interval variables] "
CT_DEP_OLD = r"Depends on: RECOG-ALG-A1C-TAIL-HARMONICS (amplitude brackets), RECOG-ALG-A1C-INBLOCK-ANGLE; DYAD-THM-LPHASE-ROWA-REMAINDER (the decomposition of $r$ under branch (B)); DYAD-THM-NF-REM ($C_7$, $c_1$ row)."
def d5_edits(g):
    Q, QS, DEP, LPH = (Q_NEW_B, QS_NEW_B, DEP_B, LPH_NEW_B) if g == "D5B" else (Q_NEW_A, QS_NEW_A, DEP_A, LPH_NEW_A)
    e = [
     (f"{g}-TAIL", g, "§6.13b TAIL-HARMONICS qualifier", "str", "live", TAIL_ANCHOR + Q_OLD, TAIL_ANCHOR + Q),
     (f"{g}-TAIL-DEP", g, "§6.13b TAIL-HARMONICS Depends on", "str", "live", r"DYAD-ALG-NF6 ($h_2$); the listed assumption.", r"DYAD-ALG-NF6 ($h_2$); " + DEP + "."),
     (f"{g}-SCHED", g, "§6.13b SHARPENED-SCHEDULE qualifier", "str", "live", SCHED_ANCHOR + Q_OLD, SCHED_ANCHOR + Q),
     (f"{g}-SCHED-DEP", g, "§6.13b SHARPENED-SCHEDULE Depends on", "str", "live", r"RECOG-ALG-A1C-COMBINED-TAIL; the listed assumption.", r"RECOG-ALG-A1C-COMBINED-TAIL; " + DEP + "."),
     (f"{g}-ENV", g, "§6.13b LOGFREE-ENVELOPE qualifier", "str", "live", ENV_ANCHOR + Q_OLD, ENV_ANCHOR + Q),
     (f"{g}-ENV-DEP", g, "§6.13b LOGFREE-ENVELOPE Depends on", "str", "live", r"the listed assumption (through $E^{(4)}$ and $\Delta_a$).", DEP + r" (through $E^{(4)}$ and $\Delta_a$)."),
     (f"{g}-SO", g, "§6.16e START-OFFSET (ii) qualifier", "str", "live", SO_ANCHOR + Q_OLD, SO_ANCHOR + Q),
     (f"{g}-SO-DEP", g, "§6.16e START-OFFSET Depends on", "str", "live", r"RECOG-RESULT-A1C-RECORD-PHASE-READOUT ($L$); the listed assumption in (ii) only.", r"RECOG-RESULT-A1C-RECORD-PHASE-READOUT ($L$); in (ii) " + DEP + "."),
     (f"{g}-ADM", g, "§6.16e ADMISSIBLE-REGION qualifier", "str", "live", ADM_ANCHOR + QS_OLD, ADM_ANCHOR + QS),
     (f"{g}-JC", g, "§6.16e JOINT-CONTRACTOR qualifier", "str", "live", JC_ANCHOR + QS_OLD, JC_ANCHOR + QS),
     (f"{g}-S7-LPH", g, "§7 LPHASE row", "str", "live", LPH_OLD, LPH),
     (f"{g}-S7-NEW", g, "§7 rows BRIDGE, SPIRAL-REM", "line", "live", "- [RID: DYAD-THM-LPHASE-ROWA-REMAINDER] ", "{LINE}" + NEW7_ROWS),
     (f"{g}-CT-DEP", g, "§6.13b COMBINED-TAIL Depends on", "str", "live", CT_DEP_OLD,
      r"Depends on: RECOG-ALG-A1C-TAIL-HARMONICS (amplitude brackets), RECOG-ALG-A1C-INBLOCK-ANGLE; DYAD-THM-LPHASE-ROWA-BRIDGE (the exact decomposition of $r$ under branch (B), registered at v6.4.23; before, DYAD-THM-LPHASE-ROWA-REMAINDER's proof); DYAD-THM-NF-REM ($C_7$, $c_1$ row)" + ("; RECOG-ALG-A1C-JET-REMAINDER-BOUNDS ($c_J^R$, $c_7^R$; v0.3.27)." if g == "D5B" else ".")),
    ]
    if g == "D5B":
        e += [
         ("D5B-S1-SCHED", g, "§1 sharpened-schedule qualifier", "str", "live", r"[RID: RECOG-THM-A1C-SHARPENED-SCHEDULE] `[assuming: Dyadic row-A bridge proof constants (D5)]` (v0.3.25)",
          r"[RID: RECOG-THM-A1C-SHARPENED-SCHEDULE] (v0.3.25; its row-A remainder constants are owner theorem rows or RECOG-certified since v0.3.27 — DYAD-THM-LPHASE-ROWA-BRIDGE, DYAD-THM-OPEN3-SPIRAL-REM, RECOG-ALG-A1C-JET-REMAINDER-BOUNDS; the former (D5) qualifier is discharged)"),
         ("D5B-S1-ENV", g, "§1 envelope qualifier", "str", "live", r"(RECOG-ALG-A1C-LOGFREE-ENVELOPE `[assuming: (D5)]`, §6.13b)", r"(RECOG-ALG-A1C-LOGFREE-ENVELOPE, §6.13b; (D5) discharged v0.3.27)"),
         ("D5B-R6-DEC", g, "§2 R6 decoder sub-item", "str", "live", r"under the (D5) `[assuming:]` of the envelope;", r"with the row-A remainder constants of the envelope (DYAD-THM-LPHASE-ROWA-BRIDGE, DYAD-THM-OPEN3-SPIRAL-REM, RECOG-ALG-A1C-JET-REMAINDER-BOUNDS; the former (D5) qualifier discharged at v0.3.27);"),
         ("D5B-CT-SRC", g, "§6.13b COMBINED-TAIL constants source", "str", "live", r"(RECOG-derived from the explicit jet and $C_7$)", r"(RECOG-ALG-A1C-JET-REMAINDER-BOUNDS, from the explicit jet and $C_7$)"),
         ("D5B-JET", g, "§6.13b JET-REMAINDER-BOUNDS block before COMBINED-TAIL", "str", "live", r"`[ALG]` [RID: RECOG-ALG-A1C-COMBINED-TAIL] [scope:", JET_BLOCK + r"`[ALG]` [RID: RECOG-ALG-A1C-COMBINED-TAIL] [scope:"),
         ("D5B-S8-JET", g, "§8 JET artifact row after CORRECTED-GRID", "line", "live", "- [RID: RECOG-ART-A1C-CORRECTED-GRID] ", "{LINE}" + "{JET_S8}"),
        ]
    else:
        e += [
         ("D5A-S1-SCHED", g, "§1 sharpened-schedule qualifier", "str", "live", r"[RID: RECOG-THM-A1C-SHARPENED-SCHEDULE] `[assuming: Dyadic row-A bridge proof constants (D5)]` (v0.3.25)",
          r"[RID: RECOG-THM-A1C-SHARPENED-SCHEDULE] `[assuming: the Dyadic proof-outline constants $c_J$, $c_7$]` (v0.3.25; the other row-A remainder constants imported since v0.3.27 — DYAD-THM-LPHASE-ROWA-BRIDGE, DYAD-THM-OPEN3-SPIRAL-REM)"),
         ("D5A-S1-ENV", g, "§1 envelope qualifier", "str", "live", r"(RECOG-ALG-A1C-LOGFREE-ENVELOPE `[assuming: (D5)]`, §6.13b)", r"(RECOG-ALG-A1C-LOGFREE-ENVELOPE `[assuming: $c_J$, $c_7$]`, §6.13b)"),
         ("D5A-R6-DEC", g, "§2 R6 decoder sub-item", "str", "live", r"under the (D5) `[assuming:]` of the envelope;", r"under the narrowed `[assuming:]` ($c_J$, $c_7$) of the envelope;"),
        ]
    return e
EDITS = []
EDITS += d5_edits("D5B") + d5_edits("D5A")
EDITS += [
 ("C7-Q", "C7", "§6.13a SHARPENED-ROWS-C7 qualifier", "str", "live", C7_Q_OLD, C7_Q_NEW),
 ("C7-DEP", "C7", "§6.13a SHARPENED-ROWS-C7 Depends on", "str", "live", C7_DEP_OLD, C7_DEP_NEW),
 ("C7-NS", "C7", "§6.13a Not supplied", "str", "live", C7_NS_OLD, C7_NS_NEW),
 ("C7-KE", "C7", "§6.13b RECIPROCAL-DRIFT Not supplied", "str", "live", C7_KE_OLD, C7_KE_NEW),
 ("C7-NFREM", "C7", "§7 NF-REM row", "str", "live", C7_NFREM_OLD, C7_NFREM_NEW),
 ("C7-S7-NEW", "C7", "§7 row C7-SHARP after NF-REM", "line", "live", "- [RID: DYAD-THM-NF-REM] ", "{LINE}" + NEW7_C7),
]
EDITS += [(k, "DISP", "display: " + k, "str", "live", o, n) for k, o, n in DISP]
EDITS += [(k, "PIN", "pin: " + k, "str", "live", o, n) for k, o, n in PIN]
EDITS += [("PIN-GAP", "PIN", "§2 R6 GAP-LOCK Lemma 3 row", "str", "live", GAP_OLD, GAP_NEW), ("PIN-GAP2", "PIN", "§2 R6 GAP-LOCK Lemma 3 row, last sentence", "str", "live", GAP2_OLD, GAP2_NEW)]
EDITS += [(k, "PIN", "pin: " + k, "sub", "live", pre, reps) for k, pre, reps in SUBS]

APPA_LINES = {
 "R1": r"- **R1 — $c'_Q$ (correction of an assumed constant, separate decision):** RECOG copied the row-A bridge constant as $c'_Q=0.36915$, a nearest-rounded display below the certified majorant $0.3691523\ldots$; Dyadic registered $c'_Q=0.36916$ in DYAD-THM-LPHASE-ROWA-BRIDGE (`dyad-v6.4.23`). The part-1b literal is changed, the eight A1c certificates and the corrected grid were rerun by the owner (every gate passes; no printed decimal changes except $\beta(625)$, now $0.7993089\ldots$, printed $\le0.800$), and the four affected §8 rows are re-registered. `[COR]` at the points of use; no Appendix B entry (no claim withdrawn).",
 "D5B": r"- **R2 — (D5) discharged, option (b) (separate decision):** new RECOG-ALG-A1C-JET-REMAINDER-BOUNDS `[ALG]` (§6.13b; $c_J\le0.500819$, $c_7\le100.231$ on $q\le q^*$, from DYAD-ALG-NF6 and DYAD-THM-NF-REM only; RECOG-ART-A1C-JET-REMAINDER-BOUNDS, §8); with DYAD-THM-LPHASE-ROWA-BRIDGE and DYAD-THM-OPEN3-SPIRAL-REM imported, every row-A remainder constant of the known-$a$ chain is an owner theorem row or RECOG-certified, and the `[assuming:]` is removed at TAIL-HARMONICS, SHARPENED-SCHEDULE, LOGFREE-ENVELOPE, START-OFFSET (ii), ADMISSIBLE-REGION, JOINT-CONTRACTOR (§1, §2 R6 decoder line, §7 rows aligned). No grade changes; no statement other than the source condition changes.",
 "D5A": r"- **R2 — (D5) narrowed, fallback (a) (separate decision):** DYAD-THM-LPHASE-ROWA-BRIDGE and DYAD-THM-OPEN3-SPIRAL-REM imported; the `[assuming:]` narrowed to the two proof-outline constants $c_J=0.50220$, $c_7=157.58$ at the same six sites (§1, §2 R6 decoder line, §7 rows aligned). No grade changes.",
 "C7": r"- **R3 — $C_7$ rows (separate decision):** RECOG-THM-R9-SHARPENED-ROWS-C7 imports DYAD-THM-NF-REM-C7-SHARP (the same ceilings $85.1/27.7$, registered at `dyad-v6.4.23`) instead of assuming them; stale wording updated (§6.13a, §6.13b K_ε *Not supplied*, §7 NF-REM row and new C7-SHARP row); the B1 certificate and its NC2 unchanged.",
 "DISP": r"- **Item 7 — display direction (separate decision):** eight displays printed in the safe direction with `[COR]` at the point of use — $K_\epsilon\le0.7204$, $0.4514$, $0.1861$ (were $0.7203$, $0.4513$, $0.1860$); $c_7^R\le100.231$ (was $100.23$); $\gamma_0\le0.17716$ (was $0.17715$); $\beta(625)\le0.800$ (was $0.799$); $K_\Phi\le75.6393$ (was $75.6392$); the B1 window $q_0<1.010\times10^{-4}$ (was $1.011\times10^{-4}$, above the certified window). Display corrections only: every certificate works with the exact intervals; no inequality, formula, grade or RID changes.",
 "PIN": r"- **R4–R6 — pins and receipts (maintenance):** live current-use Dyadic citations repinned to `dyad-v6.4.23` and NUMGEN citations to `numgen-v1.21` (claim audit v0.3.27, delimiter-anchored); GAP-LOCK Lemma 3 cited by NUMGEN-RESULT-N5AS1-GAPLOCK-SLIP-RATIO with its two consumption grades; companion pins Genesis `gen-v2.10`, OFN `ofn-v0.12` (OFN v0.11 notice received; the imported statements of §6.2a and §7.3 unchanged), TDR-G v2.12.14 (reference only); a miscopied hash abbreviation of NUMGEN v1.20.8 noted; provenance and historical-audit pins kept.",
}
APPA_TAIL = (r"- **Unchanged:** every existing RID's statement and grade; every OPEN status word (R1, R3 PARTIAL; R4, R5, R6 ACTIVE; R2, R7–R11 CLOSED); A1c-Q1′ `[OPEN]`; Appendix B." "\n"
             r"- **Records:** release record `records/recog/RECOG_v0_3_27_RELEASE_RECORD.md` (candidate); predecessor tag `recog-v0.3.26` (SHA-256 `45e307f8…dd34`)." "\n\n")
NEW_RIDS = {"R1": set(), "D5B": {"RECOG-ALG-A1C-JET-REMAINDER-BOUNDS", "RECOG-ART-A1C-JET-REMAINDER-BOUNDS"}, "D5A": set(), "C7": set(), "DISP": set(), "PIN": set()}

def appa_edit(groups):
    head = "## Appendix A — Version History\n\nOne compact entry per edition (Methodology v1.4 §1). Full records of earlier editions — adoption metadata, draft-round records, review verdicts, the stacked status summaries and the freeze history — are in Appendix A and the header of v0.3.22 (tag `recog-v0.3.22`, SHA-256 `0dcce9e4…bcd9`). Scientific corrections and retired claims: Appendix B.\n\n"
    old = head + "### v0.3.26 — 28 October 2026 — Adopted"
    new = head + "### v0.3.27 — DRAFT, stage 1 (maintenance intermediate; not adopted)\n"
    new += r"- **Basis:** the RECOG inbox round after v0.3.26 — Dyadic v6.4.23 notice (registrations DYAD-THM-LPHASE-ROWA-BRIDGE, DYAD-THM-NF-REM-C7-SHARP; $c'_Q=0.36916$) and OFN v0.11 notice; Atlas advisory and owner entry note (PR #168); independent co-owner dispositions (PR #169, PR #170); two-co-owner reconciliation of 3 Nov 2026 (PR #172 proposal, PR #173 reply, ChatGPT acceptance record). Each group below carries its own acceptance decision." + "\n"
    for g in GROUPS:
        if g in groups: new += APPA_LINES[g] + "\n"
    new += APPA_TAIL + "### v0.3.26 — 28 October 2026 — Adopted"
    return ("A-1", "ALL", "Appendix A: v0.3.27 draft entry (per variant)", "str", "appA", old, new)

def apply(s, edits):
    i = s.index(APPA_START); j = s.index(APPA_END)
    live = s[:i] + "\x00APPA\x00" + s[j:]
    appa = s[i:j]
    record = []
    for e in edits:
        k, grp, loc, mode, region = e[:5]
        txt = live if region == "live" else appa
        if mode in ("line", "sub", "s8"):
            prefix = e[5]
            lines = txt.split("\n"); hits = [l for l in lines if l.startswith(prefix)]
            assert len(hits) == 1, f"{k}: expected 1 line starting with {prefix!r}, found {len(hits)}"
            old_full = hits[0]
            if mode == "line":
                new_full = e[6].replace("{LINE}", old_full).replace("{JET_S8}", jet_s8() if "{JET_S8}" in e[6] else "")
            else:
                new_full = old_full
                for o, n, c in e[6]:
                    cnt = new_full.count(o)
                    if c is None:
                        assert cnt <= 1, f"{k}: {o!r} occurs {cnt} times"
                    else:
                        assert cnt == c, f"{k}: {o!r} occurs {cnt} times, expected {c}"
                    new_full = new_full.replace(o, n)
                if mode == "s8":
                    assert new_full != old_full, f"{k}: no hash changed"
                    new_full += e[7]
        else:
            old_full, new_full = e[5], e[6]
        n = txt.count(old_full)
        assert n == 1, f"{k}: expected 1 match, found {n}"
        assert old_full != new_full, f"{k}: no-op edit"
        txt = txt.replace(old_full, new_full)
        if region == "live": live = txt
        else: appa = txt
        record.append({"key": k, "group": grp, "location": loc, "mode": mode, "region": region,
                       "old_sha256": hashlib.sha256(old_full.encode()).hexdigest(), "new_sha256": hashlib.sha256(new_full.encode()).hexdigest(),
                       "old": old_full, "new": new_full})
    assert live.count("\x00APPA\x00") == 1
    return live.replace("\x00APPA\x00", appa), record

def main(argv):
    base, out, log = argv[1:4]
    groups = {"R1", "D5B", "C7", "DISP", "PIN"}
    if "--only" in argv:
        groups = set(argv[argv.index("--only") + 1].split(","))
        assert groups <= set(GROUPS), groups
    assert not ("D5B" in groups and "D5A" in groups), "D5B and D5A are alternatives"
    assert ("R1" in groups) == bool(groups & {"D5B", "D5A"}), "R1 is built with exactly one of D5B / D5A (the five text sites carry c'_Q through them)"
    raw = open(base, "rb").read()
    assert hashlib.sha256(raw).hexdigest() == BASE_SHA, "base is not adopted v0.3.26 (tag recog-v0.3.26)"
    s = raw.decode("utf-8")
    edits = [e for e in EDITS if e[1] in groups]
    if "R1" in groups:
        edits += [(k, "R1", "§8 row " + pre, "s8", "live", pre, reps, note) for k, pre, reps, note in s8_subs()]
    keys = [e[0] for e in edits]; assert len(keys) == len(set(keys)), "duplicate edit keys"
    edits.append(appa_edit(groups))
    t, record = apply(s, edits)
    data = t.encode("utf-8")
    open(out, "wb").write(data)
    new_rids = sorted(set().union(*(NEW_RIDS[g] for g in groups)))
    json.dump({"base_sha256": BASE_SHA, "base_tag": PREV_TAG, "groups": sorted(groups), "intermediate_sha256": hashlib.sha256(data).hexdigest(),
               "declared_new_recog_rids": new_rids, "edit_count": len(record), "edits": record}, open(log, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(hashlib.sha256(data).hexdigest(), len(record), "edits", "groups:", ",".join(sorted(groups)))

if __name__ == "__main__":
    main(sys.argv)
