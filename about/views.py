# about/views.py

from django.views.generic.list_detail import object_list, object_detail

from actionmanual.sections.models import SectionItem

def about_index(request):
    items = SectionItem.objects.filter(section__name__iexact="about")\
            .filter(content_type__name="article")
    return object_list(request, 
                       queryset=items,
                       template_name='about/about.html')
