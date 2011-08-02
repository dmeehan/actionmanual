# posts/urls.py

from django.conf.urls.defaults import *

from actionmanual.posts.models import *

urlpatterns = patterns('actionmanual.posts.views',
    url(r'^articles/(?P<slug>[-\w]+)/$', 'article_detail', name="article-detail" ),
    url(r'^links/(?P<slug>[-\w]+)/$', 'link_detail', name="link-detail" ),
)