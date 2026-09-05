"""Replay the two bounded exact Round 12 checks in an isolated directory."""
from pathlib import Path
import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime-gap-source-dir", type=Path, required=True,
                        help="Directory with pinned openai-short-gaps.pdf and .txt")
    args = parser.parse_args()
    here = Path(__file__).resolve().parent
    root = here.parents[2]
    source = root / "research/dyson/round12"
    manifest = json.loads((source / "INTAKE_MANIFEST.json").read_text())
    public = [row for row in manifest["files"] if row["public"]]
    for row in public:
        p = source / row["path"]
        assert p.stat().st_size == row["bytes"]
        assert hashlib.sha256(p.read_bytes()).hexdigest() == row["sha256"]
    results = []
    with tempfile.TemporaryDirectory(prefix="astra-round12-") as tmp:
        base = Path(tmp)
        work = base / "research-round12"
        shutil.copytree(source, work)
        shutil.copytree(root / "research/dyson/round11", base / "research-round11")
        refs = base / "sources"
        refs.mkdir()
        for name in ("openai-short-gaps.pdf", "openai-short-gaps.txt"):
            shutil.copy2(args.prime_gap_source_dir / name, refs / name)
        for script, output in [
            ("sampling-geometry/check_sampling_geometry.py", "sampling-geometry/check_sampling_geometry.json"),
            ("dispersion-transfer/check_dispersion_hypotheses.py", "dispersion-transfer/dispersion_hypotheses_certificate.json"),
        ]:
            run = subprocess.run([sys.executable, str(work / script)], cwd=work,
                                 capture_output=True, text=True, timeout=60)
            (here / (Path(script).stem + ".replay.log")).write_text(run.stdout + run.stderr)
            if run.returncode:
                raise RuntimeError(f"{script} failed: {run.returncode}")
            got = json.loads((work / output).read_text())
            expected = json.loads((source / output).read_text())
            excluded = []
            for field, keys in {
                "primary_source": ["pdf_path", "text_path"],
                "frozen_dependencies": ["conductor_report_path", "previous_prime_bound_path"],
            }.items():
                if field in got:
                    for key in keys:
                        got[field].pop(key)
                        expected[field].pop(key)
                        excluded.append(field + "." + key)
            assert got == expected, output
            results.append({"script": script, "output": output, "structured_match": True,
                            "excluded_temporary_provenance_paths": excluded})
    receipt = {
        "status": "PASS",
        "public_verbatim_files_verified": len(public),
        "checks": results,
        "scope": "Exact constants, 60 cyclotomic signed-kernel identities, source parameter inequalities and six modular-selection cases only. Analytic and asymptotic claims use written proofs and independent reviews.",
        "stronger_actual_prime_bound_proved": False,
        "new_model_sessions_or_large_scans": False,
    }
    (here / "recheck.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
