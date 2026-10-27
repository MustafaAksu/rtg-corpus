#!/usr/bin/env python3
r"""Discrete Genesis (TDR-G) v2.12.14 — corrections-only build (one stage; no layout change).

Applies, to the adopted v2.12.13 file (tag tdrg-v2.12.13, sha256 aa232643...053f), the corrections fixed by the owner
dispositions and the PI's "başla" (27 Oct 2026):
  records/tdrg/TDRG_OWNER_DISPOSITION_ADVISORY_v2_12_13_claude01SKePJ_20261027.md (PR #89),
  records/tdrg/TDRG_OWNER_DISPOSITION_ADVISORY_v2_12_13_chatgpt_20261027.md (PR #88, post-peer addendum),
  records/tdrg/TDRG_OWNER_DISPOSITION_RECONCILIATION_v2_12_13.md (PR #91; fixed dispositions §3),
  records/tdrg/ATLAS_ADVISORY_TDRG_v2_12_13_RECONCILIATION.md §3 (the 18-row list) and §5 (PI decisions).

Row groups (labels only; every edit is applied):
  TA01  orientation rule (option (b)), no-go remark, recorded G alternative, policy-table column, App. B row
  TA02  signed_centered / signed_defect_error definitions
  TA03  SG-14 (covariance group; token shift and mirror outside; largest_center exception)
  TA08  §6.12 mirror-inventory wording; orientation-covariance block (fixture, equivariance, census, DISC-2, N2)
  TC14  DISC-2 witness-effect statement (in the §6.12 block) and the NUMGEN consumer row (§7)
  TA05  LEM-RETRIG least period (§1, §6.5, regime table, §5)
  TA06  LEM-SPECCONS "therefore, in particular"
  TA04  N-scaling range tags, grades, chi=0.836 consistency line withdrawn, crystallization HEUR
  I07   §1/§2/§5/App. C current state of the TDR-24 chain; TDR-24B current-status line
  TA07  K3 96:1 and T-6 wedge marked historical
  TB09  claim RIDs (39 declarations) and the owner RID map
  TB11  §8 custody register
  TB10  header pins, §7 imports / consumers / pins, §9 repository
  TB12  compound tags unpacked; local alias table replaced
  TB13  header title/date/supersedes, status summary, App. A entry for v2.12.14, footer title line
  TC16  AZ cross-citation at narrow-band exclusion (with the I12 scope sentence)
  TC17  Programme v1.2 owner-review tasks in §2
  N1    largest_center equal-degree ID tie-break (§6.6); v18-orientation guard on §§6.6–6.10
  N2    mirror not a step symmetry (§6.12)
  XFER  OFN Finding A statement accepted, custody deferred (§7)
Not edited: every scientific number; Appendix A history entries; the footer supersession chain beyond its first line;
Appendix A ordering (v2.13 layout work); the historical claim-specific pins (OFN v0.6 at TDR-1/TDR-19).

Rules:
- the input must be the adopted v2.12.13 bytes;
- mode "line": `old` is a line prefix that must start exactly one line; the whole line is replaced by `new`
  (a string, or a function of the old line);
- mode "str": `old` is an exact substring that must occur exactly once in the whole document; `new` replaces it;
- every new text must occur exactly once in the candidate (so the checker can undo the log in reverse order).

usage: build_tdrg_v2_12_14.py BASE OUT EDITLOG_JSON
  BASE = `git show tdrg-v2.12.13:dsn/RTG_DISCRETE_GENESIS_DSN.md`
"""
import hashlib, json, sys

BASE_SHA = "aa232643f6f631694b0eda1532be213e5a517ef109cd66794f8e638e24fc053f"
BASE_TAG = "tdrg-v2.12.13"
CHECK_SCRIPT = "evidence/tdrg/scripts/check_tdrg_v2_12_14.py"

NEW_RIDS = [
    # definitions consumed by OFN / NUMGEN / AZ first
    "TDRG-DEF-ZN-STATE", "TDRG-DEF-PHYSICAL-STATE", "TDRG-DEF-REL-ADVANCE", "TDRG-DEF-KINEMATICS", "TDRG-DEF-BAND",
    "TDRG-DEF-EDGE-SET", "TDRG-DEF-NARROW-BAND", "TDRG-DEF-CONV-TICK", "TDRG-DEF-SWAP", "TDRG-DEF-CONV-P3CYC",
    "TDRG-DEF-SIGNED-CENTERED", "TDRG-DEF-SIGNED-DEFECT-ERROR", "TDRG-DEF-ORIENT", "TDRG-DEF-CYCLE-BOUND",
    "TDRG-DEF-STAR", "TDRG-DEF-MULTISTAR", "TDRG-DEF-CANONICAL-BRANCH",
    # theorems
    "TDRG-THM-HOLONOMY", "TDRG-THM-NARROW-BAND-EXCLUSION", "TDRG-THM-RECURRENCE", "TDRG-THM-REACHABILITY-K0",
    # lemmas and exact results
    "TDRG-ALG-LEM-REACH", "TDRG-ALG-LEM-NOANNIHIL", "TDRG-ALG-LEM-RETRIG", "TDRG-ALG-LEM-SPECCONS",
    "TDRG-ALG-ORIENT-NOGO", "TDRG-ALG-LARGEST-CENTER-ID-TIEBREAK", "TDRG-ALG-ORIENT-ANTIPODAL-FIXTURE",
    "TDRG-ALG-MIRROR-NOT-STEP-SYMMETRY", "TDRG-ALG-BIND3-CYCLE-N24K1",
    # numerical results
    "TDRG-NUM-BIND3-PARITY", "TDRG-NUM-BIND3-SPECTRAL-GATE", "TDRG-NUM-BIND3-MEMORY-PARITY", "TDRG-NUM-BIND3-XFER",
    "TDRG-NUM-BIND3-REGEN", "TDRG-NUM-ORIENT-EQUIVARIANCE-N24",
    # artifacts
    "TDRG-ART-SESSION-SCRIPTS", "TDRG-ART-ORIENT-V2-12-14", "TDRG-ART-ORIENT-COVARIANCE-CHECKS",
]

def rid(r):
    assert r in NEW_RIDS, r
    return f"[RID: {r}]"

# ------------------------------------------------------------------------------------------------ texts
H_TITLE = "# RTG_DISCRETE_GENESIS_DSN_v2.12.14"
H_DATE = "**Date:** October 2026 (v2.12.14, corrections only; the scientific content of the v2.12 line is dated June 2026)  "
H_SUPERSEDES = ("**Supersedes:** `RTG_DISCRETE_GENESIS_DSN_v2.12.13` (tag `tdrg-v2.12.13`, SHA-256 "
                "`aa232643f6f631694b0eda1532be213e5a517ef109cd66794f8e638e24fc053f`); the earlier lineage is in the footer "
                "and Appendix A (compaction is v2.13 work)  ")
H_COMPANION = ("**Companion documents (governing editions, October 2026):** Programme Overview v1.3 (`programme-v1.3`) · "
               "Ontological Foundations v0.10 (`ofn-v0.10`) · DSN Methodology v1.4 (`methodology-v1.4`). Claim-specific "
               "historical pins (Programme v1.1, OFN v0.6/v0.7) stay where a statement cites them.  ")
H_METH = ("**DSN Methodology:** DSN_METHODOLOGY_v1.2 (declared; kept for this corrections edition by PI decision of "
          "27 Oct 2026 — the v1.4 migration is v2.13)  ")

SS_OLD = ("(v17/v6 canonical scan, $N=120$–$1440$), strongly supporting thermodynamic crystallization in the $N\\to\\infty$ "
          "limit. The immediate frontier is the TDR-24 derivation chain (slot-volume identity, topological filtering, "
          "geometric compression), which must close before discrete triadic dynamics can be studied.")
SS_NEW = ("(v17/v6 canonical scan, full-range fit $N=120$–$1440$; the exponent is window-dependent, §1); thermodynamic "
          "crystallization in the $N\\to\\infty$ limit is a `[HEUR]` extrapolation. TDR-24D and TDR-24F are closed at the "
          "mechanism level with their analytic constants OPEN; the gate before discrete triadic dynamics is "
          "TDR-24A → TDR-24B → TDR-24C.")
SS_BIND_OLD = "exact cycle enumeration BIND3-CYCLE-N24K1 `[ALG/NUM strong]` establishing"
SS_BIND_NEW = "exact cycle enumeration BIND3-CYCLE-N24K1 (`[ALG]`, finite exact enumeration) establishing"
SS_END_OLD = "New scope guards SG-11–SG-13; new §6.12."
SS_END_NEW = ("New scope guards SG-11–SG-13; new §6.12. **v2.12.14 (corrections only):** the path orientation rule "
              "TDRG-DEF-ORIENT is made node-relabelling covariant by extending the balanced path-tie to "
              "$S=0\\wedge 2E\\equiv0 \\pmod N$, with the covariance group named in SG-14; `signed_centered` and "
              "`signed_defect_error` are defined; claim RIDs are registered (§7 owner RID map); results computed with the "
              "superseded completion keep `[conv: v18 path orientation]` and `EV-NOT-RERUN` (census bound, §6.12).")

ALIAS_OLD = ("| `[ALG/NUM]` | `[ALG]` co-certified with `[NUM]` | exact identity cross-verified numerically |\n"
             "| `[ENG/ALG]` | `[ENG]` with `[ALG]`-grade audit | implementation verified against exact reference |\n"
             "| `[NUM-strong]` | `[NUM strong]` | legacy alias; replace on next edit |\n"
             "| `[HEUR-strong]` | `[HEUR strong]` | legacy alias; replace on next edit |\n\n"
             "`[DEF]` New ledger entries must use canonical forms from `DSN_METHODOLOGY_v1.2`. Legacy aliases are accepted "
             "only during migration.")
ALIAS_NEW = ("| `[INTERP]` | `[HEUR]` [scope: interpretation] | interpretive reading of a stated result |\n"
             "| `[REVISED]` | `[COR]`; the revised assertion carries its own tag | in-place revision notes |\n"
             "| `[REJ]` | `[FAIL]` [scope: the item as stated] | rejected candidate inside an OPEN record |\n"
             "| `[REPLACED]` | `[SUPERSEDED]` with the replacement pointer | BIND3-KNIFE |\n"
             "| `[ENG audit: PASS]` | `[ENG]` [scope: the named conformance audit] | CONV-TICK |\n"
             "| `[NUM exhaustive: …]` | evidence note: exhaustive finite verification over the stated range | lemma certificates |\n"
             "| `[SCOPE …]`, `[ADMIN …]`, `[METHOD]`, `[BRANCH …]` | prose labels (scope, administrative or tooling, method, "
             "exploratory-branch notes); not truth tags | §2 |\n\n"
             "Canonical tags follow `DSN_METHODOLOGY` (declared v1.2; the spellings are unchanged in v1.4 §8.1). *(v2.12.14: "
             "the legacy rows `[ALG/NUM]`, `[ENG/ALG]`, `[NUM-strong]`, `[HEUR-strong]` are removed and the live compound "
             "tags are unpacked; Appendix A history keeps its original spellings.)*")

S1_RETRIG_OLD = ("Two-node binding threshold: exact period-2 retrigger iff $\\varepsilon\\in B_k\\cap(B_k+d)$, possible iff "
                 "$|d|_c\\le2k$ (LEM-RETRIG).")
S1_RETRIG_NEW = ("Two-node binding threshold: retrigger on every tick — period dividing 2, least period 2 for $d\\neq0$, a "
                 "fixed point at $d=0$ — iff $\\varepsilon\\in B_k\\cap(B_k+d)$, possible iff $|d|_c\\le2k$ (LEM-RETRIG).")

S1_BIND_OLD = "`[ALG/NUM strong]` **(v2.12) BIND3 headline.**"
S1_BIND_NEW = "`[NUM strong]` `[conv: v18 path orientation]` **(v2.12) BIND3 headline.**"

S1_FACT_OLD = ("`[ALG/NUM]` **TDR-24 factorization.** $C_{\\rm birth} = C_{\\rm component} / \\chi$, and $B/\\text{step} = "
               "O/\\text{step} \\cdot C_{\\rm birth}$. All identities verified")
