#!/usr/bin/env bash
# Stage 3c-a, W2 (first half): development check of jets, tails and disc evaluation (repository root). Not a certificate.
set -u
O=evidence/dyad/open20-an/stage3c-a; S=evidence/dyad/scripts/dyad_open20_an_stage3c_w2_check.py
A=evidence/dyad/open20-an/stage2/scout_N216_dps840.json
python3 -I -B $S --stage2 $A --out $O/w2_check.json > $O/w2_check.stdout.txt; rc=$?
echo "W2 check exit=$rc (expected 0)"; [ "$rc" -eq 0 ] || { echo "UNEXPECTED: positive run"; exit 1; }
python3 -I -B $S --stage2 $A --out $O/w2_control_TAMPER.json --control TAMPER > $O/w2_control_TAMPER.stdout.txt; rc=$?
echo "control TAMPER exit=$rc (expected 1)"; [ "$rc" -eq 1 ] || { echo "UNEXPECTED: control"; exit 1; }
(cd $O && sha256sum w2_check.json w2_check.stdout.txt w2_control_TAMPER.json w2_control_TAMPER.stdout.txt run_w2.sh > SHA256SUMS_W2.txt)
echo "ALL AS EXPECTED"
