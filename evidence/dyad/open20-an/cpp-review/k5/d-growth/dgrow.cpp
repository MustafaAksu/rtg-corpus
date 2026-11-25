// [SESSION] owner diagnostic: growth of the whole-disc tangent enclosure D_k with k,
// against sampled point derivatives on the disc boundary. Not a bound.
#define DYAD_K5_NO_MAIN
#include "k5.cpp"
using namespace dyad; using namespace dyad::centered;
int main(int argc,char**argv){
  if(argc!=4){std::cerr<<"usage: dgrow TRANSFER FRONTIER676 NBOX\n";return 64;}
  const Data data=read_data(argv[1]); f1::ForwardTube tube(data.c);
  std::ifstream f(argv[2]); std::string line; std::getline(f,line);
  std::vector<C> boxes; while(std::getline(f,line)){std::istringstream in(line);std::string id;int dep;Z a,b,c,d;in>>id>>dep>>a>>b>>c>>d;boxes.push_back(C(I(a,b),I(c,d)));}
  size_t n=std::stoul(argv[3]); size_t step=boxes.size()/n;
  auto dbl=[](const Z&z){return static_cast<double>(z)/std::pow(2.0,256);};
  std::cout<<"box k r |b| D_encl D_sampled ratio Dr/|b|\n";
  for(size_t j=0;j<n;++j){
    Disk di=ball(boxes[j*step]);
    for(int k=1;k<=5;++k){
      State whole=f2::iter(tube.at_start(),di,data.phi,k);
      State point=f2::iter(tube.at_start(),Disk(di.c,0),data.phi,k);
      C slope=mid(point.b.d); Z D=norm_upper(whole.b.d-slope);
      double Ds=0;
      for(int t=0;t<8;++t){
        static const int dx[8]={1,-1,0,0,1,-1,1,-1},dy[8]={0,0,1,-1,1,1,-1,-1};
        Z rr=di.r; if(t>=4) rr=rr*7/10;
        C p(I(di.c.re.l+dx[t]*rr,di.c.re.l+dx[t]*rr),I(di.c.im.l+dy[t]*rr,di.c.im.l+dy[t]*rr));
        State q=f2::iter(tube.at_start(),Disk(p,0),data.phi,k);
        Ds=std::max(Ds,dbl(norm_upper(mid(q.b.d)-slope)));
      }
      double lb=dbl(norm_lower(slope)), Dd=dbl(D), r=dbl(di.r);
      std::cout<<j<<" "<<k<<" "<<r<<" "<<lb<<" "<<Dd<<" "<<Ds<<" "<<Dd/Ds<<" "<<Dd*r/lb<<"\n"<<std::flush;
    }
  }
}