S1_FACT_NEW = ("`[ALG]` [assuming: the microscopic birth law, `[NUM]`, for the first identity] **TDR-24 factorization.** "
               "$C_{\\rm birth} = C_{\\rm component} / \\chi$, and $B/\\text{step} = O/\\text{step} \\cdot C_{\\rm birth}$. "
               "Numerically corroborated: all identities verified")

S1_NSCALE_OLD = ("`[NUM strong]` **N-scaling** (v17/v6 canonical scan). At fixed $k/N = 1/15$, $T=5000$, bulk-conditioned "
                 "(excluding tail runs $M>500$):")
S1_NSCALE_NEW = ("`[NUM]` `[scope: full-range composite fit, N=120–1440]` `[conv: v18 path orientation]` **N-scaling** "
                 "(v17/v6 canonical scan). At fixed $k/N = 1/15$, $T=5000$, bulk-conditioned (excluding tail runs $M>500$):")
S1_CONS_OLD = ("Exponent consistency: $1.593 \\approx 0.757 + 0.836$; $0.869 \\approx 1.593 - 0.723$. Scaling data spans "
               "$N = 120$–$1440$.")
S1_CONS_NEW = ("The exponent is window-dependent: read on the high-N window $N=480$–$1440$ with run-level bulk filtering, the "
               "same scan gives $B/\\text{step}\\sim N^{-0.730}$ (Experiment-0 readout, §2 OPEN-POLICY-GEOMETRY). $-0.869$ is "
               "the full-range convenience value, not a structural constant (the failure class of $\\chi$, "
               "$C_{\\rm component}$ and $q_{\\rm proj}$, §2 TDR-24A/B); no refit is made here.")
S1_CRYST_OLD = "`[HEUR strong]` **Thermodynamic crystallization.**"
S1_CRYST_NEW = "`[HEUR]` **Thermodynamic crystallization.**"

S1_SLOT_OLD = ("`[ALG / NUM strong]` **Slot-volume model (verified).** $O_t = (2k+1) M_t \\psi_t$ holds by construction in "
               "the v6 extractor.")
S1_SLOT_NEW = ("**Slot-volume model (verified).** `[ALG]` $O_t = (2k+1) M_t \\psi_t$ holds by construction in the v6 "
               "extractor. `[NUM strong]`")

S1_GATE_OLD = ("`[DEF]` **Immediate frontier gate:** TDR-24D (slot-volume identity) and TDR-24F (structural-to-slot "
               "projection mechanism) are both closed `[NUM strong]`. The remaining gate before discrete triadic dynamics "
               "(TDR-T) is TDR-24A → TDR-24B → TDR-24C.")
S1_GATE_NEW = ("`[DEF]` **Immediate frontier gate:** TDR-24D (slot-volume identity: `[ALG]` identity, `[NUM strong]` "
               "intensiveness) and TDR-24F (structural-to-slot projection mechanism, `[NUM strong]`) are closed at the "
               "mechanism level; their analytic constants ($\\bar{c}_{\\rm struct}\\approx5$, $q_{\\rm proj}\\sim(2k+1)$) "
               "remain OPEN. The remaining gate before discrete triadic dynamics (TDR-T) is TDR-24A → TDR-24B → TDR-24C.")

S2_D_OLD = "slot-volume identity **CLOSED** `[ALG / NUM strong]`; see Settled items and §6.8."
S2_D_NEW = "slot-volume identity **CLOSED** (`[ALG]` identity; `[NUM strong]` intensiveness); see Settled items and §6.8."

S2_REVIEW_OLD = "12. **OPEN-SPECCONS-STAR** — advance-spectrum behavior across star blow-up (SG-12)."
S2_REVIEW_NEW = (S2_REVIEW_OLD + "\n\n**Owner-review tasks** *(v2.12.14; recorded for TDR-G by Programme v1.2 §6, not carried "
                 "by Programme v1.3)*: (1) state/gauge conventions — advanced in v2.12.14 (state and gauge definitions "
                 "registered as TDRG-DEF-ZN-STATE and TDRG-DEF-PHYSICAL-STATE; covariance group named in SG-14; the common "
                 "token shift recorded as not a gauge, §7); otherwise open; (2) the antipodal path tie — **discharged** by "
                 "TDRG-DEF-ORIENT (v2.12.14); (3) counting observables (§6.11) — open; (4) statistical/rank interpretation "
                 "of the growth fits (§2 TDR-24B rank analysis, §6.8) — open.")

S2_22B_OLD = ("Current state: `[HEUR strong]` $B_{\\rm bulk}/\\text{step} \\sim N^{-0.869}$ (v17/v6 extended fit, "
              "$N=120$–$1440$, $R^2=0.973$) — strongly supported; stable across the extension to $N=1440$. Analytic "
              "derivation still open.")
S2_22B_NEW = ("Current state: `[NUM]` full-range fit $B_{\\rm bulk}/\\text{step} \\sim N^{-0.869}$ (v17/v6, $N=120$–$1440$, "
              "$R^2=0.973$; window-dependent — $N^{-0.730}$ on $480$–$1440$, §1); the $N\\to\\infty$ limit is `[HEUR]`. "
              "Analytic derivation still open.")
S2_23_OLD = ("Current state: `[HEUR strong]` from v17/v6 extended fit ($N=120$–$1440$): $\\alpha = 0.869$, $R^2=0.973$.")
S2_23_NEW = ("Current state: `[NUM]` full-range fit ($N=120$–$1440$): $\\alpha = 0.869$, $R^2=0.973$; window-dependent "
             "($\\alpha\\approx0.730$ on $480$–$1440$, §1).")

S2_HEURNUM_OLD = "- `[HEUR/NUM]` $\\bar{c}_{\\rm struct}$ is bounded **only at high N**:"
S2_HEURNUM_NEW = ("- `[NUM]` (finite-N values; boundedness as $N\\to\\infty$ is `[HEUR]`) $\\bar{c}_{\\rm struct}$ is bounded "
                  "**only at high N**:")

S2_24B_OLD = ("Question (revised v2.12.1): derive the clean-star-count collapse $\\texttt{clean\\_star\\_components}/"
              "\\text{row}\\sim N^{-0.73}$ — *not* the composite $\\chi$ exponent, which is not a power law (see below).")
S2_24B_NEW = (S2_24B_OLD + "\n\n**Current status (v2.12.14):** the derivation target is the clean-star-count collapse "
              "$\\texttt{clean\\_star\\_components}/\\text{row}\\sim N^{-0.73}$ ($480$–$1440$ window), which is the per-row "
              "form of TDR-24A's clean-star supply cap; $\\chi$ is a composite ratio, not an independent scaling field; "
              "field count and policy separability are not identifiable on the single-lever corpus and are compute-gated "
              "on OPEN-POLICY-GEOMETRY (four new runs). The dated paragraphs below (v2.12.1–v2.12.9) are the supporting "
              "record; moving them to Appendix A is v2.13 layout work.")

S2_INT_OLD = "- **Internal consistency `[NUM strong / ALG exact]`:**"
S2_INT_NEW = ("- **Internal consistency — `[ALG]` value-wise identity (given the microscopic birth law) and `[NUM strong]` "
              "log-exponent agreement:**")
S2_KN_OLD = "- **`[NUM / COR]` k/N is a continuous control"
S2_KN_NEW = "- **`[COR]` (`[NUM]` support from §6.7) k/N is a continuous control"
S2_BRDIAG_OLD = "all outputs `[BRANCH/NUM diagnostic]`"
S2_BRDIAG_NEW = "all outputs `[NUM]` `[scope: branch diagnostic]`"
S2_BR1_OLD = "- **`[BRANCH/NUM]` Dynamical signal layer added"
S2_BR1_NEW = "- **`[NUM]` `[scope: exploratory branch TDRG-RESPONSE-TENSOR; diagnostic]` Dynamical signal layer added"
S2_BR2_OLD = "- **`[BRANCH/NUM]` Feature-map injectivity tested"
S2_BR2_NEW = "- **`[NUM]` `[scope: exploratory branch TDRG-RESPONSE-TENSOR; diagnostic]` Feature-map injectivity tested"

SET_FACT_OLD = "- **TDR-24 factorization closed** :: `[ALG/NUM]` ✓"
SET_FACT_NEW = "- **TDR-24 factorization closed** :: `[ALG]` (given the microscopic birth law; numerically corroborated) ✓"
SET_SLOT_OLD = "- **Slot-volume identity closed (TDR-24D)** :: `[ALG / NUM strong]` ✓"
SET_SLOT_NEW = "- **Slot-volume identity closed (TDR-24D)** :: `[ALG]` identity; `[NUM strong]` intensiveness ✓"
SET_BIND_OLD = "- **(v2.12) BIND3-CYCLE-N24K1 certified** :: `[ALG/NUM strong]` ✓"
SET_BIND_NEW = ("- **(v2.12) BIND3-CYCLE-N24K1 certified** :: `[ALG]` (finite exact enumeration; `[conv: v18 path "
                "orientation]`) ✓")

SG14 = ("**[SG-14]** *(v2.12.14)* **Relabelling covariance.** On the canonical branch `bound_symmetric` — and on any "
        "other policy branch only once its covariance is separately established — the TDR-G step must commute with "
        "$G_{\\rm cov}=\\mathrm{Sym}(V)\\times\\mathbb{Z}_N^{\\rm phase}$: every permutation of node labels (path-listing "
        "reversal included) together with the global phase shift $\\theta_i\\mapsto\\theta_i+c$ (SG-2). Equality of the "
        "two sides is understood **modulo a relabelling of freshly born nodes**: a newborn node has no prior label, so the "
        "outputs are compared after a one-to-one matching of the newborn nodes (as a multiset of $(\\theta,\\delta)$), as "
        "the checks of §6.12 do. Tie conditions are declared on $G_{\\rm cov}$-invariant data only; a rule that consults "
        "node IDs, listing order or creation order is an implementation presentation, not a law (Appendix B). **Not in "
        "$G_{\\rm cov}$:** (i) the common token shift $\\delta_i\\mapsto\\delta_i+c$ — it commutes with swaps, path "
        "successor shifts and ties and is broken by star blow-up unless $2c\\equiv0$ (imported OFN statement, §7); it is a "
        "symmetry of the birth-free sector only, not a gauge; (ii) the mirror $(\\theta,\\delta)\\mapsto(-\\theta,"
        "-\\delta)$ — the step is not mirror-equivariant at $P_3$ events (TDRG-ALG-MIRROR-NOT-STEP-SYMMETRY, §6.12). "
        "**Branch scope and evidence:** for `bound_symmetric` the finite checks of §6.12 (TDRG-NUM-ORIENT-EQUIVARIANCE-N24) "
        "support SG-14 on their tested scope; they are not a theorem for all $N$ or all policies. `trap`, `bound_multistar` "
        "and `bound_path_tie` differ from `bound_symmetric` only in bookkeeping on ties and multistars (§6.3, dynamic "
        "equivalence). In `largest_center` the choice between equal-degree multistar centres is by node ID "
        "(TDRG-ALG-LARGEST-CENTER-ID-TIEBREAK, §6.6), so that branch does not satisfy SG-14 — a recorded non-covariance "
        "of a non-canonical branch, to be resolved with TDR-19. `all_centers` is equivariant modulo the relabelling of "
        "newborn nodes on the tested fixture (§6.6).  \n"
        "Violation: an event rule or tie-break that depends on node labels; reading the common token shift or the mirror "
        "as a gauge; citing SG-14 for a policy branch whose covariance has not been established.")

S5_NSCALE_OLD = ("| N-scaling exponent | $B_{\\rm bulk}/\\text{step} \\sim N^{-0.869}$ [HEUR strong], bulk-conditioned, "
                 "$k/N=1/15$, $T=5000$, $N=120$–$1440$ | Aggregate exponent $\\alpha \\approx 1$ as primary; "
                 "tail-contaminated | §6.8 |")
S5_NSCALE_NEW = ("| N-scaling exponent | $B_{\\rm bulk}/\\text{step} \\sim N^{-0.869}$ `[NUM]`, full-range composite fit, "
                 "bulk-conditioned, $k/N=1/15$, $T=5000$, $N=120$–$1440$; window-dependent ($N^{-0.730}$ on $480$–$1440$) | "
                 "Aggregate exponent $\\alpha \\approx 1$ as primary (tail-contaminated); $0.869$ as a structural or "
                 "$N\\to\\infty$ exponent | §1, §6.8 |")
