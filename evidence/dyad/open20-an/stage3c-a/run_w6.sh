#!/usr/bin/env bash
# Stage 3c-a, W6: the two legs at xi* and the two-disc test, with controls (repository root). DEVELOPMENT RUN.
# Not a certificate: no statement about the jump is drawn from the output. About 15 minutes on two cores.
set -u
O=evidence/dyad/open20-an/stage3c-a; S=evidence/dyad/scripts/dyad_open20_an_stage3c_w6_legs.py
A=evidence/dyad/open20-an/stage2/scout_N216_dps840.json
python3 -I -B $S --stage2 $A --out $O/w6_legs.json > $O/w6_legs.stdout.txt & p0=$!
python3 -I -B $S --stage2 $A --out $O/w6_control_SHORT.json --control SHORT > $O/w6_control_SHORT.stdout.txt & p1=$!
wait $p0; rc0=$?; wait $p1; rc1=$?
python3 -I -B $S --stage2 $A --out $O/w6_control_ZEROJUMP.json --control ZEROJUMP > $O/w6_control_ZEROJUMP.stdout.txt; rc2=$?
# Two further controls of design P11 act on the hypotheses of the lemma, not on the legs; they use the W4 and W5 scripts.
python3 -I -B evidence/dyad/scripts/dyad_open20_an_stage3c_w4_zone1.py --stage2 $A --w3dir $O --out $O/w6_control_ALPHA.json --control ALPHA > $O/w6_control_ALPHA.stdout.txt; rc3=$?
python3 -I -B evidence/dyad/scripts/dyad_open20_an_stage3c_w5_arc.py --out $O/w6_control_LOGBRANCH.json --control LOGBRANCH > $O/w6_control_LOGBRANCH.stdout.txt; rc4=$?
echo "W6 legs exit=$rc0 (expected 0); controls SHORT=$rc1 ZEROJUMP=$rc2 ALPHA=$rc3 LOGBRANCH=$rc4 (expected 1 1 1 1)"
[ "$rc0" -eq 0 ] && [ "$rc1" -eq 1 ] && [ "$rc2" -eq 1 ] && [ "$rc3" -eq 1 ] && [ "$rc4" -eq 1 ] || { echo "UNEXPECTED"; exit 1; }
(cd $O && sha256sum w6_legs.json w6_legs.stdout.txt w6_control_SHORT.json w6_control_SHORT.stdout.txt \
   w6_control_ZEROJUMP.json w6_control_ZEROJUMP.stdout.txt w6_control_ALPHA.json w6_control_ALPHA.stdout.txt \
   w6_control_LOGBRANCH.json w6_control_LOGBRANCH.stdout.txt run_w6.sh > SHA256SUMS_W6.txt)
echo "ALL AS EXPECTED"
