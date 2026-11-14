#!/usr/bin/env python3
"""Atlas v0.12 -> v0.13 candidate: one impact refresh for two moved sources, under Atlas Method v0.3 (`atlas-method-v0.3`):
Discrete Genesis v2.12.15 (`tdrg-v2.12.15`, adopted 12 Nov 2026) and Arithmetic Resonance and Zeta v0.9 (`az-v0.9`, adopted
14 Nov 2026; it contains the v0.8 migration). The other 16 sources are not re-extracted. Sequence by the PI's [SESSION] decision
relayed 13 Nov 2026 (records/atlas/ATLAS_V0_13_IMPACT_PREPARATION_20261113.md).

TDR-G (D5; edges in D1): star event domain as implemented (valid centre, single-star component of any shape); classification
precedence of the tick; nine new RIDs (eight nodes, one `cert`), owned by TDR-G and credited to AZ as proposer; n-node birth-free
conservation proved; TDR-6 ACTIVE — PARTIAL; P: not conserved at births and not a gauge quantity; export row on the 24A → 24B → 24C
gate. TDRG.G9 retired (the owner separated the two questions).
AZ (D5; edges in D2, D4b, H2): PROP-AZ-CORE-EQUIV THM-ALG -> THM (owner [COR]); 4|q rule at the scope of its tested null protocol,
link to the low-order obstruction HEUR; Thread C evidence qualifier from AZ §9 per artifact; owner results cited once in AZ §8
(ledger locators); new AZ-owned node AZ-NUM-TOKRES-S1 [NUM diagnostic] with edges to the TDR-G nodes (no law restated, no
number on a TDR-G node).
Method §4.1 span deletions (edition labels that only date a result) in D5, each logged with its rule.
Pipes: NUMGEN.N-I1 restated at the new snapshot.
Run from the repository root: python3 -I evidence/atlas/build/refresh_v0_13.py
"""
from __future__ import annotations
import importlib.util, json, re, sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'evidence/atlas/v0.13'
ATLAS = 'atlas/RTG_STATE_ATLAS.md'
SNAPSHOT = '2676e6ff3e111aaa7d030cc1efcff45128b1abf3'   # main after PR #253 (az-v0.9)
BASE_TAG = 'atlas-v0.12'
BASE_SHA = 'cf9d8647b4c33206537e46ca37c7879d4fc33b1a936e0a50330a469f054def55'
METHOD_TAG, METHOD_SHA = 'atlas-method-v0.3', 'a29217352d989f75310f1c5fbb5e666cb02be9bc9a7c3b67d03d6e138115509f'
TDRG_PATH, AZ_PATH = 'dsn/RTG_DISCRETE_GENESIS_DSN.md', 'dsn/RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN.md'
MOVED = {'AZ': dict(edition='v0.9', tag='az-v0.9', authority='OWNER: release record `records/az/AZ_v0_9_RELEASE_RECORD.md` (PI adopted 14 Nov 2026); v0.8: `records/az/AZ_v0_8_RELEASE_RECORD.md`'),
         'TDRG': dict(edition='v2.12.15', tag='tdrg-v2.12.15', authority='OWNER: release record `records/tdrg/TDRG_v2_12_15_RELEASE_RECORD.md` (PI adopted 12 Nov 2026)')}
SHAS = {'AZ': 'c198a8bbddb23ce0d546c3ed03bddcdcf02dd83b974da7651a89a3fec5ac7598',
        'TDRG': '1e35be54a37bb227cd75e34fc1cd6732ae95782bdc147a76e736f16760c92e64'}
# every identifier that is new at the moved tags, with its one home in the atlas (kind, line prefix)
HOMES = {
 'TDRG-ALG-EVENT-INVENTORY': ('node', 'TDRG-ALG-EVENT-INVENTORY ALG |'),
 'TDRG-ALG-NARROW-BAND-CLASSES': ('node', 'TDRG-ALG-NARROW-BAND-CLASSES ALG |'),
 'TDRG-ALG-TOKEN-CENSUS-LAW': ('node', 'TDRG-ALG-TOKEN-CENSUS-LAW ALG |'),
 'TDRG-ALG-BIRTH-SPECTRUM-INJECTION': ('node', 'TDRG-ALG-BIRTH-SPECTRUM-INJECTION ALG |'),
 'TDRG-ALG-SPECCONS-N': ('node', 'TDRG-ALG-SPECCONS-N ALG |'),
 'TDRG-ALG-BIRTH-SPECTRUM-NOT-CLOSED': ('node', 'TDRG-ALG-BIRTH-SPECTRUM-NOT-CLOSED ALG |'),
 'TDRG-ALG-PARENT-CHILD-PHASE': ('node', 'TDRG-ALG-PARENT-CHILD-PHASE ALG |'),
 'TDRG-NUM-TOKEN-LAW-CHECK': ('node', 'TDRG-NUM-TOKEN-LAW-CHECK NUM |'),
 'TDRG-ART-TOKEN-LAW-CHECKS': ('cert', 'TDRG-NUM-TOKEN-LAW-CHECK NUM |'),
 'AZ-NUM-TOKRES-S1': ('node', 'AZ-NUM-TOKRES-S1 NUM·dx |'),
 'AZ-ART-TOKRES-S1': ('cert', 'AZ-NUM-TOKRES-S1 NUM·dx |'),
 'AZ-ART-CORE-EQUIV-CHECK': ('cert', 'PROP-AZ-CORE-EQUIV THM |'),
 'AZ-OPEN-SCOPE-ZETA': ('frontier', 'AZ: AZ-OPEN-SCOPE-ZETA PARTIAL'),
 'AZ-OPEN-SCOPE-ARITH': ('frontier', 'AZ: AZ-OPEN-SCOPE-ZETA PARTIAL'),
 'AZ-OPEN-PROMO': ('frontier', 'AZ: AZ-OPEN-SCOPE-ZETA PARTIAL'),
 'TDRG-OPEN-TOPO-FILTER': ('node', 'TDRG-OPEN-TOPO-FILTER (TDR-24A) ACTIVE'),   # an owner RID that AZ newly declares as cited; its home is TDR-G's own node, unchanged
}
PIPE_SNAPSHOT = {'closed': 66, 'dispositioned': 2, 'open': 55}
ATLAS_ITEMS = ['pipes/ATLAS/20261112-AZ-v0-8-adopted.md']
PATHS = ['records/az/AZ_v0_9_RELEASE_RECORD.md', 'records/az/AZ_v0_8_RELEASE_RECORD.md', 'records/tdrg/TDRG_v2_12_15_RELEASE_RECORD.md',
         'records/tdrg/ATLAS_ROW_CHECK_TDRG_v2_12_15.md', 'records/atlas/ATLAS_V0_13_IMPACT_PREPARATION_20261113.md',
         'evidence/az/core_equiv_check/az_core_equiv_check.py', 'records/az/AZ_TOKEN_RESONANCE_STAGE1_REPORT.md'] + ATLAS_ITEMS

def _load(name):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).with_name(name + '.py'))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
R10 = _load('refresh_v0_10')   # reused helpers only: Edit, h_l5_map, l5_rows, checker, pipe_states, git, sha, at, wjson
git, sha, at, wjson, h_l5_map, checker, pipe_states = R10.git, R10.sha, R10.at, R10.wjson, R10.h_l5_map, R10.checker, R10.pipe_states

class Edit(R10.Edit):
    def rep(self, old, new, finding, where):
        super().rep(old, new, finding, where); self.log[-1]['id'] = f'AR13-{len(self.log):03d}'
    def cut(self, prefix, span, where):
        """Method §4.1 span deletion inside one line: an edition label that only dates a result. Nothing is reworded."""
        l = self._one(prefix, K1, where); assert l.count(span) == 1, (where, span)
        self.rep(l, l.replace(span, ''), K1, where)

K1 = 'Method §4.1 span deletion (edition label that only dates a result)'
BIND3 = 'BIND3 (TDRG-ALG-BIND3-CYCLE-N24K1, TDRG-NUM-BIND3-PARITY, TDRG-NUM-BIND3-SPECTRAL-GATE, TDRG-NUM-BIND3-MEMORY-PARITY, TDRG-NUM-BIND3-XFER, TDRG-NUM-BIND3-REGEN: isolated period-2 not persistent, multi-pair scattering, even-parity survival, KNIFE FAIL, odd-memory COR; conv v18 path orientation, not rerun by the owner)'

