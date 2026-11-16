#!/usr/bin/env python3
"""AZ v0.10: status-lines-only publication transform (CONVENTIONS.md §4 step 5).

    python3 -I evidence/az/v0.10/publish_az_v0_10.py            # write the published file
    python3 -I evidence/az/v0.10/publish_az_v0_10.py --check    # verify the file in dsn/ against the candidate

The candidate adopted by the PI is read from the reviewed commit (git show) and its SHA-256 is
asserted. Exactly two lines change: the header field "Document status" and the footer line
(the Date is already the day of adoption). Nothing else may differ; --check re-derives the published bytes and compares.
"""
import hashlib, os, subprocess, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
DSN = "dsn/RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN.md"
CAND_REF = "e5668cc0dede1a318f261257b48ef83277bcaa65:" + DSN
CAND_SHA = "b672fd03cfe73e4cd674721bca24a3da4b76c0fe09cf52727d92ed932a178217"
PAIRS = [
    ("**Document status:** DRAFT — candidate of v0.10; not adopted. `az-v0.9` governs until the PI adopts and tags this edition.  ",
     "**Document status:** ADOPTED — PI, 16 November 2026 (the Action 1 Stage 2 result as a separate AZ-owned `[NUM diagnostic]`, "
     "`AZ-NUM-TOKRES-S2`). Adoption record: `records/az/AZ_v0_10_RELEASE_RECORD.md`.  "),
    ("*END OF DOCUMENT — RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN_v0.10 — DRAFT candidate; adoption pending; `az-v0.9` governs until adoption and tag.*",
     "*END OF DOCUMENT — RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN_v0.10*"),
]
sha = lambda b: hashlib.sha256(b).hexdigest()
cand = subprocess.run(["git", "-C", ROOT, "show", CAND_REF], capture_output=True, check=True).stdout
if sha(cand) != CAND_SHA:
    sys.exit("candidate read from %s does not have the adopted candidate's hash" % CAND_REF)
lines = cand.decode("utf-8").split("\n")
for old, new in PAIRS:
    hits = [i for i, l in enumerate(lines) if l == old]
    if len(hits) != 1:
        sys.exit("status line occurs %d times: %r" % (len(hits), old[:60]))
    lines[hits[0]] = new
pub = "\n".join(lines).encode("utf-8")
path = os.path.join(ROOT, DSN)
if "--check" in sys.argv:
    cur = open(path, "rb").read()
    a, b = cand.decode("utf-8").split("\n"), cur.decode("utf-8").split("\n")
    diff = [i + 1 for i, (x, y) in enumerate(zip(a, b)) if x != y]
    ok = cur == pub and len(a) == len(b) and len(diff) == len(PAIRS)
    print("candidate %s  (git show %s)" % (CAND_SHA, CAND_REF))
    print("published %s  %d bytes" % (sha(cur), len(cur)))
    print("lines that differ from the candidate: %s (of %d)" % (diff, len(a)))
    print("RESULT:", "PASS" if ok else "FAIL")
    sys.exit(0 if ok else 1)
open(path, "wb").write(pub)
print("candidate %s" % CAND_SHA)
print("published %s  %d bytes" % (sha(pub), len(pub)))
