"""Verify the source receipt and replay only the small mass-cutoff check."""
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
    snapshot = root / "fable/snapshots/2073028"
    manifest = json.loads((snapshot / "SOURCE_MANIFEST.json").read_text())
    for row in manifest["files"]:
        path = snapshot / "files" / row["path"]
        assert path.stat().st_size == row["bytes"]
        assert hashlib.sha256(path.read_bytes()).hexdigest() == row["sha256"]
    source = snapshot / "files/astra_tasks/task001/f3_fock_spectrum.py"
    with tempfile.TemporaryDirectory(prefix="astra-fable-2073028-") as temporary:
        output = Path(temporary) / "check.json"
        environment = dict(os.environ, OPENBLAS_NUM_THREADS="1", PYTHONDONTWRITEBYTECODE="1")
        run = subprocess.run([sys.executable, str(here / "check_mass_cutoff.py"),
                              "--source", str(source), "--out", str(output)],
                             capture_output=True, text=True, timeout=60, env=environment)
        (here / "check_mass_cutoff.replay.log").write_text(run.stdout+run.stderr)
        if run.returncode:
            raise RuntimeError(f"small mass check failed: {run.returncode}")
        got = json.loads(output.read_text())
        expected = json.loads((here / "check_mass_cutoff.json").read_text())
        assert got == expected
        cbeta_script = Path(temporary) / "check_cbeta_repair.py"
        shutil.copy2(here / cbeta_script.name, cbeta_script)
        cbeta_run = subprocess.run([sys.executable, str(cbeta_script)], capture_output=True,
                                  text=True, timeout=60, env=environment)
        (here / "check_cbeta_repair.replay.log").write_text(cbeta_run.stdout+cbeta_run.stderr)
        if cbeta_run.returncode:
            raise RuntimeError(f"Cbeta algebra failed: {cbeta_run.returncode}")
        assert json.loads(cbeta_script.with_suffix(".json").read_text()) == json.loads(
            (here / "check_cbeta_repair.json").read_text())
    receipt = {"status": "PASS", "source_files_verified": len(manifest["files"]),
               "small_check_structured_match": True, "excluded_fields": [],
               "cbeta_exact_check_structured_match": True,
               "scope": "M=6,8,10 floating matrix checks, scalar integrals and exact finite Cbeta correction algebra only",
               "large_refuter_or_proposer_main_executed": False}
    (here / "recheck.json").write_text(json.dumps(receipt,indent=2)+"\n")
    print(json.dumps(receipt,indent=2))


if __name__ == "__main__":
    main()
