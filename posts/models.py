# posts/models.py

import datetime

from markdown import markdown

from django.conf import settings
from django.db import models
from django.db.models import permalink
from django.contrib.auth.models import User
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.contrib.comments.models import Comment
from django.contrib.comments.signals import comment_will_be_posted
from django.contrib.comments.moderation import CommentModerator, moderator
from django.contrib.sites.models import Site
from django.utils.encoding import smart_str

from imagekit.models import ImageModel
from tagging.fields import TagField

from actionmanual.fields import PositionField
from actionmanual.contacts.models import Person

class LiveManager(models.Manager):
    def get_query_set(self):
        return super(LiveManager, self).get_query_set().filter(status=self.model.LIVE_STATUS)
        
class Article(models.Model):
    """
    
        A story or entry on a website.
    
    """
    #standard Model Manager
    objects = models.Manager()
    
    # custom Model Manager 
    live = LiveManager()

    LIVE_STATUS = 1
    DRAFT_STATUS = 2
    HIDDEN_STATUS = 3
    STATUS_CHOICES = (
        (LIVE_STATUS, 'Live'),
        (DRAFT_STATUS, 'Draft'),
        (HIDDEN_STATUS, 'Hidden'),
    )
    
    # Core fields.
    title = models.CharField(max_length=250, help_text="Maximum 250 characters.")
    excerpt = models.TextField(blank=True, 
                               help_text="A short summary of the article. Optional.")
    body = models.TextField(help_text="")
    
    images = generic.GenericRelation("Image")
    
    # Fields to store generated HTML. For use with a markup syntax such as Markdown or Textile
    excerpt_html = models.TextField(editable=False, blank=True)
    body_html = models.TextField(editable=False, blank=True)
        
    # Metadata.
    posted_by = models.ForeignKey(User)
    author = models.ForeignKey(Person, blank=True, null=True, help_text="The author of the article if different from the poster.")
    enable_comments = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    slug = models.SlugField(unique_for_date='pub_date', help_text="Suggested value automatically generated from title. Must be unique.")
    status = models.IntegerField(choices=STATUS_CHOICES, default=LIVE_STATUS, help_text="Only entries with live status will be publicly displayed.")
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    
    tags = TagField(help_text="Separate tags with spaces.")
    
    class Meta:
        ordering = ['-pub_date']
        
    def save(self, force_insert=False, force_update=False):
        if settings.POSTS_MARKUP == 'markdown':
            from markdown import markdown
            self.body_html = markdown(self.body)
            if self.excerpt:
                self.excerpt_html = markdown(self.excerpt)
        elif settings.POSTS_MARKUP == 'wsywig':
            self.body_html = self.body
            self.excerpt_html = self.excerpt
        super(Article, self).save(force_insert, force_update)
    
    def __unicode__(self):
        return self.title
        
    @permalink
    def get_absolute_url(self):
        return ('article-detail', [str(self.slug)])


class Link(models.Model):
    """
    
    A link to another website.
    
    """
    #standard Model Manager
    objects = models.Manager()
    
    # custom Model Manager 
    live = LiveManager()
    
    LIVE_STATUS = 1
    DRAFT_STATUS = 2
    HIDDEN_STATUS = 3
    STATUS_CHOICES = (
        (LIVE_STATUS, 'Live'),
        (DRAFT_STATUS, 'Draft'),
        (HIDDEN_STATUS, 'Hidden'),
    )

    # Core fields.
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    website = models.URLField(unique=True)
    pub_date = models.DateTimeField(default=datetime.datetime.now)
        
    # Fields to store generated HTML. For use with a markup syntax such as Markdown or Textile
    description_html = models.TextField(editable=False, blank=True)
    
    # Metadata.
    posted_by = models.ForeignKey(User)
    enable_comments = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS_CHOICES, default=LIVE_STATUS, help_text="Only entries with live status will be publicly displayed.")
    slug = models.SlugField(unique_for_date='pub_date', help_text="Suggested value automatically generated from title. Must be unique.")
    via_name = models.CharField('Via', max_length=250, blank=True, help_text="The name of the site where you found the link. Optional")
    via_url = models.URLField('Via URL', blank=True, help_text="The URL of the site where you found the link. Optional")
    
    # Categorization.
    tags = TagField(help_text="Separate tags with spaces.")
    
    class Meta:
        ordering = ['-pub_date']
        
    def __unicode__(self):
        return self.title
        
    def save(self):
        if settings.POSTS_MARKUP == 'markdown':
            if self.description:
                self.description_html = markdown(self.description)
        elif settings.POSTS_MARKUP == 'wsywig':
            self.description_html = self.description
        super(Link, self).save()
        
    @permalink
    def get_absolute_url(self):
        return ('link-detail', [str(self.slug)])

