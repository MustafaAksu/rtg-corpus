#!/usr/bin/env bash
# Bridge note v1.1 replay (repository root). The note is the PI upload, unchanged; the DSN is read from its tag.
# Stops with a nonzero exit if the positive run does not exit 0 or any negative control does not exit exactly 1.
set -u
W=$(mktemp -d); trap 'rm -rf "$W"' EXIT
O=evidence/dyad/bridge-note-v1-1; S=evidence/dyad/scripts/dyad_bridge_note_v1_1_check.py
N=upload/dyad-bridge-note/dyad_triad_antisymmetric_bridge_v1_1.md
git show dyad-v6.4.23:dsn/RTG_DYADIC_OSCILLATOR_DSN.md > "$W/dyad.md" || exit 2
python3 -I -B $S --note $N --dsn "$W/dyad.md" --out $O/bridge_check.json > $O/bridge_check.stdout.txt; rc=$?
echo "check exit=$rc (expected 0)"; [ "$rc" -eq 0 ] || { echo "UNEXPECTED: positive run"; exit 1; }
for c in TAMPER KFORM NUSIGN ZFRAME DETMIX; do
  python3 -I -B $S --note $N --dsn "$W/dyad.md" --out $O/control_$c.json --control $c > $O/control_$c.stdout.txt; rc=$?
  echo "control $c exit=$rc (expected 1)"; [ "$rc" -eq 1 ] || { echo "UNEXPECTED: control $c"; exit 1; }
done
(cd $O && sha256sum bridge_check.json bridge_check.stdout.txt control_*.json control_*.stdout.txt run.sh > SHA256SUMS.txt)
echo "ALL AS EXPECTED"
