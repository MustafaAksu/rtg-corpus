#!/usr/bin/env python3
"""Verify Programme v1.5 publication, not science or adoption. Exact UTF-8 bytes."""
import argparse
import hashlib
import json
from pathlib import Path

ADOPTED = "c07689b0f6e617c0b4a6a29d95d194b99bbbe3f4c3c8a686ccfd02d492c0811c"
PUBLISHED = "9c53159f64feddfba7cfcb2452f9eca1c61bac63b744cb05421417d384bf9611"
HEAD = "bad1314c08287aabd6fbc7114dc391764bc96a89"
ALLOWED = (7, 8, 14, 258, 285, 560, 569, 572, 573, 641)

def sha(raw):
    return hashlib.sha256(raw).hexdigest()

def verify(candidate, published, mapping):
    assert sha(candidate) == ADOPTED
    assert sha(published) == PUBLISHED
    assert mapping["adopted_candidate_commit"] == HEAD
    assert mapping["adopted_candidate_sha256"] == ADOPTED
    assert mapping["published_sha256"] == PUBLISHED
    assert mapping["pi_decision_comment"] == 7185805217
    ops = mapping["operations"]
    assert tuple(op["line"] for op in ops) == ALLOWED
    a, b = candidate.decode("utf-8").split("\n"), published.decode("utf-8").split("\n")
    assert len(a) == len(b)
    out, inv = a[:], b[:]
    for op in ops:
        i = op["line"] - 1
        assert "\n" not in op["old"] and "\n" not in op["new"]
        assert a[i] == op["old"] and b[i] == op["new"]
        assert op["old"] != op["new"]
        out[i], inv[i] = op["new"], op["old"]
    assert "\n".join(out).encode("utf-8") == published
    assert "\n".join(inv).encode("utf-8") == candidate
    assert tuple(i + 1 for i, (x, y) in enumerate(zip(a, b)) if x != y) == ALLOWED
    print("PUBLICATION PASS", PUBLISHED, "metadata lines", len(ALLOWED), "inverse exact")

def main():
    p = argparse.ArgumentParser()
    p.add_argument("candidate", type=Path)
    p.add_argument("published", type=Path)
    p.add_argument("mapping", type=Path)
    a = p.parse_args()
    verify(a.candidate.read_bytes(), a.published.read_bytes(), json.loads(a.mapping.read_text(encoding="utf-8")))

if __name__ == "__main__":
    main()
