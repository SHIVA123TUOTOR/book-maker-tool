from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from reportlab.lib import colors
import os

# Configuration
output_path = r"C:\Users\shiva\Downloads\hello\Jarvis_Book.pdf"
logo_path = r"C:\Users\shiva\Downloads\hello\logo.png"  # Replace with your actual logo file name
company_name = "JARVIS TECHNOLOGIES PVT. LTD."
title = "Smart Book Generator"
description = """
This tool helps you create beautiful books instantly. Add your title, input content,
and export to PDF in seconds.

You can use this to write novels, documentation, school projects, startup guides,
or anything else.

This text can be very long and the tool will automatically add pages to fit all content
neatly and include a watermark on each page.
""" * 20  # Multiply to simulate long content

# Create the canvas
c = canvas.Canvas(output_path, pagesize=A4)
width, height = A4

# --- Page 1: Cover ---
if os.path.exists(logo_path):
    logo = ImageReader(logo_path)
    c.drawImage(logo, width/2 - 1*inch, height - 2.5*inch, width=2*inch, preserveAspectRatio=True, mask='auto')

c.setFont("Helvetica-Bold", 24)
c.setFillColor(colors.darkblue)
c.drawCentredString(width/2, height - 3.5*inch, company_name)

c.setFont("Helvetica", 16)
c.setFillColor(colors.black)
c.drawCentredString(width/2, height - 4*inch, f"Book Title: {title}")
c.showPage()

# --- Page 2+: Content ---
c.setFont("Helvetica", 12)
margin_x = 1 * inch
margin_y = 1 * inch
line_height = 14
lines_per_page = int((height - 2 * margin_y) / line_height)

# Split description into lines
lines = description.strip().splitlines()
wrapped_lines = []

from textwrap import wrap
for line in lines:
    wrapped_lines.extend(wrap(line, 100))  # Wrap lines to fit width

# Draw wrapped text and paginate
for i in range(0, len(wrapped_lines), lines_per_page):
    page_lines = wrapped_lines[i:i+lines_per_page]
    y = height - margin_y

    for line in page_lines:
        y -= line_height
        c.drawString(margin_x, y, line)

    # Add watermark
    c.setFont("Helvetica-Oblique", 10)
    c.setFillColor(colors.grey)
    c.drawRightString(width - margin_x, 0.5 * inch, "Jarvis AI")
    c.setFillColor(colors.black)

    c.showPage()

# Finalize PDF
c.save()
print(f"✅ PDF created at: {output_path}")
