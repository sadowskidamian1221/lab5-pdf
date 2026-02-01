from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

def create_pdf(path: Path, title: str, lines: list[str]) -> None:
    c = canvas.Canvas(str(path), pagesize=A4)
    width, height = A4

    # tytuł
    c.setFont("Helvetica-Bold", 18)
    c.drawString(50, height - 60, title)

    # treść
    c.setFont("Helvetica", 12)
    y = height - 100
    for line in lines:
        c.drawString(50, y, line)
        y -= 18

    # stopka
    c.setFont("Helvetica-Oblique", 10)
    c.drawString(50, 40, f"Wygenerowano przez ReportLab: {path.name}")

    c.showPage()
    c.save()

def main():
    out_dir = Path("output")
    out_dir.mkdir(exist_ok=True)

    pdf1 = out_dir / "a_reportlab.pdf"
    pdf2 = out_dir / "b_reportlab.pdf"

    create_pdf(pdf1, "PDF A (ReportLab)", ["Linia 1", "Linia 2", "Linia 3"])
    create_pdf(pdf2, "PDF B (ReportLab)", ["To jest drugi plik PDF", "Kolejna linia tekstu"])

    print("Gotowe! Wygenerowano dwa pliki PDF w folderze output")

if __name__ == "__main__":
    main()
