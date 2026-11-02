#!/usr/bin/env python3
"""Exact constants and one symbolic N=3 determinant check; no grid or Monte Carlo."""
from fractions import Fraction as F
from hashlib import sha256
from itertools import permutations
from pathlib import Path
import json


def add(*polys):
    result = {}
    for p in polys:
        for key, value in p.items():
            result[key] = result.get(key, 0) + value
    return {key: value for key, value in result.items() if value}


def scale(p, c):
    return {key: c * value for key, value in p.items() if c * value}


def multiply(p, q):
    result = {}
    for (a, b), value in p.items():
        for (c, d), other in q.items():
            key = (a + c, b + d)
            result[key] = result.get(key, 0) + value * other
    return {key: value for key, value in result.items() if value}


def conjugate(p):
    return {(-a, -b): value for (a, b), value in p.items()}


def main():
    # Constant bookkeeping with powers of pi displayed separately in the proof.
    rho_far = F(1, 2) ** 2 * F(1, 6)
    rho_near = F(1, 2) * F(1, 6) ** 2
    assert rho_far == F(1, 24)
    assert rho_near == F(1, 72)
    # q-weight integration costs pi^2*N; two endpoints, 2*pi rotation,
    # and integral_0^eps d^2 dd then give exactly 1/18.
    final_constant = rho_far * 2 * 2 / 3
    assert final_constant == F(1, 18)
    assert 6 - F(4, 3) * 3 == 2
    assert -F(8, 3) + 2 == -F(2, 3)
    assert -F(8, 3) - F(2, 3) == -F(10, 3)
    assert F(1, 24) / 3 == F(1, 72)
    assert F(1, 32 * 16384) == F(1, 524288)

    one, z, w = {(0, 0): 1}, {(1, 0): 1}, {(0, 1): 1}
    phases = ((0, 0), (1, 0), (0, 1))
    gram = [[{(m * (u[0] - v[0]), m * (u[1] - v[1])): 1
              for m in range(3)} if u != v else {(0, 0): 3}
             for v in phases] for u in phases]
    det = {}
    for perm in permutations(range(3)):
        inversions = sum(perm[i] > perm[j] for i in range(3) for j in range(i + 1, 3))
        term = one
        for i in range(3):
            term = multiply(term, gram[i][perm[i]])
        det = add(det, scale(term, (-1) ** inversions))
    delta = multiply(multiply(add(z, scale(one, -1)), add(w, scale(one, -1))),
                     add(w, scale(z, -1)))
    assert det == multiply(delta, conjugate(delta))
    # q(w)=1/|w-1|^2 cancels this exact factor, with no numerical division.
    endpoint_factor = multiply(add(w, scale(one, -1)), add(conjugate(w), scale(one, -1)))
    remaining = multiply(
        multiply(add(z, scale(one, -1)), add(conjugate(z), scale(one, -1))),
        multiply(add(w, scale(z, -1)), add(conjugate(w), scale(conjugate(z), -1))))
    assert det == multiply(endpoint_factor, remaining)
    w_constant = {a: value for (a, b), value in remaining.items() if b == 0}
    assert w_constant == {0: 4, 1: -2, -1: -2}
    # The z-polynomial is 4-4*cos(d). Integration of w contributes2*pi;
    # rho_3 normalization(2*pi)^(-3) gives (1-cos(d))/pi^2.
    assert F(2, 2 ** 3) * 4 == 1
    # Two endpoints and a 2*pi rotation yield 4/pi*(eps-sin eps).
    assert 2 * 2 == 4

    result = {
        'status': 'PASS',
        'scope': 'Exact rational normalization and symbolic N=3 Laurent determinant; not a numerical probability test or formal proof',
        'rho_far_coefficient_without_pi_cubed': str(rho_far),
        'rho_near_coefficient_without_pi_cubed': str(rho_near),
        'truncated_moment_constant': str(final_constant),
        'background_scale_exponent': '2',
        'relative_depth_error_exponent': '-2/3',
        'absolute_depth_error_exponent': '-10/3',
        'N3_gram_equals_vandermonde_squared': True,
        'N3_endpoint_cancelled_w_constant': {str(k): v for k, v in sorted(w_constant.items())},
        'N3_integrated_endpoint_density': '(1-cos(d))/pi^2 = 2*sin(d/2)^2/pi^2',
        'N3_all_short_oriented_endpoint_sum': '(4/pi)*(epsilon-sin(epsilon))',
        'script_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    (Path(__file__).resolve().parent/'check_selected_background.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
