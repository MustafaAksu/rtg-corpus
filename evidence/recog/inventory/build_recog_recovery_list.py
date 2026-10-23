#!/usr/bin/env python3
"""Inventory of the hashes cited in the RECOG DSN against the repository.

Usage (repository root):  python -I evidence/recog/inventory/build_recog_recovery_list.py > out.json
Reads dsn/RTG_RELATIONAL_RECOGNITION_DSN.md, hashes every tracked file, every member of every
tracked ZIP, the hand-over bundle in history (HISTORY_ZIPS) and every dsn/ file at every tag; prints JSON with one row per
cited hash (full 64-hex or short 'xxxxxxxx…yyyy') and where it was found.
"""
import hashlib, json, re, subprocess, sys, zipfile, io

DSN = "dsn/RTG_RELATIONAL_RECOGNITION_DSN.md"

def sh(*a):
    return subprocess.run(a, check=True, capture_output=True).stdout

def sha(b):
    return hashlib.sha256(b).hexdigest()

index = {}  # hash -> list of locations
def add(h, loc):
    index.setdefault(h, []).append(loc)

for p in sh("git", "ls-files", "-z").decode().split("\0"):
    if not p:
        continue
    b = open(p, "rb").read()
    add(sha(b), p)
    if p.endswith(".zip"):
        with zipfile.ZipFile(io.BytesIO(b)) as z:
            for n in z.namelist():
                if not n.endswith("/"):
                    add(sha(z.read(n)), f"{p}!{n}")
# Hand-over bundle as uploaded (history only after placement): its editions/ are not placed in the tree.
HISTORY_ZIPS = ["f177eee:upload/recog-record-recovery/RECOG_HANDOVER_RECORDS_AND_EVIDENCE_20261023.zip"]
for spec in HISTORY_ZIPS:
    with zipfile.ZipFile(io.BytesIO(sh("git", "show", spec))) as z:
        for n in z.namelist():
            if not n.endswith("/"):
                add(sha(z.read(n)), f"history {spec}!{n}")
for t in sh("git", "tag").decode().split():
    for p in sh("git", "ls-tree", "-r", "--name-only", t, "--", "dsn").decode().split():
        add(sha(sh("git", "show", f"{t}:{p}")), f"tag {t}:{p}")

text = open(DSN, encoding="utf-8").read()
lines = text.split("\n")
rows = {}
full_re = re.compile(r"\b[0-9a-f]{64}\b")
short_re = re.compile(r"\b([0-9a-f]{8})…([0-9a-f]{3,8})\b")
name_re = re.compile(r"`([A-Za-z0-9_.()\-]+\.(?:py|json|jsonl|md|txt|zip|diff|csv))`")
for i, line in enumerate(lines, 1):
    for m in full_re.finditer(line):
        h = m.group(0)
        names = name_re.findall(line[:m.start()])
        r = rows.setdefault(h, {"cited": h, "kind": "full", "lines": [], "name_before": names[-1] if names else None})
        r["lines"].append(i)
    for m in short_re.finditer(line):
        key = f"{m.group(1)}…{m.group(2)}"
        names = name_re.findall(line[:m.start()])
        r = rows.setdefault(key, {"cited": key, "kind": "short", "lines": [], "name_before": names[-1] if names else None})
        r["lines"].append(i)

for k, r in rows.items():
    if r["kind"] == "full":
        r["found"] = index.get(k, [])
    else:
        a, b = k.split("…")
        r["found"] = sorted({loc for h, locs in index.items() if h.startswith(a) and h.endswith(b) for loc in locs})
json.dump({"dsn_sha256": sha(open(DSN, "rb").read()), "rows": list(rows.values())}, sys.stdout, indent=1, ensure_ascii=False)
