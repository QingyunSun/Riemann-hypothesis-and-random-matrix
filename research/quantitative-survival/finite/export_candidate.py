"""Export an optional floating search run; never overwrite the certified seed.

Run quantify.py, then pivot.py, then this script. Floating search can vary by
BLAS/optimizer version. The committed candidate.json is the fixed certificate
input; candidate.reconstructed.json is only a search-provenance artifact.
"""
import ast
import json
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent

if __name__ == "__main__":
    floating = np.load(ROOT / "floating.npz")
    pivots = np.load(ROOT / "pivots.npz")
    scales = np.linalg.norm(floating["A"] * floating["q"], axis=1)
    data = {
        "N": 11,
        "exp_time": "85/84",
        "independent_constraints": [
            [list(part) for part in ast.literal_eval(str(floating["labels"][row]))]
            for row in pivots["rows"]
        ],
        "dependent_coordinates": pivots["cols"].tolist(),
        "candidate_relative_changes_hex": [
            float(x).hex() for x in pivots["h"]
        ],
        "row_scales_hex": [
            float(x).hex() for x in scales[pivots["rows"]]
        ],
        "survival_differences": floating["d"].astype(int).tolist(),
    }
    output = ROOT / "candidate.reconstructed.json"
    output.write_text(json.dumps(data, separators=(",", ":")))
    fixed = json.loads((ROOT / "candidate.json").read_text())
    print(json.dumps({
        "output": str(output),
        "matches_committed_candidate_as_json": data == fixed,
        "status": "Search provenance only; run the interval verifier for proof.",
    }, indent=2))
