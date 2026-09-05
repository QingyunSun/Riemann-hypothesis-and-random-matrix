"""High-precision normalization checks, not a pair-correlation certificate.

The prime polynomial in the expansion check is explicitly truncated at 64.
The continuous mean is untruncated and includes the pole contribution exactly.
No asymptotic claim and no critical-line Dirichlet expansion are used.
"""
from pathlib import Path
import hashlib
import json
import mpmath as mp


def main():
    mp.mp.dps = 60
    mean_checks = []
    x = mp.mpf(8)

    def mean(t):
        return 2*x**(1-1j*t)/((mp.mpf('.5')+1j*t)*(mp.mpf('1.5')-1j*t))

    for t in map(mp.mpf, ['0', '.75', '2']):
        integral = x**(1-1j*t) * (
            mp.quad(lambda v: mp.exp((mp.mpf('1.5')-1j*t)*v), [-mp.inf, -256, -64, -16, -4, -1, 0])
            + mp.quad(lambda v: mp.exp((-mp.mpf('.5')-1j*t)*v), [0, 1, 4, 16, 64, 256, mp.inf]))
        error = abs(integral-mean(t))
        assert error < mp.mpf('1e-35')
        mean_checks.append({'t': str(t), 'absolute_error': mp.nstr(error, 20)})

    von_mangoldt = {}
    for p in range(2, 65):
        if all(p % d for d in range(2, int(p**.5)+1)):
            n = p
            while n <= 64:
                von_mangoldt[n] = mp.log(p)
                n *= p
    weights = {n: value*min(mp.sqrt(n/x), (x/n)**mp.mpf('1.5'))
               for n, value in von_mangoldt.items()}
    T = mp.mpf(3)
    segments = [mp.mpf(j)/2 for j in range(7)]

    def polynomial(t):
        return sum(value*mp.exp(-1j*t*mp.log(n)) for n, value in weights.items())

    direct = mp.quad(lambda t: abs(polynomial(t)-mean(t))**2, segments)
    diagonal = T*sum(value**2 for value in weights.values())
    pairs = sorted(weights)
    # Use mp ratios rather than Python float ratios.
    off_diagonal = sum(2*weights[m]*weights[n]*mp.sin(T*mp.log(mp.mpf(n)/m))/mp.log(mp.mpf(n)/m)
                       for j, m in enumerate(pairs) for n in pairs[j+1:])
    cross = -2*mp.re(mp.quad(lambda t: polynomial(t)*mp.conj(mean(t)), segments))
    mean_square = mp.quad(lambda t: abs(mean(t))**2, segments)
    expanded = diagonal+off_diagonal+cross+mean_square
    assert abs(direct-expanded) < mp.mpf('1e-45')

    p0_max = mp.mpf('1.5')-2/mp.pi**2
    # A symmetric normalized bump on (6/5,7/5) has mean 13/10.
    reference = {'bump_support': ['6/5', '7/5'], 'bump_integral': '1',
                 'mean_alpha': '13/10', 'GUE_target': '1', 'AH_pairs_target': '7/10',
                 'centered_off_diagonal_GUE_target': '-3/10',
                 'centered_off_diagonal_AH_target': '-3/5'}
    result = {'status': 'PASS: high-precision algebra/normalization checks only',
              'precision_decimal_digits': mp.mp.dps,
              'continuous_mean_checks': mean_checks,
              'finite_prime_check': {'x': str(x), 'T': str(T), 'truncation_n': 64,
                 'prime_power_terms': len(weights), 'direct_mean_square': mp.nstr(direct, 40),
                 'expanded_mean_square': mp.nstr(expanded, 40),
                 'absolute_error': mp.nstr(abs(direct-expanded), 20),
                 'diagonal': mp.nstr(diagonal, 30), 'off_diagonal': mp.nstr(off_diagonal, 30),
                 'mean_cross': mp.nstr(cross, 30), 'mean_square': mp.nstr(mean_square, 30),
                 'omitting_mean_changes_answer_by': mp.nstr(diagonal+off_diagonal-direct, 30)},
              'AH_p0_upper': mp.nstr(p0_max, 30),
              'CMR_long_average_bounds_compatible_with_entire_AH_p0_range':
                 bool(mp.mpf('.9303') < 1 < p0_max < mp.mpf('1.3208')),
              'chosen_target': reference,
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    path = Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
