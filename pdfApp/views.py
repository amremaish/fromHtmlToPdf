import pdfkit
from django.http import HttpResponse
from weasyprint import HTML

html = '<!DOCTYPE html><html><body><h1>My First Heading</h1><p>My first paragraph.</p></body></html>'


def to_pdf(request):
    doc_pdf = pdfkit.from_string(html)
    return HttpResponse(doc_pdf, content_type='application/octet-stream')


def to_pdf_func():
    doc_pdf = HTML(string=html, base_url="").write_pdf()
    print(doc_pdf)
    file = open("sample.pdf", "wb")
    file.write(doc_pdf)
    file.close()
    return html
