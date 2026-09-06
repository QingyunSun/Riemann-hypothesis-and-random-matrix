"""Check the Round 6 intake, compact witnesses and exact certificate in a copy."""
from pathlib import Path
import argparse
import ast
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
ARCHIVE = ROOT / "research/prime-gaps/round6"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--full-array-directory", type=Path,
                        help="Optional directory holding the original local NPZs.")
    args = parser.parse_args()
    intake = json.loads((ARCHIVE / "INTAKE_MANIFEST.json").read_text())
    for record in intake["files"]:
        path = ROOT / record["published_path"]
        assert path.stat().st_size == record["bytes"]
        assert digest(path) == record["sha256"], str(path)

    compactions = json.loads((ARCHIVE / "residual-trial/compaction_manifest.json").read_text())
    retained = 0
    for record in compactions:
        path = ARCHIVE / "residual-trial" / record["compact_file"]
        assert digest(path) == record["compact_sha256"]
        with np.load(path, allow_pickle=False) as compact:
            assert set(compact.files) == set(record["retained_array_sha256_C_bytes"])
            for key, expected in record["retained_array_sha256_C_bytes"].items():
                assert hashlib.sha256(compact[key].tobytes(order="C")).hexdigest() == expected
                retained += 1
            if args.full_array_directory is not None:
                full_path = args.full_array_directory / record["full_file"]
                assert digest(full_path) == record["full_sha256"]
                assert full_path.stat().st_size == record["full_bytes"]
                with np.load(full_path, allow_pickle=False) as full:
                    assert set(full.files) - set(compact.files) == {"D"}
                    assert set(compact.files) <= set(full.files)
                    assert list(full["D"].shape) == record["omitted_D_shape"]
                    assert str(full["D"].dtype) == record["omitted_D_dtype"]
                    assert hashlib.sha256(full["D"].tobytes(order="C")).hexdigest() == record["omitted_D_sha256_C_bytes"]
                    for key in compact.files:
                        assert full[key].shape == compact[key].shape
                        assert full[key].dtype == compact[key].dtype
                        assert full[key].tobytes() == compact[key].tobytes()

    scripts = list(ARCHIVE.rglob("*.py")) + list(HERE.glob("*.py"))
    for path in scripts:
        ast.parse(path.read_text(), filename=str(path))
    report_paths = [ROOT / "research/reports/prime186_round6.md", ARCHIVE / "README.md"]
    links = 0
    for path in report_paths:
        for target in re.findall(r"\]\(([^)]+)\)", path.read_text()):
            if "://" not in target and not target.startswith("#"):
                assert (path.parent / target.split("#")[0]).exists(), (str(path), target)
                links += 1

    with tempfile.TemporaryDirectory(prefix="astra-round6-certificate-") as tmp:
        copy = Path(tmp) / "round6"
        shutil.copytree(ARCHIVE, copy, ignore=shutil.ignore_patterns("__pycache__"))
        folder = copy / "operator-diagnostic"
        proc = subprocess.run([sys.executable, "certify_outside_span.py"], cwd=folder,
                              env=os.environ.copy(), capture_output=True, text=True)
        (HERE / "outside_span_replay.log").write_text(proc.stdout + proc.stderr)
        assert proc.returncode == 0, proc.stderr
        expected = json.loads((ARCHIVE / "operator-diagnostic/outside_span_certificate.json").read_text())
        actual = json.loads((folder / "outside_span_certificate.json").read_text())
        assert actual == expected

    receipt = {
        "status": "PASS: intake, compact data, syntax, links and exact outside-span replay",
        "verbatim_intake_files": len(intake["files"]),
        "compact_witness_files": len(compactions),
        "retained_arrays_checked": retained,
        "full_local_arrays_checked": len(compactions) if args.full_array_directory else 0,
        "full_local_bytes_checked": sum(r["full_bytes"] for r in compactions) if args.full_array_directory else 0,
        "python_files_parsed": len(scripts),
        "relative_report_links_checked": links,
        "outside_span_json": "identical exact output from isolated copy",
        "scope": "Artifact integrity and exact independence; no new numerical integration or Rayleigh enclosure.",
    }
    (HERE / "archive_check.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
