"""Exact rational verification of the minorant polytopes and triangulations.
Coverage certificate: all vertices are enumerated from halfspaces; positively
oriented simplex chain has no boundary in the polytope interior; its multiplicity
at an explicit strict interior point is one. Degree is constant off its boundary,
so the chain covers the convex polytope exactly once almost everywhere.
"""
from fractions import Fraction as F
from itertools import combinations,permutations
from collections import defaultdict
from pathlib import Path
import json
from minorant_mass import P1,P2,ROOTS,det

def solve(A,b):
 m=[list(a)+[v] for a,v in zip(A,b)];n=len(b)
 for j in range(n):
  row=next((i for i in range(j,n) if m[i][j]),None)
  if row is None:return None
  m[j],m[row]=m[row],m[j];d=m[j][j];m[j]=[x/d for x in m[j]]
  for i in range(n):
   if i!=j:
    d=m[i][j];m[i]=[x-d*y for x,y in zip(m[i],m[j])]
 return tuple(row[-1] for row in m)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def vec(*x):return tuple(map(F,x))
Z=[vec(1,0,0,0),vec(0,1,0,0),vec(0,0,1,0),vec(0,0,0,1),vec(-1,-1,-1,-1)]
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def neg(a):return tuple(-x for x in a)
def sub(a,b):return add(a,neg(b))
def halfspaces(which):
 # Every row represents a dot z <= rhs.
 H=[(neg(a),F(2)) for a in Z]
 if which==1:
  H += [(sub(Z[i+1],Z[i]),F(0)) for i in range(3)]
  H += [(sub(Z[3],Z[4]),F(0)),(add(Z[0],Z[1]),F(1)),(neg(add(add(Z[1],Z[2]),Z[3])),F(1))]
 else:
  H += [(sub(Z[1],Z[0]),F(0)),(sub(Z[1],Z[2]),F(0)),(sub(Z[3],Z[4]),F(0)),(add(Z[0],Z[2]),F(1)),(neg(add(add(Z[0],Z[1]),Z[3])),F(1))]
 return H

def parity(ids):return (-1)**sum(ids[i]>ids[j] for i in range(len(ids)) for j in range(i+1,len(ids)))
def barycentric(vertices,x):
 A=[[vertices[j][i]-vertices[0][i] for j in range(1,5)] for i in range(4)]
 t=solve(A,sub(x,vertices[0]));return (1-sum(t),)+t

def audit(which,vertices,roots):
 H=halfspaces(which);found=set()
 for chosen in combinations(H,4):
  x=solve([a for a,b in chosen],[b for a,b in chosen])
  if x is not None and all(dot(a,x)<=b for a,b in H):found.add(x)
 assert found==set(vertices),(which,found,set(vertices))
 oriented=[];faces=defaultdict(list)
 for ids in roots:
  ids=tuple(map(int,ids));v=[vertices[i] for i in ids]
  if det([sub(p,v[0]) for p in v[1:]])<0:ids=(ids[1],ids[0],*ids[2:])
  oriented.append(ids)
  for i in range(5):
   face=ids[:i]+ids[i+1:];faces[tuple(sorted(face))].append(((-1)**i)*parity(face))
 ext=inner=0
 for face,signs in faces.items():
  if len(signs)==2:
   assert sum(signs)==0;inner+=1
  else:
   assert len(signs)==1
   assert any(all(dot(a,vertices[i])==b for i in face) for a,b in H),(which,face)
   ext+=1
 first=[vertices[i] for i in oriented[0]]
 # Rational interior point avoids any accidental cell boundary.
 weights=[F(1,31),F(2,31),F(4,31),F(8,31),F(16,31)]
 x=tuple(sum(w*p[j] for w,p in zip(weights,first)) for j in range(4))
 assert all(dot(a,x)<b for a,b in H)
 multiplicity=0
 for ids in oriented:
  bc=barycentric([vertices[i] for i in ids],x)
  assert all(t!=0 for t in bc)
  multiplicity+=int(all(t>0 for t in bc))
 assert multiplicity==1
 return {'polytope':which,'halfspace_count':len(H),'enumerated_vertices':len(found),'simplices':len(oriented),'interior_faces':inner,'exterior_faces':ext,'interior_degree':multiplicity,'status':'PASS_EXACT_RATIONAL_GEOMETRY'}

if __name__=='__main__':
 result=[audit(1,P1,['01356','02356','02456']),audit(2,P2,['01256','01346','01356'])]
 print(json.dumps(result,indent=2));Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2))
