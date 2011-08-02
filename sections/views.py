# maestro/views.py

from django.http import Http404
from django.views.generic.list_detail import object_list, object_detail

from actionmanual.maestro.models import *

def index(request):
    section_items = SectionItem.objects.filter(section__name__iexact="home")
    if not section_items:
        raise Http404
    return object_list(request, queryset=section_items)
 
def section_index(request, section):
    section_items = SectionItem.objects.filter(section__name__iexact=section)
    if not section_items:
        raise Http404
    return object_list(request, queryset=section_items, 
                       extra_context={'section':section})
                       
