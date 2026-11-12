#!/usr/bin/env bash
# Owner check of the numbers and the inequality in LIT's subpetal reply (repository root). Stops unless the positive run
# exits 0 and each negative control exits exactly 1.
set -u
O=evidence/dyad/open20-an/lit-subpetal-reply; S=evidence/dyad/scripts/dyad_open20_lit_subpetal_reply_check.py
R=evidence/dyad/open20-an/stage3-route/route_check.json; J=evidence/dyad/open20-an/stage2b/jump_scout.json
python3 -I -B $S --route $R --scout $J --out $O/reply_check.json > $O/reply_check.stdout.txt; rc=$?
echo "check exit=$rc (expected 0)"; [ "$rc" -eq 0 ] || { echo "UNEXPECTED: positive run"; exit 1; }
for c in KCLASS SEC; do
  python3 -I -B $S --route $R --scout $J --out $O/control_$c.json --control $c > $O/control_$c.stdout.txt; rc=$?
  echo "control $c exit=$rc (expected 1)"; [ "$rc" -eq 1 ] || { echo "UNEXPECTED: control $c"; exit 1; }
done
(cd $O && sha256sum reply_check.json reply_check.stdout.txt control_*.json control_*.stdout.txt run.sh > SHA256SUMS.txt)
echo "ALL AS EXPECTED"
