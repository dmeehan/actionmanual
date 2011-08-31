# resources/models.py

from django.db import models
from django.db.models import permalink
from django.contrib.contenttypes.generic import GenericRelation


from actionmanual.posts.models import Article, Link
from actionmanual.portfolio.models import Idea, Precedent
from actionmanual.contacts.models import Organization, Person

from actionmanual.categories.models import CategoryItem, Category

class LiveManager(models.Manager):
    def get_query_set(self):
        return super(LiveManager, self).get_query_set().filter(status=self.model.LIVE_STATUS)

class Essay(Article):
    """
    
    Extension of the Article model specifically for resource information about project ideas
        
    """
    #standard Model Manager
    objects = models.Manager()
    
    # custom Model Manager 
    live = LiveManager()
    
    ideas = models.ManyToManyField(Idea, blank=True, null=True)
    precedents = models.ManyToManyField(Precedent, blank=True, null=True)
    
    categories = GenericRelation(CategoryItem)
    
    class Meta:
        verbose_name = "blog"
        verbose_name_plural = "blog"

    
    @permalink
    def get_absolute_url(self):
        return ('resources-post-detail', [str(self.slug)])


   
class Web(Link):
    """
    
    Extension of the Link model specifically for resource information about project ideas.
    
    """
    #standard Model Manager
    objects = models.Manager()
    
    # custom Model Manager 
    live = LiveManager()
    
    ideas = models.ManyToManyField(Idea, blank=True, null=True)
    precedents = models.ManyToManyField(Precedent, blank=True, null=True)
    
    categories = GenericRelation(CategoryItem)
    
    class Meta:
        verbose_name = "Web Link"
        
    @permalink
    def get_absolute_url(self):
        return ('resources-link-detail', [str(self.slug)])

    
    
class ResourceOrganization(Organization):
    """
    
       Pairs an organization with an idea.
        
    """
    ideas = models.ManyToManyField(Idea, blank=True, null=True)
    precedents = models.ManyToManyField(Precedent, blank=True, null=True)
    
    categories = GenericRelation(CategoryItem)
    
    class Meta:
        verbose_name = "Organization"
        
    @permalink
    def get_absolute_url(self):
        return ('resources-org-detail', [str(self.slug)])
        
class ResourcePerson(Person):
    """
    
       Pairs a person with an idea.
        
    """
    ideas = models.ManyToManyField(Idea, blank=True, null=True)
    precedents = models.ManyToManyField(Precedent, blank=True, null=True)
    
    categories = GenericRelation(CategoryItem)
    
    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "People"
        
    @permalink
    def get_absolute_url(self):
        return ('resources-person-detail', [str(self.slug)])
