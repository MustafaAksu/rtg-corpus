#!/usr/bin/env python3
"""Re-resolve every live `[import: NAME_vX §… | RIDs]` and every `NAME_vX §… #anchor` locator of an OFN candidate against the
producer tag named by its version (git show). Reports anchors not present and RIDs not declared. SESSION evidence.
usage: python3 -I evidence/ofn/scripts/ofn_v0_13_locators_claude.py CANDIDATE.md   (from the repository root)"""
import re, subprocess, sys
from collections import Counter
C = open(sys.argv[1], encoding="utf-8").read(); live = C.split("## Appendix A —")[0]
F = {"RTG_DISCRETE_GENESIS_DSN": "tdrg", "RTG_DYADIC_OSCILLATOR_DSN": "dyad", "RTG_GENESIS_GEOMETRY_DSN": "gen",
     "RTG_RELATIONAL_RECOGNITION_DSN": "recog", "RTG_NUMBER_GENESIS_DSN": "numgen", "RTG_TRIADIC_BIRTH_LIFT_DSN": "triad",
     "RTG_PROGRAMME_OVERVIEW": "programme", "RTG_RRF_REPRESENTATION_REGISTRY": "rrf"}
cache = {}
def src(name, ver):
    k = (name, ver)
    if k not in cache:
        r = subprocess.run(["git", "show", f"{F[name]}-v{ver}:dsn/{name}.md"], capture_output=True)
        cache[k] = r.stdout.decode("utf-8") if r.returncode == 0 else None
    return cache[k]
def anchors_ok(s, loc):
    return [a for a in re.findall(r"#([\w-]+)", loc) if f"{{#{a}}}" not in s and f'id="{a}"' not in s]
bad = 0; n = 0
for name, ver, loc, rids in re.findall(r"\[import: ([A-Z_]+)_v([0-9.]+)\s+([^|\]]*?)\|\s*([^\]]+)\]", live):
    n += 1
    if name not in F: print("  unknown file", name); bad += 1; continue
    s = src(name, ver)
    if s is None: print(f"  no tag {F[name]}-v{ver}"); bad += 1; continue
    for a in anchors_ok(s, loc): print(f"  anchor missing {F[name]}-v{ver} #{a}"); bad += 1
    for r in re.findall(r"\b[A-Z]+-(?:THM|ALG|DEF|CAND|RESULT|NUM|OPEN|ART|HYP|LEM)-[A-Z0-9]+(?:-[A-Z0-9]+)*", rids):
        if not re.search(r"(RID: |\*\*RID:\*\* `)" + re.escape(r) + r"[\]`]", s): print(f"  RID not declared {F[name]}-v{ver} {r}"); bad += 1
print(f"  [import:] locators: {n}; problems: {bad}")
print("  [import:] pins:", dict(Counter(f"{F[a]}-v{v}" for a, v in re.findall(r"\[import: ([A-Z_]+)_v([0-9.]+)", live) if a in F)))
bad2 = 0; m = 0
for name, ver, loc in re.findall(r"`?(RTG_[A-Z_]+?)_v([0-9.]+)`?\s+(§[^:|\n]*?#[\w-]+)", live):
    if name not in F: continue
    m += 1; s = src(name, ver)
    if s is None: print(f"  no tag {F[name]}-v{ver}"); bad2 += 1; continue
    for a in anchors_ok(s, loc): print(f"  anchor missing {F[name]}-v{ver} #{a}"); bad2 += 1
print(f"  section-anchor locators: {m}; problems: {bad2}")
sys.exit(1 if bad or bad2 else 0)
