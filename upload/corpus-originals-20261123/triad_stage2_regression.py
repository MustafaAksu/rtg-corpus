#!/usr/bin/env python3
"""
Stage-2 infrastructure regression bundle (G1–G5 follow-up of 14 Oct).  NOT a mathematical certificate.
Needs, in one folder: engine v3.2, triad_stage2_contract.py, driver, coverage, the pinned coefficient table,
reg_config.json, and two GENUINE worker outputs W_inner.jsonl, W_outer.jsonl produced by
   python triad_stage2_driver.py --config reg_config.json --only inner --results W_inner.jsonl
   python triad_stage2_driver.py --config reg_config.json --only outer --results W_outer.jsonl
Each test states what it exercises; exit 0 iff every expectation holds.
"""
import sys, json, copy, subprocess, hashlib, shutil
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); import triad_stage2_contract as C
CFGP = HERE / 'reg_config.json'
CFG, IDENT, _ = C.load_config(CFGP); P = C.plan(CFG)
WI, WO = HERE / 'W_inner.jsonl', HERE / 'W_outer.jsonl'
results = []
def check(name, cond, detail=''):
    results.append(dict(name=name, ok=bool(cond), detail=detail)); print(('PASS ' if cond else 'FAIL ') + name + (f'  [{detail}]' if detail else ''))
def cov(*files):
    r = subprocess.run([sys.executable, '-I', str(HERE / 'triad_stage2_coverage.py'), '--config', str(CFGP), '--results', *map(str, files)],
                       capture_output=True, text=True, timeout=600)
    return r.returncode, r.stdout
genuine = [json.loads(l) for f in (WI, WO) for l in f.read_text().splitlines()]
genuine_pass = [r for r in genuine if r.get('status') == 'PASS']

# ---- positive path: genuine parallel worker outputs merge
check('genuine worker rows: all PASS and self-valid', len(genuine_pass) == 2*len(P) and all(not C.validate(r, P, CFG, IDENT) for r in genuine_pass), f'{len(genuine_pass)} rows')
rc, out = cov(WI, WO)
check('two-worker merge -> exit 0, RECORD COVERAGE COMPLETE wording (not CERTIFIED)', rc == 0 and 'RECORD COVERAGE COMPLETE' in out and 'CERTIFIED' not in out, out.strip().splitlines()[-1][:90])
rc1, _ = cov(WI)
check('one worker alone -> exit 1 (missing boxes)', rc1 == 1)

# ---- G1a mutations: each appended as an extra row next to the genuine file; must be rejected, key stays accepted
base = copy.deepcopy(genuine_pass[0]); key = (base['box_id'], base['N'])
def mut(name, f):
    r = copy.deepcopy(base); f(r)
    why = C.validate(r, P, CFG, IDENT)
    check(f'mutation rejected: {name}', bool(why), ','.join(why)[:80])
    return r
M = []
M.append(mut('negative K (K_raw=K_up=-1)', lambda r: r.update(K_raw='-1', K_up='-1')))
M.append(mut('infinite K', lambda r: r.update(K_raw='Infinity', K_up='Infinity')))
M.append(mut('R_eff=1 above Rmax', lambda r: r.update(R_eff='1')))
M.append(mut('rho_s = NaN', lambda r: r.update(rho_s='NaN')))
M.append(mut('negative step fresh_s', lambda r: r['steps'][2].update(fresh_s='-1')))
M.append(mut('non-numeric comp_bounds', lambda r: r['steps'][1].update(comp_bounds=['a', 'b', 'c', 'd'])))
M.append(mut('wrong endpoint', lambda r: r['endpoints'].update(r=['999', '1000'])))
M.append(mut('wrong Taylor degree', lambda r: r.update(K_deg=8)))
M.append(mut('wrong engine hash', lambda r: r.update(engine_sha256='0'*64)))
M.append(mut('five step records', lambda r: r.update(steps=r['steps'][:5])))
M.append(mut('down-rounded K (K_up < K_raw)', lambda r: r.update(K_up=str(float(r['K_raw'])*0.9)[:5])))
M.append(mut('wrong tau_plus', lambda r: r.update(tau_plus=['0', '1'])))
M.append(mut('R_eff below plan (too small)', lambda r: r.update(R_eff='0.001')))
M.append(mut('Rmax below plan', lambda r: r.update(Rmax=r['Rmin'])))
M.append(mut('K_up inconsistent with bound_B_up', lambda r: r.update(K_up='0.001', K_raw='0.001')))
M.append(mut('kt=2 inside record', lambda r: r.update(kt='2')))
mf = HERE / 'M_mut.jsonl'; mf.write_text(''.join(json.dumps(r) + '\n' for r in M))
rc, out = cov(WI, WO, mf)
check('genuine + 16 invalid rows -> invalid rows listed, still exit 0 (they never count)', rc == 0 and f'invalid rows {len(M)}' in out)

# ---- G1b duplicates
same = HERE / 'M_same.jsonl'; same.write_text(json.dumps(dict(base, seconds=999.9)) + '\n')
rc, out = cov(WI, WO, same)
check('identical scientific payload duplicate (only seconds differ) -> deduplicated, exit 0', rc == 0 and 'quarantined 0' in out)
conf = dict(copy.deepcopy(base)); conf['K_perp_up'] = str(int(float(base['K_perp_up'])) + 1)
check('conflict row is itself a VALID record (so the test is about payload conflict)', not C.validate(conf, P, CFG, IDENT))
cf = HERE / 'M_conflict.jsonl'; cf.write_text(json.dumps(conf) + '\n')
rc, out = cov(WI, WO, cf)
check('conflicting valid payload (K_perp_up only) -> key quarantined, exit 1', rc == 1 and 'quarantined 1' in out)
cf3 = HERE / 'M_conflict3.jsonl'; cf3.write_text(json.dumps(conf) + '\n' + json.dumps(base) + '\n')
rc, out = cov(WI, WO, cf3)
check('third repeat of the original does NOT resurrect the key -> still quarantined, exit 1', rc == 1 and 'quarantined 1' in out)
fl = HERE / 'M_fail.jsonl'; fl.write_text(json.dumps(dict(box_id=base['box_id'], N=base['N'], status='FAIL', error='synthetic')) + '\n')
rc, out = cov(WI, WO, fl)
check('a FAIL row does not block an existing valid PASS (retry policy) -> exit 0', rc == 0)

