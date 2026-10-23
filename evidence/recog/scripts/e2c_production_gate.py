#!/usr/bin/env python3
r"""
e2c_production_gate.py — fail-closed completeness gate for RECOG CELL-E2C stage 1. Usage: python3 e2c_production_gate.py [--partial] chunk1.jsonl ...
PASS (exit 0) only if: every chunk binds the same driver/core/R8 hashes and parameters; the supplied driver/core files hash to those values;
the chunk ranges partition [0, 131072) exactly; every index occurs exactly once; every record ok, n_hit <= 256, all numeric fields finite,
margin > 0 or null (null = success by certified-empty clipped set). Emits e2c_production_certificate.json on PASS.
--partial reports coverage and checks everything except completeness (exit 0 if all present records pass).
"""
import sys, json, math, hashlib, os
partial = "--partial" in sys.argv; files = [f for f in sys.argv[1:] if f != "--partial"]
here = os.path.dirname(os.path.abspath(__file__)); NTOT = 4096*32; errs = []
metas, recs, file_hashes = [], [], {}
for f in files:
    file_hashes[os.path.basename(f)] = hashlib.sha256(open(f, 'rb').read()).hexdigest()
    lines = [json.loads(l) for l in open(f)]
    m = [x for x in lines if x.get('meta')]
    if len(m) != 1: errs.append(f"{f}: expected exactly one metadata line"); continue
    metas.append(m[0]); rs = [x for x in lines if not x.get('meta')]
    lo, hi = m[0]['range']
    if sorted(r['i'] for r in rs) != list(range(lo, hi)): errs.append(f"{f}: records do not match declared range [{lo},{hi})")
    recs += rs
keys = ('driver_sha256', 'core_sha256', 'r8_sha256', 'prec_bits', 'NTH', 'NR', 'NMAX', 'WSPLIT', 'LEAF_BUDGET', 'q1', 'q2', 'clip', 'flatten')
if len({tuple(m[k] for k in keys) for m in metas}) != 1: errs.append("chunks do not share one hash/parameter binding")
m0 = metas[0] if metas else {}
for name, key in (("e2c_production_driver.py", 'driver_sha256'), ("recog_cell_e2c_twin_radial_access.py", 'core_sha256'), ("recog_cell_r8_hetero_enclosure.py", 'r8_sha256')):
    p = os.path.join(here, name)
    if not os.path.exists(p) or hashlib.sha256(open(p, 'rb').read()).hexdigest() != m0.get(key): errs.append(f"{name} does not hash to the bound value")
ranges = sorted(tuple(m['range']) for m in metas)
if not partial:
    if not ranges or ranges[0][0] != 0 or ranges[-1][1] != NTOT or any(ranges[j][1] != ranges[j+1][0] for j in range(len(ranges)-1)):
        errs.append("chunk ranges do not partition [0, 131072)")
ids = [r['i'] for r in recs]
if len(ids) != len(set(ids)): errs.append("duplicate indices")
if not partial and sorted(ids) != list(range(NTOT)): errs.append("indices are not exactly 0..131071")
def fin(v): return isinstance(v, (int, float)) and math.isfinite(v)
for r in recs:
    kt, kr = divmod(r['i'], 32)
    if (r['kt'], r['kr']) != (kt, kr): errs.append(f"i={r['i']}: flattening mismatch"); break
    if not r['ok']: errs.append(f"i={r['i']}: not ok ({r.get('fail')})"); break
    if not (fin(r['n_hit']) and r['n_hit'] <= 256): errs.append(f"i={r['i']}: n_hit"); break
    if not all(fin(r[k]) for k in ('leaves', 'peak', 'splits', 'clips', 'steps', 'max_wE')): errs.append(f"i={r['i']}: non-finite field"); break
    if not (r['margin'] is None or (fin(r['margin']) and r['margin'] > 0)): errs.append(f"i={r['i']}: margin"); break
cov = len(set(ids))
print(f"coverage {cov}/{NTOT} ({100*cov/NTOT:.2f}%); chunks {len(files)}; errors {len(errs)}")
for e in errs[:10]: print("  ERROR:", e)
if errs: print("E2C PRODUCTION GATE FAIL"); sys.exit(1)
if partial: print("E2C PRODUCTION GATE: partial check clean (completeness not asserted)"); sys.exit(0)
cert = dict(rid="RECOG-THM-TWIN-RADIAL-ACCESS", status="PASS", tiles=NTOT, chunk_files=file_hashes, binding={k: m0[k] for k in keys},
            max_leaves=max(r['leaves'] for r in recs), max_n_hit=max(r['n_hit'] for r in recs), max_wE=max(r['max_wE'] for r in recs),
            min_margin=min(r['margin'] for r in recs if r['margin'] is not None), empty_clip_only_tiles=sum(r['margin'] is None for r in recs),
            gate_sha256=hashlib.sha256(open(__file__, 'rb').read()).hexdigest())
json.dump(cert, open(os.path.join(here, "e2c_production_certificate.json"), "w"), indent=1); print("E2C PRODUCTION GATE PASS"); sys.exit(0)
