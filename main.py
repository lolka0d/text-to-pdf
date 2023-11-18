import glob
from fpdf import FPDF

filepaths = glob.glob('text_files/*.txt')

for filepath in filepaths:
    filename = filepath.split('/')[-1].split('.')[0]

    pdf = FPDF(
        orientation="P",
        unit="mm",
        format="A4",
    )

    pdf.add_page()

    # Set the header
    pdf.set_font(family="Times", size=24, style="B")
    pdf.set_text_color(0, 0, 0)

    pdf.cell(w=0, h=12, txt=filename.title(), align="L", ln=1)

    pdf.set_font(family="Times", size=10, style="B")
    with open(filepath) as file:
        content = file.read()
        pdf.multi_cell(w=0, h=6, txt=content, align="L")

    pdf.output(f'pdf`s/{filename}.pdf')