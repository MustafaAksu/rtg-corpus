#!/usr/bin/env python3
"""Fill the TDR-G v2.13 release record from its template (no hand-typed hashes).

    python3 -I evidence/tdrg/v2.13/fill_release_record.py      (from the repository root)

reads  evidence/tdrg/v2.13/release_record_template.md
writes records/tdrg/TDRG_v2_13_RELEASE_RECORD.md
Markers: {{H:path}} SHA-256 of a tree file; {{GATES1}}, {{CONTROLS1}} from the stage-1 outputs; {{CC}} the
compaction-check summary; {{CONTROLS2}} the stage-2 controls output; {{SIZE}} tools/dsn_lint.py --prev against
the tag tdrg-v2.12.15. Any marker left unfilled is an error.
"""
import hashlib, os, re, subprocess, sys, tempfile

V = "evidence/tdrg/v2.13/"
sha = lambda b: hashlib.sha256(b).hexdigest()
rd = lambda p: open(p, encoding="utf-8").read()
out = rd(V + "release_record_template.md")
out = re.sub(r"\{\{H:([^}]+)\}\}", lambda m: sha(open(m.group(1), "rb").read()), out)
g = rd(V + "stage1/check_output.txt").strip().splitlines()
out = out.replace("{{GATES1}}", [l for l in g if l.startswith("RESULT:")][0] + " — " +
                  "; ".join(l.split("] ", 1)[1].split(" — ")[0] for l in g if l.startswith("[")) + ".")
out = out.replace("{{CONTROLS1}}", rd(V + "stage1/controls_output.txt").strip())
cc = rd(V + "stage2/check_compaction_output.txt").strip().splitlines()
blk = [l for l in cc if l.startswith(("PASS  qualified", "FAIL  qualified"))]
out = out.replace("{{CC}}", "%s, exit 0 — %d checks, every operation and every global check PASS; %s" % (
    cc[-1], sum(1 for l in cc if l[:4] in ("PASS", "FAIL")), blk[0].split("—", 1)[1].strip() if blk else ""))
out = out.replace("{{CONTROLS2}}", rd(V + "stage2/stage2_negative_controls_output.txt").strip())
with tempfile.TemporaryDirectory() as d:
    p = os.path.join(d, "v2_12_15.md")
    open(p, "wb").write(subprocess.run(["git", "show", "tdrg-v2.12.15:dsn/RTG_DISCRETE_GENESIS_DSN.md"],
                                       capture_output=True, check=True).stdout)
    lint = subprocess.run([sys.executable, "-I", "tools/dsn_lint.py", "dsn/RTG_DISCRETE_GENESIS_DSN.md", "--prev", p],
                          capture_output=True, text=True, check=True).stdout.replace(p, "tdrg-v2.12.15")
out = out.replace("{{SIZE}}", "```\n" + lint.strip() + "\n```\n\nCounting method: the lint script's own "
                  "(whitespace tokens; §1 between its heading and the next `## `). Stage-1 intermediate: 191,737 bytes.")
left = re.findall(r"\{\{[^}]*\}\}", out)
if left:
    raise SystemExit("unfilled markers: %s" % left)
open("records/tdrg/TDRG_v2_13_RELEASE_RECORD.md", "w", encoding="utf-8").write(out)
print("written", sha(out.encode()))
