#!/usr/bin/env python3
"""Independent copied replay and byte-level provenance check; no numeric scan."""
from __future__ import annotations

import hashlib
import json
import platform
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else HERE.parents[1]
AUTHOR = BASE / 'research-round27/joint-dispersion-test'


def digest(path: Path) -> dict:
    data = path.read_bytes()
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}


def verify(entry: dict, base: Path) -> dict:
    actual = digest(base / entry['path'])
    ok = all(actual[key] == entry[key] for key in ('bytes', 'sha256'))
    return {'path': entry['path'], 'matches': ok, **actual}


author_receipt = json.loads((AUTHOR / 'AUTHOR_RECEIPT.json').read_text())
source_receipt = json.loads((AUTHOR / 'source_manifest.json').read_text())
author_checks = [verify(x, AUTHOR) for x in author_receipt['files']]
source_checks = [verify(x, BASE) for x in source_receipt['files']]
assert all(x['matches'] for x in author_checks + source_checks)

with tempfile.TemporaryDirectory(prefix='r27-independent-joint-') as work:
    work = Path(work)
    for name in ('JOINT_DISPERSION_TEST.md', 'check_joint_dispersion.py'):
        shutil.copyfile(AUTHOR / name, work / name)
    result = subprocess.run(
        [sys.executable, str(work / 'check_joint_dispersion.py')],
        cwd=work, capture_output=True, check=True,
    )
    output = (work / 'exact_check_results.json').read_bytes()
    assert result.stderr == b''
    assert output == result.stdout
    assert output == (AUTHOR / 'exact_check_results.json').read_bytes()
    assert output == (AUTHOR / 'exact_check_stdout.log').read_bytes()
    (HERE / 'independent_exact_check_results.json').write_bytes(output)
    (HERE / 'independent_exact_check_stdout.log').write_bytes(result.stdout)

parsed = json.loads(output)
assert parsed['status'] == 'PASS' and parsed['total_scalar_cases'] == 26
checks = {
    'status': 'PASS',
    'scope': 'Six tiny exact groups only. No asymptotic proof or matrix norm is inferred from finite tests.',
    'python_version': platform.python_version(),
    'author_manifest': digest(AUTHOR / 'AUTHOR_RECEIPT.json'),
    'source_manifest': digest(AUTHOR / 'source_manifest.json'),
    'author_files': author_checks,
    'source_files': source_checks,
    'copied_replay': {
        'temporary_copy_only': True,
        'author_directory_unmodified': True,
        'stderr_empty': True,
        'json_equals_stdout': True,
        'json_equals_author_json': True,
        'stdout_equals_author_stdout': True,
        'check_groups': len(parsed['check_groups']),
        'scalar_cases': parsed['total_scalar_cases'],
        'output': digest(HERE / 'independent_exact_check_results.json'),
    },
}
encoded = json.dumps(checks, indent=2, sort_keys=True) + '\n'
(HERE / 'source_and_replay_checks.json').write_text(encoded)
print(json.dumps({
    'status': 'PASS', 'author_files': len(author_checks),
    'source_files': len(source_checks), 'scalar_cases': 26,
    'output': checks['copied_replay']['output'],
}, indent=2))
