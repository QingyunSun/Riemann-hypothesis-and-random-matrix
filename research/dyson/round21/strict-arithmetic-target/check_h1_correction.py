#!/usr/bin/env python3
"""Exact correction addendum; preserves the original R21 checker/output bytes."""
from pathlib import Path
import hashlib
import json
import sympy as s

HERE=Path(__file__).resolve().parent
OLD=HERE/"superseded-before-h1-obstruction"

def pin(p):
    b=p.read_bytes()
    return {"bytes":len(b),"sha256":hashlib.sha256(b).hexdigest()}

def main():
    report=HERE/"CENTERED_PAIR_ERROR_TARGET.md"
    old_report=OLD/report.name
    old=old_report.read_text()
    new=report.read_text()
    preserved={}
    for name in ("check_centered_pair_target.py","centered_pair_target_checks.json",
                 "centered_pair_target_checks.log"):
        assert (HERE/name).read_bytes()==(OLD/name).read_bytes()
        preserved[name]=pin(HERE/name)

    blocks={}
    for label,start,end in (
        ("main_sections_1_through_4","## 1. The exact missing inequality","## 5."),
        ("centered_error_and_Abel_29_30","For \\(X\\) in the present window","\nIf "),
        ("square_root_budget_33_34","For the often proposed square-root-size","## 6."),
        ("primary_source_audit","## 6. Primary-source audit","## 7."),
    ):
        a=old[old.index(start):old.index(end,old.index(start))]
        b=new[new.index(start):new.index(end,new.index(start))]
        assert a==b,label
        blocks[label]={"unchanged":True,"sha256":hashlib.sha256(a.encode()).hexdigest()}

    u,v=s.symbols("u v")
    assert s.expand((u-1)*(v-1)+1-(u*v-u-v+2))==0
    lam=s.symbols("l0:25")
    def psi(n):return sum(lam[1:n+1],s.Integer(0))
    endpoint_cases=0
    for X in (2,3,4,5,8):
        for z in range(X+1,2*X+1):
            P=sum((lam[m]*lam[m+1] for m in range(X+1,z+1)),s.Integer(0))
            direct=sum(((lam[m]-1)*(lam[m+1]-1)+1
                        for m in range(X+1,z+1)),s.Integer(0))
            first=P-(psi(z)-psi(X))-(psi(z+1)-psi(X+1))+2*(z-X)
            second=P-2*((psi(z)-z)-(psi(X)-X))-lam[z+1]+lam[X+1]
            assert s.expand(direct-first)==0
            assert s.expand(direct-second)==0
            endpoint_cases+=1
    zeta_s,rho,mult=s.symbols("s rho mult",nonzero=True)
    principal=-mult/(zeta_s*(zeta_s-rho))-1/(zeta_s-1)
    residue=s.simplify(s.limit((zeta_s-rho)*principal,zeta_s,rho))
    assert residue==-mult/rho
    r=s.symbols("r")
    for n in range(1,7):
        assert s.expand((r-1)*sum(r**j for j in range(n))-(r**n-1))==0
    assert s.Rational(7,4)<2<s.Rational(9,4)
    assert s.Rational(4,9)<s.Rational(17,36)<s.Rational(1,2)

    sources={}
    for name in ("COORDINATOR_H1_OBSTRUCTION.md","dlmf-25.10.html","dlmf-25.2.html"):
        sources[name]=pin(HERE/"sources"/name)
    assert sources["COORDINATOR_H1_OBSTRUCTION.md"]["sha256"]=="5270e51de9df32aecee7fd63e569c5f3cdcd743107fc1c7f7be69cf6df587d34"

    out={
      "status":"PASS",
      "scope":"new exact algebra/delta check; analytic impossibility established by manuscript proof",
      "current_author":pin(report),
      "superseded_author":pin(old_report),
      "checker":pin(Path(__file__)),
      "original_check_files_preserved":preserved,
      "unchanged_mathematical_blocks":blocks,
      "formal_h1_expansion":str(s.expand((u-1)*(v-1)+1)),
      "formal_exact_singleton_endpoint_cases":endpoint_cases,
      "mellin_zero_residue":str(residue),
      "dyadic_geometric_identity_cases":6,
      "uniformity_scope":"all sufficiently large T; X=T^2 covers every sufficiently large X",
      "impossible_premise":"all shifts 1<=h<=X with a uniform beta<1/2 (therefore beta<4/9)",
      "not_excluded":"the actual signed aggregate; restricted-shift estimates; averaged cancellation",
      "assumption_for_obstruction":"unconditional existence of a critical-line zero; no RH needed",
      "new_source_pins":sources,
    }
    data=json.dumps(out,indent=2,sort_keys=True)+"\n"
    (HERE/"h1_correction_checks.json").write_text(data)
    print(data,end="")

if __name__=="__main__":
    main()

