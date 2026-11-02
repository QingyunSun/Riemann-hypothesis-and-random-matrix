"""One bounded Round 9 replay in a temporary copy; originals remain unchanged."""
from pathlib import Path
import argparse
import ast
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile

import numpy as np
import scipy

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
ARCHIVE = ROOT / 'research/dyson/round9'


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def comparable(value):
    if isinstance(value, dict):
        return {k: comparable(v) for k, v in value.items()
                if k not in ('seconds', 'local_file')}
    if isinstance(value, list):
        return [comparable(v) for v in value]
    return value


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--prime-gap-source-dir', type=Path,
                        default=ROOT.parent / 'Astra-Local-Archive/round9-external-sources')
    args = parser.parse_args()
    intake = json.loads((ARCHIVE / 'INTAKE_MANIFEST.json').read_text())
    originals = {r['path']: r['sha256'] for r in intake['files'] if r['public']}
    for path, expected in originals.items():
        assert digest(ARCHIVE / path) == expected, path
    for row in intake['external_references']:
        assert digest(args.prime_gap_source_dir / row['filename']) == row['sha256']
    scripts = list(ARCHIVE.rglob('*.py'))
    for p in scripts:
        ast.parse(p.read_text(), filename=str(p))
    result = {'scope': 'Fixed arithmetic identities, one q32 quadrature replay, and saved-array checks; no new zeta bound.',
              'python': sys.version, 'numpy': np.__version__, 'scipy': scipy.__version__,
              'intake_public_files_verified': len(originals), 'python_files_parsed': len(scripts),
              'excluded_comparison_fields': ['seconds', 'sources[].local_file'], 'checks': {}}
    with tempfile.TemporaryDirectory(prefix='astra-round9-replay-') as tmp:
        copy = Path(tmp) / 'round9'
        shutil.copytree(ARCHIVE, copy, ignore=shutil.ignore_patterns('__pycache__'))
        # The unmodified author's bridge script expects its two primary source
        # files beside the round folder. Verify their hashes before staging.
        source_dir = Path(tmp) / 'sources'
        source_dir.mkdir()
        for row in intake['external_references']:
            shutil.copy2(args.prime_gap_source_dir / row['filename'], source_dir / row['filename'])
        env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1',
                   OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1',
                   ASTRA_LARGE_PRIME_SOURCE=str(ROOT / 'research/dyson/round7/arithmetic-resonator/large_prime_sector.py'))
        runs = [
            ('multiplicative-profile', 'two_large_prime_sector.py', ['--order', '32'], ['two_large_prime_d4_q32.json']),
            ('multiplicative-profile', 'check_two_prime_trial.py', [], ['validation.json', 'fixed_rational_vector.json']),
            ('mesoscopic-edge', 'edge_identity_checks.py', [], ['edge_identity_checks.json']),
            ('factorization-covariance', 'check_divisor_bridge.py', [], ['check_divisor_bridge.json']),
        ]
        for folder, script, argv, outputs in runs:
            proc = subprocess.run([sys.executable, script, *argv], cwd=copy / folder,
                                  env=env, capture_output=True, text=True)
            (HERE / (Path(script).stem + '.log')).write_text(proc.stdout + proc.stderr)
            assert proc.returncode == 0, (script, proc.returncode)
            for output in outputs:
                expected = json.loads((ARCHIVE / folder / output).read_text())
                actual = json.loads((copy / folder / output).read_text())
                assert comparable(expected) == comparable(actual), (script, output)
                result['checks'][folder + '/' + output] = 'identical except declared metadata exclusions'
        arrays = {}
        for order in (20, 32):
            file = f'multiplicative-profile/two_large_prime_d4_q{order}.npz'
            with np.load(ARCHIVE / file) as saved, np.load(copy / file) as fresh:
                assert sorted(saved.files) == ['G', 'M'] == sorted(fresh.files)
                for key in saved.files:
                    assert np.array_equal(saved[key], fresh[key])
                    assert saved[key].shape == (30, 30)
                    assert np.isfinite(saved[key]).all()
                    assert np.array_equal(saved[key], saved[key].T)
                arrays[str(order)] = {'M_and_G_symmetric_finite': True,
                                      'shape': [30, 30],
                                      'recomputed_this_replay': order == 32,
                                      'exact_array_agreement': True}
        result['matrix_checks'] = arrays
    assert all(digest(ARCHIVE / p) == h for p, h in originals.items())
    result['original_files_unchanged'] = True
    result['status'] = 'PASS'
    (HERE / 'recheck.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
