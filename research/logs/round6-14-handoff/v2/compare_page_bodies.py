#!/usr/bin/env python3
"""Compare rendered page bodies exactly; never alter source PDFs or PNGs.

Requires Pillow. Run from any directory. The default directories are this
script's directory (v2) and its sibling v1. JSON records all input image hashes,
pixel-body hashes, and every matching page, including possible ambiguities.
Only the running header/footer area is excluded: 45 PDF points at each end,
rounded outwards to an integer number of rendered pixels.
"""
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

from PIL import Image, ImageChops


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def collect(folder: Path) -> tuple[dict, list[dict]]:
    mechanical = json.loads((folder / "mechanical_qa.json").read_text())
    dpi = mechanical["render_dpi"]
    padding = math.ceil(45 * dpi / 72)
    pages = []
    files = sorted(folder.glob("page-[0-9][0-9][0-9].png"))
    assert len(files) == mechanical["page_count"] == mechanical["rendered_pages"]
    assert [int(p.stem.split("-")[1]) for p in files] == list(range(1, len(files) + 1))
    for path in files:
        with Image.open(path) as image:
            image = image.convert("RGB")
            width, height = image.size
            crop_box = (0, padding, width, height - padding)
            cropped = image.crop(crop_box)
            # Dimension prefix prevents equally sized byte strings from
            # differently shaped images being treated as matching images.
            prefix = f"RGB:{cropped.width}x{cropped.height}:".encode("ascii")
            body_hash = hashlib.sha256(prefix + cropped.tobytes()).hexdigest()
        pages.append({
            "page": int(path.stem.split("-")[1]),
            "filename": path.name,
            "png_sha256": sha256(path),
            "body_pixel_sha256": body_hash,
            "full_dimensions_pixels": [width, height],
            "crop_box_pixels": list(crop_box),
        })
    return mechanical, pages


def main() -> None:
    v2 = Path(__file__).resolve().parent
    v1 = v2.parent / "v1"
    old_meta, old_pages = collect(v1)
    new_meta, new_pages = collect(v2)
    actual_pdf_sha256 = sha256(Path(new_meta["pdf"]))
    assert actual_pdf_sha256 == new_meta["pdf_sha256"], "Final PDF changed since rendering"
    assert old_meta["render_dpi"] == new_meta["render_dpi"]
    by_hash: dict[str, list[int]] = {}
    for page in old_pages:
        by_hash.setdefault(page["body_pixel_sha256"], []).append(page["page"])
    mapping = []
    used_old = set()
    for page in new_pages:
        candidates = by_hash.get(page["body_pixel_sha256"], [])
        used_old.update(candidates)
        mapping.append({"v2_page": page["page"], "matching_v1_pages": candidates})
    unmatched = [m["v2_page"] for m in mapping if not m["matching_v1_pages"]]
    ambiguous = [m for m in mapping if len(m["matching_v1_pages"]) > 1]
    # Compact consecutive ranges with a unique match and constant offset.
    ranges = []
    for entry in mapping:
        if len(entry["matching_v1_pages"]) != 1:
            continue
        new, old = entry["v2_page"], entry["matching_v1_pages"][0]
        if ranges and new == ranges[-1]["v2_last"] + 1 and old == ranges[-1]["v1_last"] + 1:
            ranges[-1].update(v2_last=new, v1_last=old)
        else:
            ranges.append({"v2_first": new, "v2_last": new, "v1_first": old, "v1_last": old})
    aligned_diagnostics = []
    unique = [m for m in mapping if len(m["matching_v1_pages"]) == 1]
    for new in unmatched:
        # This candidate is diagnostic only: it never upgrades an unmatched
        # page to an exact match. Use the next proved match's offset, or the
        # last preceding match when this is the final page.
        anchor = next((m for m in unique if m["v2_page"] > new), unique[-1])
        offset = anchor["matching_v1_pages"][0] - anchor["v2_page"]
        old = new + offset
        assert 1 <= old <= len(old_pages)
        crop = tuple(new_pages[new - 1]["crop_box_pixels"])
        with Image.open(v2 / f"page-{new:03}.png") as a, Image.open(v1 / f"page-{old:03}.png") as b:
            diff = ImageChops.difference(a.convert("RGB").crop(crop), b.convert("RGB").crop(crop))
            red, green, blue = diff.split()
            maximum_channel = ImageChops.lighter(ImageChops.lighter(red, green), blue)
            histogram = maximum_channel.histogram()
            aligned_diagnostics.append({
                "v2_page": new, "candidate_v1_page": old,
                "alignment_anchor_v2_page": anchor["v2_page"],
                "nonidentical_rgb_pixels": diff.width * diff.height - histogram[0],
                "maximum_absolute_channel_difference": maximum_channel.getextrema()[1],
                "difference_bbox_relative_to_crop": list(diff.getbbox()),
            })
    result = {
        "method": "Exact SHA-256 of RGB pixel bytes and dimensions, full width, excluding 45pt top/bottom rounded outwards; no image resampling or tolerance",
        "script_sha256": sha256(Path(__file__).resolve()),
        "v1_directory": str(v1), "v2_directory": str(v2),
        "v1_pdf_sha256_from_render_receipt": old_meta["pdf_sha256"],
        "v2_pdf_sha256_verified_current_file": actual_pdf_sha256,
        "dpi": new_meta["render_dpi"],
        "v1_page_count": len(old_pages), "v2_page_count": len(new_pages),
        "matched_v2_count": len(new_pages) - len(unmatched),
        "unmatched_v2_pages": unmatched,
        "ambiguous_mappings": ambiguous,
        "v1_pages_without_any_identical_v2_body": [p["page"] for p in old_pages if p["page"] not in used_old],
        "unique_matching_ranges": ranges,
        "mapping": mapping,
        "unmatched_alignment_diagnostics": aligned_diagnostics,
        "v1_pages": old_pages,
        "v2_pages": new_pages,
    }
    output = v2 / "page_body_comparison.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: result[k] for k in (
        "v2_pdf_sha256_verified_current_file", "v1_page_count", "v2_page_count",
        "matched_v2_count", "unmatched_v2_pages", "ambiguous_mappings",
        "v1_pages_without_any_identical_v2_body", "unique_matching_ranges")}, indent=2))


if __name__ == "__main__":
    main()
