"""Bounded Round8 replay plus an exact prime-power endpoint convention check."""
from fractions import Fraction as F
from pathlib import Path
import ast
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
ARCHIVE = ROOT / 'research/dyson/round8'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def endpoint_checks():
    # Rational formal prime-power weights; the Stieltjes identity holds for any
    # finite measure. This checks integer endpoints without floating logarithms.
    atoms = {2: 2, 3: 3, 4: 2, 8: 2, 9: 3, 16: 2, 27: 3, 32: 2, 37: 37}
    rows = []
    for cutoff in (31, 32, 37, 40):
        for exponent in (2, 3):
            x = F(cutoff)
            psi = F(sum(w for n, w in atoms.items() if n <= cutoff))
            psi_x = psi
            left = x
            integral = F(0)
            for n, weight in sorted(atoms.items()):
                if n <= cutoff:
                    continue
                right = F(n)
                integral += psi * (left**(-exponent) - right**(-exponent)) / exponent
                integral -= (right**(1-exponent) - left**(1-exponent)) / (1-exponent)
                psi += weight
                left = right
            integral += psi * left**(-exponent) / exponent - left**(1-exponent)/(exponent-1)
            partial = sum((F(w) * F(n)**(-exponent) for n, w in atoms.items() if n <= cutoff), F(0))
            lhs = sum((F(w) * F(n)**(-exponent) for n, w in atoms.items()), F(0))
            rhs = partial + x**(1-exponent)/(exponent-1) - (psi_x-x)*x**(-exponent) + exponent*integral
            assert lhs == rhs
            omitted = F(atoms.get(cutoff, 0)) * x**(-exponent)
            if cutoff in atoms:
                assert rhs + omitted != lhs
            rows.append({'cutoff': cutoff, 'exponent': exponent, 'exact_difference': str(rhs-lhs),
                         'endpoint_atom_error_if_only_endpoint_uses_left_limit': str(omitted)})
    return rows


def main():
    intake = json.loads((ARCHIVE/'INTAKE_MANIFEST.json').read_text())
    before = {}
    for row in intake['files']:
        p = ARCHIVE / row['path']
        assert p.stat().st_size == row['bytes'] and digest(p) == row['sha256']
        before[row['path']] = row['sha256']
    scripts = list(ARCHIVE.rglob('*.py'))
    for p in scripts:
        ast.parse(p.read_text(), filename=str(p))
    result = {'scope': 'Exact scalar/finite identities and fixed symbolic replay; no asymptotic zeta lower bound.',
              'intake_files_verified': len(before), 'python_files_parsed': len(scripts),
              'checks': {}, 'independent_exact_endpoint_cases': endpoint_checks()}
    with tempfile.TemporaryDirectory(prefix='astra-round8-replay-') as tmp:
        copy = Path(tmp)/'round8'
        shutil.copytree(ARCHIVE, copy, ignore=shutil.ignore_patterns('__pycache__'))
        for folder, script in [('resolvent-arithmetic', 'check_centered_tail.py'),
                               ('spectral-positivity', 'minorant_symbolic_check.py')]:
            proc = subprocess.run([sys.executable, script], cwd=copy/folder,
                                  env=dict(os.environ, PYTHONDONTWRITEBYTECODE='1'),
                                  capture_output=True, text=True)
            (HERE/(Path(script).stem+'.log')).write_text(proc.stdout+proc.stderr)
            assert proc.returncode == 0, (script, proc.returncode)
            output = Path(script).with_suffix('.json')
            expected = json.loads((ARCHIVE/folder/output).read_text())
            actual = json.loads((copy/folder/output).read_text())
            assert expected == actual, script
            result['checks'][script] = 'identical complete JSON; no fields excluded'
    assert all(digest(ARCHIVE/p) == h for p, h in before.items())
    result['original_files_unchanged'] = True
    result['status'] = 'PASS'
    (HERE/'recheck.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
