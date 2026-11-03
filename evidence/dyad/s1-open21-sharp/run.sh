#!/usr/bin/env bash
# S1 certificate run (repository root). Inputs are the governing editions read from their tags.
# Stops with a nonzero exit if the positive run does not exit 0 or any negative control does not exit exactly 1.
set -u
W=$(mktemp -d); trap 'rm -rf "$W"' EXIT
O=evidence/dyad/s1-open21-sharp; S=evidence/dyad/scripts/dyad_s1_open21_sharp_rows_cert.py
git show dyad-v6.4.23:dsn/RTG_DYADIC_OSCILLATOR_DSN.md > "$W/dyad.md" || exit 2
git show recog-v0.3.26:dsn/RTG_RELATIONAL_RECOGNITION_DSN.md > "$W/recog.md" || exit 2
python3 -I -B $S --dsn "$W/dyad.md" --recog "$W/recog.md" --out $O/s1_cert.json > $O/s1_cert.stdout.txt; rc=$?
echo "s1 exit=$rc (expected 0)"; [ "$rc" -eq 0 ] || { echo "UNEXPECTED: positive run"; exit 1; }
for c in C7 MIX FLOOR NOFACTOR W2; do
  python3 -I -B $S --dsn "$W/dyad.md" --recog "$W/recog.md" --out $O/control_$c.json --control $c > $O/control_$c.stdout.txt; rc=$?
  echo "control $c exit=$rc (expected 1)"; [ "$rc" -eq 1 ] || { echo "UNEXPECTED: control $c"; exit 1; }
done
(cd $O && sha256sum s1_cert.json s1_cert.stdout.txt control_*.json control_*.stdout.txt run.sh > SHA256SUMS.txt)
echo "ALL AS EXPECTED"
