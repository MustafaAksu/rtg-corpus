#!/usr/bin/env python3
r"""Discrete Genesis (TDR-G) v2.12.15 — scientific scope edition (one stage; no layout compaction; no rerun).

Applies to the adopted v2.12.14 file (tag tdrg-v2.12.14, sha256 3be72923...2392) the content fixed by the PI on
12 Nov 2026 ("v2.12.15 bilimsel sürümü başlatılabilir"), on the owner records
  records/tdrg/TDRG_OWNER_INBOX_DISPOSITION_20261112_claude01SKePJ.md (PR #243, §§1-4 and round 2 §7),
  the ChatGPT co-owner triage and review of 12 Nov 2026 (relayed in the session; agreement recorded in §7 there),
and the five pipes/TDRG items of 29 Oct - 12 Nov 2026.

Groups:
  N4    star event domain stated as implemented (TDRG-DEF-STAR, TDRG-DEF-MULTISTAR, CONV-TICK step 4)
  TOK   §6.13 token laws (event inventory, narrow-band classes, census law, birth injection, n-node birth-free
        conservation, not-closed counterexample, parent-child phase), credited to AZ; LEM-SPECCONS conjecture resolved
  TDR6  TDR-6 PARTIAL; OPEN-SPECCONS-STAR current status; SG-12
  P     SG-3, TDR-6 P row, Appendix B: P not conserved at births, not a gauge quantity (OFN finding)
  GATE  §7 export row TDRG-EXPORT-DISCRETE-TRIAD on the A -> B -> C gate (Programme v1.4 notice)
  PINS  header companions, §7 imports/context/consumers/pins, §6.2 AZ citation (OFN v0.12, AZ v0.7, Programme v1.4)
  REG   RIDs, §7 RID map rows, §8 artifact, Appendix A entry, header, status summary, footer
Rules as in build_tdrg_v2_12_14.py: base must be the adopted bytes; "line" = unique line prefix, whole line
replaced; "str" = unique substring; "block" = unique start/end anchors; every new text unique in the candidate.
usage: build_tdrg_v2_12_15.py BASE OUT EDITLOG_JSON   (BASE = git show tdrg-v2.12.14:dsn/RTG_DISCRETE_GENESIS_DSN.md)
"""
import hashlib, json, sys

BASE_SHA = "3be72923cd40523399363e0dc044bba6246862d12b2bca190c74969e2cce2392"
BASE_TAG = "tdrg-v2.12.14"
CHECK_SCRIPT = "evidence/tdrg/scripts/check_tdrg_v2_12_15.py"
NEW_RIDS = [
    "TDRG-ALG-EVENT-INVENTORY", "TDRG-ALG-NARROW-BAND-CLASSES", "TDRG-ALG-TOKEN-CENSUS-LAW",
    "TDRG-ALG-BIRTH-SPECTRUM-INJECTION", "TDRG-ALG-SPECCONS-N", "TDRG-ALG-BIRTH-SPECTRUM-NOT-CLOSED",
    "TDRG-ALG-PARENT-CHILD-PHASE", "TDRG-NUM-TOKEN-LAW-CHECK", "TDRG-ART-TOKEN-LAW-CHECKS",
]
def rid(r):
    assert r in NEW_RIDS, r
    return f"[RID: {r}]"

AZ_SRC = ("`records/az/AZ_TOKEN_RESONANCE_PREREGISTRATION.md` §2 (SHA-256 `198d2f4a…fb829`; Propositions 1–3, "
          "Corollaries 1.1–1.2)")
OWNER_REC = "`records/tdrg/TDRG_OWNER_INBOX_DISPOSITION_20261112_claude01SKePJ.md`"

# ---------------------------------------------------------------------------------------------------- header
H_TITLE = "# RTG_DISCRETE_GENESIS_DSN_v2.12.15"
H_DATE = ("**Date:** November 2026 (v2.12.15, scientific scope edition: star event domain stated as implemented, token "
          "laws, TDR-6 partial; the scientific content of the v2.12 line is otherwise dated June 2026)  ")
H_SUP = ("**Supersedes:** `RTG_DISCRETE_GENESIS_DSN_v2.12.14` (tag `tdrg-v2.12.14`, SHA-256 "
         "`3be72923cd40523399363e0dc044bba6246862d12b2bca190c74969e2cce2392`); the earlier lineage is in the footer and "
         "Appendix A (compaction is v2.13 work)  ")
H_COMP = ("**Companion documents (governing editions, November 2026):** Programme Overview v1.4 (`programme-v1.4`) · "
          "Ontological Foundations v0.12 (`ofn-v0.12`) · DSN Methodology v1.4 (`methodology-v1.4`). Claim-specific "
          "historical pins (Programme v1.1, OFN v0.6/v0.7) stay where a statement cites them.  ")
H_METH = ("**DSN Methodology:** DSN_METHODOLOGY_v1.2 (declared; kept for the v2.12.x line by PI decision of 27 Oct 2026 "
          "— the v1.4 migration is v2.13)  ")
