"""Exact checker extracted from AGENT_STOCHASTIC_PROTECTION.md for root replay."""
import sympy as s
from itertools import product

def h(z, r):
    return s.Add(*(
        s.prod(x**k for x, k in zip(z, ks))
        for ks in product(range(r + 1), repeat=len(z))
        if sum(ks) == r
    ))

def generator(f, z):
    n = len(z)
    e = lambda f, i: z[i] * s.diff(f, z[i])
    diffusion = -sum(e(e(f, i), i) for i in range(n))
    drift = -sum(
        (z[i] + z[j]) * (e(f, i) - e(f, j)) / (z[i] - z[j])
        for i in range(n) for j in range(i + 1, n)
    )
    return s.cancel((diffusion + drift) / (2 * n))

for n, r in [(2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 4)]:
    z = s.symbols('z:' + str(n))
    inv = tuple(1 / x for x in z)
    phi = h(z, r) * h(inv, r) - h(z, r-1) * h(inv, r-1)
    eigenvalue = s.Rational(r * (r + n - 1), n)
    residual = s.cancel(generator(phi, z) + eigenvalue * phi)
    print(f'N={n} r={r} Casimir={eigenvalue} residual={residual}')
    assert residual == 0
print('PASS: six exact Laurent-generator eigenfunction checks')