def refresh(a: Edit):
    I, T, Z, P = 'identity', 'TDR-G v2.12.15', 'AZ v0.9', 'pipes'
    G = 'reviewed item (grade, qualifier or diagnostic change)'
    # ---- identity ----
    a.rep('# RTG STATE ATLAS v0.12\n', '# RTG STATE ATLAS v0.13\n', I, 'title')
    a.rep('evidence/atlas/v0.12/source_manifest.json', 'evidence/atlas/v0.13/source_manifest.json', I, 'SOURCES header')
    a.rep('*END — RTG STATE ATLAS v0.12.', '*END — RTG STATE ATLAS v0.13.', I, 'end line')
    a.line('| AZ | RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN | v0.7 |', '| AZ | RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN | v0.9 | `az-v0.9` | canonical Tier 5 |', I, 'SOURCES row AZ')
    a.line('| TDRG | RTG_DISCRETE_GENESIS_DSN | v2.12.14 |', '| TDRG | RTG_DISCRETE_GENESIS_DSN | v2.12.15 | `tdrg-v2.12.15` | canonical Tier 4 |', I, 'SOURCES row TDRG')
    a.rep('· DZT v0.8 · AZ v0.7 Thread A.', '· DZT v0.8 · AZ v0.9 Thread A.', I, 'D2 header, AZ')
    a.line('(sources: TDRG = RTG_DISCRETE_GENESIS_DSN v2.12.14',
           '(sources: TDRG = RTG_DISCRETE_GENESIS_DSN v2.12.15 (scientific scope edition of the v2.12 line: the star event domain stated as implemented, the token laws, TDR-6 partial; Methodology v1.2 declared by PI decision, the v1.4 migration is v2.13; Tier 4, maturity record B); AZ = RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN v0.9 (infrastructure and diagnostic ledger; Methodology v1.4 declared; each owner result is cited once, in its §8; one AZ-owned diagnostic in Thread B; Tier 5, Level A retained); NUMGEN v1.21 DISC/C7B modules. Whole domain sits behind SG-PROG-1/TDRG SG-10: continuous objects appear only as reference-only or blocked edges. Local aliases: TDRG one grade per claim (node heads below carry the owner RIDs, former atlas labels in parentheses); AZ [ENG PASS] (exit-code-gated; artifact availability per entry in AZ §9), [NUM diagnostic]≡NUM[scope: named diagnostic campaign], [bridge-candidate]≡HYP[bridge-required], [bridge-disqualified]≡RES(from NUM)[scope: bridge-candidate ruled out]; [import-ref] is a label for a reference-only citation, not a status tag.)', I, 'D5 header')

    # ================= TDR-G =================
    # ---- event domain and tick precedence ----
    a.sub_in_line('TDRG-DEF-CONV-TICK DEF·ENG PASS v18', '(4) classify isolated edge/path/cycle/clean star/multistar/tie;',
                  '(4) classify each component in this order: isolated node, single edge, single-star (exactly one valid centre, TDRG-DEF-STAR), multistar (two or more valid centres), path, cycle — ties are outcomes of the path rule, not a class; the classification is complete under the narrow band (TDRG-ALG-NARROW-BAND-CLASSES);', T, 'tick step 4: precedence as implemented')
    a.line('TDRG-DEF-STAR DEF |',
           'TDRG-DEF-STAR DEF | valid centre = node with ≥3 pairwise non-adjacent defect neighbours (under the narrow band every node of defect degree ≥3, TDRG-ALG-NARROW-BAND-CLASSES); single-star component = exactly one valid centre A, any shape (pure stars K_{1,m}, m≥3, K_{1,3} minimal; trees with longer branches; components containing a cycle); blow-up: new node E, θ_E=θ_A+N/2, δ_E=δ_A; centre δ_A↦−δ_A, both read from the CONV-TICK snapshot; every other node of the component inert for that tick; node count not conserved | the K_{1,3}-only statement of the editions through v2.12.14 is superseded: the pinned engines and every TDR-G result used the domain stated here, no result changes (EV-CODE); the share of non-pure single-star events in the canonical scans is not measured | ≡ OFN IMP-O08-09 | < RTG-OFN-ALG-STAR-TOKEN-SHIFT (equivariant under common token shift c iff 2c≡0; statement accepted by TDR-G §7 at pin ofn-v0.12, custody transfer XFER-O08-01 deferred to v2.13) @TDRG§6.3', T, 'star blow-up: event domain as implemented')
    a.sub_in_line('TDRG-DEF-MULTISTAR DEF (with TDRG-DEF-CANONICAL-BRANCH) |', '≥2 valid centers ⇒ policy fork', 'two or more valid centres, any shape ⇒ policy fork', T, 'multistar: stated with the precision of TDRG-DEF-STAR')
    a.cut('TDRG-DEF-MULTISTAR DEF (with TDRG-DEF-CANONICAL-BRANCH) |', ' since v2.12.14', 'multistar: tie clause')
    # ---- spectrum conservation ----
    a.sub_in_line('TDRG-ALG-LEM-SPECCONS ALG (alias LEM-SPECCONS;', '| n-node signed-permutation invariance CAND for swap/path sectors; across star OPEN (SG-12) |',
                  '| n-node birth-free form proved (TDRG-ALG-SPECCONS-N); across a birth the update is exact but not determined by the spectrum (TDRG-ALG-BIRTH-SPECTRUM-INJECTION, TDRG-ALG-BIRTH-SPECTRUM-NOT-CLOSED); a spectrum-level invariant of the full dynamics OPEN (SG-12) |', T, 'SPECCONS: generalization as the owner states it')
    a.cut('TDRG-ALG-LEM-SPECCONS ALG (alias LEM-SPECCONS;', 'v2.12.14 wording; ', 'SPECCONS: wording label')
    # ---- the token laws (§6.13): eight nodes ----
    a.after_line('TDRG-ALG-LEM-SPECCONS ALG (alias LEM-SPECCONS;', [
        'TDRG-ALG-EVENT-INVENTORY ALG | sc: the six policies, either orientation rule | in one tick the tokens change only by (a) a permutation of the tokens of one component (antipodal swap; path successor shift), (b) identity (isolated nodes, balanced path ties, cycle bound states, multistars under trap and the bound_* policies, every non-centre node of a star component), or (c) the star map at a valid centre with snapshot token x: centre x↦−x, newborn x; snapshot components are disjoint, so no node is written by two events in one tick, and the several centres of one tick are distinct nodes read from the snapshot | ENG conformance (EV-CODE): the pinned engines write tokens in exactly three places; the node cap ends a run before a step instead of suppressing a birth inside one | proposed by AZ, verified and owned by TDR-G | <TDRG-DEF-CONV-TICK, TDRG-DEF-STAR @TDRG§6.13',
        'TDRG-ALG-NARROW-BAND-CLASSES ALG | k<N/6 ⇒ every node of defect degree ≥3 is a valid centre (two adjacent neighbours would close a fully defective K₃); a connected graph of maximum degree ≤2 is a path or a cycle, C₃ excluded ⇒ every component with an edge has a class, the CONV-TICK step-4 precedence is a complete classification and the engine\'s residual classes are empty under the narrow band | <TDRG-THM-NARROW-BAND-EXCLUSION @TDRG§6.13',
        'TDRG-ALG-TOKEN-CENSUS-LAW ALG | A₀ = set of initial tokens, S₀=A₀∪(−A₀), c_t(y) = number of nodes with token y at tick t | (i) δ_i(t)∈S₀ for every node and tick (at most |S₀|≤2|A₀| distinct tokens ever occur); (ii) a tick whose births have centre snapshot tokens x₁..x_m changes the census by c_{t+1}(y)−c_t(y)=#{a: y≡−x_a}: c_t is coordinatewise non-decreasing, Σ_y c_t(y)=M_t; (iii) the set of signed classes present, I(X_t)={[δ_i]_±}, [x]_±={x,−x}, is invariant at every tick, births included: I(X_t)={[a]_±: a∈A₀} | the object is the global multiset, not node identity (the centre\'s own token is not conserved); (iii) is a token-state quantity, unchanged by the declared phase gauge and by relabelling; whether it is purely relational is undecided, so it does not close TDR-6 | ¬ growth mechanism, ¬ bridge (SG-10, SG-12) | proposed by AZ, accepted with change, proved and owned by TDR-G | <TDRG-ALG-EVENT-INVENTORY | >AZ-NUM-TOKRES-S1 (the law whose registration formulation AZ\'s per-tick check tested; no AZ number is part of this result) @TDRG§6.13',
        'TDRG-ALG-BIRTH-SPECTRUM-INJECTION ALG | C_t = token multiset before the tick, D(C) = multiset of |y−y′|_c over unordered pairs; births at centre snapshot tokens x₁..x_m: C_{t+1}=C_t⊎{−x₁..−x_m}, D(C_{t+1})=D(C_t)⊎{|x_a+y|_c: 1≤a≤m, y∈C_t}⊎{|x_a−x_b|_c: a<b} (mM_t+C(m,2) new entries); the token sum changes by −Σ_a x_a (mod N) | an identity of unlabelled multisets, not a list of edges at the newborn; the one-birth form applied m times against the pre-tick multiset misses the newborn–newborn pairs | proposed by AZ, owned by TDR-G | <TDRG-ALG-TOKEN-CENSUS-LAW @TDRG§6.13',
        'TDRG-ALG-SPECCONS-N ALG | on any tick without a star event, for any number of nodes, the token multiset and hence {|d_ij|_c}_{i<j} are exactly conserved | ¬ across births | proves the n-node generalization of TDRG-ALG-LEM-SPECCONS (three nodes: that lemma) | proposed by AZ, owned by TDR-G | <TDRG-ALG-EVENT-INVENTORY @TDRG§6.13',
        'TDRG-ALG-BIRTH-SPECTRUM-NOT-CLOSED ALG | N=24: C=(1,3,4,5) and C′=(2,4,5,6) have D(C)=D(C′)={1,1,2,2,3,4}; a birth at the centre with token 1, respectively 2, adds {2,4,5,6}, respectively {4,6,7,8}; both realised on the pinned engine with one geometry (k=1, post-advance θ=(0,11,12,13), a K_{1,3} at centre 0) ⇒ D_{t+1} is not a function of D_t: the update needs the centre token(s) and the census | C′=C+1 is a common token shift: D is shift-invariant, the star map is not (<RTG-OFN-ALG-STAR-TOKEN-SHIFT) @TDRG§6.13',
        'TDRG-ALG-PARENT-CHILD-PHASE ALG | sc: two-body kinematics under a token-persistence hypothesis | star event at tick t₀, centre A with snapshot token x, newborn E; if the next j advances use δ_A=−x and δ_E=x, then θ_E−θ_A≡N/2+2jx (mod N); along the free orbit the separation stays in {N/2,0} for all j iff 4x≡0 (mod N), equivalently ord(2x)≤2: ord 1 iff x∈{0,N/2}, ord 2 iff 4|N and x∈{N/4,3N/4}; for N≡2 (mod 4) no token has order 2 | ¬ bond-persistence or growth mechanism (in a many-node universe further events usually break the hypothesis); no bearing on TDRG-OPEN-LOCKING-FAIL / TDR-26 | proposed by AZ, owned by TDR-G | <TDRG-DEF-STAR | >AZ-NUM-TOKRES-S1 (names the arithmetic condition of AZ\'s intervention; AZ\'s numbers are not part of this result) @TDRG§6.13',
        'TDRG-NUM-TOKEN-LAW-CHECK NUM | sc: pinned v18 engine with TDRG-DEF-ORIENT; six policies × (N,k)∈{(24,1),(30,2),(60,4),(120,8)} × 30 random four-node starts, up to 400 ticks or 70 nodes | owner check of the token laws on the engine: census law and alphabet on every tick, birth injection on every birth tick, birth-free conservation on every birth-free tick, phase law on every parent–child advance — 0 violations; in the same mixed-policy sample 3,773 of 17,466 single-star events are not pure stars (the shares in the canonical scans are not measured) | a finite check, not a proof; AZ\'s own machine checks are source-reported (EV-SRC-REPORTED) | cert TDRG-ART-TOKEN-LAW-CHECKS (placed) @TDRG§6.13'], T, 'eight new nodes (§6.13), owner RIDs')
    # ---- frontier ----
    a.line('invariants: TDRG-OPEN-SPECCONS-STAR ≡ TDR-6 TDRG-OPEN-BIRTH-INVARIANT',
           'invariants: TDR-6 TDRG-OPEN-BIRTH-INVARIANT ACTIVE — PARTIAL (a purely relational invariant preserved or predictably changed across star blow-up): total P FAIL as a birth invariant (ΔP≡−x at a birth with centre token x; P is invariant under the declared gauge, so not a gauge artifact; SG-3); Σδ² FAIL (+δ_A²); new-triangle holonomy structural (dynamical status OPEN); token census and pairwise-difference multiset resolved as a predictable-change law (TDRG-ALG-TOKEN-CENSUS-LAW, TDRG-ALG-BIRTH-SPECTRUM-INJECTION): the spectrum is not preserved at births and no update law computable from D_t alone exists (TDRG-ALG-BIRTH-SPECTRUM-NOT-CLOSED); signed-class set I(X_t) exactly invariant (TDRG-ALG-TOKEN-CENSUS-LAW (iii)), its purely relational status undecided, so TDR-6 is not closed by it · TDRG-OPEN-SPECCONS-STAR ACTIVE: a spectrum-level quantity preserved across births, or updated by a law closed on the spectrum, and which centre tokens fire (a dynamical question); cited by OFN OPEN-OFN-SECTOR (SPECCONS-STAR only)', T, 'D5.L3 invariants: TDR-6 partial; two questions')
    a.sub_in_line('TDR-T launch chain (blocking, in order):', ' | ! owner Appendix C still carries older D/A/B gate (PROG launch-gate record; no launch authorized)',
                  ' | the owner\'s §1, Appendix C and §7 export row state this one gate (*PROG:TDRG-launch-gate, D1); no launch authorized', T, 'D5.L3 launch chain: the tension note does not describe the owner text')
    a.rep('needs TDR-19 + P1 bridge; = PROG IF25) · TDRG-EXPORT-DISCRETE-TRIAD\n', 'needs TDR-19 + P1 bridge; = PROG IF25) · TDRG-EXPORT-DISCRETE-TRIAD (native discrete triad orientation / survival statistics for TDR-T; blocked by 24A → 24B → 24C and TDR-T0)\n', T, 'exports: the triad row as the owner prints it')
    a.sub_in_line('*PROG:TDRG-launch-gate |', 'owner §§1–2 and App. C gate condition (aligned by the owner in v2.12.14):', 'owner §§1–2 and App. C gate condition:', K1, 'PROG launch-gate node: edition label')
    a.sub_in_line('*PROG:TDRG-launch-gate |', 'one §7 export row (TDRG-EXPORT-DISCRETE-TRIAD) still names the earlier D/A/B gate — recorded, not repaired, no launch authorized;',
                  'Programme v1.4 §6.4 records that one owner §7 export row (TDRG-EXPORT-DISCRETE-TRIAD) names the earlier D/A/B gate, which describes the edition it read (tdrg-v2.12.14): at this snapshot the owner\'s row names 24A → 24B → 24C and TDR-T0, so that Programme sentence describes an earlier owner edition, not this one; no launch authorized;', T, 'PROG launch-gate node: export row aligned by the owner')
    # ---- guards, retired ----
    a.sub_in_line('TDRG SG-14 (v2.12.14) relabelling covariance:', ' · SG-3 total P not physical · ', ' · SG-3 total P not adopted as a physical observable: not conserved across star births (ΔP≡−x), invariant under the declared phase gauge and under relabelling, so not a gauge quantity; P-conservation is not a constraint on interaction rules · ', T, 'SG-3 as corrected by the owner')
    a.sub_in_line('TDRG SG-14 (v2.12.14) relabelling covariance:', ' · SG-12 spectrum conservation not across star · ', ' · SG-12 spectrum conservation is certified for three-node, no-birth dynamics (n-node birth-free form: TDRG-ALG-SPECCONS-N); across a birth the update is exact but needs the centre token and the census; conservation across births, or a spectrum-level invariant of the full dynamics, is OPEN and must not be assumed · ', T, 'SG-12 as updated by the owner')
    a.cut('TDRG SG-14 (v2.12.14) relabelling covariance:', ' (v2.12.14)', 'SG-14 head')
    a.sub_in_line('*TDRG:retired FAIL |', 'sine coupling primitive; P conserved; Σδ² conserved;', 'sine coupling primitive; P as a conserved physical observable (not conserved across births, ΔP≡−x; the earlier reason "gauge artifact" is withdrawn by the owner: P is invariant under the declared gauge); Σδ² conserved;', T, 'retired list: reason for P')
    a.cut('*TDRG:retired FAIL |', 'v2.12.14, ', 'retired list: node-ID completion')
    a.cut('*TDRG:retired FAIL |', ' in v2.12.14', 'retired list: K₃ explosive')
    a.sub_in_line('*OFN:rejections (live, scoped) |', 'TDR-G\'s "gauge-like"/"gauge artifact" labels referred to TDR-G (pipes/TDRG/20261029-OFN-token-sum-gauge-label.md, open)',
                  'TDR-G\'s "gauge-like"/"gauge artifact" labels were referred to TDR-G, which has withdrawn them (TDR-G SG-3 at this snapshot: not conserved at births, not a gauge quantity)', T, 'OFN rejection row: the labels it referred are withdrawn by the owner')
    # ---- TDR-G diagnostics ----
    a.drop_line('TDRG.G9 ~ D-LINK (D-RID duplicate):', G, 'TDRG.G9 retired')
    a.line('TDRG.G8 D-STALE (internal, residual after v2.12.14):', 'TDRG.G8 D-STALE (internal, layout): the footer supersession chain of the v2.12.x point releases and the Appendix A ordering (v2.12.15, v2.12.14, then v2.12 before v2.12.13…v2.12.1) are layout items deferred to v2.13 together with the Methodology v1.4 migration (PI decision 27 Oct 2026). The edition still declares Methodology v1.2.', T, 'TDRG.G8 at v2.12.15')
    a.sub_in_line('TDRG.G11 D-PROOF (b)/(a) (evidence custody, v2.12.14 §8):', 'tdr_motif_bootstrap v1–v6, analysis scripts,', 'tdr_motif_bootstrap v1–v6, analysis scripts, the token-law checks with their fixtures (TDRG-ART-TOKEN-LAW-CHECKS, evidence/tdrg/inbox_20261112/),', T, 'TDRG.G11: new placed artifact')
    a.sub_in_line('TDRG.G11 D-PROOF (b)/(a) (evidence custody, v2.12.14 §8):', '(evidence custody, v2.12.14 §8)', '(evidence custody, §8)', K1, 'TDRG.G11 head')
    a.cut('TDRG.G10 D-CONV (non-canonical branch; owner finding N1, v2.12.14):', ', v2.12.14', 'TDRG.G10 head')
    # ---- Method §4.1 span deletions in D5 (TDR-G nodes) ----
    a.cut('TDRG-DEF-ZN-STATE DEF (alias TDRG-ZN-STATE; v2.12.14) |', ' since az-v0.7', 'state node: AZ citation')
    a.sub_in_line('TDRG-DEF-ZN-STATE DEF (alias TDRG-ZN-STATE; v2.12.14) |', '(SG-14, v2.12.14)', '(SG-14)', K1, 'state node: SG-14 label')
    a.sub_in_line('TDRG-DEF-ZN-STATE DEF (alias TDRG-ZN-STATE; v2.12.14) |', 'statement accepted by TDR-G v2.12.14 §7', 'statement accepted by TDR-G §7', K1, 'state node: Finding A')
    a.sub_in_line('TDRG-DEF-ZN-STATE DEF (alias TDRG-ZN-STATE; v2.12.14) |', '(RID available since v2.12.14; NUMGEN repin is NUMGEN\'s)', '(RID available; NUMGEN repin is NUMGEN\'s)', K1, 'state node: NUMGEN edge')
    a.sub_in_line('TDRG-DEF-ZN-STATE DEF (alias TDRG-ZN-STATE; v2.12.14) |', 'resolves through the v2.12.14 §7 map', 'resolves through the owner §7 map', K1, 'state node: §7 map')
    a.sub_in_line('TDRG-DEF-ZN-STATE DEF (alias TDRG-ZN-STATE; v2.12.14) |', '(alias TDRG-ZN-STATE; v2.12.14) |', '(alias TDRG-ZN-STATE) |', K1, 'state node head')
    a.sub_in_line('TDRG-DEF-BAND DEF (with TDRG-DEF-EDGE-SET, -NARROW-BAND; v2.12.14) |', '-NARROW-BAND; v2.12.14) |', '-NARROW-BAND) |', K1, 'band node head')
    a.sub_in_line('TDRG-ALG-ORIENT-NOGO ALG (v2.12.14) |', 'TDRG-ALG-ORIENT-NOGO ALG (v2.12.14) |', 'TDRG-ALG-ORIENT-NOGO ALG |', K1, 'orientation no-go head')
    a.sub_in_line('TDRG-ALG-MIRROR-NOT-STEP-SYMMETRY ALG (v2.12.14) |', 'TDRG-ALG-MIRROR-NOT-STEP-SYMMETRY ALG (v2.12.14) |', 'TDRG-ALG-MIRROR-NOT-STEP-SYMMETRY ALG |', K1, 'mirror node head')
    a.sub_in_line('TDRG-ALG-LARGEST-CENTER-ID-TIEBREAK ALG (v2.12.14; owner finding N1) |', '(v2.12.14; owner finding N1) |', '(owner finding N1) |', K1, 'largest_center node head')
    a.sub_in_line('*TDRG:bulk-fits NUM (fits; one grade since v2.12.14)', '(fits; one grade since v2.12.14)', '(fits; one grade)', K1, 'bulk fits head')
    a.sub_in_line('*TDRG:bulk-fits NUM (fits; one grade)', 'range-tagged by the owner (v2.12.14 §1, §5, §6.8).', 'range-tagged by the owner (§1, §5, §6.8).', K1, 'bulk fits locator')
    a.sub_in_line('*TDRG:crystallization HEUR (v2.12.14: extrapolation grade) |', 'HEUR (v2.12.14: extrapolation grade) |', 'HEUR (extrapolation grade) |', K1, 'crystallization head')
    a.sub_in_line('TDR-T ladder (App C, gated):', '(historical continuous reference since v2.12.14:', '(historical continuous reference:', K1, 'TDR-T ladder')
    a.sub_in_line('D5.X1 D-LINK (ruled on the TDR-G side, v2.12.14):', '(ruled on the TDR-G side, v2.12.14):', '(ruled on the TDR-G side):', K1, 'D5.X1 head')
    a.sub_in_line('TDRG-THM-NARROW-BAND-EXCLUSION THM |', '| v2.12.14 cites AZ-ALG-ANTIPODAL-LOWORDER as AZ\'s strict generalisation (odd L impossible for Lk<N/2); the same arithmetic in two homes, cross-cited since v2.12.14 @TDRG',
                  '| the owner cites AZ-ALG-ANTIPODAL-LOWORDER (pin az-v0.7; the AZ statement is unchanged at az-v0.9) as AZ\'s strict generalisation (odd L impossible for Lk<N/2); the same arithmetic in two homes, cross-cited @TDRG', T, 'narrow-band theorem: the owner\'s AZ pin written at the edge')

    # ================= AZ =================
    a.cut('AZ-GOAL DEF |', 'v0.6: ', 'AZ goal: verdict label')
    a.sub_in_line('AZ-THREADS DEF |', 'B discrete ℤ_N arithmetic (TDRG, bridge-candidate only; restatements collapse to TDRG nodes)', 'B discrete ℤ_N arithmetic (TDRG, bridge-candidate only; owner results are edges to the TDRG nodes; one AZ-owned diagnostic, AZ-NUM-TOKRES-S1)', Z, 'AZ threads: Thread B')
    # ---- Thread C evidence qualifier, from AZ §9 per artifact ----
    a.sub_in_line('AZ-1A/1B/1C ENG PASS |', ' | evidence (AZ v0.7 §9): none of the Thread C files, the hash registry AZ-ART-AZV5-REGISTRY included, is in the repository at this edition and none is described as recreated (EV-SRC-REPORTED, EV-NOT-RERUN); the owner keeps the grades with that limit, which holds for every AZ-owned node of this block; a later [SESSION] custody record (records/az/AZ_UPLOAD_HASH_CHECK_20261111.md) is not owner text and changes nothing here @AZ',
                  ' | evidence (AZ §9, per artifact; the Thread C files are in the repository only in part): deposited and replayed — the AZ-1A/AZ-1B registry state of ten files (AZ-ART-AZV5-REGISTRY: nine original files with hashes equal to the registry, the synthetic benchmark report regenerated with the registry\'s hash; ladder, solver acceptance and AZ-1B gate replayed, exit code 0; EV-BYTES, EV-HASH, EV-RUN) and az1b_certify.py (AZ-ART-AZ1B-CERTIFY), which reads no TDR-G export, so the real-TDR-G-export part of AZ-1B is source-reported; source-reported (EV-SRC-REPORTED, EV-NOT-RERUN; not described as recreated) — the Phase-2 harness (not an entry of the received registry), AZ-ART-SPECTRAL-RADIUS-PATCH, the frozen conventions state with CONV-AZ-ANGLE-ZERO (the deposited conventions file lacks it), and the Phase-2 reports and certificates cited on the nodes of this block; the owner keeps the [ENG PASS] records with these limits @AZ§4.3.1,§9', G, 'Thread C: evidence qualifier per artifact (qualifier change)')
    # ---- PROP-AZ-CORE-EQUIV: THM-ALG -> THM ----
    a.line('PROP-AZ-CORE-EQUIV THM-ALG |',
           'PROP-AZ-CORE-EQUIV THM | sc: finite simple undirected graph, both-orientation export, no multiedges/self-loops; closed walks non-backtracking at every index, the closing one included | the set of directed edges on a directed cycle of the Hashimoto transition digraph (DEF-AZ-CORE) = both orientations of the edges of the 2-core; proof: written derivation (closed non-backtracking walk ⇒ minimum degree ≥2; non-bridge edge on a simple cycle; bridge edge between two cycle-carrying sides) | ¬ strong connectivity (a bidirected cycle splits into two SCCs; every directed 2-core edge lies in some cyclic SCC); ¬ arbitrary directed exports or multigraphs; false if backtracking is allowed where the walk closes | corroboration, not the basis of the grade: the reported enumeration AZ-ART-PROP-CORE-EQUIV (2,141,014 graphs, 0 counterexamples; source-reported, EV-NOT-RERUN) and, separately, cert AZ-ART-CORE-EQUIV-CHECK (R(G) from the definition against the 2-core on all 2,131,019 labelled simple graphs with ≤7 vertices, 0 mismatches; EV-CODE, EV-RUN; not a rerun of the former) @AZ§4.3.2', G, 'PROP-AZ-CORE-EQUIV: grade THM-ALG -> THM (owner [COR], written proof)')
    # ---- 4|q rule: scope of the tested null protocol; link HEUR ----
    a.line('TDRG-AZ-STATIC-ZN-4Q NUM·dx / HEUR strong · bridge-disqualified |',
           'TDRG-AZ-STATIC-ZN-4Q NUM·dx · bridge-disqualified (the link to the low-order obstruction is HEUR) | chain 1 (N=120, k=8, bound_symmetric, Core(G_T), full spectrum, Null0+Null1, 1000 nulls × 5 seeds): R_q elevated for 4|q (q∈{4,8,12,20,24}), ≈0 for odd-prime q (3,5,15); generic even-q elevation = bidirected-export artifact collapsing under Null1; 4|q persists above Null1 (z-scores artifact-scoped, AZ-ART-PHASE2-N120-CORE); chain 2 (N∈{120,180,240}, core-matched random-theta antipodal-band null, a per-q comparison, not a 1000-null × 5-seed report; AZ-ART-THETA-CORE-MATCHED): 4|q reproduced with no TDR-G dynamics; strong set tracks 2-adic divisors of N (q=16 only at N=240) ⇒ read as static ℤ_N antipodal-band geometry, not a TDR-G dynamical signal, at the scope of the tested null protocol (one null family, three N); nothing is asserted for every antipodal-band graph or every N (SG-AZ-7) | mechanism partly = low-order obstruction (AZ-ALG-ANTIPODAL-LOWORDER; 4-dominated cycles), the link HEUR; k-dependence prediction falsified | both certifying artifacts source-reported (AZ §9) @AZ§4.3.3', G, '4|q rule: grade spelling unpacked by the owner; verdict at the scope of its evidence')
    a.line('AZ-ART-ZETA-V3 ENG-historical |', 'AZ-ART-ZETA-V3 (artifact registry entry; the owner prints no status tag) | rtg_graph_zeta_proto_v3.py; historical, superseded by az_v5; all v3 runs unverified; not the source of any AZ result; source-reported @AZ§9', G, 'v3 prototype: the alias [ENG-historical] is removed by the owner')
    # ---- the AZ-owned diagnostic ----
    a.after_line('AZ-ART-ZETA-V3 (artifact registry entry; the owner prints no status tag) |', [
        'AZ-NUM-TOKRES-S1 NUM·dx | sc: pinned TDR-G engine with TDRG-DEF-ORIENT; policy bound_symmetric; N∈{120,122}, k=8; four initial nodes; 800 ticks; node cap 300; endpoint M≥100; conv: orientation reference of TDR-G v2.12.14 (profile P1; TDRG-DEF-ORIENT unchanged at tdrg-v2.12.15) | registered paired intervention on the engine\'s own initial draw (one of the four initial tokens replaced; the same base draw under every arm; 1,500 base draws per contrast; exact McNemar tests): replacing the token by x with 4x≡0 (mod N) raises the probability that the run ends with M≥100 against a neighbour x±1 — risk difference with 97.5 % paired-proportion interval: PC1 (2x≡0, N=120) +0.2427 [+0.2166, +0.2681]; PC2 (2x≡N/2, N=120) +0.1613 [+0.1381, +0.1841] (PC1, PC2 confirmatory, Holm); PC3 (2x≡0, N=122) +0.2193 [+0.1944, +0.2436] (supportive only); PC4, an equivalence control at N=122 where 2x≡N/2 has no solution (values nearest N/4 against the native state): −0.0073 [−0.0158, +0.0011], equivalent within ±0.05 (supportive only); the registered controls read as required | what it is: the total causal effect of the token replacement on the registered endpoint, for the engine, profile, cells, horizon, cap and threshold of the scope | ¬ mechanism (the parent–child phase law names the arithmetic condition and does not explain the effect; its role in the tail is untested); ¬ other N, k/N, policies, horizons or thresholds; ¬ the TDR-26 birth-anchored discriminator, nothing about TDR-26 or any open module of TDR-G; ¬ relation to the 4|q rule, to DYAD cyclic-subgroup selection or to any DZT object (the shared numeral is not evidence; SG-AZ-3, SG-AZ-7); OPEN-P1 untouched; not a TDR-G result, not a bridge, no bridge-candidate promoted; does not by itself close AZ-OPEN-PROMO or change the maturity level | <TDRG-ALG-PARENT-CHILD-PHASE, TDRG-ALG-TOKEN-CENSUS-LAW, TDRG-DEF-ORIENT (engine and laws owned by TDR-G, unchanged) | cert AZ-ART-TOKRES-S1 (in the repository; the registered analysis re-derived byte-identically from the stored records, EV-CODE, EV-RUN; the engine runs were made once and are not rerun; EV-INDEP for the aggregation only) @AZ§4.2.1'], Z, 'new node: AZ-owned [NUM diagnostic]')
    # ---- ledgers: each owner result cited once, in AZ §8 ----
    a.line('*AZ:B-ledger (restatement; edges only; owner RIDs since az-v0.7) |',
           '*AZ:B-ledger (edges only; each owner result is cited once, in AZ §8; pin tdrg-v2.12.15) | AZ Thread B cites, as branch-local context and bridge-candidate observable family: TDRG-DEF-ZN-STATE, TDRG-DEF-PHYSICAL-STATE, TDRG-DEF-BAND, TDRG-THM-REACHABILITY-K0, TDRG-ALG-LEM-REACH, TDRG-ALG-LEM-RETRIG (bound state of period dividing 2), TDRG-ALG-LEM-SPECCONS (gcd multiset a consequence only; converse fails; the n-node birth-free form and the open spectrum-level question followed as the owner states them), TDRG-ALG-EVENT-INVENTORY with TDRG-ALG-TOKEN-CENSUS-LAW and TDRG-ALG-PARENT-CHILD-PHASE (local use: AZ-NUM-TOKRES-S1 only; no AZ number depends on them), ' + BIND3 + ', k/N growth control with TDRG-OPEN-NSCALING and TDRG-OPEN-CRYSTALLIZATION (*TDRG:bulk-fits: full-range 0.869; window-dependent, N^{−0.730} on N=480–1440; not a structural constant), TDR-26 rule (TDRG-OPEN-LOCKING-FAIL), TDR-24 frontier (TDRG-OPEN-TOPO-FILTER → TDRG-OPEN-CHI-SCALING → TDRG-OPEN-THERMO-SUPPRESS); no row is a bridge and none is used outside its branch; owner statements read, no owner artifact rerun (EV-SRC-READ, EV-NOT-RERUN) @AZ§8', Z, 'AZ Thread B ledger at v0.9')
    a.sub_in_line('*AZ:A-ledger (→ D2 reference-only edges; pin dyad-v6.4.23 since az-v0.7) |', '(→ D2 reference-only edges; pin dyad-v6.4.23 since az-v0.7) |', '(→ D2 reference-only edges; each owner result is cited once, in AZ §8; pin dyad-v6.4.24 — read at dyad-v6.4.23 and synchronized, no cited statement differs) |', Z, 'AZ Thread A ledger: pin')
    a.sub_in_line('*AZ:A-ledger (→ D2 reference-only edges; each owner result is cited once', 'not primality" @AZ§4.1', 'not primality" (AZ §4.1.3) @AZ§8', Z, 'AZ Thread A ledger: locator')
    a.sub_in_line('*AZ:A-heur HEUR |', '(pin dyad-v6.4.23 since az-v0.7) | @AZ§4.1', '(pin dyad-v6.4.24; AZ §8) | @AZ§4.1.3', Z, 'A-heur: pin and locator')
    # ---- AZ edges in other domains: edition labels of the moved source ----
    a.cut('DYAD-ALG-Q3-DEG2-CANCEL ALG |', ' since az-v0.7', 'Q3 node: AZ consumer')
    a.cut('DYAD-ALG-B5-ALLP-NONVANISHING ALG', ' since az-v0.7', 'B5 node: AZ consumer')
    a.sub_in_line('DYAD-THM-RAW-CUBIC THM |', '(az-v0.7 imports it at this scope, with the caveat)', '(AZ imports it at this scope, with the caveat)', K1, 'raw cubic node: AZ consumer')
    a.sub_in_line('H2 D-LINK high —', 'AZ v0.7 §6 states the same verdict', 'AZ §6 states the same verdict', K1, 'H2: AZ edition label')
    a.sub_in_line('UVM-RESULT-AUDIT1 (R16) COR |', '>AZ §6 (v0.7 cites R15/R16 as stated;', '>AZ §6 (cites R15/R16 as stated;', K1, 'UVM audit node: AZ edition label')
    a.sub_in_line('OPENM.U11 ~ D-LINK:', 'AZ v0.7 §6 cites R15/R16 as stated;', 'AZ §6 cites R15/R16 as stated;', K1, 'OPENM.U11: AZ edition label')
    # ---- frontier, guards, diagnostics ----
    a.sub_in_line('AZ: AZ-OPEN-SCOPE-ZETA', 'AZ: AZ-OPEN-SCOPE-ZETA (any graph/transfer-zeta observable dynamical rather than substrate? angular spectrum = substrate)',
                  'AZ: AZ-OPEN-SCOPE-ZETA PARTIAL (any graph/transfer-zeta observable dynamical rather than substrate? closed sub-item: the first angular observable is a substrate-geometry diagnostic, TDRG-AZ-STATIC-ZN-4Q; active: a dynamical observable)', Z, 'AZ frontier: SCOPE-ZETA status')
    a.sub_in_line('AZ: AZ-OPEN-SCOPE-ZETA PARTIAL', '· AZ-OPEN-SCOPE-ARITH (ℤ_N objects', '· AZ-OPEN-SCOPE-ARITH ACTIVE (ℤ_N objects', Z, 'AZ frontier: SCOPE-ARITH status')
    a.sub_in_line('AZ: AZ-OPEN-SCOPE-ZETA PARTIAL', '· AZ-OPEN-PROMO (Level-B promotion conditions incl. artifact/transcript provenance)', '· AZ-OPEN-PROMO ACTIVE (Level-B promotion conditions incl. artifact/transcript provenance; not closed by AZ-NUM-TOKRES-S1)', Z, 'AZ frontier: PROMO status')
    a.sub_in_line('AZ: AZ-OPEN-SCOPE-ZETA PARTIAL', '(G_birth(w) sequence,', '(G_birth(w) sequence — the object has two definitions in the deposited files and has to be fixed before use —,', Z, 'AZ frontier: G_birth(w)')
    a.sub_in_line('AZ SG-PROG-1/2/4 apply ·', 'also DZT p=8ℓ^a anomaly set — NO relation asserted, AZ.A5)', 'also DZT p=8ℓ^a anomaly set — NO relation asserted, AZ.A5; the rule is reproduced without TDR-G dynamics in the tested null protocol and nothing is asserted for every antipodal-band graph or every N)', Z, 'SG-AZ-7 worked example at the scope of its evidence')
    for pre in ('AZ.A5 ~ D-LINK / SG trap |', 'AZ.A5 ~ D-LINK / SG trap:'):
        l = a._one(pre, Z, 'AZ.A5'); a.rep(l, l + ' AZ states its static-geometry reading for the tested null protocol only (SG-AZ-7), and states that the condition 4x≡0 of AZ-NUM-TOKRES-S1 is no evidence of a relation to the 4|q rule, to DYAD subgroup selection or to any DZT object.', Z, 'AZ.A5 kept; AZ clause at v0.9 (' + ('D2' if pre.endswith('|') else 'D5') + ' row)')
    a.sub_in_line('PROG.G6 D-STALE (owner-recorded):', 'AZ (since then AZ v0.7, 11 Nov 2026: a corrections edition, by its release record not the §9.2 pass — no Methodology migration, no restructuring);',
                  'AZ (after that record, at the AZ edition of this snapshot: Methodology v1.4 declared with a declared section map, and the reduction of restated owner text asked for in Programme §6.7 carried out, no merger — AZ §7);', Z, 'PROG.G6: AZ state after the Programme snapshot')
    a.sub_in_line('METH.M1 D-GRADE (programme pattern):', 'persist in DZT, AZ, TDRG, OPEN-M, FMS session labels;', 'persist in DZT, TDRG, OPEN-M, FMS session labels (AZ unpacked its compound tags; the old spellings remain only in its registered retraction block, its corrections list and its edition history);', G, 'METH.M1: AZ leaves the row')

    # ---- pipes census at the new snapshot ----
    a.line('NUMGEN.N-I1 D-LINK (pipe states, receiver side) |', 'NUMGEN.N-I1 D-LINK (pipe states, receiver side) | at the source snapshot 2676e6f, pipes_index --check passes with 123 items in 20 inboxes — 66 closed, 2 dispositioned, 55 open. Open at the snapshot, by receiver: ATLAS (AZ v0.8; answered by this edition, closed by the atlas owner after the tag) · AZ (DYAD owner check of the q=3 degree-2 cancellation) · DZT (DYAD N16–N21, AZ v0.7 and v0.8, LIT norm-law proof candidate) · ER2B (OFN v0.11, DYAD N16–N21) · FMS (OFN v0.11, v0.12) · GEN (LIT Regge interface inputs, PROG v1.4, DYAD v6.4.24) · LIT (DYAD LH2012 use report, SAT coil strong-null map-class search) · NUMGEN (TDR-G v2.12.14 and v2.12.15, RECOG v0.3.26 and v0.3.27, DYAD v6.4.23 and v6.4.24, OFN v0.11 and v0.12, PROG v1.4) · OFN (DYAD v6.4.23 and v6.4.24, GEN v2.10, TRIAD v1.7, PROG v1.4, RECOG v0.3.27, TDR-G v2.12.15) · PREL (SAT finding on K₃ degeneracy and lift) · PROG (SAT satellite interface, AZ v0.7 and v0.8, TDR-G v2.12.15) · RECOG (DYAD v6.4.24) · RER (RECOG v0.3.26, DYAD N16–N21) · RRF (RECOG v0.3.26, OFN v0.11 and v0.12, DYAD N16–N21, GEN v2.10, TRIAD v1.7) · TRIAD (DYAD bridge-note recovery, GEN 𝒫₄-identity and birth-symmetry answers, GEN v2.10, PROG v1.4, DYAD v6.4.24; F30) · UVM (GEN κ_f/B_*/sourced-junction items, DYAD N16–N21, GEN v2.10, TRIAD v1.7). DYAD and TDRG have no open inbox item. A filed item is not adopted use; each receiver decides at its own checkpoint (CONVENTIONS §7).', P, 'pipe census at 2676e6f')

