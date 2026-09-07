"""Finish interrupted R29 receipts; preserve author bytes and compare full outputs.

This performs finite exact checks and provenance validation only. It does not
prove analytic inequalities, rerun prime experiments, publish, or update Git.
"""
from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
STAGE = HERE.parent


def pin(path: Path) -> dict:
    data = path.read_bytes()
    return {"path": str(path), "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def verify(entries: list[dict], base: Path) -> list[dict]:
    checked = []
    for entry in entries:
        actual = pin(base / entry["path"])
        assert actual["bytes"] == entry["bytes"], actual["path"]
        assert actual["sha256"] == entry["sha256"], actual["path"]
        checked.append({**actual, "matches_recorded_pin": True})
    return checked


def load(path: Path) -> dict:
    return json.loads(path.read_text())


def save(path: Path, result: dict) -> None:
    path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


support = HERE / "mellin-energy-support"
energy = HERE / "mellin-energy-review"
signed = HERE / "signed-mellin-test"
review = HERE / "signed-mellin-review"

# Restore the exact previously recorded prose version, not an invented history.
# This recovery is explicitly distinguished from a contemporaneous file copy.
new_bytes = (support / "WEIGHTED_MELLIN_ENERGY.md").read_bytes()
new_phrase = b"In the continuous Poisson representation,"
assert new_bytes.count(new_phrase) == 1
old_bytes = new_bytes.replace(new_phrase, b"Equivalently,", 1)
old_hash = hashlib.sha256(old_bytes).hexdigest()
assert len(old_bytes) == 13211
assert old_hash == "c8f8c6bfcfc9d605e3d02e9031d56d88cc8ea3402096bcb06b394d0abe81ecff"
history = support / "historical-before-alias-wording"
history.mkdir(exist_ok=True)
old_path = history / "WEIGHTED_MELLIN_ENERGY.md"
if old_path.exists():
    assert old_path.read_bytes() == old_bytes
else:
    old_path.write_bytes(old_bytes)
history_record = {
    "status": "exact old bytes recovered and verified against the prior recorded hash",
    "method": "Reverse only the one recorded wording substitution in the final author file; the recovered 13211-byte file matches its previously recorded SHA256. This is recovery, not a claim of an original contemporaneous copy.",
    "old": pin(old_path), "current": pin(support / "WEIGHTED_MELLIN_ENERGY.md"),
    "mathematical_change": "None. Exact adjacent-increment resonance and continuous stationary center are related but not identical.",
}
save(history / "RECOVERY_RECEIPT.json", history_record)

energy_author = verify(load(support / "AUTHOR_RECEIPT.json")["artifacts"], support)
energy_sources = verify(load(support / "source_receipt.json")["sources"], STAGE)
assert (energy / "check_mellin_energy.py").read_bytes() == (support / "check_mellin_energy.py").read_bytes()
with tempfile.TemporaryDirectory(prefix="r29-energy-replay-") as temp:
    temp = Path(temp)
    shutil.copyfile(energy / "check_mellin_energy.py", temp / "check_mellin_energy.py")
    run = subprocess.run([sys.executable, str(temp / "check_mellin_energy.py")],
                         capture_output=True, check=True, cwd=temp)
    assert run.stderr == b""
    output = (temp / "mellin_energy_checks.json").read_bytes()
    assert output == run.stdout
    for path in (support / "mellin_energy_checks.json", support / "mellin_energy_checks.log",
                 energy / "mellin_energy_checks.json", energy / "mellin_energy_checks.log"):
        assert path.read_bytes() == output, path
parsed = json.loads(output)
assert parsed["count"] == 13 and parsed["status"] == "PASS"
assert all(parsed["checks"].values())

for folder in (energy, review):
    subprocess.run(["node", str(folder / "check_math_syntax.cjs")],
                   check=True, capture_output=True)
    assert load(folder / "math_syntax_checks.json")["status"] == "PASS"

energy_receipt = {
    "status": "ordinary proof accepted; interrupted receipt complete",
    "reviewer": "Astra root",
    "completion_agent": "r29_close; preserves the existing complete ordinary review",
    "scope": "RH fixed-order weighted Mellin energy O_j(Y log^2 X); unconditional sharp odd-log nonstationary bound. No strict deficit, one-log prime-window bound, growing derivative order, or Möbius-specific cancellation.",
    "author_artifacts_verified": energy_author,
    "source_pins_verified": energy_sources,
    "historical_wording_recovery": history_record,
    "complete_replay": {"checks": 13, "all_passed": True,
        "temporary_copy_only": True, "stderr_empty": True,
        "whole_json_equals_stdout_and_all_four_frozen_outputs": True,
        "output": pin(energy / "mellin_energy_checks.json")},
    "syntax": load(energy / "math_syntax_checks.json"),
    "artifacts": [pin(energy / name) for name in (
        "INDEPENDENT_MELLIN_ENERGY_REVIEW.md", "check_mellin_energy.py",
        "mellin_energy_checks.json", "mellin_energy_checks.log",
        "check_math_syntax.cjs", "math_syntax_checks.json")],
    "verification_boundary": "Finite exact algebra and byte comparisons are not formal verification of the analytic proof. No new prime, matrix, frequency scan, or source theorem reproof.",
}
save(energy / "REVIEW_RECEIPT.json", energy_receipt)

# The separately read, unchanged independent runner checks final author bytes,
# all source pins, and all 147 scalar cases with complete output comparison.
subprocess.run([sys.executable, str(review / "replay_review_checks.py")],
               check=True, capture_output=True)
signed_checks = load(review / "source_and_replay_checks.json")
assert signed_checks["status"] == "PASS"
historical = signed / "historical-before-schur-localization"
old_artifacts = verify(load(historical / "AUTHOR_RECEIPT.json")["files"], historical)
assert pin(historical / "SIGNED_MELLIN_BLOCK_BOUND.md")["sha256"] == "99e25b2e25085077d47b575366e92e9609e83bd8db3584d2d744d9a99ff4c3f1"
signed_receipt = {
    "status": "ordinary proof accepted after explicit Schur support localization; interrupted receipt complete",
    "reviewer": "Plato (residual_gram)",
    "completion_agent": "r29_close; preserves Plato's existing complete independent review",
    "scope": "Under ordinary RH, each complete balanced central fixed mu/log block is O(1); |t| <= pi K/2 contributes O(1/log X); fixed-j high dyadic bounds are summable. No o(1), strict constant, sign, full global partition improvement or famous-conjecture conclusion.",
    "support_clarification": "The Schur norm of S is restricted to x in [X,2X] and u in [X,3X]. G and R are compact through A and A'. S itself need not be compact.",
    "source_and_replay_checks": signed_checks,
    "historical_author_artifacts_verified": old_artifacts,
    "historical_author_receipt": pin(historical / "AUTHOR_RECEIPT.json"),
    "syntax": load(review / "math_syntax_checks.json"),
    "artifacts": [pin(review / name) for name in (
        "INDEPENDENT_SIGNED_MELLIN_REVIEW.md", "replay_review_checks.py",
        "independent_exact_check_results.json", "independent_exact_check_stdout.log",
        "source_and_replay_checks.json", "check_math_syntax.cjs", "math_syntax_checks.json")],
    "verification_boundary": "The existing ordinary independent review supplies analytic acceptance. Closure checks finite algebra, syntax, source bytes and complete replay outputs only; no Lean certification or numerical extrapolation.",
}
save(review / "REVIEW_RECEIPT.json", signed_receipt)
closure = {
    "status": "PASS",
    "scope": "Interrupted R29 review package closure only; no Git, publication, prime scan, PDF build, or additional model session.",
    "author_manuscripts_unchanged_by_closure": True,
    "main_author": pin(signed / "SIGNED_MELLIN_BLOCK_BOUND.md"),
    "support_author": pin(support / "WEIGHTED_MELLIN_ENERGY.md"),
    "receipts": [pin(energy / "REVIEW_RECEIPT.json"), pin(review / "REVIEW_RECEIPT.json"),
                 pin(history / "RECOVERY_RECEIPT.json")],
    "replay_cases": {"signed": 147, "energy": 13},
    "syntax_expressions": {"signed_review": 206, "energy_review": 81},
    "script": pin(Path(__file__).resolve()),
    "theorem_status": "Individual balanced central O(1) and low O(1/log X) under RH. The actual signed carrier improvement and strict global AH threshold remain open.",
}
save(HERE / "R29_REVIEW_CLOSURE_RECEIPT.json", closure)
print(json.dumps(closure, indent=2, sort_keys=True))
