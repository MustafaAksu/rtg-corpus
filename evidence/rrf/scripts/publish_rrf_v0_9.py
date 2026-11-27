#!/usr/bin/env python3
"""Replay the explicitly approved RRF v0.9 publication-status transform.

The frozen S2b DRAFT remains the input for its compaction checker. This script
checks the separately enumerated adoption/registration/navigation metadata
delta only; it is not a scientific or semantic equivalence proof.
"""
import argparse, copy, hashlib, json, subprocess
from pathlib import Path
def sha(t):
    return hashlib.sha256(t.encode("utf-8")).hexdigest()
def require(c, msg):
    if not c: raise ValueError(msg)
def verify(source, target, plan):
    require(sha(source) == plan["source"]["sha256"], "source hash")
    require(sha(target) == plan["target"]["sha256"], "target hash")
    require(len(source.encode("utf-8")) == plan["source"]["bytes"], "source bytes")
    require(len(target.encode("utf-8")) == plan["target"]["bytes"], "target bytes")
    lines = source.split("\n")
    seen = set()
    for e in plan["operations"]:
        i = e["line"] - 1
        require(0 <= i < len(lines) and i not in seen and lines[i] == e["old"], "edit anchor")
        require("\n" not in e["new"], "line-only metadata")
        seen.add(i)
        lines[i] = e["new"]
    require("\n".join(lines) == target, "unmapped delta")
    for e in plan["operations"]:
        lines[e["line"]-1] = e["old"]
    require("\n".join(lines) == source, "reverse")
    require([s for s in source.split("\n") if s.startswith("| OPEN-")] ==
            [s for s in target.split("\n") if s.startswith("| OPEN-")], "OPEN rows")
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, default=Path("."))
    args = ap.parse_args()
    root = args.root.resolve()
    p = json.loads((root / "evidence/rrf/v0.9/publication_transform.json").read_text(encoding="utf-8"))
    require(p["source"]["commit"] == "8de7a8cd338f37bce3a73910648eecc9a5628b2c", "reviewed head")
    require(p["source"]["path"] == "dsn/RTG_RRF_REPRESENTATION_REGISTRY.md", "reviewed path")
    require(p["source"]["sha256"] == "2950dbc0a2fd3468005a9b86190fe4513068019a21444fd8c431124043ba942d", "reviewed candidate hash")
    require(p["target"]["sha256"] == "28c9c101c715b402b5ed60eeab8bfa2c7e5e637fef3cd2b00961dfa60553075d", "publication hash")
    for anc in ("98da97c311a917d1539b9c31afaba779bc75a73f", "8de7a8cd338f37bce3a73910648eecc9a5628b2c"):
        require(subprocess.run(["git", "-C", str(root), "merge-base", "--is-ancestor", anc, "HEAD"]).returncode == 0, "archive/review ancestry " + anc)
    src = subprocess.check_output(["git", "-C", str(root), "show", "8de7a8cd338f37bce3a73910648eecc9a5628b2c:dsn/RTG_RRF_REPRESENTATION_REGISTRY.md"]).decode("utf-8")
    tgt = (root / p["target"]["path"]).read_bytes().decode("utf-8")
    verify(src, tgt, p)
    for name in ("coefficient", "missing edit", "wrong old"):
        q = copy.deepcopy(p)
        t = tgt
        if name == "coefficient":
            t = t.replace("85.1", "85.0", 1); require(t != tgt, "probe"); q["target"]["sha256"] = sha(t)
        elif name == "missing edit":
            q["operations"].pop()
        else:
            q["operations"][0]["old"] += "x"
        try:
            verify(src, t, q)
        except ValueError:
            print("PASS negative control:", name)
        else:
            raise ValueError("negative control accepted: " + name)
    print("RRF_V0_9_PUBLICATION_PASS", len(p["operations"]), "metadata lines", len(tgt.encode("utf-8")), sha(tgt))
if __name__ == "__main__":
    main()
