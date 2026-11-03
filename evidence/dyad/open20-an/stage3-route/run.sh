#!/usr/bin/env bash
# OPEN 20 stage-3 a-priori route check (repository root). Design calculation on recorded stage-1 data; no map evaluation.
# Stops with a nonzero exit if the positive run does not exit 0 or any negative control does not exit exactly 1.
set -u
O=evidence/dyad/open20-an/stage3-route; S=evidence/dyad/scripts/dyad_open20_an_stage3_apriori_route_check.py
I=evidence/dyad/open20-an/stage1_prep.json
python3 -I -B $S --stage1 $I --out $O/route_check.json > $O/route_check.stdout.txt; rc=$?
echo "check exit=$rc (expected 0)"; [ "$rc" -eq 0 ] || { echo "UNEXPECTED: positive run"; exit 1; }
for c in NOFAC ROOT TAMPER; do
  python3 -I -B $S --stage1 $I --out $O/control_$c.json --control $c > $O/control_$c.stdout.txt; rc=$?
  echo "control $c exit=$rc (expected 1)"; [ "$rc" -eq 1 ] || { echo "UNEXPECTED: control $c"; exit 1; }
done
(cd $O && sha256sum route_check.json route_check.stdout.txt control_*.json control_*.stdout.txt run.sh > SHA256SUMS.txt)
echo "ALL AS EXPECTED"