SS_OLD = "results computed with the superseded completion keep `[conv: v18 path orientation]` and `EV-NOT-RERUN` (census bound, §6.12)."
SS_NEW = (SS_OLD + " **v2.12.15 (scientific scope edition):** the star event is stated on the domain the dynamics always "
          "used — every component with exactly one valid centre, any shape (owner finding N4); the token-alphabet and "
          "census law, the exact birth update of the advance spectrum, the $n$-node birth-free spectrum conservation "
          "(resolving the LEM-SPECCONS conjecture) and a parent–child phase law are registered as `[ALG]` (§6.13, "
          "proposed by AZ, verified on the pinned engine); TDR-6 is PARTIAL; $P$ is reworded (not conserved at births, "
          "not a gauge quantity).")

# ---------------------------------------------------------------------------------------------------- §2
TDR6_STATUS_OLD = "Status: ACTIVE  \nQuestion: Identify a purely relational invariant preserved (or predictably changed) across star blow-up."
TDR6_STATUS_NEW = ("Status: ACTIVE — PARTIAL *(v2.12.15)*  \nQuestion: Identify a purely relational invariant preserved "
                   "(or predictably changed) across star blow-up.")
TDR6_P_OLD = "- Total additive momentum $P$: `[FAIL]` — gauge artifact."
TDR6_P_NEW = ("- Total additive momentum $P$: `[FAIL]` as a birth invariant — it changes by $-x$ at a birth with centre "
              "token $x$; it is invariant under the declared gauge, so not a gauge artifact (SG-3, v2.12.15 `[COR]`).")
TDR6_D_OLD = "- Pairwise difference multiset: `[OPEN]`"
TDR6_D_NEW = ("- Token census and pairwise difference multiset: **predictable-change law** `[ALG]` *(v2.12.15)* — "
              "TDRG-ALG-TOKEN-CENSUS-LAW and TDRG-ALG-BIRTH-SPECTRUM-INJECTION (§6.13): exact, given the centre token(s) "
              "and the token census; the multiset alone does not determine its update "
              "(TDRG-ALG-BIRTH-SPECTRUM-NOT-CLOSED). The sub-item is resolved in that form: the full pairwise-advance "
              "spectrum is not preserved at births, and $D_{t+1}$ is not a function of $D_t$ alone, so no closed update "
              "law computable from $D_t$ exists.\n"
              "- Signed-class set $\\mathcal I(X_t)=\\{[\\delta_i]_\\pm: i\\in V_t\\}$, $[x]_\\pm=\\{x,-x\\}$: "
              "**exactly invariant** `[ALG]` *(v2.12.15)* — TDRG-ALG-TOKEN-CENSUS-LAW (iii): preserved at every tick, "
              "births included, for all six policies; a token-state quantity, unchanged by the declared phase gauge and by "
              "relabelling (SG-14). Whether it meets the purely relational condition of this question is undecided, so it "
              "does not close TDR-6. Pointed out by the ChatGPT co-owner change-focused review (PR #250).")
SPEC_STAR_OLD = "Either outcome is valuable; neither is assumed (SG-12)."
SPEC_STAR_NEW = (SPEC_STAR_OLD + "\n\n**Current status (v2.12.15):** the birth update is exact "
                 "(TDRG-ALG-BIRTH-SPECTRUM-INJECTION) and the token support is fixed at $t=0$ "
                 "(TDRG-ALG-TOKEN-CENSUS-LAW): a birth extends the spectrum by an explicit injection that depends on the "
                 "centre token and the census, not on the spectrum alone (TDRG-ALG-BIRTH-SPECTRUM-NOT-CLOSED). This is a "
                 "characterized extension law for each birth. Still open: a spectrum-level quantity preserved across births, or "
                 "updated by a law closed on the spectrum (the token-level invariant of TDRG-ALG-TOKEN-CENSUS-LAW (iii) is not "
                 "a function of the spectrum), and which centre tokens fire (a dynamical question). Status stays ACTIVE.")

# ---------------------------------------------------------------------------------------------------- §3
SG3_OLD = "**[SG-3]** Total additive momentum $P = \\sum \\delta_i$ is not a physical observable.  "
SG3_NEW = ("**[SG-3]** Total additive momentum $P = \\sum \\delta_i$ is not adopted as a physical observable. *(v2.12.15 "
           "`[COR]`; OFN finding `pipes/TDRG/20261029-OFN-token-sum-gauge-label.md`)* $P$ is not conserved across star "
           "births — a birth at centre token $x$ changes it by $-x \\pmod N$ (TDRG-ALG-BIRTH-SPECTRUM-INJECTION) — and "
           "it is invariant under the declared phase gauge (SG-2) and under relabelling (SG-14), so it is not a gauge "
           "quantity; the earlier labels \"gauge-like\" and \"gauge artifact\" gave a wrong reason.  ")
SG3V_OLD = "Violation: Using $P$-conservation as a constraint on interaction rules. ($P$ is gauge-like; $P$ changes under birth.)"
SG3V_NEW = "Violation: Using $P$-conservation as a constraint on interaction rules; calling $P$ a gauge quantity."
SG12_OLD = ("Star blow-up creates a new node and new pairwise advances; spectrum conservation (or any controlled extension) "
            "across star blow-up is `[OPEN]` and must not be assumed.")
SG12_NEW = ("*(v2.12.15)* Its $n$-node birth-free form is TDRG-ALG-SPECCONS-N; across a birth the update is exact but "
            "needs the centre token and the census (TDRG-ALG-BIRTH-SPECTRUM-INJECTION, "
            "TDRG-ALG-BIRTH-SPECTRUM-NOT-CLOSED). Spectrum conservation across births, or a spectrum-level invariant of the "
            "full dynamics, is `[OPEN]` and must not be assumed.")

