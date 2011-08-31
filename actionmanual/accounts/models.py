# accounts/models.py

from django.db import models
from django.db.models import signals
from django.db.models import permalink
from django.contrib.auth.models import User

from tagging.fields import TagField

from actionmanual.fields import CountryField

from actionmanual.accounts.signals import create_profile

class UserProfile(models.Model):
    """

	A user profile for the website

    """
    bio = models.TextField()
    user = models.ForeignKey(User, unique=True)
    birth_date = models.DateField(blank=True, null=True)
    address_line1 = models.CharField(max_length=250, blank=True)
    address_line2 = models.CharField(max_length=250, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField('state/province', max_length=100, blank=True)
    code = models.CharField(max_length=20, blank=True, help_text="Zip or Postal Code")
    country = CountryField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    mobile = models.CharField(max_length=50, blank=True)
    fax = models.CharField(max_length=50, blank=True)
    website = models.URLField(blank=True, verify_exists=True)
    
    tags = TagField(help_text="Separate tags with spaces.")
    
    # When model instance is saved, trigger creation of corresponding profile
    signals.post_save.connect(create_profile, sender=User)
    
    @property
    def full_name(self):
        return u'%s %s' % (self.user.first_name, self.user.last_name)
        
    def __unicode__(self):
        if self.user.first_name:
            return u'%s' % self.full_name
        else:
            return u'%s' % self.user.username

    @permalink
    def get_absolute_url(self):
        return ('profiles_profile_detail', (), { 'username':
                 self.user.username })