# ---- G1c resume uses the same contract
seed = HERE / 'R_seed.jsonl'
seed.write_text(''.join(json.dumps(dict(box_id=b, N=N, status='PASS', engine_sha256=IDENT['engine_sha256'], poly_sha256=IDENT['poly_sha256'],
                                        config_sha256=IDENT['config_semantic_sha256'])) + '\n' for b in P for N in CFG['N_LIST']))
r = subprocess.run([sys.executable, '-I', str(HERE / 'triad_stage2_driver.py'), '--config', str(CFGP), '--results', str(seed), '--max-boxes', '1'],
                   capture_output=True, text=True, timeout=600)
check('driver does NOT skip jobs on hash-only minimal PASS rows (runs 1 job)', 'done 1 runs' in r.stdout and 'accepted already: 0' in r.stdout, r.stdout.strip().splitlines()[-1])
r = subprocess.run([sys.executable, '-I', str(HERE / 'triad_stage2_driver.py'), '--config', str(CFGP), '--results', str(WI), '--only', 'inner'],
                   capture_output=True, text=True, timeout=600)
check('driver resume on complete genuine inner file -> 0 runs', 'done 0 runs' in r.stdout)
qf = HERE / 'R_quar.jsonl'; shutil.copy(WI, qf); qf.write_text(qf.read_text() + json.dumps(dict(conf, box_id=genuine_pass[0]['box_id'])) + '\n')
if base['ring'] == 'inner':
    r = subprocess.run([sys.executable, '-I', str(HERE / 'triad_stage2_driver.py'), '--config', str(CFGP), '--results', str(qf), '--only', 'inner'],
                       capture_output=True, text=True, timeout=600)
    check('driver reports a quarantined key and does not rerun it', 'QUARANTINED' in r.stdout and 'done 0 runs' in r.stdout)

# ---- G2 output-path identity
c2 = json.loads(CFGP.read_text()); c2['results'] = 'somewhere_else.jsonl'; p2 = HERE / 'reg_config_other_results.json'; p2.write_text(json.dumps(c2, indent=1))
_, id2, _ = C.load_config(p2)
check('changing only "results" leaves the semantic config hash unchanged', id2['config_semantic_sha256'] == IDENT['config_semantic_sha256'])
c3 = dict(c2, HTAU='0.5'); p3 = HERE / 'reg_config_other_math.json'; p3.write_text(json.dumps(c3, indent=1))
_, id3, _ = C.load_config(p3)
check('changing a mathematical field changes the semantic hash', id3['config_semantic_sha256'] != IDENT['config_semantic_sha256'])
check('--results override honoured by the driver (worker files exist and were used)', WI.exists() and WO.exists() and not (HERE / CFG['results']).exists())

# ---- G3 scope pins
c4 = dict(json.loads(CFGP.read_text()), KT='2'); p4 = HERE / 'reg_config_kt2.json'; p4.write_text(json.dumps(c4))
try: C.load_config(p4); ok = False
except ValueError: ok = True
check('config with KT=2 refused before any resume/evaluation', ok)
alt = HERE / 'alt_poly.json'; alt.write_text((HERE / CFG['poly']).read_text().replace('"-1/2"', '"-1/3"', 1))
c5 = dict(json.loads(CFGP.read_text()), poly='alt_poly.json'); p5 = HERE / 'reg_config_altpoly.json'; p5.write_text(json.dumps(c5))
try: C.load_config(p5); ok = False
except ValueError: ok = True
check('config naming a different coefficient table refused', ok)
import importlib.util
spec = importlib.util.spec_from_file_location('e', HERE / CFG['engine']); e = importlib.util.module_from_spec(spec); spec.loader.exec_module(e)
try: e.configure(4, alt, '1'); ok = False
except ValueError: ok = True
check('engine itself refuses a non-pinned table it is asked to load', ok)
e.configure(4, HERE / CFG['poly'], '1')
check('engine reports the SHA of the table it actually loaded = pinned', e.LOADED_POLY_SHA256 == C.PINNED_POLY_SHA256)

# ---- G5 nonfinite serialisation
for x in ('inf', '-inf', 'nan'):
    for fn in (e.dec_up, e.dec_down):
        try: fn(e.mp.mpf(x)); ok = False
        except ValueError: ok = True
        check(f'{fn.__name__}({x}) raises instead of returning "0"', ok)

n_ok = sum(r['ok'] for r in results)
print(f'\n{n_ok}/{len(results)} regression expectations hold (infrastructure only; no mathematical certification)')
json.dump(dict(engine_sha256=IDENT['engine_sha256'], config_semantic_sha256=IDENT['config_semantic_sha256'], poly_sha256=IDENT['poly_sha256'],
               scope='infrastructure regression; genuine K=4 coarse-tiling engine rows for the positive path; mutations derived from a genuine row',
               results=results), open(HERE / 'REGRESSION_RESULTS.json', 'w'), indent=1)
sys.exit(0 if n_ok == len(results) else 1)
