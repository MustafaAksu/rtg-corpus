#!/usr/bin/env python3
"""Build the AZ v0.7 corrections edition from the adopted v0.6 bytes.

    python3 -I build_az_v0_7.py BASE.md OUT.md LOG.json          # build
    python3 -I build_az_v0_7.py BASE.md CANDIDATE.md LOG.json --check
    python3 -I build_az_v0_7.py BASE.md CANDIDATE.md LOG.json --controls

BASE.md is `git show az-v0.6:dsn/RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN.md`.

Every edit targets base lines by number and is asserted against the base text
(a line prefix, or an exact-once substring inside the line). `rows` names the
row(s) of records/az/AZ_REACTIVATION_TRIAGE.md that the edit carries out;
"edition" marks the header, history and footer lines every release changes.
The build is assertion-gated: any mismatch stops it. A passing build or check
authorizes nothing.
"""
import hashlib
from collections import Counter
import json
import re
import sys

BASE_SHA256 = "dec78a4721d2f34711218d9b79ba0ce6438523060098f770cad5dd3f5eb70b8a"

DYAD = "RTG_DYADIC_OSCILLATOR_DSN"
TDRG = "RTG_DISCRETE_GENESIS_DSN"

# kind: "line"   (n, prefix, new)            replace base line n
#       "str"    (n, [(old, new), ...])      exact-once substrings in base line n
#       "block"  (a, b, prefix_a, prefix_b, [new lines])  replace base lines a..b
#       "after"  (n, prefix, [new lines])    insert after base line n
#       "delete" (n, prefix)                 remove base line n
EDITS = [
    # ---- header -----------------------------------------------------------
    ("E01", "edition", "line", (1, "# RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN_v0.6",
        "# RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN_v0.7")),
    ("E02", "edition", "line", (4, "**Date:** June 2026",
        "**Date:** November 2026 (v0.7, corrections only; the scientific content is that of v0.6, June 2026)  ")),
    ("E03", "8", "line", (6, "**DSN Methodology:** DSN_METHODOLOGY_v1.2",
        "**DSN Methodology:** DSN_METHODOLOGY_v1.2 (declared; kept for this corrections edition by PI decision of 10 Nov 2026 — the governing Methodology is v1.4, `methodology-v1.4`; the v1.4 migration is a separate edition)  ")),
    ("E04", "7", "line", (10, "**Supersedes:** `RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN_v0.5`",
        "**Supersedes:** `RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN_v0.6` (tag `az-v0.6`, SHA-256 `" + BASE_SHA256 + "`)  ")),
    ("E05", "2,3,4,5,6,8", "line", (11, "**Companion documents:** `RTG_PROGRAMME_OVERVIEW_v1.1`",
        "**Companion documents (governing editions, November 2026):** Programme Overview v1.4 (`programme-v1.4`) · Dyadic Oscillator v6.4.23 (`dyad-v6.4.23`) · Discrete Genesis v2.12.14 (`tdrg-v2.12.14`) · Genesis Geometry v2.10 (`gen-v2.10`) · OPEN-M v0.7.1 (`uvm-v0.7.1`) · DSN Methodology v1.4 (`methodology-v1.4`; this document declares v1.2, see above)  ")),
    ("E06", "edition", "str", (13, [(
        " A visible correction/retraction block is added (§4.3.4 and Appendix B).",
        " A visible correction/retraction block is added (§4.3.4 and Appendix B). **v0.7 is a corrections-only edition:** every owner pin, identifier and imported statement is synchronized with the current adopted owner editions named in the header; the withdrawn OPEN-M \"legal ×2\" reading is removed (§6, Appendix B); the Thread C evidence files are recorded as not available in the repository (§9). No new scientific claim is made, no grade of an AZ-owned result changes, and Thread C is unchanged.")])),
    # ---- §0.1 ownership map -----------------------------------------------
    ("E07", "3", "str", (63, [("`" + DYAD + "_v6.4.8.1`", "`" + DYAD + "` v6.4.23 (`dyad-v6.4.23`)")])),
    ("E08", "4", "str", (64, [("`" + TDRG + "_v2.12`", "`" + TDRG + "` v2.12.14 (`tdrg-v2.12.14`)")])),
    ("E09", "28", "str", (69, [(
        "| `RTG_PROGRAMME_OVERVIEW` | patch requested; this DSN cannot self-register at Tier 0 |",
        "| `RTG_PROGRAMME_OVERVIEW` v1.4 (`programme-v1.4`) | registered there as a Tier 5 infrastructure entry (its §6.1, §6.5) with interfaces IF20 and IF21 (its §7.2); see §7 |")])),
    ("E10", "5,6", "str", (70, [(
        "`RTG_GENESIS_GEOMETRY_DSN_v2.8.4` / `RTG_OPEN_M_DSN_v0.6`",
        "`RTG_GENESIS_GEOMETRY_DSN` v2.10 (`gen-v2.10`) / `RTG_OPEN_M_DSN` v0.7.1 (`uvm-v0.7.1`)")])),
    # ---- §1.2 ---------------------------------------------------------------
    ("E11", "3", "str", (98, [("`[source: " + DYAD + "_v6.4.8.1 §6.11]`", "`[source: " + DYAD + " v6.4.23 §6.11]`")])),
    ("E12", "10", "line", (103, "- `[import-ref]` **The dyadic channel boundary is closed at $b=4$.**",
        r'''- `[import-ref]` **The dyadic channel boundary at $b=4$.** Universal pure anti-holomorphic raw vanishing (for $p\ge b+2$) holds for $b\in\{2,3,4\}$ and fails at $b=5$ for every $p\ge6$; all-$b\ge5$ persistence and general-coefficient versions remain `[OPEN]`, so no "iff $b\le4$" statement is made (the owner withdrew that shorthand). `[ALG]` `[RID: DYAD-ALG-B5-ALLP-NONVANISHING]` `[source: ''' + DYAD + " v6.4.23 §6.11]`")),
    # ---- §3 programme guards ------------------------------------------------
    ("E13", "2,27", "block", (151, 157, "Programme-level guards from `RTG_PROGRAMME_OVERVIEW_v1.1`", "**[SG-PROG-4]** No result from Tier 4 or Tier 5", [
        "Programme-level guards SG-PROG-1 to SG-PROG-4 of `RTG_PROGRAMME_OVERVIEW` v1.4 (`programme-v1.4`) §8 apply in full. Their governing text is there and is not quoted here; the three entries below state only how each applies to this study. Sub-study guards specific to this document follow.",
        "",
        "**[SG-PROG-1]** (cross-branch physical use). No physical law, coefficient, observable identification or evidential strengthening passes between the discrete and continuous branches of this study without a named, proved bridge. This is the primary firewall governing Thread B (§4) of this study. `[source: RTG_PROGRAMME_OVERVIEW v1.4 §8]`",
        "",
        "**[SG-PROG-2]** (model selection is not local proof status). All Thread A results (§4.1) are conditional on the selected continuous generator and are not described as physically primitive while OPEN-P0 is open. `[source: RTG_PROGRAMME_OVERVIEW v1.4 §8]`",
        "",
        "**[SG-PROG-4]** (document location does not create transfer authority). This study's Tier 5 hub placement is not a bridge: Thread B/C items are not injected into Thread A or vice versa. `[source: RTG_PROGRAMME_OVERVIEW v1.4 §8]`",
    ])),
    # ---- §4.1 Thread A ------------------------------------------------------
    ("E14", "3", "str", (199, [("`" + DYAD + "_v6.4.8.1`, §2 and §6.11.", "`" + DYAD + "` v6.4.23 (`dyad-v6.4.23`), §2 and §6.11.")])),
    ("E15", "3", "str", (200, [(
        "v0.6 carries the Thread A ledger forward from v0.5 unchanged in content; no Thread A item is altered by the Thread C work.",
        "v0.7 synchronizes the Thread A ledger with Dyadic v6.4.23 (pins, identifiers and owner corrections; Appendix A); no Thread A item is altered by the Thread C work.")])),
    ("E16", "9", "line", (204, "`[import-ref]` `[THM]` **Raw cubic theorem.** The raw cubic coefficient of the $p$-step map is exact.",
        r"`[import-ref]` `[THM]` **Raw cubic theorem.** For the declared $K_p$ family in the raw $Z_p$ eigenframe, the $z^2\bar z$ coefficient of the **raw one-step map** is exact, for $p\ge3$. It is not a statement about the raw $p$-step map. Owner caveat: the formula is recovered and algebraically verified; its identity with the historical proposition is not yet established (Dyadic Appendix E). `[RID: DYAD-THM-RAW-CUBIC]` `[source: " + DYAD + " v6.4.23 §2 OPEN 9]`")),
    ("E17", "18", "line", (208, r"- $p=5$: $\nu_5^{(5)}$ exact over $\mathbb{Q}(\sqrt5, \sqrt{10+2\sqrt5})$",
        r"- $p=5$: $\nu_5^{(5)}$ exact in $\mathbb{Q}(\zeta_5)$ (real and imaginary parts in $\mathbb{Q}(\sqrt5,\sqrt{10+2\sqrt5})$)")),
    ("E18", "11", "after", (220, "", [
        r"`[import-ref]` `[THM]` `[scope: all $p=4s$, $s\ge2$]` **Cubic cascade $q=4$, $(0,3)$ phase/factorization law.** $Q_p=i\,\zeta_p^3\,M_p$ with $M_p\in\mathbb{Q}(\zeta_p)^+$; $p=8$ is the zero degeneracy ($Q_8=0$). This closes the exact cascade formula for the family $p=4s$; it is not a generic-$s$ formula. `[RID: DYAD-THM-Q403-PHASELAW]` `[source: " + DYAD + " v6.4.23 §6.11]`",
        "",
    ])),
    ("E19", "3,10", "str", (229, [("`[source: " + DYAD + "_v6.4.8.1 §6.11]`",
        "`[RID: DYAD-ALG-B5-ALLP-NONVANISHING]` `[source: " + DYAD + " v6.4.23 §6.11]`")])),
    ("E20", "10,17", "str", (231, [
        ("(`DYAD-OPEN-B5-ALLP`, with `DYAD-ART-B5-SECULAR` as the secular-coefficient artifact)",
         "(`DYAD-ALG-B5-ALLP-NONVANISHING`, with `DYAD-ART-B5-SECULAR` as the secular-coefficient artifact; `DYAD-OPEN-B5-ALLP` is the closed lifecycle identifier)"),
        ("`[source: " + DYAD + "_v6.4.8.1 §6.11]`", "`[source: " + DYAD + " v6.4.23 §2 OPEN 9]`"),
    ])),
    ("E21", "17", "str", (233, [("`[source: " + DYAD + "_v6.4.8.1 §6.11]`", "`[source: " + DYAD + " v6.4.23 §2 OPEN 9]`")])),
    ("E22", "14,15", "str", (235, [
        ("anchored by the eigenframe linear-part lemma.",
         "anchored by the eigenframe linear-part lemma (the owner keeps that lemma `[ALG]`; its statement is not recovered, Dyadic Appendix D)."),
        ("`[RID: DYAD-ALG-Q3-CANCEL]` `[source: " + DYAD + "_v6.4.8.1 §2 OPEN 9]`",
         "`[RID: DYAD-ALG-Q3-DEG2-CANCEL]` `[source: " + DYAD + " v6.4.23 §6.11]`"),
    ])),
    ("E23", "15", "str", (237, [(
        "in the registered sub-horizon setting. `[source: DYAD-OPEN-P-RESONANCE]`",
        r"in the registered sub-horizon setting. Owner evidence boundary (Dyadic Appendix D): $\chi_p$, $K^{\rm extra}_{p,q}$ and the cardinality lemma are defined; the other eight objects ($\mathcal{Q}(p)$, $\Pi^{\rm extra}_{p,q}$, $J^{extra,raw}_{p,q,D}$, $\mathcal{B}^{extra}_{p,q,D}$, $Z^{\rm miss}_{p,q,D}$, $C^{\rm mult}_{\rm sub}$, $C^{\rm uniq}_{\rm sub}$, $\Delta_{\rm overlap}$) keep their names without a recovered definition, so they are not usable here for independent computation. `[source: DYAD-OPEN-P-RESONANCE]`")])),
    ("E24", "3,13", "line", (243, "The following items are owned by `" + DYAD + "_v6.4.8.1` OPEN 9.",
        "The following items are owned by `" + DYAD + "` v6.4.23 OPEN 9. They are listed here as programme context only. Progress on them is tracked in the Dyadic DSN, not here; the owner's current list is Dyadic §2 OPEN 9 (active sub-items), which also holds items not repeated here.")),
    ("E25", "11", "delete", (245, "- Exact cubic cascade formula for $q=4,(0,3)$:")),
    ("E26", "12,13", "line", (250, "- Near-cancellation structure of $-13+15\\sqrt3/2\\approx0.0096$",
        r"- Near-cancellation structure at the $p=12$, $q=4$, $(0,3)$ cascade boundary, $-13+15\sqrt3/2\approx-0.0096$ (modulus $0.0096$): algebraic nonzero is closed and the exact cascade formula is closed (`DYAD-THM-Q403-PHASELAW`, §4.1.1); the structural explanation — in the owner's current form, the exact large-$p$ behaviour of $|Q_p|$ — remains `[OPEN]`.")),
    # ---- §4.2 Thread B ------------------------------------------------------
    ("E27", "4", "str", (268, [("`" + TDRG + "_v2.12`.", "`" + TDRG + "` v2.12.14 (`tdrg-v2.12.14`).")])),
    ("E28", "4", "str", (269, [("v0.6 carries Thread B forward unchanged.",
        "v0.7 synchronizes Thread B with TDR-G v2.12.14 (owner RIDs and owner corrections; Appendix A).")])),
    ("E29", "19", "str", (271, [("`[source: " + TDRG + "_v2.12 §1]`",
        "`[RID: TDRG-DEF-ZN-STATE]` (phase universe and variable-size state) `[RID: TDRG-DEF-PHYSICAL-STATE]` (physical state as the quotient by global phase; relational phases) `[RID: TDRG-DEF-BAND]` (defect band) `[source: " + TDRG + " v2.12.14 §6.1]`")])),
    ("E30", "20", "str", (273, [("v2.12 adds the band-form extension LEM-REACH:",
        "The band-form extension is LEM-REACH (`TDRG-ALG-LEM-REACH`; the $k=0$ statement is `TDRG-THM-REACHABILITY-K0`):")])),
    ("E31", "21", "str", (275, [("LEM-RETRIG gives an exact two-node period-2 retrigger criterion:",
        r"LEM-RETRIG (`TDRG-ALG-LEM-RETRIG`) gives an exact two-node retrigger criterion for a bound state of period dividing 2 (least period 2 for $d\ne0$; $d=0$ is a fixed point):")])),
    ("E32", "22", "str", (277, [
        ("LEM-SPECCONS states", "LEM-SPECCONS (`TDRG-ALG-LEM-SPECCONS`) states"),
        (r"Equivalently, the multiset of orbit-lattice spacings $\{\gcd(d_{ij},N)\}$ is conserved.",
         r"In particular, the multiset of orbit-lattice spacings $\{\gcd(d_{ij},N)\}$ is conserved; this is a consequence only — the converse fails (owner counterexample at $N=24$: $|d|_c=1$ and $|d|_c=5$ share $\gcd=1$)."),
    ])),
    ("E33", "23", "str", (279, [(
        "`[ALG/NUM strong in source]` `[scope: N=24,k=1; no-birth/three-node]`",
        "`[ALG/NUM strong in source]` `[scope: N=24,k=1; no-birth/three-node]` `[conv: v18 path orientation]` (owner RIDs: `TDRG-ALG-BIND3-CYCLE-N24K1`; `TDRG-NUM-BIND3-PARITY`, `TDRG-NUM-BIND3-SPECTRAL-GATE`, `TDRG-NUM-BIND3-MEMORY-PARITY`, `TDRG-NUM-BIND3-XFER`, `TDRG-NUM-BIND3-REGEN`; these numbers were computed with the orientation completion the owner has since superseded and are not rerun by the owner)")])),
    ("E34", "4", "str", (281, [("TDR-G v2.12 reports", "TDR-G v2.12.14 reports")])),
    ("E35", "24", "line", (283, "at fixed $k/N=1/15$, $T=5000$, over $N=120$–$1440$, excluding tail runs $M>500$.",
        r"at fixed $k/N=1/15$, $T=5000$, over $N=120$–$1440$, excluding tail runs $M>500$ (full-range composite fit). The exponent is window-dependent: read on $N=480$–$1440$ the same scan gives $N^{-0.730}$, and $-0.869$ is the owner's full-range value, not a structural constant. Thermodynamic crystallization in the $N\to\infty$ limit is a `[HEUR]` extrapolation in the source, not theorem-grade. `[NUM]` (fit) / `[HEUR]` (limit) in source `[conv: v18 path orientation]` `[source: " + TDRG + " v2.12.14 §1; TDRG-OPEN-NSCALING, TDRG-OPEN-CRYSTALLIZATION]`")),
    ("E36", "4,26", "str", (285, [
        ("Discrete Genesis v2.12 records", "Discrete Genesis v2.12.14 records (OPEN TDR-26, `TDRG-OPEN-LOCKING-FAIL`)"),
        ("`[source: " + TDRG + "_v2.12 TDR-26]`", "`[source: " + TDRG + " v2.12.14 §2 OPEN TDR-26]`"),
    ])),
    ("E37", "25", "line", (287, "`[bridge-candidate]` **TDR-24 frontier.** The immediate discrete frontier is the TDR-24 derivation chain: slot-volume identity, topological filtering, and geometric compression.",
        "`[bridge-candidate]` **TDR-24 frontier.** The immediate discrete frontier is the TDR-24 derivation chain. In TDR-G v2.12.14 the slot-volume identity (TDR-24D) and the structural-to-slot projection (TDR-24F) are closed at the mechanism level, with their analytic constants open; the gate before discrete triadic dynamics is TDR-24A (topological filtering, `TDRG-OPEN-TOPO-FILTER`) → TDR-24B (pair-to-component compression, `TDRG-OPEN-CHI-SCALING`) → TDR-24C (thermodynamic suppression, `TDRG-OPEN-THERMO-SUPPRESS`). This DSN may track arithmetic/zeta observables that could assist TDR-24 or future OPEN-P1, but cannot promote them without source-DSN closure and bridge routing.")),
    # ---- §5 -----------------------------------------------------------------
    ("E38", "4", "str", (410, [("from Discrete Genesis v2.12 |", "from Discrete Genesis v2.12.14 |")])),
    # ---- §6 -----------------------------------------------------------------
    ("E39", "3,11,13", "line", (427, "Thread A collects the current Dyadic arithmetic horizon as an import-ref ledger from `" + DYAD + "_v6.4.8.1`.",
        r"Thread A collects the current Dyadic arithmetic horizon as an import-ref ledger from `" + DYAD + r"` v6.4.23. The active arithmetic frontier listed in §4.1.2 is: universal missing-slot rules, bridge-gap smooth baseline, near-cancellation structure, all-$b\ge5$ persistence/general-coefficient extension, and the universal $\nu_5^{(p)}$ theorem; the exact cubic cascade formula for $q=4,(0,3)$ is closed in Dyadic (`DYAD-THM-Q403-PHASELAW`). The owner's current list is Dyadic §2 OPEN 9.")),
    ("E40", "5,29", "str", (437, [(
        r"Genesis v2.8.4 closes OPEN 1C and certifies that the $\mathcal{P}_4$-only cascade is impossible in the reduced birth-race model; the cascade question routes through OPEN M.",
        r"In Genesis v2.10, OPEN 1C (triad chiral admissibility surface, `GEN-OPEN-CHIRAL-ADMISS`) is closed `[THM]`. Separately, within OPEN 1 (`GEN-OPEN-PHASE-DIST`, active) the $\mathcal{P}_4$-only cascade is impossible `[RESULT]` `[scope: reduced birth-race model]` — a statement about the reduced model, not about arbitrary phase measures; cascade then requires a non-$\mathcal{P}_4$ source, and the question routes through OPEN-GEN-II-7B (`GEN-OPEN-UVJET-ALPHAF`) and OPEN M.")])),
    ("E41", "1,6", "line", (440, "`[bridge-candidate]` The $p=6/K_4$ face-flux identity $\\lambda=e^{iF_f/2}$ is a Dyadic import-ref.",
        r'''`[bridge-candidate]` The $p=6/K_4$ face-flux identity $\lambda=e^{iF_f/2}$ is a Dyadic import-ref. The SU(2) energy ratio $E_{\rm full}/E_{\rm half}=4$ is source-scoped, and the OPEN-M cascade test is linear in the admitted source amplitude $\|H\|_B$. OPEN-M v0.7.1 certifies no numerical deficit factor: R16 (`UVM-RESULT-AUDIT1`, `[COR]`) withdraws the earlier "legal SU(2) correction $=2\times$" as a physical conclusion — the $2\times$ branch is conditional on two unproved bridges (the source identification and an $E\propto A^2$ constitutive relation), and the $4\times$ energy factor is likewise not directly admissible in the amplitude-linear inequality — and R15 (`UVM-NUM-2F-RHO`) is a calibration-conditional proxy diagnostic. No arithmetic-horizon or graph-zeta result in this DSN contributes to or supersedes that verdict. `[source: RTG_OPEN_M_DSN v0.7.1 R15, R16]` `[SG-AZ-6, SG-PROG-4]`''')),
    ("E42", "28", "line", (443, "This study is a Tier 5 infrastructure entry. The Programme Overview should be updated to register",
        "This study is a Tier 5 infrastructure entry and is registered in Programme Overview v1.4 (its §6.1, §6.5 and §7.2). See §7.")),
    # ---- §7 -----------------------------------------------------------------
    ("E43", "2,28", "block", (449, 471, "`[DEF]` The Programme Overview `RTG_PROGRAMME_OVERVIEW_v1.1` should be patched", "Also: in the cross-study dependency graph,", [
        "`[DEF]` This study is registered in `RTG_PROGRAMME_OVERVIEW` v1.4 (`programme-v1.4`): the document inventory (its §6.1; Tier 5, canonical infrastructure), the study entry (its §6.5), the cross-study dependency graph (its §7.1; a reference edge from Dyadic to Thread A and an edge from TDR-G to Threads B/C) and the interface register (its §7.2; IF20 Dyadic → AZ, reference-only, and IF21 TDR-G → AZ). The request carried through v0.6 that the Programme Overview be patched to register this study is met and closed; the proposed entry text is removed. The Programme's maintenance proposals for this study (its §6.7 and §9.2) are Programme records and are not adopted by this edition.",
    ])),
    # ---- §8 Import Ledger ---------------------------------------------------
    ("E44", "3", "str", (477, [("owned by `" + DYAD + "_v6.4.8.1`.", "owned by `" + DYAD + "` v6.4.23.")])),
    ("E45", "3", "line", (479, "### Reference imports from `" + DYAD + "_v6.4.8.1`",
        "### Reference imports from `" + DYAD + "` v6.4.23 (`dyad-v6.4.23`)")),
    ("E46", "9", "line", (481, "- [RID: DYAD-THM-RAW-CUBIC] :: Raw cubic theorem :: `[import-ref]` `[THM]`",
        r"- [RID: DYAD-THM-RAW-CUBIC] :: Raw cubic theorem (raw one-step map, $p\ge3$; owner caveat on the historical proposition) :: `[import-ref]` `[THM]`")),
    ("E47", "16", "line", (484, "- [RID: DYAD-OPEN-P-RESONANCE — sub-items] ::",
        r"- [RID: DYAD-OPEN-P-RESONANCE] (named sub-items of the owner's OPEN 9 record; the sub-labels are not identifiers) :: $G_{04}(10)=0$ reinterpretation; $p=12$ cascade boundary; $p=7$ transparency `[FAIL]`; universal $q=4,(0,3)$ `[FAIL]`; subgroup-projector/missing-slot formalism; cardinality lemma $|K^{\rm extra}_{p,q}|=s-1$ `[ALG]` :: `[import-ref]`")),
    ("E48", "10,16", "line", (488, "- [RID: DYAD-OPEN-P-RESONANCE — b-boundary] :: vanishing iff $b\\le4$",
        r"- [RID: DYAD-ALG-B5-ALLP-NONVANISHING] :: channel boundary at $b=4$: vanishing for $b\in\{2,3,4\}$, failure at $b=5$ for every $p\ge6$ :: `[import-ref]` `[ALG]` :: dyadic-map scope; all-$b\ge5$/general-coefficient `[OPEN]`; `DYAD-OPEN-B5-ALLP` is the closed lifecycle identifier")),
    ("E49", "14", "str", (491, [("[RID: DYAD-ALG-Q3-CANCEL]", "[RID: DYAD-ALG-Q3-DEG2-CANCEL]")])),
    ("E50", "16", "delete", (492, "- [RID: DYAD-OPEN-P-RESONANCE — subgroup cardinality] ::")),
    ("E51", "11", "after", (493, "- [RID: DYAD-ALG-P6-FACEFLUX] ::", [
        r"- [RID: DYAD-THM-Q403-PHASELAW] :: cubic cascade $q=4,(0,3)$ phase/factorization law, $p=4s$, $s\ge2$ :: `[import-ref]` `[THM]`",
    ])),
    ("E52", "4", "line", (495, "### Branch-local context from `" + TDRG + "_v2.12`",
        "### Branch-local context from `" + TDRG + "` v2.12.14 (`tdrg-v2.12.14`)")),
    ("E53", "19,20,21,22,23,24,25,26", "block", (497, 503, "- [RID: TDRG-ZN-STATE] ::", "- [RID: TDR-26-BIRTH-ANCHOR] ::", [
        r"- [RID: TDRG-DEF-ZN-STATE] :: $\mathbb{Z}_N$ phase universe, variable-size state :: `[bridge-candidate]` :: the consumer name `TDRG-ZN-STATE` resolves to it through the owner's §7 map",
        r"- [RID: TDRG-DEF-PHYSICAL-STATE] :: physical state as the quotient by global phase shift; relational phases $\Delta_{ij}$ (absolute-phase gauge) :: `[bridge-candidate]`",
        r"- [RID: TDRG-DEF-BAND] :: defect band $\mathcal{D}_k$ :: `[bridge-candidate]`",
        r"- [RID: TDRG-ALG-LEM-REACH] :: band-form reachability/superselection ($k=0$: `TDRG-THM-REACHABILITY-K0`) :: `[bridge-candidate]` `[THM/ALG in source]`",
        "- [RID: TDRG-ALG-LEM-RETRIG] :: two-node retrigger threshold; bound state of period dividing 2 :: `[bridge-candidate]` `[ALG in source]`",
        "- [RID: TDRG-ALG-LEM-SPECCONS] :: three-node no-birth advance-spectrum conservation; the gcd multiset as a consequence only :: `[bridge-candidate]` `[ALG in source]`",
        "- [RID: TDRG-ALG-BIND3-CYCLE-N24K1; TDRG-NUM-BIND3-PARITY; TDRG-NUM-BIND3-SPECTRAL-GATE; TDRG-NUM-BIND3-MEMORY-PARITY; TDRG-NUM-BIND3-XFER; TDRG-NUM-BIND3-REGEN; TDRG-OPEN-BIND3-NKSCAN] :: cycle enumeration / NKSCAN; survival parity, spectral gate, even-sector memory correction :: `[bridge-candidate]` `[ALG/NUM strong in source]` `[conv: v18 path orientation]`",
        r"- [RID: TDRG-OPEN-NSCALING; TDRG-OPEN-CRYSTALLIZATION; TDRG-OPEN-TOPO-FILTER; TDRG-OPEN-CHI-SCALING; TDRG-OPEN-THERMO-SUPPRESS] :: $k/N$ growth control, `bound_symmetric` full-range $N^{-0.869}$ fit (window-dependent exponent), crystallization `[HEUR]`, TDR-24A → 24B → 24C gate :: `[bridge-candidate]`",
        r"- [RID: TDRG-OPEN-LOCKING-FAIL] :: OPEN TDR-26 birth-anchored discriminator over $[\mathrm{fb},\mathrm{fb}+200)$, $N=720,722$ :: `[bridge-candidate]` `[NUM cross-cell, n=2; classifier HEUR]`",
    ])),
    # ---- §9 -----------------------------------------------------------------
    ("E54", "31", "line", (516, "**Current status (v0.6):** the engine and Phase-2 artifacts are real and named.",
        "**Current status (v0.7):** the engine and Phase-2 artifacts are named below by RID. **Availability:** none of these files, including the hash registry `AZ-ART-AZV5-REGISTRY`, is in the repository as of this edition, and they are not described as recreated. The certifications and hashes are therefore source-reported from the June 2026 Thread C work (`EV-SRC-REPORTED`), and nothing was rerun for this edition (`EV-NOT-RERUN`). This DSN lists RID-level artifact identities and points to that registry and the per-result artifact manifests as the hash source rather than duplicating hashes inline; SG-AZ-5 provenance is by pointer to that manifest and cannot be inspected from the repository until the files are supplied unchanged and hash-checked against the registry. The existing grades are kept with this verification limit; it applies wherever this document calls a Thread C artifact hashed or certified (§4.3.1, §5). The prior `v3 historical / v4,v5 planned` placeholder registry is superseded.")),
    # ---- §10, Appendix A, Appendix B, footer ----------------------------------
    ("E55", "edition", "after", (533, "", [
        "- **November 2026 — v0.7 corrections edition.** Prepared from v0.6 (tag `az-v0.6`) against the current adopted owner editions (Dyadic v6.4.23, TDR-G v2.12.14, Genesis v2.10, Programme v1.4, OPEN-M v0.7.1), limited to list (i) of `records/az/AZ_REACTIVATION_TRIAGE.md` as decided by the PI on 10 Nov 2026. No new science and no Thread C change; edit-level record in `records/az/AZ_v0_7_RELEASE_RECORD.md`.",
    ])),
    ("E56", "edition", "after", (543, "", [
        "### v0.7 — November 2026",
        "",
        "Corrections only over v0.6 (tag `az-v0.6`). No new scientific claim; no grade change of an AZ-owned result; Thread C (§4.3) unchanged. Edit-level record: `records/az/AZ_v0_7_RELEASE_RECORD.md`.",
        "",
        "- **Header [COR]:** Version → v0.7; Supersedes → v0.6 with its hash; companion documents repinned to the governing editions. DSN Methodology v1.2 stays declared (v1.4 governs; the migration is a separate edition).",
        "- **Pins [COR]:** Programme v1.1 → v1.4; Dyadic v6.4.8.1 → v6.4.23; TDR-G v2.12 → v2.12.14; Genesis v2.8.4 → v2.10; OPEN-M v0.6 → v0.7.1.",
        "- **§3 [COR]:** SG-PROG-1/2/4 cited by pointer to Programme v1.4 §8 with this study's application; the v1.1 wording is no longer quoted.",
        r'''- **§1.2 / §4.1 [COR]:** raw cubic theorem restated at the owner's scope (raw one-step map, $p\ge3$, owner caveat); the "iff $b\le4$" wording removed; cubic cascade $q=4,(0,3)$ registered as closed (`DYAD-THM-Q403-PHASELAW`) and removed from the open frontier; sign of the $p=12$ value in §4.1.2; $\mathbb{Q}(\zeta_5)$ field label; `DYAD-ALG-Q3-CANCEL` → `DYAD-ALG-Q3-DEG2-CANCEL`; `DYAD-ALG-B5-ALLP-NONVANISHING` cited for the $b=5$ result; owner evidence boundary recorded for the eigenframe lemma and eight projector objects; source pointers corrected; the frontier list points to Dyadic §2 OPEN 9.''',
        "- **§4.2 [COR]:** owner RIDs cited; LEM-RETRIG \"period dividing 2\"; LEM-SPECCONS gcd multiset as a consequence only; BIND3 and N-scaling carry `[conv: v18 path orientation]`; N-scaling exponent window-dependent and crystallization `[HEUR]`; TDR-24D/F closed at mechanism level, gate TDR-24A → 24B → 24C; TDR-26 cited as `TDRG-OPEN-LOCKING-FAIL`.",
        "- **§6 [COR]:** \"To OPEN M\" rewritten against OPEN-M v0.7.1 R15/R16 (Appendix B); Genesis OPEN 1C and the reduced-model $\\mathcal{P}_4$ statement cited as two entries of Genesis v2.10; Dyadic frontier sentence synchronized.",
        "- **§0.1 / §6 / §7 [COR]:** the Programme Overview registration is recorded as met; the patch request and the proposed entry text are removed.",
        "- **§8 [COR]:** Import Ledger rows carry the owner RIDs and editions; the `DYAD-OPEN-P-RESONANCE` sub-labels are no longer printed as identifiers.",
        "- **§9 [COR]:** availability of the Thread C files stated (`EV-SRC-REPORTED`, not in the repository, `EV-NOT-RERUN`); the present-tense \"provenance is satisfied\" claim replaced.",
        "",
    ])),
    ("E57", "1", "after", (596, "`[RETRACTED]` predicted weakening of the `4|q` rule with larger $k/N$", [
        "",
        "### Corrections registered at v0.7",
        r'''`[COR]` §6 "To OPEN M" (as printed in v0.6): "the legal correction is $\times2$, not $\times4$; applying $\times4$ is a certified dimensional type error under AUDIT-1-DIMENSIONAL in the OPEN-M ledger." Withdrawn as a current statement. Reason: OPEN-M v0.7.1 R16 (`UVM-RESULT-AUDIT1`) withdrew the "legal $2\times$" verdict as a physical conclusion and records that no certified numerical deficit factor exists. Replacement: §6 "To OPEN M". The sentence reported an owner reading; it was never an AZ result, and no AZ grade depended on it.''',
    ])),
    ("E58", "edition", "line", (600, "*END OF DOCUMENT — RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN_v0.6*",
        "*END OF DOCUMENT — RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN_v0.7*  ")),
    ("E59", "edition", "str", (601, [("*Supersedes v0.5. Infrastructure and ledger document.",
        "*Supersedes v0.6 (corrections only; no new science). Infrastructure and ledger document.")])),
]

