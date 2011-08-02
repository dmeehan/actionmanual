# categories/models.py

"""

    Categorizes and groups items on a website
    
"""

from django.db import models
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType

from imagekit.models import ImageModel

from actionmanual.fields import PositionField

class CategoryGroup(models.Model):
    """
    
    A group of categories that fit under a certain type
    
    """
    name = models.CharField(max_length=250, help_text="Maximum 250 characters.")
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True, help_text="Suggested value automatically generated from name. Must be unique.")

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        pass


class Category(ImageModel):
    """
    
    A category that a content object can belong to. Extends ImageModel to get image processing functionality
        
    """
    name = models.CharField(max_length=250, help_text="Maximum 250 characters.") 
    slug = models.SlugField(unique=True, help_text="Suggested value automatically generated from name. Must be unique.")
    description = models.TextField(blank=True, help_text="A description of the category")
    icon = models.ImageField(upload_to='categories/icons', blank=True, null=True)
    
    group = models.ForeignKey(CategoryGroup)
    order = PositionField(unique_for_field='group')
    
    # This inner class is where we define the options for ImageKit processing
    class IKOptions:
        spec_module = 'actionmanual.categories.imagespecs'
        image_field = 'icon'
        cache_filename_format = "%(specname)s/%(filename)s.%(extension)s"
        
    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['-group', 'order',]

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        pass
   
    
class CategoryItem(models.Model):
    """
    
        The relationship between a category and an arbitrary object
        
    """
    category = models.ForeignKey(Category)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    name = models.CharField(max_length=250, editable=False, null=True) 
    
    
    def __unicode__(self):
        return self.name     
         
    def save(self, *args, **kwargs):
        self.name = self.content_object.__unicode__()
        return super(CategoryItem, self).save(*args, **kwargs)
    
    class Meta:
         ordering = ['content_type']
         verbose_name = "category relation"
    
    
        

