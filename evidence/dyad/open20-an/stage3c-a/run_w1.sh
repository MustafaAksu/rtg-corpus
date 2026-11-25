#!/usr/bin/env bash
# Stage 3c-a, W1: development check of the series engine (repository root). Not a certificate.
set -u
O=evidence/dyad/open20-an/stage3c-a; S=evidence/dyad/scripts/dyad_open20_an_stage3c_w1_check.py
A=evidence/dyad/open20-an/stage2/scout_N216_dps840.json
python3 -I -B $S --stage2 $A --out $O/w1_check.json > $O/w1_check.stdout.txt; rc=$?
echo "W1 check exit=$rc (expected 0)"; [ "$rc" -eq 0 ] || { echo "UNEXPECTED: positive run"; exit 1; }
python3 -I -B $S --stage2 $A --out $O/w1_control_SHIFTCOEF.json --control SHIFTCOEF > $O/w1_control_SHIFTCOEF.stdout.txt; rc=$?
echo "control SHIFTCOEF exit=$rc (expected 1)"; [ "$rc" -eq 1 ] || { echo "UNEXPECTED: control"; exit 1; }
(cd $O && sha256sum w1_check.json w1_check.stdout.txt w1_control_SHIFTCOEF.json w1_control_SHIFTCOEF.stdout.txt run_w1.sh > SHA256SUMS_W1.txt)
echo "ALL AS EXPECTED"
