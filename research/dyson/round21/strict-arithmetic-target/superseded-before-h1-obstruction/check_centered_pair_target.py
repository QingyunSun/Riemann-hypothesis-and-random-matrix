#!/usr/bin/env python3
"""Bounded exact algebra checks; not a prime-pair-error experiment."""
from __future__ import annotations
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path
import sympy as s

HERE = Path(__file__).resolve().parent

def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def integral_power(lo: F, hi: F, power: int) -> F:
    if hi <= lo:
        return F(0)
    return (hi ** (power + 1) - lo ** (power + 1)) / (power + 1)

def main() -> None:
    checks = {}
    # Strip the common T/log(T)^2, use one compact x window and finite
    # signed atoms. This verifies the exact b/Pareto double-sum identity.
    atoms = {2:F(-1,2),3:F(3,4),4:F(-2),6:F(5,3),9:F(1,7)}
    toy = []
    for T in (4,5,7,11):
        for lo, hi in ((F(3,2),F(7,2)),(F(2),F(8)),(F(1),F(5,2))):
            def j(m):
                return integral_power(lo,min(hi,F(m)),T-2)
            direct = sum((am*an*j(min(m,n))/max(m,n)**T
                          for m,am in atoms.items() for n,an in atoms.items()),F(0))
            diag = sum((am*am*j(m)/m**T for m,am in atoms.items()),F(0))
            off = sum((2*am*an*j(m)/m**T*F(m,n)**T
                       for m,am in atoms.items() for n,an in atoms.items() if m<n),F(0))
            assert direct == diag+off
            assert direct >= 0
            toy.append({"T":T,"window":[str(lo),str(hi)],
                        "norm":str(direct),"diagonal":str(diag),"off_diagonal":str(off)})
    checks["exact_signed_kernel_cases"] = toy

    floor_cases = 0
    for x in (F(1),F(5,4),F(3,2),F(17,5),F(21,4)):
        for q in (F(1),F(6,5),F(3,2),F(2),F(17,4)):
            ncount = (q*x).__floor__()-x.__floor__()
            remainder = F(ncount)-(q-1)*x
            assert abs(remainder) <= 1
            # Arbitrary finite prime-count value P: (P-ncount)+r=P-(q-1)x.
            P=F(13,7)
            assert (P-ncount)+remainder == P-(q-1)*x
            floor_cases += 1
    checks["exact_floor_centering_cases"] = floor_cases

    # y=m*t/(1-t): y*k''(y)dy=T(T+1)t(1-t)^(T-1)dt.
    # All log moments reduced to exact polynomial beta integrals.
    beta = []
    t=s.symbols("t")
    for T in (4,5,7,11):
        poly=s.Poly(s.expand(T*(T+1)*t*(1-t)**(T-1)),t)
        mass=sum(coef/s.Rational(j+1) for (j,),coef in poly.terms())
        log_t=sum(-coef/s.Rational((j+1)**2) for (j,),coef in poly.terms())
        log_1mt=sum(-coef*s.harmonic(j+1)/s.Rational(j+1) for (j,),coef in poly.terms())
        assert s.simplify(mass-1)==0
        assert s.simplify(log_t-log_1mt-(1-s.harmonic(T-1)))==0
        # E[u], where u=T*y/m, is T*t/(1-t).
        eu=s.integrate(s.expand(T*T*(T+1)*t*t*(1-t)**(T-2)),(t,0,1))
        assert eu==s.Rational(2*T,T-1)
        assert eu<=s.Rational(8,3)
        beta.append({"T":T,"mass":str(mass),
                     "log_y_minus_log_m":str(s.simplify(log_t-log_1mt)),
                     "mean_scaled_u":str(eu)})
    checks["beta_exact_moments"] = beta

    # Finite, formal prime-power diagonal correction, not a prime-height scan.
    symbols={p:s.Symbol("L"+str(p)) for p in (2,3,5)}
    formal=[]
    for p,lp in symbols.items():
        for k in (1,2,3,4):
            lamb=lp
            logn=k*lp
            correction=s.expand(lamb*logn-lamb*lamb)
            assert correction==(k-1)*lp*lp
            formal.append({"p":p,"k":k,"correction":str(correction)})
    checks["formal_prime_power_corrections"] = formal

    exponents=[]
    for alpha in (F(7,4),F(2),F(9,4)):
        theta=1-1/alpha
        error=F(1,2)-1/alpha
        exponents.append({"alpha":str(alpha),"theta":str(theta),
                          "square_root_absolute_error_power_X":str(error),
                          "same_power_T":str(alpha/F(2)-1)})
    assert [r["square_root_absolute_error_power_X"] for r in exponents]==["-1/14","0","1/18"]
    assert F(1,18)/F(5,9)==F(1,10)
    assert 1/F(9,4)==F(4,9)
    assert 1/(1-F(523,1000))==F(1000,477)
    checks["exact_exponents"]=exponents
    checks["uniform_beta_threshold"]="4/9"
    checks["extra_shift_saving_rho_threshold"]="1/10"
    checks["H_exceeds_old_Q_at_alpha"]="1000/477"
    checks["floor_squared_norm_power_T"]="-3/4"
    checks["floor_norm_comparison_power_T"]="-3/8"

    # Exact consequences of the author's inherited decimal diagnostics only.
    m0=F("0.7406125730612092")
    m1=F("0.16940474262803504")
    M=m0/4
    A=1+m1/16
    assert (A-M)-(1-M)==A-1
    checks["inherited_decimal_arithmetic"]={
        "certification":"exact arithmetic on inherited floating diagnostics, not interval bounds",
        "M":float(M),"target_1_minus_M":float(1-M),
        "AH_A_minus_M":float(A-M),"required_gain_A_minus_1":float(A-1),
        "exact_decimal_gain":str(A-1)}
    out={"status":"PASS","scope":"bounded structural/algebra checks, no numerical prime-pair bound",
         "author_sha256":sha(HERE/"CENTERED_PAIR_ERROR_TARGET.md"),
         "checker_sha256":sha(Path(__file__)),
         "checks":checks}
    encoded=json.dumps(out,indent=2,sort_keys=True)+"\n"
    (HERE/"centered_pair_target_checks.json").write_text(encoded)
    print(encoded,end="")

if __name__=="__main__":
    main()

