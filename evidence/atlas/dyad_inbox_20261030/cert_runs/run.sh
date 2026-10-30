#!/usr/bin/env bash
# Atlas rerun of the uploaded rtg-engine certificates (30 Oct 2026). Sources are read from upload/, never changed.
# Toolchain used: g++ 13.3.0, FLINT 3.0.1 (Ubuntu libflint-dev). Run from the repository root.
set -u
SRC=upload/dyad-sources/rtg-engine; OUT=evidence/atlas/dyad_inbox_20261030/cert_runs; B=$(mktemp -d)
cp $SRC/*.cpp $SRC/*.hpp "$B"/
for b in open18_arb_cert3 open18_arb_cert2 open18_arb_cert certify_transition_strip2 certify_q_max certify_g_monotonic certify_s_max certify_branch_4_10; do
  g++ -O2 -std=c++17 -o "$B/$b" "$B/$b.cpp" -lflint
  timeout 300 "$B/$b" > "$OUT/$b.out.txt" 2>&1; echo "$b exit $?"
done
