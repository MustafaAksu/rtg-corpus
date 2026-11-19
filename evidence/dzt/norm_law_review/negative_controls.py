#!/usr/bin/env python3
"""Negative controls for dzt_norm_law_review_check.py: each mutation of a checked law must FAIL.

    python3 -I evidence/dzt/norm_law_review/negative_controls.py

Each control writes a mutated copy of the check to a temporary directory, runs it on the short range
(200 100 2000) from the repository root, and expects exit 1 with the named check in FAILURES.
"""
import os, subprocess, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = open(os.path.join(HERE, "dzt_norm_law_review_check.py"), encoding="utf-8").read()
CASES = [
    ("anomaly gate 3 mod 4 instead of 1 mod 4", "q % 4 == 1 else None", "q % 4 == 3 else None", "'A7"),
    ("denominator without [p=2^k]", "dp = ph // 4 + is_2k(p) + is_3_2k(p)", "dp = ph // 4 + is_3_2k(p)", "'A8"),
    ("N(L+1) = 1 for all 4|p (the odd-support note, line 173)", "check(RB == int(P(-1)) == B,", "check(RB == int(P(-1)) == 1,", "'A4"),
    ("I-1 taken as a unit (v0.17 line 250)", "check(RI == 2 ** (ph // 2),", "check(RI == 1,", "'A2"),
    ("sign from c1 alone", "return -1 if (c1 + c2) % 2 else 1\n\n\nsigns", "return -1 if c1 % 2 else 1\n\n\nsigns", "'B sign"),
    ("pattern with l = 3, 7 mod 8", "pp[0] % 8 in (3, 5)", "pp[0] % 8 in (3, 7)", "'C pattern"),
]
ok = True
with tempfile.TemporaryDirectory() as d:
    for name, old, new, needle in CASES:
        if SRC.count(old) != 1:
            print("BAD  %-58s anchor not unique" % name); ok = False; continue
        path = os.path.join(d, "c.py")
        open(path, "w", encoding="utf-8").write(SRC.replace(old, new))
        r = subprocess.run([sys.executable, "-I", path, "200", "100", "2000"], cwd=ROOT, capture_output=True, text=True)
        line = next((l for l in r.stdout.splitlines() if l.startswith("FAILURES")), "")
        good = r.returncode == 1 and needle in line
        ok &= good
        print("%s %-58s exit %d  %s" % ("OK  " if good else "BAD ", name, r.returncode, line[:90]))
r = subprocess.run([sys.executable, "-I", os.path.join(HERE, "dzt_norm_law_review_check.py"), "200", "100", "2000"],
                   cwd=ROOT, capture_output=True, text=True)
good = r.returncode == 0
ok &= good
print("%s %-58s exit %d" % ("OK  " if good else "BAD ", "unmutated check", r.returncode))
print("RESULT:", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
