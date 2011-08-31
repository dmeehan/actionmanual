# portfolio/views.py

from django.http import HttpResponseRedirect
from django.http import HttpResponseForbidden
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic.list_detail import object_list, object_detail
from django.template.defaultfilters import slugify
from django.template import RequestContext

from tagging.models import Tag, TaggedItem
from tagging.views import tagged_object_list

from actionmanual.portfolio.models import *
from actionmanual.sections.models import *
from actionmanual.categories.models import *

from actionmanual.portfolio.forms import *

def explore_index(request):
    recent = Idea.published.order_by('-date_published')[:3]
    featured = Idea.published.filter(featured=True)
    categories = Category.objects.all()
    cities = Idea.published.values_list('city', flat=True).distinct()
    return object_list(request,
                       queryset=recent,
                       template_name='portfolio/explore_index.html',
                       extra_context={'featured': featured,
                                      'categories': categories,
                                      'cities': cities })
                                      
def ideas_recent(request):
    recent = Idea.published.order_by('-date_published')
    categories = Category.objects.all()
    cities = Idea.published.values_list('city', flat=True).distinct()
    return object_list(request,
                       queryset=recent,
                       template_name='portfolio/explore.html',
                       extra_context={'featured': featured,
                                      'categories': categories,
                                      'cities': cities })
                                      
def ideas_featured(request):
    featured = Idea.published.filter(featured=True)
    categories = Category.objects.all()
    cities = Idea.published.values_list('city', flat=True).distinct()
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
    cities = Precedent.published.values_list('city', flat=True).distinct()
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
    cities = Idea.published.values_list('city', flat=True).distinct()
    return object_list(request,
                         queryset=precedents,
                         template_name='portfolio/precedent_by_category.html',
                         extra_context={'categories': categories,
                                        'cities': cities,
                                        'category': category,
                                        })

                         
                         
def category_index(request):
    categories = Category.objects.all()
    cities = Idea.published.values_list('city', flat=True).distinct()
    return object_list(request,
                       queryset=categories,
                       template_object_name = 'category',
                       template_name='portfolio/category_list.html',
                       extra_context={'cities': cities, })


def ideas_by_category(request, cat):
    category = Category.objects.get(slug__iexact=cat)
    categories = Category.objects.all()
    ideas = Idea.published.filter(categories__slug=cat)
    cities = Idea.published.values_list('city', flat=True).distinct()
    return object_list(request,
                         queryset=ideas,
                         template_name='portfolio/ideas_by_category.html',
                         extra_context={'ideas': ideas,
                                        'categories': categories,
                                        'cities': cities,
                                        'category': category,
                                        })
                                        
def ideas_by_city(request, city_name):
    ideas = Idea.published.filter(city__iexact=city_name)
    categories = Category.objects.all()
    cities = Idea.published.values_list('city', flat=True).distinct()
    return object_list(request,
                       queryset=ideas,
                       template_name='portfolio/ideas_by_city.html',
                       extra_context={'categories': categories,
                                      'cities': cities,
                                      'current_city': city_name })
                                        
                                        
def ideas_by_tag(request, tag):
    categories = Category.objects.all()
    cities = Idea.published.values_list('city').distinct()
    return tagged_object_list(tag, 
                              queryset_or_model=Idea,
                              template_name='portfolio/ideas_by_tag.html',
                              extra_context={'categories': categories,
                                             'cities': cities,})
                                             
@login_required                                             
def idea_add(request):
    if request.method == 'POST':
        form = IdeaForm(data=request.POST)
        if form.is_valid():
            new_idea = form.save(commit=False)
            new_idea.user = request.user
            title = form.cleaned_data['title']
            slugified_title = str(slugify(title))
            new_idea.slug = slugified_title
            new_idea.featured = False
            new_idea.enable_comments = True
            new_idea.moderate_comments = False
            new_idea.status = Idea.STATUS_PENDING
            new_idea.save()
            form.save_m2m()
            return HttpResponseRedirect(reverse('profiles_profile_detail', args=[request.user]))
    else:
        form = IdeaForm()
    context = {'form': form, 'add': True}
    return render_to_response('portfolio/idea_form.html', 
                              context, 
                              context_instance=RequestContext(request))
    

@login_required
def idea_edit(request, idea_id):
    idea = get_object_or_404(Idea, pk=idea_id)
    if request.user.id != idea.user.id:
        return HttpResponseForbidden()
    if request.method == 'POST':
        form = IdeaForm(instance=idea, data=request.POST)
        if form.is_valid():
            idea = form.save()
            if idea.status == idea.STATUS_PUBLISHED:
                return HttpResponseRedirect(idea.get_absolute_url())
            else:
                return HttpResponseRedirect(reverse('profiles_profile_detail', args=[request.user]))
        else: 
            form = IdeaForm(instance=idea)
        context = {'form': form, 'add': False}
        return render_to_response('portfolio/idea_form.html',
                                   context, 
                                   context_instance=RequestContext(request))
                                             