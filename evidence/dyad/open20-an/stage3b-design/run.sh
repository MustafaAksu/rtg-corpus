#!/usr/bin/env bash
# Stage-3b design: [NUM] sampling of the tube-lemma inequalities (repository root). Not a certificate.
# Stops unless the positive run exits 0 and each negative control exits exactly 1.
set -u
O=evidence/dyad/open20-an/stage3b-design; S=evidence/dyad/scripts/dyad_open20_an_stage3b_tube_sampling.py
A=evidence/dyad/open20-an/stage2/scout_N216_dps840.json; B=evidence/dyad/open20-an/stage2b/jump_scout.json
python3 -I -B $S --stage2 $A --stage2b $B --out $O/tube_sampling.json | grep -v '^seconds' > $O/tube_sampling.stdout.txt; rc=${PIPESTATUS[0]}
echo "sampling exit=$rc (expected 0)"; [ "$rc" -eq 0 ] || { echo "UNEXPECTED: positive run"; exit 1; }
for c in SWAP SHIFTCOEF; do
  python3 -I -B $S --stage2 $A --stage2b $B --out $O/control_$c.json --stride 3 --control $c | grep -v '^seconds' > $O/control_$c.stdout.txt; rc=${PIPESTATUS[0]}
  echo "control $c exit=$rc (expected 1)"; [ "$rc" -eq 1 ] || { echo "UNEXPECTED: control $c"; exit 1; }
done
(cd $O && sha256sum tube_sampling.json tube_sampling.stdout.txt control_*.json control_*.stdout.txt run.sh > SHA256SUMS.txt)
echo "ALL AS EXPECTED"
