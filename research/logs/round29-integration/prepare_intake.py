"""Preserve R29 verbatim and validate only dependencies named by its receipts.

No mathematical replay, numerical experiment, Git mutation, historical manifest
audit, or PDF build is performed by this publication preparation script.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
from pathlib import Path

REPO = Path('/Users/qingyunsun/Library/CloudStorage/Dropbox/Code/Riemann zeta RMT/Astra-Research')
STAGE = Path('/Users/qingyunsun/Library/CloudStorage/Dropbox/Research/ACUE-Astra-Handoff-2026-09-04')
SOURCE = STAGE / 'research-round29'
PUBLIC = REPO / 'research/dyson/round29'
ARCHIVE = REPO.parent / 'Astra-Local-Archive/round29-originals'
LOGS = REPO / 'research/logs/round29-integration'
CACHE: dict[Path, dict] = {}


def digest(path: Path) -> dict:
    path = path.resolve()
    if path not in CACHE:
        data = path.read_bytes()
        CACHE[path] = {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}
    return CACHE[path]


def save(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + '\n')


def preserve(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists():
        assert dst.read_bytes() == src.read_bytes(), f'Refuse to replace differing bytes: {dst}'
    else:
        shutil.copyfile(src, dst)
    assert digest(dst) == digest(src)


def local_only(path: Path) -> bool:
    return 'sources' in path.parts and path.suffix.lower() in {'.pdf', '.txt', '.png'}


originals = sorted(path for path in SOURCE.rglob('*') if path.is_file())
assert all('__pycache__' not in path.parts for path in originals)
PUBLIC.mkdir(parents=True, exist_ok=True)
ARCHIVE.mkdir(parents=True, exist_ok=True)
intake = []
for path in originals:
    rel = path.relative_to(SOURCE)
    preserve(path, ARCHIVE / rel)
    include = not local_only(rel)
    if include:
        preserve(path, PUBLIC / rel)
    intake.append({'path': str(rel), **digest(path), 'public_verbatim': include,
                   'omission_reason': None if include else 'Full primary reference body or page image; retained byte-for-byte in the adjacent local archive.'})
public_rows = [row for row in intake if row['public_verbatim']]
manifest = {
    'original_files': len(intake), 'original_bytes': sum(row['bytes'] for row in intake),
    'public_verbatim_files': len(public_rows),
    'public_verbatim_bytes': sum(row['bytes'] for row in public_rows),
    'source_edits': [], 'files': intake,
}
save(PUBLIC / 'INTAKE_MANIFEST.json', manifest)


def walk_records(value, trail=()):
    if isinstance(value, dict):
        if isinstance(value.get('sha256'), str) and isinstance(value.get('bytes'), int):
            declared = value.get('path')
            if declared is None and trail and re.search(r'\.(md|json|py|cjs|pdf|txt|png|log)$', trail[-1]):
                declared = trail[-1]
            yield declared, value, trail
        for key, child in value.items():
            yield from walk_records(child, (*trail, key))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from walk_records(child, (*trail, str(index)))


def expected_matches(path: Path, entry: dict) -> bool:
    return path.is_file() and digest(path) == {key: entry[key] for key in ('bytes', 'sha256')}


def canonical_path(path: Path) -> Path | None:
    try:
        stage_rel = path.relative_to(STAGE)
    except ValueError:
        return None
    match = re.fullmatch(r'research-round(\d+)', stage_rel.parts[0])
    if not match:
        return None
    return REPO / 'research/dyson' / ('round' + match.group(1)) / Path(*stage_rel.parts[1:])


checks, unresolved = [], []
for receipt in sorted(SOURCE.rglob('*.json')):
    parsed = json.loads(receipt.read_text())
    for declared, entry, trail in walk_records(parsed):
        candidates = []
        if declared:
            target = Path(declared)
            candidates = [target] if target.is_absolute() else [receipt.parent / target, STAGE / target, SOURCE / target]
        exact = next((path.resolve() for path in candidates if expected_matches(path, entry)), None)
        substituted = False
        if exact is None:
            exact = next((path.resolve() for path in originals if expected_matches(path, entry)), None)
            substituted = exact is not None and declared is not None
        if exact is None:
            unresolved.append({'receipt': str(receipt.relative_to(SOURCE)), 'json_location': '/'.join(trail),
                               'declared_path': declared, 'bytes': entry['bytes'], 'sha256': entry['sha256']})
            continue
        mapped = canonical_path(exact)
        if mapped is None or not expected_matches(mapped, entry):
            mapped = next((PUBLIC / Path(row['path']) for row in public_rows
                           if row['bytes'] == entry['bytes'] and row['sha256'] == entry['sha256']), None)
        checks.append({'receipt': str(receipt.relative_to(SOURCE)), 'json_location': '/'.join(trail),
                       'declared_path': declared, 'verified_path': str(exact),
                       'bytes': entry['bytes'], 'sha256': entry['sha256'],
                       'exact_byte_path_substitute': substituted,
                       'public_counterpart': str(mapped.relative_to(REPO)) if mapped else None,
                       'local_reference_only': mapped is None})
save(LOGS / 'DEPENDENCY_HASH_CHECK.json', {
    'status': 'PASS' if not unresolved else 'FAIL', 'checked_records': len(checks),
    'scope': 'Only SHA256/byte records explicitly contained in newly received R29 JSON; referenced older files are read only and are not mathematically replayed.',
    'checks': checks, 'unresolved': unresolved,
})
assert not unresolved, unresolved

# Keep the source-relative references readable without editing original prose.
links, link_unresolved = [], []
for source in sorted(SOURCE.rglob('*.md')):
    text = source.read_text()
    targets = set(re.findall(r'\]\(([^)]+)\)', text))
    targets.update(re.findall(r'`([^`\n]+\.(?:md|json|py|cjs|log))`', text))
    for target in sorted(targets):
        if target.startswith(('http:', 'https:', '#')):
            continue
        candidate = (source.parent / target).resolve()
        if not candidate.is_file():
            candidate = (STAGE / target).resolve()
        if not candidate.is_file():
            link_unresolved.append({'source': str(source.relative_to(SOURCE)), 'target': target})
            continue
        counterpart = canonical_path(candidate)
        if counterpart is not None and counterpart.is_file() and digest(counterpart) == digest(candidate):
            result = {'public': str(counterpart.relative_to(REPO)),
                      'relative_public_link': os.path.relpath(counterpart, PUBLIC)}
        else:
            result = {'local': str(candidate)}
        links.append({'source': str(source.relative_to(SOURCE)), 'original_target': target, **result})
save(LOGS / 'SOURCE_LINK_CHECK.json', {'status': 'PASS' if not link_unresolved else 'FAIL',
     'links': links, 'unresolved': link_unresolved})
lines = ['# Source-relative link map', '',
         'Original source files remain byte for byte unchanged. Historical submission-time status is retained; separate review receipts record acceptance. Referenced primary bodies remain local with public hashes. Existing scripts preserve their original staging paths and are not silently rewritten for a different working directory.', '',
         '| Archived source | Original target | Exact-byte public counterpart or local status |',
         '|---|---|---|']
for row in links:
    dest = f"[{row['public']}]({row['relative_public_link']})" if 'public' in row else 'Local reference: ' + row['local']
    lines.append(f"| {row['source']} | {row['original_target']} | {dest} |")
(PUBLIC / 'SOURCE_LINK_MAP.md').write_text('\n'.join(lines) + '\n')
assert not link_unresolved, link_unresolved

replay_pairs = []
for author_folder, review_folder, author_base, review_base in (
    ('signed-mellin-test', 'signed-mellin-review', 'exact_check_results.json', 'independent_exact_check_results.json'),
    ('signed-mellin-test', 'signed-mellin-review', 'exact_check_stdout.log', 'independent_exact_check_stdout.log'),
    ('mellin-energy-support', 'mellin-energy-review', 'mellin_energy_checks.json', 'mellin_energy_checks.json'),
    ('mellin-energy-support', 'mellin-energy-review', 'mellin_energy_checks.log', 'mellin_energy_checks.log'),
):
    author = Path(author_folder) / author_base
    independent = Path(review_folder) / review_base
    assert (SOURCE / author).read_bytes() == (SOURCE / independent).read_bytes()
    replay_pairs.append({'author': str(author), 'independent': str(independent),
                         **digest(SOURCE / author), 'byte_identical': True})
projection = SOURCE / 'input-plane-review/exact_projection_checks.json'
assert projection.read_bytes() == (projection.parent / 'exact_projection_checks.log').read_bytes()
receipt = {
    'status': 'PASS',
    **{key: manifest[key] for key in ('original_files', 'original_bytes', 'public_verbatim_files', 'public_verbatim_bytes')},
    'local_only_primary_files': sum(not row['public_verbatim'] for row in intake),
    'dependency_records_verified': len(checks),
    'exact_byte_path_substitutes': sum(row['exact_byte_path_substitute'] for row in checks),
    'unresolved_dependencies': unresolved,
    'existing_bounded_replays': replay_pairs,
    'complete_replay_pairs': 2,
    'bounded_checks': 'Existing final 147-case signed replay and 13-assertion energy replay; complete outputs compared unchanged. Existing 12-assertion input-plane JSON/stdout also verified identical. No checker rerun for publication preparation.',
    'input_plane_existing_output': {'path': 'input-plane-review/exact_projection_checks.json', **digest(projection),
                                    'assertions': 12, 'json_equals_stdout': True},
    'source_relative_links_checked': len(links),
    'historical_relative_links_without_public_target': link_unresolved,
    'new_mathematical_reruns_for_integration': 0,
    'new_prime_heights_for_integration': 0,
    'new_pdf_build': False, 'formal_verification': False,
    'strict_arithmetic_bound_proved': False,
    'theorem_scope': 'Under RH, one complete balanced central fixed mu/log block is O(1), its low Mellin part is O(1/log X), and all high frequencies are summably bounded. The input-plane lemma controls only one plane. No strict global deficit or famous conjecture is proved.',
    'preservation': 'Every staged original is archived unchanged; all authored files, historical copies, reviews and check outputs are public verbatim. Only eight full primary reference bodies/page images stay local with public hashes.',
    'publication_status': 'Prepared only. No Git add, commit, push, or PR mutation performed.',
}
save(LOGS / 'INTEGRATION_RECEIPT.json', receipt)
print(json.dumps(receipt, indent=2, sort_keys=True))