class File(models.Model):
    """
    
        Abstract model for files associated with an article or link
                
    """
    # Core file fields.
    user = models.ForeignKey(User, blank=True, null=True,
                             related_name="posts_%(class)s_user", 
                             help_text="The person who is uploading the file.")
    title = models.CharField(max_length=255)
    caption = models.CharField(max_length=255)
    
    # Metadata.
    public = models.BooleanField(default=True, help_text="This file is publicly available.")
    order = PositionField()
    slug = models.SlugField(unique=True, help_text="Suggested value automatically generated from title. Must be unique.")
    
    # non-editable metadata.
    creation_date = models.DateTimeField(auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(auto_now=True, editable=False)
    
    # Allow generic relations
    content_type = models.ForeignKey(ContentType, related_name="posts_%(class)s_contenttype")
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type','object_id')
        
    class Meta:
        ordering = ['-order']
        abstract = True
        
    def __unicode__(self):
        return '%s' % self.title
        
        
class Image(ImageModel, File):
    """
    
        An image file, such as a photograph or other rasterized image.
        Inherits from two abstract classes: File and imageKit.ImageModel.
        File defines fields and imageKit provides processing methods.
    
    """
    
    CROP_LEFT = 0
    CROP_CENTER = 1
    CROP_RIGHT = 2
    CROPHORIZ_CHOICES = (
        (CROP_LEFT, 'LEFT'),
        (CROP_CENTER, 'CENTER'),
        (CROP_RIGHT, 'RIGHT'),
    )
    
    CROP_TOP = 0
    CROP_CENTER = 1
    CROP_BOTTOM = 2
    CROPVERT_CHOICES = (
        (CROP_TOP, 'TOP'),
        (CROP_CENTER, 'CENTER'),
        (CROP_BOTTOM, 'BOTTOM'),
    )
    
    THUMB = 0
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    IMAGE_SIZE_CHOICES = (
        (THUMB, 'Thumbnail'),
        (SMALL, 'Small'),
        (MEDIUM, 'Medium'),
        (LARGE, 'Large'),
    )
    
    LOC_RIGHT = 0
    LOC_LEFT = 1
    LOC_TOP = 2
    LOC_BOTTOM = 3
    IMAGE_LOCATION_CHOICES = (
        (LOC_RIGHT, 'Right'),
        (LOC_LEFT, 'Left'),
        (LOC_TOP, 'Top'),
        (LOC_BOTTOM, 'Bottom'),
    )

    
    # Core image fields.
    image = models.ImageField(upload_to='posts/images')
    image_size = models.IntegerField(choices=IMAGE_SIZE_CHOICES, 
	                            default=SMALL)
    image_location = models.IntegerField(choices=IMAGE_LOCATION_CHOICES, 
	                            default=LOC_RIGHT)
    crop_horiz = models.IntegerField(verbose_name='horizontal cropping', 
                                     choices=CROPHORIZ_CHOICES, 
                                     blank=True,
                                     default=CROP_CENTER,
                                     help_text="From where to horizontally crop the image, if cropping is necessary.")
    crop_vert = models.IntegerField(verbose_name='vertical cropping', 
                                    choices=CROPVERT_CHOICES, 
                                    blank=True,
                                    default=CROP_CENTER,
                                    help_text="From were to vertically crop the image, if cropping is necessary.")
    
    # This inner class is where we define the options for ImageKit processing
    class IKOptions:
        spec_module = 'actionmanual.posts.imagespecs'
        image_field = 'image'
        cache_filename_format = "%(specname)s/%(filename)s.%(extension)s"
        
        
class Video(File):
    """
    
        A file with moving images such as .mov .m4p, .wmv, etc.
        
    """
    
    # Core Video fields.
    video = models.FileField(upload_to='posts/videos', blank=True, null=True,
                             help_text="Upload the video file if the Action Manual is hosting the video")
    poster = models.ImageField(upload_to='posts/videos/posters', blank=True, null=True,
                               help_text="A placeholder image for the video")
    
    url = models.URLField('Video URL', blank=True, help_text="Enter the URL here if this is a linked video from YouTube, Vimeo, etc")
    
    @permalink
    def get_absolute_url(self):
        pass
        
class Flash(File):
    """
    
        A Flash animation.
        
    """
    
    # Core Video fields.
    swf = models.FileField(upload_to='posts/swfs')
    poster = models.ImageField(upload_to='posts/swfs/posters')
    
    class Meta:
        verbose_name_plural = 'Flash Animations'
            
    @permalink
    def get_absolute_url(self):
        pass 



class Audio(File):
    # Core Audio fields.
    audio = models.FileField(upload_to='posts/audio')
    poster = models.ImageField(upload_to='posts/audio/posters')
    
    class Meta:
        verbose_name_plural = "Audio"
        db_table = 'portfolio_audio'
        
    @permalink
    def get_absolute_url(self):
        pass 
    
class Document(File):
    # Core document fields.
    document = models.FileField(upload_to='posts/docs')
    
    @permalink
    def get_absolute_url(self):
        pass 


class ArticleModerator(CommentModerator):
	enable_field = 'enable_comments'
	auto_moderate_field = 'pub_date'
	auto_close_field = 'pub_date'
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
			key=settings.AKISMET_API_KEY,
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
		allow = super(ArticleModerator, self).allow(comment, content_object, request)

		# change this depending on which spam provider you want to use
		spam = self.check_spam(request, comment,
			key=settings.AKISMET_API_KEY,
		)

		return not spam and allow

moderator.register(Article, ArticleModerator)
