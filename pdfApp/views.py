import pdfkit
from django.shortcuts import render

html = '<!DOCTYPE html><html><body><h1>My First Heading</h1><p>My first paragraph.</p></body></html>'


def to_pdf(request):
    doc_pdf = pdfkit.from_string(html)
    return html


def to_pdf_func():
    doc_pdf = pdfkit.from_string(html)
    print(doc_pdf)
    return html
