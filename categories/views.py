# categories/views.py

from django.views.generic.list_detail import object_list, object_detail

from actionmanual.categories.models import *
from actionmanual.portfolio.models import *
from actionmanual.posts.models import *

def category_index(request):
    categories = Category.objects.all()
    return object_list(request,
                       queryset=categories,
                       template_object_name = 'category',)


def category_detail(request, slug):
    category = Category.objects.all()
    ideas = Idea.published.filter(categories__slug=slug)
    precedents = Precedent.published.filter(categories__slug=slug)
    #links = Link.live.filter(categories__slug=slug)
    #articles = Article.live.filter(categories__slug=slug)
    return object_detail(request,
                         queryset=category,
                         slug=slug,
                         slug_field='slug',
                         template_object_name = 'category',
                         extra_context={'ideas': ideas,
                                        'precedents': precedents,
                                        #'links': links,
                                        #'articles': articles, 
                                        })
                       
