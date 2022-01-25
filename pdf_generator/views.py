from weasyprint import HTML
from django.template.loader import get_template, render_to_string


# Create your views here.
def generate_pdf(request, model, template_name):
    html_to_string = render_to_string(template_name=template_name, context=model)
    pdf_file = HTML(string=html_to_string).write_pdf(optimize_size=('images',))
    return pdf_file


