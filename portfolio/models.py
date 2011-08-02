""" 

    portfolio/models.py
    
    This app handles urban design projects and precedents
    
"""


# Python modules
import datetime

# Django modules
from django.conf import settings
from django.db import models
from django.db.models import permalink
from django.utils.encoding import smart_str
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.contrib.comments.models import Comment
from django.contrib.comments.signals import comment_will_be_posted
from django.contrib.comments.moderation import CommentModerator, moderator
from django.contrib.sites.models import Site
from django.contrib.localflavor.us.models import USStateField


# Third party Django app modules
from tagging.fields import TagField
from tagging.models import Tag, TaggedItem
from imagekit.models import ImageModel

# Local modules
from actionmanual.fields import PositionField
from actionmanual.locations.fields import LocationField
from actionmanual.contacts.models import Person, Organization
from actionmanual.sections.models import SectionItem
from actionmanual.categories.models import Category, CategoryItem
from actionmanual.posts.models import Article, Link
from actionmanual.portfolio.managers import *

# Models
class License(models.Model):
    """
    
        Model for storing copyright types 
    
    """
    
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, 
                             help_text="A short description of the license parameters. Optional.")
    url = models.URLField(blank=True, verify_exists=True)
    
    slug = models.SlugField(unique=True, help_text="Suggested value automatically generated from name. Must be unique.")

class Designer(models.Model):
    designer = models.ForeignKey(Person, blank=True, null=True, help_text="The person or persons who created the project.")
    blurb = models.TextField(blank=True, 
                             help_text="A short description of the designer in relation to this project. Optional.")
    blurb_html = models.TextField(blank=True, editable=False)
    
    # Allow generic relations
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type','object_id')
    
    def __unicode__(self):
        name = self.designer.__unicode__()
        return name
           
class Firm(models.Model):
    firm = models.ForeignKey(Organization, blank=True, null=True, help_text="The firm who created the project.")
    blurb = models.TextField(blank=True, 
                             help_text="A short description of the firm in relation to this project. Optional.")
    blurb_html = models.TextField(blank=True, editable=False)
    
    # Allow generic relations
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type','object_id')
    
    def __unicode__(self):
        name = self.firm.__unicode__()
        return name

        
class Project(models.Model):
    """
       
       An abstract model that defines a design project.
       
    """
    #default Model Manager
    objects = models.Manager()
    
    # custom Model Managers
    published = PublishedProjectManager()
    featured = FeaturedProjectManager()
    
    
    
    STATUS_PENDING = 1
    STATUS_PUBLISHED = 2
    STATUS_REJECTED = 3
    STATUS_HIDDEN = 4
    STATUS_CHOICES = (
        (STATUS_PENDING, 'Pending'),
        (STATUS_PUBLISHED, 'Published'),
        (STATUS_REJECTED, 'Rejected'),
        (STATUS_HIDDEN, 'Hidden'),
    )
        
    # Project author manages these fields
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, help_text="Suggested value automatically generated from title. Must be unique.")
    tagline = models.CharField(max_length=500, help_text="A sentence summary of the project.")
    description = models.TextField(help_text='Use <a href="http://daringfireball.net/projects/markdown/basics">markdown</a> to format text. e.g. *italic*, **bold**, ###header, * unordered list item, 1. ordered list item' )
    location = LocationField(blank=True, max_length=255)
    location_name = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100)
    state = USStateField(blank=True)
    zip_code = models.IntegerField(max_length=5, blank=True, null=True)
    website = models.URLField(blank=True)
    copyright = models.ForeignKey(License, blank=True, null=True)
    images = generic.GenericRelation('Image')
    
    description_html = models.TextField(blank=True,editable=False)
    
    # Categorization.
    categories = models.ManyToManyField(Category)
    tags = TagField(help_text="Separate tags with spaces")
    
    #Designers
    firms = generic.GenericRelation(Firm)
    designers = generic.GenericRelation(Designer)
            
    # Site admin manages these fields
    user = models.ForeignKey(User, help_text="The owner of the project.")
    status = models.IntegerField(choices=STATUS_CHOICES, default=STATUS_PENDING, 
                                 help_text="Only projects with published status will be publicly displayed.")
    enable_comments = models.BooleanField(default=True)
    moderate_comments = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
        
    # autogenerated fields
    date_added = models.DateField(auto_now_add=True, editable=False)
    date_modified = models.DateField(auto_now=True, editable=False)
    date_published = models.DateField(editable=False, blank=True, null=True)
 
    class Meta:
        abstract=True
        get_latest_by = 'date_published'
        ordering = ['-date_published']
    
    @property
    def class_name(self):
        return u'%s' % self.title
        
    def save(self, force_insert=False, force_update=False):
        if self.status == 2:
            if not self.date_published:
                self.date_published = datetime.datetime.now()
        else:
            if self.date_published:
                self.date_published = None
                
        if settings.PORTFOLIO_MARKUP == 'markdown':
            from markdown import markdown
            self.description_html = markdown(self.description)
        elif settings.PORTFOLIO_MARKUP == 'wysiwyg':
            self.description_html = self.description
        
        super(Project, self).save(force_insert, force_update)
        
    def __unicode__(self):
        return u'%s' % (self.title)
        
    def related_projects(self, num=4):
        '''Instances of this model that have a tag in common'''
        return TaggedItem.objects.get_related(self, self.__class__, num=num)
        
    def related_projects_exact(self, num=None):
        '''Exact matches'''
        return TaggedItem.objects.get_intersection_by_model(
            self.__class__.objects.exclude(slug=self.slug),
            self.tags
        )

    def projects_common_tag(self):
        '''Same as related_projects but with a different method'''
        return TaggedItem.objects.get_union_by_model(
            self.__class__.objects.exclude(slug=self.slug),
            self.tags
        )
        
            
