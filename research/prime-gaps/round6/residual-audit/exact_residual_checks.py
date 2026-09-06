#!/usr/bin/env python3
"""Small exact-rational counterchecks of the signed residual audit.

These finite toy identities test signs, projections and mass normalization.
They are not numerical evidence for a k=39 improvement.
"""
from __future__ import annotations

import json
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import random


def dot(x, y, weights):
    return sum((a*b*w for a,b,w in zip(x,y,weights)), F(0))


def plus(x,y): return [a+b for a,b in zip(x,y)]
def minus(x,y): return [a-b for a,b in zip(x,y)]
def scale(c,x): return [c*a for a in x]


def solve(matrix, rhs):
    a=[list(row)+[b] for row,b in zip(matrix,rhs)]
    n=len(a)
    for j in range(n):
        pivot=next(i for i in range(j,n) if a[i][j])
        a[j],a[pivot]=a[pivot],a[j]
        a[j]=[x/a[j][j] for x in a[j]]
        for i in range(n):
            if i!=j:
                m=a[i][j]
                a[i]=[x-m*y for x,y in zip(a[i],a[j])]
    return [row[-1] for row in a]


def project(x, basis, weights):
    gram=[[dot(u,v,weights) for v in basis] for u in basis]
    rhs=[dot(u,x,weights) for u in basis]
    coefficients=solve(gram,rhs)
    out=[F(0)]*len(x)
    for c,v in zip(coefficients,basis):out=plus(out,scale(c,v))
    return out


def matrix_action(symmetric, weights, x):
    return [sum((a*b for a,b in zip(row,x)),F(0))/w
            for row,w in zip(symmetric,weights)]


def residual_checks():
    rng=random.Random(20260905)
    weights=list(map(F,[1,2,3,5,7]))
    basis_u=[[F(int(i==j)) for i in range(5)] for j in range(2)]
    basis_v=[list(map(F,[1,1,1,0,0])),list(map(F,[0,1,0,1,1]))]
    f=basis_u[0]
    sample=None
    for trial in range(80):
        symmetric=[[F(0) for _ in range(5)] for _ in range(5)]
        for i in range(5):
            for j in range(i,5):
                value=F(rng.randint(-5,5),rng.randint(7,19))
                symmetric[i][j]=symmetric[j][i]=value
        symmetric[0][0]=F(9,10)
        symmetric[2][2]=-F(1,3)  # A witnessed negative Rayleigh direction.
        symmetric[0][1]=symmetric[1][0]=F(0) if trial%2==0 else F(1,20)
        tf=matrix_action(symmetric,weights,f)
        p_tf=project(tf,basis_u,weights)
        r=minus(tf,p_tf)
        assert dot(tf,r,weights)==dot(r,r,weights)
        lam=F(9,10) if trial%4!=3 else F(91,100)
        e=minus(p_tf,scale(lam,f))
        h=project(minus(tf,scale(lam,f)),basis_v,weights)
        ph=project(h,basis_u,weights)
        z=minus(h,ph)
        alpha=dot(h,h,weights)
        leakage=dot(ph,ph,weights)
        znorm=dot(z,z,weights)
        coupling=dot(tf,z,weights)
        assert znorm==alpha-leakage
        assert coupling==alpha-dot(e,ph,weights)
        assert dot(e,ph,weights)**2<=dot(e,e,weights)*leakage
        perturbation=scale(F(1,1000),basis_v[0])
        h_tilde=plus(h,perturbation)
        ph_tilde=project(h_tilde,basis_u,weights)
        z_tilde=minus(h_tilde,ph_tilde)
        exact_rhs=(dot(h_tilde,h_tilde,weights)
                   +dot(minus(h,h_tilde),h_tilde,weights)
                   -dot(e,ph_tilde,weights))
        assert dot(tf,z_tilde,weights)==exact_rhs
        # Witness that nonnested coupling is alpha, not the mass of Qh.
        if trial%2==0 and alpha and leakage and sample is None:
            assert coupling==alpha and coupling!=znorm
            sample={"h_mass_squared":str(alpha),"Qh_mass_squared":str(znorm),
                    "unnormalized_coupling":str(coupling),
                    "within_U_mass_squared":str(leakage),
                    "negative_rayleigh_witness":str(symmetric[2][2]/weights[2])}
        # Inexact Gram solve: exact Pythagoras correction in equation (25).
        c_exact=[ph[i] for i in range(2)]
        c0=[c_exact[0]+F(1,100),c_exact[1]-F(1,200)]
        z0=minus(h,plus(scale(c0[0],basis_u[0]),scale(c0[1],basis_u[1])))
        b=[dot(u,h,weights)-weights[i]*c0[i] for i,u in enumerate(basis_u)]
        correction=sum((b[i]**2/weights[i] for i in range(2)),F(0))
        assert dot(z0,z0,weights)-correction==znorm
    assert sample is not None
    return {"exact_trials":80,"nonnested_exact_ritz_example":sample}


