#!/usr/bin/env python3
"""Fill the TDR-G v2.12.14 release record from its template (no hand-typed hashes).

usage: fill_tdrg_v2_12_14_record.py [--root REPO]
  reads  evidence/tdrg/v2.12.14/release_record_template.md
  writes records/tdrg/TDRG_v2_12_14_RELEASE_RECORD.md
Markers: {{H:path}} full SHA-256 of a tree file; {{S:path}} short form xxxxxxxx…yyyy; {{G:ref:path}} full SHA-256 of a
file at a git ref; {{GATES}}, {{CONTROLS}}, {{EXHAUSTIVE}} from the checker outputs in evidence/tdrg/v2.12.14/;
{{SIZE}} a bytes/lines table of the base (tag tdrg-v2.12.13) and the candidate. Any marker left unfilled is an error.
"""
import hashlib, os, re, subprocess, sys

root = sys.argv[sys.argv.index("--root") + 1] if "--root" in sys.argv else os.getcwd()
P = lambda p: os.path.join(root, p)
sha = lambda b: hashlib.sha256(b).hexdigest()
tpl = open(P("evidence/tdrg/v2.12.14/release_record_template.md"), encoding="utf-8").read()


def git_show(ref, path):
    r = subprocess.run(["git", "-C", root, "show", f"{ref}:{path}"], capture_output=True)
    if r.returncode: raise SystemExit(f"cannot read {ref}:{path}")
    return r.stdout


out = re.sub(r"\{\{H:([^}]+)\}\}", lambda m: sha(open(P(m.group(1)), "rb").read()), tpl)
out = re.sub(r"\{\{S:([^}]+)\}\}", lambda m: (lambda h: f"{h[:8]}…{h[-4:]}")(sha(open(P(m.group(1)), "rb").read())), out)
out = re.sub(r"\{\{G:([^:}]+):([^}]+)\}\}", lambda m: sha(git_show(m.group(1), m.group(2))), out)
gates = open(P("evidence/tdrg/v2.12.14/check_output.txt"), encoding="utf-8").read().strip().splitlines()
summary = [l for l in gates if l.startswith("RESULT:")][0]
gate_lines = [re.sub(r"\s+", " ", l.split("]", 1)[1].strip()) for l in gates if l.startswith("[PASS]") or l.startswith("[FAIL]")]
out = out.replace("{{GATES}}", summary + " — " + "; ".join(g.split(" ")[0] + " " + g.split(" ")[1] for g in gate_lines) + ".")
out = out.replace("{{CONTROLS}}", open(P("evidence/tdrg/v2.12.14/controls_output.txt"), encoding="utf-8").read().strip())
ex = open(P("evidence/tdrg/v2.12.14/check_exhaustive_output.txt"), encoding="utf-8").read().strip().splitlines()
out = out.replace("{{EXHAUSTIVE}}", "\n".join(l for l in ex if "exhaustive" in l or l.startswith("RESULT")))
base = git_show("tdrg-v2.12.13", "dsn/RTG_DISCRETE_GENESIS_DSN.md")
cand = open(P("dsn/RTG_DISCRETE_GENESIS_DSN.md"), "rb").read()
nl = lambda b: b.count(b"\n") + (0 if b.endswith(b"\n") else 1)
size = ("| File | Bytes | Lines |\n|---|---|---|\n"
        f"| v2.12.13 (adopted) | {len(base):,} | {nl(base):,} |\n"
        f"| v2.12.14 candidate | {len(cand):,} | {nl(cand):,} |\n\n"
        f"Net change: +{len(cand) - len(base):,} bytes (+{100 * (len(cand) - len(base)) / len(base):.1f} %). Corrections "
        "only: the orientation definitions and no-go remark, SG-14, the §6.12 orientation-covariance block, the §7 register "
        "and RID map, the §8 custody register and the Appendix A entry account for the growth; compaction is v2.13.")
out = out.replace("{{SIZE}}", size)
left = re.findall(r"\{\{[^}]*\}\}", out)
if left: raise SystemExit(f"unfilled markers: {left}")
open(P("records/tdrg/TDRG_v2_12_14_RELEASE_RECORD.md"), "w", encoding="utf-8").write(out)
print("written", sha(out.encode()))
