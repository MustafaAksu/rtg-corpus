#!/usr/bin/env bash
# Stage 3c-a, W4: zone I of the tube lemma (0 < |xi| <= 0.05), both sides, and the seam with the zone-II runs of W3
# (repository root). Not a certificate. About 8 minutes on two cores, with the three controls.
set -u
O=evidence/dyad/open20-an/stage3c-a; S=evidence/dyad/scripts/dyad_open20_an_stage3c_w4_zone1.py
A=evidence/dyad/open20-an/stage2/scout_N216_dps840.json
python3 -I -B $S --stage2 $A --w3dir $O --out $O/w4_zone1.json > $O/w4_zone1.stdout.txt & p0=$!
python3 -I -B $S --stage2 $A --w3dir $O --out $O/w4_control_BIGZONE.json --control BIGZONE > $O/w4_control_BIGZONE.stdout.txt & p1=$!
wait $p0; rc0=$?; wait $p1; rc1=$?
python3 -I -B $S --stage2 $A --w3dir $O --out $O/w4_control_SIGMA.json --control SIGMA > $O/w4_control_SIGMA.stdout.txt & p2=$!
python3 -I -B $S --stage2 $A --w3dir $O --out $O/w4_control_CORE.json --control CORE > $O/w4_control_CORE.stdout.txt & p3=$!
wait $p2; rc2=$?; wait $p3; rc3=$?
echo "W4 zone I exit=$rc0 (expected 0); controls BIGZONE=$rc1 SIGMA=$rc2 CORE=$rc3 (expected 1 1 1)"
[ "$rc0" -eq 0 ] && [ "$rc1" -eq 1 ] && [ "$rc2" -eq 1 ] && [ "$rc3" -eq 1 ] || { echo "UNEXPECTED"; exit 1; }
(cd $O && sha256sum w4_zone1.json w4_zone1.stdout.txt w4_control_BIGZONE.json w4_control_BIGZONE.stdout.txt \
   w4_control_SIGMA.json w4_control_SIGMA.stdout.txt w4_control_CORE.json w4_control_CORE.stdout.txt run_w4.sh > SHA256SUMS_W4.txt)
echo "ALL AS EXPECTED"
