# contacts/models.py

from django.db import models
from django.db.models import permalink
from django.contrib.contenttypes import generic

from tagging.fields import TagField

from actionmanual.fields import CountryField
from actionmanual.categories.models import Category, CategoryItem

class Contact(models.Model):
    """
    
    Abstract contact model. Includes fields shared
    between all contact types.
        
    """
    description = models.TextField(blank=True, null=True)
    address_line1 = models.CharField(max_length=250, blank=True)
    address_line2 = models.CharField(max_length=250, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField('state/province', max_length=100, blank=True)
    code = models.CharField(max_length=20, blank=True, help_text="Zip or Postal Code")
    country = CountryField(blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    fax = models.CharField(max_length=50, blank=True)
    website = models.URLField(blank=True, verify_exists=True)
    
    tags = TagField(help_text="Separate tags with spaces.")
    
    slug = models.SlugField(unique=True, help_text="Unique web title automatically generated from name.")
    
    def __unicode__(self):
        return u'%s' % self.slug
        
    class Meta:
        abstract = True
        
        
class Organization(Contact):
    """
    
    A contact that is a company, school, government body, etc.
    Inherits from Contact.
    
    """
    
    COMPANY = 1
    SCHOOL = 2
    NONPROFIT = 3
    GOVERNMENT = 4
    ORG_CHOICES = (
        (COMPANY, 'Company'),
        (SCHOOL, 'School'),
        (NONPROFIT, 'Non-Profit'),
        (GOVERNMENT, 'Government'),
    )

    name = models.CharField(max_length=100)
    org_type = models.PositiveSmallIntegerField(choices=ORG_CHOICES)
            
    def __unicode__(self):
        return u'%s' % self.name
        
    @permalink
    def get_absolute_url(self):
        return ('org-detail', [str(self.slug)])
        
        
class Person(Contact):
    """
    
    A contact that is a person. Inherits from Contact.
    
    """
    GENDER_CHOICES = (
        (1, 'Male'),
        (2, 'Female'),
    )
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100)
    gender = models.IntegerField(choices=GENDER_CHOICES, blank=True)
    birth_date = models.DateField(blank=True, null=True)
    mobile = models.CharField(max_length=50, blank=True)


    class Meta:
        verbose_name = "person"
        verbose_name_plural = "people"
        db_table = "contacts_people"

    @property
    def full_name(self):
        return u'%s %s' % (self.first_name, self.last_name)
        
    def __unicode__(self):
        return u'%s' % self.full_name
        
    @permalink
    def get_absolute_url(self):
        return ('org-detail', [str(self.slug)])
