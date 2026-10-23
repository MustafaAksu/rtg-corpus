#!/usr/bin/env python3
r"""
e2c_production_driver.py — hash-gated production driver for RECOG CELL-E2C stage 1 (RECOG-THM-TWIN-RADIAL-ACCESS).
Imports the calibrated core recog_cell_e2c_twin_radial_access.py ONLY if its sha256 is exactly CORE_SHA256 (the core itself hash-gates the
frozen R8 engine). Grid 4096 x 32 flattened canonically: i = k_theta * NR + k_r, 0 <= i < 131072. Usage: python3 e2c_production_driver.py k0 k1
Writes e2c_prod_<k0>_<k1>.jsonl: one metadata line (driver + core + R8 hashes, parameters, range), then one record per index.
A leaf retired by an empty clipped set certifies by emptiness and carries no margin; margins are reported for hull-success leaves only.
"""
import sys, os, json, hashlib, importlib.util, time
CORE_SHA256 = "e0522aec291a6d3573ccb15e28045ad42b32e4e7225b5a616eeae34a0e1a1b22"
here = os.path.dirname(os.path.abspath(__file__)); core_path = os.path.join(here, "recog_cell_e2c_twin_radial_access.py")
if hashlib.sha256(open(core_path, 'rb').read()).hexdigest() != CORE_SHA256: print("[FAIL] calibrated core hash mismatch"); sys.exit(1)
spec = importlib.util.spec_from_file_location("e2c_core", core_path); core = importlib.util.module_from_spec(spec); spec.loader.exec_module(core)
NTH, NR = 4096, 32; NTOT = NTH*NR
k0, k1 = int(sys.argv[1]), int(sys.argv[2]); assert 0 <= k0 < k1 <= NTOT
assert (core.NTH_PROD, core.NR_PROD, core.NMAX, core.WSPLIT, core.LEAF_BUDGET) == (NTH, NR, 256, 0.05, 4096)
import flint
meta = dict(meta=True, rid="RECOG-THM-TWIN-RADIAL-ACCESS", driver_sha256=hashlib.sha256(open(__file__, 'rb').read()).hexdigest(),
            core_sha256=CORE_SHA256, r8_sha256=core.R8_SHA256, flint=flint.__version__, prec_bits=120, NTH=NTH, NR=NR, NMAX=core.NMAX,
            WSPLIT=core.WSPLIT, LEAF_BUDGET=core.LEAF_BUDGET, q1=str(core.q1), q2=str(core.q2), clip=True, range=[k0, k1],
            flatten="i = k_theta*NR + k_r")
out_path = os.path.join(here, f"e2c_prod_{k0}_{k1}.jsonl"); t0 = time.time(); bad = 0
with open(out_path, "w") as out:
    out.write(json.dumps(meta) + "\n")
    for i in range(k0, k1):
        kt, kr = divmod(i, NR)
        r = core.run_tile(kt, kr, NTH, NR); r['i'] = i
        out.write(json.dumps(r) + "\n"); out.flush()
        if not r['ok']: bad += 1; print("TILE FAIL", r, flush=True)
print(f"chunk [{k0},{k1}) done: {k1-k0} tiles, {bad} failures, {time.time()-t0:.1f}s -> {os.path.basename(out_path)}")
sys.exit(0 if bad == 0 else 1)
