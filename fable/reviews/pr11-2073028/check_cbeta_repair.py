"""Small exact algebra checks for the independent 2073028 Cbeta review."""
from pathlib import Path
import json
import sympy as s


def main():
    q, u, v, eps, w, delta = s.symbols('q u v eps w delta', positive=True)
    finite = []
    for n in (2, 3, 5):
        normalized = 1 - (s.sin(q / 2) / (n * s.sin(q / (2 * n)))) ** 2
        coefficient = s.simplify(s.limit(normalized / q**2, q, 0))
        expected = (1 - s.Rational(1, n*n)) / 12
        assert coefficient == expected
        assert s.simplify(normalized.subs(q, 2 * s.pi)) == 1
        finite.append({'N': n, 'q2_coefficient': str(coefficient), 'density_at_q_2pi': '1'})
    assert s.sin(s.pi) == 0
    integrals = {}
    for beta in (1, 2, 4):
        integral = s.integrate(u**beta * v**beta * (u+v)**beta, (v, 0, w), (u, 0, eps))
        leading = s.simplify(s.limit(integral / eps**(beta+1), eps, 0))
        assert leading == w**(2*beta+1) / ((beta+1)*(2*beta+1))
        integrals[str(beta)] = str(s.expand(integral))
    expected_beta2 = eps**3*w**5/15 + eps**4*w**4/8 + eps**5*w**3/15
    assert s.simplify(s.sympify(integrals['2'], locals={'eps': eps, 'w': w}) - expected_beta2) == 0
    # u=eps/2, v=eps**2/w, eps=delta*w: v'/v diverges as delta -> 0.
    ratio = s.simplify(((eps/2 + eps**2/w) / (eps**2/w)).subs(eps, delta*w))
    assert s.limit(ratio, delta, 0, dir='+') == s.oo
    result = {
        'status': 'PASS', 'scope': 'Exact finite algebra only; no Cbeta density theorem or stochastic simulation.',
        'sympy_version': s.__version__, 'finite_CUE': finite,
        'triple_integrals': integrals, 'nonuniform_distance_ratio': str(ratio),
        'partition_N2_beta2_actual_over_2pi_squared': 2,
        'partition_N2_beta2_source_over_2pi_squared': 4,
    }
    output = Path(__file__).with_suffix('.json')
    output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
