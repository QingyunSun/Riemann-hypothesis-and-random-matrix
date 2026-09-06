"""Render every PDF page and make traceable contact sheets for visual review.

Requires the existing Poppler commands and Pillow. The JSON is a mechanical
screen only; a reviewer must inspect the rendered sheets and flagged pages.
"""
from pathlib import Path
import argparse
import hashlib
import json
import re
import subprocess
import xml.etree.ElementTree as ET

from PIL import Image, ImageDraw


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf", type=Path)
    parser.add_argument("outdir", type=Path)
    args = parser.parse_args()
    args.outdir.mkdir(parents=True, exist_ok=True)
    prefix = args.outdir / "page"
    subprocess.run(["pdftoppm", "-r", "85", "-png", str(args.pdf), str(prefix)], check=True)
    bbox = args.outdir / "text-bboxes.html"
    subprocess.run(["pdftotext", "-bbox-layout", str(args.pdf), str(bbox)], check=True)
    info = subprocess.check_output(["pdfinfo", str(args.pdf)], text=True)
    (args.outdir / "pdfinfo.txt").write_text(info)
    page_count = int(re.search(r"^Pages:\s+(\d+)", info, re.M)[1])
    fonts = subprocess.check_output(["pdffonts", str(args.pdf)], text=True)
    (args.outdir / "pdffonts.txt").write_text(fonts)
    xml = ET.parse(bbox)
    pages = xml.findall(".//{*}page")
    assert len(pages) == page_count
    flags = []
    page_text = []
    for number, page in enumerate(pages, 1):
        width, height = float(page.attrib["width"]), float(page.attrib["height"])
        words = page.findall(".//{*}word")
        text = " ".join("".join(w.itertext()) for w in words)
        page_text.append(text)
        # The handoff has 22 mm content margins. Header/footer words must not
        # make an otherwise empty page pass the blank-page screen.
        body_words = [w for w in words if 45 <= float(w.attrib["yMin"])
                      and float(w.attrib["yMax"]) <= height-45]
        outside = []
        for word in words:
            x0, x1 = float(word.attrib["xMin"]), float(word.attrib["xMax"])
            y0, y1 = float(word.attrib["yMin"]), float(word.attrib["yMax"])
            if x0 < 12 or x1 > width-12 or y0 < 8 or y1 > height-8:
                outside.append({"text": "".join(word.itertext()), "box": [x0,y0,x1,y1]})
        if outside or not body_words or len(words) < 12 or "\ufffd" in text:
            flags.append({"page": number, "word_count": len(words),
                          "body_word_count": len(body_words),
                          "blank_body": not body_words,
                          "outside_page_safe_edge": outside,
                          "replacement_character": "\ufffd" in text})
    (args.outdir / "page_text.json").write_text(json.dumps(page_text, ensure_ascii=False)+"\n")
    images = sorted(args.outdir.glob("page-*.png"))
    assert len(images) == page_count
    sheets = []
    cell_w, cell_h, label_h = 300, 448, 22
    for start in range(0, page_count, 8):
        selected = images[start:start+8]
        canvas = Image.new("RGB", (4*cell_w, 2*(cell_h+label_h)), "#e4e8eb")
        draw = ImageDraw.Draw(canvas)
        for offset, path in enumerate(selected):
            picture = Image.open(path).convert("RGB")
            picture.thumbnail((cell_w-10, cell_h-8))
            left = (offset % 4)*cell_w
            top = (offset // 4)*(cell_h+label_h)
            draw.text((left+8, top+3), f"Page {start+offset+1}", fill="black")
            canvas.paste(picture, (left+(cell_w-picture.width)//2, top+label_h))
        sheet = args.outdir / f"contact-{start+1:04d}-{start+len(selected):04d}.png"
        canvas.save(sheet)
        sheets.append({"path": sheet.name, "first_page": start+1,
                       "last_page": start+len(selected)})
    result = {"pdf": str(args.pdf.resolve()), "pdf_sha256": hashlib.sha256(args.pdf.read_bytes()).hexdigest(),
              "page_count": page_count, "rendered_pages": len(images), "render_dpi": 85,
              "mechanical_flags": flags, "contact_sheets": sheets,
              "visual_review_status": "pending; every contact sheet must be inspected"}
    (args.outdir / "mechanical_qa.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({"pages":page_count, "sheets":len(sheets), "flagged_pages":len(flags)}))


if __name__ == "__main__":
    main()
