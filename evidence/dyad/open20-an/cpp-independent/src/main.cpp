#include "kernel.hpp"
#include <iostream>
#include <functional>
#include <iomanip>
using namespace dyad;

static int failures=0,checks=0;
static void test(const std::string&name,const std::function<bool()>&f){
    bool pass=false;std::string err;
    try{pass=f();}catch(const std::exception&e){err=e.what();}
    ++checks;if(!pass)++failures;
    std::cout<<"{\"test\":\""<<name<<"\",\"pass\":"<<(pass?"true":"false")
             <<",\"error\":\""<<err<<"\"}\n";
}
static bool rejects(const std::function<void()>&f){try{f();return false;}catch(const Failure&){return true;}}
static Pair test_point(){return {C(I(1)/I(32),I(1)/I(64)),C(I(1)/I(10000),I(-1)/I(20000))};}
static Poly test_polynomial(){Poly p(4);p[2]=pilot_a2();p[3]=(C(1)-C(I(0),sqrt(I(3))))*(C(I(1)/I(108))-p[2]/C(6));return p;}

int main(int argc,char**argv){
    try{
        if(argc==2 && std::string(argv[1])=="--help"){
            std::cout<<"dyad_cpp_kernel [--bits 128|256|512] [--sample-map]\n"
                     <<"SESSION kernel tests only. No 3c-b production mode.\n";return 0;
        }
        bool sample=false;
        for(int k=1;k<argc;k++){
            std::string a=argv[k];
            if(a=="--bits"&&k+1<argc){std::string b=argv[++k];size_t used=0;long n=std::stol(b,&used);
                if(used!=b.size()||n<64||n>4096)throw Failure("precision outside [64,4096]");
                precision=n;}
            else if(a=="--sample-map")sample=true;
            else throw Failure("unknown or incomplete argument");
        }
        std::cout<<"{\"status\":\"SESSION independent C++ kernel; not a jump certificate\",\"bits\":"<<precision
                 <<",\"mpfr\":\""<<mpfr_get_version()<<"\"}\n";
        if(sample){
            // Exact decimal inputs, not the DYAD comparison point or a claimed curve value.
            Pair z{C(I("0.8"),I("-0.4")),C(I("0.05"),I("0.07"))};auto f=raw_F(z[0],z[1]);
            std::cout<<"{\"z\":"<<f[0].str()<<",\"w\":"<<f[1].str()<<"}\n";
            auto e=evaluate(test_polynomial(),test_point());
            std::cout<<"{\"lift\":["<<e.value[0].str()<<","<<e.value[1].str()<<"],\"jacobian\":["
                     <<e.J[0][0].str()<<","<<e.J[0][1].str()<<","<<e.J[1][0].str()<<","<<e.J[1][1].str()<<"]}\n";
            mpfr_free_cache(); return 0;
        }
        test("directed_thirds",[]{return (I(1)/I(3)*I(3)).contains(I(1));});
        test("zero_division_refused",[]{return rejects([]{(void)(I(1)/inflate(I(0),I(1)));});});
        test("interval_square",[]{I a=inflate(I(0),I(2));I q=sqr(a);return q.contains(I(0))&&q.contains(I(4))&&!q.contains(I(-1));});
        test("periodic_trig_extremum",[]{return sin(pi()/I(2)).contains(I(1))&&cos(pi()).contains(I(-1));});
        test("trig_full_period",[]{I a=inflate(I(0),I(10));return sin(a).contains(I(-1))&&sin(a).contains(I(1));});
        test("exp_log_identity",[]{return exp(log(I(2))).contains(I(2));});
        test("pilot_branch",[]{C a=pilot_a2();return positive(a.im)&&above(a.re,I("0.02567"))&&above(I("0.02568"),a.re);});
        test("raw_origin_identity",[]{auto e=raw_F(Jet(C(0),C(1),C(0)),Jet(C(0),C(0),C(1)));
            return e[0].v.zero()&&e[1].v.zero()&&e[0].dx.contains(C(1))&&e[1].dd.contains(C(1))&&e[0].dd.zero()&&e[1].dx.zero();});
        test("lift_singularity_refused",[]{return rejects([]{(void)lifted_F(test_polynomial(),C(0),C(0));});});
        test("mean_value_contains_point_image",[]{auto p=test_polynomial();auto c=test_point();Pair b{inflate(c[0],I("1e-10")),inflate(c[1],I("1e-8"))};
            auto m=mean_enclosure(p,b),f=lifted_F(p,c[0],c[1]);return m[0].contains(f[0])&&m[1].contains(f[1]);});
        test("contractor_keeps_known_source",[]{auto p=test_polynomial();auto c=test_point();auto t=lifted_F(p,c[0],c[1]);
            Pair b{inflate(c[0],I("1e-10")),inflate(c[1],I("1e-8"))};contract_edge(p,b,t);
            return b[0].contains(c[0])&&b[1].contains(c[1]);});
        test("inverse_box_uniform_target",[]{auto p=test_polynomial();auto c=test_point();auto t=lifted_F(p,c[0],c[1]);
            t[0]=inflate(t[0],I("1e-15"));t[1]=inflate(t[1],I("1e-13"));
            auto w=inverse_box(p,c,{I("1e-10"),I("1e-8")},t);return w.included&&above(I(1),w.q);});
        test("inverse_box_rejects_far_target",[]{auto p=test_polynomial();auto c=test_point();auto t=lifted_F(p,c[0],c[1]);t[0]=t[0]+C(1);
            return !inverse_box(p,c,{I("1e-10"),I("1e-8")},t).included;});
        test("forward_chain_inclusion",[]{auto p=test_polynomial();auto c=test_point();std::vector<Pair>exact{c},b;
            for(int k=0;k<3;k++){auto a=exact.back();exact.push_back(lifted_F(p,a[0],a[1]));}
            for(const auto&a:exact)b.push_back({inflate(a[0],I("1e-12")),inflate(a[1],I("1e-10"))});
            b.front()[0]=c[0];contract_chain(p,b,false,2);
            for(size_t k=0;k<b.size();k++)if(!b[k][0].contains(exact[k][0])||!b[k][1].contains(exact[k][1]))return false;
            return true;});
        test("reverse_chain_inclusion",[]{auto p=test_polynomial();auto c=test_point();std::vector<Pair>exact{c},b;
            for(int k=0;k<3;k++){auto a=exact.back();exact.push_back(lifted_F(p,a[0],a[1]));}
            std::reverse(exact.begin(),exact.end());for(const auto&a:exact)b.push_back({inflate(a[0],I("1e-12")),inflate(a[1],I("1e-10"))});
            contract_chain(p,b,true,2);for(size_t k=0;k<b.size();k++)if(!b[k][0].contains(exact[k][0])||!b[k][1].contains(exact[k][1]))return false;
            return true;});
        test("strict_disjoint_discs",[]{return two_disc_test({C(0),I(1)},{C(3),I(1)});});
        test("tangent_discs_not_separated",[]{return !two_disc_test({C(0),I(1)},{C(2),I(1)});});
        test("overlapping_discs_not_separated",[]{return !two_disc_test({C(0),I(1)},{C(1),I(1)});});
        test("negative_radius_refused",[]{return rejects([]{(void)two_disc_test({C(0),I(-1)},{C(3),I(1)});});});
        test("rectangle_to_disc",[]{C b=inflate(C(0),I(1));auto d=enclosing_disc(b);return !above(I(2),sqr(d.radius));});
        std::cout<<"{\"checks\":"<<checks<<",\"failures\":"<<failures<<",\"status\":\"development tests only\"}\n";
        mpfr_free_cache(); return failures?1:0;
    }catch(const std::exception&e){std::cerr<<"INCONCLUSIVE: "<<e.what()<<"\n";return 2;}
}
