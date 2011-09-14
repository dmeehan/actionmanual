# categories/urls.py

from django.conf.urls.defaults import *
from actionmanual.categories.models import *
from actionmanual.portfolio.models import Idea, Precedent

urlpatterns = patterns('actionmanual.categories.views',

    # explore by category
    url(r'^$', 'category_index', name="explore"),

    # category detail
    url(r'^(?P<slug>[-\w]+)/$', 'category_detail', name="category-detail"),
    
)
