#!/usr/bin/env python3
"""
Stage-2 coverage certificate and aggregator.
1. Re-derives the box plan from the config (same exact-rational tiling as the driver).
2. Coverage proof: for each sub-annulus and tau layer, the plane tiling by squares of side 2h anchored at the origin
   covers R^2; a point s of the sub-annulus lies in a square Q with dist(Q,0) <= |s| <= R_hi and
   maxdist(Q,0) >= |s| >= R_lo, so Q is selected.  tau layers [TAU_LO,TAU_HI] are checked to be contiguous.
   Hence region  subset  union(selected boxes).  Also verifies, for a random sample of exact rational points in the
   region, membership in a selected box (sanity, not the proof).
3. Reads results.jsonl; a (box,N) counts only with status PASS and matching engine/poly/config hashes.
4. Reports: missing boxes per N, global K_N = max K_up over boxes (upward), K_perp,N, per-ring maxima,
   and the largest remainders/lambda seen.  Exit 0 iff coverage proved AND no missing boxes for every N.
Usage: python triad_stage2_coverage.py --config CONFIG.json
"""
import sys, json, hashlib, random
from pathlib import Path
from fractions import Fraction as Fr
from decimal import Decimal
HERE = Path(__file__).resolve().parent
args = sys.argv[1:]
CFG_PATH = Path(args[args.index('--config')+1]) if '--config' in args else HERE / 'stage2_config.json'
CFG = json.loads(CFG_PATH.read_text())
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
H_ENGINE = sha(HERE / CFG['engine']); H_POLY = sha(HERE / CFG['poly']); H_CFG = hashlib.sha256(CFG_PATH.read_bytes()).hexdigest()

def tiles(h, rlo, rhi):
    h = Fr(h); rlo = Fr(rlo); rhi = Fr(rhi); side = 2*h; n = int(rhi/side) + 2; out = {}
    for i in range(-n, n):
        for j in range(-n, n):
            x0, x1, y0, y1 = i*side, (i+1)*side, j*side, (j+1)*side
            dx = 0 if x0 <= 0 <= x1 else min(abs(x0), abs(x1)); dy = 0 if y0 <= 0 <= y1 else min(abs(y0), abs(y1))
            if dx*dx + dy*dy <= rhi*rhi and max(abs(x0), abs(x1))**2 + max(abs(y0), abs(y1))**2 >= rlo*rlo:
                out[(x0, y0)] = (x0, x1, y0, y1)
    return out
def tau_layers():
    lo, hi, ht = Fr(CFG['TAU_LO']), Fr(CFG['TAU_HI']), Fr(CFG['HTAU']); L = []; t = lo
    while t < hi: L.append((t, t + 2*ht)); t += 2*ht
    return L
rings = [('inner', CFG['H_IN'], CFG['R_LO'], CFG['R_MID']), ('outer', CFG['H_OUT'], CFG['R_MID'], CFG['R_HI'])]
plan = {}
for ring, h, rlo, rhi in rings:
    T = tiles(h, rlo, rhi)
    for (x0, y0), sq in T.items():
        for (ta, tb) in tau_layers():
            plan[f"{ring}_x{x0}_y{y0}_t{ta}"] = dict(ring=ring, sq=sq, tau=(ta, tb), h=Fr(h))
# --- coverage proof (structural) + sampled sanity
ok = True
lay = tau_layers()
ok &= lay[0][0] == Fr(CFG['TAU_LO']) and lay[-1][1] >= Fr(CFG['TAU_HI']) and all(lay[i][1] == lay[i+1][0] for i in range(len(lay)-1))
print('tau layers contiguous and covering [TAU_LO,TAU_HI]:', ok)
print('sub-annuli contiguous (R_LO..R_MID..R_HI):', Fr(CFG['R_LO']) < Fr(CFG['R_MID']) < Fr(CFG['R_HI']))
print('structural coverage argument: plane tiling by origin-anchored squares of side 2h; selection = all squares meeting the sub-annulus (exact test) -> region subset of union. HOLDS by construction.')
random.seed(1); miss = 0
for _ in range(20000):
    rr = Fr(CFG['R_LO']) + (Fr(CFG['R_HI']) - Fr(CFG['R_LO'])) * Fr(random.randint(0, 10**6), 10**6)
    th = Fr(random.randint(0, 10**6), 10**6) * 2 * 355 / 113   # rational pseudo-angle
    import math
    x = rr * Fr(Decimal(math.cos(float(th))).quantize(Decimal('1e-12'))); y = rr * Fr(Decimal(math.sin(float(th))).quantize(Decimal('1e-12')))
    r2 = x*x + y*y
    if not (Fr(CFG['R_LO'])**2 <= r2 <= Fr(CFG['R_HI'])**2): continue
    found = any(sq[0] <= x <= sq[1] and sq[2] <= y <= sq[3] for b in plan.values() for sq in [b['sq']] if (b['ring'] == 'inner') == (r2 <= Fr(CFG['R_MID'])**2))
    miss += (not found)
print('sampled points of the annulus not in any selected square (sanity):', miss); ok &= (miss == 0)
# --- results
RES = HERE / CFG['results']; got = {}; rejected = []
def sigdigits(sv):
    d = Decimal(sv); return len(d.as_tuple().digits) if d != 0 else 1