S5_CRYST_OLD = "| Thermodynamic crystallization | Strongly supported `[HEUR strong]`; requires $N\\to\\infty$ limit |"
S5_CRYST_NEW = "| Thermodynamic crystallization | `[HEUR]` extrapolation of finite-$N$ fits; requires the $N\\to\\infty$ limit |"
S5_FACT_OLD = "| TDR-24 factorization | Pool-level identity verified to machine precision `[ALG/NUM]` |"
S5_FACT_NEW = ("| TDR-24 factorization | Pool-level identity `[ALG]` (given the microscopic birth law), verified to machine "
               "precision |")
S5_SLOT_OLD = ("| Slot-volume model | Identity verified `[ALG / NUM strong]`; $\\psi_{\\rm slot}^{\\rm bulk}$ N-independent "
               "(numerical) | Analytic derivation of $\\psi_t$ intensiveness (that is TDR-24F, OPEN) | §6.8 |")
S5_SLOT_NEW = ("| Slot-volume model | Identity `[ALG]` (by construction); $\\psi_{\\rm slot}^{\\rm bulk}$ N-independent "
               "`[NUM strong]` | Analytic derivation of $\\psi_t$ intensiveness (the TDR-24F mechanism is closed "
               "numerically; its analytic constants are OPEN) | §6.8 |")
S5_K3_OLD = ("| $K_3$ global explosiveness | Cross-branch caution: `[FAIL]` in continuous Triadic DSN — only a quartic pump "
             "channel exists; full return has dominant healing (96:1 ratio) | Importing continuous $K_3$ explosiveness "
             "language into TDR-G | Appendix B |")
S5_K3_NEW = ("| $K_3$ global explosiveness | Historical continuous reference only: TRIAD v1.6.1 keeps the 96:1 healing/pump "
             "ratio as coefficient bookkeeping with the same-object correspondence `[OPEN]`; not a current fact about "
             "either branch | Importing continuous $K_3$ explosiveness or 96:1 language into TDR-G | Appendix B |")
S5_RETRIG_OLD = "| Two-node retrigger | Exact isolated period-2 result under LEM-RETRIG |"
S5_RETRIG_NEW = ("| Two-node retrigger | Exact isolated retrigger result under LEM-RETRIG (period dividing 2; fixed point "
                 "at $d=0$) |")

S6_2_PHYS_OLD = ("Physical consequence: fully defective $K_3$ triangles are forbidden. Physical discrete triadic objects are "
                 "partial-defect (path) or star-supported structures.")
S6_2_PHYS_NEW = (S6_2_PHYS_OLD + " *(v2.12.14, cross-citation; AZ-owned)* `AZ-ALG-ANTIPODAL-LOWORDER` (`az-v0.6`) is the "
                 "same antipodal-band arithmetic extended to closed non-backtracking walks: none of length 2 or 3 under "
                 "$k<N/6$, and none of odd length $L$ while $Lk<N/2$. It is a static $\\mathbb{Z}_N$ graph statement — not "
                 "TDR-G dynamics and not a bridge (SG-10); TDR-19 stays OPEN, and AZ's angular-spectrum results do not "
                 "confirm TDR-G's N-scaling.")

SIGNED_DEFS = (
    "`[DEF]` " + rid("TDRG-DEF-SIGNED-CENTERED") + " **Centered representative.** For even $N$ and $x\\in\\mathbb{Z}$, "
    "$\\operatorname{signed\\_centered}(x,N)$ is the representative of $x \\bmod N$ in the half-open interval "
    "$(-N/2,\\,N/2]$. The half-open choice is a convention; it gives $\\operatorname{signed\\_centered}(N/2)="
    "\\operatorname{signed\\_centered}(-N/2)=+N/2$, which is the source of the reversal-invariant stratum in the orientation "
    "rule below. *(v2.12.14: previously used here but defined only in the engine, function `signed_centered`.)*\n\n"
    "`[DEF]` " + rid("TDRG-DEF-SIGNED-DEFECT-ERROR") + " **Signed defect error.** "
    "$\\operatorname{signed\\_defect\\_error}(\\theta_i,\\theta_j,N)=\\operatorname{signed\\_centered}\\big((\\theta_i-"
    "\\theta_j) \\bmod N - N/2,\\;N\\big)$, the signed distance of $\\Delta_{ij}$ from the antipode. A pair is a defect edge "
    "iff $|\\operatorname{signed\\_defect\\_error}|\\le k$ (TDRG-DEF-EDGE-SET). On a defect edge "
    "$|\\operatorname{signed\\_defect\\_error}|\\le k<N/6$, so the value never reaches $\\pm N/2$ and it changes sign exactly "
    "when the pair is listed in the opposite order. *(Engine: function `signed_defect_error`.)*\n\n")

ORIENT_OLD = ("`[DEF]` **Path orientation rule.** For path $P_n$ ($n \\geq 3$): compute signed phase-gradient score $S = "
              "\\sum_i \\operatorname{signed\\_defect\\_error}(\\theta_{v_i}, \\theta_{v_{i+1}}, N)$. Orient forward if "
              "$S > 0$, reversed if $S < 0$. If $S = 0$, use endpoint advance $E = \\operatorname{signed\\_centered}"
              "(\\delta_{v_n} - \\delta_{v_1}, N)$. If $S = E = 0$: balanced path-tie (no gauge-invariant orientation exists "
              "under current axiom set).")
ORIENT_NEW = (
    SIGNED_DEFS +
    "`[DEF]` " + rid("TDRG-DEF-ORIENT") + " **Path orientation rule.** *(v2.12.14 `[COR]`; owner dispositions of "
    "27 Oct 2026, option (b).)* For a path $P_n$ ($n \\geq 3$) listed as $[v_1,\\ldots,v_n]$: $S = \\sum_i "
    "\\operatorname{signed\\_defect\\_error}(\\theta_{v_i}, \\theta_{v_{i+1}}, N)$. Orient forward if $S > 0$, reversed if "
    "$S < 0$. If $S = 0$, let $E = \\operatorname{signed\\_centered}(\\delta_{v_n} - \\delta_{v_1}, N)$: forward if "
    "$0<E<N/2$, reversed if $-N/2<E<0$. If $S=0$ and $2E\\equiv0 \\pmod N$ — that is, $E\\in\\{0,\\,N/2\\}$ — "
    "**balanced path-tie**: no orientation can be read from the declared invariants (TDRG-ALG-ORIENT-NOGO below; SG-14). "
    "The policies treat the tie as before (`bound_path_tie`, `bound_symmetric`: inert bound state; `trap`, "
    "`bound_multistar`: ambiguous). Reference implementation: `evidence/tdrg/scripts/tdrg_orient_v2_12_14.py` (drop-in "
    "`orient_path`). **Superseded completion:** v2.12.13 stated the tie only for $S=E=0$; at $S=0\\wedge E\\equiv N/2$ "
    "the pinned engine (the v17 engine `genesis_mode_b_mc.py` and v18 share one `orient_path`) oriented \"forward\" "
    "relative to the node-ID listing of `raw_ordered_path` — a label-dependent completion (Appendix B). Every motif-log "
    "and BIND3 result of this document was computed under that completion and is kept with `[conv: v18 path "
    "orientation]`, not rerun (`EV-NOT-RERUN`; three-node census bound in §6.12).\n\n"
    "`[ALG]` " + rid("TDRG-ALG-ORIENT-NOGO") + " **No orientation from $(S,E)$ on the antipodal-endpoint stratum.** "
    "Reversing the listing maps $S\\mapsto-S$ always (each defect-edge term is reversal-odd, "
    "TDRG-DEF-SIGNED-DEFECT-ERROR), and maps $E\\mapsto-E$ except when $\\delta_{v_n}-\\delta_{v_1}\\equiv N/2$, where "
    "$\\operatorname{signed\\_centered}$ returns $+N/2$ for both listings. Hence on $S=0\\wedge E\\equiv N/2$ the pair "
    "$(S,E)$ is reversal-invariant, and any selector that is a function of $(S,E)$ alone is either the tie or depends on "
    "the listing. The extended tie is the declared rule's covariant completion; it adds no new input. **Recorded "
    "alternative (not adopted):** for $P_3$ with centre $c$, $G=\\operatorname{signed\\_centered}(\\delta_{v_1}-\\delta_c)-"
    "\\operatorname{signed\\_centered}(\\delta_{v_3}-\\delta_c)$ is reversal-odd and never $0$ on the stratum (because "
    "$\\delta_{v_3}-\\delta_{v_1}\\equiv N/2\\neq0$; atlas check C2, exhaustive at $N=24$), so admitting the centre token "
    "as an orientation input would give a covariant non-tie rule for $P_3$; for longer paths a tie would still be needed "
    "on reversal-symmetric (palindromic) configurations. Choosing it is a law choice of the TDR-19 kind; it is kept for "
    "comparison with the adopted rule on the same universes in the later sensitivity campaign "
    "(`make_orient_g_alternative` in the reference implementation).")

POLTAB_OLD = "| Policy | Multistar treatment | Path double-tie | Character |"
POLTAB_NEW = "| Policy | Multistar treatment | Path tie ($S=0$, $2E\\equiv0$) | Character |"

S66_GUARD_OLD = "> **[Local guard SG-7 applies]** Policy results are branch-specific."
S66_GUARD_NEW = ("> **[Local guard SG-7 applies]** Policy results are branch-specific. **(v2.12.14)** All motif-log results "
                 "of §§6.6–6.10 come from the pinned engine (`upload/tdrg-records/genesis_mode_b_mc.py`, SHA-256 "
                 "`4c94d874…a608`, and its logging-only extension `genesis_mode_b_mc_v18.py`, `9d787b43…675e`; one "
                 "`orient_path`) and carry `[conv: v18 path orientation]`: they were computed with the label-dependent "
                 "completion at $S=0\\wedge E\\equiv N/2$ that TDRG-DEF-ORIENT replaces. They are not rerun "
                 "(`EV-NOT-RERUN`, PI decision 27 Oct 2026); the exposure is bounded only for the three-node universe "
                 "(§6.12) — the many-node exposure rate is not measured.")

S66_LC_OLD = ("`[NUM]` [conv: `largest_center`] **Continuous inflation branch:** Many multistar events, one birth per event, "
              "persistent expansion. Typical at $k/N \\approx 0.0667$: $rN_T \\approx 0.76$–$0.80$.")
S66_LC_NEW = (S66_LC_OLD + "\n\n`[ALG]` " + rid("TDRG-ALG-LARGEST-CENTER-ID-TIEBREAK") + " `[scope: engine function "
              "choose_largest_center, pinned v17/v18 engines]` *(v2.12.14, owner finding N1)* **`largest_center` breaks "
              "equal-degree ties by node ID.** The centre that fires is the first under the key $(-\\deg,\\ \\text{node "
              "id})$, so when two or more valid centres have the same degree the choice depends on node labels and the "
              "branch is not relabelling-covariant there (SG-14). Fixture: $K_{2,3}$ at $N=24$, $k=1$, centres of equal "
              "degree 3 with tokens 1 and 2 — exchanging the two centre labels changes which centre fires under "
              "`largest_center`, while `all_centers` and `bound_symmetric` are equivariant "
              "(`evidence/tdrg/disposition/multistar_fixture.py`, output `fe3928a4…`). The `largest_center` results of "
              "§§6.6–6.7 and §1 are kept with this scope note, not rerun (`EV-NOT-RERUN`); the canonical branch is "
              "unaffected (`bound_symmetric` binds multistars).")

S65_REACH_OLD = "`[THM]` **Reachability condition** ($k=0$):"
S65_REACH_NEW = "`[THM]` " + rid("TDRG-THM-REACHABILITY-K0") + " **Reachability condition** ($k=0$):"
S65_RES_OLD = "`[RESULT]` Noninteracting two-node sectors are superselection sectors."
S65_RES_NEW = "`[RESULT]` `[from: THM]` Noninteracting two-node sectors are superselection sectors."
S65_RETRIG_OLD = ("If the realized impact offset lies in the overlap, the isolated dyad forms an **exact period-2 bound state** "
                  "$(\\varepsilon,d)\\leftrightarrow(\\varepsilon-d,-d)$ (exact because CONV-TICK applies the swap against "
                  "the snapshot with no same-tick re-advance).")
