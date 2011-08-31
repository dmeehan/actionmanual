# posts/admin.py

from django.contrib import admin
from django.contrib.contenttypes import generic
from django.conf import settings

from actionmanual.posts.models import *
from actionmanual.sections.models import SectionItem
from actionmanual.categories.models import CategoryItem

class CategoryItemInline(generic.GenericTabularInline):
    model = CategoryItem
    extra = 2
    verbose_name = "category"
    verbose_name_plural = "categories"
    
    # Grappelli options
    allow_add = True
    sortable = True
    
class SectionItemInline(generic.GenericTabularInline):
    model = SectionItem
    extra = 2
    exclude = ['order']
    verbose_name = "section"
    verbose_name_plural = "sections"
    
    # Grappelli options
    allow_add = True
    sortable_field_name = "order"
    
class ImageInline(generic.GenericStackedInline):
    model = Image
    prepopulated_fields = {"slug": ("title",)}
    fields = ('order', 'image', 'title', 'caption', 'public', 'user', 
	          'slug', 'crop_horiz', 'crop_vert', 'image_size', 'image_location',) 
    extra = 3
    ordering = ('order',)
    
    # Grappelli options
    allow_add = True

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'author', 'status', 'featured', 'enable_comments',)
    prepopulated_fields = {"slug": ("title",)}
    list_editable = ('status', 'featured', 'enable_comments')
    inlines = [
        ImageInline,
        CategoryItemInline,
        SectionItemInline,
    ]
    
    fieldsets = (
        (None, {
            'fields': ('posted_by', 'author',),
        }),
        ('Content', {
            'fields': ('title', 'excerpt', 'body',),
        }),
        ('Options', {
            'fields' : ('status', 'featured', 'enable_comments', 'pub_date',),
        }),
        ('Metadata', {
            'fields' : ('slug', 'tags',),
        }),
    )
    
    # Media
    class Media:
        js = [
            settings.ADMIN_MEDIA_PREFIX + 'tinymce/jscripts/tiny_mce/tiny_mce.js',
            settings.ADMIN_MEDIA_PREFIX + 'tinymce_setup/tinymce_setup.js',
        ]
        

class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date',)
    prepopulated_fields = {"slug": ("title",)}
    inlines = [
	CategoryItemInline,
        SectionItemInline,
    ]
    
    fieldsets = (
        (None, {
            'fields': ('posted_by',),
        }),
        ('Content', {
            'fields': ('title', 'description', 'website', 'via_name', 'via_url', 'tags'),
        }),
        ('Display Options', {
            'fields' : ('status', 'pub_date', 'slug',),
        }),
    )

admin.site.register(Article, ArticleAdmin)
