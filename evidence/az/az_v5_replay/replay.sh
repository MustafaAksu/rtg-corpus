#!/usr/bin/env bash
# AZ Thread C (az_v5) recovery - replay of the three runnable deposited scripts. [SESSION] custody check.
# Runs from the repository root. The deposited files are never executed in place: benchmark_ladder.py writes into
# benchmarks/ next to itself and az1b_certify.py rewrites the registry there, so the package is copied to temporary
# directories first.
# usage: bash evidence/az/az_v5_replay/replay.sh     (needs python3 with numpy and scipy; well under a minute)
set -euo pipefail
SRC=upload/az-records/az_v5
OUT=evidence/az/az_v5_replay
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT
( cd upload/az-records && sha256sum -c --quiet SHA256SUMS )
echo "deposited bytes: SHA256SUMS OK"
python3 -I - "$SRC" <<'PY'
import hashlib, json, os, sys
src = sys.argv[1]
reg = json.load(open(os.path.join(src, "benchmarks", "AZ_ARTIFACT_REGISTRY.json")))["sha256"]
for rel, want in reg.items():
    p = os.path.join(src, rel)
    state = "absent" if not os.path.exists(p) else ("equal" if hashlib.sha256(open(p, "rb").read()).hexdigest() == want else "DIFFERENT")
    print("registry %-52s %s" % (rel, state))
    if state == "DIFFERENT":
        sys.exit(1)
PY
python3 -I -c "import sys, numpy, scipy; print('python', sys.version.split()[0], 'numpy', numpy.__version__, 'scipy', scipy.__version__)"

# ---- A. AZ-1A: benchmark ladder and solver acceptance, in a copy without any benchmark file
mkdir -p "$TMP/a/lib"
cp "$SRC"/lib/*.py "$TMP/a/lib/"
cp "$SRC"/benchmark_ladder.py "$SRC"/validate_solver.py "$TMP/a/"
set +e
( cd "$TMP/a" && python3 -I benchmark_ladder.py ) > "$TMP/ladder.txt" 2>&1; RC1=$?
( cd "$TMP/a" && python3 -I validate_solver.py ) > "$TMP/solver.txt" 2>&1; RC2=$?
set -e
echo "--- A. benchmark_ladder.py (exit code $RC1)"
sed "s#$TMP/a/##" "$TMP/ladder.txt"
echo "--- A. validate_solver.py (exit code $RC2; timings omitted)"
sed -E 's/ in [0-9.]+s//' "$TMP/solver.txt"
echo "--- A. regenerated benchmark files"
( cd "$TMP/a/benchmarks" && sha256sum az_v5_synthetic_benchmark_report.json )
cp "$TMP/a/benchmarks/az_v5_synthetic_benchmark_report.json" "$OUT/az_v5_synthetic_benchmark_report.regenerated.json"
python3 -I - "$SRC" "$TMP/a" <<'PY'
import hashlib, json, os, sys
import numpy as np
src, run = sys.argv[1], sys.argv[2]
reg = json.load(open(os.path.join(src, "benchmarks", "AZ_ARTIFACT_REGISTRY.json")))["sha256"]
rel = "benchmarks/az_v5_synthetic_benchmark_report.json"
got = hashlib.sha256(open(os.path.join(run, rel), "rb").read()).hexdigest()
print("regenerated report equals the registry entry of the missing original:", got == reg[rel])
a = json.load(open(os.path.join(src, "benchmarks/bouquet_2_4_hashimoto_matrix.json")))
b = json.load(open(os.path.join(run, "benchmarks/bouquet_2_4_hashimoto_matrix.json")))
same = all(a[k] == b[k] for k in ("k", "L", "edges", "matrix_size", "matrix"))
ea = np.array(a["eigenvalues_real"]) + 1j * np.array(a["eigenvalues_imag"])
eb = list(np.array(b["eigenvalues_real"]) + 1j * np.array(b["eigenvalues_imag"]))
d = 0.0
for x in ea:
    j = int(np.argmin([abs(x - y) for y in eb]))
    d = max(d, abs(x - eb[j]))
    eb.pop(j)
print("bouquet matrix: k, L, edges, matrix_size, matrix identical to the deposited original:", same)
print("bouquet matrix: stored eigenvalues, greedy multiset distance to the regenerated ones < 1e-6:", bool(d < 1e-6))
rd = lambda p: [complex(x.strip()) for x in open(p) if x.strip() and not x.startswith("#")]
ca = rd(os.path.join(src, "benchmarks/bouquet_2_4_charpoly.txt"))
cb = rd(os.path.join(run, "benchmarks/bouquet_2_4_charpoly.txt"))
print("bouquet charpoly: 9 coefficients, max difference to the regenerated ones < 1e-12:",
      len(ca) == len(cb) == 9 and bool(max(abs(x - y) for x, y in zip(ca, cb)) < 1e-12))
print("bouquet charpoly rounded to 9 places:", [round(c.real, 9) + 0.0 for c in ca])
ok = got == reg[rel] and same and d < 1e-6
sys.exit(0 if ok else 1)
PY

# ---- B. AZ-1B: certification over the deposited bytes plus the regenerated (hash-equal) report
mkdir -p "$TMP/b/lib" "$TMP/b/benchmarks"
cp "$SRC"/lib/*.py "$TMP/b/lib/"
cp "$SRC"/benchmark_ladder.py "$SRC"/validate_solver.py "$SRC"/az1b_certify.py "$TMP/b/"
cp "$SRC"/benchmarks/bouquet_2_4_hashimoto_matrix.json "$SRC"/benchmarks/bouquet_2_4_charpoly.txt "$TMP/b/benchmarks/"
cp "$TMP/a/benchmarks/az_v5_synthetic_benchmark_report.json" "$TMP/b/benchmarks/"
set +e
( cd "$TMP/b" && python3 -I az1b_certify.py ) > "$TMP/az1b.txt" 2>&1; RC3=$?
set -e
echo "--- B. az1b_certify.py (exit code $RC3; residuals omitted)"
sed -e "s#$TMP/b/##" -E -e 's/= [0-9.]+e-[0-9]+ over/= <residual> over/' "$TMP/az1b.txt"
( cd "$TMP/b/benchmarks" && sha256sum AZ_ARTIFACT_REGISTRY.json )
cmp "$TMP/b/benchmarks/AZ_ARTIFACT_REGISTRY.json" "$SRC/benchmarks/AZ_ARTIFACT_REGISTRY.json"
echo "registry written by the deposited az1b_certify.py is byte-identical to the deposited registry: True"
test "$RC1" -eq 0
test "$RC2" -eq 0
test "$RC3" -eq 0
echo "REPLAY PASS"
