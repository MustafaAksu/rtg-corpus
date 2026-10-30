#!/usr/bin/env bash
# Dyadic owner checks for the inbox round of 30 Oct 2026 (D1-D3). Run from the repository root of a checkout that
# contains PR #125's uploads (branch claude/atlas-advisory-dyad-inbox, or main after its merge).
# Owner run 30 Oct 2026: Linux, Python 3.13, python-flint 0.9.0, mpmath; about 2 s per run.
set -u
W=$(mktemp -d)
unzip -q upload/dyad-sources/NUMGEN_v1_20_8_DRAFT_r3_REVIEW.zip -d "$W/numgen"            # a7fc9ed6...e1ee84
unzip -q upload/dyad-sources/DYAD_RETURN_ENCLOSURE_P2B_v2_evidence.zip -d "$W/p2b"       # e4e2bab0...dbe4 (DSN-recorded)
R="$W/numgen/NUMGEN_v1_20_8_DRAFT_r3_REVIEW/replay_inputs_dyad"
P="$W/p2b/DYAD_RETURN_ENCLOSURE_P2B_v2/outputs/certificate.json"
S=evidence/dyad/scripts/dyad_inbox_20261030_owner_checks.py
O=evidence/dyad/inbox-20261030
python3 -I -B $S --rowa-dir "$R" --p2b-cert "$P" --out $O/owner_checks.json > $O/owner_checks.stdout.txt; echo "owner_checks exit=$?"
for c in A B C; do
  python3 -I -B $S --rowa-dir "$R" --p2b-cert "$P" --out $O/control_$c.json --control $c > $O/control_$c.stdout.txt; echo "control $c exit=$? (expected 1)"
done
rm -rf "$W"
(cd $O && sha256sum owner_checks.json owner_checks.stdout.txt control_A.json control_A.stdout.txt control_B.json control_B.stdout.txt control_C.json control_C.stdout.txt run.sh > SHA256SUMS.txt)
