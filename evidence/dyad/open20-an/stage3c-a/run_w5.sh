#!/usr/bin/env bash
# Stage 3c-a, W5: the common arc (validated continuation, analytic tail, link), repository root. Not a certificate.
set -u
O=evidence/dyad/open20-an/stage3c-a; S=evidence/dyad/scripts/dyad_open20_an_stage3c_w5_arc.py
python3 -I -B $S --out $O/w5_arc.json > $O/w5_arc.stdout.txt; rc=$?
echo "W5 arc exit=$rc (expected 0)"; [ "$rc" -eq 0 ] || { echo "UNEXPECTED: positive run"; exit 1; }
for C in BIGSTEP CORE BRANCH; do
  python3 -I -B $S --out $O/w5_control_$C.json --control $C > $O/w5_control_$C.stdout.txt; rc=$?
  echo "control $C exit=$rc (expected 1)"; [ "$rc" -eq 1 ] || { echo "UNEXPECTED: control $C"; exit 1; }
done
(cd $O && sha256sum w5_arc.json w5_arc.stdout.txt w5_control_BIGSTEP.json w5_control_BIGSTEP.stdout.txt \
   w5_control_CORE.json w5_control_CORE.stdout.txt w5_control_BRANCH.json w5_control_BRANCH.stdout.txt run_w5.sh > SHA256SUMS_W5.txt)
echo "ALL AS EXPECTED"
