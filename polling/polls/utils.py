from django.http import HttpResponse
from xhtml2pdf import pisa


def render_to_pdf(template, context):

    html = template.render(context)
    response = HttpResponse(content_type='application/pdf')

    # to view on browser we can remove attachment 
    response['Content-Disposition'] = 'filename="report.pdf"'

   # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
      return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
