# portfolio/urls.py

from django.conf.urls.defaults import *
from tagging.views import tagged_object_list

from actionmanual.portfolio.models import *

urlpatterns = patterns('actionmanual.actionmanual.portfolio.views',

    # explore index
    url(r'^$', 'explore_index', name="explore"),
    
     # user input of ideas
    url(r'^ideas/add/$', 'idea_add', name='idea-add'),
    url(r'^ideas/edit/(?P<idea_id>\d+)/$', 'idea_edit', name='idea-edit'),
    
    url(r'^ideas/$', 'idea_list', name="idea-list" ),
    url(r'^ideas/(?P<slug>[-\w]+)/$', 'idea_detail', name="idea-detail" ),
     
           
    url(r'^precedents/$', 'precedent_list', name="precedent-list" ),
    url(r'^precedents/(?P<slug>[-\w]+)/$', 'precedent_detail', name="precedent-detail" ),
    
    # precedents by category
    url(r'^precedents/categories/(?P<cat>[-\w]+)/$', 'precedent_by_category', name="precedent-by-category"),


    # ideas by category
    url(r'^ideas/categories/(?P<cat>[-\w]+)/$', 'ideas_by_category', name="ideas-by-category"), 
    
    # ideas by city
    url(r'^ideas/cities/(?P<city_name>[-\w]+)/$', 'ideas_by_city', name="ideas-by-city"), 
    
    # ideas by tag
    url(r'^tags/(?P<tag>[^/]+)/$', tagged_object_list,
           dict(queryset_or_model=Idea),
           name='ideas-by-tag'),
           
)