def face_mass_checks():
    one_mass=list(map(F,[2,3,7]))
    g=list(map(F,[1,2,3]))
    points=list(product(range(3),repeat=3))
    outer=[x for x in points if sum(x)<=4]
    mass={x:one_mass[x[0]]*one_mass[x[1]]*one_mass[x[2]] for x in outer}
    amplitude={x:F(1+2*x[0]-x[1]+3*x[2],7) for x in outer}
    G={x:g[x[0]]*g[x[1]]*g[x[2]] for x in outer}
    f={x:G[x]*amplitude[x] for x in outer}
    rho=F(1,4)
    tf={x:F(0) for x in outer}
    conjugated={x:F(0) for x in outer}
    wrong_adjoint_discrepancy=None
    for i in range(3):
        faces=list(product(range(3),repeat=2))
        def insert(y,j):
            out=list(y);out.insert(i,j);return tuple(out)
        marginal={y:sum((one_mass[j]*f.get(insert(y,j),F(0)) for j in range(3)),F(0)) for y in faces}
        psi={y:F(1+y[0]+2*y[1],5) for y in faces}
        lhs=sum((marginal[y]*psi[y]*one_mass[y[0]]*one_mass[y[1]] for y in faces),F(0))
        rhs=sum((f[x]*psi[x[:i]+x[i+1:]]*mass[x] for x in outer),F(0))
        assert lhs==rhs
        conditional={y:sum((one_mass[j] for j in range(3) if insert(y,j) in mass),F(0)) for y in faces}
        wrong=sum((marginal[y]*psi[y]*one_mass[y[0]]*one_mass[y[1]]/conditional[y]
                   for y in faces if conditional[y]),F(0))
        if wrong!=lhs:wrong_adjoint_discrepancy=str(lhs-wrong)
        for x in outer:
            y=x[:i]+x[i+1:]
            multiplier=F(1) if sum(y)<=1 else F(9,10) if sum(y)<=2 else -F(1,10)
            tf[x]+=rho*multiplier*marginal[y]
            integral=sum((one_mass[j]*g[j]*amplitude.get(insert(y,j),F(0)) for j in range(3)),F(0))
            conjugated[x]+=rho*multiplier*integral/g[x[i]]
    assert all(tf[x]/G[x]==conjugated[x] for x in outer)
    assert wrong_adjoint_discrepancy is not None
    q={s:F(0) for s in range(5)}
    b={s:F(0) for s in range(5)}
    for x in outer:
        q[sum(x)]+=G[x]**2*mass[x]
        b[sum(x)]+=G[x]*tf[x]*mass[x]
    projected={x:G[x]*b[sum(x)]/q[sum(x)] for x in outer}
    for s in range(5):
        inner=sum(((tf[x]-projected[x])*G[x]*mass[x] for x in outer if sum(x)==s),F(0))
        assert inner==0
    return {"outer_points":len(outer),"face_adjoint_checks":3,
            "conditional_expectation_wrong_adjoint_defect":wrong_adjoint_discrepancy,
            "conjugated_single_g_identity":True,"radial_projection_checks":5}


if __name__=="__main__":
    output={"status":"all exact rational toy checks passed; no k39 numerical gain asserted",
            "residual":residual_checks(),"mass":face_mass_checks()}
    path=Path(__file__).with_suffix(".json")
    path.write_text(json.dumps(output,indent=2)+"\n")
    print(json.dumps(output,indent=2))
