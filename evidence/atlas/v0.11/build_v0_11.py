#!/usr/bin/env python3
"""Atlas v0.11 assembly: the reviewed pilot chain (stage 1 -> 2a -> 2b) plus the three self-version edits.

No source moved: the source snapshot and all 18 source identities are those of atlas-v0.10.
Usage: build_v0_11.py STAGE2B.md OUT_ATLAS.md MANIFEST_V0_10.json OUT_MANIFEST.json
"""
import hashlib, json, sys
BASE_SHA = '66f0b2ebdad84a578a7159d727c2d51d3831ebea15f18c07d9b17744173c20da'
EDITS = [(1, '# RTG STATE ATLAS v0.10', '# RTG STATE ATLAS v0.11'),
         (4, 'evidence/atlas/v0.10/source_manifest.json', 'evidence/atlas/v0.11/source_manifest.json'),
         (1542, '*END — RTG STATE ATLAS v0.10.', '*END — RTG STATE ATLAS v0.11.')]
def main():
    src, out, m10, mout = sys.argv[1:5]
    raw = open(src, 'rb').read(); assert hashlib.sha256(raw).hexdigest() == BASE_SHA, 'base is not the stage-2b output'
    L = raw.decode('utf-8').split('\n'); assert len(L) == 1543
    for n, old, new in EDITS:
        assert L[n - 1].count(old) == 1, (n, old); L[n - 1] = L[n - 1].replace(old, new)
    cand = '\n'.join(L).encode('utf-8'); open(out, 'wb').write(cand)
    m = json.load(open(m10, encoding='utf-8')); assert m['atlas'] == 'v0.10'
    m.update(atlas='v0.11', frozen_at='2026-11-10', previous_atlas_tag='atlas-v0.10')   # repository_snapshot and sources unchanged
    m['note'] = 'No source moved since atlas-v0.10: repository_snapshot and every source entry are copied unchanged from evidence/atlas/v0.10/source_manifest.json.'
    open(mout, 'w', encoding='utf-8').write(json.dumps(m, ensure_ascii=False, indent=1) + '\n')
    print(hashlib.sha256(cand).hexdigest(), len(cand), len(L))
if __name__ == '__main__': main()
