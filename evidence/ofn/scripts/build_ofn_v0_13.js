// Deterministic OFN v0.13 maintenance builder; exact UTF-8 base, fixed line-addressed edit map.
// The build() core and sha256() were executed in the connector JS runtime; Node is only the CLI adapter.
function sha256(txt){
 const bin=unescape(encodeURIComponent(txt)),n=bin.length,m=Math.ceil((n+9)/64)*64,b=new Uint8Array(m);
 for(let i=0;i<n;i++)b[i]=bin.charCodeAt(i);b[n]=128;const bits=n*8;
 for(let j=0;j<8;j++)b[m-1-j]=Math.floor(bits/Math.pow(2,j*8))&255;
 const primes=[];for(let p=2;primes.length<64;p++){let ok=true;for(let d=2;d*d<=p;d++)if(p%d===0){ok=false;break;}if(ok)primes.push(p);}
 const frac=n=>(Math.floor((n-Math.floor(n))*4294967296)>>>0);
 const h=primes.slice(0,8).map(p=>frac(Math.sqrt(p))),k=primes.map(p=>frac(Math.cbrt(p))),w=new Uint32Array(64);
 const rotr=(n,r)=>(n>>>r)|(n<<(32-r));
 for(let pos=0;pos<m;pos+=64){
  for(let j=0;j<16;j++)w[j]=((b[pos+j*4]<<24)|(b[pos+j*4+1]<<16)|(b[pos+j*4+2]<<8)|b[pos+j*4+3])>>>0;
  for(let j=16;j<64;j++){let a=w[j-15],c=w[j-2];w[j]=(w[j-16]+(rotr(a,7)^rotr(a,18)^(a>>>3))+w[j-7]+(rotr(c,17)^rotr(c,19)^(c>>>10)))>>>0;}
  let [a,bb,c,d,e,f,g,hh]=h;
  for(let j=0;j<64;j++){const t1=(hh+(rotr(e,6)^rotr(e,11)^rotr(e,25))+((e&f)^(~e&g))+k[j]+w[j])>>>0,t2=((rotr(a,2)^rotr(a,13)^rotr(a,22))+((a&bb)^(a&c)^(bb&c)))>>>0;hh=g;g=f;f=e;e=(d+t1)>>>0;d=c;c=bb;bb=a;a=(t1+t2)>>>0;}
  const v=[a,bb,c,d,e,f,g,hh];for(let j=0;j<8;j++)h[j]=(h[j]+v[j])>>>0;
 }return h.map(x=>x.toString(16).padStart(8,"0")).join("");
}
function build(base,plan,hash){
 function req(x,m){if(!x)throw Error(m);}
 req(plan.schema==="ofn-stage1-line-addressed-v1","schema");
 req(hash(base)===plan.base_sha256,"base SHA-256");
 const original=base.split("\n"); let current=base,delta=0,last=0,log=[];
 const ids=new Set();
 for(const e of plan.edits){
  req(Number.isInteger(e.line)&&e.line>last&&e.line<=original.length,"ordered unique original line "+e.id);
  req(!ids.has(e.id),"duplicate edit id");ids.add(e.id);last=e.line;
  req(typeof e.old==="string"&&typeof e.new==="string"&&e.old!==e.new&&!e.old.includes("\n"),"payload "+e.id);
  req(original[e.line-1]===e.old,"immutable base anchor "+e.id);
  const a=current.split("\n"),i=e.line-1+delta;
  req(a[i]===e.old,"exact current anchor "+e.id);
  const before=hash(current);a.splice(i,1,...e.new.split("\n"));current=a.join("\n");delta+=e.new.split("\n").length-1;
  log.push({id:e.id,line:e.line,group:e.group,reason:e.reason,old_sha256:hash(e.old),new_sha256:hash(e.new),doc_sha256_before:before,doc_sha256_after:hash(current)});
 }
 return {candidate:current,log:{schema:plan.schema,base_sha256:hash(base),candidate_sha256:hash(current),edits:log}};
}
module.exports={sha256,build};
if(require.main===module){
 const fs=require("node:fs"); const [basePath,mapPath,outPath,logPath]=process.argv.slice(2);
 if(!basePath||!mapPath||!outPath||!logPath) throw Error("usage: node build_ofn_v0_13.js BASE MAP OUT LOG");
 if(sha256("abc")!=="ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad")throw Error("SHA self-test");
 const b=build(fs.readFileSync(basePath,"utf8"),JSON.parse(fs.readFileSync(mapPath,"utf8")),sha256);
 fs.writeFileSync(outPath,b.candidate);fs.writeFileSync(logPath,JSON.stringify(b.log,null,2)+"\n");
 console.log("BUILD PASS",b.log.edits.length,b.log.candidate_sha256);
}