# Base regions that must come through byte-identical (AZ-owned content).
PROTECTED = [
    (119, 148, "§2 Active Frontier / OPEN Registry"),
    (159, 196, "§3 SG-AZ guards"),
    (297, 401, "§4.3 Thread C"),
    (582, 596, "Appendix B entries registered through v0.6"),
]

# Strings that may survive only in the dated history lines of the base.
STALE = [
    r"v6\.4\.8\.1", r"DSN_v2\.12(?!\.14)", r"Genesis v2\.12(?!\.14)", r"TDR-G v2\.12(?!\.14)",
    r"v2\.8\.4", r"OVERVIEW_v1\.1", r"OPEN_M_DSN_v0\.6", r"DYAD-ALG-Q3-CANCEL\b",
    r"TDR-26-BIRTH-ANCHOR", r"\[RID: TDRG-ZN-STATE\]", r"\[RID: LEM-", r"\[RID: BIND3-\*\]",
    r"TDR-24 / N-SCALING", r"(holds|vanishing) iff", r"the legal correction is",
    r"Equivalently, the multiset", r"period-2 retrigger", r"cannot self-register", r"should be patched",
    r"provenance is satisfied", r"p\$-step map is exact",
]
# The v0.7 Appendix A entry and Appendix B correction name what was replaced.
RECORD_EDITS = ("E56", "E57")
TEXT_REMOVAL_EDITS = ("E43",)
# Edits that change or move a tag on purpose. All three concern owner tags of
# imported statements, none an AZ grade:
#   E35, E53  TDR-G v2.12.14 retagged its N-scaling fit [NUM] and the
#             crystallization limit [HEUR] (were "[NUM strong]" / "[HEUR strong]");
#   E50       the cardinality-lemma row is deleted and its [ALG] moves into E47.
TAG_CHANGE_EDITS = ("E35", "E50", "E53")
HISTORY_BASE_LINES = (111, 537, 572)  # §1.3 milestone AZ-0, §10 v0.3 entry, Appendix A v0.3