class Precedent(Project):
    """
        
        A built project that serves as an example
        
    """
    @permalink
    def get_absolute_url(self):
        return ('precedent-detail', [str(self.slug)])
 
    
class Idea(Project):
    """
    
        An unbuilt project which serves as an idea generator

    """
    @permalink
    def get_absolute_url(self):
        return ('idea-detail', [str(self.slug)])
        
        
class FeaturedCategoryIdea(models.Model):
    idea = models.ForeignKey(Idea)
    category = models.ForeignKey(Category)
    
    order = PositionField(unique_for_field='category')
    
    def __unicode__(self):
        name = self.idea.__unicode__()
        return name
  
    
class PrecedentIdeaRelation(models.Model):
    idea = models.ForeignKey(Idea)
    precedent = models.ForeignKey(Precedent)
    
    def __unicode__(self):
        name = self.idea.__unicode__()
        return name

class Resource(models.Model):
    FILE_MODELS = {'model__in':('article', 'link', 'organization', 'person')}
    content_type = models.ForeignKey(ContentType, limit_choices_to=FILE_MODELS,
                                     help_text="An article, link, organization, or person related to this idea.")
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    idea = models.ForeignKey(Idea)
    
    
class File(models.Model):
    """
    
        Abstract model for files associated with a project
                
    """
    # Core file fields.
    user = models.ForeignKey(User, blank=True, null=True, help_text="The person who is uploading the file.")
    title = models.CharField(max_length=255)
    caption = models.CharField(max_length=255)
    author = models.ForeignKey(Person, blank=True, null=True, help_text="The person who created the content of the file.")
    
    # Metadata.
    public = models.BooleanField(default=True, help_text="This file is publicly available.")
    lead = models.BooleanField(default=False, help_text="This file is the projects lead file")
    order = PositionField()
    copyright = models.ForeignKey(License, blank=True, null=True, help_text="Copyright details.")
    slug = models.SlugField(unique=True, help_text="Suggested value automatically generated from title. Must be unique.")
    
    # non-editable metadata.
    creation_date = models.DateTimeField(auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(auto_now=True, editable=False)
    
    # Allow generic relations
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type','object_id')
        
    class Meta:
        ordering = ['order']
        abstract = True
        
    def __unicode__(self):
        return '%s' % self.title
        
    #def save(self, *args, **kwargs):
        #if self.lead:
            #related_files = self._default_manager.filter(content_object=self.content_object)
            #related_files.update(lead=False)
                
        #return super(File, self).save(*args, **kwargs) 
        
        
class Image(ImageModel, File):
    """
    
        An image file, such as a photograph or other rasterized image.
        Inherits from two abstract classes: File and imageKit.ImageModel.
        File defines fields and imageKit provides processing methods.
    
    """
    
    LEFT = 0
    CENTER = 1
    RIGHT = 2
    CROPHORIZ_CHOICES = (
        (LEFT, 'LEFT'),
        (CENTER, 'CENTER'),
        (RIGHT, 'RIGHT'),
    )
    
    TOP = 0
    CENTER = 1
    BOTTOM = 2
    CROPVERT_CHOICES = (
        (TOP, 'TOP'),
        (CENTER, 'CENTER'),
        (BOTTOM, 'BOTTOM'),
    )
    
    # Core image fields.
    image = models.ImageField(upload_to='images')
    crop_horiz = models.IntegerField(verbose_name='horizontal cropping', 
                                     choices=CROPHORIZ_CHOICES, 
                                     blank=True,
                                     default=CENTER,
                                     help_text="From where to horizontally crop the image, if cropping is necessary.")
    crop_vert = models.IntegerField(verbose_name='vertical cropping', 
                                    choices=CROPVERT_CHOICES, 
                                    blank=True,
                                    default=CENTER,
                                    help_text="From were to vertically crop the image, if cropping is necessary.")
    
    class Meta:
        ordering = ['order']
    

    # This inner class is where we define the options for ImageKit processing
    class IKOptions:
        spec_module = 'actionmanual.portfolio.imagespecs'
        image_field = 'image'
        cache_filename_format = "%(specname)s/%(filename)s.%(extension)s"
        
        
class Video(File):
    """
    
        A file with moving images such as .mov .m4p, .wmv, etc.
        
    """
    
    # Core Video fields.
    video = models.FileField(upload_to='videos')
    poster = models.ImageField(upload_to='videos/posters')
    
    @permalink
    def get_absolute_url(self):
        pass
        
class Flash(File):
    """
    
        A Flash animation.
        
    """
    
    # Core Video fields.
    swf = models.FileField(upload_to='swfs')
    poster = models.ImageField(upload_to='swfs/posters')
    
    class Meta:
        verbose_name_plural = 'Flash Animations'
            
    @permalink
    def get_absolute_url(self):
        pass 



class Audio(File):
    # Core Audio fields.
    audio = models.FileField(upload_to='audio')
    poster = models.ImageField(upload_to='audio/posters')
    
    class Meta:
        verbose_name_plural = "Audio"
        db_table = 'portfolio_audio'
        
    @permalink
    def get_absolute_url(self):
        pass 
    
class Document(File):
    # Core document fields.
    document = models.FileField(upload_to='docs')
    
    @permalink
    def get_absolute_url(self):
        pass 
            
class ProjectModerator(CommentModerator):
    enable_field = 'enable_comments'
    auto_moderate_field = 'date_published'
    auto_close_field = 'date_published'
    moderate_after = settings.COMMENTS_MODERATE_AFTER
    close_after = settings.COMMENTS_CLOSE_AFTER
    email_notification = True
    
    def check_spam(self, request, comment, key, blog_url=None, base_url=None):
        try:
            from akismet import Akismet
        except:
            return False

        if blog_url is None:
            blog_url = 'http://%s/' % Site.objects.get_current().domain

        ak = Akismet(
            key=settings.COMMENTS_AKISMET_API_KEY,
            blog_url=blog_url
        )

        if base_url is not None:
            ak.baseurl = base_url

        if ak.verify_key():
            data = {
                'user_ip': request.META.get('REMOTE_ADDR', '127.0.0.1'),
                'user_agent': request.META.get('HTTP_USER_AGENT', ''),
                'referrer': request.META.get('HTTP_REFERER', ''),
                'comment_type': 'comment',
                'comment_author': comment.user_name.encode('utf-8'),
            }

            if ak.comment_check(comment.comment.encode('utf-8'), data=data, build_data=True):
                return True

        return False

    def allow(self, comment, content_object, request):
        allow = super(ProjectModerator, self).allow(comment, content_object, request)

        # change this depending on which spam provider you want to use
        spam = self.check_spam(request, comment,
            key=settings.COMMENTS_AKISMET_API_KEY,
        )

        return not spam and allow

moderator.register(Project, ProjectModerator)


