#!/usr/bin/env bash
# Stage 3c-a, W7: computations behind the proof record (repository root). Development runs; not a certificate.
#   structure: exact derivation of S1, S2, S3, S5 (a few seconds);  branch: one inverse branch for G (about 20 minutes).
set -u
O=evidence/dyad/open20-an/stage3c-a; A=evidence/dyad/open20-an/stage2/scout_N216_dps840.json
S=evidence/dyad/scripts/dyad_open20_an_stage3c_w7_structure.py; B=evidence/dyad/scripts/dyad_open20_an_stage3c_w7_branch.py
python3 -I -B $S --out $O/w7_structure.json > $O/w7_structure.stdout.txt; rc=$?
echo "W7 structure exit=$rc (expected 0)"; [ "$rc" -eq 0 ] || { echo "UNEXPECTED"; exit 1; }
for C in SCALE SHIFT; do
  python3 -I -B $S --out $O/w7_structure_control_$C.json --control $C > $O/w7_structure_control_$C.stdout.txt; rc=$?
  echo "structure control $C exit=$rc (expected 1)"; [ "$rc" -eq 1 ] || { echo "UNEXPECTED"; exit 1; }
done
python3 -I -B $B --stage2 $A --w3 $O/w3_zone2_G.json --out $O/w7_branch.json > $O/w7_branch.stdout.txt & p0=$!
python3 -I -B $B --stage2 $A --w3 $O/w3_zone2_G.json --out $O/w7_branch_control_SMALLSECTOR.json --control SMALLSECTOR > $O/w7_branch_control_SMALLSECTOR.stdout.txt & p1=$!
wait $p0; rc0=$?; wait $p1; rc1=$?
echo "W7 branch exit=$rc0 (expected 0); control SMALLSECTOR=$rc1 (expected 1)"
[ "$rc0" -eq 0 ] && [ "$rc1" -eq 1 ] || { echo "UNEXPECTED"; exit 1; }
(cd $O && sha256sum w7_structure.json w7_structure.stdout.txt w7_structure_control_SCALE.json w7_structure_control_SCALE.stdout.txt \
   w7_structure_control_SHIFT.json w7_structure_control_SHIFT.stdout.txt w7_branch.json w7_branch.stdout.txt \
   w7_branch_control_SMALLSECTOR.json w7_branch_control_SMALLSECTOR.stdout.txt run_w7.sh > SHA256SUMS_W7.txt)
echo "ALL AS EXPECTED"
