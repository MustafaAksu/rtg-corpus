#!/usr/bin/env python3
"""
F3-FINITE-JET-CONTROL stage 2 — resumable box-sweep driver on engine v3.

Region (exact decimals): annulus R_LO <= |s|_2 <= R_HI, tau in [TAU_LO, TAU_HI]; kappa = sqrt3.
Tiling: two Cartesian square tilings (side 2h) anchored at the origin: 'inner' (h = H_IN) for the sub-annulus
[R_LO, R_MID], 'outer' (h = H_OUT) for [R_MID, R_HI]; tau layers of half-width HTAU.  A square is selected iff it
meets its sub-annulus (exact rational test on min/max distance to the origin).  Coverage: every point of the
sub-annulus lies in some square of the plane tiling, hence in a selected square -> union of selected boxes covers the
region (certified separately by triad_stage2_coverage.py).

Records: one JSON line per (box, N) in RESULTS, with exact rational endpoints, config/engine/poly hashes, K, dps,
status, upward-rounded constants (decimal strings), post-map radius, tau+1 interval, six per-step bounds, and the
B-orthogonal transverse defect.  A box counts as done only if a PASS record with matching hashes exists.

Usage:  python triad_stage2_driver.py --config CONFIG.json [--pilot] [--max-boxes M] [--only inner|outer]
"""
import sys, json, time, hashlib, itertools, importlib.util, traceback
from pathlib import Path
from fractions import Fraction as Fr
from decimal import Decimal, ROUND_CEILING

HERE = Path(__file__).resolve().parent
args = sys.argv[1:]
def opt(name, default, cast=str):
    return cast(args[args.index(name)+1]) if name in args else default
CFG_PATH = Path(opt('--config', str(HERE / 'stage2_config.json')))
PILOT = '--pilot' in args
MAXB = opt('--max-boxes', 0, int)
ONLY = opt('--only', '', str)

DEFAULT_CFG = dict(R_LO='0.03', R_MID='0.05', R_HI='0.08', H_IN='0.0025', H_OUT='0.005',
                   TAU_LO='0', TAU_HI='2', HTAU='0.5', K=8, DPS=30, N_LIST=[7, 8], KT='1',
                   engine='triad_tm_engine_v3.py', poly='age_family_polynomials_kt1.json', results='stage2_results.jsonl')
if not CFG_PATH.exists():
    CFG_PATH.write_text(json.dumps(DEFAULT_CFG, indent=1)); print('wrote default config', CFG_PATH)
CFG = json.loads(CFG_PATH.read_text())
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
H_ENGINE = sha(HERE / CFG['engine']); H_POLY = sha(HERE / CFG['poly']); H_CFG = hashlib.sha256(CFG_PATH.read_bytes()).hexdigest()

spec = importlib.util.spec_from_file_location('engine', HERE / CFG['engine']); eng = importlib.util.module_from_spec(spec); spec.loader.exec_module(eng)
eng.configure(int(CFG['K'])); eng.mp.mp.dps = int(CFG['DPS']); eng.iv.dps = int(CFG['DPS'])

# ---------------------------------------------------------------- tiling
def tiles(h, rlo, rhi):
    """all squares [i*2h,(i+1)*2h] x [j*2h,(j+1)*2h] meeting the annulus rlo<=|s|<=rhi (exact rationals)."""
    h = Fr(h); rlo = Fr(rlo); rhi = Fr(rhi); side = 2*h
    n = int(rhi / side) + 2; out = []
    for i in range(-n, n):
        for j in range(-n, n):
            x0, x1, y0, y1 = i*side, (i+1)*side, j*side, (j+1)*side
            dx = 0 if x0 <= 0 <= x1 else min(abs(x0), abs(x1)); dy = 0 if y0 <= 0 <= y1 else min(abs(y0), abs(y1))
            dmin2 = dx*dx + dy*dy; dmax2 = max(abs(x0), abs(x1))**2 + max(abs(y0), abs(y1))**2
            if dmin2 <= rhi*rhi and dmax2 >= rlo*rlo:
                out.append(dict(cx=x0 + h, cy=y0 + h, h=h, x0=x0, x1=x1, y0=y0, y1=y1))
    return out
def tau_layers():
    lo, hi, ht = Fr(CFG['TAU_LO']), Fr(CFG['TAU_HI']), Fr(CFG['HTAU'])
    layers = []; t = lo
    while t < hi:
        layers.append(dict(t0=t + ht, ht=ht)); t += 2*ht
    return layers
def box_list():
    L = []
    for ring, h, rlo, rhi in (('inner', CFG['H_IN'], CFG['R_LO'], CFG['R_MID']), ('outer', CFG['H_OUT'], CFG['R_MID'], CFG['R_HI'])):
        if ONLY and ring != ONLY: continue
        for sq in tiles(h, rlo, rhi):
            for ti, lay in enumerate(tau_layers()):
                bid = f"{ring}_x{sq['x0']}_y{sq['y0']}_t{lay['t0']-lay['ht']}"
                L.append(dict(id=bid, ring=ring, sq=sq, lay=lay, R_floor=Fr(rlo)))
    return L

