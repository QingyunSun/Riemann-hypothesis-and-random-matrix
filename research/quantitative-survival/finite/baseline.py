from flint import arb,acb,ctx
from pathlib import Path
import json,time
from base import summary_fibres,is_survivor
D=Path(__file__).parent
ctx.prec=160;n=11;m=22
allsets=[s for family in summary_fibres(n).values() for s in family]
roots=[acb(arb(j)/n).exp_pi_i() for j in range(m)]
heat=[(arb(85)/84)**(j*(n-j)) for j in range(n+1)]
factors=[4*(arb(k)/m*arb.pi()).sin()**2 for k in range(m)]
total=arb(0);survive=arb(0);count=0
lift={r:arb(0) for r in (2,3,4)}
t=time.time()
for S in allsets:
 size=len({tuple(sorted((f*i+j)%m for i in S)) for f in (-1,1) for j in range(m)})
 q=arb(size)/m**n
 for i,x in enumerate(S):
  for y in S[i+1:]:q*=factors[y-x]
 total+=q
 for r in lift:lift[r]+=size*(q/size)**r
 if is_survivor(S,roots,heat):survive+=q;count+=1
assert total.contains(1)
out={'orbit_count':len(allsets),'surviving_orbit_count':count,'original_total_mass':str(total),'ACUE_survival':str(survive),'full_lift_support_mass':{str(r):str(v) for r,v in lift.items()},'seconds':time.time()-t}
print(json.dumps(out,indent=2));(D/'baseline.json').write_text(json.dumps(out,indent=2))
