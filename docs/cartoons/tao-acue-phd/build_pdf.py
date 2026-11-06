"""Rebuild the poster PDF without changing the source image pixels."""
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.lib.utils import ImageReader

ROOT = Path(__file__).resolve().parent
IMAGE = ROOT / "Tao-ACUE-PhD-cartoon.png"
OUTPUT = ROOT / "Tao-ACUE-PhD-cartoon.pdf"
ROWS = [
    (128, 628, "1-2  The statistical question and the heat experiment",
     "<b>Convention.</b> Time runs in the attractive scalar-heat direction. Fourier modes decay, while real zeros may approach and collide. The curve illustration is schematic. Both ensemble rings illustrate the same particle count, N = 7."),
    (634, 1086, "3-4  An exact counterexample and its mechanism",
     "<b>Exact interpretation.</b> Both four-point examples are grid configurations. Their unlabelled full pair data agree. The six-point example also matches the gap histogram. Its graph shows tangent slopes from the common initial value 7; it does not plot complete trajectories."),
    (1090, 1480, "5-6  The scale distinction and the missing arithmetic",
     "<b>Scope.</b> The CUE scale is probabilistic. The ACUE statement is a lower bound, and some configurations never collide. The arithmetic bridge to actual zeta zeros remains open in these results. The six-point construction changes a protected cubic moment.")
]
style = ParagraphStyle("notes", fontName="Helvetica", fontSize=10,
                       leading=13, textColor="#233d3d")

def main():
    image = ImageReader(str(IMAGE))
    iw, ih = image.getSize()
    if (iw, ih) != (1024, 1536):
        raise ValueError("Review panel crop coordinates before using another raster size.")
    pdf = canvas.Canvas(str(OUTPUT), pagesize=(768,1152), pageCompression=1, invariant=1)
    pdf.setTitle("What pair correlations forget - a PhD cartoon")
    pdf.setAuthor("Riemann zeta / random-matrix research programme")
    pdf.setSubject("Finite ACUE counterexamples, scalar heat, and the unresolved zeta bridge")
    pdf.drawImage(image, 0, 0, width=768, height=1152)
    pdf.showPage()
    width, height = landscape(A4)
    for page, (top, bottom, title, caption) in enumerate(ROWS, start=2):
        pdf.setPageSize((width, height))
        pdf.setFillColorRGB(.04,.23,.22)
        pdf.setFont("Helvetica-Bold", 15)
        pdf.drawString(24, height-31, title)
        scale = (width-48)/iw
        panel_height = (bottom-top)*scale
        panel_bottom = height-51-panel_height
        pdf.saveState()
        clip = pdf.beginPath()
        clip.rect(24, panel_bottom, width-48, panel_height)
        pdf.clipPath(clip, stroke=0)
        pdf.drawImage(image, 24, panel_bottom+(bottom-ih)*scale,
                      width=iw*scale, height=ih*scale)
        pdf.restoreState()
        para = Paragraph(caption, style)
        _, note_height = para.wrap(width-48, 100)
        note_top = panel_bottom-16
        if note_top-note_height < 47:
            raise ValueError("Caption would overlap footer.")
        para.drawOn(pdf, 24, note_top-note_height)
        pdf.setFont("Helvetica", 8)
        pdf.setFillColorRGB(.3,.35,.35)
        pdf.drawString(24, 23, "Tao meeting note, 5 Nov 2026 | Mathematical details and sources: accompanying README")
        pdf.drawRightString(width-24, 23, f"{page} / 4")
        pdf.showPage()
    pdf.save()
    print(OUTPUT)

if __name__ == "__main__":
    main()
