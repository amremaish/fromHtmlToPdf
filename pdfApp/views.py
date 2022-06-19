import pdfkit
from django.http import HttpResponse
from django.shortcuts import render

html = '<!DOCTYPE html><html><body><h1>My First Heading</h1><p>My first paragraph.</p></body></html>'


def to_pdf(request):
    doc_pdf = pdfkit.from_string(html)
    return HttpResponse(doc_pdf, content_type='application/octet-stream')


def to_pdf_func():
    doc_pdf = pdfkit.from_string(html)
    print(doc_pdf)
    return html
