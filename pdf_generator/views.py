from django.shortcuts import render
from weasyprint import HTML
from django.template.loader import get_template, render_to_string
from django.http import HttpResponse


# Create your views here.
def generate_pdf(request, model, template_name, pdf_name):
    print(f"model {model}") #passes
    # html_template = get_template(f"{template_name}")
    # print('html_template') #passes
    html_to_string = render_to_string(template_name=template_name, context=model)
    print('html to string')
    pdf_file = HTML(string=html_to_string).write_pdf()
    print('pdf file')
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f"filename={pdf_name}.pdf"
    print(response)
    return response


