# Independent S0 scan: hash every loose file and every archive member (nested zips too) under a root.
# Reads bytes only; executes nothing from the scanned tree.
import hashlib, io, json, os, sys, zipfile
root = sys.argv[1]; out = sys.argv[2]
rows = []
def h(b): return hashlib.sha256(b).hexdigest()
def scan_zip(data, label, depth=0):
    try: z = zipfile.ZipFile(io.BytesIO(data))
    except Exception as e: rows.append({"loc": label, "err": str(e)}); return
    for info in z.infolist():
        if info.is_dir(): continue
        b = z.read(info.filename); loc = f"{label}!{info.filename}"
        rows.append({"loc": loc, "name": os.path.basename(info.filename), "size": len(b), "sha256": h(b)})
        if info.filename.lower().endswith(".zip") and depth < 4: scan_zip(b, loc, depth+1)
for dp, dn, fn in os.walk(root):
    dn[:] = [d for d in dn if d != ".git"]
    for f in fn:
        p = os.path.join(dp, f); b = open(p, "rb").read(); rel = os.path.relpath(p, root)
        rows.append({"loc": rel, "name": f, "size": len(b), "sha256": h(b)})
        if f.lower().endswith(".zip"): scan_zip(b, rel)
json.dump(rows, open(out, "w"), indent=0)
print(len(rows), "objects;", sum(1 for r in rows if "!" in r.get("loc","")), "archive members;", sum(1 for r in rows if "err" in r), "errors")
