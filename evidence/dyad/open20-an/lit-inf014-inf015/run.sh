#!/usr/bin/env bash
# Exact check of the DYAD-side hypotheses of LIT INF-014/INF-015 (repository root). Stops unless the positive run exits 0
# and each negative control exits exactly 1.
set -u
O=evidence/dyad/open20-an/lit-inf014-inf015; S=evidence/dyad/scripts/dyad_open20_lit_inf014_inf015_hypothesis_check.py
I=evidence/dyad/open20-an/stage1_prep.json
python3 -I -B $S --stage1 $I --out $O/hypothesis_check.json > $O/hypothesis_check.stdout.txt; rc=$?
echo "check exit=$rc (expected 0)"; [ "$rc" -eq 0 ] || { echo "UNEXPECTED: positive run"; exit 1; }
for c in ALPHA MUBAR; do
  python3 -I -B $S --stage1 $I --out $O/control_$c.json --control $c > $O/control_$c.stdout.txt; rc=$?
  echo "control $c exit=$rc (expected 1)"; [ "$rc" -eq 1 ] || { echo "UNEXPECTED: control $c"; exit 1; }
done
(cd $O && sha256sum hypothesis_check.json hypothesis_check.stdout.txt control_*.json control_*.stdout.txt run.sh > SHA256SUMS.txt)
echo "ALL AS EXPECTED"
