#!/usr/bin/env bash
# Stage 3c-a, W8 (r2): hand-over runs (repository root). DEVELOPMENT RUNS; not a certificate; no statement about the jump.
#   A  replays of the zone-II covers of W3 (both sides), with the machine check of every piece disc and float bound
#   B  the inverse branch with --strict-e, and a replay of the W7 branch run
#   C  the legs in the form the proof record covers (--full-fibre --strict-snd), and a replay of the W6 run
#   D  replays of W2, W2b, W4, W5 (positive runs), a replay of the control "zero-jump model" of W6 (must fail as before),
#      and the control "wrong branch"
# Every positive process must exit 0 AND every replay must be byte-identical to the committed output.
# A control of this rule is run at the end: a replay that writes the correct file and then exits 1 must be rejected.
# About 50 minutes on two cores.
set -u
O=evidence/dyad/open20-an/stage3c-a; SD=evidence/dyad/scripts; A=evidence/dyad/open20-an/stage2/scout_N216_dps840.json
T=$(mktemp -d); R=$O/w8_replay.txt; RC=$T/rc.txt; : > $R; : > $RC
POS="w3F w3G branch w7branch legs w6legs w2b w2 w4 w5"
run() { n=$1; shift; "$@"; echo "$n $?" >> $RC; }           # run a process and record its exit code under a name
same() { if cmp -s "$1" "$2"; then echo "identical: $(basename $2)" >> $R; else echo "DIFFERENT: $(basename $2)" >> $R; fi; }
verdict() {  # $1: file of "name code" lines, $2: replay report. 0 iff every name of POS is present once with code 0 and no DIFFERENT
  for n in $POS; do [ "$(awk -v n=$n '$1==n{c++; if($2!=0) b=1} END{print (c==1 && !b) ? "ok" : "bad"}' $1)" = ok ] || return 1; done
  ! grep -q DIFFERENT $2
}
py() { python3 -I -B "$@"; }
# A
( run w3F py $SD/dyad_open20_an_stage3c_w3_zone2.py --stage2 $A --side 0 --rho0 0.05 --out $T/w3_zone2_F.json > $T/o1.txt ) & p0=$!
( run w3G py $SD/dyad_open20_an_stage3c_w3_zone2.py --stage2 $A --side 1 --rho0 0.05 --out $T/w3_zone2_G.json > $T/o2.txt ) & p1=$!
wait $p0; wait $p1
same $T/w3_zone2_F.json $O/w3_zone2_F.json; same $T/w3_zone2_G.json $O/w3_zone2_G.json
# B
( run branch py $SD/dyad_open20_an_stage3c_w7_branch.py --stage2 $A --w3 $O/w3_zone2_G.json --strict-e --out $O/w8_branch.json > $O/w8_branch.stdout.txt ) & p0=$!
( run w7branch py $SD/dyad_open20_an_stage3c_w7_branch.py --stage2 $A --w3 $O/w3_zone2_G.json --out $T/w7_branch.json > $T/o3.txt ) & p1=$!
wait $p0; wait $p1
same $T/w7_branch.json $O/w7_branch.json
# C
( run legs py $SD/dyad_open20_an_stage3c_w6_legs.py --stage2 $A --full-fibre --strict-snd --out $O/w8_legs.json > $O/w8_legs.stdout.txt ) & p0=$!
( run w6legs py $SD/dyad_open20_an_stage3c_w6_legs.py --stage2 $A --out $T/w6_legs.json > $T/o4.txt ) & p1=$!
wait $p0; wait $p1
same $T/w6_legs.json $O/w6_legs.json
# D
( run w2b py $SD/dyad_open20_an_stage3c_w2b_check.py --stage2 $A --out $T/w2b_check.json > $T/o5.txt
  py $SD/dyad_open20_an_stage3c_w6_legs.py --stage2 $A --out $T/w6_control_ZEROJUMP.json --control ZEROJUMP > $T/o9.txt; echo $? > $T/rz.txt ) & p0=$!
( run w2 py $SD/dyad_open20_an_stage3c_w2_check.py --stage2 $A --out $T/w2_check.json > $T/o6.txt
  run w4 py $SD/dyad_open20_an_stage3c_w4_zone1.py --stage2 $A --w3dir $O --out $T/w4_zone1.json > $T/o7.txt
  run w5 py $SD/dyad_open20_an_stage3c_w5_arc.py --out $T/w5_arc.json > $T/o8.txt ) & p1=$!
wait $p0; wait $p1
same $T/w2b_check.json $O/w2b_check.json; same $T/w2_check.json $O/w2_check.json
same $T/w4_zone1.json $O/w4_zone1.json; same $T/w5_arc.json $O/w5_arc.json
same $T/w6_control_ZEROJUMP.json $O/w6_control_ZEROJUMP.json; rZ=$(cat $T/rz.txt)
py $SD/dyad_open20_an_stage3c_w4_zone1.py --stage2 $A --w3dir $O --out $O/w8_control_BRANCH.json --control BRANCH > $O/w8_control_BRANCH.stdout.txt; rC=$?
# control of the acceptance rule: a replay of W5 that writes the committed file and exits 1
grep -v '^w5 ' $RC > $T/rc_fake.txt
sh -c "cp $O/w5_arc.json $T/fake_w5_arc.json; exit 1"; echo "w5 $?" >> $T/rc_fake.txt
cmp -s $T/fake_w5_arc.json $O/w5_arc.json && fake_same=yes || fake_same=no
if verdict $T/rc_fake.txt $R; then hc="NOT rejected"; else hc="rejected"; fi
echo "exit codes: $(tr '\n' ' ' < $RC)" >> $R
echo "control ZEROJUMP (replay) exit code: $rZ (expected 1)" >> $R
echo "control BRANCH exit code: $rC (expected 1)" >> $R
echo "rule control: a replay with identical output ($fake_same) and exit code 1 is $hc (expected: rejected)" >> $R
cat $R
verdict $RC $R && [ "$rC" -eq 1 ] && [ "$rZ" = 1 ] && [ "$hc" = rejected ] && [ "$fake_same" = yes ] || { echo "UNEXPECTED (work files kept in $T)"; exit 1; }
(cd $O && sha256sum w8_branch.json w8_branch.stdout.txt w8_legs.json w8_legs.stdout.txt w8_control_BRANCH.json w8_control_BRANCH.stdout.txt \
   w8_replay.txt run_w8.sh > SHA256SUMS_W8.txt)
rm -rf $T
echo "ALL AS EXPECTED"
