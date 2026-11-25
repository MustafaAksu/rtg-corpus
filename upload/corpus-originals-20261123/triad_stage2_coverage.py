#!/usr/bin/env python3
"""
Stage-2 coverage certificate and aggregator (v3), on the shared contract module.
Usage: python triad_stage2_coverage.py --config CONFIG.json [--results A.jsonl B.jsonl ...]
Exit 0 iff: structural coverage holds, every planned (box, N) has exactly one accepted payload, and no key is quarantined.
Even then the report says RECORD COVERAGE COMPLETE for engine-reported bounds; it does not certify the Taylor-model
lemmas, which are reviewed separately.
"""
import sys, random, math
from pathlib import Path
from fractions import Fraction as Fr
from decimal import Decimal
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); import triad_stage2_contract as C
args = sys.argv[1:]
CFG_PATH = Path(args[args.index('--config')+1]) if '--config' in args else HERE / 'stage2_config.json'
CFG, IDENT, CDIR = C.load_config(CFG_PATH)
if '--results' in args:
    i = args.index('--results'); RESS = [Path(a) for a in args[i+1:] if not a.startswith('--')]
else: RESS = [CDIR / CFG.get('results', 'stage2_results.jsonl')]
P = C.plan(CFG)
lay = C.tau_layers(CFG)
ok = lay[0][0] == Fr(CFG['TAU_LO']) and lay[-1][1] >= Fr(CFG['TAU_HI']) and all(lay[i][1] == lay[i+1][0] for i in range(len(lay)-1))
ok &= Fr(CFG['R_LO']) < Fr(CFG['R_MID']) < Fr(CFG['R_HI'])
print('tau layers contiguous/covering and sub-annuli ordered:', ok)
print('structural coverage: origin-anchored square tiling, selection = all squares meeting the sub-annulus (exact) -> region subset of union of planned boxes.')
random.seed(1); miss = 0
for _ in range(20000):
    rr = Fr(CFG['R_LO']) + (Fr(CFG['R_HI']) - Fr(CFG['R_LO'])) * Fr(random.randint(0, 10**6), 10**6)
    th = random.random() * 2 * math.pi
    x = rr * Fr(Decimal(math.cos(th)).quantize(Decimal('1e-12'))); y = rr * Fr(Decimal(math.sin(th)).quantize(Decimal('1e-12')))
    r2 = x*x + y*y
    if not (Fr(CFG['R_LO'])**2 <= r2 <= Fr(CFG['R_HI'])**2): continue
    ring = 'inner' if r2 <= Fr(CFG['R_MID'])**2 else 'outer'
    miss += not any(b['ring'] == ring and b['sq']['x0'] <= x <= b['sq']['x1'] and b['sq']['y0'] <= y <= b['sq']['y1'] for b in P.values())
print('sampled annulus points outside the planned boxes (sanity only):', miss); ok &= (miss == 0)
accepted, quarantined, rejected, fails = C.collect(RESS, P, CFG, IDENT)
print(f"result files {[p.name for p in RESS]}: accepted {len(accepted)}, quarantined {len(quarantined)}, invalid rows {len(rejected)}, FAIL rows {len(fails)}")
for k, w in rejected[:8]: print('   invalid:', k, w)
for k in list(quarantined)[:8]: print('   QUARANTINED:', k)
complete = not quarantined
for N in CFG['N_LIST']:
    have = [b for b in P if (b, N) in accepted]; missing = len(P) - len(have)
    print(f"N={N}: planned {len(P)}, accepted {len(have)}, missing {missing}")
    if have:
        Kmax = max(Decimal(accepted[(b, N)]['K_up']) for b in have); Kp = max(Decimal(accepted[(b, N)]['K_perp_up']) for b in have)
        for ring in ('inner', 'outer'):
            hh = [b for b in have if P[b]['ring'] == ring]
            if hh: print(f"   {ring}: max K_up {max(Decimal(accepted[(b,N)]['K_up']) for b in hh)}  max K_perp_up {max(Decimal(accepted[(b,N)]['K_perp_up']) for b in hh)}  ({len(hh)} boxes)")
        tag = 'RECORD COVERAGE COMPLETE (engine-reported upper bounds; Taylor-model lemma review pending)' if (missing == 0 and not quarantined) else 'PARTIAL — not a region result'
        print(f"   {tag}: K_{N} <= {Kmax}, K_perp,{N} <= {Kp}")
    complete &= (missing == 0)
sys.exit(0 if (ok and complete) else 1)
