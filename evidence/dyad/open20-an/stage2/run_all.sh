#!/usr/bin/env bash
# Stage-2 [NUM] scouting runs (OPEN 20 analytic branch, sectorial pilot). Run from this directory.
# Owner run 23/24 October 2026 (Linux, Python 3.13, python-flint 0.9.0). Timings of the owner run: 4.6 s, 5.3 s, 66 s, 82 s, 0.3 s, 322 s.
set -u
S=../../scripts/dyad_open20_an_stage2_scout.py
cp ../stage1_prep.json .          # input: stage-1 exact data (SHA-256 2c9ae6376e0c482f2ba520a7ea8e2b38606a6821f7ac3bfa259d4d6020d04739)
run(){ name=$1; shift; python3 -I -B $S "$@" --stage1 stage1_prep.json --out $name.json > $name.stdout.txt 2>&1; echo "$name exit=$?"; }
run scout_N72_dps330 --N 72 --dps 330
run scout_N72_dps400 --N 72 --dps 400
run scout_N144_dps600 --N 144 --dps 600
run scout_N144_dps700 --N 144 --dps 700
run control_N36_dps60 --N 36 --dps 60          # negative control: expected exit 1 (C3 fails)
run scout_N216_dps840 --N 216 --dps 840
rm -f stage1_prep.json
# exact cross-check of a_5..a_8 (co-owner review check 1): stage-1 field tower, jets to degree 11; control W evaluates at the other root (expected exit 1)
python3 -I -B ../../scripts/dyad_open20_an_stage2_exact_crosscheck.py --scout scout_N216_dps840.json --out exact_crosscheck.json > exact_crosscheck.stdout.txt; echo "exact_crosscheck exit=$?"
python3 -I -B ../../scripts/dyad_open20_an_stage2_exact_crosscheck.py --scout scout_N216_dps840.json --out exact_crosscheck_control_W.json --control W > exact_crosscheck_control_W.stdout.txt; echo "exact_crosscheck control W exit=$?"
python3 -I -B ../../scripts/dyad_open20_an_stage2_summary.py . > summary_output.txt 2>&1; echo "summary exit=$?"
sha256sum control_N36_dps60.json control_N36_dps60.stdout.txt scout_N*.json scout_N*.stdout.txt exact_crosscheck*.json exact_crosscheck*.stdout.txt summary_output.txt run_all.sh > SHA256SUMS.txt
