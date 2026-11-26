#!/usr/bin/env python3
"""Rebuild/check the RRF S2a intermediate from the immutable adopted tag.
No owner certificates are executed. Default: compare with the working-tree DSN.
"""
import argparse, hashlib, json, re, subprocess
from pathlib import Path

def digest(data):
    return hashlib.sha256(data).hexdigest()

def require(condition, msg):
    if not condition:
        raise ValueError(msg)

# Same lexical coverage as the unmodified independent reviewer check (#406).
# This is a pointer-presence check, not proof of semantic equivalence.
PRESERVATION_ALLOWED = {"RTG_RRF_REPRESENTATION_REGISTRY_v0_8_3.md"}
PRESERVATION_PATTERNS = [
    r"\b[A-Z][A-Z0-9]*(?:-[A-Z0-9]+){2,}\b",
    r"\bSG-[A-Z0-9-]+\b", r"\bRF-O\d+-\d+\b",
    r"\bOPEN-[A-Z0-9-]+\b", r"\b[\w.-]+\.(?:zip|json|jsonl|py|md)\b",
]

def preservation_tokens(old):
    toks = set()
    for pattern in PRESERVATION_PATTERNS:
        toks.update(re.findall(pattern, old))
    return toks

def missing_tokens(old, new):
    return sorted(t for t in preservation_tokens(old) if t not in new and t not in PRESERVATION_ALLOWED)

def require_preservation(old, new, plan):
    lost = missing_tokens(old, new)
    require(not lost, "lost preserved pointers: " + ", ".join(lost))
    p = plan["preservation"]
    receipt = "\n".join(old.split("\n")[p["historical_receipt_start"]-1:p["historical_receipt_end"]])
    require(receipt in new, "verbatim historical receipt block")

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
    require_preservation(raw.decode("utf-8"), data.decode("utf-8"), plan)
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
    old_text, new_text = raw.decode("utf-8"), candidate.decode("utf-8")
    # Test the lexical detector itself, independently of target hash failure.
    probe = "RF-O09-03"
    require(probe in new_text, "preservation probe absent")
    require(probe in missing_tokens(old_text, new_text.replace(probe, "")), "pointer negative control")
    try:
        require_preservation(old_text, new_text.replace(probe, ""), plan)
    except ValueError:
        print("PASS negative control: removed protected pointer")
    else:
        raise ValueError("preservation negative control accepted")
    print("PRESERVATION_PASS", len(preservation_tokens(old_text)), "tokens; lost 0; verbatim historical receipts")
    archive = plan["preservation"]["archive"]
    data = (root / archive["path"]).read_bytes()
    require(len(data) == archive["bytes"] and digest(data) == archive["sha256"], "P2-B archive identity")
    print("P2B_ARCHIVE_IDENTITY_PASS", len(data), digest(data), "(not certificate replay)")
    if args.output:
        args.output.write_bytes(candidate)
    else:
        require((root / plan["path"]).read_bytes() == candidate, "working-tree candidate differs")
    print("S2A_BUILD_PASS", len(plan["operations"]), "operations", len(candidate), digest(candidate))

if __name__ == "__main__":
    main()
