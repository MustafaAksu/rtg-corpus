#!/usr/bin/env python3
"""AZ v0.9: comparison of the TDR-G owner statements cited by AZ between tdrg-v2.12.14 and tdrg-v2.12.15.

    python3 -I evidence/az/v0.9/owner_sync_check.py

Reads the two tagged editions with git show, asserts their SHA-256, and for every TDR-G identifier cited in the AZ
import ledger (clauses IMP-B) and in §4.2.1 compares (a) the defining block - the paragraph that carries the RID tag -
and (b) the nearest preceding section heading. It reads statements; it runs no owner artifact (EV-SRC-READ).
Exit code 0 iff the result is the one recorded in AZ v0.9 §8: every block identical except TDRG-ALG-LEM-SPECCONS,
every heading identical, and the three §6.13 identifiers present at tdrg-v2.12.15 only.
"""
import hashlib, os, re, subprocess, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
DSN = "dsn/RTG_DISCRETE_GENESIS_DSN.md"
ED = (("tdrg-v2.12.14", "3be72923cd40523399363e0dc044bba6246862d12b2bca190c74969e2cce2392"),
      ("tdrg-v2.12.15", "1e35be54a37bb227cd75e34fc1cd6732ae95782bdc147a76e736f16760c92e64"))
ROWS = ["TDRG-DEF-ZN-STATE", "TDRG-DEF-PHYSICAL-STATE", "TDRG-DEF-BAND", "TDRG-ALG-LEM-REACH", "TDRG-THM-REACHABILITY-K0",
        "TDRG-ALG-LEM-RETRIG", "TDRG-ALG-LEM-SPECCONS", "TDRG-ALG-BIND3-CYCLE-N24K1", "TDRG-NUM-BIND3-PARITY",
        "TDRG-NUM-BIND3-SPECTRAL-GATE", "TDRG-NUM-BIND3-MEMORY-PARITY", "TDRG-NUM-BIND3-XFER", "TDRG-NUM-BIND3-REGEN",
        "TDRG-OPEN-BIND3-NKSCAN", "TDRG-OPEN-NSCALING", "TDRG-OPEN-CRYSTALLIZATION", "TDRG-OPEN-LOCKING-FAIL",
        "TDRG-OPEN-TOPO-FILTER", "TDRG-OPEN-CHI-SCALING", "TDRG-OPEN-THERMO-SUPPRESS"]
ELSEWHERE = ["TDRG-DEF-ORIENT"]                                  # cited in §4.2.1 (scope of AZ-NUM-TOKRES-S1)
NEW = ["TDRG-ALG-EVENT-INVENTORY", "TDRG-ALG-TOKEN-CENSUS-LAW", "TDRG-ALG-PARENT-CHILD-PHASE"]
EXPECT_CHANGED = {"TDRG-ALG-LEM-SPECCONS"}


def load(tag, want):
    raw = subprocess.run(["git", "-C", ROOT, "show", "%s:%s" % (tag, DSN)], capture_output=True, check=True).stdout
    if hashlib.sha256(raw).hexdigest() != want:
        sys.exit("STOP: %s does not have the recorded SHA-256" % tag)
    return raw.decode("utf-8")


def entry(text, rid):
    blocks = [b for b in text.split("\n\n") if "RID: %s]" % rid in b]
    if len(blocks) != 1:
        return None, None
    head = None
    for line in text[:text.index(blocks[0])].split("\n"):
        if re.match(r"#{2,4} ", line):
            head = line.strip()
    return blocks[0], head


old, new = load(*ED[0]), load(*ED[1])
print("compared: %s (%s...) and %s (%s...)" % (ED[0][0], ED[0][1][:8], ED[1][0], ED[1][1][:8]))
ok = True
changed = set()
for rid in ROWS + ELSEWHERE:
    (b0, h0), (b1, h1) = entry(old, rid), entry(new, rid)
    if b0 is None or b1 is None:
        print("%-32s NOT FOUND as a single defining block" % rid)
        ok = False
        continue
    same_b, same_h = b0 == b1, h0 == h1
    if not same_b:
        changed.add(rid)
    ok &= same_h
    print("%-32s block %-9s heading %-9s %s" % (rid, "identical" if same_b else "CHANGED", "identical" if same_h else "CHANGED", h1))
for rid in NEW:
    (b0, _), (b1, h1) = entry(old, rid), entry(new, rid)
    good = b0 is None and b1 is not None
    ok &= good
    print("%-32s %s %s" % (rid, "new at tdrg-v2.12.15" if good else "UNEXPECTED", h1 or ""))
ok &= changed == EXPECT_CHANGED
print("identifiers cited in the IMP-B rows: %d; defining block identical: %d; changed: %s" % (
    len(ROWS), len(ROWS) - len(changed & set(ROWS)), sorted(changed)))
print("RESULT:", "AS RECORDED" if ok else "DIFFERS FROM THE RECORD")
sys.exit(0 if ok else 1)
