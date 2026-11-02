"""Replay the two bounded R13 scripts without changing archived originals."""
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
    parser.add_argument("--prime-gap-source-dir", type=Path, required=True)
    parser.add_argument("--minor-arc-source-dir", type=Path, required=True)
    args = parser.parse_args()
    here = Path(__file__).resolve().parent
    root = here.parents[2]
    source = root / "research/dyson/round13"
    manifest = json.loads((source / "INTAKE_MANIFEST.json").read_text())
    public = [row for row in manifest["files"] if row["public"]]
    for row in public:
        path = source / row["path"]
        assert path.stat().st_size == row["bytes"]
        assert hashlib.sha256(path.read_bytes()).hexdigest() == row["sha256"]
    results = []
    with tempfile.TemporaryDirectory(prefix="astra-round13-") as temporary:
        base = Path(temporary)
        work = base / "research-round13"
        shutil.copytree(source, work)
        shutil.copytree(root / "research/dyson/round11", base / "research-round11")
        refs = base / "sources"
        refs.mkdir()
        shutil.copy2(args.prime_gap_source_dir / "openai-short-gaps.pdf", refs)
        for name in ("montgomery-vaughan-II-author-draft.pdf", "schoenfeld-1976-II.pdf"):
            shutil.copy2(args.minor_arc_source_dir / name, work / "minor-arc-source/sources" / name)
        for script, output in [
            ("phase-resonance/check_phase_resonance.py", "phase-resonance/phase_resonance_certificate.json"),
            ("signed-kernel/check_signed_kernel_norm.py", "signed-kernel/check_signed_kernel_norm.json"),
        ]:
            run = subprocess.run([sys.executable, str(work / script)], cwd=work,
                                 capture_output=True, text=True, timeout=60)
            (here / (Path(script).stem + ".replay.log")).write_text(run.stdout + run.stderr)
            if run.returncode:
                raise RuntimeError(f"{script} failed: {run.returncode}")
            got = json.loads((work / output).read_text())
            expected = json.loads((source / output).read_text())
            excluded = []
            for index, receipt in enumerate(got.get("source_receipts", [])):
                receipt.pop("path")
                expected["source_receipts"][index].pop("path")
                excluded.append(f"source_receipts[{index}].path")
            assert got == expected, output
            results.append({"script": script, "structured_match": True,
                            "excluded_temporary_paths": excluded})
    receipt = {"status": "PASS", "public_verbatim_files_verified": len(public),
               "checks": results,
               "scope": "Exact CRT and unit-mask completion, centered variance, constants, residue counts and source hashes. No numerical proof of the analytic asymptotics.",
               "new_actual_zeta_lower_bound": False, "large_scan": False}
    (here / "recheck.json").write_text(json.dumps(receipt, indent=2)+"\n")
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
