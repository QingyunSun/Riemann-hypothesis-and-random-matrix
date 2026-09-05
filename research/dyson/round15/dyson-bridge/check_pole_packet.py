"""Bounded checks for the pole-annihilating packet, not zeta-target evidence."""
from __future__ import annotations

from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

import mpmath as mp

mp.mp.dps = 70
HERE = Path(__file__).resolve().parent


def decimal(x: mp.mpf | mp.mpc) -> str:
    return mp.nstr(x, 62)


def packet(t, sigma, width):
    a = 1 - sigma
    return (t * t + a * a) / (width * width) * mp.exp(
        -t * t / (2 * width * width)
    )


def kernel(lam, sigma, width):
    a = 1 - sigma
    return mp.sqrt(2 * mp.pi) * width * (
        1 + (a / width) ** 2 - (width * lam) ** 2
    ) * mp.exp(-(width * lam) ** 2 / 2)


def require_small(x, tolerance=mp.mpf("1e-55")):
    assert abs(x) < tolerance, decimal(x)


def main():
    # Exact polynomial coefficients in P(z)(1+z)^2.
    p = [F(15, 16), F(13, 4), F(3, 4), F(1)]
    q = [sum((p[i] * [F(1), F(2), F(1)][j - i]
              for i in range(len(p)) if 0 <= j - i <= 2), F(0))
         for j in range(6)]
    assert q == [F(15, 16), F(41, 8), F(131, 16), F(23, 4), F(11, 4), F(1)]
    assert sum(q) == F(95, 4)
    # Gaussian moments are 2^j Gamma((j+1)/2); even j carry sqrt(pi).
    root_pi_coefficient = q[0] + 2 * q[2] + 12 * q[4]
    rational_coefficient = 2 * q[1] + 8 * q[3] + 64 * q[5]
    assert root_pi_coefficient == F(805, 16)
    assert rational_coefficient == F(481, 4)
    full_constant = 2 * F(18, 7) * F(16, 15) * (
        F(805, 16) * F(16, 9) + F(481, 4)
    )
    assert full_constant == F(120784, 105) < 1200
    tail_constant = F(18, 7) * F(16, 15) * 95
    assert tail_constant < 270
    assert F(22, 7) < F(16, 9) ** 2
    assert 2 * F(22, 7) < F(18, 7) ** 2

    pole_checks = []
    fourier_checks = []
    for sigma_s, width_s in [("0.6", "1"), ("0.7", "2"), ("0.55", "5")]:
        sigma, width = mp.mpf(sigma_s), mp.mpf(width_s)
        a = 1 - sigma
        pole_value = packet(-1j * a, sigma, width)
        require_small(pole_value)
        pole_checks.append({
            "sigma": sigma_s, "time_width": width_s,
            "packet_at_pole": decimal(pole_value),
        })
        for lam_s in ["0", "0.3", "1"]:
            lam = mp.mpf(lam_s)
            # Real even Fourier integral; u is time divided by width.
            direct = 2 * width * mp.quad(
                lambda u: (u * u + (a / width) ** 2) * mp.exp(-u * u / 2)
                * mp.cos(width * lam * u), [0, 1, 3, mp.inf]
            )
            predicted = kernel(lam, sigma, width)
            require_small(direct - predicted)
            fourier_checks.append({
                "sigma": sigma_s, "time_width": width_s, "lambda": lam_s,
                "direct": decimal(direct), "formula": decimal(predicted),
                "absolute_difference": decimal(abs(direct - predicted)),
            })

    masses = []
    for b_s in ["0", "0.1", "0.4"]:
        b = mp.mpf(b_s)
        r = mp.sqrt(1 + b * b)
        g = lambda z: (1 + b * b - z * z) * mp.exp(-z * z / 2)
        pos = mp.quad(g, [-r, 0, r])
        # Integrate disjoint negative intervals explicitly.
        neg = -mp.quad(g, [-mp.inf, -r]) - mp.quad(g, [r, mp.inf])
        pos_formula = 2 * r * mp.exp(-r * r / 2) + 2 * b * b * mp.quad(
            lambda z: mp.exp(-z * z / 2), [0, r]
        )
        neg_formula = pos_formula - b * b * mp.sqrt(2 * mp.pi)
        require_small(pos - pos_formula)
        require_small(neg - neg_formula)
        tilted_pos = mp.quad(lambda z: g(z) * mp.exp(b * z), [-r, 0, r])
        tilted_neg = -mp.quad(lambda z: g(z) * mp.exp(b * z), [-mp.inf, -r])
        tilted_neg -= mp.quad(lambda z: g(z) * mp.exp(b * z), [r, mp.inf])
        tilted_formula = 2 * mp.exp(-r * r / 2) * (
            r * mp.cosh(b * r) + b * mp.sinh(b * r)
        )
        require_small(tilted_pos - tilted_formula)
        require_small(tilted_neg - tilted_formula)
        masses.append({
            "b": b_s, "positive_unweighted": decimal(pos),
            "negative_unweighted": decimal(neg),
            "negative_to_positive": decimal(neg / pos),
            "positive_tilted": decimal(tilted_pos),
            "negative_tilted": decimal(tilted_neg),
            "tilted_formula": decimal(tilted_formula),
        })

    # A finite honest Dirichlet polynomial tests the weighted mixed normalization.
    # This is not a truncated critical-strip zeta series.
    sigma, width, x = mp.mpf("0.6"), mp.mpf("1.7"), mp.mpf("2.3")
    coefficients = {2: mp.log(2), 3: mp.log(3), 4: mp.log(2)}
    direct = 2 * mp.quad(
        lambda t: sum(coeff * mp.power(n, -sigma)
                      * mp.cos(t * mp.log(x / n))
                      for n, coeff in coefficients.items())
        * packet(t, sigma, width),
        [0, width, 3 * width, mp.inf],
    )
    formula = sum(coeff * mp.power(n, -sigma)
                  * kernel(mp.log(n / x), sigma, width)
                  for n, coeff in coefficients.items())
    require_small(direct - formula)

    # Three finite-step centered Stieltjes identities, integrating at all jumps.
    stieltjes = []
    for x_s in ["1.3", "3", "7"]:
        x = mp.mpf(x_s)
        sigma, width = mp.mpf("0.6"), mp.mpf("1.2")
        a = 1 - sigma
        f = lambda y: y ** (-sigma) * kernel(mp.log(y / x), sigma, width)
        # For a finite atomic measure psi, extend E=psi-y to all y>0.
        atoms = [(mp.mpf(n), coeff) for n, coeff in coefficients.items()]
        psi = lambda y: sum(coeff for n, coeff in atoms if n <= y)
        direct_sum = sum(coeff * f(n) for n, coeff in atoms)
        # Logarithmic variable avoids arbitrary cutoffs at zero and infinity.
        def centered_integrand(z):
            y = x * mp.exp(z / width)
            b = a / width
            g = (1 + b * b - z * z) * mp.exp(-z * z / 2)
            gp = (z ** 3 - (3 + b * b) * z) * mp.exp(-z * z / 2)
            derivative_dz = mp.sqrt(2 * mp.pi) * y ** (-sigma) * (
                -sigma * g + width * gp
            )
            return -(psi(y) - y) * derivative_dz
        jumps = sorted(width * mp.log(n / x) for n, _ in atoms)
        integral = mp.quad(centered_integrand, [-mp.inf, *jumps, mp.inf])
        require_small(integral - direct_sum)
        stieltjes.append({
            "X": x_s, "finite_atom_sum": decimal(direct_sum),
            "centered_integral": decimal(integral),
            "absolute_difference": decimal(abs(integral - direct_sum)),
        })

    source = HERE / "POLE_ANNIHILATING_PACKET.md"
    output = {
        "status": "PASS",
        "scope": "Exact rational constants and high-precision diagnostics for a proved packet identity; no large-T zeta estimate, RH verification, interval certificate or conjecture claim.",
        "mpmath_version": mp.__version__, "decimal_precision": mp.mp.dps,
        "report_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "gaussian_moment_coefficients": [str(t) for t in q],
        "explicit_full_constant_upper": str(full_constant),
        "explicit_tail_constant_upper": str(tail_constant),
        "pole_checks": pole_checks, "fourier_checks": fourier_checks,
        "signed_mass_checks": masses,
        "finite_polynomial_mixed_check": {
            "direct": decimal(direct), "formula": decimal(formula),
            "absolute_difference": decimal(abs(direct - formula)),
        },
        "finite_atom_centered_checks": stieltjes,
        "limiting_single_signed_density_mass_coefficient": decimal(
            2 * mp.sqrt(2 * mp.pi / mp.e)
        ),
        "dense_continuum_cost_over_diagonal_coefficient": decimal(
            2 / (mp.sqrt(mp.e) * mp.log(2))
        ),
    }
    (HERE / "pole_packet_checks.json").write_text(
        json.dumps(output, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps({
        "status": "PASS", "report_sha256": output["report_sha256"],
        "fourier_checks": len(fourier_checks), "pole_checks": len(pole_checks),
        "mass_cases": len(masses), "centered_step_cases": len(stieltjes),
        "full_constant_upper": str(full_constant),
        "tail_constant_upper": str(tail_constant),
    }, indent=2))


if __name__ == "__main__":
    main()