def sha(b):
    return hashlib.sha256(b).hexdigest()


def build(base_bytes):
    assert sha(base_bytes) == BASE_SHA256, "base is not the adopted az-v0.6 file"
    text = base_bytes.decode("utf-8")
    assert text.endswith("\n"), "base must end with a newline"
    lines = text[:-1].split("\n")
    n = len(lines)
    repl, insert, log, used = {}, {}, [], set()

    def claim(i):
        assert 1 <= i <= n, i
        assert i not in used, "two edits touch base line %d" % i
        used.add(i)

    for eid, rows, kind, arg in EDITS:
        assert rows, eid
        if kind == "line":
            i, prefix, new = arg
            claim(i)
            assert lines[i - 1].startswith(prefix), (eid, lines[i - 1][:80])
            old, repl[i] = [lines[i - 1]], [new]
            newl = [new]
        elif kind == "str":
            i, pairs = arg
            claim(i)
            cur = lines[i - 1]
            for a, b in pairs:
                assert cur.count(a) == 1, (eid, a[:60], cur.count(a))
                cur = cur.replace(a, b)
            old, repl[i] = [lines[i - 1]], [cur]
            newl = [cur]
        elif kind == "block":
            a, b, pa, pb, new = arg
            for i in range(a, b + 1):
                claim(i)
            assert lines[a - 1].startswith(pa), (eid, lines[a - 1][:80])
            assert lines[b - 1].startswith(pb), (eid, lines[b - 1][:80])
            old = lines[a - 1:b]
            repl[a] = list(new)
            for i in range(a + 1, b + 1):
                repl[i] = []
            newl = list(new)
        elif kind == "after":
            i, prefix, new = arg
            assert i not in insert, (eid, i)
            assert lines[i - 1].startswith(prefix), (eid, lines[i - 1][:80])
            if prefix == "":
                assert lines[i - 1] == "", (eid, "expected a blank line at %d" % i)
            insert[i] = list(new)
            old, newl = [], list(new)
        elif kind == "delete":
            i, prefix = arg
            claim(i)
            assert lines[i - 1].startswith(prefix), (eid, lines[i - 1][:80])
            old, repl[i], newl = [lines[i - 1]], [], []
        else:
            raise AssertionError(kind)
        base_lines = arg[0] if kind != "block" else [arg[0], arg[1]]
        log.append({
            "id": eid, "triage_rows": rows, "kind": kind, "base_lines": base_lines,
            "old": old, "new": newl,
            "old_sha256": sha("\n".join(old).encode()), "new_sha256": sha("\n".join(newl).encode()),
        })

    out = []
    for i in range(1, n + 1):
        out.extend(repl.get(i, [lines[i - 1]]))
        out.extend(insert.get(i, []))
    cand = ("\n".join(out) + "\n").encode("utf-8")
    return cand, log, lines


