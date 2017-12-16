from django import template
from django.template.defaultfilters import stringfilter

import mimetypes 
register = template.Library()


#con este filtro generaremos los distintos Htmls de previsualización de los documentos teniendo en cuenta su mimetype
@register.filter(is_safe=True)
@stringfilter
def filetype(value):
    tipo=str(mimetypes.guess_type(value,strict=True)[0])
    if ('pdf' in tipo):
        return '<div class="valign-wrapper center-align"><a target="_blank" href=/media/'+value+'><i class="large material-icons">picture_as_pdf</i></a></div>'
    elif ('image' in tipo):
        
        return '<div class="valign-wrapper center-align"><a target="_blank" href=/media/'+value+'><img class="responsive-img" src=/media/'+value+'></a></div>'
    elif ('None' in tipo ):
        return ''
    else:
        return '<div class="valign-wrapper center-align"><a target="_blank" href=/media/'+value+'><i class="large material-icons">insert_drive_file</i></a></div>'