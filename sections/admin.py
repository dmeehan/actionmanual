# sections/admin.py

from django.contrib import admin
from actionmanual.sections.models import *

class SectionItemInline(admin.TabularInline):
    model = SectionItem
    verbose_name = "section item"
    verbose_name_plural = "section items"
    
    # Grappelli options
    allow_add = True
    sortable_field_name = "order"
    
class SectionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    inlines = [
        SectionItemInline
    ]

admin.site.register(Section, SectionAdmin)
