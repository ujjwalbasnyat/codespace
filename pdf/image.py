from fpdf import FPDF

pdf =FPDF()
pdf.add_page()
pdf.image('shirtificate.png', w=20, h=20)
pdf.output('pdf_with_img.pdf')