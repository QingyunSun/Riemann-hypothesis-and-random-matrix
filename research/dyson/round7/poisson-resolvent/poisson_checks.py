"""Reproduce the Poisson variance discriminator; no actual-zeta limit assumed."""
from pathlib import Path
from itertools import combinations
import json
import time

import mpmath as mp
import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent


def sine_variance(b):
    return -2 * mp.expm1(-b) / b**2


def lattice_variance(b):
    return 2 * mp.tanh(b / 2) / b**2 + 2 / mp.expm1(2 * b)


def finite_variances(n, b):
    # Periodized P_a on a circle of length n has Fourier coefficients
    # exp(-2*pi*a*|m|/n)/n. b=4*pi*a.
    q = mp.exp(-b / n)
    cue = 2 / n**2 * (sum(m * q**m for m in range(1, n + 1))
                      + n * q**(n + 1) / (1 - q))
    acue = 2 / n**2 * (sum(min(m, 2*n-m) * q**m for m in range(1, 2*n))
                       + n**2 * q**(2*n)) / (1 - q**(2*n))
    return cue, acue


def enumeration_check(n):
    roots = np.exp(2j * np.pi * np.arange(2*n) / (2*n))
    modes = np.arange(1, 4*n + 1)
    means = np.zeros(len(modes))
    mass = 0.0
    for indices in combinations(range(2*n), n):
        z = roots[list(indices)]
        weight = np.prod([abs(z[i]-z[j])**2 for i in range(n) for j in range(i+1, n)]) / (2*n)**n
        mass += weight
        means += weight * np.abs(np.sum(z[:, None]**modes[None, :], axis=0))**2
    target = np.array([n*n if m % (2*n) == 0 else min(m % (2*n), 2*n-m % (2*n)) for m in modes])
    error = float(np.max(np.abs(means-target)))
    assert error < 1e-10 and abs(mass-1) < 1e-12
    return {"N": n, "subsets": int(sp.binomial(2*n,n)),
            "normalization_error": mass-1, "max_trace_second_moment_error": error}


def main():
    start = time.perf_counter()
    mp.mp.dps = 65
    b = sp.symbols("b", positive=True)
    sine = 2*(1-sp.exp(-b))/b**2
    alt = 2*(1-sp.exp(-b))/(1+sp.exp(-b))/b**2 + 2/(sp.exp(2*b)-1)
    gap = sine-alt
    factorized = 2*sp.exp(-2*b)*(4*sp.sinh(b/2)**2-b**2)/(b**2*(1-sp.exp(-2*b)))
    assert sp.simplify(gap-factorized.rewrite(sp.exp)) == 0
    series = sp.series(gap, b, 0, 5)
    assert sp.limit(gap/b,b,0) == sp.Rational(1,12)
    assert sp.limit(gap*b**2*sp.exp(b),b,sp.oo) == 2

    # Paired canonical-product normalization: exact rational finite analogue.
    eta, t, rho = sp.Rational(2,7), sp.Rational(5,3), sp.Rational(7,5)
    zeros = [sp.Rational(-7,2), sp.Rational(-1), sp.Rational(1), sp.Rational(7,2)]
    s = sp.symbols("s")
    product = sp.prod(s-sp.I*g for g in zeros)
    derivative = sp.diff(product,s)/product
    lhs = sp.re(derivative.subs(s,eta+sp.I*t))/(sp.pi*rho)
    a = rho*eta
    rhs = sum(a/(sp.pi*(a*a+rho*rho*(t-g)**2)) for g in zeros)
    assert sp.simplify(lhs-rhs) == 0

    rows=[]
    for value in ("0.125", "0.25", "0.5", "1", "2", "4", "8", "16"):
        bb=mp.mpf(value)
        vc, va=sine_variance(bb), lattice_variance(bb)
        # Independent integration of one triangular period plus exact Bragg sum.
        period=mp.quad(lambda u:u*mp.exp(-bb*u),[0,1])+mp.quad(lambda u:(2-u)*mp.exp(-bb*u),[1,2])
        quadrature=2*period/(-mp.expm1(-2*bb))+2/mp.expm1(2*bb)
        assert abs(quadrature-va)<mp.mpf("1e-58")
        assert vc>va>0
        refinements=[]
        for n in (16,64,256,1024):
            fc,fa=finite_variances(n,bb)
            ratio=(bb/(2*n)/mp.sinh(bb/(2*n)))**2
            assert abs(fc/vc-ratio)<mp.mpf("1e-58")
            refinements.append({"N":n,"CUE":float(fc),"ACUE":float(fa),
                                "CUE_error":float(fc-vc),"ACUE_error":float(fa-va)})
        rows.append({"b":value,"a_unit_spacing":float(bb/(4*mp.pi)),
                     "sine_variance":mp.nstr(vc,35),"ACUE_variance":mp.nstr(va,35),
                     "difference":mp.nstr(vc-va,35),"relative_difference":float((vc-va)/vc),
                     "quadrature_error":float(quadrature-va),"finite_refinements":refinements})
    enumerations=[enumeration_check(n) for n in range(2,7)]
    output={"status":"PASS","fourier_convention":"exp(-2*pi*i*x*alpha)",
            "b_definition":"4*pi*a, where a is the Poisson width in mean-spacing units",
            "sine_minus_ACUE_small_b_series":str(series),
            "small_b_gap_over_b":"1/12","large_b_gap_times_b_squared_exp_b":"2",
            "canonical_product_normalization":"exact rational finite paired-product identity verified",
            "values":rows,"floating_subset_enumeration":enumerations,
            "scope":"Exact analytic identities plus numerical integration/finite ensemble checks. No actual-zeta variance, AH refutation or novelty claim.",
            "elapsed_seconds":time.perf_counter()-start}
    (HERE/"poisson_checks.json").write_text(json.dumps(output,indent=2)+"\n")
    print(json.dumps({k:v for k,v in output.items() if k!="values"},indent=2))


if __name__=="__main__":
    main()
