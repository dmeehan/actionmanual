# portfolio/views/explore.py
from operator import attrgetter
from itertools import chain

from django.views.generic.simple import direct_to_template
from django.views.generic.list_detail import object_list, object_detail

from tagging.models import Tag, TaggedItem
from tagging.views import tagged_object_list

from actionmanual.portfolio.models import *
from actionmanual.categories.models import *
    

def get_city_list():
    c1 = Idea.published.values_list('city', flat=True).distinct().order_by()
    c2 = Precedent.published.values_list('city', flat=True).distinct().order_by()
    cities = list(set(chain(c1, c2)))
    return cities


def explore_index(request):
    def get_recent_list():
        ideas = Idea.published.order_by('-date_published')[:2]
        precedents = Precedent.published.order_by('-date_published')[:1]
        recent = sorted(
                    chain(ideas, precedents),
                    key=attrgetter('date_published'),
                    reverse=True)
        return recent
    def get_featured_list():
        ideas = Idea.published.filter(featured=True)
        precedents = Precedent.published.filter(featured=True)
        featured = sorted(
                    chain(ideas, precedents),
                    key=attrgetter('date_published'),
                    reverse=True)
        return featured
    ideas = Idea.published.filter(featured=True)
    recent = get_recent_list()
    featured = get_featured_list()
    categories = Category.objects.all()
    cities = Idea.published.values_list('city', flat=True).distinct().order_by()
    return object_list(request,
                       queryset=ideas,
                       template_name='portfolio/explore_index.html',
                       extra_context={'recent': recent,
                                      'featured': featured,
                                      'categories': categories,
                                      'cities': cities })
                                      
def ideas_recent(request):
    recent = Idea.published.order_by('-date_published')
    categories = Category.objects.all()
    cities = Idea.published.values_list('city', flat=True).distinct().order_by()
    return object_list(request,
                       queryset=recent,
                       template_name='portfolio/explore.html',
                       extra_context={'featured': featured,
                                      'categories': categories,
                                      'cities': cities })
                                      
def ideas_featured(request):
    featured = Idea.published.filter(featured=True)
    categories = Category.objects.all()
    cities = Idea.published.values_list('city', flat=True).distinct().order_by()
    return object_list(request,
                       queryset=featured,
                       template_name='portfolio/explore.html',
                       extra_context={'featured': featured,
                                      'categories': categories,
                                      'cities': cities })

def idea_list(request):
    ideas = Idea.published.all()
    categories = Category.objects.all()
    return object_list(request,
                       queryset=ideas,
                       template_name='portfolio/idea_list.html',
                       extra_context={'categories': categories, })

def idea_detail(request, slug):
    ideas = Idea.published.select_related()
    precedents = PrecedentIdeaRelation.objects.filter(idea__slug=slug, precedent__status=2)
    return object_detail(request,
                         queryset=ideas,
                         slug=slug,
                         template_object_name='project',
                         template_name='portfolio/idea_detail.html',
                         extra_context={'precedents': precedents })
                         
def precedent_list(request):
    precedents = Precedent.published.all()
    categories = Category.objects.all()
    cities = Precedent.published.values_list('city', flat=True).distinct().order_by()
    return object_list(request,
                       queryset=precedents,
                       template_name='portfolio/precedent_list.html',
                       extra_context={'categories': categories, 'cities': cities })
                         
def precedent_detail(request, slug):
    precedents = Precedent.published.all()
    return object_detail(request,
                         queryset=precedents,
                         slug=slug,
                         template_object_name='project',
                         template_name='portfolio/precedent_detail.html',)
                         
def precedent_by_category(request, cat):
    category = Category.objects.get(slug__iexact=cat)
    categories = Category.objects.all()
    precedents = Precedent.published.filter(categories__slug=cat)
    cities = Idea.published.values_list('city', flat=True).distinct().order_by()
    return object_list(request,
                         queryset=precedents,
                         template_name='portfolio/precedent_by_category.html',
                         extra_context={'categories': categories,
                                        'cities': cities,
                                        'category': category,
                                        })

                         
                         
def category_index(request):
    categories = Category.objects.all()
    cities = Idea.published.values_list('city', flat=True).distinct().order_by()
    return object_list(request,
                       queryset=categories,
                       template_object_name = 'category',
                       template_name='portfolio/category_list.html',
                       extra_context={'cities': cities, })


def ideas_by_category(request, cat):
    def get_project_list(cat):
        ideas = Idea.published.filter(categories__slug=cat)
        precedents = Precedent.published.filter(categories__slug=cat)
        projects = sorted(
                    chain(ideas, precedents),
                    key=attrgetter('date_published'),
                    reverse=True)
        return projects
    ideas = Idea.published.filter(categories__slug=cat)
    precedents = Precedent.published.filter(categories__slug=cat)
    projects = get_project_list(cat)
    category = Category.objects.get(slug__iexact=cat)
    categories = Category.objects.all()
    cities = get_city_list()
    return object_list(request,
                       queryset = ideas,
                       paginate_by = 12,
                       template_name='portfolio/ideas_by_category.html',
                       extra_context={'object_list': projects,
                                      'categories': categories,
                                      'cities': cities,
                                      'category': category,
                                     })
                                        
def ideas_by_city(request, city_name):
    def get_project_list(city_name):
        ideas = Idea.published.filter(city__iexact=city_name)
        precedents = Precedent.published.filter(city__iexact=city_name)
        projects = sorted(
                    chain(ideas, precedents),
                    key=attrgetter('date_published'),
                    reverse=True)
        return projects
    projects = get_project_list(city_name)
    ideas = Idea.published.filter(city__iexact=city_name)
    categories = Category.objects.all()
    cities = Idea.published.values_list('city', flat=True).distinct().order_by()
    return object_list(request,
                       queryset=ideas,
                       template_name='portfolio/ideas_by_city.html',
                       extra_context={'object_list': projects,
                                      'categories': categories,
                                      'cities': cities,
                                      'current_city': city_name })
                                        
                                        
def ideas_by_tag(request, tag):
    categories = Category.objects.all()
    cities = Idea.published.values_list('city').distinct().order_by()
    return tagged_object_list(request,
                              tag=tag, 
                              queryset_or_model=Idea,
                              template_name='portfolio/ideas_by_tag.html',
                              extra_context={'categories': categories,
                                             'cities': cities,})