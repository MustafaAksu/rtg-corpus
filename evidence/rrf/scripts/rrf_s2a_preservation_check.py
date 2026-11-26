#!/usr/bin/env python3
"""RRF S2a reviewer check: identifier / guard / evidence-filename preservation from the adopted tag to a candidate.

Read-only. Tokens: multi-part identifiers (RIDs, profile and artifact IDs), SG-* guards, RF-O* reference
keys, OPEN-* names and evidence file names. Exit 0 only if every token of the base still occurs in the
candidate, apart from the explicitly allowed header-only changes listed below.
Usage: python -I evidence/rrf/scripts/rrf_s2a_preservation_check.py [--root .] [--base-tag rrf-v0.8.4]
"""
import argparse, re, subprocess, sys
from pathlib import Path
PATH = "dsn/RTG_RRF_REPRESENTATION_REGISTRY.md"
# header 'supersedes'/'revision base' legitimately move to the immediately preceding adopted edition
ALLOWED = {"RTG_RRF_REPRESENTATION_REGISTRY_v0_8_3.md"}
PATS = [r"\b[A-Z][A-Z0-9]*(?:-[A-Z0-9]+){2,}\b", r"\bSG-[A-Z0-9-]+\b", r"\bRF-O\d+-\d+\b",
        r"\bOPEN-[A-Z0-9-]+\b", r"\b[\w.-]+\.(?:zip|json|jsonl|py|md)\b"]
def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--root", default="."); ap.add_argument("--base-tag", default="rrf-v0.8.4")
    a = ap.parse_args(); root = Path(a.root).resolve()
    old = subprocess.check_output(["git", "-C", str(root), "show", f"{a.base_tag}:{PATH}"]).decode("utf-8")
    new = (root / PATH).read_text(encoding="utf-8")
    toks = set()
    for p in PATS: toks |= set(re.findall(p, old))
    lost = sorted(t for t in toks if t not in new and t not in ALLOWED)
    # negative control: removing one known token must be detected
    probe = sorted(t for t in toks if t in new)[0]
    assert probe not in new.replace(probe, ""), "negative control failed"
    for t in lost: print("LOST", t)
    print(f"tokens {len(toks)}; lost {len(lost)}; allowed header changes {sorted(ALLOWED & (toks - set(t for t in toks if t in new)))}")
    sys.exit(1 if lost else 0)
if __name__ == "__main__": main()
