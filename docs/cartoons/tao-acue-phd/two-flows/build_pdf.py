"""Place the unchanged comic pages into a two-page printable PDF."""
from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent


def build() -> Path:
    output = ROOT / "Tao-ACUE-two-flows-cartoon.pdf"
    width, height = A4
    margin = 14
    document = canvas.Canvas(str(output), pagesize=A4, pageCompression=1)
    document.setTitle("Pair data, two flows, and the missing arithmetic bridge")
    document.setSubject("Two English mathematical comic pages based on the Tao meeting note")
    for filename in ("01-pair-data.png", "02-two-flows.png"):
        image = ImageReader(str(ROOT / filename))
        iw, ih = image.getSize()
        scale = min((width - 2 * margin) / iw, (height - 2 * margin) / ih)
        w, h = iw * scale, ih * scale
        assert 0 < w <= width - 2 * margin + 1e-8
        assert 0 < h <= height - 2 * margin + 1e-8
        document.drawImage(image, (width - w) / 2, (height - h) / 2, w, h)
        document.showPage()
    document.save()
    reader = PdfReader(str(output))
    assert len(reader.pages) == 2
    assert all(len(page.images) == 1 for page in reader.pages)
    print(output)
    return output


if __name__ == "__main__":
    build()
