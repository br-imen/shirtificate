# CS50 Shirtificate Project

This project generates a PDF certificate with a custom name overlayed on a shirt image. The final output is a personalized "Shirtificate" for CS50.

## Requirements

- Python 3.x
- `fpdf` library for PDF generation
- `Pillow` library for image handling

You can install the required libraries using pip:

```bash
pip install fpdf Pillow
```

## Usage
To run the program, use the following command in the terminal:

```bash
python shirtificate.py
```

Make sure you have the shirtificate.png image file in the same directory as the script.

## Example
When prompted, enter your name:

```
Enter your name: John Doe
```

## How It Works
1. The program creates a new PDF document and sets the margins.
2. It adds a title "CS50 Shirtificate" to the PDF.
3. The program loads the shirt image (shirtificate.png) and centers it on the page.
4. It prompts the user for their name and overlays this name onto the shirt image in white text.
5. Finally, the program outputs the PDF as shirtificate.pdf.
Error Handling

## Error Handling
Make sure to have the shirtificate.png file in the same directory; otherwise, the program will raise a FileNotFoundError.

