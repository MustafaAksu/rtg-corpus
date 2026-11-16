# AZ Action 1 — Stage 2: design decision, compute authorisation and start of the campaign

**[SESSION] NONCANONICAL.** A distinct record, as review `5906866246` asks: the registered bytes of the preregistration stay as they were at the authorised commit, and what happened after is written here. Prepared by the AZ co-owner (Claude), 14 November 2026. It reports no Stage 2 result; none exists.

## 1. PI decisions

| Decision | Words and source | Evidence state |
|---|---|---|
| Design: **A3 + B1 + C1** (pilot intake §7; preregistration §3, §6) | "A3 + B1 + C1'i benimsiyorum" — given by the PI in the second co-owner's (ChatGPT) conversation on 14 Nov 2026, quoted in that co-owner's review `5906866246` on PR #264 (GitHub, 14 Nov 2026, 20:08:56Z) | recorded on GitHub by the second co-owner; **source-reported to this lane** (the words were not given in this session). The PI relayed the second co-owner's report of them to this session on 14 Nov 2026, 23:16 +03:00, together with the terminal output of §4 |
| Compute: the confirmatory campaign `AZ-TOKRES-S2`, **only** for commit `74ad6946e9710a2272b9d7792d6d8f0c45cda168` with `evidence/az/token_resonance/stage2/SHA256SUMS` of SHA-256 `25b796b3890a0e49c8f99f91a8866758b826c87a40dc5918b35928b5fb35eb4b` | "Hesaplama yetkisi veriyorum" — same source, same review receipt | as above; in addition the PI started the run himself (§4) |

They are a design choice and a compute authorisation. They are not an adoption of any Stage 2 result, and they are not the adoption of AZ v0.9 (a separate decision of the same evening, recorded in `records/az/AZ_v0_9_RELEASE_RECORD.md` §8).

## 2. Review and custody state at the start

- Preregistration r2 at `74ad694`: review `5890473916` (accept scoped, two narrow corrections), readback `5906866246` (pass; scripts, registered constants, test outputs and `SHA256SUMS` unchanged since `9e11fbb`).
- Merged by merge commits on 14 Nov 2026, 20:09Z, verified on GitHub by this lane: PR #251 `cdecc857` (pilot plan and script), PR #259 `e47ba31b` (pilot output, unchanged), PR #260 `e4a48e0f` (intake), PR #264 `41cef97a` (preregistration r2 and package; second parent `74ad694`). `main` = `41cef97` when this record was written.
- Package on `main`: `sha256sum -c evidence/az/token_resonance/stage2/SHA256SUMS` passes; the file's SHA-256 is the authorised one (checked in this session on a checkout of `41cef97`).

## 3. The server block that was run

