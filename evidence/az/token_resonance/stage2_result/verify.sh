#!/usr/bin/env bash
# AZ token resonance, Stage 2 - custody check and rerun of the registered analysis from the uploaded directory.
# [SESSION]. Runs from the repository root after the upload (PR from upload/az-token-resonance-stage2) is on the branch;
# standard-library Python only; a few seconds.
# usage: bash evidence/az/token_resonance/stage2_result/verify.sh
set -euo pipefail
S=evidence/az/scripts
E=upload/tdrg-records/genesis_mode_b_mc.py
O=evidence/tdrg/scripts/tdrg_orient_v2_12_14.py
D=upload/az-token-resonance-stage2
P=upload/az-token-resonance-s2-pilot
R=evidence/az/token_resonance/stage2_result
AUTH_SUMS=25b796b3890a0e49c8f99f91a8866758b826c87a40dc5918b35928b5fb35eb4b
test "$(sha256sum evidence/az/token_resonance/stage2/SHA256SUMS | cut -c1-64)" = "$AUTH_SUMS"
sha256sum -c --quiet evidence/az/token_resonance/stage2/SHA256SUMS
echo "registered package: SHA256SUMS OK and equal to the authorised hash $AUTH_SUMS"
( cd "$D" && sha256sum -c --quiet HASHES.txt )
echo "campaign directory: HASHES.txt OK ($(wc -l < "$D/HASHES.txt") files); SHA-256 of HASHES.txt = $(sha256sum "$D/HASHES.txt" | cut -c1-64)"
python3 -I - "$D" "$S" "$E" "$O" <<'PY'
import hashlib, json, os, sys
d, s, e, o = sys.argv[1:5]
sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()
m = json.load(open(os.path.join(d, "CAMPAIGN_COMPLETE.json")))
print("marker: plan %s, confirmatory %s, jobs %d, resumed %s, fixtures_skipped %s, pilot_supplied %s, python %s" % (
    m["plan"], m["confirmatory"], m["jobs"], m["resumed"], m["fixtures_skipped"], m["pilot_supplied"], m["python"]))
print("marker: started %s, finished %s, %.0f s, records %s" % (m["started_utc"], m["finished_utc"], m["seconds"], json.dumps(m["records"], sort_keys=True)))
here = {"engine": sha(e), "orient": sha(o), "runner": sha(os.path.join(s, "az_tokres_run.py")),
        "fixtures": sha(os.path.join(s, "az_tokres_fixtures.py")), "analysis_s1": sha(os.path.join(s, "az_tokres_analyse.py")),
        "analysis_s2": sha(os.path.join(s, "az_tokres_s2_analyse.py")), "driver": sha(os.path.join(s, "az_tokres_s2_campaign.py")),
        "golden": sha("evidence/az/token_resonance/fixtures/golden.json"), "HASHES.txt": sha(os.path.join(d, "HASHES.txt"))}
bad = [k for k in here if m["sha256"].get(k) != here[k]]
print("marker: the nine SHA-256 values it records equal the bytes in this repository: %s" % (not bad))
n = sum(1 for f in sorted(os.listdir(d)) if f.endswith(".jsonl") for _ in open(os.path.join(d, f), "rb"))
print("record files: %d records in %d files" % (n, sum(f.endswith(".jsonl") for f in os.listdir(d))))
ok = (not bad) and n == 26300 and m["plan"] == "stage2" and m["confirmatory"] and m["pilot_supplied"] and not m["fixtures_skipped"]
sys.exit(0 if ok else 1)
PY
python3 -I "$S/az_tokres_s2_analyse.py" --plan stage2 --dir "$D" --engine "$E" --orient "$O" --runner "$S/az_tokres_run.py" \
  --analysis-s1 "$S/az_tokres_analyse.py" --fixtures-log "$D/fixtures_output.txt" --pilot-dir "$P" > "$R/analysis_stage2.rerun.txt"
echo "registered Stage 2 analysis: exit code 0"
cmp "$R/analysis_stage2.rerun.txt" "$D/analysis_stage2.txt"
echo "rerun output is byte-identical to the output produced on the campaign machine"
echo "VERIFY PASS"