def validate(r):
    """strict record contract: every published field must match the plan/config and be internally consistent."""
    why = []
    if r.get('status') != 'PASS': return ['status']
    for k, h in (('engine_sha256', H_ENGINE), ('poly_sha256', H_POLY), ('config_sha256', H_CFG)):
        if r.get(k) != h: why.append(k)
    bid = r.get('box_id'); b = plan.get(bid)
    if b is None: return why + ['unknown box_id']
    sq = b['sq']; ta, tb = b['tau']
    ep = r.get('endpoints', {})
    try:
        if [Fr(x) for x in ep['r']] != [sq[0], sq[1]] or [Fr(x) for x in ep['e']] != [sq[2], sq[3]] or [Fr(x) for x in ep['tau']] != [ta, tb]: why.append('endpoints')
    except Exception: why.append('endpoints-parse')
    if r.get('N') not in CFG['N_LIST']: why.append('N')
    if r.get('K_deg') != int(CFG['K']): why.append('K_deg')
    if r.get('dps') != int(CFG['DPS']): why.append('dps')
    if str(r.get('kt')) != str(CFG['KT']): why.append('kt')
    rlo = Fr(CFG['R_LO']) if b['ring'] == 'inner' else Fr(CFG['R_MID'])
    if Fr(r.get('R_floor', '0')) != rlo: why.append('R_floor')
    try:
        tol = Decimal(10) ** (-(int(CFG['DPS']) - 4))     # engine R_eff is the conservative lower endpoint of max(Rmin, R_floor)
        if not (Decimal(r['R_eff']) >= Decimal(rlo.numerator) / Decimal(rlo.denominator) - tol): why.append('R_eff<R_floor')
        if Decimal(r['Rmax']) <= Decimal(r['Rmin']): why.append('Rmin/Rmax')
        if Decimal(r['K_up']) < Decimal(r['K_raw']) or sigdigits(r['K_up']) > 4: why.append('K_up rounding')
        for k in ('bound_B_up', 'centre_abs_up', 'trans_B_up', 'K_perp_up'):
            if sigdigits(r[k]) > 4 or Decimal(r[k]) < 0: why.append(k)
        for k in ('rho_s', 'rho_c', 'lam_last', 'L_C', 'Rm_postmap'): Decimal(r[k])
        if [Fr(x) for x in r['tau_plus']] != [ta + 1, tb + 1]: why.append('tau_plus')
        st = r['steps']
        if len(st) != 6: why.append('steps!=6')
        for x in st:
            for k in ('edge_bound', 'lam', 'fresh_s', 'fresh_c', 'rho_s', 'rho_c'): Decimal(x[k])
            if len(x['comp_bounds']) != 4: why.append('comp_bounds')
        if Decimal(st[-1]['rho_c']) > Decimal(r['rho_c']) * Decimal('1.0000001') or Decimal(st[-1]['lam']) != Decimal(r['lam_last']): why.append('step/record mismatch')
    except Exception as ex: why.append(f'field-parse:{type(ex).__name__}')
    return why
if RES.exists():
    for line in RES.read_text().splitlines():
        try: r = json.loads(line)
        except Exception: rejected.append(('unparsable', ['json'])); continue
        why = validate(r)
        key = (r.get('box_id'), r.get('N'))
        if why: rejected.append((key, why)); continue
        if key in got and got[key]['K_raw'] != r['K_raw']: rejected.append((key, ['duplicate with different K_raw'])); got.pop(key, None); continue
        got[key] = r
print(f"records accepted {len(got)}, rejected {len(rejected)}" + (f"; first rejections: {rejected[:5]}" if rejected else ""))
complete = True
for N in CFG['N_LIST']:
    have = [plan_id for plan_id in plan if (plan_id, N) in got]; missing = [p for p in plan if (p, N) not in got]
    print(f"N={N}: boxes planned {len(plan)}, PASS with matching hashes {len(have)}, missing {len(missing)}")
    if have:
        Kmax = max(Decimal(got[(p, N)]['K_up']) for p in have); Kp = max(Decimal(got[(p, N)]['K_perp_up']) for p in have)
        worst = max(have, key=lambda p: Decimal(got[(p, N)]['K_up']))
        for ring in ('inner', 'outer'):
            hh = [p for p in have if plan[p]['ring'] == ring]
            if hh: print(f"   {ring}: max K_up = {max(Decimal(got[(p,N)]['K_up']) for p in hh)}  max K_perp_up = {max(Decimal(got[(p,N)]['K_perp_up']) for p in hh)}  ({len(hh)} boxes)")
        print(f"   max rho_c = {max(Decimal(got[(p,N)]['rho_c']) for p in have):.2e}, max lam = {max(Decimal(got[(p,N)]['lam_last']) for p in have):.3f}, worst box {worst}")
        if not missing: print(f"   ==> CERTIFIED over the whole region: K_{N} = {Kmax} (upward), K_perp,{N} = {Kp}")
        else: print(f"   partial (NOT a region certificate): max over available boxes K={Kmax}, K_perp={Kp}")
    complete &= not missing
sys.exit(0 if (ok and complete) else 1)
