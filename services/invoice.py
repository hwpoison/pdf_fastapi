from .pdf_generator import pdf

def invoice(vars):
    new_ticket = pdf.create_pdf('factura/index.html', vars)
    return new_ticket