def dec(x):   # plain decimal string (40 digits) of an interval endpoint / mpf
    return eng.mp.nstr(eng.mp.mpf(x.b if isinstance(x, eng.iv.mpf) else x), 40)
def upq(x, places=4):   # upward-rounded decimal string with `places` significant digits (x: upper endpoint)
    d = Decimal(dec(x))
    if d == 0: return '0'
    exp = d.adjusted() - places + 1
    return str(d.quantize(Decimal(10) ** exp, rounding=ROUND_CEILING))

def run_box(b, N):
    sq, lay = b['sq'], b['lay']
    t0 = time.time()
    res = eng.certify_box(N, str(sq['cx']), str(sq['cy']), str(lay['t0']), str(sq['h']), str(lay['ht']), R_floor=str(b['R_floor']))
    rec = dict(box_id=b['id'], ring=b['ring'], N=N, status='PASS', K_deg=int(CFG['K']), dps=int(CFG['DPS']), kt=CFG['KT'],
               engine_sha256=H_ENGINE, poly_sha256=H_POLY, config_sha256=H_CFG,
               endpoints=dict(r=[str(sq['x0']), str(sq['x1'])], e=[str(sq['y0']), str(sq['y1'])],
                              tau=[str(lay['t0']-lay['ht']), str(lay['t0']+lay['ht'])]),
               R_floor=str(b['R_floor']), Rmin=dec(res['Rmin'].a), Rmax=dec(res['Rmax'].b), R_eff=dec(res['R_eff'].a),
               bound_B_up=upq(res['bound_B'].b), centre_abs_up=upq(res['centre_abs'].b),
               K_up=upq(res['K'].b), K_raw=dec(res['K'].b), trans_B_up=upq(res['trans_B'].b), K_perp_up=upq(res['K_perp'].b),
               rho_s=dec(res['rem'][0].b), rho_c=dec(res['rem'][1].b), lam_last=dec(res['lam'].b), L_C=dec(res['L_C'].b),
               Rm_postmap=dec(res['Rm_postmap'].b), tau_plus=res['tau_plus'], steps=res['steps'], seconds=round(time.time()-t0, 1))
    return rec

RES = HERE / CFG['results']
done = set()
if RES.exists():
    for line in RES.read_text().splitlines():
        try: r = json.loads(line)
        except Exception: continue
        if r.get('status') == 'PASS' and r.get('engine_sha256') == H_ENGINE and r.get('poly_sha256') == H_POLY and r.get('config_sha256') == H_CFG:
            done.add((r['box_id'], r['N']))
boxes = box_list()
if PILOT:   # corners: inner radius at angle 0 and 135 deg, outer radius at 135 deg; first tau layer, plus one on the last layer
    def pick(ring, ang, rr, ti):
        import math
        tx, ty = rr*math.cos(ang), rr*math.sin(ang)
        cands = [b for b in boxes if b['ring'] == ring and list(tau_layers()).index(b['lay']) == ti]
        return min(cands, key=lambda b: (float(b['sq']['cx'])-tx)**2 + (float(b['sq']['cy'])-ty)**2)
    import math
    boxes = [pick('inner', 0, 0.03, 0), pick('inner', 3*math.pi/4, 0.03, 0), pick('outer', 3*math.pi/4, 0.08, 0), pick('inner', 3*math.pi/4, 0.03, len(tau_layers())-1)]
print(f"config {CFG_PATH.name} sha {H_CFG[:12]}; engine {CFG['engine']} sha {H_ENGINE[:12]}; poly sha {H_POLY[:12]}; K={CFG['K']} dps={CFG['DPS']}")
print(f"boxes in plan: {len(boxes)} (x {len(CFG['N_LIST'])} N) ; already done: {len(done)}")
count = 0
with open(RES, 'a') as f:
    for b in boxes:
        for N in CFG['N_LIST']:
            if (b['id'], N) in done: continue
            if MAXB and count >= MAXB: break
            try:
                rec = run_box(b, N)
                print(f"PASS {b['id']} N={N} R_eff={rec['R_eff'][:7]} K_up={rec['K_up']} K_perp_up={rec['K_perp_up']} rho_c={rec['rho_c'][:8]} [{rec['seconds']}s]")
            except Exception as ex:
                rec = dict(box_id=b['id'], N=N, status='FAIL', error=repr(ex), trace=traceback.format_exc()[-800:],
                           engine_sha256=H_ENGINE, poly_sha256=H_POLY, config_sha256=H_CFG)
                print(f"FAIL {b['id']} N={N}: {ex!r}")
            f.write(json.dumps(rec) + '\n'); f.flush(); count += 1
print('done', count, 'runs this session')
