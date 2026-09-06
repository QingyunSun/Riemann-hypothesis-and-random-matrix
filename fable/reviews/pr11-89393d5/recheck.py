"""Replay only two bounded Fable refuters and the independent sign check in a copy."""
from pathlib import Path
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile


def main() -> None:
    here = Path(__file__).resolve().parent
    root = here.parents[2]
    snapshot = root / "fable/snapshots/89393d5"
    manifest = json.loads((snapshot / "SOURCE_MANIFEST.json").read_text())
    for row in manifest["files"]:
        p = snapshot / "files" / row["path"]
        assert p.stat().st_size == row["bytes"]
        assert hashlib.sha256(p.read_bytes()).hexdigest() == row["sha256"]
    env = dict(os.environ, OPENBLAS_NUM_THREADS="1", OMP_NUM_THREADS="1", MKL_NUM_THREADS="1")
    receipt = {"source_commit": manifest["commit"], "verbatim_files_verified": len(manifest["files"]),
               "execution_scope": "Two named refuters only, bounded to L<=10^6; no other Fable main program executed"}
    with tempfile.TemporaryDirectory(prefix="astra-fable-89393d5-") as name:
        work = Path(name) / "files"
        shutil.copytree(snapshot / "files", work)
        task = work / "astra_tasks/task001"
        for script in ("refute_F1_rigour.py", "refute_F1_repro.py"):
            run = subprocess.run([sys.executable, str(task / script)], cwd=work, env=env,
                                 text=True, capture_output=True, timeout=180)
            (here / (Path(script).stem + ".replay.log")).write_text(run.stdout + run.stderr)
            if run.returncode:
                raise RuntimeError(f"{script} exited {run.returncode}")
        rigour = json.loads((task / "refute_F1_rigour_results.json").read_text())
        saved_rigour = json.loads((snapshot / "files/astra_tasks/task001/refute_F1_rigour_results.json").read_text())
        assert rigour == saved_rigour
        probes = rigour["direct_diff_probe_-zz3(1+eps)*eps^4_should_tend_to_6"]
        assert all(float(v) == -6.0 for v in probes.values())
        repro = json.loads((task / "refute_F1_repro_results.json").read_text())
        saved = json.loads((snapshot / "files/astra_tasks/task001/refute_F1_repro_results.json").read_text())
        assert repro["n_checks"] == saved["n_checks"] == 10
        assert repro["n_failed"] == saved["n_failed"] == 3
        flags = [(c["name"], c["passed"]) for c in repro["checks"]]
        assert flags == [(c["name"], c["passed"]) for c in saved["checks"]]
        numeric_check_name = "independent re-run of f1_insertion_decomposition.decompose at L=1000 matches f1_insertion_results.json"
        changed_details = [c["name"] for c, old in zip(repro["checks"], saved["checks"]) if c != old]
        assert all(name == numeric_check_name for name in changed_details)
        numeric_row = next(c for c in repro["checks"] if c["name"] == numeric_check_name)
        values = json.loads(numeric_row["detail"])
        max_difference = max(abs(v["recomputed"] - v["reported_json"]) for v in values.values())
        assert max_difference < 1e-12
        for key in ("seconds",):
            repro.pop(key, None)
            saved.pop(key, None)
        receipt.update({"rigour_output_exact_match": True,
                        "rigour_probe_sign_bug_reproduced": True,
                        "repro_check_count": 10, "repro_expected_narrative_failures": 3,
                        "repro_all_check_flags_match": True,
                        "repro_output_exact_except_timing": repro == saved,
                        "changed_detail_fields": changed_details,
                        "insertion_max_absolute_difference": max_difference,
                        "insertion_acceptance_tolerance": 1e-12})
        (here / "refute_F1_repro.replay.json").write_text(json.dumps(repro, indent=2) + "\n")
        check = Path(name) / "check_pole_coefficient.py"
        shutil.copy2(here / check.name, check)
        run = subprocess.run([sys.executable, str(check)], env=env, text=True, capture_output=True, timeout=30)
        (here / "check_pole_coefficient.replay.log").write_text(run.stdout + run.stderr)
        if run.returncode:
            raise RuntimeError("independent pole check failed")
        shutil.copy2(check.with_suffix(".json"), here / "check_pole_coefficient.json")
    receipt["status"] = "PASS for faithful replay and independent correction, not acceptance of the three failed narrative assertions"
    (here / "recheck.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
