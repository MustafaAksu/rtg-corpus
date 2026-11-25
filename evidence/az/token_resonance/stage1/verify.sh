#!/usr/bin/env bash
# AZ token resonance, Stage 1 - custody check and rerun of the registered analysis from the uploaded directory.
# [SESSION]. Runs from the repository root; standard-library Python only; about half a minute.
# usage: bash evidence/az/token_resonance/stage1/verify.sh
set -euo pipefail
S=evidence/az/scripts
E=upload/tdrg-records/genesis_mode_b_mc.py
O=evidence/tdrg/scripts/tdrg_orient_v2_12_14.py
D=upload/az-token-resonance-stage1
R=evidence/az/token_resonance/stage1
( cd evidence/az/token_resonance && sha256sum -c --quiet SHA256SUMS )
echo "registered package (scripts, fixtures, pilot): SHA256SUMS OK; SHA-256 of SHA256SUMS = $(sha256sum evidence/az/token_resonance/SHA256SUMS | cut -c1-64)"
( cd "$D" && sha256sum -c --quiet HASHES.txt )
echo "campaign directory: HASHES.txt OK ($(wc -l < "$D/HASHES.txt") files); SHA-256 of HASHES.txt = $(sha256sum "$D/HASHES.txt" | cut -c1-64)"
python3 -I - "$D" "$S" "$E" "$O" <<'PY'
import hashlib, json, os, sys
d, s, e, o = sys.argv[1:5]
sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()
m = json.load(open(os.path.join(d, "CAMPAIGN_COMPLETE.json")))
print("marker: plan %s, confirmatory %s, jobs %d, resumed %s, fixtures_skipped %s, python %s" % (
    m["plan"], m["confirmatory"], m["jobs"], m["resumed"], m["fixtures_skipped"], m["python"]))
print("marker: started %s, finished %s, records %s" % (m["started_utc"], m["finished_utc"], json.dumps(m["records"], sort_keys=True)))
here = {"engine": sha(e), "orient": sha(o), "runner": sha(os.path.join(s, "az_tokres_run.py")),
        "fixtures": sha(os.path.join(s, "az_tokres_fixtures.py")), "analysis": sha(os.path.join(s, "az_tokres_analyse.py")),
        "driver": sha(os.path.join(s, "az_tokres_campaign.py")),
        "golden": sha("evidence/az/token_resonance/fixtures/golden.json"), "HASHES.txt": sha(os.path.join(d, "HASHES.txt"))}
bad = [k for k in here if m["sha256"].get(k) != here[k]]
print("marker: the eight SHA-256 values it records equal the bytes in this repository: %s" % (not bad))
n = sum(1 for f in sorted(os.listdir(d)) if f.endswith(".jsonl") for _ in open(os.path.join(d, f), "rb"))
print("record files: %d records in %d files" % (n, sum(f.endswith(".jsonl") for f in os.listdir(d))))
sys.exit(1 if bad or n != 19900 else 0)
PY
python3 -I "$S/az_tokres_analyse.py" --registered S1-C1 --engine "$E" --orient "$O" --runner "$S/az_tokres_run.py" \
  --fixtures-log "$D/fixtures_output.txt" "$D"/S1-C1_*.jsonl --sensitivity "$D"/S1-C3_*.jsonl > "$R/analysis_S1-C1.rerun.txt"
echo "registered analysis S1-C1 (with sensitivity set S1-C3): exit code 0"
python3 -I "$S/az_tokres_analyse.py" --registered S1-C2 --engine "$E" --orient "$O" --runner "$S/az_tokres_run.py" \
  --fixtures-log "$D/fixtures_output.txt" "$D"/S1-C2_*.jsonl > "$R/analysis_S1-C2.rerun.txt"
echo "registered analysis S1-C2: exit code 0"
cmp "$R/analysis_S1-C1.rerun.txt" "$D/analysis_S1-C1.txt"
cmp "$R/analysis_S1-C2.rerun.txt" "$D/analysis_S1-C2.txt"
echo "rerun outputs are byte-identical to the outputs produced on the campaign machine"
echo "VERIFY PASS"
