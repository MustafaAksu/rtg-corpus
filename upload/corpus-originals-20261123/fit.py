import numpy as np, subprocess, re, sys
sys.argv=['x']; exec(open('cm.py').read().split("for kv in")[0])
s3=np.sqrt(3)
ks=[-2,-1,-0.5,0.1,0.25,0.5,0.8,1,1.2,1.5,1.8,2.5,3,5,10]
rows=[]
for kv in ks:
    co,r=pq(kv); p,q=co
    D=(kv-2)*(kv**2-kv+1); g=(2*kv**2-3*kv+2)/(kv**2-kv+1)
    qpred=-(2/3)*(kv-1)**3/D - 1j*(2*s3/9)*g
    rows.append((kv,p,q,qpred,r))
    print(f"k={kv:6.2f} q={q:.8f} pred={qpred:.8f} |dq|={abs(q-qpred):.1e}  Imp/Imq={p.imag/q.imag:.6f}  Re p*D={p.real*D:.8f} resid={r:.0e}")
K=np.array([x[0] for x in rows]); Y=np.array([x[1].real*(x[0]-2)*(x[0]**2-x[0]+1) for x in rows])
for deg in (2,3,4):
    c=np.polyfit(K,Y,deg); print(deg,"coeffs",np.round(c,8),"maxerr",np.max(abs(np.polyval(c,K)-Y)))
