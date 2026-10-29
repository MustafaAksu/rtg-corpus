"""F5: an RTG-OFN identifier dropped from the live text by a declared history-removal (base and archive
modified consistently). The pre-fix tool cannot see RTG-OFN identifiers, so the removal passes as history.
Usage: python3 -I ofn_f5_fixture.py TOOL WORKTREE OUTDIR MAP"""
import hashlib, json, subprocess, sys, os
tool, wt, out, map_path = sys.argv[1:5]
base = open(os.path.join(wt, 'evidence/ofn/v0.11/stage1_intermediate.md'), encoding='utf-8').read()
cand = open(os.path.join(wt, 'dsn/RTG_ONTOLOGICAL_FOUNDATIONS.md'), encoding='utf-8').read()
mp = json.load(open(map_path, encoding='utf-8'))
anchor = '\n---\n\n<a id="ofn-artifacts-provenance"></a>'
assert base.count(anchor) == 1 and cand.count(anchor) == 1
para = '\n\nIn v0.10 the record `RTG-OFN-DEF-PHANTOM-TWO` was listed here.'
base2 = base.replace(anchor, para + anchor)
bp = os.path.join(out, 'F5_base.md'); open(bp, 'w', encoding='utf-8').write(base2)
m = json.loads(json.dumps(mp))
m['base_sha256'] = hashlib.sha256(base2.encode()).hexdigest()
m['archives'] = [{'name': 'stage1-intermediate', 'path': bp, 'sha256': m['base_sha256']}]
m['operations'].append({'id': 'F5', 'op': 'edit', 'class': 'history-removal', 'archive': ['stage1-intermediate'],
                        'old': para + anchor, 'new': anchor})
mpp = os.path.join(out, 'F5_map.json'); json.dump(m, open(mpp, 'w', encoding='utf-8'), ensure_ascii=False)
r = subprocess.run([sys.executable, '-I', tool, bp, os.path.join(wt, 'dsn/RTG_ONTOLOGICAL_FOUNDATIONS.md'), mpp], capture_output=True, text=True, cwd=wt)
fails = [l for l in r.stdout.splitlines() if l.startswith('FAIL')]
print(f'F5_ofn_rid_removed_as_history: exit {r.returncode} ->', 'CAUGHT' if r.returncode == 1 else 'NOT CAUGHT', '|', '; '.join(f[:110] for f in fails[:2]))
