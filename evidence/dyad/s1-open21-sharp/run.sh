#!/usr/bin/env bash
# S1 certificate run (repository root). Inputs are the governing editions read from their tags.
set -u
W=$(mktemp -d); O=evidence/dyad/s1-open21-sharp; S=evidence/dyad/scripts/dyad_s1_open21_sharp_rows_cert.py
git show dyad-v6.4.23:dsn/RTG_DYADIC_OSCILLATOR_DSN.md > "$W/dyad.md"
git show recog-v0.3.26:dsn/RTG_RELATIONAL_RECOGNITION_DSN.md > "$W/recog.md"
python3 -I -B $S --dsn "$W/dyad.md" --recog "$W/recog.md" --out $O/s1_cert.json > $O/s1_cert.stdout.txt; echo "s1 exit=$?"
for c in C7 MIX FLOOR NOFACTOR W2; do
  python3 -I -B $S --dsn "$W/dyad.md" --recog "$W/recog.md" --out $O/control_$c.json --control $c > $O/control_$c.stdout.txt; echo "control $c exit=$? (expected 1)"
done
rm -rf "$W"
(cd $O && sha256sum s1_cert.json s1_cert.stdout.txt control_*.json control_*.stdout.txt run.sh > SHA256SUMS.txt)
