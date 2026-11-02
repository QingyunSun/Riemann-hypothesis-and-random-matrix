"""Replay bounded R14 algebra in a copy and verify its proof/source receipts."""
from pathlib import Path
import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime-gap-source-dir", type=Path, required=True)
    parser.add_argument("--cue-source-dir", type=Path, required=True)
    args = parser.parse_args()
    here = Path(__file__).resolve().parent
    root = here.parents[2]
    source = root / "research/dyson/round14"
    manifest = json.loads((source / "INTAKE_MANIFEST.json").read_text())
    public = [row for row in manifest["files"] if row["public"]]
    for row in public:
        path = source / row["path"]
        assert path.stat().st_size == row["bytes"] and digest(path) == row["sha256"]
    refs = json.loads((source / "cue-selected-background/source_receipt.json").read_text())
    primary = refs["primary_source"]
    for kind in ("pdf", "text"):
        path = args.cue_source_dir / Path(primary[kind+"_path"]).name
        assert digest(path) == primary[kind+"_sha256"]
    publication = []
    for row in refs["inherited_proofs"]:
        path = root / "research/reports" / Path(row["path"]).name
        actual = digest(path)
        if path.name == "galilean-proof-audit.md":
            # Earlier publication corrected only title and reviewer attribution.
            assert actual == "f3896ff6b7a07d1296762ff09ad8bf9315766459f16394d6636e64d9036c8f13"
            assert row["sha256"] == "c85684fe873c19c193a81d3d16cde2507f10cf6753324ce31eda99b14672a2da"
            publication.append({"file": str(path.relative_to(root)),
                                "original_sha256": row["sha256"], "published_sha256": actual,
                                "difference": "title and same-agent second-pass attribution only; root compared complete mathematical bodies"})
        else:
            assert actual == row["sha256"]
    results = []
    with tempfile.TemporaryDirectory(prefix="astra-round14-") as temporary:
        base = Path(temporary)
        work = base / "research-round14"
        shutil.copytree(source, work)
        for round_number in (9, 13):
            shutil.copytree(root / f"research/dyson/round{round_number}",
                            base / f"research-round{round_number}")
        (base / "sources").mkdir()
        shutil.copy2(args.prime_gap_source_dir / "openai-short-gaps.pdf", base / "sources")
        for script, output in [
            ("smooth-long-factor/check_smooth_long_factor.py", "smooth-long-factor/smooth_long_factor_certificate.json"),
            ("cue-selected-background/check_selected_background.py", "cue-selected-background/check_selected_background.json"),
        ]:
            run = subprocess.run([sys.executable, str(work / script)], cwd=work,
                                 capture_output=True, text=True, timeout=60)
            (here / (Path(script).stem+".replay.log")).write_text(run.stdout+run.stderr)
            if run.returncode:
                raise RuntimeError(f"{script} failed: {run.returncode}")
            got = json.loads((work / output).read_text())
            expected = json.loads((source / output).read_text())
            excluded = []
            if "source" in got:
                got["source"].pop("path")
                expected["source"].pop("path")
                excluded.append("source.path")
            assert got == expected, output
            results.append({"script": script, "structured_match": True,
                            "excluded_temporary_paths": excluded})
    receipt = {"status": "PASS", "public_verbatim_files_verified": len(public),
               "checks": results, "inherited_publication_correspondence": publication,
               "scope": "Exact finite determinant, convolution and centering algebra; two fixed floating Poisson diagnostics; proof/source hashes. No Monte Carlo or large scan.",
               "new_actual_zeta_lower_bound": False}
    (here / "recheck.json").write_text(json.dumps(receipt,indent=2)+"\n")
    print(json.dumps(receipt,indent=2))


if __name__ == "__main__":
    main()