S65_RETRIG_NEW = ("If the realized impact offset lies in the overlap, the isolated dyad forms an **exact bound state of period "
                  "dividing 2**, $(\\varepsilon,d)\\leftrightarrow(\\varepsilon-d,-d)$ (exact because CONV-TICK applies the "
                  "swap against the snapshot with no same-tick re-advance); its least period is 2 for $d\\neq0$, and $d=0$ "
                  "is a fixed point $(\\varepsilon,0)$ at which the swap fires on every tick *(v2.12.14 `[COR]`)*. The "
                  "retrigger band $|d|_c\\le2k<N/3$ never reaches $d\\equiv N/2$, so no other degenerate case occurs.")
S65_TAB_OLD = ("| Period-2 bound state (v2.12) | $\\varepsilon\\in B_k\\cap(B_k+d)$, $|d|_c\\le2k$ | exact retrigger 2-cycle "
               "(LEM-RETRIG) |")
S65_TAB_NEW = ("| Retrigger bound state (v2.12; period dividing 2) | $\\varepsilon\\in B_k\\cap(B_k+d)$, $|d|_c\\le2k$ | "
               "exact retrigger: a 2-cycle for $d\\neq0$, a fixed point for $d=0$ (LEM-RETRIG) |")

S64_FACT_OLD = "`[ALG/NUM]` **TDR-24 pool-level factorization:**"
S64_FACT_NEW = ("`[ALG]` [assuming: the microscopic birth law (`[NUM]`, below) for the first identity] **TDR-24 pool-level "
                "factorization:**")
S64_EDGE_OLD = "`[ENG/ALG]` **Edge-builder audit.**"
S64_EDGE_NEW = "`[ENG]` `[scope: 500 random inputs against the $O(n^2)$ reference]` **Edge-builder audit.**"
S66_BPE_OLD = "`[ALG/NUM]` **Multistar expansion character (ms_bpe).**"
S66_BPE_NEW = ("**Multistar expansion character (ms_bpe)** (`[ALG]` for `largest_center`, definitional; `[NUM]` for "
               "`all_centers`).")

S68_GUARD_OLD = ("> **[Local guard SG-6 applies]** All claims are finite-horizon (canonical scan currently N = 120–1440, "
                 "T=5000, with high-N asymptotic claims separately guarded).")
S68_GUARD_NEW = (S68_GUARD_OLD[:-2] + "; the v18-orientation scope of §6.6 applies).")
S68_HEUR_OLD = "`[HEUR strong]` **Bulk-conditioned N-scaling** (v4 motif analysis,"
S68_HEUR_NEW = ("`[NUM]` `[scope: full-range fits; composite exponents are window-dependent — §1, §2 TDR-24A/B]` "
                "**Bulk-conditioned N-scaling** (v4 motif analysis,")
S68_CONS_OLD = ("`[NUM strong]` [scope: fitted exponent consistency] $1.593 \\approx 0.757 + 0.836$; $0.869 \\approx 1.593 - "
                "0.723$. These are consistency checks on independently fitted exponents, **not** algebraic identities: they "
                "would be exact only if the power-law ansatz were perfect. The agreement to three decimals confirms the "
                "power-law form fits all observables simultaneously; residuals are consistent with fit uncertainty.")
S68_CONS_NEW = ("`[NUM]` [scope: full-range fits] $0.869 \\approx 1.593 - 0.723$ reflects the exact factorization "
                "$B/\\text{step}=O/\\text{step}\\cdot C_{\\rm birth}$ (§6.4) read on fitted exponents; it does not confirm a "
                "power-law form, and the composite exponents drift with the fit window. `[COR]` *(v2.12.14)* The former "
                "companion check $1.593\\approx0.757+0.836$ used the $\\chi$ exponent $+0.836$ superseded in v2.12.1 (§2 "
                "TDR-24B) and is withdrawn; no replacement sum is promoted.")
S68_SLOT_OLD = ("`[ALG / NUM strong]` **Slot-volume model (verified).** $O_t = (2k+1) M_t \\psi_t$ holds by construction. "
                "The v6 extractor confirms")
S68_SLOT_NEW = ("**Slot-volume model (verified).** `[ALG]` $O_t = (2k+1) M_t \\psi_t$ holds by construction. `[NUM strong]` "
                "The v6 extractor confirms")
S68_D_OLD = "**OPEN TDR-24D is structurally closed** `[ALG / NUM strong]`;"
S68_D_NEW = "**OPEN TDR-24D is structurally closed** (`[ALG]` identity; `[NUM strong]` intensiveness);"

S610_HEAD_OLD = "### §6.10 Multistar Locking Mechanism `[NUM / mixed]` {#sec-6-10-mechanism}"
S610_HEAD_NEW = "### §6.10 Multistar Locking Mechanism `[NUM]` — mixed content {#sec-6-10-mechanism}"
S610_OLD = "`[NUM / ALG structure]` In long-horizon `bound_symmetric` runs:"
S610_NEW = "`[NUM]` In long-horizon `bound_symmetric` runs:"

S612_HEAD_OLD = ("### §6.12 Three-Node Universe and BIND3 Certification `[ALG / NUM strong]` {#sec-6-12-threenode}")
S612_HEAD_NEW = ("### §6.12 Three-Node Universe and BIND3 Certification `[ALG]` — mixed content (exact lemma and "
                 "enumerations; numerical suites) {#sec-6-12-threenode}")
S612_GUARD_OLD = ("> **[SG-11, SG-12, SG-13 apply.]** All results in this section are scoped to the three-node, no-birth "
                  "universe under `bound_symmetric` with canonical v18 conventions (CONV-TICK, CONV-P3CYC) unless stated "
                  "otherwise.")
S612_GUARD_NEW = (S612_GUARD_OLD + " **(v2.12.14)** The enumerations and suites were run with the v18 path orientation "
                  "(label-dependent at $S=0\\wedge E\\equiv N/2$; replaced by TDRG-DEF-ORIENT): their numbers carry "
                  "`[conv: v18 path orientation]` and are not rerun (`EV-NOT-RERUN`; census bound in the "
                  "orientation-covariance block at the end of this section). LEM-SPECCONS is unaffected (ties act as "
                  "identity).")
S612_SPEC_OLD = "**LEM-SPECCONS — conservation of the relational advance spectrum.**"
S612_SPEC_NEW = rid("TDRG-ALG-LEM-SPECCONS") + " **LEM-SPECCONS — conservation of the relational advance spectrum.**"
S612_EQUIV_OLD = ("is **exactly conserved** — equivalently, the multiset of orbit-lattice spacings $\\{\\gcd(d_{ij},N)\\}$ is "
                  "conserved.")
S612_EQUIV_NEW = ("is **exactly conserved** — therefore, in particular, the multiset of orbit-lattice spacings "
                  "$\\{\\gcd(d_{ij},N)\\}$ is conserved *(v2.12.14 `[COR]`: the converse fails — at $N=24$, $|d|_c=1$ and "
                  "$|d|_c=5$ share $\\gcd=1$)*. Under TDRG-DEF-ORIENT (v2.12.14) the extended balanced tie also acts as "
                  "identity, so the lemma holds unchanged.")
S612_CYC_OLD = ("`[ALG/NUM strong]` `[scope: $N=24$, $k=1$, post-advance BIND3 ICs, exact cycle enumeration, 3456 ICs, both "
                "$P_3$ conventions]` **BIND3-CYCLE-N24K1 — exact certification.**")
S612_CYC_NEW = ("`[ALG]` `[scope: $N=24$, $k=1$, post-advance BIND3 ICs, exact cycle enumeration, 3456 ICs, both $P_3$ "
                "conventions]` `[conv: v18 path orientation]` " + rid("TDRG-ALG-BIND3-CYCLE-N24K1") +
                " **BIND3-CYCLE-N24K1 — exact certification.**")
S612_ANAT_OLD = "`[ALG/NUM strong]` `[scope: $N=24$, $k=1$]` **d-resolved anatomy"
S612_ANAT_NEW = "`[ALG]` `[scope: $N=24$, $k=1$]` `[conv: v18 path orientation]` **d-resolved anatomy"
S612_MIRROR_OLD = "Exact $\\pm d$ mirror symmetry holds in both families (relabeling-covariance check: PASS)."
S612_MIRROR_NEW = ("Exact $\\pm d$ mirror symmetry of the class inventory holds in both families (mirror-inventory check: "
                   "PASS). *(v2.12.14 `[COR]`: this is not node-relabelling covariance (SG-14), and the step itself is not "
                   "mirror-equivariant at $P_3$ events — TDRG-ALG-MIRROR-NOT-STEP-SYMMETRY, below.)*")
S612_PAR_OLD = "**BIND3-PARITY** *(replaces BIND3-KNIFE"
S612_PAR_NEW = rid("TDRG-NUM-BIND3-PARITY") + " **BIND3-PARITY** *(replaces BIND3-KNIFE"
S612_GATE_OLD = "**BIND3-SPECTRAL-GATE.** If every spacing"
S612_GATE_NEW = rid("TDRG-NUM-BIND3-SPECTRAL-GATE") + " **BIND3-SPECTRAL-GATE.** If every spacing"
S612_MEM_OLD = "`[COR]` **BIND3-MEMORY correction + `[NUM strong]` BIND3-MEMORY-PARITY**"
S612_MEM_NEW = ("`[COR]` **BIND3-MEMORY correction + `[NUM strong]` BIND3-MEMORY-PARITY** " +
                rid("TDRG-NUM-BIND3-MEMORY-PARITY"))
S612_XFER_OLD = "**BIND3-XFER — bond transfer.**"
S612_XFER_NEW = rid("TDRG-NUM-BIND3-XFER") + " **BIND3-XFER — bond transfer.**"
S612_REGEN_OLD = "**BIND3-REGEN — regeneration beyond the two-node threshold.**"
S612_REGEN_NEW = rid("TDRG-NUM-BIND3-REGEN") + " **BIND3-REGEN — regeneration beyond the two-node threshold.**"

S612_SYN_OLD = ("**Synthesis** `[INTERP]`: The BIND3 layer is not governed by \"bound survival versus dissolution.\" It is "
                "governed by a **conserved advance spectrum** whose **parity/lattice-avoidance structure** controls which "
                "pairs can autonomously retrigger (SPECTRAL-GATE), which spectators can avoid disruption (PARITY), and which "
                "initial bonds leave residence-time memory (MEMORY-PARITY).")
