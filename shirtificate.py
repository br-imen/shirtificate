from fpdf import FPDF
from PIL import Image

# Create a new PDF instance
pdf = FPDF()
pdf.set_margins(left=10, top=10, right=10)
pdf.add_page(orientation='P', format='A4')

# Set the title of the PDF
pdf.set_font('Times', 'B', 24)
pdf.cell(0, 10, 'CS50 Shirtificate', ln=True, align='C')

# Add some space between the title and the image
pdf.ln(20)

# Add the shirt image, centered
shirt = Image.open("shirtificate.png")
width, height = shirt.size
pdf.image('shirtificate.png', x=(210 - 190) / 2, w=190, h=(190/width)*height)

# Prompt the user for their name
name = input("Enter your name: ")

# Set font and text color to white for the name on the shirt
pdf.set_font('Times', 'B', 36)
pdf.set_text_color(255, 255, 255)

# Position the name on top of the shirt (adjust y-position based on the shirt image)
pdf.text(x=55, y=140, txt=name)

# Output the PDF
pdf.output('shirtificate.pdf')
