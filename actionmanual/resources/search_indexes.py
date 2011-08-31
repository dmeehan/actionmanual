import datetime
from haystack.indexes import *
from haystack import site
from actionmanual.resources.models import *

class WebIndex(SearchIndex):
     text = CharField(document=True, use_template=True)
     
     def get_queryset(self):
        """Used when the entire index for model is updated."""
        return Web.objects.filter(status=Web.LIVE_STATUS)
        
class EssayIndex(SearchIndex):
     text = CharField(document=True, use_template=True)
     
     def get_queryset(self):
        """Used when the entire index for model is updated."""
        return Essay.objects.filter(status=Essay.LIVE_STATUS)
        
class OrgIndex(SearchIndex):
     text = CharField(document=True, use_template=True)
     
     def get_queryset(self):
        """Used when the entire index for model is updated."""
        return ResourceOrganization.objects.all()
        
class PersonIndex(SearchIndex):
     text = CharField(document=True, use_template=True)
     
     def get_queryset(self):
        """Used when the entire index for model is updated."""
        return ResourcePerson.objects.all()
        
        
site.register(Web, WebIndex)
site.register(Essay, EssayIndex)
site.register(ResourceOrganization, OrgIndex)
site.register(ResourcePerson, PersonIndex)