Issued by the second co-owner in its conversation and run by the PI on the Ubuntu server; text as relayed by the PI. It follows the form of preregistration §8 with three differences, none of which changes a registered parameter: the pilot directory is always extracted from `origin/main` with `git archive` (after PR #259 the pilot output is on `main`; the driver checks its hashes against the registered values before any run); the resume flag is passed through an array; the copy into the upload directory uses `cp -a`.

```bash
cat > "$HOME/az_tokres_stage2.sh" <<'AZ_STAGE2'
#!/usr/bin/env bash
set -euo pipefail

REPO="$HOME/rtg-corpus"
WT="$HOME/az_tokres_s2_wt"
OUT="$HOME/az_tokres_stage2"
PILOT="$HOME/az_tokres_s2_pilot_from_git"

COMMIT="74ad6946e9710a2272b9d7792d6d8f0c45cda168"
SUMS="25b796b3890a0e49c8f99f91a8866758b826c87a40dc5918b35928b5fb35eb4b"

git -C "$REPO" fetch -q origin

if [ ! -d "$WT" ]; then
    git -C "$REPO" worktree add -q --detach "$WT" "$COMMIT"
fi

cd "$WT"
git checkout -q --detach "$COMMIT"
test "$(git rev-parse HEAD)" = "$COMMIT"
test -z "$(git status --porcelain)"

test "$(sha256sum evidence/az/token_resonance/stage2/SHA256SUMS | cut -d' ' -f1)" = "$SUMS"
sha256sum -c --quiet evidence/az/token_resonance/stage2/SHA256SUMS
echo "REGISTERED PACKAGE: PASS"

mkdir -p "$PILOT"
git archive origin/main upload/az-token-resonance-s2-pilot \
    | tar -x -C "$PILOT" --strip-components=2

ARGS=()
if [ "${AZ_RESUME:-0}" = 1 ]; then
    ARGS+=(--resume)
fi

python3 -I evidence/az/scripts/az_tokres_s2_campaign.py \
    --plan stage2 \
    --jobs 1 \
    --out "$OUT" \
    --pilot-dir "$PILOT" \
    --confirmatory \
    "${ARGS[@]}"

test -f "$OUT/CAMPAIGN_COMPLETE.json"
(cd "$OUT" && sha256sum -c --quiet HASHES.txt)
echo "CAMPAIGN HASHES: PASS"

git checkout -q -b upload/az-token-resonance-stage2 origin/main
mkdir -p upload/az-token-resonance-stage2
cp -a "$OUT/." upload/az-token-resonance-stage2/
git add upload/az-token-resonance-stage2
git commit -q -m "upload: AZ Stage 2 campaign output, unchanged"
git push -q -u origin upload/az-token-resonance-stage2

echo "UPLOADED: upload/az-token-resonance-stage2 at $(git rev-parse --short HEAD)"
AZ_STAGE2

setsid nohup bash "$HOME/az_tokres_stage2.sh" > "$HOME/az_tokres_stage2.out" 2>&1 < /dev/null &
```
Resume after an interruption: `AZ_RESUME=1 setsid nohup bash ~/az_tokres_stage2.sh >> ~/az_tokres_stage2.out 2>&1 < /dev/null &`.

## 4. Start of the campaign

Terminal output relayed by the PI in the project conversation on 14 Nov 2026, 23:16 +03:00 (`tail -n 5 ~/az_tokres_stage2.out`), verbatim:

```
REGISTERED PACKAGE: PASS
Stage 2 analysis self-test: exit code 0
pilot files: hashes and structure as registered
fixtures: exit code 0
```

So, on the campaign machine and before any run: the package had the authorised bytes; the Stage 2 analysis self-test passed; the three pilot files had the registered hashes and structure; the Stage 1 fixtures passed (gate G1's log exists). The cells follow in the order S2-C240, S2-C242, S2-C480, one process. The exact start time is not in the relayed output; it will be in `CAMPAIGN_COMPLETE.json` (`started_utc`). **These lines are source-reported (`EV-SRC-REPORTED`): this lane has not seen the server.**

## 5. Rules while it runs, and what follows

- **No interim look.** The driver analyses once, after the last cell. Record counts may be looked at (`wc -l ~/az_tokres_stage2/*.jsonl`: 9,400 / 7,500 / 9,400 when complete); the record files are not opened by anyone before `CAMPAIGN_COMPLETE.json` exists (preregistration §5). The pilot's exposed draws are first tabulated by that same registered analysis (D5).
- **A directory without `CAMPAIGN_COMPLETE.json` is not a campaign result.** If the driver ends with `CAMPAIGN FAILED`, nothing is uploaded and `CAMPAIGN_FAILED.txt` names the step; the next action is then decided with the PI and recorded, not improvised.
- **After `UPLOADED: upload/az-token-resonance-stage2 at …`:** this lane — custody PR for the upload branch; `HASHES.txt` and marker checks; a rerun of the registered analysis from the uploaded records against the stored output; then a report with the readings exactly as printed, the qualifiers, the descriptive outputs, deviations if any; review by the second co-owner. Under the PI's outcome rule a validated, supported contrast is *eligible* for a PI-approved `[NUM diagnostic]` entry; that entry is a separate PI decision.
- Expected duration from the pilot's run times: about 10 hours if the arms behave as at `N = 120`, about 6 with no effect; a planning figure, not a bound (preregistration §8).
