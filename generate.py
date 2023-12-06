from io import BytesIO
from fpdf import FPDF
from barcode import Code128
from barcode.writer import SVGWriter

# Create a new PDF document
pdf = FPDF()
pdf.add_page()

pdf.set_font("helvetica", "B", 16)
pdf.cell(40, 10, "A PDF page with Code128 barcodes.")

# Generate a Code128 barcode as SVG:
svg_img_bytes = BytesIO()
code1 = Code128("Code 128", writer=SVGWriter())
code1.write(svg_img_bytes)
pdf.image(svg_img_bytes, x=10, y=50, w=100, h=70)

# Generate a second Code128 barcode as SVG:
svg_img_bytes = BytesIO()
code2 = Code128("Second Code 128", writer=SVGWriter())
code2.write(svg_img_bytes)
pdf.image(svg_img_bytes, x=10, y=120, w=100, h=70)

# Output a PDF file:
pdf.output('code128_barcode.pdf')