STALE = [r'`tdrg-v2\.12\.14` \|', r'\| v2\.12\.14 \| `tdrg', r'`az-v0\.7` \|', r'\| v0\.7 \| `az', r'AZ v0\.7 Thread A', r'AZ v0\.7 §', r'ZETA_DSN v0\.7', r'GENESIS_DSN v2\.12\.14 \(',
         r'since az-v0\.7', r'az-v0\.7 imports', r'K_\{1,3\} center A', r'P FAIL \(gauge\)', r'TDRG\.G9', r'PROP-AZ-CORE-EQUIV THM-ALG', r'NUM·dx / HEUR strong', r'ENG-historical', r'recorded, not repaired',
         r'none of the Thread C files', r'snapshot c8e7198', r'total P not physical', r'still carries older D/A/B', r'restatement; edges only', r'one question, two RIDs', r'CAND for swap/path sectors',
         r'evidence/atlas/v0\.12/']
def stale_editions(text):
    return [l[:90] for l in text.split('\n') if not l.startswith('*ATLAS:checked-') and any(re.search(p, l) for p in STALE)]

def node(text, prefix):
    ls = [l for l in text.split('\n') if l.startswith(prefix)]
    return ls[0] if len(ls) == 1 else ''

TDRG_NEW_NODES = [p for r, (k, p) in HOMES.items() if k == 'node' and r.startswith('TDRG-') and '-OPEN-' not in r]   # the eight §6.13 nodes
STAGE1_NUMBERS = ['0.2427', '0.1613', '0.2193', '0.0073', '0.2580', '0.1853', '0.2307', '19,900', '1,500 base draws']

