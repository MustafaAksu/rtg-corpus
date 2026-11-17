#!/usr/bin/env python3
"""Atlas v0.13 -> v0.14 candidate: one impact refresh for two moved sources, under Atlas Method v0.3 (`atlas-method-v0.3`):
Discrete Genesis v2.13 (`tdrg-v2.13`, adopted 16 Nov 2026; maintenance edition: Methodology v1.4 migration, no result, RID or
§§2-9 grade changes) and Arithmetic Resonance and Zeta v0.10 (`az-v0.10`, adopted 16 Nov 2026; one addition, the AZ-owned
diagnostic AZ-NUM-TOKRES-S2). The other 16 sources are byte-identical to the v0.13 manifest and are not re-extracted.

TDR-G (D5; edges in D1): Methodology v1.4 declared; XFER-O08-01 open as a separate decision of both owners; the owner's AZ pin
az-v0.10; the stale "no plateau through N=1080" leaves (the owner dropped it); the owner's crystallization grade question is
recorded; *TDRG:policies takes the owner's per-branch grades (the old single [NUM strong] came from the former §1 typing);
*BIND3:d-table takes the owner's [ALG]; TDRG.G8 retired; METH.M1 without TDR-G; PROG.G6 records the migration.
AZ (D5; edges in D2): new node AZ-NUM-TOKRES-S2 [NUM diagnostic] with cert AZ-ART-TOKRES-S2, relations typed as for S1;
the pointers that named one diagnostic name both.
Method §4.1 span deletions (edition labels that only date a result), each logged with its rule and asserted contiguous.
Pipes: NUMGEN.N-I1 restated at the new snapshot.
Run from the repository root: python3 -I evidence/atlas/build/refresh_v0_14.py
"""
from __future__ import annotations
import importlib.util, json, re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'evidence/atlas/v0.14'
ATLAS = 'atlas/RTG_STATE_ATLAS.md'
SNAPSHOT = 'a5826ac'   # resolved to the full commit in main(); main after PR #292 (TDR-G v2.13 post-tag)
BASE_TAG = 'atlas-v0.13'
BASE_SHA = '208ddd9622b2ea9d291b40dbc103d6eaa3f357aa0e23b2de6190df2c0f879045'
METHOD_TAG, METHOD_SHA = 'atlas-method-v0.3', 'a29217352d989f75310f1c5fbb5e666cb02be9bc9a7c3b67d03d6e138115509f'
TDRG_PATH, AZ_PATH = 'dsn/RTG_DISCRETE_GENESIS_DSN.md', 'dsn/RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN.md'
MOVED = {'AZ': dict(edition='v0.10', tag='az-v0.10', authority='OWNER: release record `records/az/AZ_v0_10_RELEASE_RECORD.md` (PI adopted 16 Nov 2026)'),
         'TDRG': dict(edition='v2.13', tag='tdrg-v2.13', authority='OWNER: release record `records/tdrg/TDRG_v2_13_RELEASE_RECORD.md` (PI adopted 16 Nov 2026, candidate 6a4b94d5…de88; publication transform: Document status line only)')}
SHAS = {'AZ': '0cc84c9a587bab270624a824d5e004a327f20f41f0c03307e01a6725afe80e6e',
        'TDRG': '98b4cba5ecb30f23f9dd97be27a7896191aa514ddefc402fd129ea673f0357f6'}
HOMES = {'AZ-NUM-TOKRES-S2': ('node', 'AZ-NUM-TOKRES-S2 NUM·dx |'),
         'AZ-ART-TOKRES-S2': ('cert', 'AZ-NUM-TOKRES-S2 NUM·dx |')}
PIPE_SNAPSHOT = {'closed': 72, 'dispositioned': 1, 'open': 62}
ATLAS_ITEMS = ['pipes/ATLAS/20261116-AZ-v0-10-adopted.md']
PATHS = ['records/az/AZ_v0_10_RELEASE_RECORD.md', 'records/tdrg/TDRG_v2_13_RELEASE_RECORD.md', 'records/tdrg/ATLAS_ROW_CHECK_TDRG_v2_13.md',
         'records/az/AZ_TOKEN_RESONANCE_STAGE2_REPORT.md', 'records/az/AZ_TOKEN_RESONANCE_STAGE2_PREREGISTRATION.md'] + ATLAS_ITEMS

def _load(name):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).with_name(name + '.py'))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
R10 = _load('refresh_v0_10')   # Edit base class, h_l5_map, checker, pipe_states, git, sha, at, wjson, ROW
R13 = _load('refresh_v0_13')   # Edit with cut(), K1, LOC, k1_violations, node, RID
git, sha, at, wjson, h_l5_map, checker, pipe_states = R10.git, R10.sha, R10.at, R10.wjson, R10.h_l5_map, R10.checker, R10.pipe_states
K1, LOC, k1_violations, node, RID = R13.K1, R13.LOC, R13.k1_violations, R13.node, R13.RID

class Edit(R13.Edit):
    def rep(self, old, new, finding, where):
        R10.Edit.rep(self, old, new, finding, where); self.log[-1]['id'] = f'AR14-{len(self.log):03d}'
    def cut(self, prefix, span, where):
        l = self._one(prefix, K1, where); assert l.count(span) == 1, (where, span)
        self.rep(l, l.replace(span, ''), K1, where)

