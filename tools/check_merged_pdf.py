"""Verify every merged PDF page equals its indexed source rendering.

This does not replace source visual review. Exact pixel matches preserve that
review's coverage. Any differing page is recorded for further visual review.
Requires Poppler and Pillow; all page images and per-page hashes are retained.
"""
from pathlib import Path
import argparse
import hashlib
import json
import subprocess

from PIL import Image, ImageChops

ROOT = Path(__file__).resolve().parents[1]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def resolve(index: Path, name: str) -> Path:
    candidates = [ROOT / name, index.parent / name, ROOT / "output/pdf" / name]
    return next(p for p in candidates if p.is_file())


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("outdir", type=Path)
    parser.add_argument("indexes", type=Path, nargs="+")
    args = parser.parse_args()
    args.outdir.mkdir(parents=True, exist_ok=True)
    rendered = {}

    def render(path: Path, expected_hash: str, expected_pages: int) -> list[str]:
        assert digest(path) == expected_hash, f"Source changed: {path}"
        if expected_hash in rendered:
            return rendered[expected_hash]
        folder = args.outdir / expected_hash[:16]
        folder.mkdir(exist_ok=True)
        subprocess.run(["pdftoppm", "-r", "55", "-png", str(path),
                        str(folder / "page")], check=True)
        images = sorted(folder.glob("page-*.png"))
        assert len(images) == expected_pages, (path, len(images), expected_pages)
        hashes = []
        for image in images:
            with Image.open(image) as opened:
                rgb = opened.convert("RGB")
                hashes.append(hashlib.sha256(str(rgb.size).encode()+rgb.tobytes()).hexdigest())
        (folder / "render.json").write_text(json.dumps({
            "pdf_sha256": expected_hash, "pages": expected_pages, "dpi": 55,
            "pixel_hashes": hashes}, indent=2)+"\n")
        rendered[expected_hash] = hashes
        return hashes

    receipts = []
    for index_path in args.indexes:
        index = json.loads(index_path.read_text())
        combined = render(resolve(index_path, index["pdf_file"]),
                          index["pdf_sha256"], index["combined_pages"])
        mapped = []
        differences = []
        for volume in index["volumes"]:
            source = render(resolve(index_path, volume["pdf"]),
                            volume["pdf_sha256"], volume["pages"])
            for position, source_hash in enumerate(source):
                merged_page = volume["zero_based_page_offset"]+position+1
                identical = combined[merged_page-1] == source_hash
                if not identical:
                    merged_image = args.outdir / index["pdf_sha256"][:16] / f"page-{merged_page:03d}.png"
                    source_folder = args.outdir / volume["pdf_sha256"][:16]
                    source_images = sorted(source_folder.glob("page-*.png"))
                    with Image.open(merged_image) as left, Image.open(source_images[position]) as right:
                        assert left.size == right.size, (index_path, merged_page, "different dimensions")
                        diff = ImageChops.difference(left.convert("RGB"), right.convert("RGB"))
                        pixels = list(diff.get_flattened_data())
                        differences.append({"combined_page": merged_page,
                            "source_volume": volume["volume"], "source_page": position+1,
                            "different_pixels": sum(p != (0, 0, 0) for p in pixels),
                            "maximum_channel_difference": max(max(p) for p in pixels),
                            "difference_bbox": diff.getbbox()})
                mapped.append({"combined_page": merged_page,
                               "source_volume": volume["volume"],
                               "source_page": position+1, "source_pixel_sha256": source_hash,
                               "merged_pixel_sha256": combined[merged_page-1],
                               "pixel_identical": identical})
        assert [r["combined_page"] for r in mapped] == list(range(1, len(combined)+1))
        receipt = {"index_file": index_path.name, "index_sha256": digest(index_path),
                   "pdf_sha256": index["pdf_sha256"], "pages": len(combined),
                   "render_dpi": 55, "exactly_matching_pages": len(combined)-len(differences),
                   "full_page_pixel_identity": "PASS" if not differences else "DIFFERENCES_REQUIRE_VISUAL_REVIEW",
                   "scope": "Every page compared with its indexed source; exact matches inherit source visual QA. Recorded differences require separate review.",
                   "differing_pages": differences,
                   "page_mapping": mapped}
        (args.outdir / (index_path.stem+"_RASTER_QA.json")).write_text(json.dumps(receipt, indent=2)+"\n")
        receipts.append({k:v for k,v in receipt.items() if k != "page_mapping"})
    print(json.dumps(receipts, indent=2))


if __name__ == "__main__":
    main()
