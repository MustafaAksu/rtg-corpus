#pragma once
// SESSION development code. Directed MPFR endpoints; no Arb or Python dependency.
#include <mpfr.h>
#include <algorithm>
#include <array>
#include <stdexcept>
#include <string>
#include <utility>

namespace dyad {
inline mpfr_prec_t precision = 256; // Set once, before creating any interval.
struct Failure : std::runtime_error { using std::runtime_error::runtime_error; };
struct Real {
    mpfr_t v;
    Real() { mpfr_init2(v, precision); mpfr_set_si(v, 0, MPFR_RNDN); }
    Real(const Real& x): Real() { mpfr_set(v, x.v, MPFR_RNDN); }
    Real(Real&& x) noexcept: Real() { mpfr_swap(v, x.v); }
    Real& operator=(const Real& x) { if(this!=&x) mpfr_set(v,x.v,MPFR_RNDN); return *this; }
    Real& operator=(Real&& x) noexcept { if(this!=&x) mpfr_swap(v,x.v); return *this; }
    ~Real() { mpfr_clear(v); }
};
inline bool less(const Real& a,const Real& b){return mpfr_cmp(a.v,b.v)<0;}
inline std::string decimal(const Real& x, mpfr_rnd_t rnd) {
    if(!mpfr_number_p(x.v)) throw Failure("nonfinite print endpoint");
    if(mpfr_zero_p(x.v)) return "0";
    mpfr_exp_t e=0; char *p=mpfr_get_str(nullptr,&e,10,48,x.v,rnd);
    if(!p) throw Failure("MPFR string allocation");
    std::string s(p); mpfr_free_str(p); std::string sign;
    if(s.front()=='-'){sign="-";s.erase(s.begin());}
    return sign+s.substr(0,1)+"."+s.substr(1)+"e"+std::to_string(e-1);
}
struct I {
    Real lo,hi;
    I()=default;
    I(long n){mpfr_set_si(lo.v,n,MPFR_RNDD);mpfr_set_si(hi.v,n,MPFR_RNDU);}
    explicit I(const std::string& s){
        if(mpfr_set_str(lo.v,s.c_str(),10,MPFR_RNDD)||mpfr_set_str(hi.v,s.c_str(),10,MPFR_RNDU))
            throw Failure("invalid decimal");
        check();
    }
    I(Real a,Real b):lo(std::move(a)),hi(std::move(b)){check();}
    void check() const {
        if(!mpfr_number_p(lo.v)||!mpfr_number_p(hi.v)||less(hi,lo)) throw Failure("invalid/nonfinite interval");
    }
    bool zero()const{return mpfr_cmp_si(lo.v,0)<=0 && mpfr_cmp_si(hi.v,0)>=0;}
    bool contains(const I& a)const{return !less(a.lo,lo)&&!less(hi,a.hi);}
    bool inside(const I& a)const{return less(a.lo,lo)&&less(hi,a.hi);}
    I midpoint()const{Real m;mpfr_add(m.v,lo.v,hi.v,MPFR_RNDN);mpfr_div_ui(m.v,m.v,2,MPFR_RNDN);return I(m,m);}
    I upper()const{return I(hi,hi);}
    std::string str()const{return "["+decimal(lo,MPFR_RNDD)+","+decimal(hi,MPFR_RNDU)+"]";}
};
inline I operator+(const I&a,const I&b){I c;mpfr_add(c.lo.v,a.lo.v,b.lo.v,MPFR_RNDD);mpfr_add(c.hi.v,a.hi.v,b.hi.v,MPFR_RNDU);c.check();return c;}
inline I operator-(const I&a,const I&b){I c;mpfr_sub(c.lo.v,a.lo.v,b.hi.v,MPFR_RNDD);mpfr_sub(c.hi.v,a.hi.v,b.lo.v,MPFR_RNDU);c.check();return c;}
inline I operator-(const I&a){I c;mpfr_neg(c.lo.v,a.hi.v,MPFR_RNDD);mpfr_neg(c.hi.v,a.lo.v,MPFR_RNDU);return c;}
inline I operator*(const I&a,const I&b){
    std::array<Real,4> l,h;const Real *aa[]={&a.lo,&a.hi},*bb[]={&b.lo,&b.hi};
    for(int i=0;i<2;i++)for(int j=0;j<2;j++){
        mpfr_mul(l[2*i+j].v,aa[i]->v,bb[j]->v,MPFR_RNDD);
        mpfr_mul(h[2*i+j].v,aa[i]->v,bb[j]->v,MPFR_RNDU);
    }
    return I(*std::min_element(l.begin(),l.end(),less),*std::max_element(h.begin(),h.end(),less));
}
inline I inverse(const I&a){
    if(a.zero())throw Failure("division interval contains zero");
    I c,one(1);mpfr_div(c.lo.v,one.lo.v,a.hi.v,MPFR_RNDD);mpfr_div(c.hi.v,one.hi.v,a.lo.v,MPFR_RNDU);c.check();return c;
}
inline I operator/(const I&a,const I&b){return a*inverse(b);}
inline I sqr(const I&a){
    Real l,h,l2,h2;mpfr_mul(l.v,a.lo.v,a.lo.v,MPFR_RNDD);mpfr_mul(h.v,a.lo.v,a.lo.v,MPFR_RNDU);
    mpfr_mul(l2.v,a.hi.v,a.hi.v,MPFR_RNDD);mpfr_mul(h2.v,a.hi.v,a.hi.v,MPFR_RNDU);
    if(a.zero())mpfr_set_si(l.v,0,MPFR_RNDN);else if(less(l2,l))l=l2;
    if(less(h,h2)) h=h2;
    return I(l,h);
}
inline I absup(const I&a){Real l,h;mpfr_abs(l.v,a.lo.v,MPFR_RNDU);mpfr_abs(h.v,a.hi.v,MPFR_RNDU);if(less(l,h))l=h;return I(l,l);}
inline I intersect(const I&a,const I&b){return I(less(a.lo,b.lo)?b.lo:a.lo,less(a.hi,b.hi)?a.hi:b.hi);}
inline I hull(const I&a,const I&b){return I(less(a.lo,b.lo)?a.lo:b.lo,less(a.hi,b.hi)?b.hi:a.hi);}
inline bool positive(const I&a){return mpfr_cmp_si(a.lo.v,0)>0;}
inline bool above(const I&a,const I&b){return less(b.hi,a.lo);}
inline I exp(const I&a){I r;mpfr_exp(r.lo.v,a.lo.v,MPFR_RNDD);mpfr_exp(r.hi.v,a.hi.v,MPFR_RNDU);r.check();return r;}
inline I log(const I&a){if(!positive(a))throw Failure("log domain");I r;mpfr_log(r.lo.v,a.lo.v,MPFR_RNDD);mpfr_log(r.hi.v,a.hi.v,MPFR_RNDU);r.check();return r;}
inline I sqrt(const I&a){if(mpfr_cmp_si(a.lo.v,0)<0)throw Failure("sqrt domain");I r;mpfr_sqrt(r.lo.v,a.lo.v,MPFR_RNDD);mpfr_sqrt(r.hi.v,a.hi.v,MPFR_RNDU);r.check();return r;}
inline I atan(const I&a){I r;mpfr_atan(r.lo.v,a.lo.v,MPFR_RNDD);mpfr_atan(r.hi.v,a.hi.v,MPFR_RNDU);r.check();return r;}
inline I pi(){I r;mpfr_const_pi(r.lo.v,MPFR_RNDD);mpfr_const_pi(r.hi.v,MPFR_RNDU);return r;}
inline I inflate(const I&a,const I&r){if(mpfr_cmp_si(r.lo.v,0)<0)throw Failure("negative radius");return I((a-r.upper()).lo,(a+r.upper()).hi);}
inline I sincos_real(const I&a,bool cosine){
    I m=a.midpoint(),r=absup(a-m),v;
    auto fn=cosine?mpfr_cos:mpfr_sin;fn(v.lo.v,m.lo.v,MPFR_RNDD);fn(v.hi.v,m.hi.v,MPFR_RNDU);
    I unit;mpfr_set_si(unit.lo.v,-1,MPFR_RNDN);mpfr_set_si(unit.hi.v,1,MPFR_RNDN);
    return intersect(inflate(v,r),unit);
}
inline I sin(const I&a){return sincos_real(a,false);}
inline I cos(const I&a){return sincos_real(a,true);}
inline I sinh(const I&a){I r;mpfr_sinh(r.lo.v,a.lo.v,MPFR_RNDD);mpfr_sinh(r.hi.v,a.hi.v,MPFR_RNDU);r.check();return r;}
inline I cosh(const I&a){
    I l,h;mpfr_cosh(l.lo.v,a.lo.v,MPFR_RNDD);mpfr_cosh(l.hi.v,a.lo.v,MPFR_RNDU);
    mpfr_cosh(h.lo.v,a.hi.v,MPFR_RNDD);mpfr_cosh(h.hi.v,a.hi.v,MPFR_RNDU);
    I r=hull(l,h);if(a.zero())mpfr_set_si(r.lo.v,1,MPFR_RNDN);return r;
}
struct C {
    I re,im;
    C()=default;C(long n):re(n),im(0){}C(I r,I i=I(0)):re(std::move(r)),im(std::move(i)){}
    bool zero()const{return re.zero()&&im.zero();}
    bool contains(const C&x)const{return re.contains(x.re)&&im.contains(x.im);}
    bool inside(const C&x)const{return re.inside(x.re)&&im.inside(x.im);}
    C midpoint()const{return C(re.midpoint(),im.midpoint());}
    std::string str()const{return "{\"re\":"+re.str()+",\"im\":"+im.str()+"}";}
};
inline C operator+(const C&a,const C&b){return C(a.re+b.re,a.im+b.im);}
inline C operator-(const C&a,const C&b){return C(a.re-b.re,a.im-b.im);}
inline C operator-(const C&a){return C(-a.re,-a.im);}
inline C operator*(const C&a,const C&b){return C(a.re*b.re-a.im*b.im,a.re*b.im+a.im*b.re);}
inline C operator/(const C&a,const C&b){I q=sqr(b.re)+sqr(b.im);return C((a.re*b.re+a.im*b.im)/q,(a.im*b.re-a.re*b.im)/q);}
inline C intersect(const C&a,const C&b){return C(intersect(a.re,b.re),intersect(a.im,b.im));}
inline C inflate(const C&a,const I&r){return C(inflate(a.re,r),inflate(a.im,r));}
inline I abs2(const C&a){return sqr(a.re)+sqr(a.im);}
inline I absup(const C&a){return sqrt(abs2(a)).upper();}
inline I norm1(const C&a){return absup(a.re)+absup(a.im);}
inline C exp(const C&a){I e=exp(a.re);return C(e*cos(a.im),e*sin(a.im));}
inline C sin(const C&a){return C(sin(a.re)*cosh(a.im),cos(a.re)*sinh(a.im));}
inline C cos(const C&a){return C(cos(a.re)*cosh(a.im),-sin(a.re)*sinh(a.im));}
inline C principal_sqrt(const C&a){
    I u=sqrt((sqrt(abs2(a))+a.re)/I(2));if(!positive(u))throw Failure("sqrt chart not supported");
    return C(u,a.im/(I(2)*u));
}
inline C omega(){return C(I(-1)/I(2),sqrt(I(3))/I(2));}
inline C omega_bar(){return C(I(-1)/I(2),-sqrt(I(3))/I(2));}
} // namespace dyad