S2_NODE = ('AZ-NUM-TOKRES-S2 NUM·dx | sc: pinned TDR-G engine with TDRG-DEF-ORIENT; policy bound_symmetric; cells (N,k)∈{(240,16),(242,16),(480,32)}; four initial nodes; node cap 300; '
 'endpoint E_θ: M≥θ(N) at the horizon T(N), (T,θ)=(1460,106),(1460,84),(2670,114); endpoint E_100: M≥100 at tick 800; the 2x≡N/2 intervention only at N=240,480; '
 'conv: orientation reference of TDR-G v2.12.14 (profile P1; TDRG-DEF-ORIENT unchanged at tdrg-v2.12.15) | '
 'the registered paired intervention of AZ-NUM-TOKRES-S1, run in three further cells (1,500 base draws per cell; every arm on the same base draw): replacing one initial token by x with 2x≡0 (mod N) rather than by x±1 raises the probability of the endpoint in all three cells, and by x with 2x≡N/2 in the two cells where such values exist, on both endpoints; '
 'all ten contrasts of the single confirmatory family meet the registered support criterion for a risk difference above 0.05 (Holm-adjusted exact McNemar p<0.05 and the lower limit of the 99.5 % simultaneous Agresti–Min interval above 0.05) — '
 'E_θ: N=240 +0.2353 [+0.2035, +0.2666] (2x≡0), +0.1507 [+0.1233, +0.1776] (2x≡N/2); N=242 +0.2780 [+0.2435, +0.3118]; N=480 +0.2393 [+0.2065, +0.2715], +0.1580 [+0.1297, +0.1859]; '
 'E_100: N=240 +0.2060 [+0.1755, +0.2360], +0.1347 [+0.1083, +0.1606]; N=242 +0.2220 [+0.1913, +0.2521]; N=480 +0.2093 [+0.1787, +0.2394], +0.1427 [+0.1163, +0.1687]; '
 'the ten intervals are Bonferroni intervals with nominal 95 % joint coverage under the normal approximation, no exact finite-sample familywise coverage claimed; '
 'near-quarter control at N=242, separate from the family (one mixture arm over the four values nearest N/4, 3N/4): E_θ −0.0040 [−0.0144, +0.0064], E_100 −0.0020 [−0.0095, +0.0055], equivalent to the native state within ±0.05; the registered controls read as required | '
 'what it is: the total causal effect of the token replacement on each registered endpoint, for the engine, profile, policy, cells, horizons, cap and thresholds of the scope; a separate registration from AZ-NUM-TOKRES-S1, whose scope it does not widen; with it the contrast is observed at N=120,122,240,242,480 | '
 '¬ mechanism (action through the parent–child phase law untested); ¬ dependence or independence of the effect on N, ¬ the endpoints as the same event at different N (θ(N) calibrated on non-resonant native pilot draws; equality of population rates not shown); '
 '¬ other k/N, policies, profiles, horizons or thresholds; ¬ the TDR-26 birth-anchored discriminator, nothing about TDR-26 or any open module of TDR-G; ¬ relation to the 4|q rule, to DYAD cyclic-subgroup selection or to any DZT object (SG-AZ-3, SG-AZ-7); '
 'OPEN-P1 untouched; not a TDR-G result (TDR-G receives no separate item for it, PI 16 Nov 2026), not a bridge, no bridge-candidate promoted; does not by itself close AZ-OPEN-PROMO or change the maturity level | '
 '<TDRG-DEF-ORIENT (the engine and its orientation convention, as pinned in the scope; owned by TDR-G) | '
 'context (not a dependency): TDRG-ALG-PARENT-CHILD-PHASE (names the arithmetic condition of the intervention; not shown to be the mechanism of the effect) | '
 'checked law (not a dependency): TDRG-ALG-TOKEN-CENSUS-LAW (its registration formulation is the object of the per-tick check; no violation in the 26,300 campaign runs; no AZ number depends on it) | '
 'cert AZ-ART-TOKRES-S2 (in the repository: calibration pilot, registration with its package fixed by hash, authorisation, the 26,300 campaign records, report; the registered analysis re-derived byte-identically from the stored records, EV-CODE, EV-RUN; '
 'the engine runs were made once, on the PI\'s server, and are not rerun; EV-INDEP for the ten statistics from the published discordant counts only) @AZ§4.2.2')

