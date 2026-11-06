"""Certify midpoint tests at three predeclared blocks. Requires python-flint 0.8.0."""
import argparse
import json
import flint
from flint import acb, acb_series, arb, ctx

# The cited Platt--Trudgian finite-RH theorem covers both signs by symmetry.
VERIFIED_HEIGHT = 3_000_000_000_000
BLOCKS = ((2, 128), (6645, 128), (99937, 128))


def xi_log_derivative(s):
    zeta = acb_series([s, 1], prec=2).zeta()
    return 1/s + 1/(s-1) + ((s/2).digamma()-arb.pi().log())/2 + zeta[1]/zeta[0]


def regular_slope_at_zero(rho):
    # Derivative of the regular part of xi'/xi at a known simple zero.
    zeta = acb_series([rho, 1], prec=4).zeta()
    assert not zeta[1].contains(0)
    return (-1/rho**2 - 1/(rho-1)**2 + (rho/2).polygamma(1)/4
            + 2*zeta[3]/zeta[1] - (zeta[2]/zeta[1])**2).real


def serial(x):
    return x.str(17, radius=True)


def scan(start, count):
    zeros = acb.zeta_zeros(start, count+1)
    assert all(z.real == arb(1)/2 for z in zeros)
    slopes = [regular_slope_at_zero(z) for z in zeros]
    threshold = 7 - 3*arb(5).sqrt()
    true_cut = arb(4)/5
    rows = []
    for off in range(count):
        a, b = zeros[off].imag, zeros[off+1].imag
        assert b > a > 0
        d, m = b-a, (b+a)/2
        v = d * xi_log_derivative(acb((1+d)/2, m)).real
        residual = 2*v-4
        epsilon = 1/(4*(VERIFIED_HEIGHT-m)**2)
        c = (1-epsilon)/(1+epsilon)**2
        robust = residual/c
        assert m < VERIFIED_HEIGHT-1 and 0 < c and c <= 1 and residual > 0
        passes = bool(robust < threshold)
        assert passes or robust > threshold, "threshold undecided"
        directed = d**2*(slopes[off]+slopes[off+1])-2
        endpoint_eps = 1/(4*(VERIFIED_HEIGHT-b)**2)
        endpoint_factor = (1-endpoint_eps)/(1+endpoint_eps)**2
        upper_from_derivatives = directed/endpoint_factor
        actual = bool(upper_from_derivatives < true_cut)
        assert actual or directed > true_cut, "projected energy classification undecided"
        if passes:
            bound = 2*robust/(1-robust/2)**2
            assert bound < true_cut and directed < bound
        rows.append(dict(n=start+off, gap=serial(d), midpoint_residual=serial(residual),
                         projected_upper=serial(bound) if passes else None,
                         regular_derivative_value=serial(directed),
                         projected_upper_from_derivatives=serial(upper_from_derivatives),
                         passes=passes,
                         derivative_below_four_fifths=actual,
                         normalized_gap=serial(d*(m/(2*arb.pi())).log()/(2*arb.pi()))))
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bits", type=int, default=176)
    args = parser.parse_args()
    if args.bits < 128:
        parser.error("request at least 128 bits")
    ctx.prec = args.bits
    blocks = []
    for start, count in BLOCKS:
        rows = scan(start, count)
        blocks.append(dict(start=start, count=count, certified=sum(r["passes"] for r in rows),
                           derivative_below=sum(r["derivative_below_four_fifths"] for r in rows),
                           pairs=rows))
    print(json.dumps(dict(python_flint=flint.__version__, bits=ctx.prec, blocks=blocks),
                     indent=2))


if __name__ == "__main__":
    main()
