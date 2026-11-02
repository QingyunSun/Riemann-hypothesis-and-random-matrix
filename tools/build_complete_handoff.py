"""Combine already-reviewed research volumes without rewriting source proofs.

The PDF retains each volume's cover, page numbering and explicit checkpoint.
Poppler supplies concatenation and independent text/page-count verification.
"""
from pathlib import Path
import argparse
import hashlib
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
LOCAL = ROOT.parent / "Astra-Local-Archive"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pages(path: Path) -> int:
    info = subprocess.check_output(["pdfinfo", str(path)], text=True)
    return int(re.search(r"^Pages:\s+(\d+)", info, re.M)[1])


def text(path: Path) -> str:
    return subprocess.check_output(["pdftotext", "-layout", str(path), "-"], text=True)


def build(include_private: bool) -> dict:
    later_md = ROOT / "docs/handoff/ASTRA_ROUNDS_6_14_HANDOFF.md"
    later_pdf = ROOT / "output/pdf/ASTRA_ROUNDS_6_14_HANDOFF.pdf"
    prior_md = (LOCAL / "ASTRA_FULL_LOCAL_RESEARCH_HANDOFF.md" if include_private else
                ROOT / "docs/handoff/ASTRA_PUBLIC_RESEARCH_HANDOFF.md")
    prior_pdf = (LOCAL / "ASTRA_FULL_LOCAL_RESEARCH_HANDOFF.pdf" if include_private else
                 ROOT / "output/pdf/ASTRA_PUBLIC_RESEARCH_HANDOFF.pdf")
    volumes = [
        ("Latest audited programme, Rounds 6--14", later_md, later_pdf),
        ("Earlier main archive; historical claims retain their original status", prior_md, prior_pdf),
        ("Detailed Rounds 4--5 proof and experiment supplement",
         ROOT / "docs/handoff/ASTRA_ROUNDS_4_5_HANDOFF.md",
         ROOT / "output/pdf/ASTRA_ROUNDS_4_5_HANDOFF.pdf"),
    ]
    basename = "ASTRA_COMPLETE_LOCAL_CONTEXT_2026_09_05" if include_private else "ASTRA_COMPLETE_RESEARCH_CONTEXT_2026_09_05"
    md_out = LOCAL / (basename+".md") if include_private else ROOT / "docs/handoff" / (basename+".md")
    pdf_out = LOCAL / (basename+".pdf") if include_private else ROOT / "output/pdf" / (basename+".pdf")
    heading = "# Complete research handoff through Round 14\n\n"
    heading += "最新审计放在最前面。随后保留此前主档案与第 4-5 轮补编的完整原文，以保全发现、反例、失败和修正过程。历史记录中的旧状态标签不取代最新 claim ledger。当前没有证明 RH、AH 的反驳、完整 GUE、新的 zeta 间隙纪录或低于 186 的素数间隙。\n\n"
    heading += "The three complete volumes are ordered for takeover: read the latest audited results first, then consult the earlier archive and Rounds 4--5 supplement. No source proof is silently rewritten. The combined PDF retains per-volume covers and page numbering; its total page count is recorded in the accompanying index. The latest-volume source checkpoint is 2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba.\n\n"
    if include_private:
        heading += "Local-only edition: the earlier full archive includes supplied private context. This edition is not included in the public Git repository.\n\n"
    parts = [heading]
    rows = []
    next_page = 1
    for number, (title, md, pdf) in enumerate(volumes, 1):
        parts.append(f"# Volume {number}: {title}\n\n"+md.read_text())
        volume_pages = pages(pdf)
        rows.append({"volume": number, "title": title, "markdown": str(md.relative_to(ROOT)) if md.is_relative_to(ROOT) else md.name,
                     "markdown_sha256": digest(md), "pdf": str(pdf.relative_to(ROOT)) if pdf.is_relative_to(ROOT) else pdf.name,
                     "pdf_sha256": digest(pdf), "pages": volume_pages,
                     "combined_first_page": next_page,
                     "combined_last_page": next_page+volume_pages-1,
                     "zero_based_page_offset": next_page-1})
        next_page += volume_pages
    md_out.write_text("\n\n".join(parts)+"\n")
    subprocess.run(["pdfunite", *[str(v[2]) for v in volumes], str(pdf_out)], check=True)
    total = pages(pdf_out)
    assert total == sum(row["pages"] for row in rows)
    original_text = "".join(text(v[2]) for v in volumes)
    combined_text = text(pdf_out)
    assert combined_text == original_text, "PDF concatenation changed extracted source text"
    receipt = {"scope": "local private-inclusive archive" if include_private else "public archive",
               "volumes": rows, "combined_pages": total,
               "markdown_file": md_out.name, "markdown_bytes": md_out.stat().st_size,
               "markdown_sha256": digest(md_out), "pdf_file": pdf_out.name,
               "pdf_bytes": pdf_out.stat().st_size, "pdf_sha256": digest(pdf_out),
               "page_sum_check": "PASS", "complete_extracted_text_preservation": "PASS",
               "pagination": "original page numbering within each complete volume",
               "new_scientific_claims_from_combination": False}
    md_out.with_name(basename+"_INDEX.json").write_text(json.dumps(receipt,indent=2)+"\n")
    return receipt


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--include-local", action="store_true")
    args = parser.parse_args()
    results = [build(False)]
    if args.include_local:
        results.append(build(True))
    print(json.dumps(results,indent=2))


if __name__ == "__main__":
    main()