# ---------------------------------------------------------------------------------------------------- §6.2, §6.3
AZCIT_OLD = "`AZ-ALG-ANTIPODAL-LOWORDER` (`az-v0.6`) is the same"
AZCIT_NEW = "`AZ-ALG-ANTIPODAL-LOWORDER` (`az-v0.7`; statement unchanged from `az-v0.6`) is the same"
STEP4_OLD = "4. Classify each component as isolated edge, path, cycle, clean star, multistar, or tie."
STEP4_NEW = ("4. Classify each component, in this order: no edge (isolated node); single edge; single-star component "
             "(exactly one valid centre, TDRG-DEF-STAR); multistar (two or more valid centres); path; cycle. *(v2.12.15 "
             "`[COR]`: the precedence as implemented; ties are outcomes of the path rule, not a class; under the narrow "
             "band no other class occurs, TDRG-ALG-NARROW-BAND-CLASSES.)*")
STAR_PREFIX = "`[DEF]` [RID: TDRG-DEF-STAR] **Star blow-up** ($K_{1,3}$"
STAR_NEW = (
    "`[DEF]` [RID: TDRG-DEF-STAR] **Star blow-up** *(v2.12.15 `[COR]` — event domain stated as implemented; owner finding "
    "N4)*. A **valid centre** of a defect component is a node with at least three defect neighbours that are pairwise "
    "non-adjacent; under the narrow band every node of defect degree $\\ge3$ is one (TDRG-ALG-NARROW-BAND-CLASSES). A "
    "**single-star component** is a component with exactly one valid centre $A$: the pure stars $K_{1,m}$ ($m\\ge3$, "
    "$K_{1,3}$ the minimal case) and every other shape with one such node — trees with longer branches, and components "
    "containing a cycle. Blow-up: a new node $E$ is created at $\\theta_E = (\\theta_A + N/2) \\bmod N$ with "
    "$\\delta_E = \\delta_A$, and the centre inverts, $\\delta_A \\mapsto -\\delta_A \\bmod N$, both read from the "
    "CONV-TICK snapshot; every other node of the component is inert for that tick. **Superseded wording:** v2.12.14 and "
    "earlier stated the event on $K_{1,3}$ only. The pinned engines (`star_centers`, `classify_component`, "
    "`blow_up_star_with_snapshot`) and every TDR-G result — the microscopic birth law included, whose counter "
    "`clean_star_components` counts every single-star component — used the domain stated here. The correction widens "
    "the declared event domain of the model to the rule the dynamics always applied; no result changes (`EV-CODE`; in a "
    "mixed-policy owner sample 3,773 of 17,466 single-star events were not pure stars, TDRG-NUM-TOKEN-LAW-CHECK).")
MS_PREFIX = "`[DEF]` [RID: TDRG-DEF-MULTISTAR] **Multistar**"
MS_NEW = ("`[DEF]` [RID: TDRG-DEF-MULTISTAR] **Multistar** (two or more valid centres, any shape; *v2.12.15 `[COR]`: stated "
          "with the precision of TDRG-DEF-STAR*): a component with several equally valid blow-up centres. Policy fork "
          "required (table below): `trap` and the `bound_*` policies leave it inert; `largest_center` fires one centre "
          "(TDRG-ALG-LARGEST-CENTER-ID-TIEBREAK); `all_centers` fires every centre, each against the snapshot.")
SPECC_OLD = ("**Generalization:** $n$-node signed-permutation invariance is conjectured for swap/path-cycle sectors; **star "
             "blow-up creates a new node and new pairwise advances and is `[OPEN]` (SG-12)**.")
SPECC_NEW = ("**Generalization** *(v2.12.15 `[COR]`)*: the $n$-node birth-free statement is proved, TDRG-ALG-SPECCONS-N "
             "(§6.13), replacing the former conjecture; across star blow-up the update is exact but not determined by the "
             "spectrum (TDRG-ALG-BIRTH-SPECTRUM-INJECTION, TDRG-ALG-BIRTH-SPECTRUM-NOT-CLOSED), and a spectrum-level "
             "invariant of the full dynamics is `[OPEN]` (SG-12).")

