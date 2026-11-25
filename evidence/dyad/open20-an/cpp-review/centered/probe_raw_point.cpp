#define main core_main
#include "independent_core.cpp"
#undef main
#include "ce_local.hpp"
#include <cstdio>
using namespace dyad; using namespace dyad::centered;
void out(const char*n,const C&c){ std::cout<<n<<" "<<c.re.l<<" "<<c.re.h<<" "<<c.im.l<<" "<<c.im.h<<"\n"; }
int main(){
  C rho(I::rat(3,100),I::rat(1,100)), eta(I::rat(-2,100),I::rat(1,200));
  Flow f=from_raw({rho,eta},{C(1),C(0)});
  for(int k=1;k<=334;++k){ f=advance(f);
    if(k==1||k==10||k==100||k==334){ State s=raw_readout(f); std::cout<<"k "<<k<<"\n"; out("rho",s.a.v); out("eta",s.b.v); out("drho",s.a.d); out("deta",s.b.d);} }
}
