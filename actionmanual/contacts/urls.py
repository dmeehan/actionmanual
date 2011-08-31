# contacts/urls.py

from django.conf.urls.defaults import *
from tagging.views import tagged_object_list

from actionmanual.contacts.models import *

urlpatterns = patterns('actionmanual.actionmanual.contacts.views',
    url(r'^people/(?P<slug>[-\w]+)/$', 'person_detail', name="person-detail" ),
    url(r'^organizations/(?P<slug>[-\w]+)/$', 'org_detail', name="org-detail" ),
)