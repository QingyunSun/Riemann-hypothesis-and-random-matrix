"""Replay bounded round-five certificates in a copy and check saved Ritz witnesses.

Set PRIME186_SOURCE to the pinned official certificate. Original evidence is read
only; subprocess outputs and comparison receipts go beside this script.
"""
from pathlib import Path
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
SOURCE = ROOT / "research/prime-gaps/round5"
EXPECTED = "7f71bdefcfe3bb5ca76a143929b3cb3f4156c21dc483253cda3077420f1e5de4"


def main():
    external = Path(os.environ["PRIME186_SOURCE"])
    assert hashlib.sha256(external.read_bytes()).hexdigest() == EXPECTED
    env = dict(os.environ, OPENBLAS_NUM_THREADS="1")
    result = {"upstream_sha256": EXPECTED, "exact_replays": {}, "saved_matrices": []}
    with tempfile.TemporaryDirectory(prefix="astra-round5-recheck-") as tmp:
        copy = Path(tmp) / "round5"
        shutil.copytree(SOURCE, copy, ignore=shutil.ignore_patterns("__pycache__"))
        commands = [
            ("geometry-audit", "geometry_feasibility.py", "geometry_feasibility.json", {"elapsed_seconds"}),
            ("exceptional-radius", "certify_exceptional_radius.py", "certify_exceptional_radius.json", {"source_text_sha256"}),
            ("geometry-trial", "validate_geometry.py", "geometry_checks.json", set()),
        ]
        for folder, script, output, ignored in commands:
            proc = subprocess.run([sys.executable, script], cwd=copy / folder, env=env, text=True, capture_output=True)
            (HERE / (folder + ".log")).write_text(proc.stdout + proc.stderr)
            assert proc.returncode == 0, (folder, proc.returncode)
            old = json.loads((SOURCE / folder / output).read_text())
            new = json.loads((copy / folder / output).read_text())
            for key in ignored:
                old.pop(key, None)
                new.pop(key, None)
            assert old == new, folder
            result["exact_replays"][folder] = {"match": True, "ignored_metadata": sorted(ignored)}
        geometry = json.loads((copy / "geometry-audit/geometry_feasibility.json").read_text())
        result["geometry_cases"] = len(geometry["cases"])
        result["valid_natural_templates"] = sum(c["largest_cap_template_valid"] for c in geometry["cases"])
        assert result["geometry_cases"] == 15 and result["valid_natural_templates"] == 12

    # This checks stored matrix/vector consistency, not the physical integral model
    # or an interval enclosure of the generalized eigenvalue.
    for path in sorted((SOURCE / "geometry-trial").glob("*_k39_n*.npz")):
        saved = json.loads(path.with_suffix(".json").read_text())
        with np.load(path, allow_pickle=False) as arrays:
            G, B = arrays["gram"], arrays["numerator"]
            assert G.shape == B.shape == (77, 77)
            assert np.isfinite(G).all() and np.isfinite(B).all()
            assert np.array_equal(G, G.T) and np.array_equal(B, B.T)
            errors = []
            norm_errors = []
            direct_errors = []
            for trial in saved["trials"]:
                c = np.asarray(trial["coefficients_float"])
                norm = float(c @ G @ c)
                numerator = float(c @ B @ c)
                error = abs(numerator - trial["rho_J_over_I"])
                assert error < 2e-9 and abs(norm - 1) < 2e-9
                assert abs(numerator / norm - trial["rho_J_over_I"]) < 3e-9
                direct_error = abs(trial["rho_J_over_I"] - trial["direct_candidate_evaluation"]["rho_J_over_I"])
                assert direct_error < 3e-9
                errors.append(error)
                norm_errors.append(abs(norm - 1))
                direct_errors.append(direct_error)
            result["saved_matrices"].append({"file": path.name, "candidates": len(errors),
                "max_numerator_replay_error": max(errors), "max_unit_norm_error": max(norm_errors),
                "max_recorded_matrix_direct_difference": max(direct_errors)})
    assert len(result["saved_matrices"]) == 12
    result["status"] = "PASS: exact certificate replays and saved finite-matrix witness checks"
    result["scope"] = "No fresh full integral sweep; no certified finite-family upper bound; no smaller prime-gap claim."
    (HERE / "recheck.json").write_text(json.dumps(result, indent=2) + "\n")
    print(result["status"])
    print("15 exact cases; 12 accepted cap templates; 20 mask nestings; 12 matrices / 36 candidate vectors")


if __name__ == "__main__":
    main()
