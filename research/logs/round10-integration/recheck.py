"""Replay two exact Round 10 checks without modifying archived evidence."""
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

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
ARCHIVE = ROOT / 'research/dyson/round10'


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def normalized(output):
    # The only variable fields in the completion output are these two
    # provenance paths. Their file hashes remain part of the comparison.
    output = json.loads(json.dumps(output))
    for key in ('primary_source', 'frozen_round9'):
        if key in output:
            output[key].pop('path')
    return output


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--prime-gap-source-dir', type=Path,
                        default=ROOT.parent / 'Astra-Local-Archive/round9-external-sources')
    args = parser.parse_args()
    intake = json.loads((ARCHIVE / 'INTAKE_MANIFEST.json').read_text())
    originals = {r['path']: r['sha256'] for r in intake['files'] if r['public']}
    for p, expected in originals.items():
        assert digest(ARCHIVE / p) == expected, p
    scripts = list(ARCHIVE.rglob('*.py'))
    for p in scripts:
        ast.parse(p.read_text(), filename=str(p))
    source = args.prime_gap_source_dir / 'openai-short-gaps.pdf'
    assert digest(source) == '456f05e0a3ef589ebb0e9abcfd31f140f3c945adbf6950e00ef371a3c88b0930'
    old = ROOT / 'research/dyson/round9/factorization-covariance/COMPLEMENTARY_MODULI_TYPE_I_BRIDGE.md'
    assert digest(old) == '982039f0e163b84c1c5b8f2b52f215eb40e7b89863085f2840c039853606f39a'
    result = {'scope': 'Exact finite algebra and source-range implications only; analytic bounds rely on written proofs and reviews.',
              'intake_public_files_verified': len(originals), 'python_files_parsed': len(scripts),
              'checks': {}, 'python': sys.version}
    with tempfile.TemporaryDirectory(prefix='astra-round10-replay-') as tmp:
        base = Path(tmp)
        copy = base / 'research-round10'
        shutil.copytree(ARCHIVE, copy, ignore=shutil.ignore_patterns('__pycache__'))
        (base / 'sources').mkdir()
        shutil.copy2(source, base / 'sources/openai-short-gaps.pdf')
        old_copy = base / 'research-round9/factorization-covariance' / old.name
        old_copy.parent.mkdir(parents=True)
        shutil.copy2(old, old_copy)
        for folder, script in [('shift-average', 'check_shift_completion.py'),
                               ('arithmetic-residual', 'check_edge_mixed_moment.py')]:
            proc = subprocess.run([sys.executable, script], cwd=copy / folder,
                                  env=dict(os.environ, PYTHONDONTWRITEBYTECODE='1'),
                                  capture_output=True, text=True)
            (HERE / (Path(script).stem + '.log')).write_text(proc.stdout + proc.stderr)
            assert proc.returncode == 0, (script, proc.returncode)
            output = Path(script).with_suffix('.json')
            expected = json.loads((ARCHIVE / folder / output).read_text())
            actual = json.loads((copy / folder / output).read_text())
            assert normalized(expected) == normalized(actual), script
            result['checks'][script] = {
                'identical_output': True,
                'excluded_fields': ['primary_source.path', 'frozen_round9.path']
                if folder == 'shift-average' else [],
            }
    assert all(digest(ARCHIVE / p) == h for p, h in originals.items())
    result['original_files_unchanged'] = True
    result['status'] = 'PASS'
    (HERE / 'recheck.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