S612_SYN_NEW = (S612_SYN_OLD + "\n\n"
    "#### Orientation covariance at the antipodal-endpoint stratum *(v2.12.14)*\n\n"
    "`[ALG]` " + rid("TDRG-ALG-ORIENT-ANTIPODAL-FIXTURE") + " `[scope: one explicit state; pinned v18 engine]` **The "
    "v2.12.13/v18 orientation is not relabelling-covariant.** $N=24$, $k=1$, $\\theta_{\\rm pre}=(0,11,12)$, "
    "$\\delta=(0,1,12)$: after the advance $\\theta=(0,12,0)$; the defect graph is the path $0$–$1$–$2$ with $S=0$ and "
    "$E=+12=N/2$ under both listings. Exchanging the endpoint labels changes the v18 outcome (it gives $\\delta'=(1,12,0)$, "
    "which is not the relabelled image of the outcome in the other labelling); under TDRG-DEF-ORIENT the event is a balanced "
    "tie and the step is equivariant (the recorded G-alternative gives $\\delta'=(12,0,1)$, also equivariant). Evidence: "
    "`evidence/tdrg/disposition/antipodal_fixture.txt` (`c47d78b9…`); checker `evidence/tdrg/scripts/check_tdrg_v2_12_14.py`, "
    "gate C10 (negative control).\n\n"
    "`[NUM]` " + rid("TDRG-NUM-ORIENT-EQUIVARIANCE-N24") + " `[scope: N=24; three nodes exhaustive over the 331,776 "
    "gauge-reduced states (θ₀=δ₀=0) at k=1 and k=3, generators (01) and (12) of S₃; four nodes, 100,000 random (state, "
    "k∈{1,2,3}, permutation∈S₄) samples; bound_symmetric, and largest_center at four nodes; the pinned engine's own "
    "step_universe with only orient_path exchanged]` **Relabelling equivariance of the step.** Failures per generator: v18 "
    "72 / 72 at $k=1$ and 168 / 168 at $k=3$; TDRG-DEF-ORIENT 0; the G-alternative 0. Four nodes: v18 112 failures; "
    "TDRG-DEF-ORIENT and the G-alternative 0. Global phase shift: 0 failures in every variant (1/97 sample). Evidence: "
    "`evidence/tdrg/disposition/owner_relabel_equivariance_check.py` (`2f54e0fc…`), output "
    "`owner_relabel_equivariance_check_output.txt` (`a0b33690…`). A finite check, not a theorem for all $N$ or all "
    "policies.\n\n"
    "`[NUM]` `[scope: N=24, k=1, three nodes, the whole gauge-reduced state space; atlas independent check]` **Census bound "
    "for results computed under v18.** Under the v18 completion, 77 of 9,800 eventual cycles contain a listing-dependent "
    "event and 16,322 of 331,776 states (4.9 %) flow into such a cycle; under the extended tie the same universe has 9,789 "
    "eventual cycles, 66 of which contain a tie event on the stratum. Whether any of the 3,456 retrigger-entry or 10,368 "
    "one-pass BIND3 ICs reaches the stratum is not determined (the IC construction script is missing, §8). Source: "
    "`evidence/atlas/tdrg/atlas_tdrg_orientation_covariance_check.py` (`5684da96…`), results "
    "`atlas_tdrg_orientation_covariance_check.json` (`2d15b12f…`), rerun byte-identically by the owner session "
    "(owner disposition record claude01SKePJ, §5 (i)).\n\n"
    "`[NUM]` `[scope: NUMGEN DISC-2 ratified panel, 136 witnesses; atlas rerun of NUMGEN's audit verdict logic]` **DISC-2 "
    "witness effect.** 40 witnesses touch the stratum; under TDRG-DEF-ORIENT **20 of 136** records change verdict or class "
    "(for comparison: reverse completion 10, G-alternative 12); the ten admitted labels are unchanged; the 96 unexposed "
    "witnesses are unchanged by construction. DISC-1 and other panels are not covered; re-annotation is NUMGEN's.\n\n"
    "`[ALG]` " + rid("TDRG-ALG-MIRROR-NOT-STEP-SYMMETRY") + " *(owner finding N2)* **The mirror is not a step symmetry.** "
    "Under $(\\theta,\\delta)\\mapsto(-\\theta,-\\delta)$ every $\\operatorname{signed\\_defect\\_error}$ on a defect edge "
    "changes sign, so away from ties the path orientation reverses; the successor shift along the reversed path sends "
    "$(-\\delta_{v_1},-\\delta_{v_2},-\\delta_{v_3})\\mapsto(-\\delta_{v_3},-\\delta_{v_1},-\\delta_{v_2})$, which differs "
    "from the mirror image $(-\\delta_{v_2},-\\delta_{v_3},-\\delta_{v_1})$ of the original update unless the three tokens "
    "are equal. `[NUM]` check: 2,661 failures among the 2,703 states with a $P_3$ event in 60,000 random three-node states "
    "($N=24$, $k=1$; `evidence/tdrg/disposition/mirror_probe.py`, output `9f8bdf59…`). The $\\pm d$ mirror identity of the "
    "BIND3 class inventories (above) is therefore an inventory statement, not equivariance of the dynamics.")

S7_OLD = ("TDR-G imports no scientific coefficients, tensors, interaction laws, or continuous-branch results under the "
          "cross-branch firewall (SG-10). All scientific claims in this document are native $\\mathbb{Z}_N$ definitions, "
          "derivations, simulations, or diagnostics.\n\n"
          "The following are referenced as context only, not imported as scientific claims:\n\n"
          "- `RTG_PROGRAMME_OVERVIEW_v1.1` — programme-level scope guards SG-PROG-1 through SG-PROG-4.\n"
          "- `RTG_ONTOLOGICAL_FOUNDATIONS_v0.6` — O0–O3 motivational layer. Motivates but does not derive TDR-G "
          "interaction laws.\n\n"
          "If a bridge theorem between TDR-G and the continuous programme is ever established (OPEN-P1), the relevant "
          "imported claims must be registered here at that time.")
S7_NEW = (
    "TDR-G imports no scientific coefficients, tensors, interaction laws or continuous-branch results under the "
    "cross-branch firewall (SG-10). All scientific claims in this document are native $\\mathbb{Z}_N$ definitions, "
    "derivations, simulations or diagnostics, with the one scoped import below. *(v2.12.14: four-way register — imports, "
    "consumers, pins, exports — with the states received / statement accepted / adopted use read from records, not from "
    "queue states.)*\n\n"
    "**Imports.**\n\n"
    "- `[ALG]` [import: RTG_ONTOLOGICAL_FOUNDATIONS_v0.10 §4.1 | RTG-OFN-ALG-STAR-TOKEN-SHIFT] **Common token shift and the "
    "star rule.** Under $B_c:\\delta_i\\mapsto\\delta_i+c$, antipodal swaps, path successor shifts and ties commute with "
    "$B_c$ (they permute tokens); star blow-up (TDRG-DEF-STAR) commutes with $B_c$ iff $2c\\equiv0 \\pmod N$, because the "
    "centre goes to $-\\delta_A-c$ instead of $-\\delta_A+c$. State: **statement accepted** (owner dispositions, "
    "27 Oct 2026; checked as one-line algebra on TDRG-DEF-STAR and against the engine function "
    "`blow_up_star_with_snapshot`, `EV-CODE`). Use: SG-14 (the token shift lies outside $G_{\\rm cov}$). Custody "
    "transfer XFER-O08-01: **deferred** to v2.13 (the RID stays OFN's). OFN REQ-O09-05 is answered by TDRG-DEF-ORIENT "
    "(endpoint policy) and this entry.\n"
    "- Context only (not imported): Programme Overview v1.3 SG-PROG-1–SG-PROG-4; OFN v0.10 O0–O3 motivational layer "
    "(motivates, does not derive, TDR-G interaction laws). If a bridge theorem with the continuous programme is established "
    "(OPEN-P1), the imported claims are registered here at that time.\n\n"
    "**Consumers** (from the consumers' own records; adopted use is read only from a consumer's Import Ledger or release "
    "record):\n\n"
    "| Consumer (edition) | What it uses | State at v2.12.14 | Effect of v2.12.14 |\n"
    "|---|---|---|---|\n"
    "| NUMGEN v1.21 (`numgen-v1.21`) | state, recurrence and v18 event conventions for DISC-1/DISC-2 (\"RID unavailable\" "
    "imports); request `pipes/TDRG/20261026-NUMGEN-orientation-policy-s0-e-half-n.md` | received; request dispositioned (accept) | "
    "TDRG-DEF-ORIENT ruling; DISC-2 effect 20 of 136 records (§6.12); RIDs available; the C7C-M4 release is NUMGEN's |\n"
    "| OFN v0.10 (`ofn-v0.10`) | IMP-O08-02 to IMP-O08-16 (state, band, holonomy, narrow-band exclusion, recurrence, "
    "star, CONV-TICK, CONV-P3CYC, four lemmas); Finding A offered under XFER-O08-01; REQ-O09-05 | Finding A: statement "
    "accepted, custody deferred | owner RIDs below replace \"RID unavailable\"; REQ-O09-05 answered |\n"
    "| AZ v0.6 (`az-v0.6`) | Threads B/C: state (`TDRG-ZN-STATE`), LEM-REACH, LEM-RETRIG, LEM-SPECCONS | reference | "
    "`TDRG-ZN-STATE` resolves (map below); narrow-band exclusion cites `AZ-ALG-ANTIPODAL-LOWORDER` (§6.2) |\n"
    "| Genesis (Programme IF25) | `TDRG-EXPORT-POLICY-PHASE` | blocked (below) | none |\n\n"
    "Notices to NUMGEN, OFN and AZ are filed in their inboxes after the tag.\n\n"
    "**Pins.** Governing editions at this release: Programme Overview v1.3, OFN v0.10, DSN Methodology v1.4 (this edition "
    "still declares v1.2; the migration is v2.13). Claim-specific historical pins (OFN v0.6/v0.7 at §2 TDR-1/TDR-19 and "
    "LEM-NOANNIHIL; Programme v1.1 in earlier entries) stay as written: they record what the claim was stated against.\n\n"
    "**Owner RID map** (v2.12.14). RID names carry the category of the statement at registration (Methodology v1.4 §4.2); "
    "the names in the last column were used by consumers or the atlas before registration, resolve to the owner RID, and "
    "are not separate claims.\n\n"
    "| Owner RID | Statement | Location | Names in use elsewhere |\n"
    "|---|---|---|---|\n"
    "| TDRG-DEF-ZN-STATE | phase universe; variable-size state | §6.1 | `TDRG-ZN-STATE` (AZ); OFN IMP-O08-02 |\n"
    "| TDRG-DEF-PHYSICAL-STATE | quotient by global phase; $\\Delta_{ij}$ | §6.1 | OFN IMP-O08-02 |\n"
    "| TDRG-DEF-REL-ADVANCE | relative advance $d_{ij}$ | §6.1 | OFN IMP-O08-02 |\n"
    "| TDRG-DEF-KINEMATICS | free kinematic evolution | §6.1 | — |\n"
    "| TDRG-DEF-BAND | defect band $\\mathcal D_k$ | §6.1 | OFN IMP-O08-03 |\n"
    "| TDRG-DEF-EDGE-SET | defect edge set $E_{\\rm def}$ | §6.1 | — |\n"
    "| TDRG-DEF-NARROW-BAND | narrow-band condition $k<N/6$ | §6.1 | — |\n"
    "| TDRG-THM-HOLONOMY | holonomy identity | §6.2 | OFN IMP-O08-04 |\n"
    "| TDRG-THM-NARROW-BAND-EXCLUSION | no fully defective $K_3$ under $k<N/6$ | §6.2 | OFN IMP-O08-04B |\n"
    "| TDRG-THM-RECURRENCE | finite-state recurrence | §6.2 | OFN IMP-O08-08; NUMGEN DISC |\n"
    "| TDRG-DEF-CONV-TICK | step semantics | §6.3 | `CONV-TICK` (OFN IMP-O08-14) |\n"
    "| TDRG-DEF-SWAP | antipodal swap | §6.3 | atlas `TDRG-SWAP` |\n"
    "| TDRG-DEF-CONV-P3CYC | path successor shift | §6.3 | `CONV-P3CYC` (OFN IMP-O08-15) |\n"
    "| TDRG-DEF-SIGNED-CENTERED, TDRG-DEF-SIGNED-DEFECT-ERROR | conventions of the orientation rule | §6.3 | — |\n"
    "| TDRG-DEF-ORIENT | path orientation rule (v2.12.14) | §6.3 | `TDRG-ORIENT` (NUMGEN request; atlas) |\n"
    "| TDRG-ALG-ORIENT-NOGO | no orientation from $(S,E)$ on the stratum | §6.3 | — |\n"
    "| TDRG-DEF-CYCLE-BOUND | cycle bound states | §6.3 | atlas `TDRG-CYCLE` |\n"
    "| TDRG-DEF-STAR | star blow-up | §6.3 | OFN IMP-O08-09 |\n"
    "| TDRG-DEF-MULTISTAR | multistar and the policy fork | §6.3 | atlas `TDRG-MULTISTAR` |\n"
    "| TDRG-DEF-CANONICAL-BRANCH | `bound_symmetric` | §6.3 | — |\n"
    "| TDRG-THM-REACHABILITY-K0 | reachability at $k=0$ | §6.5 | — |\n"
    "| TDRG-ALG-LEM-REACH, TDRG-ALG-LEM-NOANNIHIL, TDRG-ALG-LEM-RETRIG | two-node lemmas | §6.5 | `LEM-REACH`, "
    "`LEM-NOANNIHIL`, `LEM-RETRIG` (OFN IMP-O08-05/06/07; AZ) |\n"
    "| TDRG-ALG-LARGEST-CENTER-ID-TIEBREAK | `largest_center` ID tie-break (N1) | §6.6 | — |\n"
    "| TDRG-ALG-LEM-SPECCONS | advance-spectrum conservation | §6.12 | `LEM-SPECCONS` (OFN IMP-O08-16; AZ) |\n"
    "| TDRG-ALG-BIND3-CYCLE-N24K1 | exact cycle enumeration | §6.12 | `BIND3-CYCLE-N24K1` |\n"
    "| TDRG-NUM-BIND3-PARITY, -SPECTRAL-GATE, -MEMORY-PARITY, -XFER, -REGEN | BIND3 results | §6.12 | `BIND3-*` |\n"
    "| TDRG-ALG-ORIENT-ANTIPODAL-FIXTURE, TDRG-NUM-ORIENT-EQUIVARIANCE-N24, TDRG-ALG-MIRROR-NOT-STEP-SYMMETRY | "
    "orientation covariance | §6.12 | — |\n"
    "| TDRG-ART-SESSION-SCRIPTS, TDRG-ART-ORIENT-V2-12-14, TDRG-ART-ORIENT-COVARIANCE-CHECKS | artifacts | §8 | — |\n\n"
    "**Exports.**")

