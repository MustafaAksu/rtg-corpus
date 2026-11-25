#!/usr/bin/env bash
# OFN v0.13 DRAFT candidate review (Claude co-owner, 25 Nov 2026) — native replay and locator checks. SESSION evidence.
# usage: bash evidence/ofn/scripts/ofn_v0_13_review_claude.sh CANDIDATE_REF   (from the repository root; e.g. origin/chatgpt/ofn-v0.13-stage1)
set -euo pipefail
ref="$1"; tmp=$(mktemp -d); trap 'rm -rf "$tmp"' EXIT
echo "candidate ref: $ref = $(git rev-parse "$ref")"; node --version; python3 --version
for f in dsn/RTG_ONTOLOGICAL_FOUNDATIONS.md evidence/ofn/scripts/build_ofn_v0_13.js evidence/ofn/scripts/check_ofn_v0_13.js \
         evidence/ofn/v0.13/edit_map.json evidence/ofn/v0.13/edit_log.json evidence/ofn/v0.13/source_verification.json \
         evidence/ofn/v0.13/check_output.txt evidence/ofn/v0.13/negative_controls_output.txt; do
  mkdir -p "$tmp/c/$(dirname "$f")"; git show "$ref:$f" > "$tmp/c/$f"; done
git show ofn-v0.12:dsn/RTG_ONTOLOGICAL_FOUNDATIONS.md > "$tmp/base.md"
( cd "$tmp/c" && sha256sum dsn/RTG_ONTOLOGICAL_FOUNDATIONS.md evidence/ofn/scripts/*.js evidence/ofn/v0.13/* ); sha256sum "$tmp/base.md" | cut -c1-64
echo "R1 native build"
node "$tmp/c/evidence/ofn/scripts/build_ofn_v0_13.js" "$tmp/base.md" "$tmp/c/evidence/ofn/v0.13/edit_map.json" "$tmp/out.md" "$tmp/log.json"
cmp "$tmp/out.md" "$tmp/c/dsn/RTG_ONTOLOGICAL_FOUNDATIONS.md" && echo "  candidate byte-identical"
cmp "$tmp/log.json" "$tmp/c/evidence/ofn/v0.13/edit_log.json" && echo "  edit log byte-identical"
echo "  native sha256 of rebuilt candidate: $(sha256sum "$tmp/out.md" | cut -c1-64)"
echo "R2 native checker (Node crypto SHA-256)"
A=("$tmp/base.md" "$tmp/c/evidence/ofn/v0.13/edit_map.json" "$tmp/c/evidence/ofn/v0.13/edit_log.json" "$tmp/c/dsn/RTG_ONTOLOGICAL_FOUNDATIONS.md" "$tmp/c/evidence/ofn/v0.13/source_verification.json")
node "$tmp/c/evidence/ofn/scripts/check_ofn_v0_13.js" "${A[@]}" > "$tmp/chk.txt"; cmp "$tmp/chk.txt" "$tmp/c/evidence/ofn/v0.13/check_output.txt" && echo "  check output byte-identical ($(tail -1 "$tmp/chk.txt"))"
node "$tmp/c/evidence/ofn/scripts/check_ofn_v0_13.js" "${A[@]}" --controls | tail -n +13 > "$tmp/nc.txt"; cmp "$tmp/nc.txt" "$tmp/c/evidence/ofn/v0.13/negative_controls_output.txt" && echo "  negative-control output byte-identical ($(wc -l < "$tmp/nc.txt") lines)"
echo "R3 informational DSN lint (--prev ofn-v0.12)"; python3 -I tools/dsn_lint.py "$tmp/c/dsn/RTG_ONTOLOGICAL_FOUNDATIONS.md" --prev "$tmp/base.md" | sed -n '/^previous/,$p'
echo "R4 pipes index"; python3 -I tools/pipes_index.py --check
echo "R5 import and section-anchor locators re-resolved from tags (independent of source_verification.json)"
python3 -I evidence/ofn/scripts/ofn_v0_13_locators_claude.py "$tmp/c/dsn/RTG_ONTOLOGICAL_FOUNDATIONS.md"
