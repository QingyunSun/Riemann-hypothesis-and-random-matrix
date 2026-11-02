"""Bounded exact replay of Round 11, retaining source artifacts unchanged."""
from pathlib import Path
import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime-gap-source", type=Path, required=True,
                        help="Locally retained openai-short-gaps.pdf from the pinned 186 source")
    args = parser.parse_args()
    here = Path(__file__).resolve().parent
    root = here.parents[2]
    source = root / "research/dyson/round11"
    manifest = json.loads((source / "INTAKE_MANIFEST.json").read_text())
    public = [e for e in manifest["files"] if e["public"]]
    for row in public:
        p = source / row["path"]
        assert p.stat().st_size == row["bytes"]
        assert hashlib.sha256(p.read_bytes()).hexdigest() == row["sha256"]
    gap_hash = hashlib.sha256(args.prime_gap_source.read_bytes()).hexdigest()
    assert gap_hash == "456f05e0a3ef589ebb0e9abcfd31f140f3c945adbf6950e00ef371a3c88b0930"
    results = []
    with tempfile.TemporaryDirectory(prefix="astra-round11-") as tmp:
        work = Path(tmp) / "research-round11"
        shutil.copytree(source, work)
        refs = Path(tmp) / "sources"
        refs.mkdir()
        shutil.copy2(args.prime_gap_source, refs / "openai-short-gaps.pdf")
        scripts = [
            ("conductor-arithmetic/check_conductor_construction.py", "conductor-arithmetic/conductor_construction_certificate.json"),
            ("prime-frequency/check_small_arc_bound.py", "prime-frequency/check_small_arc_bound.json"),
        ]
        for script, output in scripts:
            run = subprocess.run([sys.executable, str(work / script)], cwd=work,
                                 env=dict(os.environ, OPENBLAS_NUM_THREADS="1"),
                                 capture_output=True, text=True, timeout=60)
            (here / (Path(script).stem + ".replay.log")).write_text(run.stdout + run.stderr)
            if run.returncode:
                raise RuntimeError(f"{script} exited {run.returncode}")
            got = json.loads((work / output).read_text())
            expected = json.loads((source / output).read_text())
            omitted = []
            if "primary_source" in got:
                got["primary_source"].pop("path")
                expected["primary_source"].pop("path")
                omitted = ["primary_source.path (temporary-copy provenance only)"]
            assert got == expected, output
            results.append({"script": script, "output": output, "structured_match": True,
                            "excluded_fields": omitted})
    receipt = {
        "status": "PASS",
        "public_verbatim_files_verified": len(public),
        "primary_186_source_sha256": gap_hash,
        "checks": results,
        "scope": "Exact exponent, counting constant and finite frequency bookkeeping checks. Ordinary written proofs and independent reviews support the RH analytic estimate and asymptotic PNT construction.",
        "large_computations": "None; no prime realization, zeta sample, coefficient scan or optimizer",
    }
    (here / "recheck.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
