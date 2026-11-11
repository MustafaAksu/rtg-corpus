#!/usr/bin/env bash
# OPEN 20 stage 2b: [NUM] scouting of the sectorial jump (repository root). Not a certificate.
# Stops with a nonzero exit if the positive run does not exit 0 or any negative control does not exit exactly 1.
set -u
O=evidence/dyad/open20-an/stage2b; S=evidence/dyad/scripts/dyad_open20_an_stage2b_jump_scout.py
I=evidence/dyad/open20-an/stage2/scout_N216_dps840.json
python3 -I -B $S --stage2 $I --out $O/jump_scout.json > $O/jump_scout.stdout.txt; rc=$?
echo "scout exit=$rc (expected 0)"; [ "$rc" -eq 0 ] || { echo "UNEXPECTED: positive run"; exit 1; }
for c in SHIFTCOEF WRONGMAP; do
  python3 -I -B $S --stage2 $I --out $O/control_$c.json --control $c --radii 0.40,0.30 > $O/control_$c.stdout.txt; rc=$?
  echo "control $c exit=$rc (expected 1)"; [ "$rc" -eq 1 ] || { echo "UNEXPECTED: control $c"; exit 1; }
done
python3 -I -B evidence/dyad/scripts/dyad_open20_an_stage2b_law.py --stage2 $I --out $O/jump_law.json > $O/jump_law.stdout.txt; rc=$?
echo "law exit=$rc (expected 0)"; [ "$rc" -eq 0 ] || { echo "UNEXPECTED: law run"; exit 1; }
(cd $O && sha256sum jump_scout.json jump_scout.stdout.txt jump_law.json jump_law.stdout.txt control_*.json control_*.stdout.txt run.sh > SHA256SUMS.txt)
echo "ALL AS EXPECTED"