def gates(base_bytes, cand_bytes, log):
    res = []
    built, built_log, base_lines = build(base_bytes)
    res.append(("G1 BUILD (candidate equals the build from the tag)", built == cand_bytes))
    res.append(("G2 LOG (edit log equals the build's log)", built_log == log))
    cand = cand_bytes.decode("utf-8")
    ok = all(("\n".join(base_lines[a - 1:b]) + "\n") in cand for a, b, _ in PROTECTED)
    res.append(("G3 PROTECTED (%d AZ-owned regions byte-identical)" % len(PROTECTED), ok))
    hist = {base_lines[i - 1] for i in HISTORY_BASE_LINES}
    for e in built_log:
        if e["id"] in RECORD_EDITS:
            hist.update(e["new"])
    hits = []
    for ln in cand.split("\n"):
        if ln in hist:
            continue
        for pat in STALE:
            if re.search(pat, ln):
                hits.append((pat, ln[:90]))
    res.append(("G4 STALE (no superseded pin, identifier or sentence outside the history lines)", not hits))
    # No edit may drop an AZ-owned identifier or an AZ grade/status tag from the
    # text it replaces. The one exception is E43, which removes the proposed
    # Programme entry text of the old section 7 (mentions only, no declaration).
    id_pat = r"\b(?:AZ-[A-Z0-9][A-Z0-9-]*|PROP-AZ-[A-Z-]+|TDRG-AZ-[A-Z0-9-]+|SG-AZ-[0-9.]+|DEF-AZ-[A-Z]+|CONV-AZ-[A-Z-]+)"
    tag_pat = r"\[(?:THM-ALG|ENG PASS|NUM diagnostic|HEUR/NUM strong|RETRACTED|bridge-disqualified|ALG|THM|FAIL|OPEN|HEUR|NUM)[^\]]*\]"
    lost_ids, lost_tags = [], []
    for e in log:
        old, new = "\n".join(e["old"]), "\n".join(e["new"])
        d = Counter(re.findall(id_pat, old)) - Counter(re.findall(id_pat, new))
        t = Counter(re.findall(tag_pat, old)) - Counter(re.findall(tag_pat, new))
        if d and e["id"] not in TEXT_REMOVAL_EDITS:
            lost_ids.append((e["id"], dict(d)))
        if t and e["id"] not in TEXT_REMOVAL_EDITS and e["id"] not in TAG_CHANGE_EDITS:
            lost_tags.append((e["id"], dict(t)))
    res.append(("G5 OWNED-IDS (no edit drops an AZ-owned identifier; E43 removes proposal text only)", not lost_ids))
    res.append(("G6 TAGS (no edit drops a grade or status tag except the declared owner-tag changes)", not lost_tags))
    hits = hits + [("lost", x) for x in lost_ids + lost_tags]
    res.append(("G7 ROWS (every edit names its triage row)", all(e["triage_rows"] for e in log)))
    return res, hits


