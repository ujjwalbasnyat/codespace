from fpdf import FPDF

def main():
    pdf = FPDF()
    pdf.add_page()

    name = input("Enter name: ")
    text = name + "took CS50"
    image_x = 10
    image_y = 10
    img_path = 'shirtificate.png'
    pdf.image(img_path, x = image_x, y= image_y, w=200)
    pdf.set_font('Arial',size=16 )
    text_x= image_x + 50
    text_y= image_y + 50
    pdf.set_xy(text_x, text_y)
    pdf.output('random.pdf')

main()       