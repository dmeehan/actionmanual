# contacts/admin.py

from django.contrib import admin
from django.contrib.contenttypes import generic
from actionmanual.contacts.models import Person, Organization
from actionmanual.sections.models import SectionItem
from actionmanual.categories.models import CategoryItem

class CategoryItemInline(generic.GenericTabularInline):
        model = CategoryItem
        extra = 2
        verbose_name = "category"
        verbose_name_plural = "categories"

        # Grappelli options
        allow_add = True

class SectionItemInline(generic.GenericTabularInline):
       model = SectionItem
       extra = 2
       exclude = ['order']
       verbose_name = "section"
       verbose_name_plural = "sections"

       # Grappelli options
       allow_add = True

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
	          'email', 'phone', 'fax', 'mobile', 'website', 'gender', 'birth_date', 'tags',
                  'slug', )
	
class OrganizationAdmin(admin.ModelAdmin):
	list_display = ('name',)
	ordering = ('name',)
	search_fields = ('name',)
	prepopulated_fields = {'slug': ('name',)}
        inlines = [
              CategoryItemInline,
              SectionItemInline,
        ]
	fields = ('name', 'org_type', 'description', 'address_line1', 'address_line2', 
	          'city', 'state', 'code', 'country',
	          'email', 'phone', 'fax', 
	          'website', 'tags', 'slug', )


admin.site.register(Person, PersonAdmin)
admin.site.register(Organization, OrganizationAdmin)
