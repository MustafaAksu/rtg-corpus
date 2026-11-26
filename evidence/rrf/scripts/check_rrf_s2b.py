#!/usr/bin/env python3
"""RRF-specific exact-span compaction check for the frozen S2a input.

The general checker has no profile support for this input's YAML header,
cross-section moves, or explicitly tagged historical receipts. This is a
scoped adapter accepted for this edition in review 6079644693, subject to
corrected-head readback. Mechanical coverage is not approval of archival or
editorial classification. Navigation content is not constrained beyond declared
bytes. The archive commit must remain an ancestor of HEAD; verify ancestry
again on main after authorized merge-commit integration.
"""
import argparse, copy, hashlib, json, re, subprocess
from pathlib import Path

def sha(t):
    return hashlib.sha256(t.encode("utf-8")).hexdigest()

def require(ok, message):
    if not ok:
        raise ValueError(message)

def verify(base, candidate, plan):
    require(sha(base) == plan["base"]["sha256"], "frozen source identity")
    require(sha(candidate) == plan["candidate"]["sha256"], "candidate identity")
    b, c = base.split("\n"), candidate.split("\n")
    require(len(b) == plan["base"]["lines"] and len(c) == plan["candidate"]["lines"], "line counts")
    require(len(base.encode("utf-8")) == plan["base"]["bytes"] and len(candidate.encode("utf-8")) == plan["candidate"]["bytes"], "byte counts")
    src, dst = set(), set()
    ids = set()
    for op in plan["operations"]:
        oid, kind = op["id"], op["kind"]
        require(oid not in ids, "duplicate operation")
        ids.add(oid)
        if "source" in op:
            a, z = op["source"]
            require(1 <= a <= z <= len(b), "source bounds " + oid)
            rng = set(range(a, z+1))
            require(not src & rng, "overlap source " + oid)
            src.update(rng)
            source = "\n".join(b[a-1:z])
            require(sha(source) == op["source_sha256"], "source span " + oid)
        else:
            source = None
            require(kind == "navigation", "only navigation may lack source")
        if kind == "archive":
            require("destination" not in op and source is not None, "archive shape " + oid)
            require(op["archive"]["git"] == plan["base"]["git"] and op["archive"]["lines"] == op["source"] and op["archive"]["sha256"] == sha(source), "archive locator " + oid)
            continue
        require(kind in {"exact", "editorial", "navigation"}, "unknown kind")
        a, z = op["destination"]
        require(1 <= a <= z <= len(c), "destination bounds " + oid)
        rng = set(range(a, z+1))
        require(not dst & rng, "overlap destination " + oid)
        dst.update(rng)
        target = "\n".join(c[a-1:z])
        require(sha(target) == op["destination_sha256"], "destination span " + oid)
        require(target == (source if kind == "exact" else op["text"]), "declared text " + oid)
        if kind == "editorial":
            require(source is not None, "editorial source")
        if kind == "navigation":
            require(source is None, "navigation cannot replace a claim")
    require(src == set(range(1,len(b)+1)), "incomplete source coverage")
    require(dst == set(range(1,len(c)+1)), "incomplete destination coverage")
    # Every indexed use still has the same inline source-tag text at its
    # original qualified line, independent of the added navigation table.
    for use in plan["import_use_index"]:
        require(b[use["source_line"]-1] == c[use["candidate_line"]-1],
                "changed indexed use " + use["key"])
    # These are extra structural gates, not scientific equivalence.
    profiles = [x for x in b if re.match(r"^## 2\.[1-5] `RRF-", x)]
    require(len(profiles)==5 and all(x in c for x in profiles), "profile headings")
    for i in ("RRF-OPEN-POLE-RELABELING","RRF-OPEN-IDENTIFICATION-PRIMITIVE","RRF-OPEN-NETWORK-VARIABLES","RRF-OPEN-JOINT-NF"):
        rows = [line for line in c if line.startswith("| OPEN-") and i in line]
        require(len(rows)==1 and "| ACTIVE | RRF |" in rows[0], "OPEN state " + i)
    require(sum(line.startswith("*END OF DOCUMENT") for line in c)==1, "one footer")
    require("**Document status:** DRAFT" in candidate, "draft status")
    require("**Closure criterion wording: PI_PENDING.**" in candidate, "closure decision must remain pending at this review head")
    require("Proposed closure criterion (PI_PENDING); relevant interfaces" in candidate, "closure column metadata")
    require("records/rrf/RTG_RRF_REPRESENTATION_REGISTRY_v0_8_4_ADOPTION_RECORD.md" in candidate, "predecessor adoption-record pointer")
    return len(src),len(dst)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--root",type=Path,default=Path("."))
    args=ap.parse_args()
    root=args.root.resolve()
    plan=json.loads((root / "evidence/rrf/v0.9/s2b_movement_map.json").read_text(encoding="utf-8"))
    frozen = "98da97c311a917d1539b9c31afaba779bc75a73f"
    require(plan["base"]["commit"] == frozen, "reviewed archive commit")
    require(plan["base"]["git"] == frozen + ":dsn/RTG_RRF_REPRESENTATION_REGISTRY.md", "reviewed archive path")
    ancestry = subprocess.run(["git", "-C", str(root), "merge-base", "--is-ancestor", frozen, "HEAD"])
    require(ancestry.returncode == 0, "frozen archive commit must be ancestor of HEAD")
    print("PASS archive base ancestry:", frozen)
    base=subprocess.check_output(["git","-C",str(root),"show",plan["base"]["git"]]).decode("utf-8")
    candidate=(root / plan["candidate"]["path"]).read_bytes().decode("utf-8")
    require(plan["base"]["sha256"]=="390f75e447b7d5a9dcb01810d7eb513e9feef3c157f0de2f2f79afb259b39d72", "expected reviewed freeze")
    sb,sc=verify(base,candidate,plan)
    def controls():
        m=copy.deepcopy(plan)
        d=candidate.replace("85.1","85.0",1)
        require(d!=candidate,"formula probe")
        m["candidate"]["sha256"]=sha(d)
        yield "changed coefficient with rehashed file",d,m
        m=copy.deepcopy(plan)
        m["operations"].pop(next(i for i,o in enumerate(m["operations"]) if o["kind"]=="exact"))
        yield "unaccounted exact block",candidate,m
        m=copy.deepcopy(plan)
        o=copy.deepcopy(next(o for o in m["operations"] if o["kind"]=="exact"))
        o["id"]="NEG-DUP"
        m["operations"].append(o)
        yield "duplicate span",candidate,m
        m=copy.deepcopy(plan)
        o=next(o for o in m["operations"] if o["kind"]=="archive")
        o["archive"]["lines"][0]+=1
        yield "broken archival locator",candidate,m
    for name,d,m in controls():
        try:
            verify(base,d,m)
        except ValueError:
            print("PASS negative control:",name)
        else:
            raise ValueError("accepted negative control: "+name)
    print("RRF_S2B_EXACT_MAP_PASS",sb,"source lines",sc,"destination lines",len(plan["operations"]),"operations",sha(candidate))
    print("REVIEW_REQUIRED: history classifications, editorial changes, import ledger and profile-specific checker eligibility")

if __name__=="__main__":
    main()
