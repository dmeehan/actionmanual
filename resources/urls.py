# resources/urls.py

from django.conf.urls.defaults import *

from actionmanual.portfolio.models import Idea

urlpatterns = patterns('actionmanual.resources.views',
    url(r'^$', 'resources_index', name="resources" ),
    url(r'^people/(?P<slug>[-\w]+)/$', 'resources_person_detail', name="resources-person-detail" ),
    url(r'^organizations/(?P<slug>[-\w]+)/$', 'resources_org_detail', name="resources-org-detail" ),
    url(r'^blog/(?P<slug>[-\w]+)/$', 'resources_post_detail', name="resources-post-detail" ),
    url(r'^links/(?P<slug>[-\w]+)/$', 'resources_link_detail', name="resources-link-detail" ),
    
    url(r'^people/$', 'resources_person_list', name="resources-person-list" ),
    url(r'^organizations/$', 'resources_org_list', name="resources-org-list" ),
    url(r'^blog/$', 'resources_post_list', name="resources-post-list" ),
    url(r'^links/$', 'resources_link_list', name="resources-link-list" ),
    
    
    #url(r'^(?P<type>[-\w]+)/$', 'resources_type', name="resources-type" ),
    #url(r'^(?P<type>[-\w]+)/(?P<slug>[-\w]+)/$', 'resource_detail', name="resource-detail" ),
    
    #url(r'^cities/$', 'resources_cities_list', name="resource-cities-list" ),
    #url(r'^cities/(?P<city>[-\w]+)/$', 'resources_city', name="resources-city" ),
    
    #url(r'^categories/$', 'resource_categories_list', name="resource-categories-list" ),
    url(r'^categories/(?P<slug>[-\w]+)/$', 'resources_by_category', name="resources-by-category" ),
    url(r'^categories/(?P<slug>[-\w]+)/essays/$', 'resources_post_by_category', name="resources-post-by-category" ),
    url(r'^categories/(?P<slug>[-\w]+)/links/$', 'resources_link_by_category', name="resources-link-by-category" ),
    url(r'^categories/(?P<slug>[-\w]+)/organizations/$', 'resources_org_by_category', name="resources-org-by-category" ),
    url(r'^categories/(?P<slug>[-\w]+)/people/$', 'resources_person_by_category', name="resources-person-by-category" ),
)
