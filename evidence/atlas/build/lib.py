import re
P='/home/claude/rtg-corpus/atlas/RTG_STATE_ATLAS.md'
class A:
    def __init__(s): s.t=open(P,encoding='utf-8').read(); s.log=[]
    def line(s,prefix,new,key=''):
        L=s.t.split('\n'); idx=[i for i,l in enumerate(L) if l.startswith(prefix)]
        assert len(idx)==1,(prefix,len(idx)); old=L[idx[0]]
        if new is None: del L[idx[0]]
        else: L[idx[0]]=new
        s.t='\n'.join(L); s.log.append((key,'line',prefix[:60]))
    def rep(s,old,new,key=''):
        n=s.t.count(old); assert n==1,(old[:80],n); s.t=s.t.replace(old,new); s.log.append((key,'rep',old[:60]))
    def after(s,prefix,newlines,key=''):
        L=s.t.split('\n'); idx=[i for i,l in enumerate(L) if l.startswith(prefix)]
        assert len(idx)==1,(prefix,len(idx)); L[idx[0]+1:idx[0]+1]=newlines if isinstance(newlines,list) else [newlines]
        s.t='\n'.join(L); s.log.append((key,'after',prefix[:60]))
    def save(s): open(P,'w',encoding='utf-8').write(s.t)
