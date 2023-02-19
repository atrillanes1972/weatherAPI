from pathlib import Path
from fpdf import FPDF
import glob

filepaths = glob.glob(r'texts\*.txt')

for filepath in filepaths:
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    filename = Path(filepath).stem.capitalize()
    #print(filename)
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=10, txt=f"{filename}")
    pdf.output(f"PDFs\{filename}.pdf")


