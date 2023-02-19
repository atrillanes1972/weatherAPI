from pathlib import Path
from fpdf import FPDF
import glob

filepaths = glob.glob(r'texts\*.txt')

pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:
    pdf.add_page()
    filename = Path(filepath).stem
    name = filename.capitalize()

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=10, txt=f"{name}")
    pdf.output(f"PDFs\{filename}.pdf")


