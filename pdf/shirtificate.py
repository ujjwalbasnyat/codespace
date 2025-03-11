from fpdf import FPDF

def main():
    pdf = FPDF()
    name = input("Enter name: ")
    pdf.add_page()
    pdf.set_font('arial',size=16 )
    pdf.text(50, 50, txt=f"{name}i took CS50")
    pdf.image('shirtificate.png')
    pdf.output('random.pdf')

main()       