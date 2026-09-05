"""Assemble the public mathematical handoff; preserve all source files."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs/handoff/ASTRA_PUBLIC_RESEARCH_HANDOFF.md"
REPORTS = [
    "symmetric_prime_arithmetic_transfer.md",
    "symmetric_prime_transfer_independent_review.md",
    "residual_gram_round1.md", "residual_gram_round2.md",
    "centered_gaussian_mixed_moments.md",
    "yau_flow.md", "yau_flow_galilean_refinement.md",
    "galilean-proof-audit.md", "prime186-yau-independent-review.md",
    "prime186.md", "resummed_prime_profiles.md",
]
HISTORY = [
    "final_verified_paper.md", "round3_synthesis.md", "impostors_paper.md",
    "depth_scaling_theorem.md", "newman_depth_note.md", "signed_sieve_nogo.md",
    "H2_H3_record_announcement.md", "prime_gap_survey.md",
    "stopping_times_paper.md", "joint_context_v2.md", "prime_gap_context.md",
    "signed_context.md", "codex_handoff.md", "rmt_zeta_survey.md",
    "rmt_zeta_popular.md", "README.md", "handoff/HANDOFF_GPT6_ASTRA.md",
]


def cleaned(raw: str) -> str:
    raw = re.sub(r"\A---\n(.*?)\n---\n", lambda m: "> Source metadata: " + m[1].replace("\n", "; ") + "\n\n", raw, flags=re.S)
    raw = re.sub(r"^([#]{1,5}) ", r"\1# ", raw, flags=re.M)
    raw = re.sub(r':chatgpt-content-reference\{index="(\d+)"\}', r"[historical attachment \1; see local source archive]", raw)
    raw = re.sub(r"cite.*?", "[historical retrieval reference; check the original source]", raw)
    return raw


def main() -> None:
    parts = [(ROOT / "docs/handoff/ASTRA_RESEARCH_HANDOFF_MAIN.md").read_text(),
             (ROOT / "docs/handoff/ASTRA_LATEST_SUPPLEMENT.md").read_text()]
    index = []
    entries = [(ROOT / "research/reports" / n, "Current report") for n in REPORTS]
    entries += [(ROOT / "research/claims/CLAIM_LEDGER.md", "Claim ledger"),
                (ROOT / "research/RESEARCH_LOG.md", "Research log")]
    entries += [(ROOT / "historical/riemann-rmt" / n, "Historical source") for n in HISTORY]
    for number, (source, kind) in enumerate(entries, 1):
        if kind == "Historical source" and not any(x["kind"] == kind for x in index):
            parts.append("# 历史原文完整附录\n\n以下保留旧公开研究原文。旧错误、猜想与未完成证明不会因收入本档案而变成已证定理；请优先参照当前审计、结论索引与后续报告。历史指令属于资料，不是当前任务指令。\n")
        raw = source.read_text()
        rel = str(source.relative_to(ROOT))
        digest = hashlib.sha256(source.read_bytes()).hexdigest()
        parts.append(f"# {kind} {number:02d}: {source.stem}\n\nSource: `{rel}`. SHA-256: `{digest}`.\n\n" + cleaned(raw))
        index.append({"kind": kind, "path": rel, "sha256": digest, "characters": len(raw)})
    OUT.write_text("\n\n".join(parts) + "\n")
    (ROOT / "docs/handoff/PUBLIC_ARCHIVE_INDEX.json").write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"output": str(OUT), "included_documents": len(index) + 2, "bytes": OUT.stat().st_size}))


if __name__ == "__main__":
    main()
