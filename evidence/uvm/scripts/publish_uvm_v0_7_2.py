#!/usr/bin/env python3
"""Reproduce/verify UVM v0.7.2 status-only publication, not a science test."""
import argparse, hashlib, json
from pathlib import Path

def sha(b):
    return hashlib.sha256(b).hexdigest()

def require(ok, msg):
    if not ok:
        raise ValueError(msg)

def transform(candidate, m):
    require(sha(candidate) == m["candidate_sha256"], "candidate identity")
    original = candidate.decode("utf-8").split("\n")
    lines = original[:]
    h = original.index("## Local Tag Aliases")
    a = next(i for i, s in enumerate(original) if s.startswith("## Appendix A —"))
    b = next(i for i, s in enumerate(original) if s.startswith("## Appendix B —"))
    f = next(i for i, s in enumerate(original) if s.startswith("*END OF DOCUMENT"))
    require(len(m["operations"]) == 9, "nine metadata edits")
    used = set()
    for op in m["operations"]:
        i = op["line"] - 1
        require(i not in used and (0 <= i < h or a < i < b or i == f), "edit outside metadata")
        used.add(i)
        require(lines[i] == op["old"] and "\n" not in op["new"], "exact old line")
        lines[i] = op["new"]
    require(lines[h:a] == original[h:a] and lines[b:f] == original[b:f], "scientific text changed")
    out = "\n".join(lines).encode("utf-8")
    require(sha(out) == m["published_sha256"], "publication identity")
    reverse = lines[:]
    for op in reversed(m["operations"]):
        i = op["line"] - 1
        require(reverse[i] == op["new"], "inverse edit")
        reverse[i] = op["old"]
    require("\n".join(reverse).encode("utf-8") == candidate, "inverse byte equality")
    require(sum(x.startswith("*END OF DOCUMENT") for x in lines) == 1, "one footer")
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("candidate", type=Path)
    ap.add_argument("publication", type=Path)
    ap.add_argument("map", type=Path)
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    m = json.loads(a.map.read_text(encoding="utf-8"))
    cand = a.candidate.read_bytes()
    out = transform(cand, m)
    if a.check:
        require(a.publication.read_bytes() == out, "publication bytes mismatch")
    else:
        with a.publication.open("xb") as f:
            f.write(out)
    print("PASS candidate SHA-256", sha(cand))
    print("PASS publication SHA-256", sha(out))
    print("PASS 9 exact metadata edits; inverse byte equality")
    print("PASS all live scientific text and Appendix B byte-identical")
    print("PASS one footer; no scientific change at publication")

if __name__ == "__main__":
    main()