def refresh(a: Edit):
    I, T, Z, P = 'identity', 'TDR-G v2.13', 'AZ v0.10', 'pipes'
    G = 'reviewed item (grade, qualifier or diagnostic change)'
    # ---- identity ----
    a.rep('# RTG STATE ATLAS v0.13\n', '# RTG STATE ATLAS v0.14\n', I, 'title')
    a.rep('evidence/atlas/v0.13/source_manifest.json', 'evidence/atlas/v0.14/source_manifest.json', I, 'SOURCES header')
    a.rep('*END — RTG STATE ATLAS v0.13.', '*END — RTG STATE ATLAS v0.14.', I, 'end line')
    a.line('| AZ | RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN | v0.9 |', '| AZ | RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN | v0.10 | `az-v0.10` | canonical Tier 5 |', I, 'SOURCES row AZ')
    a.line('| TDRG | RTG_DISCRETE_GENESIS_DSN | v2.12.15 |', '| TDRG | RTG_DISCRETE_GENESIS_DSN | v2.13 | `tdrg-v2.13` | canonical Tier 4 |', I, 'SOURCES row TDRG')
    a.rep('· DZT v0.8 · AZ v0.9 Thread A.', '· DZT v0.8 · AZ v0.10 Thread A.', I, 'D2 header, AZ')
    a.sub_in_line('(sources: TDRG = RTG_DISCRETE_GENESIS_DSN v2.12.15',
                  'TDRG = RTG_DISCRETE_GENESIS_DSN v2.12.15 (scientific scope edition of the v2.12 line: the star event domain stated as implemented, the token laws, TDR-6 partial; Methodology v1.2 declared by PI decision, the v1.4 migration is v2.13; Tier 4, maturity record B)',
                  'TDRG = RTG_DISCRETE_GENESIS_DSN v2.13 (Methodology v1.4 declared; §1 holds readouts that carry the owner grades of §§2–9 with RIDs and pointers; Tier 4, maturity record B)', I, 'D5 header, TDRG')
    a.sub_in_line('(sources: TDRG = RTG_DISCRETE_GENESIS_DSN v2.13',
                  'AZ = RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN v0.9 (infrastructure and diagnostic ledger; Methodology v1.4 declared; each owner result is cited once, in its §8; one AZ-owned diagnostic in Thread B; Tier 5, Level A retained)',
                  'AZ = RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN v0.10 (infrastructure and diagnostic ledger; Methodology v1.4 declared; each owner result is cited once, in its §8; two AZ-owned diagnostics in Thread B; Tier 5, Level A retained)', I, 'D5 header, AZ')

    # ================= TDR-G =================
    a.sub_in_line('RTG-OFN-ALG-STAR-TOKEN-SHIFT RES(from ALG) |', 'custody transfer XFER-O08-01 deferred by TDR-G to v2.13, the RID stays OFN\'s;',
                  'custody transfer XFER-O08-01 open, a separate decision of both owners (TDR-G §7), the RID stays OFN\'s;', T, 'OFN star-shift node: custody state as TDR-G states it')
    a.sub_in_line('admin queue (OFN, v0.11 §12.3–§12.4) |', 'custody deferred to TDR-G v2.13, RID stays OFN\'s',
                  'custody deferred to TDR-G v2.13 as this OFN queue records it (TDR-G §7: open, a separate decision of both owners), RID stays OFN\'s', T, 'OFN admin queue: OFN\'s record kept, TDR-G\'s current state added')
    a.sub_in_line('TDRG-DEF-STAR DEF |', 'custody transfer XFER-O08-01 deferred to v2.13)', 'custody transfer XFER-O08-01 open, a separate decision of both owners)', T, 'star node: custody state')
    a.sub_in_line('TDRG-THM-NARROW-BAND-EXCLUSION THM |', '(pin az-v0.7; the AZ statement is unchanged at az-v0.9)', '(pin az-v0.10)', T, 'narrow-band theorem: the owner\'s AZ pin')
    a.line('*TDRG:crystallization HEUR (extrapolation grade) |',
           '*TDRG:crystallization HEUR (extrapolation grade) | B_bulk/step→0 as N→∞ by extrapolation; sign unaffected by range choice; not theorem-grade (SG-6) | an owner grade question, unresolved: the [ADMIN] note of TDR-24B (§2) says [HEUR strong], TDR-22b and the §1 readouts say [HEUR] (TDR-G v2.13 release record §6) | >TDR-22b, TDR-24C @TDRG',
           G, 'crystallization: the stale clause "no plateau through N=1080" leaves (dropped by the owner; §6.8 extends to N=1440); the owner\'s grade question recorded')
    a.line('*TDRG:policies NUM strong |',
           '*TDRG:policies NUM (graded per statement as in the owner\'s §6.6) | bound_symmetric → crystallization NUM (p_ambig=0, slow growth); largest_center → continuous inflation NUM (rN_T≈0.76–0.80 at k/N≈0.0667; rN_late_birth=0.9995 at N=90,k=8; ms_bpe=1.00, ALG definitional); all_centers → avalanche HEUR strong (b/step≈16–25, often cap-limited; ms_bpe≈33.91 at N=60,k=4, NUM); rN_T(largest)>rN_T(all)>rN_T(bound_symmetric) at k/N≈0.0667 NUM (cap-protocol dependent); multi-birth b/step>1 universal NUM strong (1.03–1.24 bound_symmetric; 1.01–1.02 largest_center) @TDRG§6.6',
           G, 'policies: one [NUM strong] for all branches (the former §1 typing) replaced by the owner\'s per-statement grades')
    a.sub_in_line('*BIND3:d-table ALG/NUM strong |', '*BIND3:d-table ALG/NUM strong |', '*BIND3:d-table ALG (sc: N=24, k=1) |', G, 'BIND3 d-table: the owner grades the d-resolved anatomy [ALG] (§6.12)')
    a.drop_line('TDRG.G8 D-STALE (internal, layout):', G, 'TDRG.G8 retired')
    a.sub_in_line('METH.M1 D-GRADE (programme pattern):', 'persist in DZT, TDRG, OPEN-M, FMS session labels', 'persist in DZT, OPEN-M, FMS session labels (TDR-G v2.13 declares Methodology v1.4 and carries none)', G, 'METH.M1: TDR-G leaves the row')
    a.sub_in_line('PROG.G6 D-STALE (owner-recorded):', 'executed in part for TDR-G (v2.12.14 corrections edition; Methodology v1.4 migration planned for v2.13)',
                  'executed in part for TDR-G (v2.12.14 corrections edition; Methodology v1.4 migration planned for v2.13 — after that record, the TDR-G edition of this snapshot is that migration, Methodology v1.4 declared)', T, 'PROG.G6: TDR-G state after the Programme record')
    a.cut('TDRG-DEF-ORIENT DEF [COR v2.12.14] (alias TDRG-ORIENT)', ' [COR v2.12.14]', 'orientation node head')
    a.cut('TDRG-ALG-LEM-RETRIG ALG (alias LEM-RETRIG;', 'v2.12.14 wording; ', 'retrigger lemma: wording label')
    a.cut('D5.X1 D-LINK (ruled on the TDR-G side):', ' since v2.12.14', 'D5.X1: owner-review tasks')

    # ================= AZ =================
    a.sub_in_line('AZ-THREADS DEF |', 'one AZ-owned diagnostic, AZ-NUM-TOKRES-S1)', 'two AZ-owned diagnostics, AZ-NUM-TOKRES-S1 and AZ-NUM-TOKRES-S2)', Z, 'AZ threads: Thread B')
    a.after_line('AZ-NUM-TOKRES-S1 NUM·dx |', [S2_NODE], Z, 'new node: AZ-owned [NUM diagnostic], Stage 2')
    a.sub_in_line('*AZ:B-ledger (edges only;', '(local use: AZ-NUM-TOKRES-S1 only; no AZ number depends on them)', '(local use: AZ-NUM-TOKRES-S1 and AZ-NUM-TOKRES-S2 only; no AZ number depends on them)', Z, 'B ledger: local use')
    a.sub_in_line('AZ: AZ-OPEN-SCOPE-ZETA PARTIAL', 'not closed by AZ-NUM-TOKRES-S1)', 'not closed by AZ-NUM-TOKRES-S1 or AZ-NUM-TOKRES-S2)', Z, 'AZ frontier: PROMO')
    for pre in ('AZ.A5 ~ D-LINK / SG trap |', 'AZ.A5 ~ D-LINK / SG trap:'):
        a.sub_in_line(pre, 'the condition 4x≡0 of AZ-NUM-TOKRES-S1 is no evidence', 'the condition 4x≡0 of AZ-NUM-TOKRES-S1 and AZ-NUM-TOKRES-S2 is no evidence', Z, 'AZ.A5: both diagnostics (' + ('D2' if pre.endswith('|') else 'D5') + ' row)')
    a.sub_in_line('TDRG-DEF-ORIENT DEF (alias TDRG-ORIENT)', 'AZ-NUM-TOKRES-S1 (engine convention of its scope)', 'AZ-NUM-TOKRES-S1 and AZ-NUM-TOKRES-S2 (engine convention of their scopes)', Z, 'orientation node: reverse dependency of both diagnostics')
    a.sub_in_line('TDRG-ALG-TOKEN-CENSUS-LAW ALG |', '| checked by: AZ-NUM-TOKRES-S1 (its registration formulation is the object of the per-tick check of AZ\'s registered run;',
                  '| checked by: AZ-NUM-TOKRES-S1, AZ-NUM-TOKRES-S2 (its registration formulation is the object of the per-tick checks of AZ\'s registered runs;', Z, 'census law: checked by both')
    a.sub_in_line('TDRG-ALG-PARENT-CHILD-PHASE ALG |', '| context for: AZ-NUM-TOKRES-S1 (names the arithmetic condition of AZ\'s intervention;',
                  '| context for: AZ-NUM-TOKRES-S1, AZ-NUM-TOKRES-S2 (names the arithmetic condition of AZ\'s interventions;', Z, 'phase law: context for both')

    # ---- pipes census at the new snapshot ----
    a.line('NUMGEN.N-I1 D-LINK (pipe states, receiver side) |', 'NUMGEN.N-I1 D-LINK (pipe states, receiver side) | at the source snapshot a5826ac, pipes_index --check passes with 135 items in 20 inboxes — 72 closed, 1 dispositioned, 62 open. Open at the snapshot, by receiver: ATLAS (AZ v0.10; answered by this edition, closed by the atlas owner after the tag) · AZ (TDR-G v2.13) · DYAD (AZ v0.10) · DZT (DYAD N16–N21, AZ v0.7 and v0.8, LIT norm-law proof candidate) · ER2B (OFN v0.11, DYAD N16–N21) · FMS (OFN v0.11, v0.12) · GEN (LIT Regge interface inputs, PROG v1.4, DYAD v6.4.24) · LIT (DYAD LH2012 use report and Prop. 5.3 scope, SAT coil strong-null map-class search, SAT HCG Abdulali type III source) · NUMGEN (TDR-G v2.12.14 and v2.12.15, RECOG v0.3.26 and v0.3.27, DYAD v6.4.23 and v6.4.24, OFN v0.11 and v0.12, PROG v1.4) · OFN (DYAD v6.4.23 and v6.4.24, GEN v2.10, TRIAD v1.7, PROG v1.4, RECOG v0.3.27, TDR-G v2.12.15 and v2.13) · PREL (SAT finding on K₃ degeneracy and lift) · PROG (SAT satellite interface, AZ v0.7, v0.8, v0.9 and v0.10, TDR-G v2.12.15 and v2.13) · RECOG (DYAD v6.4.24) · RER (RECOG v0.3.26, DYAD N16–N21) · RRF (RECOG v0.3.26, OFN v0.11 and v0.12, DYAD N16–N21, GEN v2.10, TRIAD v1.7) · TRIAD (DYAD bridge-note recovery, GEN 𝒫₄-identity and birth-symmetry answers, GEN v2.10, PROG v1.4, DYAD v6.4.24) · UVM (GEN κ_f/B_*/sourced-junction items, DYAD N16–N21, GEN v2.10, TRIAD v1.7). TDRG has no open inbox item. A filed item is not adopted use; each receiver decides at its own checkpoint (CONVENTIONS §7).', P, 'pipe census at a5826ac')

