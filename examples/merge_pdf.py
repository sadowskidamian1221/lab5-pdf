from pathlib import Path
from PyPDF2 import PdfMerger, PdfReader

def main():
    out_dir = Path("output")

    pdf_a = out_dir / "a_reportlab.pdf"
    pdf_b = out_dir / "b_reportlab.pdf"
    merged = out_dir / "merged.pdf"

    # Jeżeli brak plików - informacja
    if not pdf_a.exists() or not pdf_b.exists():
        print("Brakuje plików PDF do połączenia.")
        print("Najpierw uruchom create_pdf.py, żeby wygenerować a_reportlab.pdf i b_reportlab.pdf")
        return

    # Łączenie PDF
    merger = PdfMerger()
    merger.append(str(pdf_a))
    merger.append(str(pdf_b))

    with open(merged, "wb") as f:
        merger.write(f)

    merger.close()
    print(f"Połączono PDF -> {merged}")

    # Odczyt tekstu z pierwszej strony
    reader = PdfReader(str(merged))
    text = reader.pages[0].extract_text() or ""

    print("\n--- Tekst z 1 strony merged.pdf ---")
    print(text.strip())

if __name__ == "__main__":
    main()
