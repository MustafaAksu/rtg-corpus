import mpmath as mp
mp.mp.dps=50; SQ3=mp.sqrt(3)
def Tmap(p):
    r,e=p; return (r-mp.sin(e), e+(mp.e**r-1)-mp.sin(e))
def wrap(a): return mp.fmod(a+mp.pi,2*mp.pi)-mp.pi
def Q(p):
    r,e=p; w=wrap(e); return r*r-r*w+w*w
def Th(p):
    r,e=p; w=wrap(e); return mp.atan2(SQ3*w,2*r-w)
def orb(s,n):
    o=[s];p=s
    for _ in range(n): p=Tmap(p); o.append(p)
    return o
def gaps(o, th0):
    th=[Th(p) for p in o]; phi=[th[0]]
    for i in range(1,len(th)): phi.append(phi[-1]+wrap(th[i]-th[i-1]))
    s=1 if phi[-1]>phi[0] else -1
    cr=[]
    for i in range(len(phi)-1):
        a,b=s*(phi[i]-th0), s*(phi[i+1]-th0)
        k=mp.floor(a/(2*mp.pi))
        if b>=(k+1)*2*mp.pi: cr.append(i+1)
    return [cr[i+1]-cr[i] for i in range(len(cr)-1)]

print("=== A. section-independence: many sections Theta_0, small-amplitude seeds ===")
seeds=[(mp.mpf("0.010"),mp.mpf("0.004")),(mp.mpf("-0.008"),mp.mpf("0.011")),(mp.mpf("0.013"),mp.mpf("0.013"))]
allg=set()
for s in seeds:
    o=orb(s,300)
    for k in range(12):
        th0=mp.mpf(k)*2*mp.pi/12
        g=gaps(o,th0); allg|=set(g)
print("distinct return gaps over 12 sections x 3 seeds:", sorted(allg))

print("=== B. mean rotation per primitive step vs Q (limit pi/3 = %s) ===" % mp.nstr(mp.pi/3,8))
for s in [(mp.mpf("0.01"),mp.mpf("0.004")),(mp.mpf("0.1"),mp.mpf("0.07")),(mp.mpf("0.45"),mp.mpf("0.3")),(mp.mpf("0.8"),mp.mpf("-0.5"))]:
    o=orb(s,60); th=[Th(p) for p in o]
    inc=[wrap(th[i+1]-th[i]) for i in range(len(th)-1)]
    m=sum(inc[:12])/12
    print(f"  Q0={mp.nstr(Q(o[0]),4):>10}  mean rot (first 12 steps) = {mp.nstr(m,10)}  rot.number = {mp.nstr(m/(2*mp.pi),8)}")

print("=== C. asymptotic tail: gap word deep in the contracted regime ===")
for s in [(mp.mpf("0.8"),mp.mpf("-0.5")),(mp.mpf("1.1"),mp.mpf("0.75")),(mp.mpf("-0.9"),mp.mpf("0.6"))]:
    o=orb(s,900); g=gaps(o,mp.mpf(0))
    print(f"  Q0={mp.nstr(Q(o[0]),4):>8} -> Qend={mp.nstr(Q(o[-1]),4):>10}  last-40 gaps distinct={sorted(set(g[-40:]))}")
