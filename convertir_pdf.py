from docx import Document
from fpdf import FPDF

def docx_to_pdf(docx_path, pdf_path):
    # Lee el archivo DOCX
    doc = Document(docx_path)
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=10)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Extrae y agrega el texto del DOCX al PDF
    for para in doc.paragraphs:
        pdf.multi_cell(0, 10, para.text)

    # Guarda el PDF
    pdf.output(pdf_path)
    print(f"PDF guardado en: {pdf_path}")

# Usar la función
docx_to_pdf("prueba_VIANEY.docx", "salida.pdf")
