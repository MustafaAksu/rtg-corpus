#!/usr/bin/env python3
"""TDR-G v2.13 publication transform: one header line, applied to the adopted candidate bytes.

    python3 -I evidence/tdrg/v2.13/publish_tdrg_v2_13.py [--check]

The PI adopted the candidate 6a4b94d5…de88 (16 Nov 2026, 18:20 +03:00). The transform replaces only the
*Document status* line of the header (DRAFT → ADOPTED, with the release record) and nothing else.
Without --check: reads dsn/RTG_DISCRETE_GENESIS_DSN.md, asserts the adopted candidate hash, writes the
published bytes. With --check: reads the published file, undoes the one line, and asserts that the result is
the adopted candidate byte for byte and that exactly one line differs.
"""
import hashlib, sys

DSN = "dsn/RTG_DISCRETE_GENESIS_DSN.md"
ADOPTED = "6a4b94d5ec6946cad177889d453044a69eb4aa451763a2e81148b2e11739de88"
OLD = ("**Document status:** DRAFT — stage-2 candidate of v2.13; not adopted. `tdrg-v2.12.15` governs until the PI "
       "adopts and tags this edition.")
NEW = ("**Document status:** ADOPTED by the PI on 16 November 2026; release record "
       "`records/tdrg/TDRG_v2_13_RELEASE_RECORD.md`; tag `tdrg-v2.13`.")
sha = lambda b: hashlib.sha256(b).hexdigest()
t = open(DSN, "rb").read()
if "--check" in sys.argv:
    s = t.decode("utf-8")
    assert s.count(NEW) == 1 and s.count(OLD) == 0, "published status line"
    back = s.replace(NEW, OLD).encode("utf-8")
    assert sha(back) == ADOPTED, "undoing the transform does not give the adopted bytes"
    diff = [i for i, (a, b) in enumerate(zip(t.split(b"\n"), back.split(b"\n"))) if a != b]
    assert len(diff) == 1 and t.count(b"\n") == back.count(b"\n"), diff
    print("published", sha(t), "= adopted", ADOPTED[:16], "with one line changed (line %d)" % (diff[0] + 1))
else:
    assert sha(t) == ADOPTED, "the file is not the adopted candidate: %s" % sha(t)
    s = t.decode("utf-8")
    assert s.count(OLD) == 1, "status line"
    out = s.replace(OLD, NEW).encode("utf-8")
    open(DSN, "wb").write(out)
    print("published", sha(out), len(out), "bytes")