S8_OLD_START = "- [RID: TDRG-ART-GENESIS-MC] :: `genesis_mode_b_mc.py` ::"
S8_OLD_END = "`[NUM strong]` session-certified; consolidate into `bind3_nkscan_suite.py`"
S8_NEW = (
    "Custody states (Methodology v1.4 §12): **placed** — in the repository, path and SHA-256; **replayed** — an output "
    "reproduced byte-for-byte from a placed input; **held** — outside the repository with SHA-256 recorded; **missing** — "
    "no original located. Held files are never reconstructed; a re-derivation is an independent contribution, not a "
    "recovery. *(v2.12.14 register; hash check `records/tdrg/TDRG_UPLOAD_HASH_CHECK_20261027.md`.)*\n\n"
    "- [RID: TDRG-ART-GENESIS-MC] :: `genesis_mode_b_mc.py` — the engine that produced the v17 motif corpus (header label "
    "\"v15.3\"; \"v17\" is the data-campaign label of the 258-field motif schema) :: three-policy Monte Carlo engine; "
    "`argparse` CLI (`--policy`, `--N`, `--k`, `--grid-N`, `--ratios`, `--T`, `--batch`, `--max-nodes`, `--seed`, "
    "`--audit-trials`, `--motif-log`, `--motif-stride`) :: `[ENG]` **placed** `upload/tdrg-records/genesis_mode_b_mc.py`, "
    "SHA-256 `4c94d8741dc43780394cc563d04be9b2ee5c9767a43a048878fc67640dafa608`; **replayed** for two v17 files "
    "(`motif_TEST_N120_k8_T1200_b3_v17.csv`, `de0f3e42…`; canonical-scan `motif_N120_k08_T5000_b20_v17.csv`, `7ef343b0…`; "
    "`evidence/tdrg/disposition/engine_replay_log.txt`); schema-consistent, not replayed, for the other placed v17 files; "
    "the held v17 files cannot be replayed here.\n"
    "- [RID: TDRG-ART-GENESIS-MC-V18] :: `genesis_mode_b_mc_v18.py` :: convention ground truth for v2.12 (CONV-TICK audit, "
    "CONV-P3CYC); differs from TDRG-ART-GENESIS-MC only by dense-birth-window logging (same `step_universe`, `orient_path` "
    "and event rules) :: `[ENG]` **placed** `upload/tdrg-records/genesis_mode_b_mc_v18.py`, SHA-256 "
    "`9d787b435c42fd2024c81e614e3c6e3e076dc2bd30ad1e7e286ada8e6dfe675e` (byte-equal to the copy on `upload/numgen-records`). "
    "Its `orient_path` is the superseded completion (§6.3); the engine is not patched in v2.12.14 — the amended rule's "
    "reference implementation is TDRG-ART-ORIENT-V2-12-14.\n"
    "- [RID: TDRG-ART-MOTIF-V6] :: `tdr_motif_bootstrap_v6.py` :: current canonical motif analysis script (bulk/tail split, "
    "multi-threshold $p_{\\rm tail}$, slot-volume and structural metrics, per-run CSV, DSN patch output) :: `[ENG]` "
    "**placed** `upload/tdrg-records/tdr_motif_bootstrap_v6.py`, `3ebf064d…`; its per-run CSV and DSN-patch outputs are "
    "**missing** (not identified in any upload).\n"
    "- [RID: TDRG-ART-MOTIF-V4] :: `tdr_motif_bootstrap_v4.py` :: superseded by v6; produced the 6-point $N^{-0.876}$ fit :: "
    "`[ENG]` archived; **placed** `upload/tdrg-records/tdr_motif_bootstrap_v4.py`, `86e77511…` (v1–v3, v5 and "
    "`tdr_motif_analysis*.py` are placed beside it).\n"
    "- [RID: TDRG-ART-MOTIF-V17-DATA] :: v17 motif log corpus :: current canonical source data for TDR-24D/F, the extended "
    "N-scaling ($N=120$–$1440$) and the N=720/722 tail diagnosis :: `[ENG]` partly **placed** (`upload/tdrg-records/`: "
    "N=120, 240, 480, 1080 at b20; N=718 and N=840 `bound_symmetric` as zip archives; TESTGRID and TEST files), partly "
    "**held** with SHA-256 in `upload/tdrg-records/SHA256SUMS_tdrg_held.txt`: N=1200 and 1440 (b50); N=720, 722, 840 and "
    "960 (b100, T5000).\n"
    "- [RID: TDRG-ART-MOTIF-V16-DATA] :: v16 motif log corpus :: archive-valid for the TDR-24 factorization and the earlier "
    "v4 scaling; superseded for v17/v6 scaling :: `[ENG]` archived; partly **placed** (`upload/tdrg-records/*_v16.csv`), "
    "partly **held** (N=720 b100, two seeds; N=960 b100; hashes in the same manifest).\n"
    "- [RID: TDRG-ART-KINEMATIC-CERTS] :: genesis-layer lemma certificates (LEM-REACH, LEM-NOANNIHIL, LEM-RETRIG, "
    "first-return period) :: finite exhaustive verification as reported in v2.12 (77,552 band cases, even $N\\le40$; zero "
    "failures) :: **missing** — session-certified in an earlier session; no original located. The lemmas keep their "
    "algebraic arguments in §6.5; the finite verification is `EV-SRC-REPORTED`.\n"
    "- [RID: TDRG-ART-SPECCONS] :: LEM-SPECCONS verification (signed-permutation argument; 3000 random ICs × 500 steps) :: "
    "**missing**; the algebraic argument stands in §6.12; the sampled verification is `EV-SRC-REPORTED`.\n"
    "- [RID: TDRG-ART-BIND3-N24K1] :: BIND3-CYCLE-N24K1 exact enumeration (3456 post-advance ICs, both $P_3$ conventions; "
    "taxonomy, d-resolved anatomy, transfer, period spectrum) :: **missing**; the numbers are `EV-SRC-REPORTED` and carry "
    "`[conv: v18 path orientation]`.\n"
    "- [RID: TDRG-ART-BIND3-SUITE] :: NKSCAN falsification suite ($k=2$ parity, spectral gate, memory stratification) :: "
    "**missing**; the numbers are `EV-SRC-REPORTED` and carry `[conv: v18 path orientation]`.\n"
    "- " + rid("TDRG-ART-SESSION-SCRIPTS") + " :: scripts of the TDR-24A/B/F, TDR-25/26, OPEN-POLICY-GEOMETRY and "
    "TDRG-RESPONSE-TENSOR entries of §2 (`tdr24a_decomposition.py`, `tdr24a_provenance.py`, `tdr24a_ratelaw.py`, "
    "`tdr24b_chi_refit.py`, `tdr24b_field_structure.py`, `tdr24f_consistency_audit.py`, `tdr24f_data_recompute.py`, "
    "`tdr24_observable_rank.py`, `tdr25_burst_bridge.py`, `tdr26_early_basin_classifier.py` with its two CSV outputs, "
    "`tdr24_policy_geometry/EXPERIMENT_DESIGN.md`, `tdr24_policy_geometry_classify.py`, "
    "`tdrg_response_tensor/BRANCH_CHARTER.md`, `response_tensor.py`, `dynamical_extractor.py`) :: `[ENG]` **held** by "
    "co-owner session claude01SKePJ as its final copies and uploaded unchanged to branch `upload/tdrg-session-scripts` "
    "(commit `386e9d4`, `SHA256SUMS.txt` there); placed on `main` after the atlas hash check. They are final copies, not "
    "shown to be the exact versions that produced each historical number.\n"
    "- " + rid("TDRG-ART-ORIENT-V2-12-14") + " :: `evidence/tdrg/scripts/tdrg_orient_v2_12_14.py` :: reference "
    "implementation of TDRG-DEF-ORIENT (drop-in `orient_path`) and of the recorded G-alternative :: `[ENG]` **placed**; "
    "exercised by the v2.12.14 checker.\n"
    "- " + rid("TDRG-ART-ORIENT-COVARIANCE-CHECKS") + " :: `evidence/tdrg/disposition/` (equivariance check, antipodal and "
    "multistar fixtures, mirror probe, engine replay log; `SHA256SUMS.txt`) and the v2.12.14 builder and checker "
    "(`evidence/tdrg/scripts/build_tdrg_v2_12_14.py`, `check_tdrg_v2_12_14.py`) :: evidence for the v2.12.14 entries of "
    "§6.3, §6.6 and §6.12 :: `[ENG]` **placed**.\n"
    "- Post-edition data, not cited by any claim here: `motif_N720_k48_T5000_b500_v18.csv` (held), "
    "`motif_N840_k56_largest_center_b100_v17.csv`, `motif_N840_sweep_b100_v17.csv`, "
    "`motif_PG_N840_k56_largest_center_b100_telemetry1.csv` with its manifest, `genesis_mode_b_mc_telemetry.py` "
    "(`ba99e307…`) — placed or held as received, for the OPEN-POLICY-GEOMETRY record that will use them.")

S9_REPO_OLD = "**Repository:** `rtg-resonance-2025`"
S9_REPO_NEW = ("**Repository:** `MustafaAksu/rtg-corpus` (governing edition = the latest `tdrg-v…` tag with its release "
               "record); earlier archive label `rtg-resonance-2025`")
S9_POL_OLD = "| `bound_path_tie` / `bound_symmetric` cleanup | `[ALG/NUM]` | in-session policy evolution |"
S9_POL_NEW = "| `bound_path_tie` / `bound_symmetric` cleanup | `[DEF]` (policies), exercised `[NUM]` | in-session policy evolution |"
S9_EDGE_OLD = "| Optimized edge-builder audit | `[ENG/ALG]` | brute-force comparison, 500 random trials |"
S9_EDGE_NEW = "| Optimized edge-builder audit | `[ENG]` | brute-force comparison, 500 random trials |"

APPA_OLD = "## Appendix A — Version History {#appendix-a}\n\n### v2.12 — June 2026"
APPA_ENTRY = (
    "### v2.12.14 — October 2026\n\n"
    "Corrections-only edition: the owner pass after the v2.12.13 advisories (Methodology v1.2 kept as declared; no layout "
    "change; no rerun). Predecessor `tdrg-v2.12.13` (SHA-256 `aa232643…053f`). Release record "
    "`records/tdrg/TDRG_v2_12_14_RELEASE_RECORD.md`; fixed dispositions "
    "`records/tdrg/TDRG_OWNER_DISPOSITION_RECONCILIATION_v2_12_13.md`; edit log `evidence/tdrg/v2.12.14/edit_log.json`.\n"
    "- **§6.3 [COR/DEF]:** TDRG-DEF-ORIENT — balanced tie extended to $S=0\\wedge2E\\equiv0$ (relabelling-covariant; "
    "replaces the node-ID completion at $E\\equiv N/2$); TDRG-ALG-ORIENT-NOGO; `signed_centered` and `signed_defect_error` "
    "defined; the G-rule recorded, not adopted.\n"
    "- **§3 [NEW]:** SG-14 relabelling covariance ($\\mathrm{Sym}(V)\\times\\mathbb{Z}_N^{\\rm phase}$; token shift and "
    "mirror outside; `largest_center` exception).\n"
    "- **§6.12 [NEW/COR]:** orientation-covariance block (fixture, equivariance check, census bound, DISC-2 effect, mirror "
    "not a step symmetry); the \"relabeling-covariance check\" renamed mirror-inventory check; LEM-SPECCONS \"equivalently\" "
    "→ \"therefore, in particular\"; BIND3 results `[conv: v18 path orientation]`, `EV-NOT-RERUN`.\n"
    "- **§6.5 [COR]:** LEM-RETRIG least period (period dividing 2; fixed point at $d=0$).\n"
    "- **§6.6 [NEW]:** TDRG-ALG-LARGEST-CENTER-ID-TIEBREAK; v18-orientation guard on §§6.6–6.10.\n"
    "- **§1, §2, §5, §6.8 [COR]:** N-scaling range-tagged and graded `[NUM]` (window-dependent; $-0.730$ on 480–1440); the "
    "$\\chi=0.836$ consistency check withdrawn; crystallization `[HEUR]`; current state of TDR-24 D/F versus A/B/C aligned; "
    "TDR-24B current-status line; the Programme v1.2 owner-review tasks recorded.\n"
    "- **Tags [COR]:** live compound tags unpacked; the local alias table replaced.\n"
    "- **RIDs [NEW]:** 39 definition, claim and artifact RIDs (§7 owner RID map; consumer names `TDRG-ORIENT`, "
    "`TDRG-ZN-STATE`, `CONV-*`, `LEM-*` mapped); no OPEN-module RID renamed.\n"
    "- **§7 [COR]:** imports, consumers, pins and RID map; OFN Finding A statement accepted (custody deferred).\n"
    "- **§8 [COR]:** custody register (placed / replayed / held / missing) with hashes; engine identity of the v17 corpus.\n"
    "- **Header, §9, Appendices B and C [COR]:** governing editions; repository named; Appendix B row for the node-ID "
    "completion; K₃ 96:1 and the T-6 wedge marked historical; TDR-T gate aligned with §1.\n"
    "- **Not changed:** every scientific number; Appendix A history; the footer chain and the Appendix A order (v2.13).\n\n"
    "### v2.12 — June 2026")

