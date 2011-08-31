from django.conf.urls.defaults import *
from django.contrib import admin

from tagging.models import Tag
admin.autodiscover()


urlpatterns = patterns('',
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    # django-grapelli custom admin interface
    (r'^grappelli/', include('grappelli.urls')),
    
    # admin-tools
    url(r'^admin_tools/', include('admin_tools.urls')),
    
    # tinymce admin extension
    #(r'^tinymce/', include('tinymce.urls')),
    
    # registration
    (r'^accounts/', include('registration.backends.default.urls')),
    
    # Profiles
    (r'^profiles/', include('profiles.urls')),
    
    #Comment
    (r'^flatblocks/', include('flatblocks.urls')),
    
    #Search
    (r'^search/', include('haystack.urls')),
    
    # home page
    url(r'^$', 'actionmanual.actionmanual.home.views.index', name="home"),

    #Comment
    (r'^comments/', include('django.contrib.comments.urls')),
    
    # Portfolio:
    (r'^share/', include('actionmanual.actionmanual.portfolio.urls.share')),
    (r'^explore/', include('actionmanual.actionmanual.portfolio.urls.explore')),
    
    # Resources:
    (r'^resources/', include('actionmanual.resources.urls')),

    # About:
    url(r'^about/', 'actionmanual.actionmanual.about.views.about_index', name="about"),
    
    # Contacts:
    (r'^contacts/', include('actionmanual.actionmanual.contacts.urls')),
    
    # Posts:
    (r'^posts/', include('actionmanual.actionmanual.posts.urls')),
    
     #Tags:
    (r'^tags/$',
      'django.views.generic.list_detail.object_list',
      { 'queryset': Tag.objects.all() }),
 
)