# ---------------------------------------------------------------------------------------------------- §6.13
S613_ANCHOR = "\n\n---\n\n## §7. Import Ledger {#sec-7-imports}"
S613 = (
    "\n\n### §6.13 Token Alphabet and Birth Laws `[ALG]` {#sec-6-13-tokens} *(new in v2.12.15)*\n\n"
    "> **[SG-12 applies.]** These are statements about tokens and the unlabelled advance spectrum under the event rules of "
    "§6.3. They describe the token and spectrum updates exactly; none closes TDR-6 or OPEN-SPECCONS-STAR, and none "
    "is a growth mechanism or a bridge (SG-10). Sources: "
    "proposed by the AZ co-owner, " + AZ_SRC + ", offered as `pipes/TDRG/20261112-AZ-token-alphabet-law-offer.md`; "
    "verified by the TDR-G owner sessions (" + OWNER_REC + ", §3 and §7) and registered here as TDR-G results, credited "
    "to AZ. AZ's registered Stage 1 campaign and its numbers are not part of them.\n\n"
    "`[ALG]` " + rid("TDRG-ALG-EVENT-INVENTORY") + " `[scope: the six policies of §6.3, either orientation rule]` "
    "**Token-changing events (E).** In one tick the tokens change only by (a) a permutation of the tokens of one "
    "component (antipodal swap; path successor shift), (b) identity (isolated nodes, balanced path ties, cycle bound "
    "states, multistars under `trap` and the `bound_*` policies, every non-centre node of a star component), or (c) the "
    "star map at a valid centre with snapshot token $x$: centre $x\\mapsto-x$, newborn $x$. Snapshot components are "
    "disjoint, so no node is written by two events in one tick, and the several centres of one tick (several "
    "single-star components, or `all_centers`) are distinct nodes read from the snapshot. *Proof:* the DEFs of §6.3 "
    "under CONV-TICK. ∎ `[ENG]` conformance: the pinned engines write tokens in exactly three places — "
    "`apply_single_edge_swap`, `apply_path_cycle`, `blow_up_star_with_snapshot` — and the node cap ends a run before a "
    "step instead of suppressing a birth inside one (`EV-CODE`, " + OWNER_REC + " §3.1).\n\n"
    "`[ALG]` " + rid("TDRG-ALG-NARROW-BAND-CLASSES") + " **Under the narrow band every component with an edge has a "
    "class.** If $k<N/6$, a node of defect degree $\\ge3$ is a valid centre (two adjacent neighbours would close a fully "
    "defective $K_3$, excluded by TDRG-THM-NARROW-BAND-EXCLUSION); a connected graph of maximum degree $\\le2$ is a path or "
    "a cycle, and $C_3$ is excluded. ∎ So the engine's residual classes (`triangle_forbidden_or_wideband`, `ambiguous_*`) "
    "are empty under the narrow band, and the precedence of CONV-TICK step 4 is a complete classification.\n\n"
    "`[ALG]` " + rid("TDRG-ALG-TOKEN-CENSUS-LAW") + " **Signed token alphabet and census law.** Let $A_0$ be the set of "
    "initial tokens, $S_0=A_0\\cup(-A_0)$, and $c_t(y)$ the number of nodes with token $y$ at tick $t$. Under "
    "TDRG-ALG-EVENT-INVENTORY: (i) $\\delta_i(t)\\in S_0$ for every node and tick, so at most $|S_0|\\le2|A_0|$ distinct "
    "tokens ever occur; (ii) a tick whose births have centre snapshot tokens $x_1,\\dots,x_m$ changes the census by "
    "$c_{t+1}(y)-c_t(y)=\\#\\{a: y\\equiv-x_a\\}$, so $c_t$ is coordinatewise non-decreasing and $\\sum_y c_t(y)=M_t$; "
    "(iii) the set of signed classes present, $\\mathcal I(X_t)=\\{[\\delta_i]_\\pm\\}$ with $[x]_\\pm=\\{x,-x\\}$, is "
    "invariant at every tick, births included: $\\mathcal I(X_t)=\\{[a]_\\pm: a\\in A_0\\}$. "
    "*Proof.* (a) and (b) leave the multiset of tokens unchanged; in (c) the centre's $x$ becomes $-x$ and the newborn adds "
    "$x$, a net gain of one $-x$; distinct centres compose; (i) follows by induction because $S_0=-S_0$. (iii): by (ii) no "
    "token count decreases, so no class disappears, and a birth adds only $-x$, whose class $[x]_\\pm$ is already present "
    "at the centre. ∎ The object is the global multiset, not node identity: the centre's own token is not conserved. Item "
    "(iii) was pointed out by the ChatGPT co-owner change-focused review (PR #250).\n\n"
    "`[ALG]` " + rid("TDRG-ALG-BIRTH-SPECTRUM-INJECTION") + " **Birth update of the advance spectrum.** Let $C_t$ be the "
    "token multiset before the tick and $D(C)$ the multiset of $|y-y'|_c$ over unordered pairs of $C$. With births at "
    "centre snapshot tokens $x_1,\\dots,x_m$: $C_{t+1}=C_t\\uplus\\{-x_1,\\dots,-x_m\\}$ and "
    "$$D(C_{t+1})=D(C_t)\\uplus\\{|x_a+y|_c: 1\\le a\\le m,\\ y\\in C_t\\}\\uplus\\{|x_a-x_b|_c: a<b\\},$$ "
    "which adds $mM_t+\\binom m2$ entries; the token sum changes by $-\\sum_a x_a \\pmod N$. *Proof:* census law (ii) and "
    "$|{-x_a}-y|_c=|x_a+y|_c$. ∎ This is an identity of unlabelled multisets, not a list of edges at the newborn: the "
    "centre's own differences change ($|x-y|_c\\to|x+y|_c$) and the identity holds only after the centre's and the "
    "newborn's contributions are combined. Applying the one-birth form $m$ times against the pre-tick multiset would miss "
    "the newborn–newborn pairs.\n\n"
    "`[ALG]` " + rid("TDRG-ALG-SPECCONS-N") + " **$n$-node birth-free conservation.** On any tick without a star event, for "
    "any number of nodes, the token multiset and hence $\\{|d_{ij}|_c\\}_{i<j}$ are exactly conserved. *Proof:* only "
    "events (a) and (b) occur. ∎ This proves the $n$-node generalization that LEM-SPECCONS recorded as conjectured (§6.12); "
    "for three nodes it is LEM-SPECCONS.\n\n"
    "`[ALG]` " + rid("TDRG-ALG-BIRTH-SPECTRUM-NOT-CLOSED") + " **The spectrum alone does not determine its birth "
    "update.** At $N=24$, $C=(1,3,4,5)$ and $C'=(2,4,5,6)$ have $D(C)=D(C')=\\{1,1,2,2,3,4\\}$; a birth at the centre "
    "with token $1$, respectively $2$, adds $\\{2,4,5,6\\}$, respectively $\\{4,6,7,8\\}$. Both are realised on the pinned "
    "engine with one geometry ($k=1$, post-advance $\\theta=(0,11,12,13)$, a $K_{1,3}$ at centre 0; fixture F2 of "
    "TDRG-NUM-TOKEN-LAW-CHECK). So $D_{t+1}$ is not a function of $D_t$: the update needs the centre token(s) and the "
    "census. $C'=C+1$ is a common token shift: $D$ is shift-invariant and the star map is not (imported Finding A, §7). "
    "Counterexample from the ChatGPT co-owner review (" + OWNER_REC + " §7.2).\n\n"
    "`[ALG]` " + rid("TDRG-ALG-PARENT-CHILD-PHASE") + " `[scope: two-body kinematics under a token-persistence "
    "hypothesis]` **Free parent–child phase law and order classification.** If a star event at tick $t_0$ has centre $A$ "
    "with snapshot token $x$ and newborn $E$, and the next $j$ advances use $\\delta_A=-x$ and $\\delta_E=x$, then after "
    "the advance of tick $t_0+j$, $\\theta_E-\\theta_A\\equiv N/2+2jx \\pmod N$. *Proof:* the separation is $N/2$ at birth "
    "(TDRG-DEF-STAR) and each advance adds $2x$. ∎ Along the free orbit — the hypothesis holding for every $j\\ge0$ — "
    "the separation stays in $\\{N/2,0\\}$ for all $j$ iff $4x\\equiv0 \\pmod N$; already $j=1$ forces "
    "$2x\\in\\{0,N/2\\}$, so the same holds on any window with at least one advance, while a window with no advance "
    "imposes no condition. Equivalently $\\operatorname{ord}(2x)\\le2$: "
    "$\\operatorname{ord}(2x)=1$ iff $x\\in\\{0,N/2\\}$, and $\\operatorname{ord}(2x)=2$ iff $4\\mid N$ and "
    "$x\\in\\{N/4,3N/4\\}$; for $N\\equiv2 \\pmod 4$ no token has order 2. This is a kinematic identity, not a "
    "bond-persistence or growth mechanism: in a many-node universe further events usually break the hypothesis, and it "
    "has no bearing on TDRG-OPEN-LOCKING-FAIL or TDR-26.\n\n"
    "`[NUM]` " + rid("TDRG-NUM-TOKEN-LAW-CHECK") + " `[scope: pinned v18 engine with TDRG-DEF-ORIENT; six policies × "
    "(N,k) ∈ {(24,1),(30,2),(60,4),(120,8)} × 30 random four-node starts, up to 400 ticks or 70 nodes]` **Owner check of "
    "the token laws on the engine.** 223,651 ticks (21,838 with births; 33,121 births): census law and alphabet on every "
    "tick, birth injection on every birth tick ($M_{\\rm post}$ up to 136), birth-free conservation on all 201,813 "
    "birth-free ticks, and the phase law on 765,224 parent–child advances with the parent taken from the engine's own "
    "birth call — 0 violations. Single-star events in the same sample: 17,466, of which pure $K_{1,3}$ 4,648, pure "
    "$K_{1,m}$ with $m\\ge4$ 9,045, and not pure 3,773 (trees 1,944; containing a cycle 1,829); the shares in the "
    "canonical scans are not measured. Fixtures: F1 (a five-node tailed tree blown up as a single star) and F2 (above). "
    "Evidence: `evidence/tdrg/inbox_20261112/owner_token_law_check_v2.py` (`491cee3b…`), output "
    "`owner_token_law_check_v2_output.json` (`acbc55db…`). AZ's own machine checks (exhaustive at $N=6,k=0$ and "
    "$N=8,k=1$, 16 ticks) are `EV-SRC-REPORTED`. A finite check, not a proof.")

