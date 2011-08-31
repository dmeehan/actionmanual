# resources/admin.py

from django.contrib import admin
from django.contrib.contenttypes import generic
from django.conf import settings

from actionmanual.resources.models import *
from actionmanual.posts.models import Image
from actionmanual.categories.models import CategoryItem

class CategoryItemInline(generic.GenericTabularInline):
    model = CategoryItem
    extra = 2
    verbose_name = "category"
    verbose_name_plural = "categories"
    
    # Grappelli options
    allow_add = True
    
class ImageInline(generic.GenericStackedInline):
    model = Image
    prepopulated_fields = {"slug": ("title",)}
    fields = ('order', 'image', 'title', 'caption', 'public', 'user', 
	          'slug', 'crop_horiz', 'crop_vert', 'image_size', 'image_location',) 
    extra = 3
    ordering = ('order',)
    
    # Grappelli options
    allow_add = True

class EssayAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'featured', 'enable_comments', 'author',)
    prepopulated_fields = {"slug": ("title",)}
    verbose_name = "blog post"
    verbose_name_plural = "blog posts"
    inlines = [
        ImageInline,
        CategoryItemInline,
    ]
    
    # Media
    class Media:
        js = [
            settings.ADMIN_MEDIA_PREFIX + 'tinymce/jscripts/tiny_mce/tiny_mce.js',
            settings.ADMIN_MEDIA_PREFIX + 'tinymce_setup/tinymce_setup.js'
        ]

class WebAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date',)
    prepopulated_fields = {"slug": ("title",)}
    inlines = [
        CategoryItemInline,
    ]
        
    # Media
    class Media:
        js = [
            settings.ADMIN_MEDIA_PREFIX + 'tinymce/jscripts/tiny_mce/tiny_mce.js',
            settings.ADMIN_MEDIA_PREFIX + 'tinymce_setup/tinymce_setup.js',
        ]
        
class PersonAdmin(admin.ModelAdmin):
	list_display = ('last_name', 'first_name',)
	ordering = ('last_name', 'first_name',)
	search_fields = ('first_name', 'last_name',)
	prepopulated_fields = {'slug': ('first_name','last_name',)}
	inlines = [
              CategoryItemInline,
        ]
        fields = ('first_name', 'middle_name', 'last_name', 
                  'description', 
                  'address_line1', 'address_line2', 
	              'city', 'state', 'code', 'country', 
	              'email', 'phone', 'fax', 'mobile', 'website', 'gender', 'birth_date',
	              'tags',
                  'slug', )
	
class OrganizationAdmin(admin.ModelAdmin):
	list_display = ('name',)
	ordering = ('name',)
	search_fields = ('name',)
	prepopulated_fields = {'slug': ('name',)}
        inlines = [
              CategoryItemInline,
        ]
	fields = ('name', 'org_type', 'description', 'address_line1', 'address_line2', 
	          'city', 'state', 'code', 'country',
	          'email', 'phone', 'fax', 
	          'website', 'tags',
	          'slug' )
      


admin.site.register(Essay, EssayAdmin)
admin.site.register(Web, WebAdmin)
admin.site.register(ResourceOrganization, OrganizationAdmin)
admin.site.register(ResourcePerson, PersonAdmin)