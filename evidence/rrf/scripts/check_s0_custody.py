#!/usr/bin/env python3
"""S0 byte custody: read-only; no historical source or scientific script executed.
Run from checkout root: python -I evidence/rrf/scripts/check_s0_custody.py .
"""
import difflib
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import zipfile

root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
m = json.loads((root / "evidence/rrf/s0/custody_manifest.json").read_text(encoding="utf-8"))
U = root / "upload/corpus-originals-20261123"
def sha(b):
    return hashlib.sha256(b).hexdigest()
def require(ok, label):
    if not ok:
        raise SystemExit("FAIL " + label)
def git(*args):
    return subprocess.check_output(["git", "-C", str(root), *args])
def read(p):
    return (root / p).read_bytes()
def diff(a, b, fa, fb):
    return "".join(difflib.unified_diff(a.decode("utf-8").splitlines(True),
        b.decode("utf-8").splitlines(True), fa, fb, n=3)).encode("utf-8")
require(sha(b"abc") == "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad", "SHA-256 self-test")
for g in m["governing"]:
    tag, path = g["tag"], g["path"]
    require(git("rev-parse", "refs/tags/" + tag).decode().strip() == g["tag_object"], tag + " object")
    require(git("rev-parse", tag + "^{commit}").decode().strip() == g["commit"], tag + " commit")
    require(git("rev-parse", tag + ":" + path).decode().strip() == g["blob"], tag + " blob")
    b = git("show", tag + ":" + path)
    require(len(b) == g["bytes"] and sha(b) == g["sha256"] and b == read(path), tag + " bytes")
    print("PASS governing", tag, len(b), sha(b))
require(git("rev-parse", "HEAD:upload/corpus-originals-20261123").decode().strip() == m["original_upload_tree"], "upload tree")
require(git("diff", "--name-only", m["checkpoint"], "HEAD", "--", "upload/", "dsn/", "noncanonical/", "BASELINE.md") == b"", "protected paths")
v83 = "RTG_RRF_REPRESENTATION_REGISTRY_v0_8_3.md"
v84 = "RTG_RRF_REPRESENTATION_REGISTRY_v0_8_4.md"
cand = "RTG_RRF_REPRESENTATION_REGISTRY_v0_8_4_REVISED_REVIEW_CANDIDATE.md"
ctl = m["review_diff_control"]
with zipfile.ZipFile(root / ctl["archive"]) as z:
    c = z.read(cand)
    original = z.read(ctl["member"])
a, b = (U / v83).read_bytes(), (U / v84).read_bytes()
require(sha(a) == "b393657e75e78ce46aea8920f4e5c25480e523caaa105589920a34ee55d4a187", "v0.8.3 input")
require(sha(c) == "fc53acff20c17e152884bc1835d4de2d4354a406f4d63262cdb04c200e2cab9e", "candidate input")
require(sha(b) == m["governing"][0]["sha256"], "v0.8.4 input")
d = diff(a, c, v83, cand)
require(d == original and sha(d) == ctl["sha256"] and len(d) == ctl["bytes"], "archived review diff A control")
print("PASS review diff A control", len(d), sha(d))
require(sha(diff(a, b.replace(b"v0.8.4", b"v0.8.5", 1), v83, v84)) != "bcb8c9b5721ea4fbeb22f1be88d9578f193e1555f56ef8f7f7e414817321a967", "negative control")
print("PASS negative control")
for x in m["placements"]:
    out = read(x["destination"])
    if x["kind"] == "original":
        expected = read(x["source"])
    elif x["kind"] == "archive member":
        require(sha(read(x["source"])) == x["archive_sha256"], x["source"] + " digest")
        with zipfile.ZipFile(root / x["source"]) as z:
            expected = z.read(x["member"])
    elif x["kind"] == "regenerated":
        expected = diff(c if x["from"] == cand else a, b, x["from"], v84)
    else:
        raise SystemExit("Unknown kind")
    require(out == expected and len(out) == x["bytes"] and sha(out) == x["sha256"], x["destination"])
    require(git("rev-parse", "HEAD:" + x["destination"]).decode().strip() == x["blob"], x["destination"] + " blob")
    print("PASS", x["kind"], x["destination"], len(out), sha(out))
print("S0_CUSTODY_PASS", len(m["placements"]), "placements (byte identity only; no scientific adoption)")