# ---------------------------------------------------------------------------------------------------- §7
IMP_OLD = "[import: RTG_ONTOLOGICAL_FOUNDATIONS_v0.10 §4.1 | RTG-OFN-ALG-STAR-TOKEN-SHIFT]"
IMP_NEW = "[import: RTG_ONTOLOGICAL_FOUNDATIONS_v0.12 §4.1 | RTG-OFN-ALG-STAR-TOKEN-SHIFT]"
IMPU_OLD = "OFN REQ-O09-05 is answered by TDRG-DEF-ORIENT (endpoint policy) and this entry."
IMPU_NEW = (IMPU_OLD + " *(v2.12.15: repinned from `ofn-v0.10` to `ofn-v0.12`; the statement text is byte-identical at "
            "both tags, only OFN's scope tag changed. Also cited by TDRG-ALG-BIRTH-SPECTRUM-NOT-CLOSED.)*\n"
            "- Contributions registered as TDR-G results, not imports *(v2.12.15)*: the token laws of §6.13, proposed by AZ "
            "(" + AZ_SRC + ") and verified by the owner; the RIDs are TDR-G's, credited to AZ.")
CTX_OLD = ("- Context only (not imported): Programme Overview v1.3 SG-PROG-1–SG-PROG-4; OFN v0.10 O0–O3 motivational layer")
CTX_NEW = ("- Context only (not imported): Programme Overview v1.4 SG-PROG-1–SG-PROG-4; OFN v0.12 O0–O3 motivational layer")
CONS_START = "| Consumer (edition) | What it uses | State at v2.12.14 | Effect of v2.12.14 |"
CONS_END = "| Genesis (Programme IF25) | `TDRG-EXPORT-POLICY-PHASE` | blocked (below) | none |"
CONS_NEW = (
    "| Consumer (edition) | What it uses | State at v2.12.15 | Effect of v2.12.15 |\n"
    "|---|---|---|---|\n"
    "| NUMGEN v1.21 (`numgen-v1.21`) | state, recurrence and event conventions for DISC-1/DISC-2; TDRG-DEF-ORIENT | request "
    "closed (accept, v2.12.14) | none on its panels: the event domain they ran on is unchanged (TDRG-DEF-STAR states it) |\n"
    "| OFN v0.12 (`ofn-v0.12`) | IMP-O08-02 to IMP-O08-16 (owner RIDs); Finding A (XFER-O08-01); token-sum finding "
    "`pipes/TDRG/20261029-OFN-token-sum-gauge-label.md` | Finding A statement accepted (repinned); token-sum finding "
    "dispositioned (accept with change) | SG-3, TDR-6 and Appendix B reworded on $P$; custody transfer still deferred to "
    "v2.13 |\n"
    "| AZ v0.7 (`az-v0.7`) | Threads B/C: state, LEM-REACH, LEM-RETRIG, LEM-SPECCONS; token-alphabet offer "
    "`pipes/TDRG/20261112-AZ-token-alphabet-law-offer.md` | v0.7 notice closed (no action); offer dispositioned (accept "
    "with change) | token laws registered in §6.13, credited to AZ; §6.2 citation at `az-v0.7` |\n"
    "| Programme v1.4 (`programme-v1.4`) | §6.4 TDRG entry and launch gate; IF03, IF13, IF25 | notice dispositioned "
    "(accept) | `TDRG-EXPORT-DISCRETE-TRIAD` names the A → B → C gate; companion pin `programme-v1.4` |\n"
    "| Genesis (Programme IF25) | `TDRG-EXPORT-POLICY-PHASE` | blocked (below) | none |")
