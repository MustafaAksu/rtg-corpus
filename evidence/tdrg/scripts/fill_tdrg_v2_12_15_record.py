#!/usr/bin/env python3
"""Fill the TDR-G v2.12.15 release record from its template (no hand-typed hashes).

usage: fill_tdrg_v2_12_15_record.py [--root REPO]
  reads  evidence/tdrg/v2.12.15/release_record_template.md
  writes records/tdrg/TDRG_v2_12_15_RELEASE_RECORD.md
Markers: {{H:path}} full SHA-256 of a tree file; {{S:path}} short form; {{GATES}}, {{CONTROLS}} from the checker
outputs in evidence/tdrg/v2.12.15/; {{SIZE}} bytes/lines of the base (tag tdrg-v2.12.14) and the candidate.
Any marker left unfilled is an error.
"""
import hashlib, os, re, subprocess, sys

root = sys.argv[sys.argv.index("--root") + 1] if "--root" in sys.argv else os.getcwd()
P = lambda p: os.path.join(root, p)
sha = lambda b: hashlib.sha256(b).hexdigest()
V = "evidence/tdrg/v2.12.15/"
out = open(P(V + "release_record_template.md"), encoding="utf-8").read()
out = re.sub(r"\{\{H:([^}]+)\}\}", lambda m: sha(open(P(m.group(1)), "rb").read()), out)
out = re.sub(r"\{\{S:([^}]+)\}\}", lambda m: (lambda h: f"{h[:8]}…{h[-4:]}")(sha(open(P(m.group(1)), "rb").read())), out)
g = open(P(V + "check_output.txt"), encoding="utf-8").read().strip().splitlines()
summary = [l for l in g if l.startswith("RESULT:")][0]
names = [" ".join(l.split("]", 1)[1].split()[:2]) for l in g if l.startswith("[PASS]") or l.startswith("[FAIL]")]
out = out.replace("{{GATES}}", summary + " — " + "; ".join(names) + ".")
out = out.replace("{{CONTROLS}}", open(P(V + "controls_output.txt"), encoding="utf-8").read().strip())
base = subprocess.run(["git", "-C", root, "show", "tdrg-v2.12.14:dsn/RTG_DISCRETE_GENESIS_DSN.md"], capture_output=True, check=True).stdout
cand = open(P("dsn/RTG_DISCRETE_GENESIS_DSN.md"), "rb").read()
nl = lambda b: b.count(b"\n") + (0 if b.endswith(b"\n") else 1)
out = out.replace("{{SIZE}}", "| File | Bytes | Lines |\n|---|---|---|\n"
                  f"| v2.12.14 (adopted) | {len(base):,} | {nl(base):,} |\n| v2.12.15 candidate | {len(cand):,} | {nl(cand):,} |\n\n"
                  f"Net change: +{len(cand) - len(base):,} bytes (+{100 * (len(cand) - len(base)) / len(base):.1f} %), "
                  "almost all of it the new §6.13 and the TDRG-DEF-STAR statement.")
left = re.findall(r"\{\{[^}]*\}\}", out)
if left: raise SystemExit(f"unfilled markers: {left}")
open(P("records/tdrg/TDRG_v2_12_15_RELEASE_RECORD.md"), "w", encoding="utf-8").write(out)
print("written", sha(out.encode()))
