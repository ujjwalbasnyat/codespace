from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        #  setting font in bold size 15
        self.set_font("helvetica", style="B", size = 15)
        # moving cursor to the right
        self.cell(80)
        # printing title
        self.cell(30, 10 , "CS50 Shirtificate", align = "C")
        self.ln(20)

def main():
    pdf = PDF()
    pdf.output("header.pdf")
main()