PINS_OLD = ("**Pins.** Governing editions at this release: Programme Overview v1.3, OFN v0.10, DSN Methodology v1.4 (this "
            "edition still declares v1.2; the migration is v2.13).")
PINS_NEW = ("**Pins.** Governing editions at this release: Programme Overview v1.4, OFN v0.12, AZ v0.7, DSN Methodology "
            "v1.4 (this edition still declares v1.2; the migration is v2.13).")
MAP_HDR_OLD = "**Owner RID map** (v2.12.14)."
MAP_HDR_NEW = "**Owner RID map** (v2.12.14; rows for v2.12.15 added at the end)."
MAP_LAST = "| TDRG-ART-SESSION-SCRIPTS, TDRG-ART-ORIENT-V2-12-14, TDRG-ART-ORIENT-COVARIANCE-CHECKS | artifacts | §8 | — |"
MAP_NEW = (MAP_LAST + "\n"
    "| TDRG-ALG-EVENT-INVENTORY, TDRG-ALG-NARROW-BAND-CLASSES | token-changing events (E); complete classification "
    "under the narrow band | §6.13 | AZ \"(E)\" |\n"
    "| TDRG-ALG-TOKEN-CENSUS-LAW | signed token alphabet and census law | §6.13 | AZ Proposition 1 |\n"
    "| TDRG-ALG-BIRTH-SPECTRUM-INJECTION | birth update of the advance spectrum | §6.13 | AZ Corollary 1.1 |\n"
    "| TDRG-ALG-SPECCONS-N | $n$-node birth-free spectrum conservation | §6.13 | AZ Corollary 1.2 |\n"
    "| TDRG-ALG-BIRTH-SPECTRUM-NOT-CLOSED | spectrum does not determine its birth update | §6.13 | — |\n"
    "| TDRG-ALG-PARENT-CHILD-PHASE | free parent–child phase law; order classification | §6.13 | AZ Propositions 2–3 |\n"
    "| TDRG-NUM-TOKEN-LAW-CHECK, TDRG-ART-TOKEN-LAW-CHECKS | owner check of the token laws; its artifacts | §6.13, §8 | — |")
EXP_OLD = ("- [RID: TDRG-EXPORT-DISCRETE-TRIAD] :: Native discrete triad orientation / survival statistics for TDR-T :: "
           "blocked by TDR-24D/A/B and TDR-T0.")
EXP_NEW = ("- [RID: TDRG-EXPORT-DISCRETE-TRIAD] :: Native discrete triad orientation / survival statistics for TDR-T :: "
           "blocked by TDR-24A → TDR-24B → TDR-24C and TDR-T0 (TDR-24D and TDR-24F are closed at the mechanism level, "
           "§1). *(v2.12.15 `[COR]`: the row named the earlier D/A/B gate; Programme v1.4 §6.4 notice.)*")

