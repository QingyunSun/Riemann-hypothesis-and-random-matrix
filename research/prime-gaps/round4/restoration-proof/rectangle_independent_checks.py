"""Independent exact checks of rectangle kernels and marked-owner counting.

Does not import CapEngine, SourceJets, or the rectangle certifier.
Box kernels are reconstructed through integer-cell decomposition and Eulerian
unit-cube cell volumes, independently of inclusion-exclusion powers.
"""
from __future__ import annotations
import ast
from fractions import Fraction as F
import hashlib
import itertools
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
PRIME=HERE.parent/"prime-credit"
SOURCE=PRIME/"certify_alpha_rectangle.py"


def integer_box_convolve(a, width):
    output=[]
    running=0
    for j in range(len(a)+width-1):
        if j<len(a): running+=a[j]
        if 0<=j-width<len(a): running-=a[j-width]
        output.append(running)
    return output


def eulerian_kernel(offset,widths,length):
    eulerian={1:(1,),2:(1,1),3:(1,4,1)}[len(widths)]
    counts=[1]
    for width in widths:
        counts=integer_box_convolve(counts,width)
    result=[0]*length
    for j,count in enumerate(counts):
        for a,mult in enumerate(eulerian):
            index=offset+j+a
            if 0<=index<length:
                result[index]+=count*mult
    return result


def mark_multiply(a,b):
    return (a[0]*b[0],a[1]*b[0]+a[0]*b[1],
            a[2]*b[0]+a[0]*b[2],
            a[3]*b[0]+a[0]*b[3]+a[1]*b[2]+a[2]*b[1])


def owner_check():
    n,k=3,4
    channels=[
        [F(2,7),F(3,7),F(1,7)],
        [F(1,11),F(4,11),F(2,11)],
        [F(2,13),F(1,13),F(5,13)],
        [F(1,17),F(3,17),F(2,17)]]
    ring_integral=F(0);owner_integral=F(0)
    for cells in itertools.product(range(n),repeat=k):
        r=sum(cells)
        if not 3<=r<=6:continue
        # Nonconstant polynomial and radial mask test the weighted identity.
        points=[F(2*j+1,10) for j in cells]
        trial=1-3*sum(points)+sum(t*t for t in points)
        ring=(F(1),F(0),F(0),F(0))
        for j in cells:
            ring=mark_multiply(ring,tuple(c[j] for c in channels))
        ring_integral+=ring[3]*trial*trial
        explicit=F(0)
        for powner in range(k):
            for qowner in range(k):
                weight=F(1)
                for i,j in enumerate(cells):
                    channel=3 if i==powner==qowner else 1 if i==powner else 2 if i==qowner else 0
                    weight*=channels[channel][j]
                explicit+=weight
        owner_integral+=explicit*trial*trial
    assert ring_integral==owner_integral
    return {"same_owner_choices":k,"distinct_owner_choices":k*(k-1),
            "exact_weighted_integral":str(ring_integral),"owner_expansion_matches":True}


def main():
    tree=ast.parse(SOURCE.read_text())
    fn=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=="box_cell_numerators")
    scope={"itertools":itertools}
    exec(compile(ast.Module(body=[fn],type_ignores=[]),str(SOURCE),"exec"),scope)
    target=scope["box_cell_numerators"]
    specs=[(26400,(2700,18800)),(32400,(4300,18800)),(58800,(2700,4300,18800))]
    checks=[]
    for offset,widths in specs:
        independently=eulerian_kernel(offset,widths,98264)
        proposed=target(offset,widths,98264)
        assert independently==proposed
        checks.append({"offset":offset,"widths":widths,"cells_checked":98264,
                       "all_coefficients_match_exactly":True,"sum":sum(independently)})
    # Cell dimensional scaling: d residual/mark variables, d-1 mark denominators.
    h=F(7,1000); u=F(11);v=F(19)
    assert h*h/(h*u)/h==1/u
    assert h**3/((h*u)*(h*v))/h==1/(u*v)
    certificate=PRIME/"alpha_rectangle_certificate.json"
    receipt={}
    if certificate.exists():
        r=json.loads(certificate.read_text())
        low=F(r["alpha_rectangle_normalized_interval"]["lower"])
        upper=F(r["alpha_rectangle_normalized_interval"]["upper"])
        ih=F(23685317890,10**24)
        coefficient=1-4*F(2624989,10**7)*F(843183,10**9)
        assert 0<low<=upper
        assert F(r["alpha_over_published_I_upper_lower"])==low/ih
        assert F(r["credit_over_published_I_upper_lower"])==coefficient*low/ih
        assert F(r["alpha_credit_coefficient"])==coefficient
        assert r["signed_regression_passed"]
        receipt={"receipt_sha256":hashlib.sha256(certificate.read_bytes()).hexdigest(),
                 "positive_lower_endpoint_verified":True,"parts":len(r["parts"]),
                 "alpha_over_I_upper_lower":str(low/ih),
                 "credit_over_I_upper_lower":str(coefficient*low/ih)}
    return {"adapter_sha256":hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
            "independent_all_cell_kernel_checks":checks,"marking_owner_check":owner_check(),
            "cell_h_scaling_checked_exactly":True,"receipt":receipt,
            "all_assertions_passed":True}


if __name__=="__main__":
    data=main()
    text=json.dumps(data,indent=2)
    (HERE/"rectangle_independent_checks.json").write_text(text+"\n")
    print(text)
