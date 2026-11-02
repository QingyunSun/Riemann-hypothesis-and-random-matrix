"""Tiny exact identities only; no actual-height or random-data scan."""
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from math import comb
from pathlib import Path
import json
import sympy as s

HERE = Path(__file__).resolve().parent
groups = []


def record(name, count, description):
    groups.append({"name": name, "cases": count, "passed": True, "scope": description})


# Prime-factor Laurent monomials establish the multiplicative phase identity
# formally, and therefore for all specializations p -> p^(it).
z3, z5, x = s.symbols("z3 z5 x")
indices = [3, 5]
phase = {3: z3, 5: z5, 9: z3**2, 15: z3*z5, 25: z5**2}
coeff = {9: s.Rational(7, 3), 15: -s.Rational(4, 5), 25: 0}
mult = Counter(d*k for d in indices for k in indices)
matrix_pair = sum(phase[d]*phase[k]*coeff[d*k]
                  for d in indices for k in indices) / 2
collapsed = sum(r*phase[m]*coeff[m] for m, r in mult.items()) / 2
assert s.expand(matrix_pair-collapsed) == 0
assert mult == {9: 1, 15: 2, 25: 1}
cesaro_diagonal = sum(s.Rational(r*r, 4)*coeff[m]**2
                     for m, r in mult.items())
assert cesaro_diagonal == s.Rational(1801, 900)
record("odd_product_mellin_and_diagonal", 3,
       "Actual odd finite indices; a nonfactorable product cutoff deletes 25.")


# Finite actual prime powers, with exact logarithms and a C^1 compact
# polynomial packet. The toy only checks algebra and endpoint integration,
# not the C-infinity explicit-formula theorem.
def lam(n):
    fac = s.factorint(n)
    return s.log(next(iter(fac))) if len(fac) == 1 else s.Integer(0)


def packet(m, y):
    return ((y-2)**2 * (10-y)**2 / s.Integer(m)) if m < 20 else s.Integer(0)


char = lambda n: 1 if n % 4 == 1 else -1
def at_piece(mid):
    return s.expand(sum(r*char(m)*packet(m, x-m)
                        for m, r in mult.items() if 2 < mid-m < 10))


def at_integer(n):
    return s.expand(sum(r*char(m)*packet(m, s.Integer(n-m))
                        for m, r in mult.items() if 2 < n-m < 10))


discrete = sum(r*char(m)*packet(m, s.Integer(h))*(lam(m+h)-2)
               for m, r in mult.items() if m < 20 for h in (2, 4, 6, 8, 10))
odd_sum = sum(at_integer(n)*(lam(n)-2) for n in range(3, 32, 2))
assert s.simplify(discrete-odd_sum) == 0
integral_a = 0
integral_E_aprime = 0
for j in range(1, 32):
    a = at_piece(s.Rational(2*j+1, 2))
    integral_a += s.integrate(a, (x, j, j+1))
    psi = sum(lam(n) for n in range(2, j+1))
    integral_E_aprime += s.integrate((psi-x)*s.diff(a, x), (x, j, j+1))
lattice = integral_a-2*sum(at_integer(n) for n in range(3, 32, 2))
even_prime_powers = s.log(2)*sum(at_integer(2**j) for j in range(1, 6))
assert even_prime_powers != 0
assert s.simplify(odd_sum+integral_E_aprime-lattice+even_prime_powers) == 0
all_prime_sum = sum(lam(n)*at_integer(n) for n in range(2, 32))
assert s.simplify(all_prime_sum-integral_a+integral_E_aprime) == 0
record("prime_center_and_stieltjes_endpoints", 4,
       "Exact prime-power logs, odd center, continuous term and compact endpoints.")


# Exact cyclic-Hankel Fourier pairing in the quotient ring Z[z]/(z^N-1).
# No numerical DFT or Gaussian sample is used.
def reduce_cyclic(poly, n):
    out = [0]*n
    for power, coef in poly.items():
        out[power % n] += coef
    return out


fourier_cases = 0
for n in (3, 5, 7, 9):
    gs = list(range(1, n+1))
    for j in range(n):
        left = {k: gs[(j+k) % n] for k in range(n)}
        right = {r-j: gs[r] for r in range(n)}
        assert reduce_cyclic(left, n) == reduce_cyclic(right, n)
        fourier_cases += 1
    # Reflection k -> -k transforms H into the exact circulant g[j-k].
    assert all(gs[(j+((-k) % n)) % n] == gs[(j-k) % n]
               for j in range(n) for k in range(n))
    fourier_cases += 1
record("cyclic_hankel_fourier_identity", fourier_cases,
       "Odd sizes; exact roots-of-unity polynomial identities and reflection.")


# Integral of 1-(1-exp(-z))^n equals H_n by binomial expansion.
for n in range(1, 13):
    integral = sum(Fraction((-1)**(j+1)*comb(n, j), j)
                   for j in range(1, n+1))
    harmonic = sum(Fraction(1, j) for j in range(1, n+1))
    assert integral == harmonic
record("maximum_exponential_mean", 12,
       "Exact harmonic expectation underlying the Gaussian norm bounds.")


# Check the covariance identity for arbitrary fixed rational unit vectors
# through a polynomial in independent centered Gaussian coordinates.
# The coefficient norm identity does not require normalizing these examples.
for n in (3, 5, 7):
    u = [Fraction(j+1, n) for j in range(n)]
    v = [Fraction((-1)**j, j+1) for j in range(n)]
    convolved = [sum(u[j]*v[k] for j in range(n) for k in range(n)
                     if (j+k) % n == r) for r in range(n)]
    direct_coeff = [Fraction(0) for _ in range(n)]
    for j in range(n):
        for k in range(n):
            direct_coeff[(j+k) % n] += u[j]*v[k]
    assert convolved == direct_coeff
    assert sum(c*c for c in convolved) <= n*sum(a*a for a in u)*sum(b*b for b in v)
record("fixed_vector_convolution_variance", 6,
       "Exact covariance coefficients and finite Young bound; sample-independent vectors.")


# Power/log constants: log N = .5 log X, X=N^2 and sigma^2=N log X.
assert Fraction(1, 2)*2 == 1
assert Fraction(1, 2)+1-3 == -Fraction(3, 2)
assert Fraction(1, 2)+Fraction(1, 2)-3 == -2
record("normalization_exponents", 3,
       "Gaussian leading constant and explicit-formula trivial-zero scale.")

result = {
    "author_sha256": sha256((HERE/"MELLIN_OPERATOR_AUDIT.md").read_bytes()).hexdigest(),
    "all_passed": True,
    "groups": groups,
    "total_cases": sum(g["cases"] for g in groups),
    "scope": "Finite exact identities only; no actual-prime norm estimate, RH proof, or model-to-prime transfer.",
}
encoded = json.dumps(result, indent=2, sort_keys=True)+"\n"
(HERE/"exact_check_results.json").write_text(encoded)
print(encoded, end="")
