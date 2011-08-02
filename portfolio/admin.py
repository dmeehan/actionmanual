# portfolio/admin.py

from django import forms
from django.contrib import admin
from django.contrib.contenttypes import generic
from django.conf import settings

from actionmanual.widgets import AdminImageWidget
from actionmanual.portfolio.models import *
from actionmanual.sections.models import SectionItem
from actionmanual.categories.models import CategoryItem
from actionmanual.contacts.models import Person, Organization

def make_published(modeladmin, request, queryset):
    queryset.update(status='2')
make_published.short_description = "Mark selected as published"

class CategoryIdeaInline(admin.TabularInline):
    model = Idea.categories.through
    extra = 1
    verbose_name = "category"
    verbose_name_plural = "categories"

    # Grappelli options
    allow_add = True
    classes = ('collapse closed',)

class CategoryPrecedentInline(admin.TabularInline):
    model = Precedent.categories.through
    extra = 0
    verbose_name = "category"
    verbose_name_plural = "categories"
   
    # Grappelli options
    allow_add = True
    classes = ('collapse closed',)
    
class ResourceInline(admin.TabularInline):
    model = Resource
    extra = 0

    # Grappelli options
    allow_add = True
    classes = ('collapse closed',)
    
    
class ImageInline(generic.GenericStackedInline):
    model = Image
    prepopulated_fields = {"slug": ("title",)}
    fields = ('order', 'image', 'title', 'caption', 'public', 'lead', 'user', 'author', 
	          'copyright', 'slug', 'crop_horiz', 'crop_vert', ) 
    extra = 0
    ordering = ('order',)
    
    # Grappelli options
    allow_add = True
    sortable_field_name = "order"
    classes = ('collapse closed',)
    
class VideoInline(generic.GenericTabularInline):
    model = Video
    extra = 0
    
    # Grappelli options
    allow_add = True
    sortable_field_name = "order"
    classes = ('collapse closed',)
    
class FlashInline(generic.GenericTabularInline):
    model = Flash
    extra = 1
    
    # Grappelli options
    allow_add = True
    sortable_field_name = "order"
    classes = ('collapse closed',)
    
class AudioInline(generic.GenericTabularInline):
    model = Audio
    extra = 0
    
    # Grappelli options
    allow_add = True
    sortable_field_name = "order"
    classes = ('collapse closed',)
    
class DocumentInline(generic.GenericTabularInline):
    model = Document
    extra = 0
    
    # Grappelli options
    allow_add = True
    sortable_field_name = "order"
    classes = ('collapse closed',)
    
class DesignerInline(generic.GenericStackedInline):
    model = Designer
    extra = 0
    
    #Grappelli options
    allow_add = True
    sortable_field_name = "order"
    classes = ('collapse closed',)
 
class FirmInline(generic.GenericStackedInline):
    model = Firm
    extra = 0
    
    #Grappelli options
    allow_add = True 
    sortable_field_name = "order" 
    classes = ('collapse closed',) 
    
class PrecedentIdeaInline(admin.TabularInline):
    model = PrecedentIdeaRelation
    extra = 0
    
    verbose_name = "related idea"
    verbose_name_plural = "related ideas"
    
    #Grappelli options
    allow_add = True
    sortable_field_name = "order"
    classes = ('collapse closed',)

class IdeaPrecedentInline(admin.TabularInline):
    model = PrecedentIdeaRelation
    extra = 0

    verbose_name = "precedent"
    verbose_name_plural = "precedents"

    #Grappelli options
    allow_add = True
    sortable_field_name = "order" 
    classes = ('collapse closed',)
    
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title','admin_thumbnail_view', 'caption')
    prepopulated_fields = {"slug": ("title",)}
    fields = ('image', 'title', 'caption', 'order', 'public', 'lead', 'user', 'author', 
	          'copyright', 'slug', 'crop_horiz', 'crop_vert',)

    
class IdeaAdmin(admin.ModelAdmin):
    def queryset(self, request):
         return Idea.objects
    list_display = ('title', 'tagline', 'user', 'status', 'date_published', 'featured', 'enable_comments', 'city',)
    prepopulated_fields = {"slug": ("title",)}
    list_editable = ('status', 'featured', 'enable_comments')
    inlines = [
        CategoryIdeaInline,
        ImageInline,
        FirmInline,
        DesignerInline,
    ]
    actions = [make_published]

    fieldsets = (
        (None, {
            'fields': ('user',)
        }),
        ('Project Info', {
            'classes': ('collapse open',),
            'fields': ('title', 'tagline', 'description', 'tags',),
        }),
        ('Display Options', {
            'classes': ('collapse open',),
            'fields' : ('status', 'featured', 'enable_comments', 'slug',),
        }),
         ('Location', {
            'classes': ('collapse open',),
            'fields': ('location', 'location_name', 'address', 'city', 'state', 'zip_code',)
        }),
    )
    
    # Media
    class Media:
        js = [
            settings.ADMIN_MEDIA_PREFIX + 'tinymce/jscripts/tiny_mce/tiny_mce.js',
            settings.ADMIN_MEDIA_PREFIX + 'tinymce_setup/tinymce_setup.js',
        ]
    
class PrecedentAdmin(admin.ModelAdmin):
    list_display = ('title', 'tagline', 'city', 'user', 'status', 'date_published', 'featured', 'enable_comments',)
    prepopulated_fields = {"slug": ("title",)}
    list_editable = ('status', 'featured', 'enable_comments')
    inlines = [
        PrecedentIdeaInline,
        CategoryPrecedentInline,
        ImageInline,
        FirmInline,
        DesignerInline,
    ]
    actions = [make_published]
    
    fieldsets = (
        (None, {
            'fields': ('user',)
        }),
        ('Precedent Info', {
            'fields': ('title', 'tagline', 'description', 'tags', 'website', ),
        }),
        ('Location', {
            'fields': ('location', 'location_name', 'address', 'city', 'state', 'zip_code',)
        }),
        ('Display Options', {
            'classes': ('collapse-open',),
            'fields' : ('status', 'featured', 'enable_comments', 'slug',),
        }),
    )
    
    # Media
    class Media:
        js = [
            settings.ADMIN_MEDIA_PREFIX + 'tinymce/jscripts/tiny_mce/tiny_mce.js',
            settings.ADMIN_MEDIA_PREFIX + 'tinymce_setup/tinymce_setup.js',
        ]

admin.site.register(Idea, IdeaAdmin)
admin.site.register(Precedent, PrecedentAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Firm)
admin.site.register(Designer)
