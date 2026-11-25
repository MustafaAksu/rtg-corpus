"""Fixtures for the two check_compaction.py gaps reported in the OFN v0.11 release record §7.
Usage: python3 -I ofn_gap_fixtures.py TOOL WORKTREE OUTDIR
Each fixture changes the candidate and the declared operation consistently (re-derivation still exact)
and recomputes candidate_sha256, so only the targeted rule can catch it."""
import hashlib, json, subprocess, sys, os
tool, wt, out = sys.argv[1:4]
map_path = sys.argv[4] if len(sys.argv) > 4 else os.path.join(wt, 'evidence/ofn/v0.11/movement_map.json')
base = os.path.join(wt, 'evidence/ofn/v0.11/stage1_intermediate.md')
cand = open(os.path.join(wt, 'dsn/RTG_ONTOLOGICAL_FOUNDATIONS.md'), encoding='utf-8').read()
mp = json.load(open(map_path, encoding='utf-8'))
def run(name, c, m):
    cp, mpp = os.path.join(out, name + '.md'), os.path.join(out, name + '.json')
    open(cp, 'w', encoding='utf-8').write(c)
    m = json.loads(json.dumps(m)); m['candidate_sha256'] = hashlib.sha256(c.encode()).hexdigest()
    json.dump(m, open(mpp, 'w', encoding='utf-8'), ensure_ascii=False)
    r = subprocess.run([sys.executable, '-I', tool, base, cp, mpp], capture_output=True, text=True, cwd=wt)
    fails = [l for l in r.stdout.splitlines() if l.startswith('FAIL')]
    print(f'{name}: exit {r.returncode} ->', 'CAUGHT' if r.returncode == 1 else 'NOT CAUGHT', '|', (fails[0][:150] if fails else ''))
def inject_in_appendix_c(token):
    op = next(o for o in mp['operations'] if o['id'] == 'S2-T')
    anchor = op['new'].split('\n')[0]           # the new Appendix C heading line
    new2 = op['new'].replace(anchor + '\n', anchor + '\n\nRecord names ' + token + '.\n', 1)
    m = json.loads(json.dumps(mp)); next(o for o in m['operations'] if o['id'] == 'S2-T')['new'] = new2
    assert cand.count(op['new']) == 1
    return cand.replace(op['new'], new2), m
run('baseline', cand, mp)
c, m = inject_in_appendix_c('`RTG-OFN-DEF-PHANTOM`'); run('GAP1_ofn_rid_phantom_in_history', c, m)
c, m = inject_in_appendix_c('`DYAD-THM-PHANTOM`');   run('GAP2_dyad_rid_phantom_in_history', c, m)
# F3: drop the only live mention of an RTG-OFN RID that appears in a replaced §12 section (via its 'new' pointer)
import re
for oid in ('S2-S1','S2-S2','S2-S5'):
    o = next(x for x in mp['operations'] if x['id']==oid)
    print(oid, 'new pointer RIDs:', sorted(set(re.findall(r'RTG-OFN-[A-Z0-9-]+', o['new']))))
# F4: a source hash deleted (not relocated): remove one relocated hash from the new Appendix C
op = next(o for o in mp['operations'] if o['id']=='S2-T')
h = '58e2dec5…3610'
if h in op['new']:
    new2 = op['new'].replace(h, 'XXXXXXXX…XXXX', 1)
    m = json.loads(json.dumps(mp)); next(o for o in m['operations'] if o['id']=='S2-T')['new'] = new2
    run('F4_history_hash_deleted', cand.replace(op['new'], new2), m)
# GAP1b: an RTG-OFN RID dropped from the live text by a declared history-removal
s1 = open(base, encoding='utf-8').read()
target = 'RTG-OFN-ALG-STAR-TOKEN-SHIFT'
lines = [l for l in cand.split('\n') if target in l and not l.startswith('`[')]
print('candidate lines naming', target, ':', len(lines))