def main(argv):
    if len(argv) < 4:
        print(__doc__)
        return 2
    base = open(argv[1], "rb").read()
    if "--check" in argv or "--controls" in argv:
        cand = open(argv[2], "rb").read()
        log = json.load(open(argv[3], encoding="utf-8"))["edits"]
        if "--controls" in argv:
            bad = 0
            ctrl = [
                ("K1 withdrawn ×2 sentence restored", cand.replace("OPEN-M v0.7.1 certifies no numerical deficit factor".encode(), "the legal correction is $\\times2$, not $\\times4$; applying it".encode(), 1)),
                ("K2 old Dyadic pin restored in one place", cand.replace(b"`RTG_DYADIC_OSCILLATOR_DSN` v6.4.23 (`dyad-v6.4.23`), ", b"`RTG_DYADIC_OSCILLATOR_DSN_v6.4.8.1`, ", 1)),
                ("K3 unlogged change inside Thread C", cand.replace("**Status (v0.6):** Engineering **CERTIFIED**".encode(), "**Status (v0.7):** Engineering **CERTIFIED**".encode(), 1)),
                ("K4 unlogged removal of an AZ grade tag (header)", cand.replace(b"[THM-ALG]", b"[ALG]", 1)),
            ]
            for name, mutated in ctrl:
                assert mutated != cand, name
                r, _ = gates(base, mutated, log)
                failing = [g for g, okk in r if not okk]
                print("[%s] %s: failing gates %s" % ("CAUGHT" if failing else "MISSED", name, [g.split(" ")[0] for g in failing]))
                bad += 0 if failing else 1
            print("CONTROLS: %s" % ("PASS (all caught)" if not bad else "FAIL"))
            return 1 if bad else 0
        r, hits = gates(base, cand, log)
        for g, okk in r:
            print("[%s] %s" % ("PASS" if okk else "FAIL", g))
        for h in hits:
            print("   stale:", h)
        npass = sum(1 for _, okk in r if okk)
        print("candidate sha256 %s" % sha(cand))
        print("RESULT: %s (%d/%d gates)" % ("PASS" if npass == len(r) else "FAIL", npass, len(r)))
        return 0 if npass == len(r) else 1
    cand, log, _ = build(base)
    open(argv[2], "wb").write(cand)
    json.dump({"base_sha256": BASE_SHA256, "candidate_sha256": sha(cand), "edits": log},
              open(argv[3], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("edits %d; candidate sha256 %s" % (len(log), sha(cand)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
