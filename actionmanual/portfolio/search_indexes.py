import datetime
from haystack.indexes import *
from haystack import site
from actionmanual.portfolio.models import Idea, Precedent

class IdeaIndex(SearchIndex):
     text = CharField(document=True, use_template=True)
     
     def get_queryset(self):
        """Used when the entire index for model is updated."""
        return Idea.objects.filter(status=Idea.LIVE_STATUS)
        
class PrecedentIndex(SearchIndex):
     text = CharField(document=True, use_template=True)
     
     def get_queryset(self):
        """Used when the entire index for model is updated."""
        return Idea.objects.filter(status=Precedent.LIVE_STATUS)
        
site.register(Idea, IdeaIndex)
site.register(Precedent, PrecedentIndex)