APPB_OLD = "- [FAIL] Arbitrary path label fallback as tie-breaking — background-independence violation."
APPB_NEW = (APPB_OLD + "\n- [FAIL] *(v2.12.14)* Path-orientation completion by node-ID listing at $S=0\\wedge E\\equiv N/2$ "
            "(the v17/v18 engine's `orient_path` with `raw_ordered_path`, standing in for the v2.12.13 rule there) — not "
            "relabelling-covariant (TDRG-ALG-ORIENT-ANTIPODAL-FIXTURE): an unintended instance of the arbitrary-label "
            "fallback above. Replaced by the extended balanced tie (TDRG-DEF-ORIENT). Results computed under it are kept "
            "with `[conv: v18 path orientation]`.")
APPB_K3_OLD = ("- [FAIL] $K_3$ globally explosive — only a quartic pump *channel* exists; the full six-step return has dominant "
               "healing terms (96:1 healing/pump ratio). See Triadic DSN.")
APPB_K3_NEW = (APPB_K3_OLD + " *(v2.12.14: historical continuous reference — TRIAD v1.6.1 keeps 96:1 as coefficient "
               "bookkeeping with the same-object correspondence OPEN; not a current fact about either branch.)*")

APPC_GATE_OLD = ("> **Gate condition:** Do not begin full discrete triadic dynamics until OPEN TDR-24D, TDR-24A, TDR-24B are "
                 "all closed.")
APPC_GATE_NEW = ("> **Gate condition:** Do not begin full discrete triadic dynamics until TDR-24A → TDR-24B → TDR-24C close "
                 "(TDR-24D and TDR-24F are closed at the mechanism level, §1). *(v2.12.14 `[COR]`; aligned with §1 and "
                 "§2.)*")
APPC_D_OLD = "| TDR-24D | Slot-volume identity | Derive candidate-pool scaling | Immediate |"
APPC_D_NEW = "| TDR-24D | Slot-volume identity | Derive candidate-pool scaling | closed (mechanism level) |"
APPC_T3_OLD = "| TDR-T3 | Safe-wedge reachability | Determine if safe orientation reachable | TDR-T2 |"
APPC_T3_NEW = ("| TDR-T3 | Safe-wedge reachability *(historical continuous reference: the sector/wedge imports were withdrawn "
               "by TRIAD v1.6.1 CN-05; to be restated natively before use)* | Determine if safe orientation reachable | "
               "TDR-T2 |")
APPC_R0_OLD = ("**R0** `[ALG structure]` Continuous tensors and coefficients ($1/3$, $3/4$, $x_*$, $-32r^4$, Plücker "
               "constants) cannot be used in TDR-G unless reproduced by a native $\\mathbb{Z}_N$ derivation.")
APPC_R0_NEW = (APPC_R0_OLD + " *(v2.12.14: $x_*$ is a historical root of the continuous T-6 chain, and TRIAD v1.6.1 "
               "withdraws its safe-wedge reading (CN-05); it is listed here only as a historical example.)*")
APPC_R2_OLD = ("**R2** `[OPEN]` Multistar vacuum prerequisite: TDR-24D → TDR-24A → TDR-24B must be closed before discrete "
               "triadic dynamics.")
APPC_R2_NEW = ("**R2** `[OPEN]` Multistar vacuum prerequisite: TDR-24A → TDR-24B → TDR-24C must close before discrete "
               "triadic dynamics (TDR-24D and TDR-24F are closed at the mechanism level).")

FOOT_TITLE_OLD = "*END OF DOCUMENT — RTG_DISCRETE_GENESIS_DSN_v2.12.13*"
FOOT_TITLE_NEW = "*END OF DOCUMENT — RTG_DISCRETE_GENESIS_DSN_v2.12.14*"
FOOT_SUP_OLD = "*Supersedes RTG_DISCRETE_GENESIS_DSN_v2.12.12,"
FOOT_SUP_NEW = "*Supersedes RTG_DISCRETE_GENESIS_DSN_v2.12.13 (tag `tdrg-v2.12.13`), RTG_DISCRETE_GENESIS_DSN_v2.12.12,"

def rid_after(bold, r):
    return (bold, rid(r) + " " + bold)

