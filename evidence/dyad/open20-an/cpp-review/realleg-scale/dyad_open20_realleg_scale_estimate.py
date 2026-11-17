import sys, time; sys.path.insert(0,'evidence/dyad/scripts')
from flint import acb, arb, ctx
import dyad_open20_an_stage3c_lib as L
ctx.dps = 400
K = L.Consts(); t0=time.time(); a = L.coefficients(K, 40); print('coeffs %.1fs' % (time.time()-t0), flush=True)
ctx.dps = 80
K = L.Consts(); a=[acb(x.mid()) for x in a]
TAU = L.tau_coefficients(); TB = L.Tube(K, TAU, 0)
OM, OMB, DEN = K.OM, K.OMB, K.DEN
def phi(x): 
    s=acb(0)
    for c in reversed(a): s=s*x+c
    return s
def dphi(x):
    s=acb(0)
    for k in range(len(a)-1,0,-1): s=s*x+k*a[k]
    return s
def T(r,e,dr,de):
    s=e.sin(); c=e.cos(); ex=r.exp()
    return r-s, e+ex-1-s, dr-c*de, de+ex*dr-c*de
def run(d0, n):
    x = acb('0.4')*(acb(0,1)*arb.pi()/6).exp()/K.c
    z, w = x, phi(x)+x*x*d0; dz, dw = acb(0), x*x
    out=[]
    for k in range(1,n+1):
        e=(z-w)/DEN; r=z-OM*e; de=(dz-dw)/DEN; dr=dz-OM*de
        for _ in range(6): r,e,dr,de = T(r,e,dr,de)
        z=acb((r+OM*e).mid()); w=acb((r+OMB*e).mid()); dz=acb((dr+OM*de).mid()); dw=acb((dr+OMB*de).mid())
        d=(w-phi(z))/(z*z); dd=((dw-dphi(z)*dz)*z*z-(w-phi(z))*2*z*dz)/(z**4)
        out.append((z,d,dd))
    return out
R0 = L.R_upper(TB, acb('0.4')*(acb(0,1)*arb.pi()/6).exp()/K.c)
print('R(xi*) =', R0.str(5))
res = run(acb(0), 334)
for k in (1,2,3,5,10,20,50,100,200,334):
    z,d,dd = res[k-1]; xi=K.c*z
    Rk = L.R_upper(TB, z)
    rho = Rk/(abs(dd)*R0)
    print('k=%3d |xi|=%.4f arg/pi=%.4f |d_k|=%.3e |b_k|=%.3e R_k=%.3e  R_k/(|b_k| R*)=%.3e' % (k, float(abs(xi).mid()), float((xi.arg()/arb.pi()).mid()), float(abs(d).mid()), float(abs(dd).mid()), float(Rk), float(rho.mid())))
print('--- variation over the fibre |d0| <= 0.002 (12 boundary points) ---')
import cmath
for n in (1,2,5,10,20):
    bs=[]; xs=[]
    for j in range(12):
        d0 = acb('0.002')*(acb(0,1)*arb.pi()*j/6).exp()
        z,d,dd = run(d0, n)[-1]; bs.append(dd); xs.append(K.c*z)
    z0,d00,b0 = res[n-1]
    vb = max(float(abs(b-b0).mid()) for b in bs); vx = max(float(abs(x-K.c*z0).mid()) for x in xs)
    print('n=%2d |b(0)|=%.3e max|b(d)-b(0)|=%.3e (ratio %.3f) max|xi(d)-xi(0)|=%.3e' % (n, float(abs(b0).mid()), vb, vb/float(abs(b0).mid()), vx))
