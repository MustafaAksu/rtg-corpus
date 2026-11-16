#define main core_main
#include "independent_core.cpp"
#undef main
#include <chrono>
#include <cstdio>
#include <cmath>
using namespace dyad;
long double toLD(const Z& z){ // z / 2^256 approx
    long double r = 0; Z a = az(z); int sgn = z<0?-1:1;
    // shift down to fit
    unsigned m = a==0?0:boost::multiprecision::msb(a);
    int sh = m>100? m-100:0; Z b = a>>sh; r = (long double)b.convert_to<long double>(); r = ldexpl(r, sh-(int)PREC); return sgn*r;
}
void pr(const char*n,const C&c){ printf("%s re[%.21Lg, %.21Lg] im[%.21Lg, %.21Lg] w=%.3Lg\n",n,toLD(c.re.l),toLD(c.re.h),toLD(c.im.l),toLD(c.im.h),toLD(c.re.h-c.re.l)+toLD(c.im.h-c.im.l)); }
int main(int argc,char**argv){ setvbuf(stdout,NULL,_IONBF,0); try {
    // 1. raw F at a complex point (rho,eta), value and d/drho
    C rho(I::rat(3,100),I::rat(1,100)), eta(I::rat(-2,100),I::rat(1,200));
    auto t0=std::chrono::steady_clock::now();
    State s=F({J(rho,C(1)),J(eta,C(0))});
    auto t1=std::chrono::steady_clock::now();
    pr("F.rho",s.a.v); pr("F.eta",s.b.v); pr("dFrho/drho",s.a.d); pr("dFeta/drho",s.b.d);
    printf("one F with jets: %.3f s\n", std::chrono::duration<double>(t1-t0).count());
    // 2. exp at the range edge
    C e8=exp_c(C(8)); pr("exp(8)",e8); printf("true exp(8)=%.21Lg\n", expl(8.0L));
    // 3. iterate raw F from a point: width growth
    State p{J(rho),J(eta)}; int n = argc>1? atoi(argv[1]):20;
    t0=std::chrono::steady_clock::now();
    for(int k=1;k<=n;++k){ p=F(p); if(k%10==0||k==1){ printf("k=%d ",k); pr("rho",p.a.v);} }
    t1=std::chrono::steady_clock::now();
    printf("%d F steps: %.2f s\n", n, std::chrono::duration<double>(t1-t0).count());
    // 4. nonlinear contractor witness test: f(d)=7(d-r)+(d-r)^2 on B(0,1/4), derivative 7+2(d-r) over B
    C root(I::rat(1,16),I::rat(-1,32)); Disk B(C(0),SCALE/4);
    auto f=[&](const C&d){ C u=d-root; return C(7)*u+u*u; };
    C fa=f(C(0)); C der=C(7)+C(2)*(B.box()-root);
    Z M=SCALE/100; Disk Dk=necessary_disk(B,fa,der,C(7),M);
    bool ok=true; long cnt=0;
    for(long a=-160;a<=160;++a)for(long b=-160;b<=160;++b){
        C x=root+C(I::rat(a,65536),I::rat(b,65536)); if(!contains_point(B,x)) continue;
        C fx=f(x); Z ux=au(fx.re), uy=au(fx.im); // |f(x)|<=M check (conservative: use lower)
        Z lx=al(fx.re), ly=al(fx.im);
        if(lx*lx+ly*ly<=M*M){ ++cnt; ok &= contains_point(Dk,x); }
    }
    printf("nonlinear contractor: %ld feasible grid points, all inside: %d, radius=%.4Lg\n",cnt,(int)ok,toLD(Dk.r));
    } catch(const std::exception&e){ printf("EXCEPTION: %s\n", e.what()); }
    return 0;
}