# ---------------------------------------------------------------------------------------------------- §8, App. A, App. B, footer
ART_ANCHOR = "- Post-edition data, not cited by any claim here:"
ART_NEW = ("- " + rid("TDRG-ART-TOKEN-LAW-CHECKS") + " :: `evidence/tdrg/inbox_20261112/` (owner token-law checks v1 "
           "and v2 with fixtures F1–F2; `SHA256SUMS.txt`) and the v2.12.15 builder and checker "
           "(`evidence/tdrg/scripts/build_tdrg_v2_12_15.py`, `check_tdrg_v2_12_15.py`) :: evidence for §6.3 (N4) and "
           "§6.13 :: `[ENG]` **placed**.\n" + ART_ANCHOR)
APPB_OLD = "- [FAIL] Total additive momentum $P = \\sum \\delta_i$ as a conserved physical observable — gauge artifact."
APPB_NEW = ("- [FAIL] Total additive momentum $P = \\sum \\delta_i$ as a conserved physical observable — not conserved "
            "across births ($\\Delta P\\equiv-x$ for centre token $x$). *(v2.12.15 `[COR]`: formerly \"gauge artifact\"; $P$ "
            "is invariant under the declared gauge, SG-3.)*")
APPA_OLD = "## Appendix A — Version History {#appendix-a}\n\n### v2.12.14 — October 2026"
APPA_NEW = (
    "## Appendix A — Version History {#appendix-a}\n\n"
    "### v2.12.15 — November 2026\n\n"
    "Scientific scope edition on the PI's decision of 12 Nov 2026 (Methodology v1.2 kept as declared; no layout "
    "compaction; no rerun). Predecessor `tdrg-v2.12.14` (SHA-256 `3be72923…2392`). Release record "
    "`records/tdrg/TDRG_v2_12_15_RELEASE_RECORD.md`; owner record " + OWNER_REC + "; edit log "
    "`evidence/tdrg/v2.12.15/edit_log.json`.\n"
    "- **§6.3 [COR]:** TDRG-DEF-STAR states the event domain as implemented — every component with exactly one valid "
    "centre, any shape, only the centre and the newborn changing (owner finding N4); TDRG-DEF-MULTISTAR aligned; "
    "CONV-TICK step 4 gives the classification precedence.\n"
    "- **§6.13 [NEW]:** token laws — TDRG-ALG-EVENT-INVENTORY, -NARROW-BAND-CLASSES, -TOKEN-CENSUS-LAW, "
    "-BIRTH-SPECTRUM-INJECTION, -SPECCONS-N, -BIRTH-SPECTRUM-NOT-CLOSED, -PARENT-CHILD-PHASE; owner check "
    "TDRG-NUM-TOKEN-LAW-CHECK. Proposed by AZ, verified by the owner, credited to AZ.\n"
    "- **§6.12 [COR]:** the LEM-SPECCONS $n$-node conjecture resolved by TDRG-ALG-SPECCONS-N.\n"
    "- **§2 [COR]:** TDR-6 PARTIAL (the pairwise-multiset sub-item resolved as a predictable-change law; the signed-class "
    "set registered as an exact invariant, its relational status undecided — ChatGPT co-owner review, PR #250); "
    "OPEN-SPECCONS-STAR current status.\n"
    "- **§3 [COR]:** SG-3 — $P$ not conserved at births and not a gauge quantity (OFN finding); SG-12 updated.\n"
    "- **§7 [COR]:** export row `TDRG-EXPORT-DISCRETE-TRIAD` on the A → B → C gate (Programme v1.4 notice); Finding A "
    "repinned to `ofn-v0.12`; consumers, context and pins at Programme v1.4, OFN v0.12, AZ v0.7; RID map rows.\n"
    "- **§6.2, §8, header, Appendix B [COR/NEW]:** AZ citation at `az-v0.7`; TDRG-ART-TOKEN-LAW-CHECKS; companion editions; "
    "$P$ row reworded.\n"
    "- **Not changed:** every number of earlier editions; the engine; Appendix A history; layout (v2.13).\n\n"
    "### v2.12.14 — October 2026")
FOOT_OLD = "*END OF DOCUMENT — RTG_DISCRETE_GENESIS_DSN_v2.12.14*"
FOOT_NEW = "*END OF DOCUMENT — RTG_DISCRETE_GENESIS_DSN_v2.12.15*"
FSUP_OLD = "*Supersedes RTG_DISCRETE_GENESIS_DSN_v2.12.13 (tag `tdrg-v2.12.13`),"
FSUP_NEW = ("*Supersedes RTG_DISCRETE_GENESIS_DSN_v2.12.14 (tag `tdrg-v2.12.14`), RTG_DISCRETE_GENESIS_DSN_v2.12.13 (tag "
            "`tdrg-v2.12.13`),")

