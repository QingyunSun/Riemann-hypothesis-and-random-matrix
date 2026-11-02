"""Pin this bounded note and its actually read sources; no mathematical replay."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
STAGE = HERE.parents[2]


def pin(path):
    data = path.read_bytes()
    return {"path": str(path), "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


specs = [
    ("bui-florea-milinovich", "https://arxiv.org/pdf/2310.03949",
     "Theorem 3.1 and its complete surrounding proof, printed pages 8-10; journal theorem also read at DOI 10.1112/blms.13092."),
    ("carneiro-chandee-milinovich-S", "https://arxiv.org/pdf/1309.1526",
     "Printed pages 1-2, zero counting convention, equation (1), and Theorem 2; only the RH order bound for S(t) is used."),
    ("milinovich-ng-gonek", "https://home.olemiss.edu/~mbmilino/Gonek.pdf",
     "Proposition (2.3), fixed theta and prefix definition, printed pages 3-4; reciprocal residue and horizontal-error passages in sections 3-4."),
]
sources = []
for name, url, scope in specs:
    for suffix in (".pdf", ".txt"):
        sources.append({**pin(HERE / "sources" / (name + suffix)), "url": url,
                        "read_scope": scope, "publication": "Full primary body/extraction stays local; hashes may be public."})
dependencies = [
    STAGE / "research-round29/signed-mellin-test/SIGNED_MELLIN_BLOCK_BOUND.md",
    STAGE / "research-round29/signed-mellin-test/sources/montgomery-vaughan-hilbert-1974.pdf",
    STAGE / "research-round30/stationary-challenge/UPPER_HEIGHT_BALANCED_CHECK.md",
    STAGE / "research-round30/central-followup/ROOT_JOINT_ZERO_SAMPLING.md",
]
syntax = json.loads((HERE / "math_syntax_checks.json").read_text())
result = {
    "status": "bounded ordinary source/applicability note complete",
    "author": "r29_close",
    "sources": sources,
    "programme_dependencies": [pin(path) for path in dependencies],
    "artifacts": [pin(HERE / name) for name in ("ZERO_MOMENT_APPLICABILITY.md", "check_note_syntax.cjs", "math_syntax_checks.json", "write_source_receipt.py")],
    "syntax": syntax,
    "source_findings": "The exact all-length BFM theorem applies but its error is too large at D comparable to T. The explicit prime-power cross term vanishes for the sharp annulus. Milinovich-Ng's fixed-theta weighted prefix theorem is not an endpoint theorem for this annulus.",
    "ordinary_result": "RH zero-counting plus fixed-width phase removal proves density-normalized separate sampling with an additive O(T^2/loglog T) error. No relative asymptotic for every central carrier window is assumed.",
    "independent_joint_review": "Complete ROOT_JOINT_ZERO_SAMPLING.md read and independently checked: all three centered derivative norms, common phase log(DK/X), full product variation O(T^2 log^2 T), multiplicity-aware complex Stieltjes integration, coefficient 2/(X log^3 T), and absolute O(1/loglog T) error are correct. Accepted as a comparison, with the signed zero sum unevaluated.",
    "height_review": "Uniform bounded proof extends to alpha=2; specified uniformly controlled balanced dyadic families have limsup absolute tail O(2^(-3J/4)). Fixed central blocks and global masked/unbalanced packets remain uncontrolled.",
    "formal_verification": False,
    "new_prime_or_zero_scan": False,
    "strict_joint_gain_proved": False,
    "limits": "Ordinary proof review, not external novelty audit or proof-assistant certification. Sources remain local. No Git mutation, model call, or new numerical computation."
}
path = HERE / "SOURCE_REVIEW_RECEIPT.json"
path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
print(json.dumps({"receipt": pin(path), "note": pin(HERE / "ZERO_MOMENT_APPLICABILITY.md"),
                  "syntax": syntax}, indent=2))
