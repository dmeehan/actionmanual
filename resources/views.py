# resources/views.py

from django.db.models import Q
from django.views.generic.list_detail import object_list, object_detail
from django.views.generic.date_based import archive_index

from tagging.models import Tag, TaggedItem

from actionmanual.sections.models import *
from actionmanual.resources.models import *
from actionmanual.categories.models import *

def resources_index(request):
    categories = Category.objects.all()
    links = Web.live.order_by('-pub_date')[:5]
    articles = Essay.live.order_by('-pub_date')[:1]
    orgs = ResourceOrganization.objects.order_by('-id')[:5]
    people = ResourcePerson.objects.order_by('-id')[:5]
    precedents = Precedent.published.all()[:5]
    return object_list(request,
                       queryset=precedents,
                       template_name='resources/resources_index.html',
                       template_object_name='precedent',
                       extra_context={'articles': articles,
                                      'links': links,
                                      'orgs': orgs,
                                      'people': people,
                                      'categories': categories,})


def resources_by_category(request, slug):
    precedents = Precedent.published.filter(categories__slug=slug).order_by('-date_published')[:4]
    category = Category.objects.get(slug=slug)
    categories = Category.objects.all()
    links = Web.live.filter(categories__category__slug=slug).order_by('pub_date')[:5]
    articles = Essay.live.filter(categories__category__slug=slug)[:1]
    orgs = ResourceOrganization.objects.filter(categories__category__slug=slug)[:5]
    people = ResourcePerson.objects.filter(categories__category__slug=slug)[:5]
    return object_list(request,
                       queryset=precedents,
                       template_name='resources/resources_by_category.html',
                       template_object_name='precedent',
                       extra_context={'categories': categories,
                                      'category': category,
                                      'articles': articles,
                                      'links': links,
                                      'orgs': orgs,
                                      'people': people,
                                      })

                                              
def resources_person_list(request):
    categories = Category.objects.all()
    people = ResourcePerson.objects.order_by('-id')
    return object_list(request, 
                       queryset=people,
                       extra_context={'categories': categories,})
    
def resources_person_detail(request, slug):
    categories = Category.objects.all()
    person = ResourcePerson.objects.filter(slug=slug)
    return object_detail(request, 
                         queryset=person,
                         slug=slug,
                         extra_context={'categories': categories,})

def resources_person_by_category(request, slug):
    categories = Category.objects.all()
    category = Category.objects.get(slug=slug)
    people = ResourcePerson.objects.filter(categories__category__slug=slug)
    return object_list(request, 
                       queryset=people,
                       extra_context={'categories': categories,
                                      'category': category,})



def resources_org_list(request):
    categories = Category.objects.all()
    orgs = ResourceOrganization.objects.order_by('-id')
    return object_list(request, 
                         queryset=orgs,
                         extra_context={'categories': categories,})
                         
def resources_org_detail(request, slug):
    categories = Category.objects.all()
    org = ResourceOrganization.objects.filter(slug=slug)
    return object_detail(request, 
                         queryset=org,
                         slug=slug,
                         extra_context={'categories': categories,})
                         
def resources_org_by_category(request, slug):
    categories = Category.objects.all()
    category = Category.objects.get(slug=slug)
    orgs = ResourceOrganization.objects.filter(categories__category__slug=slug)
    return object_list(request, 
                       queryset=orgs,
                       template_name='resources/resourceorg_by_category.html',
                       extra_context={'categories': categories,
                                      'category': category,})

                         
                         
def resources_post_list(request):
    categories = Category.objects.all()
    essays = Essay.live.all()
    return object_list(request, 
                       queryset=essays,
                       template_name='resources/post_list.html',
                       extra_context={'categories': categories,})
                         
def resources_post_detail(request, slug):
    categories = Category.objects.all()
    essay = Essay.objects.filter(slug=slug)
    return object_detail(request, 
                         queryset=essay,
                         template_name='resources/post_detail.html',
                         slug=slug,
                         extra_context={'categories': categories,})
                        
def resources_post_by_category(request, slug):
    categories = Category.objects.all()
    category = Category.objects.get(slug=slug)
    essays = Essay.live.filter(categories__category__slug=slug)
    return object_list(request, 
                       queryset=essays,
                       template_name='resources/post_by_category.html',
                       extra_context={'categories': categories,
                                      'category': category,})


def resources_link_list(request):
    categories = Category.objects.all()
    links = Web.live.all()
    return object_list(request, 
                       queryset=links,
                       template_name='resources/link_list.html',
                       extra_context={'categories': categories,})
                       

def resources_link_detail(request, slug):
    categories = Category.objects.all()
    web = Web.live.filter(slug=slug)
    return object_detail(request, 
                         queryset=web,
                         slug=slug,
                         template_name='resources/link_detail.html',
                         extra_context={'categories': categories,})
                         
def resources_link_by_category(request, slug):
    categories = Category.objects.all()
    category = Category.objects.get(slug=slug)
    links = Web.live.filter(categories__category__slug=slug)
    return object_list(request, 
                       queryset=links,
                       template_name='resources/link_by_category.html',
                       extra_context={'categories': categories,
                                      'category': category,})
                         
