from django.conf.urls.defaults import *
from django.contrib import admin

from tagging.models import Tag
admin.autodiscover()


urlpatterns = patterns('',
    # home page
    url(r'^$', 'actionmanual.home.views.index', name="home"),

    # Portfolio:
    (r'^share/', include('actionmanual.portfolio.urls.share')),
    (r'^explore/', include('actionmanual.portfolio.urls.explore')),

    # Resources:
    (r'^resources/', include('actionmanual.resources.urls')),

    # About:
    url(r'^about/', 'actionmanual.about.views.about_index', name="about"),

    # Contacts:
    (r'^contacts/', include('actionmanual.contacts.urls')),

    # Posts:
    (r'^posts/', include('actionmanual.posts.urls')),

)
