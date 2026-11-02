#!/usr/bin/env python3
"""Verify the frozen parity manuscript and its declared input hashes."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent
    author = root.parent / "parity-adjusted-target"
    receipt_path = author / "AUTHOR_RECEIPT.json"
    receipt_bytes = receipt_path.read_bytes()
    receipt = json.loads(receipt_bytes)
    verified = []
    for entry in [receipt["author"], receipt["syntax"], *receipt["inputs"]]:
        data = Path(entry["path"]).read_bytes()
        assert len(data) == entry["bytes"]
        assert hashlib.sha256(data).hexdigest() == entry["sha256"]
        verified.append({**entry, "status": "MATCH"})
    result = {
        "status": "PASS",
        "scope": "Four frozen-file hashes only; ordinary proof review is separate and the pending singleton dependency is not relabeled as checked.",
        "author_receipt_sha256": hashlib.sha256(receipt_bytes).hexdigest(),
        "verified": verified,
    }
    output = json.dumps(result, indent=2) + "\n"
    (root / "input_hash_checks.json").write_text(output)
    print(output, end="")


if __name__ == "__main__":
    main()
