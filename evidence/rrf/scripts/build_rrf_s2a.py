#!/usr/bin/env python3
"""Rebuild/check the RRF S2a intermediate from the immutable adopted tag.
No owner certificates are executed. Default: compare with the working-tree DSN.
"""
import argparse, hashlib, json, subprocess
from pathlib import Path

def digest(data):
    return hashlib.sha256(data).hexdigest()

def require(condition, msg):
    if not condition:
        raise ValueError(msg)

def build(raw, plan):
    require(len(raw) == plan["base_bytes"] and digest(raw) == plan["base_sha256"], "base identity")
    lines = raw.decode("utf-8").split("\n")
    result, cur = [], 1
    for op in plan["operations"]:
        start, end = op["start"], op["end"]
        require(cur <= start <= end <= len(lines), "range " + op["id"])
        old = "\n".join(lines[start-1:end]).encode("utf-8")
        new = op["replacement"].encode("utf-8")
        require(digest(old) == op["old_sha256"], "anchor " + op["id"])
        require(digest(new) == op["new_sha256"] and old != new, "replacement " + op["id"])
        result.extend(lines[cur-1:start-1])
        result.extend(op["replacement"].split("\n"))
        cur = end + 1
    result.extend(lines[cur-1:])
    data = "\n".join(result).encode("utf-8")
    require(len(data) == plan["target_bytes"] and digest(data) == plan["target_sha256"], "target identity")
    return data

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    plan = json.loads((root / "evidence/rrf/v0.9/s2a_build_plan.json").read_bytes())
    raw = subprocess.check_output(["git", "-C", str(root), "show", plan["base_tag"] + ":" + plan["path"]])
    commit = subprocess.check_output(["git", "-C", str(root), "rev-parse", plan["base_tag"] + "^{commit}"]).decode().strip()
    require(commit == plan["base_commit"], "tag commit")
    candidate = build(raw, plan)
    for name, bad_raw, bad_plan in [
        ("changed base", raw + b" ", plan),
        ("changed anchor", raw, {**plan, "operations": [{**plan["operations"][0], "old_sha256": "0"*64}, *plan["operations"][1:]]}),
        ("changed target", raw, {**plan, "target_sha256": "0"*64}),
    ]:
        try:
            build(bad_raw, bad_plan)
        except ValueError:
            print("PASS negative control:", name)
        else:
            raise ValueError("negative control accepted: " + name)
    if args.output:
        args.output.write_bytes(candidate)
    else:
        require((root / plan["path"]).read_bytes() == candidate, "working-tree candidate differs")
    print("S2A_BUILD_PASS", len(plan["operations"]), "operations", len(candidate), digest(candidate))

if __name__ == "__main__":
    main()
