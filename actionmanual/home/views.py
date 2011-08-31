# home/views.py

from django.views.generic.list_detail import object_list, object_detail

from tagging.models import Tag, TaggedItem

from actionmanual.portfolio.models import *
from actionmanual.posts.models import *
from actionmanual.contacts.models import *
from actionmanual.sections.models import *
from actionmanual.resources.models import *

def index(request):
    latest_links = Web.live.order_by('-pub_date')[:5]
    latest_articles = Essay.live.all()[:1]
    latest_orgs = ResourceOrganization.objects.all()[:5]
    latest_people = ResourcePerson.objects.all()[:5]
    ideas = Idea.published.filter(featured=True).order_by('title')
    latest_ideas = Idea.published.all().order_by('-date_published')[:1]
    precedents = Precedent.published.filter(featured=True).order_by('title')
    articles = SectionItem.objects.filter(section__name="Home")\
               .filter(content_type__name="article")
    about = SectionItem.objects.filter(section__name="About")\
               .filter(content_type__name="article")
    return object_list(request,
                       queryset=ideas,
                       template_name='home/index.html',
                       extra_context={'precedents': precedents,
                                      'articles': articles,
                                      'about': about,
                                      'latest_orgs': latest_orgs,
                                      'latest_links': latest_links,
									  'latest_ideas': latest_ideas,
                                      'latest_articles': latest_articles, })
