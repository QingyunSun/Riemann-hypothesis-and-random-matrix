"""Replay the bounded Round6 diagnostic in a copy; preserve original evidence."""
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
ARCHIVE = ROOT / "research/prime-gaps/round6"
SOURCE_SHA = "7f71bdefcfe3bb5ca76a143929b3cb3f4156c21dc483253cda3077420f1e5de4"


def main():
    source = Path(os.environ["PRIME186_SOURCE"])
    assert hashlib.sha256(source.read_bytes()).hexdigest() == SOURCE_SHA
    env = dict(os.environ, OPENBLAS_NUM_THREADS="1",
               PRIME186_TRIAL_ROOT=str(ROOT / "research/prime-gaps/round4/k39-trial"))
    receipt = {"upstream_sha256": SOURCE_SHA, "exact_checks": {}, "scope":
               "One fine-grid replay plus exact algebra and saved-output checks; no outward certificate or full residual norm."}
    with tempfile.TemporaryDirectory(prefix="astra-round6-recheck-") as tmp:
        copy = Path(tmp) / "round6"
        shutil.copytree(ARCHIVE, copy, ignore=shutil.ignore_patterns("__pycache__"))

        def run(folder, name, *args):
            proc = subprocess.run([sys.executable, name, *args], cwd=copy / folder,
                                  env=env, capture_output=True, text=True)
            (HERE / (name.replace(".py", "") + ".log")).write_text(proc.stdout + proc.stderr)
            assert proc.returncode == 0, (name, proc.returncode)

        for folder, script, output in [
            ("operator-diagnostic", "finite_marked_operator_check.py", "finite_marked_operator_check.json"),
            ("residual-audit", "exact_residual_checks.py", "exact_residual_checks.json"),
            ("residual-trial", "audit_outputs.py", "projection_audit.json"),
        ]:
            run(folder, script)
            expected = json.loads((ARCHIVE / folder / output).read_text())
            actual = json.loads((copy / folder / output).read_text())
            assert expected == actual, output
            receipt["exact_checks"][script] = "identical JSON output"

        stem = "radial_residual_n98304_cut1e-09_tilt20"
        expected = json.loads((ARCHIVE / "residual-trial" / (stem + ".json")).read_text())
        run("residual-trial", "radial_residual.py", "--intervals", "98304")
        actual = json.loads((copy / "residual-trial" / (stem + ".json")).read_text())
        fields = ["original_77_quotient", "new_78_matrix_quotient", "radial_norm_squared",
                  "outside_77_norm_squared", "orthogonal_complement_coupling"]
        differences = {key: actual[key] - expected[key] for key in fields}
        assert max(abs(v) for v in differences.values()) < 5e-10
        direct_difference = (actual["new_78_direct_evaluation"]["rho_J_over_I"]
                             - expected["new_78_direct_evaluation"]["rho_J_over_I"])
        assert abs(direct_difference) < 5e-10
        with np.load(ARCHIVE / "residual-trial" / (stem + "_compact.npz"), allow_pickle=False) as old, \
             np.load(copy / "residual-trial" / (stem + ".npz"), allow_pickle=False) as new:
            profile_error2 = float(np.sum(np.maximum(old["q"], 0) * (new["h"] - old["h"]) ** 2))
            reference2 = float(np.sum(np.maximum(old["q"], 0) * old["h"] ** 2))
            assert profile_error2 / reference2 < 1e-12
            assert np.array_equal(old["active"], new["active"])
            assert np.array_equal(old["radial"], new["radial"])
        receipt["fine_replay"] = {"N": 98304, "field_differences": differences,
                                  "direct_quotient_difference": direct_difference,
                                  "relative_radial_profile_mass_error_squared": profile_error2 / reference2,
                                  "active_mask_identical": True, "radial_cells_identical": True,
                                  "replayed_direct_quotient": actual["new_78_direct_evaluation"]["rho_J_over_I"]}
    receipt["status"] = "PASS: exact checks and independent fine radial-residual replay"
    (HERE / "recheck.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