EDITS = [
    ("E01", "REG", "header title", "line", "# RTG_DISCRETE_GENESIS_DSN_v2.12.14", H_TITLE),
    ("E02", "REG", "header date", "line", "**Date:**", H_DATE),
    ("E03", "REG", "header supersedes", "line", "**Supersedes:**", H_SUP),
    ("E04", "PINS", "header companion editions", "line", "**Companion documents", H_COMP),
    ("E05", "PINS", "header declared methodology", "line", "**DSN Methodology:**", H_METH),
    ("E06", "REG", "status summary sentence", "str", SS_OLD, SS_NEW),
    ("E07", "TDR6", "TDR-6 status PARTIAL", "str", TDR6_STATUS_OLD, TDR6_STATUS_NEW),
    ("E08", "P", "TDR-6 P row", "str", TDR6_P_OLD, TDR6_P_NEW),
    ("E09", "TDR6", "TDR-6 pairwise multiset row", "str", TDR6_D_OLD, TDR6_D_NEW),
    ("E10", "TDR6", "OPEN-SPECCONS-STAR current status", "str", SPEC_STAR_OLD, SPEC_STAR_NEW),
    ("E11", "P", "SG-3", "line", "**[SG-3]**", SG3_NEW),
    ("E12", "P", "SG-3 violation", "str", SG3V_OLD, SG3V_NEW),
    ("E13", "TDR6", "SG-12", "str", SG12_OLD, SG12_NEW),
    ("E14", "PINS", "§6.2 AZ citation at az-v0.7", "str", AZCIT_OLD, AZCIT_NEW),
    ("E15", "N4", "CONV-TICK step 4 precedence", "str", STEP4_OLD, STEP4_NEW),
    ("E16", "N4", "TDRG-DEF-STAR event domain", "line", STAR_PREFIX, STAR_NEW),
    ("E17", "N4", "TDRG-DEF-MULTISTAR", "line", MS_PREFIX, MS_NEW),
    ("E18", "TOK", "LEM-SPECCONS conjecture resolved", "str", SPECC_OLD, SPECC_NEW),
    ("E19", "TOK", "§6.13 token laws", "str", S613_ANCHOR, S613 + S613_ANCHOR),
    ("E20", "PINS", "§7 Finding A repinned", "str", IMP_OLD, IMP_NEW),
    ("E21", "PINS", "§7 import note and contributions", "str", IMPU_OLD, IMPU_NEW),
    ("E22", "PINS", "§7 context editions", "str", CTX_OLD, CTX_NEW),
    ("E23", "PINS", "§7 consumers table", "block", (CONS_START, CONS_END), CONS_NEW),
    ("E24", "PINS", "§7 pins", "str", PINS_OLD, PINS_NEW),
    ("E25", "REG", "§7 RID map header", "str", MAP_HDR_OLD, MAP_HDR_NEW),
    ("E26", "REG", "§7 RID map rows", "str", MAP_LAST, MAP_NEW),
    ("E27", "GATE", "§7 export row gate", "str", EXP_OLD, EXP_NEW),
    ("E28", "REG", "§8 token-law artifacts", "str", ART_ANCHOR, ART_NEW),
    ("E29", "REG", "Appendix A entry", "str", APPA_OLD, APPA_NEW),
    ("E30", "P", "Appendix B P row", "str", APPB_OLD, APPB_NEW),
    ("E31", "REG", "footer title", "str", FOOT_OLD, FOOT_NEW),
    ("E32", "REG", "footer supersedes", "str", FSUP_OLD, FSUP_NEW),
]


def apply_edit(text, key, mode, old, new):
    if mode == "line":
        lines = text.split("\n")
        hits = [i for i, l in enumerate(lines) if l.startswith(old)]
        assert len(hits) == 1, f"{key}: line prefix hits {len(hits)}"
        o = lines[hits[0]]
        assert new != o, f"{key}: no-op"
        lines[hits[0]] = new
        return "\n".join(lines), o, new
    if mode == "block":
        a, b = old
        assert text.count(a) == 1 and text.count(b) == 1, f"{key}: block anchors"
        i, j = text.index(a), text.index(b) + len(b)
        assert i < j
        return text[:i] + new + text[j:], text[i:j], new
    c = text.count(old)
    assert c == 1, f"{key}: str anchor count {c}"
    assert old != new, f"{key}: no-op"
    return text.replace(old, new), old, new


def build(base_text):
    assert hashlib.sha256(base_text.encode()).hexdigest() == BASE_SHA, f"base is not adopted v2.12.14 ({BASE_TAG})"
    keys = [e[0] for e in EDITS]
    assert len(keys) == len(set(keys))
    text, record = base_text, []
    for key, grp, row, mode, old, new in EDITS:
        text, o, n = apply_edit(text, key, mode, old, new)
        record.append({"key": key, "group": grp, "row": row, "mode": mode,
                       "old_sha256": hashlib.sha256(o.encode()).hexdigest(),
                       "new_sha256": hashlib.sha256(n.encode()).hexdigest(), "old": o, "new": n})
    for e in record:
        assert text.count(e["new"]) == 1, f"{e['key']}: new text not unique"
    for r in NEW_RIDS:
        assert text.count(f"[RID: {r}]") == 1, r
    return text, record


def main(argv):
    base, out, log = argv[1:4]
    text, record = build(open(base, "rb").read().decode("utf-8"))
    data = text.encode("utf-8")
    open(out, "wb").write(data)
    json.dump({"base_sha256": BASE_SHA, "base_tag": BASE_TAG, "candidate_sha256": hashlib.sha256(data).hexdigest(),
               "declared_new_tdrg_rids": NEW_RIDS, "check_script": CHECK_SCRIPT, "edit_count": len(record),
               "edits": record}, open(log, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(hashlib.sha256(data).hexdigest(), len(record), "edits", len(NEW_RIDS), "new RIDs")


if __name__ == "__main__":
    main(sys.argv)
