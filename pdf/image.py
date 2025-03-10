from fpdf import FPDF

pdf =FPDF()
pdf.add_page()
pdf.image('pdf/shirtificate.png')
pdf.output('pdf_with_img.pdf')