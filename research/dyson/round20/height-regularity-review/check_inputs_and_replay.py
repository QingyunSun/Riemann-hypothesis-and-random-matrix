#!/usr/bin/env python3
"""Read-only source verification and unchanged checker replay in a temp copy."""
from pathlib import Path
import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--research-base", type=Path, default=Path(
        "/Users/qingyunsun/Library/CloudStorage/Dropbox/Research/ACUE-Astra-Handoff-2026-09-04"
    ))
    args = parser.parse_args()
    source = args.research_base / "research-round20/height-regularity"
    here = Path(__file__).resolve().parent
    checks = []
    author_manifest = json.loads((source / "author_manifest.json").read_text())
    for entry in author_manifest["files"]:
        path = source / entry["path"]
        actual = sha(path)
        checks.append({"path": str(path), "expected": entry["sha256"], "actual": actual,
                       "matches": actual == entry["sha256"] and path.stat().st_size == entry["bytes"]})
    source_manifest = json.loads((source / "source_manifest.json").read_text())
    for item in source_manifest["sources"]:
        for entry in item["files"]:
            path = Path(entry["path"])
            actual = sha(path)
            checks.append({"path": str(path), "expected": entry["sha256"], "actual": actual,
                           "matches": actual == entry["sha256"] and path.stat().st_size == entry["bytes"]})
    expected_height = "6048b8792084d1523212ddd5f0c05dcc5b54fb158c3dab37762675e91a1072fe"
    expected_length = "cd8c2f7dc48530ed02f915dd202c8aedaaaadb1096cafc019beeb595b9beebbe"
    height_report = source / "MULTIPLICATIVE_HEIGHT_EQUICONTINUITY.md"
    length_report = args.research_base / "research-round20/length-averaged-variance/EXPONENTIAL_LENGTH_AVERAGE.md"
    assert sha(height_report) == expected_height
    assert sha(length_report) == expected_length
    assert all(entry["matches"] for entry in checks)

    with tempfile.TemporaryDirectory(prefix="height-replay-", dir=here) as temp:
        copied = Path(temp)
        for name in ["check_height_regularity.py", "MULTIPLICATIVE_HEIGHT_EQUICONTINUITY.md"]:
            shutil.copyfile(source / name, copied / name)
            assert sha(source / name) == sha(copied / name)
        replay = subprocess.run([sys.executable, str(copied / "check_height_regularity.py")],
                                capture_output=True, check=True)
        generated = (copied / "height_regularity_checks.json").read_bytes()
        json_identical = generated == (source / "height_regularity_checks.json").read_bytes()
        log_identical = replay.stdout == (source / "height_regularity_checks.log").read_bytes()
        assert json_identical and log_identical and not replay.stderr
        (here / "replayed_height_checks.json").write_bytes(generated)
        (here / "replayed_height_checks.log").write_bytes(replay.stdout)

    result = {
        "status": "PASS",
        "scope": "Author/source hash verification plus unchanged exact-checker replay in a temporary copy. Does not establish a positive zeta deficit or independently prove the separate length-average identity.",
        "reviewed_height_sha256": expected_height,
        "combined_length_dependency_sha256": expected_length,
        "manifest_entries_checked": checks,
        "replay_json_byte_identical": json_identical,
        "replay_log_byte_identical": log_identical,
        "replay_json_sha256": sha(here / "replayed_height_checks.json"),
        "replay_script_sha256": sha(source / "check_height_regularity.py"),
        "review_reproducer_sha256": sha(Path(__file__)),
    }
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    (here / "input_and_replay_checks.json").write_text(payload)
    print(payload, end="")


if __name__ == "__main__":
    main()
