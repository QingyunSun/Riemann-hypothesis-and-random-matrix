#!/usr/bin/env python3
"""Exact elementary transform checks, not analytic or numerical zeta proof."""
from pathlib import Path
import hashlib
import json
import sympy as sp


def main() -> None:
    y, lam, cut, delta, height = sp.symbols("y lambda L delta T", positive=True)
    cosine_laplace = sp.integrate(sp.exp(-lam) * sp.cos(lam * y), (lam, 0, sp.oo))
    kernel = sp.simplify((1 - cosine_laplace) / (2 * y**2))
    density = -4 / sp.pi * y * sp.diff(kernel, y)
    mass = sp.integrate(density, (y, 0, sp.oo))
    cumulative = 2 / sp.pi * (sp.atan(y) - y / (1 + y**2))
    mean_length = sp.integrate(lam * sp.exp(-lam), (lam, 0, sp.oo))
    length_tail = sp.integrate(lam * sp.exp(-lam), (lam, cut, sp.oo))
    s_value = 1 / (sp.exp(delta) - 1)
    kappa = sp.simplify(sp.log(1 + 1 / s_value) / 2)
    assertions = {
        "cosine_laplace": sp.simplify(cosine_laplace - 1 / (1 + y**2)) == 0,
        "averaged_kernel": sp.simplify(kernel - 1 / (2 * (1 + y**2))) == 0,
        "kernel_zero_value": sp.limit(kernel, y, 0) == sp.Rational(1, 2),
        "density": sp.simplify(density - 4 * y**2 / (sp.pi * (1 + y**2)**2)) == 0,
        "density_mass_one": sp.simplify(mass - 1) == 0,
        "cdf_derivative": sp.simplify(sp.diff(cumulative, y) - density) == 0,
        "expected_length_one": mean_length == 1,
        "arithmetic_tail_factor": sp.simplify(length_tail - (cut + 1) * sp.exp(-cut)) == 0,
        "exact_log_interval": sp.simplify(1 + 1 / s_value - sp.exp(delta)) == 0,
        "exact_kappa": sp.simplify(kappa - delta / 2) == 0,
        "density_half_endpoint": sp.simplify(density.subs(y, sp.Rational(1, 2)) - 16 / (25 * sp.pi)) == 0,
        "density_two_endpoint": sp.simplify(density.subs(y, 2) - 16 / (25 * sp.pi)) == 0,
        "density_derivative": sp.simplify(sp.diff(density, y) - 8 * y * (1 - y**2) / (sp.pi * (1 + y**2)**3)) == 0,
    }
    report = Path(__file__).with_name("EXPONENTIAL_LENGTH_AVERAGE.md")
    result = {
        "status": "PASS" if all(assertions.values()) else "FAIL",
        "scope": "Exact symbolic elementary kernels and reparameterization only. No analytic error estimate, zeta theorem, numerical sweep, or gain enclosure is verified by this script.",
        "sympy_version": sp.__version__,
        "checks": assertions,
        "expressions": {
            "kernel": str(kernel),
            "height_density": str(sp.factor(density)),
            "density_mass": str(mass),
            "density_cdf": str(cumulative),
            "length_tail": str(length_tail),
            "kappa": str(kappa),
        },
        "author_report_sha256": hashlib.sha256(report.read_bytes()).hexdigest(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    Path(__file__).with_name("length_kernel_checks.json").write_text(payload)
    print(payload, end="")
    if not all(assertions.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
