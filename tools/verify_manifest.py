"""Create/check a content manifest of explicitly selected research artifacts."""
from pathlib import Path
import argparse
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "RESEARCH_MANIFEST.json"
FOLDERS = ("research", "historical", "docs", "tasks", "output", "fable")


def collect() -> list[dict]:
    files = []
    for folder in FOLDERS:
        for p in sorted((ROOT / folder).rglob("*")):
            if not p.is_file() or "__pycache__" in p.parts:
                continue
            files.append({"path": str(p.relative_to(ROOT)), "bytes": p.stat().st_size,
                          "sha256": hashlib.sha256(p.read_bytes()).hexdigest()})
    return files


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="Record the current files, after review.")
    args = parser.parse_args()
    current = collect()
    if args.write:
        MANIFEST.write_text(json.dumps({"algorithm": "sha256", "files": current}, indent=2) + "\n")
        print(f"Recorded {len(current)} files")
    else:
        expected = json.loads(MANIFEST.read_text())["files"]
        if expected != current:
            old = {r["path"]: r for r in expected}
            new = {r["path"]: r for r in current}
            changed = [p for p in sorted(old.keys() | new.keys()) if old.get(p) != new.get(p)]
            raise SystemExit("Manifest mismatch: " + ", ".join(changed))
        print(f"Verified {len(current)} files")


if __name__ == "__main__":
    main()
