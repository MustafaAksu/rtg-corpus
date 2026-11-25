#!/usr/bin/env bash
# Stage 3c-a, W2 (second half): development check of second-order jets, the remainder in d, tube pieces and the
# local inverse (repository root). Not a certificate.
set -u
O=evidence/dyad/open20-an/stage3c-a; S=evidence/dyad/scripts/dyad_open20_an_stage3c_w2b_check.py
A=evidence/dyad/open20-an/stage2/scout_N216_dps840.json
python3 -I -B $S --stage2 $A --out $O/w2b_check.json > $O/w2b_check.stdout.txt; rc=$?
echo "W2b check exit=$rc (expected 0)"; [ "$rc" -eq 0 ] || { echo "UNEXPECTED: positive run"; exit 1; }
for C in SHRINKREM SHIFTINV; do
  python3 -I -B $S --stage2 $A --out $O/w2b_control_$C.json --control $C > $O/w2b_control_$C.stdout.txt; rc=$?
  echo "control $C exit=$rc (expected 1)"; [ "$rc" -eq 1 ] || { echo "UNEXPECTED: control $C"; exit 1; }
done
(cd $O && sha256sum w2b_check.json w2b_check.stdout.txt w2b_control_SHRINKREM.json w2b_control_SHRINKREM.stdout.txt \
   w2b_control_SHIFTINV.json w2b_control_SHIFTINV.stdout.txt run_w2b.sh > SHA256SUMS_W2B.txt)
echo "ALL AS EXPECTED"
