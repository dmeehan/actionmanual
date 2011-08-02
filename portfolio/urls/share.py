# portfolio/urls/share.py

from django.conf.urls.defaults import *
from tagging.views import tagged_object_list

from actionmanual.portfolio.models import *

urlpatterns = patterns('actionmanual.portfolio.views.share',

    # share index
    url(r'^$', 'share_index', name="share"),
	
	# user input of ideas
    url(r'^ideas/add/$', 'idea_add', name='idea-add'),
    url(r'^ideas/edit/(?P<idea_id>\d+)/$', 'idea_edit', name='idea-edit'),

    url(r'^ideas/add/(?P<idea_id>\d+)/image/add/$', 'image_add', name='portfolio-image-add'),
    url(r'^ideas/add/(?P<idea_id>\d+)/images/edit/(?P<image_id>\d+)/$', 'image_edit', name='portfolio-image-edit'),
    
)