# --------------------------------------------------------------------------------------------- edit list
# (key, group, row, mode, old, new)
EDITS = [
    ("E01", "TB13", "header title", "line", "# RTG_DISCRETE_GENESIS_DSN_v2.12.13", H_TITLE),
    ("E02", "TB13", "header date", "line", "**Date:** June 2026", H_DATE),
    ("E03", "TB13", "header supersedes", "line", "**Supersedes:**", H_SUPERSEDES),
    ("E04", "TB10", "header companion documents -> governing editions", "line", "**Companion documents:**", H_COMPANION),
    ("E05", "TB10", "header declared methodology", "line", "**DSN Methodology:**", H_METH),
    ("E06", "TA04", "status summary: scaling scope, crystallization HEUR, TDR-24 gate", "str", SS_OLD, SS_NEW),
    ("E07", "TB12", "status summary: BIND3 tag", "str", SS_BIND_OLD, SS_BIND_NEW),
    ("E08", "TB13", "status summary: v2.12.14 sentence", "str", SS_END_OLD, SS_END_NEW),
    ("E09", "TB12", "local alias table replaced", "str", ALIAS_OLD, ALIAS_NEW),
    ("E10", "TA05", "§1 LEM-RETRIG least period", "str", S1_RETRIG_OLD, S1_RETRIG_NEW),
    ("E11", "TB12", "§1 BIND3 headline tag", "str", S1_BIND_OLD, S1_BIND_NEW),
    ("E12", "TB12", "§1 TDR-24 factorization tag", "str", S1_FACT_OLD, S1_FACT_NEW),
    ("E13", "TA04", "§1 N-scaling grade and scope", "str", S1_NSCALE_OLD, S1_NSCALE_NEW),
    ("E14", "TA04", "§1 chi=0.836 consistency removed; window dependence", "str", S1_CONS_OLD, S1_CONS_NEW),
    ("E15", "TA04", "§1 crystallization HEUR", "str", S1_CRYST_OLD, S1_CRYST_NEW),
    ("E16", "TB12", "§1 slot-volume tags split", "str", S1_SLOT_OLD, S1_SLOT_NEW),
    ("E17", "I07", "§1 frontier gate", "str", S1_GATE_OLD, S1_GATE_NEW),
    ("E18", "TB12", "§2 TDR-24D tag", "str", S2_D_OLD, S2_D_NEW),
    ("E19", "TC17", "§2 owner-review tasks", "str", S2_REVIEW_OLD, S2_REVIEW_NEW),
    ("E20", "TA04", "§2 TDR-22b grade and range", "str", S2_22B_OLD, S2_22B_NEW),
    ("E21", "TA04", "§2 TDR-23 grade and range", "str", S2_23_OLD, S2_23_NEW),
    ("E22", "TB12", "§2 TDR-24F HEUR/NUM", "str", S2_HEURNUM_OLD, S2_HEURNUM_NEW),
    ("E23", "I07", "§2 TDR-24B current status", "str", S2_24B_OLD, S2_24B_NEW),
    ("E24", "TB12", "§2 TDR-24B internal consistency tag", "str", S2_INT_OLD, S2_INT_NEW),
    ("E25", "TB12", "§2 TDR-24B k/N tag", "str", S2_KN_OLD, S2_KN_NEW),
    ("E26", "TB12", "§2 branch diagnostic tag", "str", S2_BRDIAG_OLD, S2_BRDIAG_NEW),
    ("E27", "TB12", "§2 branch dynamical layer tag", "str", S2_BR1_OLD, S2_BR1_NEW),
    ("E28", "TB12", "§2 branch injectivity tag", "str", S2_BR2_OLD, S2_BR2_NEW),
    ("E29", "TB12", "§2 settled: factorization tag", "str", SET_FACT_OLD, SET_FACT_NEW),
    ("E30", "TB12", "§2 settled: slot-volume tag", "str", SET_SLOT_OLD, SET_SLOT_NEW),
    ("E31", "TB12", "§2 settled: BIND3 tag", "str", SET_BIND_OLD, SET_BIND_NEW),
    ("E32", "TA03", "§3 SG-14", "str",
     "Violation: Reading the gate as a ban on band entry, or applying it across births.",
     "Violation: Reading the gate as a ban on band entry, or applying it across births.\n\n" + SG14),
    ("E33", "TA04", "§5 N-scaling row", "str", S5_NSCALE_OLD, S5_NSCALE_NEW),
    ("E34", "TA04", "§5 crystallization row", "str", S5_CRYST_OLD, S5_CRYST_NEW),
    ("E35", "TB12", "§5 factorization row", "str", S5_FACT_OLD, S5_FACT_NEW),
    ("E36", "I07", "§5 slot-volume row", "str", S5_SLOT_OLD, S5_SLOT_NEW),
    ("E37", "TA07", "§5 K3 row historical", "str", S5_K3_OLD, S5_K3_NEW),
    ("E38", "TA05", "§5 two-node retrigger row", "str", S5_RETRIG_OLD, S5_RETRIG_NEW),
    ("E39", "TB09", "RID TDRG-DEF-ZN-STATE", "str", "`[DEF]` **Phase universe.**",
     "`[DEF]` " + rid("TDRG-DEF-ZN-STATE") + " **Phase universe.**"),
    ("E40", "TB09", "RID TDRG-DEF-PHYSICAL-STATE", "str", "`[DEF]` **Physical state** is",
     "`[DEF]` " + rid("TDRG-DEF-PHYSICAL-STATE") + " **Physical state** is"),
    ("E41", "TB09", "RID TDRG-DEF-REL-ADVANCE", "str", "`[DEF]` **Relative advance:**",
     "`[DEF]` " + rid("TDRG-DEF-REL-ADVANCE") + " **Relative advance:**"),
    ("E42", "TB09", "RID TDRG-DEF-KINEMATICS", "str", "`[DEF]` **Kinematic evolution:**",
     "`[DEF]` " + rid("TDRG-DEF-KINEMATICS") + " **Kinematic evolution:**"),
    ("E43", "TB09", "RID TDRG-DEF-BAND", "str", "`[DEF]` **Defect band:**",
     "`[DEF]` " + rid("TDRG-DEF-BAND") + " **Defect band:**"),
    ("E44", "TB09", "RID TDRG-DEF-EDGE-SET", "str", "`[DEF]` **Defect edge set:**",
     "`[DEF]` " + rid("TDRG-DEF-EDGE-SET") + " **Defect edge set:**"),
    ("E45", "TB09", "RID TDRG-DEF-NARROW-BAND", "str", "`[DEF]` **Narrow-band condition:**",
     "`[DEF]` " + rid("TDRG-DEF-NARROW-BAND") + " **Narrow-band condition:**"),
    ("E46", "TB09", "RID TDRG-THM-HOLONOMY", "str", "`[THM]` **Holonomy identity.**",
     "`[THM]` " + rid("TDRG-THM-HOLONOMY") + " **Holonomy identity.**"),
    ("E47", "TB09", "RID TDRG-THM-NARROW-BAND-EXCLUSION", "str", "`[THM]` **Narrow-band exclusion.** Under $k < N/6$, no "
     "three nodes can all be mutually defect-related:",
     "`[THM]` " + rid("TDRG-THM-NARROW-BAND-EXCLUSION") + " **Narrow-band exclusion.** Under $k < N/6$, no three nodes "
     "can all be mutually defect-related:"),
    ("E48", "TC16", "§6.2 AZ cross-citation and scope (I12)", "str", S6_2_PHYS_OLD, S6_2_PHYS_NEW),
    ("E49", "TB09", "RID TDRG-THM-RECURRENCE", "str", "`[THM]` **Finite-state recurrence.**",
     "`[THM]` " + rid("TDRG-THM-RECURRENCE") + " **Finite-state recurrence.**"),
    ("E50", "TB09", "RID TDRG-DEF-CONV-TICK", "str", "`[DEF]` **Canonical step semantics (CONV-TICK).**",
     "`[DEF]` " + rid("TDRG-DEF-CONV-TICK") + " **Canonical step semantics (CONV-TICK).**"),
    ("E51", "TB09", "RID TDRG-DEF-SWAP", "str", "`[DEF]` **Antipodal swap**",
     "`[DEF]` " + rid("TDRG-DEF-SWAP") + " **Antipodal swap**"),
    ("E52", "TB09", "RID TDRG-DEF-CONV-P3CYC", "str", "`[DEF]` **Path-cycle interaction (CONV-P3CYC)**",
     "`[DEF]` " + rid("TDRG-DEF-CONV-P3CYC") + " **Path-cycle interaction (CONV-P3CYC)**"),
    ("E53", "TA01", "§6.3 orientation rule (b), signed definitions (TA02), no-go, G recorded", "str", ORIENT_OLD, ORIENT_NEW),
    ("E54", "TB09", "RID TDRG-DEF-CYCLE-BOUND", "str", "`[DEF]` **Cycle bound states.**",
     "`[DEF]` " + rid("TDRG-DEF-CYCLE-BOUND") + " **Cycle bound states.**"),
    ("E55", "TB09", "RID TDRG-DEF-STAR", "str", "`[DEF]` **Star blow-up**",
     "`[DEF]` " + rid("TDRG-DEF-STAR") + " **Star blow-up**"),
    ("E56", "TB09", "RID TDRG-DEF-MULTISTAR", "str", "`[DEF]` **Multistar**",
     "`[DEF]` " + rid("TDRG-DEF-MULTISTAR") + " **Multistar**"),
    ("E57", "TA01", "policy table column", "str", POLTAB_OLD, POLTAB_NEW),
    ("E58", "TB09", "RID TDRG-DEF-CANONICAL-BRANCH", "str", "`[DEF]` **Canonical clean branch:**",
     "`[DEF]` " + rid("TDRG-DEF-CANONICAL-BRANCH") + " **Canonical clean branch:**"),
    ("E59", "TB12", "§6.4 factorization tag", "str", S64_FACT_OLD, S64_FACT_NEW),
    ("E60", "TB12", "§6.4 edge-builder tag", "str", S64_EDGE_OLD, S64_EDGE_NEW),
    ("E61", "TB09", "RID TDRG-THM-REACHABILITY-K0", "str", S65_REACH_OLD, S65_REACH_NEW),
    ("E62", "TB09", "RID TDRG-ALG-LEM-REACH", "str", *rid_after("**(v2.12) LEM-REACH — band-form reachability.**",
                                                             "TDRG-ALG-LEM-REACH")),
    ("E63", "TB09", "RID TDRG-ALG-LEM-NOANNIHIL", "str", *rid_after("**(v2.12) LEM-NOANNIHIL — no free annihilation.**",
                                                                 "TDRG-ALG-LEM-NOANNIHIL")),
    ("E64", "TB09", "RID TDRG-ALG-LEM-RETRIG", "str",
     *rid_after("**(v2.12) LEM-RETRIG — two-node retrigger / binding threshold.**", "TDRG-ALG-LEM-RETRIG")),
    ("E65", "TA05", "§6.5 LEM-RETRIG least period", "str", S65_RETRIG_OLD, S65_RETRIG_NEW),
    ("E66", "TB12", "§6.5 bare RESULT paired", "str", S65_RES_OLD, S65_RES_NEW),
    ("E67", "TA05", "§6.5 regime table", "str", S65_TAB_OLD, S65_TAB_NEW),
    ("E68", "N1", "§6.6 guard: v18 orientation scope", "str", S66_GUARD_OLD, S66_GUARD_NEW),
    ("E69", "N1", "§6.6 largest_center ID tie-break", "str", S66_LC_OLD, S66_LC_NEW),
    ("E70", "TB12", "§6.6 ms_bpe tag", "str", S66_BPE_OLD, S66_BPE_NEW),
    ("E71", "N1", "§6.8 guard pointer", "str", S68_GUARD_OLD, S68_GUARD_NEW),
    ("E72", "TA04", "§6.8 fits grade", "str", S68_HEUR_OLD, S68_HEUR_NEW),
    ("E73", "TA04", "§6.8 consistency line", "str", S68_CONS_OLD, S68_CONS_NEW),
    ("E74", "TB12", "§6.8 slot-volume tags split", "str", S68_SLOT_OLD, S68_SLOT_NEW),
    ("E75", "TB12", "§6.8 TDR-24D tag", "str", S68_D_OLD, S68_D_NEW),
    ("E76", "TB12", "§6.10 heading tag", "str", S610_HEAD_OLD, S610_HEAD_NEW),
    ("E77", "TB12", "§6.10 tag", "str", S610_OLD, S610_NEW),
    ("E78", "TB12", "§6.12 heading tag", "str", S612_HEAD_OLD, S612_HEAD_NEW),
    ("E79", "TA08", "§6.12 guard: v18 orientation scope", "str", S612_GUARD_OLD, S612_GUARD_NEW),
    ("E80", "TB09", "RID TDRG-ALG-LEM-SPECCONS", "str", S612_SPEC_OLD, S612_SPEC_NEW),
    ("E81", "TA06", "LEM-SPECCONS therefore, in particular", "str", S612_EQUIV_OLD, S612_EQUIV_NEW),
    ("E82", "TB09", "RID TDRG-ALG-BIND3-CYCLE-N24K1; tag", "str", S612_CYC_OLD, S612_CYC_NEW),
    ("E83", "TB12", "d-resolved anatomy tag", "str", S612_ANAT_OLD, S612_ANAT_NEW),
    ("E84", "TA08", "§6.12 mirror-inventory wording", "str", S612_MIRROR_OLD, S612_MIRROR_NEW),
    ("E85", "TB09", "RID TDRG-NUM-BIND3-PARITY", "str", S612_PAR_OLD, S612_PAR_NEW),
    ("E86", "TB09", "RID TDRG-NUM-BIND3-SPECTRAL-GATE", "str", S612_GATE_OLD, S612_GATE_NEW),
    ("E87", "TB09", "RID TDRG-NUM-BIND3-MEMORY-PARITY", "str", S612_MEM_OLD, S612_MEM_NEW),
    ("E88", "TB09", "RID TDRG-NUM-BIND3-XFER", "str", S612_XFER_OLD, S612_XFER_NEW),
    ("E89", "TB09", "RID TDRG-NUM-BIND3-REGEN", "str", S612_REGEN_OLD, S612_REGEN_NEW),
    ("E90", "TA08", "§6.12 orientation-covariance block (fixture, equivariance, census, DISC-2, N2)", "str",
     S612_SYN_OLD, S612_SYN_NEW),
    ("E91", "TB10", "§7 imports, consumers, pins, RID map", "str", S7_OLD, S7_NEW),
    ("E92", "TB11", "§8 custody register", "block", (S8_OLD_START, S8_OLD_END), S8_NEW),
    ("E93", "TB10", "§9 repository", "str", S9_REPO_OLD, S9_REPO_NEW),
    ("E94", "TB12", "§9 policy cleanup tag", "str", S9_POL_OLD, S9_POL_NEW),
    ("E95", "TB12", "§9 edge-builder tag", "str", S9_EDGE_OLD, S9_EDGE_NEW),
    ("E96", "TB13", "Appendix A entry v2.12.14", "str", APPA_OLD, "## Appendix A — Version History {#appendix-a}\n\n"
     + APPA_ENTRY),
    ("E97", "TA01", "Appendix B row: node-ID completion", "str", APPB_OLD, APPB_NEW),
    ("E98", "TA07", "Appendix B K3 historical", "str", APPB_K3_OLD, APPB_K3_NEW),
    ("E99", "I07", "Appendix C gate", "str", APPC_GATE_OLD, APPC_GATE_NEW),
    ("E100", "I07", "Appendix C TDR-24D row", "str", APPC_D_OLD, APPC_D_NEW),
    ("E101", "TA07", "Appendix C TDR-T3 historical", "str", APPC_T3_OLD, APPC_T3_NEW),
    ("E102", "TA07", "Appendix C R0 historical", "str", APPC_R0_OLD, APPC_R0_NEW),
    ("E103", "I07", "Appendix C R2", "str", APPC_R2_OLD, APPC_R2_NEW),
    ("E104", "TB13", "footer title", "str", FOOT_TITLE_OLD, FOOT_TITLE_NEW),
    ("E105", "TB13", "footer supersedes first item", "str", FOOT_SUP_OLD, FOOT_SUP_NEW),
]


def apply_edit(text, key, mode, old, new):
    if mode == "line":
        lines = text.split("\n")
        hits = [i for i, l in enumerate(lines) if l.startswith(old)]
        assert len(hits) == 1, f"{key}: line prefix hits {len(hits)}"
        o = lines[hits[0]]
        n = new(o) if callable(new) else new
        assert n != o, f"{key}: no-op"
        lines[hits[0]] = n
        return "\n".join(lines), o, n
    if mode == "block":
        a, b = old
        assert text.count(a) == 1 and text.count(b) == 1, f"{key}: block anchors"
        i, j = text.index(a), text.index(b) + len(b)
        assert i < j
        o = text[i:j]
        return text[:i] + new + text[j:], o, new
    assert mode == "str", key
    c = text.count(old)
    assert c == 1, f"{key}: str anchor count {c}"
    assert old != new, f"{key}: no-op"
    return text.replace(old, new), old, new


def build(base_text):
    assert hashlib.sha256(base_text.encode()).hexdigest() == BASE_SHA, f"base is not adopted v2.12.13 ({BASE_TAG})"
    keys = [e[0] for e in EDITS]
    assert len(keys) == len(set(keys)), "duplicate edit keys"
    text, record = base_text, []
    for key, grp, row, mode, old, new in EDITS:
        text, o, n = apply_edit(text, key, mode, old, new)
        record.append({"key": key, "group": grp, "row": row, "mode": mode,
                       "old_sha256": hashlib.sha256(o.encode()).hexdigest(),
                       "new_sha256": hashlib.sha256(n.encode()).hexdigest(), "old": o, "new": n})
    for e in record:
        assert text.count(e["new"]) == 1, f"{e['key']}: new text not unique in the candidate (reverse check impossible)"
    declared = [r for r in NEW_RIDS if f"[RID: {r}]" in text]
    assert declared == NEW_RIDS, set(NEW_RIDS) - set(declared)
    return text, record


def main(argv):
    base, out, log = argv[1:4]
    text, record = build(open(base, "rb").read().decode("utf-8"))
    data = text.encode("utf-8")
    open(out, "wb").write(data)
    json.dump({"base_sha256": BASE_SHA, "base_tag": BASE_TAG, "candidate_sha256": hashlib.sha256(data).hexdigest(),
               "declared_new_tdrg_rids": NEW_RIDS, "check_script": CHECK_SCRIPT,
               "edit_count": len(record), "edits": record},
              open(log, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(hashlib.sha256(data).hexdigest(), len(record), "edits", len(NEW_RIDS), "new RIDs")


if __name__ == "__main__":
    main(sys.argv)
