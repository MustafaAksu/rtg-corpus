#!/usr/bin/env python3
"""AZ receiver check for pipes/AZ/20261116-TDRG-v2-13-adopted.md: are the TDR-G statements AZ cites unchanged
between tdrg-v2.12.15 (AZ v0.10 IMP-B pin) and tdrg-v2.13?

    python3 -I evidence/az/owner_sync/tdrg_v2_13_check.py

Reads both tagged editions with git show and asserts their SHA-256. For every identifier in the AZ v0.9 owner-sync list
(evidence/az/v0.9/owner_sync_check.py: IMP-B rows, TDRG-DEF-ORIENT, the three §6.13 identifiers) it compares the defining
block (the paragraph carrying the RID tag). A changed block is accepted as editorial only if it becomes identical after
removing edition-history markers: "(v2.12) ", " *(v2.12.14 `[COR]`)*", "*(v2.12.14 `[COR]`; ...)* ", "(v2.12.14) ",
"v2.12.14 `[COR]`: ", " *(v2.12.15 `[COR]`)*" (Methodology v1.4: DSNs hold current state only).
Exit 0 iff every block is identical or identical modulo those markers. Reads statements; runs no owner artifact.
"""
import hashlib, os, re, subprocess, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
DSN = "dsn/RTG_DISCRETE_GENESIS_DSN.md"
ED = (("tdrg-v2.12.15", "1e35be54a37bb227cd75e34fc1cd6732ae95782bdc147a76e736f16760c92e64"),
      ("tdrg-v2.13", "98b4cba5ecb30f23f9dd97be27a7896191aa514ddefc402fd129ea673f0357f6"))
RIDS = ["TDRG-DEF-ZN-STATE", "TDRG-DEF-PHYSICAL-STATE", "TDRG-DEF-BAND", "TDRG-ALG-LEM-REACH", "TDRG-THM-REACHABILITY-K0",
        "TDRG-ALG-LEM-RETRIG", "TDRG-ALG-LEM-SPECCONS", "TDRG-ALG-BIND3-CYCLE-N24K1", "TDRG-NUM-BIND3-PARITY",
        "TDRG-NUM-BIND3-SPECTRAL-GATE", "TDRG-NUM-BIND3-MEMORY-PARITY", "TDRG-NUM-BIND3-XFER", "TDRG-NUM-BIND3-REGEN",
        "TDRG-OPEN-BIND3-NKSCAN", "TDRG-OPEN-NSCALING", "TDRG-OPEN-CRYSTALLIZATION", "TDRG-OPEN-LOCKING-FAIL",
        "TDRG-OPEN-TOPO-FILTER", "TDRG-OPEN-CHI-SCALING", "TDRG-OPEN-THERMO-SUPPRESS", "TDRG-DEF-ORIENT",
        "TDRG-ALG-EVENT-INVENTORY", "TDRG-ALG-TOKEN-CENSUS-LAW", "TDRG-ALG-PARENT-CHILD-PHASE"]
MARKERS = [r"\(v2\.12\) ", r" \*\(v2\.12\.14 `\[COR\]`\)\*", r"\*\(v2\.12\.14 `\[COR\]`;.*?\.\)\* ",
           r"\(v2\.12\.14\) ", r"v2\.12\.14 `\[COR\]`: ", r" \*\(v2\.12\.15 `\[COR\]`\)\*"]


def load(tag, want):
    raw = subprocess.run(["git", "-C", ROOT, "show", "%s:%s" % (tag, DSN)], capture_output=True, check=True).stdout
    if hashlib.sha256(raw).hexdigest() != want:
        sys.exit("STOP: %s does not have the recorded SHA-256" % tag)
    return raw.decode("utf-8")


def block(text, rid):
    b = [x for x in text.split("\n\n") if "RID: %s]" % rid in x]
    return b[0] if len(b) == 1 else None


def strip(s):
    for m in MARKERS:
        s = re.sub(m, "", s)
    return s


old, new = load(*ED[0]), load(*ED[1])
print("compared: %s (%s...) and %s (%s...)" % (ED[0][0], ED[0][1][:8], ED[1][0], ED[1][1][:8]))
ok, n_id, n_ed = True, 0, 0
for rid in RIDS:
    a, b = block(old, rid), block(new, rid)
    if a is None or b is None:
        verdict, ok = "NOT FOUND as a single defining block", False
    elif a == b:
        verdict, n_id = "identical", n_id + 1
    elif strip(a) == strip(b):
        verdict, n_ed = "identical after removing edition-history markers", n_ed + 1
    else:
        verdict, ok = "CHANGED in substance", False
    print("%-32s %s" % (rid, verdict))
print("identifiers: %d; identical: %d; history markers only: %d" % (len(RIDS), n_id, n_ed))
print("RESULT:", "CITED STATEMENTS UNCHANGED" if ok else "SUBSTANTIVE CHANGE - AZ IMP-B REVIEW NEEDED")
sys.exit(0 if ok else 1)
