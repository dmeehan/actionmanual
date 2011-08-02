# portfolio/views/share.py

from markdown import markdown

from django.http import HttpResponseRedirect
from django.http import HttpResponseForbidden
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify
from django.template import RequestContext
from django.contrib.contenttypes.generic import generic_inlineformset_factory
from django.views.generic.simple import direct_to_template

from actionmanual.portfolio.models import *

from actionmanual.portfolio.forms import *
                                           
def share_index(request):
    recent = Idea.published.order_by('-date_published')[:3]
    return direct_to_template(request, 
	                          template='portfolio/share_index.html',
	                          extra_context={'recent': recent} )

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
            return HttpResponseRedirect(reverse('portfolio-image-add', args=[new_idea.id]))
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
            idea.status = Idea.STATUS_PENDING
            idea = form.save()
            if idea.status == idea.STATUS_PUBLISHED:
                return HttpResponseRedirect(idea.get_absolute_url())
            else:
                return HttpResponseRedirect(reverse('profiles_profile_detail', args=[request.user]))
    else: 
        form = IdeaForm(instance=idea)
    context = {'idea': idea, 'form': form, 'add': False}
    return render_to_response('portfolio/idea_form.html',
                               context, 
                               context_instance=RequestContext(request))
                                             
@login_required
def image_add(request, idea_id):
    idea = get_object_or_404(Idea, pk=idea_id)
    if request.user.id != idea.user.id:
        return HttpResponseForbidden()
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            new_image = form.save(commit=False)
            new_image.user = request.user
            title = form.cleaned_data['title']
            slugified_title = str(slugify(title))
            new_image.slug = slugified_title
            new_image.public = True
            new_image.content_type_id = 29
            new_image.object_id = idea.id
            new_image.save()
            form.save()
            if '_save' in request.POST:
                return HttpResponseRedirect(reverse('profiles_profile_detail', 
                                        args=[request.user]))
            elif '_addanother' in request.POST:
                return HttpResponseRedirect(reverse('portfolio-image-add', 
                                                     args=[idea.id]))
    else:
        form = ImageForm()
    context = {'idea': idea, 'form': form, 'add': True}
    return render_to_response('portfolio/image_form.html',
                               context,
                               context_instance=RequestContext(request))

@login_required
def image_edit(request, idea_id, image_id):
    idea = get_object_or_404(Idea, pk=idea_id)
    image = get_object_or_404(Image, pk=image_id)
    if request.user.id != idea.user.id:
        return HttpResponseForbidden()
    if request.method == 'POST':
        form = ImageForm(instance=image, data=request.POST, files=request.FILES)
        if form.is_valid():
            image = form.save()
            if '_save' in request.POST:
                return HttpResponseRedirect(reverse('profiles_profile_detail', 
                                                     args=[request.user]))
            elif '_edit' in request.POST:
                return HttpResponseRedirect(reverse('idea-edit', 
                                                     args=[idea.id]))
    else: 
        form = ImageForm(instance=image)
    context = {'idea': idea, 'form': form, 'add': False}
    return render_to_response('portfolio/image_form.html',
                               context, 
                               context_instance=RequestContext(request))

