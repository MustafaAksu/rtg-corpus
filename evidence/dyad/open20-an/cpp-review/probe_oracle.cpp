#define main core_main
#include "independent_core.cpp"
#undef main
#include <cstdio>
using namespace dyad;
void out(const char*n,const I&i){ std::cout<<n<<" "<<i.l<<" "<<i.h<<"\n"; }
int main(){
    C rho(I::rat(3,100),I::rat(1,100)), eta(I::rat(-2,100),I::rat(1,200));
    State p{J(rho,C(1)),J(eta)};
    for(int k=1;k<=20;++k){ p=F(p); if(k==1||k==10||k==20){ std::cout<<"k "<<k<<"\n"; out("rr",p.a.v.re); out("ri",p.a.v.im); out("er",p.b.v.re); out("ei",p.b.v.im); out("dr",p.a.d.re);} }
}
