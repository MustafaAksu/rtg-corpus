#!/usr/bin/env python3
"""DZT v0.18: status-lines-only publication transform (CONVENTIONS.md §4 step 5).

    python3 -I evidence/dzt/v0.18/publish_dzt_v0_18.py            # write the published file
    python3 -I evidence/dzt/v0.18/publish_dzt_v0_18.py --check    # verify the file in dsn/ against the candidate

The candidate adopted by the PI is read from the stage-2 commit (git show) and its SHA-256 is
asserted. Exactly three lines change: the header field "Document status", the heading of the
v0.18 entry in Appendix A, and the footer line. Nothing else may differ; --check re-derives the
published bytes and compares.
"""
import hashlib, os, subprocess, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
DSN = "dsn/RTG_DYADIC_ARITHMETIC_RESONANCE_TRANSFORM_DSN.md"
CAND_REF = "523282a0a55979507a47962d89bbdb7a321d6f58:" + DSN
CAND_SHA = "086bb348e46f3ae4eca94bfac05d35a0efd57ff4d59866cc2ce64d3d369e67d2"
PAIRS = [
    ("**Document status:** DRAFT — stage-2 candidate of v0.18; not adopted. `dzt-v0.8` governs until the PI adopts and tags this edition.",
     "**Document status:** ADOPTED — PI, 19 November 2026 (corrections and synchronization after the reactivation triage, "
     "list (i); Methodology v1.4 layout; no new claim, no grade raised). Adoption record: "
     "`records/dzt/DZT_v0_18_RELEASE_RECORD.md`."),
    ("### v0.18 — 18 November 2026 — DRAFT (stage-2 candidate)",
     "### v0.18 — 18 November 2026 — adopted 19 November 2026"),
    ("*END OF DOCUMENT — RTG_DYADIC_ARITHMETIC_RESONANCE_TRANSFORM_DSN_v0.18 — DRAFT, stage-2 candidate; adoption pending; "
     "`dzt-v0.8` governs until adoption and tag.*",
     "*END OF DOCUMENT — RTG_DYADIC_ARITHMETIC_RESONANCE_TRANSFORM_DSN_v0.18*"),
]
sha = lambda b: hashlib.sha256(b).hexdigest()
cand = subprocess.run(["git", "-C", ROOT, "show", CAND_REF], capture_output=True, check=True).stdout
if sha(cand) != CAND_SHA:
    sys.exit("candidate read from %s does not have the adopted candidate's hash" % CAND_REF)
lines = cand.decode("utf-8").split("\n")
for old, new in PAIRS:
    hits = [i for i, l in enumerate(lines) if l.rstrip(" ") == old]
    if len(hits) != 1:
        sys.exit("status line occurs %d times: %r" % (len(hits), old[:60]))
    tail = lines[hits[0]][len(old):]          # keep a Markdown line break ("  ") if present
    lines[hits[0]] = new + tail
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
