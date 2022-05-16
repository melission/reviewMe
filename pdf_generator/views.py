from weasyprint import HTML, CSS
from django.template.loader import get_template, render_to_string
from django.shortcuts import render


# Create your views here.
# def generate_pdf(request, context):
#     css = CSS(string='@page {size: landscape; background: white;} ')
#     html_to_string = render_to_string(template_name='pdf_generator/pdf_template.html', context=context)
#     pdf_file = HTML(string=html_to_string).write_pdf(optimize_size=('images',),
#                                                      stylesheets=[
#                                                          css,
#                                                          'pdf_generator/static/pdf_generator/pdf_template.css'])
#     return render(request, context=context, template_name='pdf_generator/pdf_template.html')


def generate_pdf(context):
    css = CSS(string='@page {size: landscape; background: white;} ')
    html_to_string = render_to_string(template_name='pdf_generator/pdf_template.html', context=context)
    pdf_file = HTML(string=html_to_string).write_pdf(optimize_size=('images',),
                                                     stylesheets=[
                                                         css,
                                                         CSS('pdf_generator/static/pdf_generator/pdf_template.css')])
    return pdf_file


def test(context):
    css = CSS(string='@page {size: landscape; background: white;} ')


def pdf_template(request):
    return render(request, 'pdf_generator/pdf_template.html')
