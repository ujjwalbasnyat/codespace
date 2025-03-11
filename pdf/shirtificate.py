from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        # self.set_text_color(0,0,0)
        self.cell(0,10, "CS50 Shirtificate", ln=1, align='C')
        self.ln(20)

def main():
    pdf = PDF()
    pdf.add_page()

    name = input("Enter name: ")
    text = name + " " + "took CS50"
    image_x = 10
    image_y = 10
    img_path = 'shirtificate.png'
    pdf.image(img_path, x = image_x, y= image_y, w=200)
    pdf.set_font('Arial',size=24 )
    pdf.set_text_color(255, 255, 255)
    text_x= image_x + 50
    text_y= image_y + 50
    pdf.set_xy(text_x, text_y)
    pdf.cell(0, 10, txt=text, ln=1, align ='C')
    pdf.output('random.pdf')

main()       