STALE = [r'`tdrg-v2\.12\.15` \|', r'\| v2\.12\.15 \| `tdrg', r'`az-v0\.9` \|', r'\| v0\.9 \| `az', r'AZ v0\.9 Thread A', r'ZETA_DSN v0\.9 ', r'GENESIS_DSN v2\.12\.15 \(',
         r'no plateau through N=1080', r'XFER-O08-01 deferred', r'deferred by TDR-G to v2\.13', r'TDRG\.G8', r'persist in DZT, TDRG', r'DEF-ORIENT DEF \[COR', r'v2\.12\.14 wording',
         r'one AZ-owned diagnostic', r'pin az-v0\.7', r'Methodology v1\.2 declared by PI decision', r'\*TDRG:policies NUM strong', r'\*BIND3:d-table ALG/NUM', r'evidence/atlas/v0\.13/', r'snapshot 54cddd7',
         r'local use: AZ-NUM-TOKRES-S1 only', r'not closed by AZ-NUM-TOKRES-S1\)']
def stale_editions(text):
    return [l[:90] for l in text.split('\n') if not l.startswith('*ATLAS:checked-') and any(re.search(p, l) for p in STALE)]

S2_NUMBERS = ['0.2353', '0.1507', '0.2780', '0.2393', '0.1580', '0.2060', '0.1347', '0.2220', '0.2093', '0.1427', '26,300']

def scope_guards(text):
    bad = []; need = lambda cond, msg: None if cond else bad.append(msg)
    deps = lambda l, sig: [g for g in l.split(' | ') if g.startswith(sig)]
    s2 = node(text, 'AZ-NUM-TOKRES-S2 NUM·dx |')
    need(s2.rstrip().endswith('@AZ§4.2.2') and 'cert AZ-ART-TOKRES-S2' in s2, 'S2: AZ-owned, one node')
    need('(240,16),(242,16),(480,32)' in s2 and '(1460,106),(1460,84),(2670,114)' in s2 and 'M≥100 at tick 800' in s2 and 'bound_symmetric' in s2 and 'only at N=240,480' in s2 and 'conv: orientation reference of TDR-G v2.12.14' in s2, 'S2: scope and convention')
    need(all(n in s2 for n in S2_NUMBERS[:10]) and 'no exact finite-sample familywise coverage claimed' in s2 and 'within ±0.05' in s2, 'S2: the ten contrasts, coverage caveat, control')
    need('¬ mechanism' in s2 and '¬ dependence or independence of the effect on N' in s2 and '¬ the endpoints as the same event at different N' in s2 and 'whose scope it does not widen' in s2, 'S2: negatives')
    need('not a TDR-G result' in s2 and 'not a bridge, no bridge-candidate promoted' in s2 and 'does not by itself close AZ-OPEN-PROMO' in s2 and 'OPEN-P1 untouched' in s2, 'S2: ownership and promotion negatives')
    need(any(g.startswith('<TDRG-DEF-ORIENT (') for g in deps(s2, '<')) and not any('PARENT-CHILD' in g or 'TOKEN-CENSUS' in g for g in deps(s2, '<')), 'S2: one dependency')
    need('context (not a dependency): TDRG-ALG-PARENT-CHILD-PHASE (' in s2 and 'checked law (not a dependency): TDRG-ALG-TOKEN-CENSUS-LAW (' in s2 and 'iff 4x≡0' not in s2, 'S2: typed relations, law not restated')
    need(len([l for l in text.split('\n') if re.match(r'(?:AZ|TDRG)-NUM-TOKRES-S2', l)]) == 1, 'S2: one home')
    s1 = node(text, 'AZ-NUM-TOKRES-S1 NUM·dx |'); need('N∈{120,122}, k=8' in s1 and '¬ other N' in s1 and s1.rstrip().endswith('@AZ§4.2.1'), 'S1 unchanged in scope')
    for p in ('TDRG-ALG-TOKEN-CENSUS-LAW ALG |', 'TDRG-ALG-PARENT-CHILD-PHASE ALG |', 'TDRG-DEF-ORIENT DEF (alias TDRG-ORIENT)'):
        l = node(text, p); need('AZ-NUM-TOKRES-S2' in l and not any(n in l for n in S2_NUMBERS) and not any('AZ-NUM-TOKRES' in g for g in deps(l, '>') if p != 'TDRG-DEF-ORIENT DEF (alias TDRG-ORIENT)'), 'reverse relation, no AZ number: ' + p)
    need('checked by: AZ-NUM-TOKRES-S1, AZ-NUM-TOKRES-S2 (' in node(text, 'TDRG-ALG-TOKEN-CENSUS-LAW ALG |') and 'context for: AZ-NUM-TOKRES-S1, AZ-NUM-TOKRES-S2 (' in node(text, 'TDRG-ALG-PARENT-CHILD-PHASE ALG |'), 'reverse relations typed')
    cr = node(text, '*TDRG:crystallization HEUR (extrapolation grade) |'); need('not theorem-grade (SG-6)' in cr and '[HEUR strong]' in cr and 'unresolved' in cr, 'crystallization: grade question recorded, ceiling kept')
    po = node(text, '*TDRG:policies NUM (graded per statement'); need('avalanche HEUR strong' in po and 'crystallization NUM' in po and 'continuous inflation NUM' in po and 'universal NUM strong' in po and 'cap-protocol dependent' in po, 'policies: owner grades per statement')
    need(bool(node(text, '*BIND3:d-table ALG (sc: N=24, k=1) |')) and 'not poolable into headline' in node(text, '*BIND3:d-table ALG (sc: N=24, k=1) |'), 'BIND3 d-table: owner grade, caveat kept')
    for p in ('RTG-OFN-ALG-STAR-TOKEN-SHIFT RES(from ALG) |', 'TDRG-DEF-STAR DEF |'):
        need('XFER-O08-01 open, a separate decision of both owners' in node(text, p), 'XFER open: ' + p)
    need('as this OFN queue records it (TDR-G §7: open' in node(text, 'admin queue (OFN, v0.11 §12.3–§12.4) |'), 'OFN queue: OFN record kept apart from TDR-G state')
    need('(pin az-v0.10)' in node(text, 'TDRG-THM-NARROW-BAND-EXCLUSION THM |'), 'narrow-band: owner pin')
    need(bool(node(text, 'AZ.A5 ~ D-LINK / SG trap:')) and bool(node(text, 'AZ.A5 ~ D-LINK / SG trap |')), 'AZ.A5 kept (both rows)')
    fr = node(text, 'AZ: AZ-OPEN-SCOPE-ZETA PARTIAL'); need('AZ-OPEN-PROMO ACTIVE' in fr and 'not closed by AZ-NUM-TOKRES-S1 or AZ-NUM-TOKRES-S2' in fr, 'AZ frontier')
    need('Methodology v1.4 declared' in node(text, '(sources: TDRG = RTG_DISCRETE_GENESIS_DSN v2.13'), 'D5 header: TDR-G Methodology')
    need('the TDR-G edition of this snapshot is that migration' in node(text, 'PROG.G6 D-STALE (owner-recorded):'), 'PROG.G6: migration recorded')
    return bad

