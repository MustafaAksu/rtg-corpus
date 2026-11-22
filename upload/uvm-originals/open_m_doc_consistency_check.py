"""open_m_doc_consistency_check.py — verifies that every result/lemma/candidate
referenced in the addenda, §5 ledger, or changelog has a §6 body. [ENG, v0.5]"""
import re,sys
p=sys.argv[1] if len(sys.argv)>1 else 'RTG_OPEN_M_DSN_v0_5_candidate.md'
s=open(p).read()
referenced=set(re.findall(r'\b(R1[01]|R[1-9]|LEM-M-CENTRAL|CAND-M-BCH|HYP-M-FRACTURE|THM-M-LOCK|HYP-IDENT)\b',s))
ok=True
for r in sorted(referenced):
    # a §6 body = a bold header line containing the name with an em-dash title
    if r in ('HYP-IDENT',):   # registered in §2, not §6
        body=bool(re.search(r'\*\*HYP-IDENT —',s))
    elif r=='THM-M-LOCK':
        body=bool(re.search(r'\*\*R8 — THM-M-LOCK',s))
    else:
        body=bool(re.search(r'\*\*'+re.escape(r)+r' ?[—-]',s))
    print(f"[{'PASS' if body else 'FAIL'}] {r}: body present")
    ok&=body
print("DOC CONSISTENCY:","PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