def scope_guards(text):
    """Owner scope that must survive in the refreshed nodes (focused, statement-level)."""
    bad = []; need = lambda cond, msg: None if cond else bad.append(msg)
    s = node(text, 'TDRG-DEF-STAR DEF |')
    need('exactly one valid centre A, any shape' in s and 'pairwise non-adjacent' in s and 'no result changes (EV-CODE)' in s and 'K_{1,3} minimal' in s, 'star: event domain as implemented')
    need('not measured' in s, 'star: unmeasured share in the canonical scans')
    need('two or more valid centres, any shape' in node(text, 'TDRG-DEF-MULTISTAR DEF (with TDRG-DEF-CANONICAL-BRANCH) |'), 'multistar domain')
    need('ties are outcomes of the path rule, not a class' in node(text, 'TDRG-DEF-CONV-TICK DEF·ENG PASS v18'), 'tick precedence')
    inv = node(text, 'invariants: TDR-6 TDRG-OPEN-BIRTH-INVARIANT ACTIVE — PARTIAL')
    need('not a gauge artifact' in inv and 'ΔP≡−x' in inv, 'TDR-6: reason for P')
    need('its purely relational status undecided, so TDR-6 is not closed by it' in inv, 'TDR-6: signed-class set does not close it')
    need('TDRG-OPEN-SPECCONS-STAR ACTIVE' in inv and 'no update law computable from D_t alone exists' in inv, 'SPECCONS-STAR stays active')
    sn = node(text, 'TDRG-ALG-SPECCONS-N ALG |'); need('without a star event' in sn and '¬ across births' in sn, 'SPECCONS-N: birth-free only')
    lem = node(text, 'TDRG-ALG-LEM-SPECCONS ALG (alias LEM-SPECCONS;'); need('sc: 3 nodes, no star' in lem and 'OPEN (SG-12)' in lem and 'TDRG-ALG-SPECCONS-N' in lem, 'LEM-SPECCONS: scope and open part')
    ph = node(text, 'TDRG-ALG-PARENT-CHILD-PHASE ALG |')
    need('token-persistence hypothesis' in ph and '¬ bond-persistence or growth mechanism' in ph and 'no bearing on TDRG-OPEN-LOCKING-FAIL' in ph, 'phase law: kinematic identity only')
    cl = node(text, 'TDRG-ALG-TOKEN-CENSUS-LAW ALG |'); need('does not close TDR-6' in cl and '¬ growth mechanism' in cl, 'census law: negatives')
    ck = node(text, 'TDRG-NUM-TOKEN-LAW-CHECK NUM |'); need('a finite check, not a proof' in ck and 'cert TDRG-ART-TOKEN-LAW-CHECKS' in ck, 'owner check: finite check')
    for p in TDRG_NEW_NODES:
        l = node(text, p); need(bool(l) and l.rstrip().endswith('@TDRG§6.13'), 'owner locator: ' + p)
        need('@AZ' not in l, 'TDR-G law under an AZ locator: ' + p)
        need(not any(n in l for n in STAGE1_NUMBERS), 'Stage 1 number on a TDR-G node: ' + p)
    g = node(text, 'TDRG SG-14 relabelling covariance:'); need('so not a gauge quantity' in g and 'must not be assumed' in g, 'SG-3 / SG-12')
    need('"gauge artifact" is withdrawn by the owner' in node(text, '*TDRG:retired FAIL |'), 'retired list: P')
    tk = node(text, 'AZ-NUM-TOKRES-S1 NUM·dx |')
    need(tk.rstrip().endswith('@AZ§4.2.1') and 'cert AZ-ART-TOKRES-S1' in tk, 'diagnostic: AZ-owned, one node')
    need('N∈{120,122}, k=8' in tk and '800 ticks' in tk and 'endpoint M≥100' in tk and 'bound_symmetric' in tk and 'conv: orientation reference of TDR-G v2.12.14' in tk, 'diagnostic: scope and convention')
    need('not a TDR-G result, not a bridge, no bridge-candidate promoted' in tk and '¬ mechanism' in tk and 'OPEN-P1 untouched' in tk and 'does not by itself close AZ-OPEN-PROMO' in tk, 'diagnostic: negatives')
    need('(supportive only)' in tk and 'confirmatory' in tk and 'equivalence control' in tk, 'diagnostic: families')
    need('<TDRG-ALG-PARENT-CHILD-PHASE, TDRG-ALG-TOKEN-CENSUS-LAW, TDRG-DEF-ORIENT' in tk and 'iff 4x≡0' not in tk, 'diagnostic: edges only, law not restated')
    need(len([l for l in text.split('\n') if l.startswith('AZ-NUM-TOKRES-S1') or l.startswith('TDRG-NUM-TOKRES') or l.startswith('*TDRG:tokres')]) == 1, 'diagnostic: one home')
    ce = node(text, 'PROP-AZ-CORE-EQUIV THM |')
    need('proof: written derivation' in ce and 'corroboration, not the basis of the grade' in ce and 'the closing one included' in ce and 'not a rerun of the former' in ce, 'core equivalence: THM on the written proof')
    need(not node(text, 'PROP-AZ-CORE-EQUIV THM-ALG |'), 'core equivalence: old grade')
    z = node(text, 'TDRG-AZ-STATIC-ZN-4Q NUM·dx · bridge-disqualified')
    need('at the scope of the tested null protocol' in z and 'nothing is asserted for every antipodal-band graph or every N' in z and 'not a TDR-G dynamical signal' in z and 'the link HEUR' in z, '4|q: verdict at the scope of its evidence')
    c = node(text, 'AZ-1A/1B/1C ENG PASS |')
    need('only in part' in c and 'reads no TDR-G export' in c and 'EV-SRC-REPORTED' in c and 'not described as recreated' in c and 'the owner keeps the [ENG PASS] records with these limits' in c, 'Thread C: evidence qualifier')
    need(bool(node(text, 'AZ.A5 ~ D-LINK / SG trap:')) and bool(node(text, 'AZ.A5 ~ D-LINK / SG trap |')), 'AZ.A5 kept (both rows)')
    bl = node(text, '*AZ:B-ledger (edges only;'); need('no row is a bridge' in bl and bl.rstrip().endswith('@AZ§8') and 'pin tdrg-v2.12.15' in bl, 'B ledger')
    al = node(text, '*AZ:A-ledger (→ D2 reference-only edges;'); need('with the owner caveat' in al and 'not recovered at the owner' in al and 'pin dyad-v6.4.24' in al, 'A ledger: owner caveats and pin')
    fr = node(text, 'AZ: AZ-OPEN-SCOPE-ZETA PARTIAL'); need('AZ-OPEN-SCOPE-ARITH ACTIVE' in fr and 'AZ-OPEN-PROMO ACTIVE' in fr and 'not closed by AZ-NUM-TOKRES-S1' in fr, 'AZ frontier statuses')
    u = node(text, 'UVM-RESULT-AUDIT1 (R16) COR |'); need('v0.6 "legal 2×" SUPERSEDED' in u and 'AZ App. B' in u, 'UVM node: verdict kept')
    pg = node(text, '*PROG:TDRG-launch-gate |'); need('no launch authorized' in pg and 'describes an earlier owner edition, not this one' in pg, 'launch gate: Programme sentence against the owner')
    return bad

