import io,json,subprocess,sys,re
sys.path.insert(0,'.')
import importlib.util
spec=importlib.util.spec_from_file_location('eng','ng_migration_engine_v1.py'); eng=importlib.util.module_from_spec(spec); spec.loader.exec_module(eng)
FP0=json.load(open('fp1202.json'))
byline={b['line']:b['h'] for b in FP0['blocks']}
queue_h=byline[154]
mirror=[x for x in eng.INV if x['disposition']=='MIRROR-RECONCILED'][0]
def ranges(path):
    L=io.open(path,encoding='utf-8').read().split('\n')
    f=lambda p: next(i+1 for i,l in enumerate(L) if l.startswith('## '+p))
    return f'{f("§2")}:{f("§3")}', f'{f("§6")}:{f("§7")}'
def run(cmd): r=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8',errors='replace'); return r.returncode,r.stdout
res=[]
for K in range(1,len(eng.ORDER)+1):
    text,reg=eng.build(K)
    p=f'/tmp/mig_{K}.md'; io.open(p,'w',encoding='utf-8').write(text)
    s2,s6=ranges(p)
    run([sys.executable,'ng_state_fingerprint_v2_3.py','fingerprint',p,'--s2',s2,'--s6',s6])
    led={"reconciled":[],"tag_norm":[],"stop":[],"registry_conversion":[byline[n] for n in reg],"registry_only_inplace":[queue_h]}
    # HEADING-DEMOTION: derive, then admit only if the derived hash exists in the new file
    import hashlib
    nf=json.load(open(p.replace('.md','_fingerprint_v2.json'))); nhs={b['h'] for b in nf['blocks']}
    L0=eng.L; led['heading_demotion']=[]
    moved=[r for r in eng.HIER['modules'] if r['batch'] in set(eng.ORDER[:K])]
    for b in FP0['blocks']:
        if not L0[b['line']-1].startswith('#'): continue
        if not any(r['start']<=b['line']<r['end'] for r in moved): continue
        lines=[eng.demote(L0[b['line']-1])]+L0[b['line']:b['end']]
        body="\n".join(re.sub(r"[ \t]+"," ",x.strip()) for x in lines).strip()
        ah=hashlib.sha256(body.encode('utf-8')).hexdigest()
        if ah in nhs: led['heading_demotion'].append({"class":"HEADING-DEMOTION","base_line":b['line'],"before_h":b['h'],"after_h":ah})
        else: print(f"   !! heading-anchored block L{b['line']}: derived demoted hash NOT found in new file")
    if '§6.3a' in eng.ORDER[:K]:
        led['reconciled']=[{"discarded_h":mirror['h'],"retained_h":mirror['retained_twin_h']}]
    json.dump(led,open(f'/tmp/led_{K}.json','w'))
    rc,out=run([sys.executable,'ng_state_fingerprint_v2_3.py','compare','fp1202.json',p.replace('.md','_fingerprint_v2.json'),f'/tmp/led_{K}.json'])
    inv=[l for l in out.split('\n') if l.startswith('[')]
    fp_ok=all(('PASS' in l) for l in inv if 'INV-3' not in l)
    inv3=[l for l in inv if 'INV-3' in l][0]
    rcs,outs=run([sys.executable,'ng_migration_checks_v2_1.py','invS','RTG_NUMBER_GENESIS_DSN_v1_20_2.md',p,'NG_V1203_REVERSE_INVENTORY_v2.json','--mode','partial'])
    print(f"batch {K:2d} {eng.ORDER[K-1]:6} | FP INV-0/1/1b/2/4a/4b {'PASS' if fp_ok else 'FAIL'} | {inv3.split(']')[0]+']'} {inv3.split('(')[-1].rstrip(')')} §2 theorem blocks left | INV-S partial exit {rcs}")
    if not fp_ok: print("   ",[l for l in inv if 'FAIL' in l])
    if rcs: print("   ",[l for l in outs.split('\n') if 'FAIL' in l][:4])
    res.append(fp_ok and rcs==0)
print("ALL BATCHES CLEAN" if all(res) else "BATCH FAILURE")
