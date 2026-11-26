"""RRF S0 reviewer check: regenerate the two v0.8.4 publication diffs whose files are missing.

Reads bytes only from the repository (no file from upload/ is executed). Exit code 0 only if
(1) the generator reproduces the archived Review diff A byte-exactly (control), and
(2) both regenerated diffs equal the SHA-256 and byte counts printed in the v0.8.4 adoption
    record and RTG_RRF_v0_8_4_ADOPTION_QA.json.
Usage: python -I evidence/rrf/scripts/rrf_s0_regenerate_v084_diffs.py <repo-root> [--write <outdir>]
"""
import difflib, hashlib, os, sys, zipfile
root = sys.argv[1]; U = os.path.join(root, "upload", "corpus-originals-20261123")
out = sys.argv[sys.argv.index("--write") + 1] if "--write" in sys.argv else None
sha = lambda b: hashlib.sha256(b).hexdigest()
def rd(p): return open(os.path.join(U, p), "rb").read()
pkg = zipfile.ZipFile(os.path.join(U, "RTG_RRF_v0_8_4_REVISED_REVIEW_PACKAGE.zip"))
cand_name = "RTG_RRF_REPRESENTATION_REGISTRY_v0_8_4_REVISED_REVIEW_CANDIDATE.md"
cand = pkg.read(cand_name); diffA = pkg.read("RTG_RRF_v0_8_3_ADOPTED_to_v0_8_4_REVISED_REVIEW_CANDIDATE.diff")
v083n, v084n = "RTG_RRF_REPRESENTATION_REGISTRY_v0_8_3.md", "RTG_RRF_REPRESENTATION_REGISTRY_v0_8_4.md"
v083, v084 = rd(v083n), rd(v084n)
tagged = open(os.path.join(root, "dsn", "RTG_RRF_REPRESENTATION_REGISTRY.md"), "rb").read()
def ud(a, b, fa, fb):
    return "".join(difflib.unified_diff(a.decode("utf-8").splitlines(True), b.decode("utf-8").splitlines(True), fa, fb, n=3)).encode("utf-8")
checks = []
def chk(name, ok, detail=""): checks.append((name, ok)); print(("PASS " if ok else "FAIL ") + name, detail)
chk("input sha v0.8.3", sha(v083) == "b393657e75e78ce46aea8920f4e5c25480e523caaa105589920a34ee55d4a187")
chk("input sha revised candidate", sha(cand) == "fc53acff20c17e152884bc1835d4de2d4354a406f4d63262cdb04c200e2cab9e")
chk("input sha v0.8.4 upload = tagged dsn", sha(v084) == sha(tagged) == "2fb0a0fe9d998be91618cb731e2dee7301952ffdbe374f4889dd5e61c5cbafce")
ctl = ud(v083, cand, v083n, cand_name)
chk("control: generator reproduces archived Review diff A", ctl == diffA, f"{len(ctl)} bytes {sha(ctl)}")
targets = [("RTG_RRF_v0_8_4_REVISED_CANDIDATE_to_ADOPTED.diff", cand, v084, cand_name, 7893, "e8eb5193a71fc573f4003cad1052c6b0b2cbe15290c584b06ac0a14c973403ce"),
           ("RTG_RRF_v0_8_3_ADOPTED_to_v0_8_4_ADOPTED.diff", v083, v084, v083n, 37612, "bcb8c9b5721ea4fbeb22f1be88d9578f193e1555f56ef8f7f7e414817321a967")]
for fn, a, b, fa, n, h in targets:
    d = ud(a, b, fa, v084n)
    chk("regenerated " + fn, len(d) == n and sha(d) == h, f"{len(d)} bytes {sha(d)}")
    if out: os.makedirs(out, exist_ok=True); open(os.path.join(out, fn), "wb").write(d)
# negative control: a one-byte change must break the match
bad = ud(v083, v084.replace(b"v0.8.4", b"v0.8.5", 1), v083n, v084n)
chk("negative control: perturbed input does not match", sha(bad) != targets[1][5])
sys.exit(0 if all(ok for _, ok in checks) else 1)
