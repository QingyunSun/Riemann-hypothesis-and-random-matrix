"""Independent exact-rational enclosure of the fixed 186 minorant mass.
Inputs: six 4-simplex triangulation cells in official Numerical certificate Lemma2.8.
For f(alpha)=prod(alpha_i)^(-1), log f is convex, hence f is convex.
On each simplex, f(centroid)<=average(f)<=average(f(vertices)).
Every cell contribution is rounded outwards to 10^-30 using integer arithmetic.
Adaptive bisection choice uses floats solely to select which valid cell to bisect.
No interval arithmetic package or special convolution library is required.
"""
from fractions import Fraction as F
from heapq import heappush,heappop
from itertools import permutations,combinations
from pathlib import Path
import json,time
SCALE=10**30
T=F(481,100000)
P1=[(-F(1,3),)*4,(F(0),)*4,(F(1,2),F(1,2),-F(3,4),-F(3,4)),(F(1,2),F(1,2),-F(1,3),-F(1,3)),(F(1,2),F(1,2),F(1,2),-F(2)),(F(1,2),F(1,2),F(1,2),-F(3,4)),(F(4,3),-F(1,3),-F(1,3),-F(1,3))]
P2=[(-F(2),-F(2),-F(2),F(3)),(-F(1,3),-F(1,3),F(4,3),-F(1,3)),(F(1,2),-F(2),F(1,2),F(1,2)),(F(1,2),F(1,2),F(1,2),-F(2)),(F(1,2),F(1,2),F(1,2),-F(3,4)),(F(3),-F(2),-F(2),-F(2)),(F(3),-F(2),-F(2),F(1,2))]
ROOTS=[(P1,ids,v) for ids,v in [('01356',F(125,5184)),('02356',F(625,20736)),('02456',F(625,6912))]]+[(P2,ids,v) for ids,v in [('01256',F(625,288)),('01346',F(625,576)),('01356',F(625,288))]]
def prod(a):
 r=F(1)
 for v in a:r*=v
 return r
def det(a):
 return sum((-1)**sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))*prod(a[i][p[i]] for i in range(4)) for p in permutations(range(4)))
def f(v):
 alpha=[F(1,5)+T*x for x in v];alpha.append(1-sum(alpha))
 assert min(alpha)>0
 return 1/prod(alpha)
def floor(x):return x.numerator//x.denominator
def ceil(x):return -floor(-x)
def bounds(v,volume):
 center=tuple(sum(p[j] for p in v)/5 for j in range(4))
 lo=volume*T**4*f(center);hi=volume*T**4*sum(map(f,v))/5
 return floor(lo*SCALE),ceil(hi*SCALE)
def split(v):
 # Longest edge in the Euclidean coordinates on the 4-simplex.
 i,j=max(combinations(range(5),2),key=lambda ij:sum((v[ij[0]][r]-v[ij[1]][r])**2 for r in range(4)))
 m=tuple((a+b)/2 for a,b in zip(v[i],v[j]));a=list(v);b=list(v);a[i]=m;b[j]=m
 return tuple(a),tuple(b)
def run(count):
 start=time.monotonic();heap=[];serial=0;lower=upper=0
 for ps,ids,vol in ROOTS:
  vs=tuple(ps[int(i)] for i in ids)
  actual=abs(det([[vs[i][j]-vs[0][j] for j in range(4)] for i in range(1,5)]))/24
  assert actual==vol
  lo,hi=bounds(vs,vol);lower+=lo;upper+=hi;heappush(heap,(-(hi-lo),serial,vs,vol,lo,hi));serial+=1
 for n in range(count-6):
  _,_,vs,vol,lo,hi=heappop(heap);lower-=lo;upper-=hi
  for sub in split(vs):
   l,u=bounds(sub,vol/2);lower+=l;upper+=u;heappush(heap,(-(u-l),serial,sub,vol/2,l,u));serial+=1
 out={'method':'exact rational convex simplex bounds, dyadic adaptive bisection','leaf_simplices':len(heap),'lower_numerator':lower,'upper_numerator':upper,'common_denominator':SCALE,'lower':float(F(lower,SCALE)),'upper':float(F(upper,SCALE)),'width':float(F(upper-lower,SCALE)),'seconds':time.monotonic()-start,'status':'RIGOROUS_BOUNDS_CONDITIONAL_ON_PUBLISHED_TRIANGULATION_COVERAGE','coverage_note':'Volumes checked exactly; polytope triangulation covering/no-overlap inherited from cited companion lemma.'}
 print(json.dumps(out,indent=2));Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2));return out
if __name__=='__main__':run(16384)
