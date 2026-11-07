"""Assemble the handoff without erasing the historical research stages."""
from pathlib import Path
import posixpath
import re

ROOT = Path(__file__).resolve().parent
SOURCES = (
    "README.md",
    "finite/REPORT.md",
    "finite/INDEPENDENT_REVIEW.md",
    "PERIODIC_LIFT_MASS.md",
    "bounded/REPORT.md",
    "arithmetic/REPORT.md",
    "arithmetic/CONDITIONAL_NEXT.md",
    "arithmetic/ENDPOINT_CORRECTION.md",
    "arithmetic/MAIN_TERM_THEOREM.md",
    "arithmetic/MAIN_TERM_INDEPENDENT_REVIEW.md",
    "arithmetic/SOURCE_INPUT_AUDIT.md",
    "arithmetic/SURROGATE_SHARPNESS.md",
    "source_refresh/DBM_BACKWARD_OBSTRUCTION.md",
    "source_refresh/SOURCE_REFRESH.md",
    "REPRODUCTION.md",
)


def adjusted_links(text: str, relative_source: str) -> str:
    parent = posixpath.dirname(relative_source)

    def replace(match: re.Match[str]) -> str:
        label, target = match.groups()
        if target.startswith(("https:", "http:", "#", "/", "mailto:")):
            return match.group(0)
        return f"[{label}]({posixpath.normpath(posixpath.join(parent, target))})"

    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", replace, text)


if __name__ == "__main__":
    chunks = [
        "# Research addendum: quantitative survival and a conditional zeta theorem\n\n"
        "6 November 2026. This addendum supplements the full historical handoff in PR #6. "
        "The singular-series main term has now been evaluated; the required actual-prime "
        "discrepancy estimate remains open. Earlier intermediate records are retained "
        "and explicitly labelled as historical stages. Finite certificates, conditional "
        "theorems, numerical diagnostics and external source claims are distinguished.\n"
    ]
    for source in SOURCES:
        text = (ROOT / source).read_text()
        heading, _, remainder = adjusted_links(text, source).partition("\n")
        chunks.append(f"\n\n---\n\n{heading}\n\n_Source: {source}_\n" + remainder)
    output = ROOT / "HANDOFF_ADDENDUM.md"
    output.write_text("".join(chunks).rstrip() + "\n")
    print(f"{output}: {len(output.read_text().split())} whitespace-delimited words")
