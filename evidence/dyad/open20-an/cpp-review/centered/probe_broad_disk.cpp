#define main core_main
#include "independent_core.cpp"
#undef main
#include "ce_local.hpp"
using namespace dyad; using namespace dyad::centered;
void out(const char*n,const C&c){ std::cout<<n<<" "<<c.re.l<<" "<<c.re.h<<" "<<c.im.l<<" "<<c.im.h<<"\n"; }
int main(int argc,char**argv){
  std::vector<C> phi{C(0),C(0),C(I::rat(1,2))};
  C x(I::rat(1,64),I::rat(1,128));
  Z r = cd(SCALE,Z(500));                       // radius ~2e-3, as in the co-owner's broad test
  Disk D(C(0),r);
  Flow f=from_lift(x,D,phi);
  for(int k=1;k<=334;++k) f=advance(f);
  State s=lifted_readout(f,phi);
  out("d334",s.b.v); out("dd334",s.b.d);
}
