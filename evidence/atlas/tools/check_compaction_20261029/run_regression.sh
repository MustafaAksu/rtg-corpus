#!/bin/bash
# run the regression set from a tree root ($1) into an output dir ($2)
R=$1; O=$2; I=/tmp/claude-0/-home-claude/d325df82-74eb-5155-8331-fb30c4d86d36/scratchpad/reg/in; mkdir -p $O; cd $R
python3 -I tools/test_check_compaction.py $I/dyad_base.md $I/dyad_cand.md evidence/dyad/v6.4.21/movement_map.json --regions evidence/dyad/v6.4.21/reviewed_regions.json > $O/dyad.txt 2>&1; echo "dyad exit $?" >> $O/exits
python3 -I evidence/recog/scripts/test_check_compaction_recog.py $I/r23_base.md $I/r23_cand.md evidence/recog/v0.3.23/movement_map.json > $O/r23.txt 2>&1; echo "r23 exit $?" >> $O/exits
python3 -I evidence/recog/scripts/test_check_compaction_move.py $I/r24_base.md $I/r24_cand.md evidence/recog/v0.3.24/movement_map.json > $O/r24.txt 2>&1; echo "r24 exit $?" >> $O/exits
python3 -I tools/check_compaction.py $I/gen_base.md $I/gen_cand.md evidence/gen/v2.9/movement_map.json > $O/gen_tool.txt 2>&1; echo "gen_tool exit $?" >> $O/exits
python3 -I evidence/gen/scripts/check_gen_v2_9_stage2.py $I/gen_base.md $I/gen_cand.md evidence/gen/v2.9/movement_map.json --fixtures > $O/gen_guard.txt 2>&1; echo "gen_guard exit $?" >> $O/exits
python3 -I tools/check_compaction.py $I/ng_base.md $I/ng_cand.md evidence/numgen/v1.21/movement_map.json > $O/ng_tool.txt 2>&1; echo "ng_tool exit $?" >> $O/exits
python3 -I evidence/numgen/scripts/check_numgen_v1_21_stage2.py $I/ng_base.md $I/ng_cand.md evidence/numgen/v1.21/movement_map.json --fixtures > $O/ng_guard.txt 2>&1; echo "ng_guard exit $?" >> $O/exits
python3 -I evidence/programme/scripts/test_check_compaction_programme.py $I/prog_base.md $I/prog_cand.md evidence/programme/v1.3/movement_map.json > $O/prog.txt 2>&1; echo "prog exit $?" >> $O/exits