def homes_check(text, tdrg_new, az_new):
    """The shared checker's coverage check extracts Dyadic RIDs only. For the two moved sources: every identifier new at the tag
    has exactly one home, of the kind declared in HOMES."""
    bad = []; lines = text.split('\n')
    for r in sorted(tdrg_new | az_new):
        if r not in HOMES: bad.append(('no declared home', r)); continue
        kind, pre = HOMES[r]; hl = [l for l in lines if l.startswith(pre)]
        if len(hl) != 1: bad.append(('home line count', r, len(hl))); continue
        if kind == 'node':
            if len([l for l in lines if re.match(re.escape(r) + r'(?![A-Za-z0-9-])', l)]) != 1: bad.append(('node count', r))
        elif kind == 'cert':
            if len(re.findall(r'cert ' + re.escape(r) + r'(?![A-Za-z0-9-])', text)) != 1 or ('cert ' + r) not in hl[0]: bad.append(('cert home', r))
        else:
            if not re.search(re.escape(r) + r'(?![A-Za-z0-9-])', hl[0]): bad.append(('frontier home', r))
    return bad

RID = lambda t: set(re.findall(r'RID: ([A-Z][A-Z0-9]*(?:-[A-Z0-9.]+)+)', t))

def main():
    snap = git('rev-parse', SNAPSHOT + '^{commit}').decode().strip(); assert snap == SNAPSHOT
    base = at(BASE_TAG, ATLAS).decode(); assert sha(base) == BASE_SHA
    assert sha(at(METHOD_TAG, 'atlas/RTG_STATE_ATLAS_METHOD.md')) == METHOD_SHA and at(SNAPSHOT, 'atlas/RTG_STATE_ATLAS_METHOD.md') == at(METHOD_TAG, 'atlas/RTG_STATE_ATLAS_METHOD.md')
    a = Edit(base); refresh(a); text = a.text
    assert not stale_editions(text), stale_editions(text)
    assert not scope_guards(text), scope_guards(text)
    # ---- manifest ----
    old = json.loads(at(BASE_TAG, 'evidence/atlas/v0.12/source_manifest.json'))
    m = json.loads(json.dumps(old)); m.pop('note', None)
    for s in m['sources']:
        for k in [k for k in s if k.startswith('v0_11_')]: del s[k]
    m.update(atlas='v0.13', frozen_at='2026-11-14', repository_snapshot=SNAPSHOT, previous_atlas_tag=BASE_TAG, method_tag=METHOD_TAG, method_edition='v0.3', method_sha256=METHOD_SHA)
    for s in m['sources']:
        prev = next(x for x in old['sources'] if x['key'] == s['key'])
        s['v0_12_edition'] = prev['edition']; s['v0_12_input_sha256'] = prev['sha256']
        oldbytes = at(prev['tag'], prev['path']); assert sha(oldbytes) == prev['sha256'], s['key']
        if s['key'] in MOVED:
            mv = MOVED[s['key']]; data = at(mv['tag'], s['path'])
            s.update(edition=mv['edition'], tag=mv['tag'], commit=git('rev-parse', mv['tag'] + '^{commit}').decode().strip(), sha256=sha(data), authority=mv['authority'])
        data = at(s['tag'], s['path']); resolved = git('rev-parse', s['tag'] + '^{commit}').decode().strip()
        assert sha(data) == s['sha256'] and resolved == s['commit'], s['key']
        assert data == at(SNAPSHOT, s['path']), ('snapshot/tag divergence', s['key'])
        newest = git('tag', '--list', s['tag'].rsplit('-v', 1)[0] + '-v*', '--sort=v:refname').decode().split()[-1]
        assert newest == s['tag'], ('a newer source tag exists', s['key'], newest)
        s['v0_12_input_equality'] = 'EQUAL' if data == oldbytes else 'CHANGED'
    assert Counter(x['v0_12_input_equality'] for x in m['sources']) == {'EQUAL': 16, 'CHANGED': 2}
    assert {x['key'] for x in m['sources'] if x['v0_12_input_equality'] == 'CHANGED'} == set(MOVED)
    for k, h in SHAS.items(): assert next(s for s in m['sources'] if s['key'] == k)['sha256'] == h, k
    for t in ('az-v0.9', 'tdrg-v2.12.15'): assert git('cat-file', '-t', t).decode().strip() == 'tag', t
    wjson(OUT / 'source_manifest.json', m)
    # ---- H -> L5 ----
    hm = h_l5_map(text); assert not hm['dangling'], hm['dangling']
    wjson(OUT / 'h_l5_map.json', dict(convention='Every HEADLINE line cites L5 row ids only (many-to-one allowed). High L5 rows cited by no H are listed here and dispositioned in the release record.', **hm))
    # ---- retired keys (cumulative) ----
    oldret = json.loads(at(BASE_TAG, 'evidence/atlas/v0.12/retired_l5_keys.json'))
    newret = {'TDRG.G9': 'TDR-G v2.12.15 (tdrg-v2.12.15 §2, edits E09–E10 of its edit log): the row recorded one question under two RIDs — the pairwise-difference-multiset sub-item of TDR-6 (TDRG-OPEN-BIRTH-INVARIANT) and TDRG-OPEN-SPECCONS-STAR. The owner now separates them: the TDR-6 sub-item is resolved as a predictable-change law (TDRG-ALG-TOKEN-CENSUS-LAW, TDRG-ALG-BIRTH-SPECTRUM-INJECTION, TDRG-ALG-BIRTH-SPECTRUM-NOT-CLOSED), and TDRG-OPEN-SPECCONS-STAR stays ACTIVE for a different question (a spectrum-level invariant or a law closed on the spectrum, and which centre tokens fire). No duplicate remains; the frontier line carries both items with their statuses.'}
    for k in newret: assert not re.search(r'(?<![A-Za-z0-9_.-])' + re.escape(k) + r'(?![A-Za-z0-9_-])', text), k
    assert not set(newret) & set(oldret['retired'])
    retired = oldret['retired'] + list(newret) + [k.replace('.', ' ') for k in newret if '.' in k]
    wjson(OUT / 'retired_l5_keys.json', dict(retired=retired, note='Keys not reused; v0.13 reasons in dispositions.json.'))
    # ---- shared checker, with this edition's own manifest, coverage map and cumulative retired list (Method §7) ----
    c = checker(); src = c.load_sources(m)
    cmap = json.loads(at(BASE_TAG, 'evidence/atlas/v0.12/coverage_map.json'))
    cmap['_note_v0_13'] = 'coverage_map.json of atlas-v0.12, unchanged in its homes. The checker\'s coverage check extracts Dyadic RIDs only; the homes of the identifiers new at tdrg-v2.12.15 and az-v0.9 are asserted by the builder (verification_summary.json, moved_source_homes).'
    wjson(OUT / 'coverage_map.json', cmap)
    idmap = json.loads(at('atlas-v0.2', 'evidence/atlas/owner_identifier_map_v0_2.json'))
    report = c.run(text, m, src, cmap, idmap, retired)
    meta = dict(atlas=ATLAS, atlas_sha=sha(text), manifest='evidence/atlas/v0.13/source_manifest.json')
    c.write_report(report, str(OUT / 'atlas_check_report.md'), meta)
    wjson(OUT / 'atlas_check_report.json', dict(meta=meta, rows=report.rows))
    assert not report.fails(), report.fails()
    shared = c.self_test(m, src, cmap, idmap, retired, text)
    wjson(OUT / 'shared_controls.json', [dict(name=n, item=i, as_expected=bool(b)) for n, i, b in shared]); assert all(x[2] for x in shared), shared
    # ---- identifiers of the two moved sources: nothing lost, every new one has one home ----
    t14 = at('tdrg-v2.12.14', TDRG_PATH).decode(); t15 = src['TDRG']; z7 = at('az-v0.7', AZ_PATH).decode(); z9 = src['AZ']
    tdrg_new = RID(t15) - RID(t14); az_new = RID(z9) - RID(z7)
    assert RID(t14) <= RID(t15), RID(t14) - RID(t15)
    assert RID(z7) <= RID(z9), RID(z7) - RID(z9)
    assert tdrg_new | az_new == set(HOMES), (sorted((tdrg_new | az_new) - set(HOMES)), sorted(set(HOMES) - (tdrg_new | az_new)))
    hc = homes_check(text, tdrg_new, az_new); assert not hc, hc
    az_owned = lambda t: set(re.findall(r'(?<![A-Z0-9-])((?:AZ|PROP-AZ|DEF-AZ|CONV-AZ|TDRG-AZ|SG-AZ)-[A-Z0-9.-]*[A-Z0-9])', t))
    blk = lambda t: [l for l in t.split('\n') if 'RID: AZ-ALG-ANTIPODAL-LOWORDER' in l]
    owner_facts = dict(
        tdrg_star_domain='A **single-star component** is a component with exactly one valid centre' in t15 and 'no result changes (`EV-CODE`' in t15,
        tdrg_tdr6_partial='Status: ACTIVE — PARTIAL' in t15 and 'so it does not close TDR-6' in t15,
        tdrg_p_not_gauge='so it is not a gauge quantity' in t15 and 'so not a gauge artifact' in t15,
        tdrg_speccons_n='[RID: TDRG-ALG-SPECCONS-N]' in t15 and 'replacing the former conjecture' in t15,
        tdrg_speccons_star_active='Still open: a spectrum-level quantity preserved across births' in t15 and 'Status stays ACTIVE' in t15,
        tdrg_phase_law_scope='`[ALG]` [RID: TDRG-ALG-PARENT-CHILD-PHASE] `[scope: two-body kinematics under a token-persistence hypothesis]`' in t15 and 'not a bond-persistence or growth mechanism' in t15,
        tdrg_stage1_not_part="AZ's registered Stage 1 campaign and its numbers are not part of them" in t15,
        tdrg_export_row_aligned='blocked by TDR-24A → TDR-24B → TDR-24C and TDR-T0' in t15 and t15.count('D/A/B') == 1,
        tdrg_az_pin='`AZ-ALG-ANTIPODAL-LOWORDER` (`az-v0.7`' in t15,
        tdrg_methodology_v1_2='DSN_METHODOLOGY_v1.2 (declared' in t15,
        tdrg_check_counts='17,466' in t15 and 'not pure 3,773' in t15 and '0 violations' in t15,
        programme_sentence_unchanged='still names the earlier D/A/B gate' in src['PROG'],
        az_core_equiv_thm='`[THM]` `[RID: PROP-AZ-CORE-EQUIV]` `[proof: written derivation, below]`' in z9 and '*Corroboration; not the basis of the grade.*' in z9,
        az_4q_scope='nothing is asserted for every antipodal-band graph or every $N$' in z9 or 'nothing is asserted for every antipodal-band graph or every N' in z9,
        az_4q_tag='`[NUM diagnostic]` `[RID: TDRG-AZ-STATIC-ZN-4Q]`' in z9 and 'is `[HEUR]`, not exact' in z9,
        az_tokres='`[NUM diagnostic]` `[RID: AZ-NUM-TOKRES-S1]`' in z9 and 'it is not a TDR-G result, not a bridge, and no bridge-candidate is promoted by it' in z9,
        az_tokres_numbers=all(n in z9 for n in ['+0.2427', '+0.2166, +0.2681', '+0.1613', '+0.1381, +0.1841', '+0.2193', '+0.1944, +0.2436', '-0.0073', '-0.0158, +0.0011', '1,500 base draws']),
        az_tokres_no_promo='does not by itself close `AZ-OPEN-PROMO`' in z9,
        az_open_status=z9.count('Status: ACTIVE') == 2 and z9.count('Status: PARTIAL') == 1,
        az_thread_c_partial='The Thread C files are in the repository only in part.' in z9 and 'it reads no TDR-G export' in z9 and 'it does not contain CONV-AZ-ANGLE-ZERO' in z9,
        az_gbirth_two_definitions='Two definitions of `G_birth(w)` in the deposited files' in z9,
        az_pins='`dyad-v6.4.24`' in z9 and '`tdrg-v2.12.15`' in z9 and 'DSN Methodology v1.4' in z9,
        az_compound_tags_only_in_history=all(any(k in l for k in ('angular consequence stays', 'pre-migration form', 'June 2026 — v0.6 ledger-state', 'Methodology v1.4 migration with a declared section map', '(as printed through v0.7)')) for l in z9.split('\n') if re.search(r'HEUR/NUM strong|THM-ALG|\[[A-Z]{2,5}/[A-Z]{2,5}', l)),
        az_antipodal_statement_unchanged=blk(z7) == blk(z9) and len(blk(z9)) == 1,
        az_owned_identifiers_kept=az_owned(z7) - {'AZ-ART-ZETA-V3'} <= az_owned(z9) | set(),
        az_no_least_period='least period' not in z9)
    assert all(owner_facts.values()), [k for k, v in owner_facts.items() if not v]
    for p in PATHS: assert at(SNAPSHOT, p), p
    n_snap, st_snap = pipe_states(SNAPSHOT); assert n_snap == 123 and st_snap == PIPE_SNAPSHOT, (n_snap, st_snap)
    for it in ATLAS_ITEMS: assert re.search(r'^state:\s*open', at(SNAPSHOT, it).decode(), re.M), it
    # ---- dispositions: every L5 row of the opened domain D5, and every other row this edition touches ----
    def row(t, key):
        ls = [l for l in t.split('\n') if l.startswith(key + ' ')]; return '\n'.join(ls) if ls else None
    bl_, tl_ = base.split('\n'), text.split('\n')
    i0 = bl_.index('### D5.L5 DIAGNOSTICS'); d5keys = []
    for l in bl_[i0 + 1:]:
        if l.startswith('#') or l.startswith('---'): break
        mm = R10.ROW.match(l)
        if mm: d5keys.append(mm.group(1))
    touched = list(dict.fromkeys(d5keys + ['PROG.G6', 'METH.M1', 'METH.M2', 'NUMGEN.N-I1', 'OPENM.U11', 'OPENM.U2', 'DYAD.X8', 'DZT.Q1']))
    disp = []
    for key in touched:
        o = row(base, key); n = row(text, key); assert o, key
        state = 'retired' if key in newret else ('retained' if n == o else 'reworded'); assert (n is None) == (key in newret), key
        why = [e['where'] for e in a.log if key in e['where'] or (e['old'].startswith(key + ' '))]
        disp.append(dict(key=key, disposition=state, reason=newret.get(key, 'unchanged: what it records is unchanged at the v0.13 sources' if state == 'retained' else 'reworded; operations: ' + '; '.join(why)),
                         previous_sha256=sha(o), current_sha256=sha(n) if n else None))
    wjson(OUT / 'dispositions.json', disp)
    # ---- focused negative controls ----
    controls = []
    def ctl(cid, what, detected): controls.append(dict(id=cid, what=what, detected=bool(detected)))
    run = lambda t, with_sources=True: bool(c.run(t, m, src, cmap, idmap, retired, with_sources=with_sources).fails())
    def sw(old, new, n=1):
        assert text.count(old) >= 1, old[:60]; return text.replace(old, new, n)
    homes = lambda t: bool(homes_check(t, tdrg_new, az_new))
    ctl('V1', 'star stated on K_{1,3} only', scope_guards(sw('single-star component = exactly one valid centre A, any shape (pure stars K_{1,m}, m≥3, K_{1,3} minimal; trees with longer branches; components containing a cycle)', 'K_{1,3} center A')))
    ctl('V2', '"gauge" restored as the reason for P', scope_guards(sw('P is invariant under the declared gauge, so not a gauge artifact; SG-3)', 'gauge)')) and stale_editions(sw('total P FAIL as a birth invariant (ΔP≡−x at a birth with centre token x; P is invariant under the declared gauge, so not a gauge artifact; SG-3)', 'total P FAIL (gauge)')))
    ctl('V3', 'TDR-6 shown as closed', scope_guards(sw('invariants: TDR-6 TDRG-OPEN-BIRTH-INVARIANT ACTIVE — PARTIAL', 'invariants: TDR-6 TDRG-OPEN-BIRTH-INVARIANT CLOSED')))
    ctl('V4', 'signed-class invariant shown as closing TDR-6', scope_guards(sw('its purely relational status undecided, so TDR-6 is not closed by it', 'which closes TDR-6')))
    ctl('V5', 'n-node conservation shown as holding across births', scope_guards(sw('on any tick without a star event, for any number of nodes,', 'on any tick, for any number of nodes,').replace(' | ¬ across births | proves', ' | proves', 1)))
    ctl('V6', 'phase law shown as a bond or growth mechanism', scope_guards(sw('¬ bond-persistence or growth mechanism (in a many-node universe further events usually break the hypothesis)', 'a bond-persistence mechanism')))
    ctl('V7', 'PROP-AZ-CORE-EQUIV left at THM-ALG', scope_guards(sw('PROP-AZ-CORE-EQUIV THM |', 'PROP-AZ-CORE-EQUIV THM-ALG |')) and stale_editions(sw('PROP-AZ-CORE-EQUIV THM |', 'PROP-AZ-CORE-EQUIV THM-ALG |')))
    ctl('V8', 'enumeration shown as the proof', scope_guards(sw('corroboration, not the basis of the grade: the reported enumeration', 'proof: the reported enumeration').replace('proof: written derivation (', 'sketch (', 1)))
    ctl('V9', '4|q verdict stated beyond the tested protocol', scope_guards(sw(', at the scope of the tested null protocol (one null family, three N); nothing is asserted for every antipodal-band graph or every N (SG-AZ-7)', ' for any antipodal-band graph on any ℤ_N')))
    ctl('V10', 'the diagnostic placed under a TDR-G RID', scope_guards(sw('AZ-NUM-TOKRES-S1 NUM·dx |', 'TDRG-NUM-TOKRES-S1 NUM·dx |')) and homes(sw('AZ-NUM-TOKRES-S1 NUM·dx |', 'TDRG-NUM-TOKRES-S1 NUM·dx |')) and run(sw('AZ-NUM-TOKRES-S1 NUM·dx |', 'TDRG-NUM-TOKRES-S1 NUM·dx |'), False))
    ctl('V11', 'a TDR-G law placed under an AZ locator', scope_guards(sw('AZ\'s numbers are not part of this result) @TDRG§6.13', 'AZ\'s numbers are not part of this result) @AZ§4.2.1')))
    ctl('V12', 'a Stage 1 number on a TDR-G node', scope_guards(sw('no bearing on TDRG-OPEN-LOCKING-FAIL / TDR-26 |', 'no bearing on TDRG-OPEN-LOCKING-FAIL / TDR-26; risk difference +0.2427 at N=120 |')))
    ctl('V13', 'the phase law restated inside the AZ node', scope_guards(sw('<TDRG-ALG-PARENT-CHILD-PHASE, TDRG-ALG-TOKEN-CENSUS-LAW, TDRG-DEF-ORIENT (engine', 'separation stays in {N/2,0} iff 4x≡0; <TDRG-ALG-PARENT-CHILD-PHASE, TDRG-ALG-TOKEN-CENSUS-LAW, TDRG-DEF-ORIENT (engine')))
    ctl('V14', 'the diagnostic read as a mechanism or a promotion', scope_guards(sw('¬ mechanism (the parent–child phase law names', 'mechanism: (the parent–child phase law names')) and scope_guards(sw('does not by itself close AZ-OPEN-PROMO or change the maturity level', 'closes AZ-OPEN-PROMO')))
    ctl('V15', 'supportive contrasts shown as confirmatory', scope_guards(sw(' (supportive only); PC4', ' (confirmatory); PC4').replace('equivalent within ±0.05 (supportive only)', 'equivalent within ±0.05', 1)))
    ctl('V16', 'a second home for the diagnostic', scope_guards(text + 'AZ-NUM-TOKRES-S1 NUM·dx | duplicate\n') or homes(text + 'AZ-NUM-TOKRES-S1 NUM·dx | duplicate\n'))
    ctl('V17', 'a new TDR-G RID without a home', homes('\n'.join(l for l in text.split('\n') if not l.startswith('TDRG-ALG-NARROW-BAND-CLASSES ALG |'))))
    ctl('V18', 'a new TDR-G RID misspelled against the source', run(sw('TDRG-ALG-SPECCONS-N ALG |', 'TDRG-ALG-SPECCONS-NN ALG |'), False) or homes(sw('TDRG-ALG-SPECCONS-N ALG |', 'TDRG-ALG-SPECCONS-NN ALG |')))
    ctl('V19', 'the artifact RID cited twice as a certificate', homes(sw('TDRG-ALG-EVENT-INVENTORY ALG | sc:', 'TDRG-ALG-EVENT-INVENTORY ALG | cert TDRG-ART-TOKEN-LAW-CHECKS | sc:')))
    ctl('V20', 'Thread C recovery read as full certification', scope_guards(sw('the owner keeps the [ENG PASS] records with these limits', 'all Thread C files are recovered and the grades are confirmed').replace('source-reported (EV-SRC-REPORTED, EV-NOT-RERUN; not described as recreated)', 'also deposited', 1)))
    ctl('V21', 'retired TDRG.G9 reused', run(text + 'TDRG.G9 ~ D-LINK: reused\n', False) and stale_editions(text + 'TDRG.G9 ~ D-LINK: reused\n'))
    ctl('V22', 'SOURCES row older than the manifest (TDRG)', run(sw('| v2.12.15 | `tdrg-v2.12.15` |', '| v2.12.14 | `tdrg-v2.12.14` |')) and stale_editions(sw('| v2.12.15 | `tdrg-v2.12.15` |', '| v2.12.14 | `tdrg-v2.12.14` |')))
    ctl('V23', 'SOURCES row older than the manifest (AZ)', run(sw('| v0.9 | `az-v0.9` |', '| v0.7 | `az-v0.7` |')) and stale_editions(sw('| v0.9 | `az-v0.9` |', '| v0.7 | `az-v0.7` |')))
    ctl('V24', 'AZ.A5 dropped', scope_guards('\n'.join(l for l in text.split('\n') if not l.startswith('AZ.A5 ~ D-LINK / SG trap:'))))
    ctl('V25', 'AZ open items shown as closed by the diagnostic', scope_guards(sw('AZ-OPEN-PROMO ACTIVE (Level-B promotion conditions incl. artifact/transcript provenance; not closed by AZ-NUM-TOKRES-S1)', 'AZ-OPEN-PROMO CLOSED')))
    ctl('V26', 'spectrum conservation assumed across births (SG-12)', scope_guards(sw('is OPEN and must not be assumed', 'holds')))
    wjson(OUT / 'negative_controls.json', controls); assert all(x['detected'] for x in controls), [x for x in controls if not x['detected']]
    wjson(OUT / 'edit_log.json', a.log)
    r = Edit(base); refresh(r); assert r.text == text   # replay
    (ROOT / ATLAS).write_text(text, encoding='utf-8')
    k1 = [e for e in a.log if e['finding'] == K1]
    summary = dict(status='DRAFT_REVIEW_READY', base_atlas=BASE_TAG, base_sha256=BASE_SHA, atlas_sha256=sha(text), atlas_bytes=len(text.encode()), atlas_lines=text.count('\n'),
                   base_bytes=len(base.encode()), base_lines=base.count('\n'), source_snapshot=SNAPSHOT, method=dict(tag=METHOD_TAG, sha256=METHOD_SHA), changed_sources=list(MOVED),
                   edit_operations=len(a.log), operations_by_finding=dict(Counter(e['finding'] for e in a.log)),
                   span_deletions_rule_4_1=dict(count=len(k1), bytes_removed=sum(len(e['old'].encode()) - len(e['new'].encode()) for e in k1)), span_deletions_rule_4_7=0,
                   retired_keys=list(newret), new_keys=[], moved_source_homes={r: dict(kind=k, home=p) for r, (k, p) in HOMES.items()},
                   new_identifiers=dict(TDRG=sorted(tdrg_new), AZ=sorted(az_new)), rids_at_tag=dict(TDRG=len(RID(t15)), AZ=len(RID(z9))),
                   owner_facts=owner_facts, pipes=dict(items=n_snap, snapshot=st_snap), dispositions=dict(Counter(d['disposition'] for d in disp)),
                   shared_counts={ch: dict(report.count(ch)) for ch in c.CHECKS}, shared_controls=len(shared), focused_controls=len(controls),
                   h_l5=dict(dangling=hm['dangling'], high_without_h=hm['high_l5_without_h'], l5_rows=hm['l5_rows']),
                   tool_sha256={'tools/atlas_check.py': sha((ROOT / 'tools/atlas_check.py').read_bytes()), 'evidence/atlas/build/refresh_v0_13.py': sha(Path(__file__).read_bytes()),
                                'evidence/atlas/build/refresh_v0_10.py': sha(Path(__file__).with_name('refresh_v0_10.py').read_bytes())},
                   limitations=['Structural checks only; no owner certificate was rerun for this edition; new identifiers are checked for presence in the tagged sources and for one home each, not re-proved.',
                                'Impact refresh of two moved sources; the other 16 sources were not re-extracted. TDR-G v2.12.15 was read in its full diff against v2.12.14 (all added lines, §6.13 in full) and through the atlas row check of 12 Nov 2026. AZ v0.9 was read in full at statement level (header, §§0.2–9, Appendix A v0.8/v0.9 entries, Appendix B); its Dyadic rows of §8 were read but not re-compared word by word with the Dyadic text, which is unchanged since atlas-v0.12.',
                                'The shared checker\'s coverage check extracts Dyadic RIDs only; the homes of the TDR-G and AZ identifiers are asserted by this builder (homes_check), which is not the shared tool.',
                                'Method §4.1 deletions were applied in D5 to edition labels on TDR-G nodes and to AZ edition labels made stale by the source movement (three edges outside D5: H2, the OPEN-M audit node, OPENM.U11; three Dyadic nodes\' AZ consumer clauses). Labels inside H4, H9, D5.X1 and the orientation node that distinguish what two editions state are kept (rule 4.1, third sentence). Rule 4.7 was not applied: no certificate-run span in D5 was identified as removable without rewording.',
                                'AZ-ART-ZETA-V3 loses the grade token ENG-historical because the owner removed that alias; the atlas line now carries no grade.'])
    wjson(OUT / 'verification_summary.json', summary)
    print(json.dumps({k: v for k, v in summary.items() if k not in ('owner_facts', 'moved_source_homes', 'limitations')}, ensure_ascii=False, indent=1))

if __name__ == '__main__':
    main()
