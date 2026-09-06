#!/usr/bin/env python3
"""Verify frozen inputs and replay the author's bounded scalar checker in a copy."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> None:
    review = Path(__file__).resolve().parent
    author = review.parent / "log-prime-heat"
    receipt = json.loads((author / "AUTHOR_RECEIPT.json").read_text())
    inputs = []
    for entry in receipt["owned_files"] + receipt["dependencies"]:
        path = Path(entry["path"])
        data = path.read_bytes()
        assert len(data) == entry["bytes"], path
        assert sha(data) == entry["sha256"], path
        inputs.append({**entry, "status": "MATCH"})
    with tempfile.TemporaryDirectory(prefix="r21-heat-review-") as folder:
        target = Path(folder)
        for name in ("check_heat_multiplier.py", "LOCALIZED_MELLIN_HEAT_ENERGY.md"):
            shutil.copyfile(author / name, target / name)
        process = subprocess.run(
            [sys.executable, str(target / "check_heat_multiplier.py")],
            check=True, capture_output=True, timeout=60,
        )
        generated = (target / "heat_multiplier_checks.json").read_bytes()
        assert generated == (author / "heat_multiplier_checks.json").read_bytes()
        assert process.stdout == (author / "heat_multiplier_checks.log").read_bytes()
        assert not process.stderr, process.stderr
    (review / "replayed_heat_checks.json").write_bytes(generated)
    (review / "replayed_heat_checks.log").write_bytes(process.stdout)
    result = {
        "status": "PASS",
        "scope": "Pinned-input checks and unchanged eight-scalar-assertion replay in a temporary copy; not analytic proof certification.",
        "author_receipt_sha256": sha((author / "AUTHOR_RECEIPT.json").read_bytes()),
        "verified_inputs": inputs,
        "scalar_assertions": json.loads(generated)["checks"]["scalar_assertions"],
        "generated_json_sha256": sha(generated),
        "stdout_sha256": sha(process.stdout),
        "byte_identical_to_author": True,
    }
    rendered = json.dumps(result, indent=2) + "\n"
    (review / "input_and_replay_checks.json").write_text(rendered)
    print(rendered, end="")


if __name__ == "__main__":
    main()
