#!/usr/bin/env python3
"""[SESSION] Owner check of the C++ transfer pads (review of the F1 tube contractor, R4).

The C++ transfer (import_phi40.py of DYAD_CPP_PHI40_B_EVALUATOR_DIAGNOSTIC_V2) reads the 80-digit midpoint strings
info.coefficients[k] (k = 2..40) and the 40-digit info.c_pil of the stage-2 JSON and pads them by 1e-65 and 1e-32.
This script bounds, in ball arithmetic, the distance between those strings and the library's own balls of a_k and c
(dyad_open20_an_stage3c_lib: Consts and coefficients(K, 40) at 400 digits, the recursion of stage 2).
PASS if every distance (upper bound, modulus) is below the pad.  Run from evidence/dyad/scripts with -I off, e.g.
    cd evidence/dyad/scripts && python3 ../open20-an/cpp-review/f1-tube/dyad_open20_cpp_f1_transfer_check.py
"""
import hashlib, json, pathlib, sys
sys.path.insert(0, str(pathlib.Path.cwd()))
from flint import arb, acb, ctx
import dyad_open20_an_stage3c_lib as L

SRC = pathlib.Path('../open20-an/stage2/scout_N216_dps840.json')
SHA = '6ca8c663061ce2fa9e062938a1e6046c932da4cbddccc6e3e2c3de4df68c477e'
raw = SRC.read_bytes(); assert hashlib.sha256(raw).hexdigest() == SHA, 'source SHA mismatch'
info = json.loads(raw)['info']
ctx.dps = 400
K = L.Consts(); phi = L.coefficients(K, 40)
dk = max(arb(abs(phi[k] - acb(arb(info['coefficients'][str(k)][0]), arb(info['coefficients'][str(k)][1]))).upper())
         for k in range(2, 41))
dc = arb(abs(K.c - acb(arb(info['c_pil'][0]), arb(info['c_pil'][1]))).upper())
ok = bool(dk < arb('1e-65')) and bool(dc < arb('1e-32'))
print('SOURCE_SHA256', SHA)
print('MAX_COEFF_DISTANCE_UPPER k=2..40', dk.str(5, radius=False), '(pad 1e-65)')
print('C_DISTANCE_UPPER', dc.str(5, radius=False), '(pad 1e-32)')
print('PASS' if ok else 'FAIL')
sys.exit(0 if ok else 1)
