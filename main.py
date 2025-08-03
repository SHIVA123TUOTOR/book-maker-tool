from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
import os

# Config
title = "Jarvis AI Project Report"
description = "This is a multi-page report with watermark and logo."
output_pdf = os.path.join("docs", "Jarvis_Report.pdf")
logo_path = os.path.join("docs", "logo.png")  # You must add this manually

def create_pdf():
    c = canvas.Canvas(output_pdf, pagesize=A4)
    width, height = A4

    # First page with logo
    if os.path.exists(logo_path):
        c.drawImage(ImageReader(logo_path), inch, height - 2*inch, width=2*inch, preserveAspectRatio=True)
    c.setFont("Helvetica-Bold", 24)
    c.drawCentredString(width/2, height - 3*inch, "Jarvis AI")
    c.setFont("Helvetica", 14)
    c.drawString(inch, height - 4*inch, description)
    c.setFont("Helvetica-Oblique", 10)
    c.drawRightString(width - inch, 0.5*inch, "Jarvis AI")
    c.showPage()

    # Simulated multiple pages
    for i in range(1, 6):
        c.setFont("Helvetica", 14)
        c.drawString(inch, height - inch, f"Page {i} - Sample content goes here...")
        c.setFont("Helvetica-Oblique", 10)
        c.drawRightString(width - inch, 0.5*inch, "Jarvis AI")  # watermark
        c.showPage()

    c.save()

if _name_ == "_main_":
    create_pdf()
