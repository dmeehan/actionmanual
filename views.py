# views.py

from django.views.generic.list_detail import object_list, object_detail

from tagging.views import tagged_object_list

from actionmanual.portfolio.models import Idea, Precedent
                       
                       

def ideas_by_tag(request, tag):
    queryset = Idea.published.all()
    return tagged_object_list(request, 
                              queryset,
                              tag,
                              template_name='portfolio/project_list.html',)

def precedents_by_tag(request, tag):
    queryset = Precedent.published.all()
    return tagged_object_list(request, 
                              queryset,
                              tag,
                              template_name='portfolio/project_list.html',)

def tag_detail(request, tag):
    query_tag = Tag.objects.get(name=tag)
    queryset = query_tag.items.all()
    return object_list(request,
                       queryset,
                       tag,
                       template_name='tag_detail.html',)
