#!/usr/bin/env bash
# Stage 3c-a, W8: hand-over runs (repository root). DEVELOPMENT RUNS; not a certificate; no statement about the jump.
#   A  replay of the zone-II cover of Omega_0 and the inverse-branch run of Omega_1, both with the machine check of
#      every piece disc and of every float constant (lib: piece_disc, _assert_up); the replay must reproduce W3 byte for byte
#   B  the legs in the form the proof record covers (--full-fibre --strict-snd), and a replay of the W6 run
#   C  replays of W2, W2b, W4, W5 (positive runs) and the control "wrong branch"
# About 35 minutes on two cores.
set -u
O=evidence/dyad/open20-an/stage3c-a; SD=evidence/dyad/scripts; A=evidence/dyad/open20-an/stage2/scout_N216_dps840.json
T=$(mktemp -d); R=$O/w8_replay.txt; : > $R
same() { if cmp -s "$1" "$2"; then echo "identical: $(basename $2)" >> $R; else echo "DIFFERENT: $(basename $2)" >> $R; fi; }
# A
python3 -I -B $SD/dyad_open20_an_stage3c_w3_zone2.py --stage2 $A --side 0 --rho0 0.05 --out $T/w3_zone2_F.json > $T/w3_zone2_F.stdout.txt & p0=$!
python3 -I -B $SD/dyad_open20_an_stage3c_w7_branch.py --stage2 $A --w3 $O/w3_zone2_G.json --strict-e --out $O/w8_branch.json > $O/w8_branch.stdout.txt & p1=$!
wait $p0; rA0=$?; wait $p1; rA1=$?
same $T/w3_zone2_F.json $O/w3_zone2_F.json
# B
python3 -I -B $SD/dyad_open20_an_stage3c_w6_legs.py --stage2 $A --full-fibre --strict-snd --out $O/w8_legs.json > $O/w8_legs.stdout.txt & p0=$!
python3 -I -B $SD/dyad_open20_an_stage3c_w6_legs.py --stage2 $A --out $T/w6_legs.json > $T/w6_legs.stdout.txt & p1=$!
wait $p0; rB0=$?; wait $p1; rB1=$?
same $T/w6_legs.json $O/w6_legs.json
# C
python3 -I -B $SD/dyad_open20_an_stage3c_w2b_check.py --stage2 $A --out $T/w2b_check.json > $T/w2b.stdout.txt & p0=$!
( python3 -I -B $SD/dyad_open20_an_stage3c_w2_check.py --stage2 $A --out $T/w2_check.json > $T/w2.stdout.txt
  python3 -I -B $SD/dyad_open20_an_stage3c_w4_zone1.py --stage2 $A --w3dir $O --out $T/w4_zone1.json > $T/w4.stdout.txt
  python3 -I -B $SD/dyad_open20_an_stage3c_w5_arc.py --out $T/w5_arc.json > $T/w5.stdout.txt ) & p1=$!
wait $p0; wait $p1
same $T/w2b_check.json $O/w2b_check.json; same $T/w2_check.json $O/w2_check.json
same $T/w4_zone1.json $O/w4_zone1.json; same $T/w5_arc.json $O/w5_arc.json
python3 -I -B $SD/dyad_open20_an_stage3c_w4_zone1.py --stage2 $A --w3dir $O --out $O/w8_control_BRANCH.json --control BRANCH > $O/w8_control_BRANCH.stdout.txt; rC=$?
echo "exit codes: w3F replay=$rA0 branch=$rA1 legs=$rB0 w6 replay=$rB1 (expected 0 0 0 0); control BRANCH=$rC (expected 1)"
cat $R
[ "$rA0" -eq 0 ] && [ "$rA1" -eq 0 ] && [ "$rB0" -eq 0 ] && [ "$rB1" -eq 0 ] && [ "$rC" -eq 1 ] && ! grep -q DIFFERENT $R || { echo "UNEXPECTED"; exit 1; }
(cd $O && sha256sum w8_branch.json w8_branch.stdout.txt w8_legs.json w8_legs.stdout.txt w8_control_BRANCH.json w8_control_BRANCH.stdout.txt \
   w8_replay.txt run_w8.sh > SHA256SUMS_W8.txt)
rm -rf $T
echo "ALL AS EXPECTED"
