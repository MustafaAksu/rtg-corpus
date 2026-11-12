#!/usr/bin/env python3
"""AZ v0.8: status-lines-only publication transform (CONVENTIONS.md §4 step 5).

    python3 -I evidence/az/v0.8/publish_az_v0_8.py            # write the published file
    python3 -I evidence/az/v0.8/publish_az_v0_8.py --check    # verify the file in dsn/ against the candidate

The candidate adopted by the PI is read from the reviewed commit (git show) and its SHA-256 is
asserted. Exactly two lines change: the header field "Document status" and the footer line.
Nothing else may differ; --check re-derives the published bytes and compares.
"""
import hashlib, os, subprocess, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
DSN = "dsn/RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN.md"
CAND_REF = "906eec7ea66c40059eb4821810544fdaa9f75e14:" + DSN
CAND_SHA = "f15ee1d7601b43a7219f245990fa6e8f7c61bd0dd6e221e3267d683cb129a50d"
PAIRS = [
    ("**Document status:** DRAFT — stage-2 candidate of v0.8; not adopted. `az-v0.7` governs until the PI adopts and tags this edition.  ",
     "**Document status:** ADOPTED — PI, 12 November 2026 (Methodology v1.4 migration with a declared section map; Programme §6.7 "
     "reduction; availability corrections; PROP-AZ-CORE-EQUIV `[THM]` on a written proof). Adoption record: "
     "`records/az/AZ_v0_8_RELEASE_RECORD.md`.  "),
    ("*END OF DOCUMENT — RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN_v0.8 — DRAFT, stage-2 candidate; adoption pending; `az-v0.7` governs until adoption and tag.*",
     "*END OF DOCUMENT — RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN_v0.8*"),
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
    ok = cur == pub and len(a) == len(b) and len(diff) == 2
    print("candidate %s  (git show %s)" % (CAND_SHA, CAND_REF))
    print("published %s  %d bytes" % (sha(cur), len(cur)))
    print("lines that differ from the candidate: %s (of %d)" % (diff, len(a)))
    print("RESULT:", "PASS" if ok else "FAIL")
    sys.exit(0 if ok else 1)
open(path, "wb").write(pub)
print("candidate %s" % CAND_SHA)
print("published %s  %d bytes" % (sha(pub), len(pub)))