def homes_check(text, new):
    bad = []; lines = text.split('\n')
    for r in sorted(new):
        if r not in HOMES: bad.append(('no declared home', r)); continue
        kind, pre = HOMES[r]; hl = [l for l in lines if l.startswith(pre)]
        if len(hl) != 1: bad.append(('home line count', r, len(hl))); continue
        if kind == 'node' and len([l for l in lines if re.match(re.escape(r) + r'(?![A-Za-z0-9-])', l)]) != 1: bad.append(('node count', r))
        if kind == 'cert' and (len(re.findall(r'cert ' + re.escape(r) + r'(?![A-Za-z0-9-])', text)) != 1 or ('cert ' + r) not in hl[0]): bad.append(('cert home', r))
    return bad

def main():
    snap = git('rev-parse', SNAPSHOT + '^{commit}').decode().strip()
    base = at(BASE_TAG, ATLAS).decode(); assert sha(base) == BASE_SHA
    assert sha(at(METHOD_TAG, 'atlas/RTG_STATE_ATLAS_METHOD.md')) == METHOD_SHA and at(snap, 'atlas/RTG_STATE_ATLAS_METHOD.md') == at(METHOD_TAG, 'atlas/RTG_STATE_ATLAS_METHOD.md')
    a = Edit(base); refresh(a); text = a.text
    assert not k1_violations(a.log), k1_violations(a.log)
    assert not stale_editions(text), stale_editions(text)
    assert not scope_guards(text), scope_guards(text)
    # ---- manifest ----
    old = json.loads(at(BASE_TAG, 'evidence/atlas/v0.13/source_manifest.json'))
    m = json.loads(json.dumps(old))
    for k in ('note', 'first_candidate_snapshot', 'snapshot_note'): m.pop(k, None)
    for s in m['sources']:
        for k in [k for k in s if k.startswith('v0_12_')]: del s[k]
    m.update(atlas='v0.14', frozen_at='2026-11-17', repository_snapshot=snap, previous_atlas_tag=BASE_TAG, method_tag=METHOD_TAG, method_edition='v0.3', method_sha256=METHOD_SHA)
    for s in m['sources']:
        prev = next(x for x in old['sources'] if x['key'] == s['key'])
        s['v0_13_edition'] = prev['edition']; s['v0_13_input_sha256'] = prev['sha256']
        oldbytes = at(prev['tag'], prev['path']); assert sha(oldbytes) == prev['sha256'], s['key']
        if s['key'] in MOVED:
            mv = MOVED[s['key']]; data = at(mv['tag'], s['path'])
            s.update(edition=mv['edition'], tag=mv['tag'], commit=git('rev-parse', mv['tag'] + '^{commit}').decode().strip(), sha256=sha(data), authority=mv['authority'])
        data = at(s['tag'], s['path']); resolved = git('rev-parse', s['tag'] + '^{commit}').decode().strip()
        assert sha(data) == s['sha256'] and resolved == s['commit'], s['key']
        assert data == at(snap, s['path']), ('snapshot/tag divergence', s['key'])
        newest = git('tag', '--list', s['tag'].rsplit('-v', 1)[0] + '-v*', '--sort=v:refname').decode().split()[-1]
        assert newest == s['tag'], ('a newer source tag exists', s['key'], newest)
        s['v0_13_input_equality'] = 'EQUAL' if data == oldbytes else 'CHANGED'
    assert Counter(x['v0_13_input_equality'] for x in m['sources']) == {'EQUAL': 16, 'CHANGED': 2}
    assert {x['key'] for x in m['sources'] if x['v0_13_input_equality'] == 'CHANGED'} == set(MOVED)
    for k, h in SHAS.items(): assert next(s for s in m['sources'] if s['key'] == k)['sha256'] == h, k
    for t in ('az-v0.10', 'tdrg-v2.13'): assert git('cat-file', '-t', t).decode().strip() == 'tag', t
    wjson(OUT / 'source_manifest.json', m)
    # ---- H -> L5 ----
    hm = h_l5_map(text); assert not hm['dangling'], hm['dangling']
    wjson(OUT / 'h_l5_map.json', dict(convention='Every HEADLINE line cites L5 row ids only (many-to-one allowed). High L5 rows cited by no H are listed here and dispositioned in the release record.', **hm))
    # ---- retired keys (cumulative) ----
    oldret = json.loads(at(BASE_TAG, 'evidence/atlas/v0.13/retired_l5_keys.json'))
    newret = {'TDRG.G8': 'TDR-G v2.13 (tdrg-v2.13; release record §4): the row recorded three layout items the PI deferred to v2.13 on 27 Oct 2026 — the footer supersession chain of the v2.12.x point releases, the Appendix A ordering, and the Methodology v1.2 declaration. At tdrg-v2.13 the file has one footer line, Appendix A in edition order (v2.13, v2.12.15, v2.12.14, then one line per earlier edition), and declares Methodology v1.4. Nothing of the row remains.'}
    for k in newret: assert not re.search(r'(?<![A-Za-z0-9_.-])' + re.escape(k) + r'(?![A-Za-z0-9_-])', text), k
    assert not set(newret) & set(oldret['retired'])
    retired = oldret['retired'] + list(newret) + [k.replace('.', ' ') for k in newret if '.' in k]
    wjson(OUT / 'retired_l5_keys.json', dict(retired=retired, note='Keys not reused; v0.14 reasons in dispositions.json.'))
    # ---- shared checker (Method §7) ----
    c = checker(); src = c.load_sources(m)
    cmap = json.loads(at(BASE_TAG, 'evidence/atlas/v0.13/coverage_map.json'))
    cmap.pop('_note_v0_13', None)
    cmap['_note_v0_14'] = 'coverage_map.json of atlas-v0.13, unchanged in its homes. The checker\'s coverage check extracts Dyadic RIDs only; the homes of the identifiers new at az-v0.10 are asserted by the builder (verification_summary.json, moved_source_homes). tdrg-v2.13 declares the same RID set as tdrg-v2.12.15.'
    wjson(OUT / 'coverage_map.json', cmap)
    idmap = json.loads(at('atlas-v0.2', 'evidence/atlas/owner_identifier_map_v0_2.json'))
    report = c.run(text, m, src, cmap, idmap, retired)
    meta = dict(atlas=ATLAS, atlas_sha=sha(text), manifest='evidence/atlas/v0.14/source_manifest.json')
    c.write_report(report, str(OUT / 'atlas_check_report.md'), meta)
    wjson(OUT / 'atlas_check_report.json', dict(meta=meta, rows=report.rows))
    assert not report.fails(), report.fails()
    shared = c.self_test(m, src, cmap, idmap, retired, text)
    wjson(OUT / 'shared_controls.json', [dict(name=n, item=i, as_expected=bool(b)) for n, i, b in shared]); assert all(x[2] for x in shared), shared
    # ---- identifiers of the moved sources ----
    t15 = at('tdrg-v2.12.15', TDRG_PATH).decode(); t13 = src['TDRG']; z9 = at('az-v0.9', AZ_PATH).decode(); z10 = src['AZ']
    assert RID(t13) == RID(t15), (RID(t13) ^ RID(t15))
    assert RID(z9) <= RID(z10), RID(z9) - RID(z10)
    new = (RID(t13) - RID(t15)) | (RID(z10) - RID(z9))
    assert new == set(HOMES), (sorted(new - set(HOMES)), sorted(set(HOMES) - new))
    hc = homes_check(text, new); assert not hc, hc
    s2blk = z10[z10.index('#### §4.2.2'):z10.index('### §4.3')]
    owner_facts = dict(
        tdrg_methodology_v1_4='**DSN Methodology:** DSN_METHODOLOGY_v1.4' in t13,
        tdrg_xfer_open='Custody transfer XFER-O08-01: **open**, a separate decision of both owners' in t13,
        tdrg_az_pin='az-v0.10' in t13 and 'Verified source editions used by this release' in t13,
        tdrg_no_plateau_dropped='No plateau' not in t13 and 'no plateau' not in t13 and '1440' in t13,
        tdrg_policy_grades='`[NUM]` **Crystallization branch**' in t13 and '`[HEUR strong]` **Avalanche branch**' in t13 and '`[NUM strong]` **Multi-birth phenomenon (universal).**' in t13 and '[conv: `largest_center`] **Continuous inflation branch:**' in t13,
        tdrg_dtable_alg='`[ALG]` `[scope: $N=24$, $k=1$]` `[conv: v18 path orientation]` **d-resolved anatomy' in t13,
        tdrg_one_footer=t13.rstrip().count('\n*END') + t13.rstrip().startswith('*END') <= 1 and len(re.findall(r'^\*END', t13, re.M)) == 1,
        tdrg_appendix_order=t13.index('### v2.13 —') < t13.index('### v2.12.15 —') < t13.index('### v2.12.14 —') < t13.index('### v2.12.13 —') < t13.index('### v2.12 —'),
        tdrg_no_compound_tag=not re.search(r'`\[[A-Z]{2,6}/[A-Z]{2,6}', t13),
        tdrg_crystallization_question='[HEUR strong]' in t13 and 'Crystallization grade' in at(snap, 'records/tdrg/TDRG_v2_13_RELEASE_RECORD.md').decode(),
        tdrg_retrig_clause='least period is 2 for $d\\neq0$, and $d=0$ is a fixed point' in t13 and 'no other degenerate case occurs' in t13,
        programme_record_unchanged='Methodology v1.4 migration planned for v2.13' in src['PROG'] or 'planned for v2.13' in src['PROG'],
        az_s2_block='`[NUM diagnostic]` `[RID: AZ-NUM-TOKRES-S2]`' in s2blk and 'It is a separate registration from §4.2.1, whose scope it does not widen.' in s2blk,
        az_s2_numbers=all(n in s2blk for n in ['+0.2353', '+0.2035, +0.2666', '+0.1507', '+0.1233, +0.1776', '+0.2780', '+0.2435, +0.3118', '+0.2393', '+0.2065, +0.2715', '+0.1580', '+0.1297, +0.1859',
                                               '+0.2060', '+0.1755, +0.2360', '+0.1347', '+0.1083, +0.1606', '+0.2220', '+0.1913, +0.2521', '+0.2093', '+0.1787, +0.2394', '+0.1427', '+0.1163, +0.1687',
                                               '-0.0040', '-0.0144, +0.0064', '-0.0020', '-0.0095, +0.0055', '1,500 base draws', '26,300', '(1460,106),(1460,84),(2670,114)']),
        az_s2_negatives='No dependence or independence of the effect on $N$ is tested or claimed' in s2blk and 'no exact finite-sample familywise coverage is claimed' in s2blk and 'TDR-G receives no separate item for it (PI, 16 November 2026)' in s2blk,
        az_s2_artifact='[RID: AZ-ART-TOKRES-S2]' in z10 and 'the engine runs were made once, on the PI\'s server' in z10,
        az_s1_unchanged=z9[z9.index('#### §4.2.1'):z9.index('### §4.3')] .split('#### §4.2.2')[0] == z10[z10.index('#### §4.2.1'):z10.index('#### §4.2.2')],
        az_tdrg_pin_unchanged='`RTG_DISCRETE_GENESIS_DSN` v2.12.15 §6.13' in z10,
        az_open_status=z10.count('Status: ACTIVE') == 2 and z10.count('Status: PARTIAL') == 1,
        az_level_a='Maturity remains **Level A**' in z10)
    assert all(owner_facts.values()), [k for k, v in owner_facts.items() if not v]
    for p in PATHS: assert at(snap, p), p
    n_snap, st_snap = pipe_states(snap); assert n_snap == 135 and st_snap == PIPE_SNAPSHOT, (n_snap, st_snap)
    for it in ATLAS_ITEMS: assert re.search(r'^state:\s*open', at(snap, it).decode(), re.M), it
    # ---- dispositions ----
    def row(t, key):
        ls = [l for l in t.split('\n') if l.startswith(key + ' ')]; return '\n'.join(ls) if ls else None
    bl_ = base.split('\n'); i0 = bl_.index('### D5.L5 DIAGNOSTICS'); d5keys = []
    for l in bl_[i0 + 1:]:
        if l.startswith('#') or l.startswith('---'): break
        mm = R10.ROW.match(l)
        if mm: d5keys.append(mm.group(1))
    touched = list(dict.fromkeys(d5keys + ['PROG.G6', 'METH.M1', 'NUMGEN.N-I1']))
    disp = []
    for key in touched:
        o = row(base, key); n = row(text, key); assert o, key
        state = 'retired' if key in newret else ('retained' if n == o else 'reworded'); assert (n is None) == (key in newret), key
        why = [e['where'] for e in a.log if key in e['where'] or e['old'].startswith(key + ' ')]
        disp.append(dict(key=key, disposition=state, reason=newret.get(key, 'unchanged: what it records is unchanged at the v0.14 sources' if state == 'retained' else 'reworded; operations: ' + '; '.join(why)),
                         previous_sha256=sha(o), current_sha256=sha(n) if n else None))
    wjson(OUT / 'dispositions.json', disp)
    # ---- focused negative controls ----
    controls = []
    def ctl(cid, what, detected): controls.append(dict(id=cid, what=what, detected=bool(detected)))
    run = lambda t, with_sources=True: bool(c.run(t, m, src, cmap, idmap, retired, with_sources=with_sources).fails())
    def sw(old, new_, n=1):
        assert text.count(old) >= 1, old[:60]; return text.replace(old, new_, n)
    homes = lambda t: bool(homes_check(t, new))
    s2 = node(text, 'AZ-NUM-TOKRES-S2 NUM·dx |')
    ctl('W1', 'S2 placed under a TDR-G RID', scope_guards(sw('AZ-NUM-TOKRES-S2 NUM·dx |', 'TDRG-NUM-TOKRES-S2 NUM·dx |')) and homes(sw('AZ-NUM-TOKRES-S2 NUM·dx |', 'TDRG-NUM-TOKRES-S2 NUM·dx |')))
    ctl('W2', 'S2 under a TDR-G locator', scope_guards(sw('EV-INDEP for the ten statistics from the published discordant counts only) @AZ§4.2.2', 'EV-INDEP for the ten statistics from the published discordant counts only) @TDRG§6.13')))
    ctl('W3', 'an S2 number on a TDR-G node', scope_guards(sw('| context for: AZ-NUM-TOKRES-S1, AZ-NUM-TOKRES-S2 (', '| context for: AZ-NUM-TOKRES-S1, AZ-NUM-TOKRES-S2 (risk difference +0.2353 at N=240; ')))
    ctl('W4', 'the phase law made a dependency of S2', scope_guards(text.replace(s2, s2.replace('| context (not a dependency): TDRG-ALG-PARENT-CHILD-PHASE (', '| <TDRG-ALG-PARENT-CHILD-PHASE ('))))
    ctl('W5', 'the census law shown as consumed by S2', scope_guards(sw('| checked by: AZ-NUM-TOKRES-S1, AZ-NUM-TOKRES-S2 (', '| >AZ-NUM-TOKRES-S1, AZ-NUM-TOKRES-S2 (')))
    ctl('W6', 'S2 read as N-independence', scope_guards(text.replace(s2, s2.replace('¬ dependence or independence of the effect on N, ', ''))))
    ctl('W7', 'S2 read as widening S1', scope_guards(text.replace(s2, s2.replace('a separate registration from AZ-NUM-TOKRES-S1, whose scope it does not widen; ', ''))))
    ctl('W8', 'the coverage caveat of the ten intervals dropped', scope_guards(text.replace(s2, s2.replace(', no exact finite-sample familywise coverage claimed', ''))))
    ctl('W9', 'S2 shown as closing AZ-OPEN-PROMO', scope_guards(text.replace(s2, s2.replace('does not by itself close AZ-OPEN-PROMO or change the maturity level', 'closes AZ-OPEN-PROMO'))))
    ctl('W10', 'a second home for S2', scope_guards(text + 'AZ-NUM-TOKRES-S2 NUM·dx | duplicate\n') and homes(text + 'AZ-NUM-TOKRES-S2 NUM·dx | duplicate\n'))
    ctl('W11', 'the S2 artifact cited twice as a certificate', homes(sw('| cert AZ-ART-TOKRES-S1 (', '| cert AZ-ART-TOKRES-S2 | cert AZ-ART-TOKRES-S1 (')))
    ctl('W12', 'the stale plateau clause restored', stale_editions(sw('B_bulk/step→0 as N→∞ by extrapolation; sign', 'B_bulk/step→0 as N→∞ by extrapolation; no plateau through N=1080; sign')))
    ctl('W13', 'the crystallization grade question dropped', scope_guards(sw(' | an owner grade question, unresolved: the [ADMIN] note of TDR-24B (§2) says [HEUR strong], TDR-22b and the §1 readouts say [HEUR] (TDR-G v2.13 release record §6)', '')))
    ctl('W14', 'one [NUM strong] restored for all policy branches', scope_guards(sw('avalanche HEUR strong', 'avalanche NUM strong')) and stale_editions(text.replace(node(text, '*TDRG:policies NUM (graded per statement'), '*TDRG:policies NUM strong | all branches')))
    ctl('W15', 'BIND3 d-table compound grade restored', stale_editions(sw('*BIND3:d-table ALG (sc: N=24, k=1) |', '*BIND3:d-table ALG/NUM strong |')) and scope_guards(sw('*BIND3:d-table ALG (sc: N=24, k=1) |', '*BIND3:d-table ALG/NUM strong |')))
    ctl('W16', 'XFER custody shown as deferred to v2.13', stale_editions(sw('custody transfer XFER-O08-01 open, a separate decision of both owners)', 'custody transfer XFER-O08-01 deferred to v2.13)')) and scope_guards(sw('custody transfer XFER-O08-01 open, a separate decision of both owners)', 'custody transfer XFER-O08-01 deferred to v2.13)')))
    ctl('W17', 'the OFN queue record overwritten by the TDR-G state', scope_guards(sw('custody deferred to TDR-G v2.13 as this OFN queue records it (TDR-G §7: open, a separate decision of both owners)', 'custody open')))
    ctl('W18', 'retired TDRG.G8 reused', run(text + 'TDRG.G8 D-STALE: reused\n', False) and stale_editions(text + 'TDRG.G8 D-STALE: reused\n'))
    ctl('W19', 'METH.M1 still lists TDR-G', stale_editions(sw('persist in DZT, OPEN-M, FMS session labels (TDR-G v2.13 declares Methodology v1.4 and carries none)', 'persist in DZT, TDRG, OPEN-M, FMS session labels')))
    ctl('W20', 'SOURCES row older than the manifest (TDRG)', run(sw('| v2.13 | `tdrg-v2.13` |', '| v2.12.15 | `tdrg-v2.12.15` |')) and stale_editions(sw('| v2.13 | `tdrg-v2.13` |', '| v2.12.15 | `tdrg-v2.12.15` |')))
    ctl('W21', 'SOURCES row older than the manifest (AZ)', run(sw('| v0.10 | `az-v0.10` |', '| v0.9 | `az-v0.9` |')) and stale_editions(sw('| v0.10 | `az-v0.10` |', '| v0.9 | `az-v0.9` |')))
    ctl('W22', 'D5 header still declaring Methodology v1.2 for TDR-G', stale_editions(sw('TDRG = RTG_DISCRETE_GENESIS_DSN v2.13 (Methodology v1.4 declared;', 'TDRG = RTG_DISCRETE_GENESIS_DSN v2.13 (Methodology v1.2 declared by PI decision;')))
    ctl('W23', 'AZ.A5 dropped', scope_guards('\n'.join(l for l in text.split('\n') if not l.startswith('AZ.A5 ~ D-LINK / SG trap:'))))
    ctl('W24', 'a reworded span filed as a §4.1 deletion', bool(k1_violations([dict(finding=K1, old='(pin az-v0.7; the AZ statement is unchanged at az-v0.9)', new='(pin az-v0.10)')])))
    ctl('W25', 'an AZ pointer still naming one diagnostic', stale_editions(sw('(local use: AZ-NUM-TOKRES-S1 and AZ-NUM-TOKRES-S2 only;', '(local use: AZ-NUM-TOKRES-S1 only;')))
    wjson(OUT / 'negative_controls.json', controls); assert all(x['detected'] for x in controls), [x for x in controls if not x['detected']]
    wjson(OUT / 'edit_log.json', a.log)
    r = Edit(base); refresh(r); assert r.text == text   # replay
    (ROOT / ATLAS).write_text(text, encoding='utf-8')
    k1 = [e for e in a.log if e['finding'] == K1]
    summary = dict(status='DRAFT_REVIEW_READY', base_atlas=BASE_TAG, base_sha256=BASE_SHA, atlas_sha256=sha(text), atlas_bytes=len(text.encode()), atlas_lines=text.count('\n'),
                   base_bytes=len(base.encode()), base_lines=base.count('\n'), source_snapshot=snap, method=dict(tag=METHOD_TAG, sha256=METHOD_SHA), changed_sources=list(MOVED),
                   edit_operations=len(a.log), operations_by_finding=dict(Counter(e['finding'] for e in a.log)),
                   span_deletions_rule_4_1=dict(count=len(k1), bytes_removed=sum(len(e['old'].encode()) - len(e['new'].encode()) for e in k1)), span_deletions_rule_4_7=0,
                   retired_keys=list(newret), new_keys=[], moved_source_homes={r: dict(kind=k, home=p) for r, (k, p) in HOMES.items()},
                   new_identifiers=sorted(new), rids_at_tag=dict(TDRG=len(RID(t13)), AZ=len(RID(z10))),
                   owner_facts=owner_facts, pipes=dict(items=n_snap, snapshot=st_snap), dispositions=dict(Counter(d['disposition'] for d in disp)),
                   shared_counts={ch: dict(report.count(ch)) for ch in c.CHECKS}, shared_controls=len(shared), focused_controls=len(controls),
                   h_l5=dict(dangling=hm['dangling'], high_without_h=hm['high_l5_without_h'], l5_rows=hm['l5_rows']),
                   tool_sha256={'tools/atlas_check.py': sha((ROOT / 'tools/atlas_check.py').read_bytes()), 'evidence/atlas/build/refresh_v0_14.py': sha(Path(__file__).read_bytes()),
                                'evidence/atlas/build/refresh_v0_13.py': sha(Path(__file__).with_name('refresh_v0_13.py').read_bytes()),
                                'evidence/atlas/build/refresh_v0_10.py': sha(Path(__file__).with_name('refresh_v0_10.py').read_bytes())},
                   limitations=['Structural checks only; no owner certificate was rerun; the new identifiers are checked for presence in the tagged source and for one home each, not re-proved.',
                                'Impact refresh of two moved sources; the other 16 sources were not re-extracted. AZ v0.10 was read in its full diff against v0.9 (every changed line, §4.2.2 in full). TDR-G v2.13 was read through its release record, its stage-1 edit list and the atlas row checks of 16 Nov 2026 (four rounds, both stages rerun byte-identically), and at statement level where an Atlas line depends on it; it was not reread in full.',
                                'The shared checker\'s coverage check extracts Dyadic RIDs only; the homes of the AZ identifiers are asserted by this builder.',
                                'Four Atlas-side compound heads in D5 that this movement does not touch (*TDRG:TDR-24-factorization ALG/NUM, *TDRG:edge-builder ENG/ALG, *TDRG:slot-volume ALG/NUM strong, *NUMGEN:imp-DISC DEF/THM import) are left for a D5 opening; *BIND3:d-table is corrected because its grade differed from the owner\'s.'])
    wjson(OUT / 'verification_summary.json', summary)
    print(json.dumps({k: v for k, v in summary.items() if k not in ('owner_facts', 'moved_source_homes', 'limitations')}, ensure_ascii=False, indent=1))

if __name__ == '__main__':
    main()
