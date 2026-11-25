#!/usr/bin/env bash
# Stage 3c-a, W3: zone II of the tube lemma on a cover by pieces, for F on Omega_0 and for G on Omega_1
# (repository root). Not a certificate. The two sides run in parallel; about 20 minutes on two cores, with the controls.
set -u
O=evidence/dyad/open20-an/stage3c-a; S=evidence/dyad/scripts/dyad_open20_an_stage3c_w3_zone2.py
A=evidence/dyad/open20-an/stage2/scout_N216_dps840.json
python3 -I -B $S --stage2 $A --side 0 --rho0 0.05 --out $O/w3_zone2_F.json > $O/w3_zone2_F.stdout.txt & p0=$!
python3 -I -B $S --stage2 $A --side 1 --rho0 0.05 --out $O/w3_zone2_G.json > $O/w3_zone2_G.stdout.txt & p1=$!
wait $p0; rc0=$?; wait $p1; rc1=$?
echo "W3 zone II: F exit=$rc0, G exit=$rc1 (expected 0, 0)"; [ "$rc0" -eq 0 ] && [ "$rc1" -eq 0 ] || { echo "UNEXPECTED: positive run"; exit 1; }
for C in CORE SIGMA QZERO; do
  python3 -I -B $S --stage2 $A --side 0 --rho0 0.40 --out $O/w3_control_$C.json --control $C > $O/w3_control_$C.stdout.txt; rc=$?
  echo "control $C exit=$rc (expected 1)"; [ "$rc" -eq 1 ] || { echo "UNEXPECTED: control $C"; exit 1; }
done
(cd $O && sha256sum w3_zone2_F.json w3_zone2_F.stdout.txt w3_zone2_G.json w3_zone2_G.stdout.txt \
   w3_control_CORE.json w3_control_CORE.stdout.txt w3_control_SIGMA.json w3_control_SIGMA.stdout.txt \
   w3_control_QZERO.json w3_control_QZERO.stdout.txt run_w3.sh > SHA256SUMS_W3.txt)
echo "ALL AS EXPECTED"
