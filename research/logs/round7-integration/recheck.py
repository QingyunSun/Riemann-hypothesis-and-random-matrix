"""Replay bounded Round7 checks in a copy, preserving all original outputs."""
from pathlib import Path
import ast
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
ARCHIVE = ROOT / 'research/dyson/round7'
SOURCE = ROOT / 'research/residual-gram/general_prime_features.py'
SOURCE_SHA = '29318c9b0176f7a056d0b1372a00c4f7ccea5228caa53d91882396a3e7556fdb'


def content_hash(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def without_timing(obj):
    if isinstance(obj, dict):
        return {k: without_timing(v) for k, v in obj.items()
                if k not in {'seconds', 'elapsed_seconds'}}
    if isinstance(obj, list):
        return [without_timing(v) for v in obj]
    return obj


def main():
    assert content_hash(SOURCE) == SOURCE_SHA
    before = {str(p.relative_to(ARCHIVE)): content_hash(p)
              for p in ARCHIVE.rglob('*') if p.is_file() and '__pycache__' not in p.parts}
    intake = json.loads((ARCHIVE / 'INTAKE_MANIFEST.json').read_text())
    for row in intake['files']:
        if row['public']:
            p = ARCHIVE / row['source_relative_path']
            assert content_hash(p) == row['public_sha256']
    extra = intake['additional_coordinator_certificate']
    assert content_hash(ARCHIVE / extra['relative_path']) == extra['sha256']
    scripts = sorted(ARCHIVE.rglob('*.py'))
    for p in scripts:
        ast.parse(p.read_text(), filename=str(p))
    receipt = {'scope': 'Bounded replay of exact identities and numerical witnesses; no new zeta bound or interval integration certificate.',
               'prior_arithmetic_source_sha256': SOURCE_SHA,
               'public_intake_hashes_verified': sum(row['public'] for row in intake['files']),
               'python_files_parsed': len(scripts), 'checks': {}}
    env = dict(os.environ, OPENBLAS_NUM_THREADS='1', PYTHONDONTWRITEBYTECODE='1',
               ASTRA_PRIME_FEATURES_SOURCE=str(SOURCE))
    with tempfile.TemporaryDirectory(prefix='astra-round7-replay-') as tmp:
        copy = Path(tmp) / 'round7'
        shutil.copytree(ARCHIVE, copy, ignore=shutil.ignore_patterns('__pycache__'))

        def run(folder, script, *args):
            result = subprocess.run([sys.executable, script, *args], cwd=copy / folder,
                                    env=env, capture_output=True, text=True)
            (HERE / f'{Path(script).stem}.log').write_text(result.stdout + result.stderr)
            assert result.returncode == 0, (script, result.returncode)

        def compare(folder, output):
            a = json.loads((ARCHIVE / folder / output).read_text())
            b = json.loads((copy / folder / output).read_text())
            assert without_timing(a) == without_timing(b), (folder, output)
            receipt['checks'][f'{folder}/{output}'] = 'identical JSON after removing only timing fields'

        for folder, script, output in [
            ('poisson-resolvent', 'poisson_checks.py', 'poisson_checks.json'),
            ('poisson-resolvent', 'two_scale_certificate.py', 'two_scale_certificate.json'),
            ('true-zeta-flow', 'forward_flow_checks.py', 'forward_flow_checks.json'),
            ('dyson-frontier', 'kernel_identity_check.py', 'kernel_identity_check.json'),
            ('arithmetic-resonator', 'independent_identity_checks.py', 'independent_identity_checks.json'),
            ('arithmetic-resonator', 'validate_sector.py', 'validation.json'),
        ]:
            run(folder, script)
            compare(folder, output)
        folder = 'arithmetic-resonator'
        run(folder, 'large_prime_sector.py', '--order', '40', '--degree', '4')
        compare(folder, 'large_prime_sector_d4_q40.json')
        with np.load(ARCHIVE / folder / 'large_prime_sector_d4_q40.npz', allow_pickle=False) as old, \
             np.load(copy / folder / 'large_prime_sector_d4_q40.npz', allow_pickle=False) as new:
            assert old.files == new.files
            for key in old.files:
                assert np.array_equal(old[key], new[key]), key
            receipt['matrix_replay'] = {'order': 40, 'identical_arrays': old.files}
        run(folder, 'finite_integer_check.py')
        compare(folder, 'fixed_rational_vector.json')
        compare(folder, 'finite_integer_results.json')
    assert all(content_hash(ARCHIVE / p) == h for p, h in before.items())
    receipt['original_files_unchanged'] = len(before)
    receipt['status'] = 'PASS'
    (HERE / 'recheck.json').write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps(receipt, indent=2))


if __name__ == '__main__':
    main()
