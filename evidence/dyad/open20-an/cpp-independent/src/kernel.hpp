#pragma once
#include "interval.hpp"
#include <vector>
#include <type_traits>

namespace dyad {
using Poly=std::vector<C>; // Coefficient boxes; one fixed (unknown) polynomial lies in them.
using Pair=std::array<C,2>;
using Matrix=std::array<std::array<C,2>,2>;

// Holomorphic first-order automatic differentiation in the independent variables x,d.
struct Jet {
    C v,dx,dd;
    Jet()=default;Jet(long n):v(n){}Jet(C x):v(std::move(x)){}
    Jet(C x,C a,C b):v(std::move(x)),dx(std::move(a)),dd(std::move(b)){}
};
inline Jet operator+(const Jet&a,const Jet&b){return {a.v+b.v,a.dx+b.dx,a.dd+b.dd};}
inline Jet operator-(const Jet&a,const Jet&b){return {a.v-b.v,a.dx-b.dx,a.dd-b.dd};}
inline Jet operator-(const Jet&a){return {-a.v,-a.dx,-a.dd};}
inline Jet operator*(const Jet&a,const Jet&b){return {a.v*b.v,a.dx*b.v+a.v*b.dx,a.dd*b.v+a.v*b.dd};}
inline Jet operator/(const Jet&a,const Jet&b){C inv=C(1)/b.v;return {a.v*inv,(a.dx-a.v*inv*b.dx)*inv,(a.dd-a.v*inv*b.dd)*inv};}
inline Jet exp(const Jet&a){C e=exp(a.v);return {e,e*a.dx,e*a.dd};}
inline Jet sin(const Jet&a){C s=sin(a.v),c=cos(a.v);return {s,c*a.dx,c*a.dd};}
inline Jet cos(const Jet&a){C c=cos(a.v),s=-sin(a.v);return {c,s*a.dx,s*a.dd};}

template<class V> std::array<V,2> raw_F(V z,V w) {
    // z,w are independent complex coordinates, not numerical conjugates.
    const V om(omega()),ob(omega_bar()),den=om-ob;
    V rho=(om*w-ob*z)/den, eta=(z-w)/den;
    for(int k=0;k<6;k++){
        V s=sin(eta),er=exp(rho);
        V r=rho-s,e=eta+er-V(1)-s;rho=std::move(r);eta=std::move(e);
    }
    return {rho+om*eta,rho+ob*eta};
}
template<class V> V polynomial(const Poly&p,const V&x){
    V y(0);for(auto it=p.rbegin();it!=p.rend();++it)y=y*x+V(*it);return y;
}
template<class V> std::array<V,2> lifted_F(const Poly&p,V x,V d){
    // This evaluator deliberately uses the full elementary map, not Taylor tails.
    if constexpr(std::is_same_v<V,C>){if(x.zero())throw Failure("lift input contains x=0");}
    else {if(x.v.zero())throw Failure("lift input contains x=0");}
    V w=polynomial(p,x)+x*x*d;auto f=raw_F(x,w);
    return {f[0],(f[1]-polynomial(p,f[0]))/(f[0]*f[0])};
}
struct Evaluation {Pair value;Matrix J;};
inline Evaluation evaluate(const Poly&p,const Pair&b){
    auto f=lifted_F(p,Jet(b[0],C(1),C(0)),Jet(b[1],C(0),C(1)));
    return {{f[0].v,f[1].v},{{{f[0].dx,f[0].dd},{f[1].dx,f[1].dd}}}};
}
inline Pair midpoint(const Pair&b){return {b[0].midpoint(),b[1].midpoint()};}
inline Pair mean_enclosure(const Poly&p,const Pair&b){
    Pair c=midpoint(b),h=lifted_F(p,c[0],c[1]);auto e=evaluate(p,b);
    Pair r=h;for(int i=0;i<2;i++)for(int k=0;k<2;k++)r[i]=r[i]+e.J[i][k]*(b[k]-c[k]);return r;
}
inline void contract_edge(const Poly&p,Pair&source,Pair&target){
    // Inclusion-only contractor. Does NOT establish existence or branch identity.
    // Integral mean value identity on a convex complex rectangle:
    // H(u)=H(c)+A(u-c), each A_ik in the interval enclosure of DH on source.
    Pair c=midpoint(source),h=lifted_F(p,c[0],c[1]);
    auto e=evaluate(p,source),atc=evaluate(p,c);
    for(int i=0;i<2;i++){
        C out=h[i];for(int k=0;k<2;k++)out=out+e.J[i][k]*(source[k]-c[k]);
        target[i]=intersect(target[i],out);
    }
    for(int i=0;i<2;i++){
        C a=atc.J[i][i].midpoint();if(a.zero())throw Failure("zero contractor pivot");
        int k=1-i;
        C correction=(target[i]-h[i]-e.J[i][k]*(source[k]-c[k])
                      -(e.J[i][i]-a)*(source[i]-c[i]))/a;
        source[i]=intersect(source[i],c[i]+correction);
    }
}
inline void contract_chain(const Poly&p,std::vector<Pair>&nodes,bool reverse,unsigned sweeps){
    if(nodes.size()<2)throw Failure("chain needs at least two nodes");
    auto edge=[&](size_t k){if(reverse)contract_edge(p,nodes[k+1],nodes[k]);else contract_edge(p,nodes[k],nodes[k+1]);};
    for(unsigned s=0;s<sweeps;s++){
        for(size_t k=0;k+1<nodes.size();k++)edge(k);
        for(size_t k=nodes.size()-1;k>0;k--)edge(k-1);
    }
}
inline Matrix point_inverse(const Matrix&a){
    C det=a[0][0]*a[1][1]-a[0][1]*a[1][0];
    if(det.zero())throw Failure("singular preconditioner candidate");
    Matrix c{{{(a[1][1]/det).midpoint(),(-a[0][1]/det).midpoint()},
              {(-a[1][0]/det).midpoint(),(a[0][0]/det).midpoint()}}};
    if((c[0][0]*c[1][1]-c[0][1]*c[1][0]).zero())throw Failure("rounded preconditioner singular");
    return c;
}
struct InverseWitness {bool included;I q;Pair image;};
inline InverseWitness inverse_box(const Poly&p,const Pair&centre,const std::array<I,2>&radius,const Pair&target){
    // B consists of two complex SQUARES, with exact point centres and positive halfwidths.
    Pair c=midpoint(centre);for(int i=0;i<2;i++)if(!positive(radius[i]))throw Failure("inverse radius not positive");
    Pair b{inflate(c[0],radius[0]),inflate(c[1],radius[1])};
    auto atc=evaluate(p,c),eb=evaluate(p,b);Matrix C0=point_inverse(atc.J),E;
    for(int i=0;i<2;i++)for(int j=0;j<2;j++){
        E[i][j]=C(i==j?1:0);for(int k=0;k<2;k++)E[i][j]=E[i][j]-C0[i][k]*eb.J[k][j];
    }
    Pair image=c;I q(0);
    for(int i=0;i<2;i++){
        I row(0);
        for(int j=0;j<2;j++){
            image[i]=image[i]+C0[i][j]*(target[j]-atc.value[j])+E[i][j]*(b[j]-c[j]);
            row=row+norm1(E[i][j])*radius[j].upper()/radius[i].upper();
        }
        if(less(q.hi,row.hi))q=row.upper();
    }
    bool ok=above(I(1),q)&&image[0].inside(b[0])&&image[1].inside(b[1]);
    // Banach on the real weighted infinity norm proves one preimage per target,
    // IN THIS BOX only. No identification with the selected sectorial inverse is implied.
    return {ok,q,image};
}
struct Disc {C centre;I radius;};
inline Disc enclosing_disc(const C&b){C c=b.midpoint();return {c,absup(b-c)};}
inline bool two_disc_test(const Disc&a,const Disc&b){
    if(mpfr_cmp_si(a.radius.lo.v,0)<0||mpfr_cmp_si(b.radius.lo.v,0)<0)throw Failure("negative disc radius");
    return above(abs2(a.centre-b.centre),sqr(a.radius+b.radius));
}
inline C pilot_a2(){
    C root3i(I(0),sqrt(I(3))),mu=C(I(-1)/I(2))-root3i*C(I(2)/I(3));
    C mubar=C(I(-1)/I(2))+root3i*C(I(2)/I(3));
    C c40=C(I(-1)/I(16))+root3i*C(I(7)/I(144));
    C d31=C(I(1)/I(3))-root3i*C(I(1)/I(9));
    C cc=C(I(-61)/I(2160))+root3i*C(I(43)/I(6480));
    C A=mubar-C(2)*mu,B=d31-C(2)*c40;
    C a=(-B-principal_sqrt(B*B-C(4)*A*cc))/(C(2)*A);
    if(!positive(a.im)) throw Failure("pilot radical did not select Im(a)>0");
    return a;
}
} // namespace dyad
