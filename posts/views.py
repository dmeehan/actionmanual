# posts/views.py

from django.views.generic.list_detail import object_list, object_detail

from actionmanual.posts.models import *

def article_detail(request, slug):
    article = Article.live.filter(slug=slug)
    return object_detail(request, 
                       queryset=article,
                       slug = slug,)
                       
def link_detail(request, slug):
    link = Link.live.filter(slug=slug)
    return object_detail(request, 
                         queryset=link,
                         slug=slug,)