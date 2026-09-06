"""Exact arithmetic implications of the refined fixed-minorant mass bound.
This replays only the printed scalar endpoints, not the original 149 integrals.
"""
from fractions import Fraction as F
from pathlib import Path
from itertools import permutations,combinations
import json
BASE=Path(__file__).parent
kap=json.loads((BASE/'minorant_mass.json').read_text())
knew=F(kap['upper_numerator'],kap['common_denominator']);kold=F(1,50000)
rho=F(2624989,10**7);K=F(17,50);lam=F(1,125)
Iminus=F(23685317816,10**24);Iplus=F(23685317890,10**24);Jminus=F(90248755123,10**24)
groups={'outer_order2':38927522,'outer_order5/2':622829241,'inner_old_order2':55254,'inner_old_order5/2':435544,'inner_new_order2':1405159,'inner_new_order5/2':32422390}
assert sum(groups.values())==696075110
L=Iminus*F(sum(groups.values()),10**12)
margin=rho*(Jminus-L)/Iplus-1

def coefs(k):
 m=1-k;a=m*m-m*lam;b=(1-m/lam)*k*K
 return a,b,a+b,1-a-b

a0,b0,c0,d0=coefs(kold);a1,b1,c1,d1=coefs(knew)
assert c1>c0 and b1>b0 and d1<d0
# Each old outer cap multiplier h is base1, enlarged c0, or tailabs(b0).
# The new multiplier is <= r times the old one, with r=c1/c0.
r=c1/c0
outer=Iminus*F(groups['outer_order2']+groups['outer_order5/2'],10**12)
inner_old=Iminus*F(groups['inner_old_order2']+groups['inner_old_order5/2'],10**12)
inner_new=Iminus*F(groups['inner_new_order2']+groups['inner_new_order5/2'],10**12)
newloss_upper=r*outer+(d1/d0)*inner_old+((1-b1)/(1-b0))*inner_new
# New J >= old J since Jplus,Jtail>=0.
newmargin_floor=rho*(Jminus-newloss_upper)/Iplus-1
# Same fixed trial and lambda: Jplus+Jtail <= Jfull <=4I.
cap_gain_upper=4*rho*max(c1-c0,b1-b0)
# Maximum possible net gain also includes recovering all old restoration cost.
net_gain_upper=cap_gain_upper+rho*L/Iplus
# The coefficient 12/5 in b <=(12/5) N2 is attained on this open chamber.
a=tuple(F(n,1000) for n in [198,199,200,201,202]);A=F(40481,100000);B=1-A;xi=F(19038,100000);u=F(23848,100000)
bone=btwo=0
for p in permutations(a):
 p1,p2,p3,p4,m5=p
 bone+=int(xi<=p4<p3<p2<p1<A and p1+p2<A and p2+p3+p4>B and m5>=p4)
 p2,p3,p4,p5,p6=p
 btwo+=int(all(xi<=v<=u for v in p) and p2>p3 and p4>p3 and p2+p4<A and p2+p3+p5>B and p6>=p5)
npairs=sum(x+y<A for x,y in combinations(a,2))
assert (bone,btwo,npairs)==(4,20,10)

def val(x):return {'exact':str(x),'float':float(x)}
out={'status':'EXACT_SCALAR_REPLAY_ONLY_NOT_FRESH_149_INTEGRAL_CERTIFICATE','published_margin':val(margin),'published_cap_quotient':val(rho*Jminus/Iplus),'published_loss_ratio':val(L/Iminus),'published_loss_groups':{g:val(F(n,sum(groups.values()))) for g,n in groups.items()},'old_kappa':val(kold),'new_kappa_upper':val(knew),'old_coefficients':list(map(val,(a0,b0,c0,d0))),'new_coefficients':list(map(val,(a1,b1,c1,d1))),'new_trial_lambda_fixed_margin_guarantee':val(newmargin_floor),'same_trial_same_lambda_cap_gain_upper':val(cap_gain_upper),'same_trial_same_lambda_net_gain_upper':val(net_gain_upper),'implication':'Refinement preserves a positive full restored k40 margin. Printed combined cap endpoint alone does not quantify an actual positive gain or prove k39.','sharp_pair_majorant':{'exponents':list(map(str,a)),'b1':bone,'b2':btwo,'N2':npairs,'ratio':str(F(bone+btwo,npairs))}}
print(json.dumps(out,indent=2));(BASE/'margin_ledger.json').write_text(json.dumps(out,indent=2))
