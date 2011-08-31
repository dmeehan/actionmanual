# categories/admin.py

from django.contrib import admin
from actionmanual.categories.models import *
from actionmanual.portfolio.models import FeaturedCategoryIdea
from actionmanual.portfolio.models import Idea

class CategoryInline(admin.TabularInline):
    model = Category
    extra = 1
    fields = ('order', 'name',)
    readonly_fields = ('name',)
    ordering = ['order']
    
    # Grappelli options
    sortable_field_name = "order"
    allow_add = False
    
    

class CategoryItemInline(admin.TabularInline):
    model = CategoryItem
    extra = 1
    verbose_name = "category item"
    verbose_name_plural = "category items"
    
    # Grappelli options
    sortable_field_name = "order"
    
class FeaturedCategoryIdeaInline(admin.TabularInline):
    model = FeaturedCategoryIdea
    extra = 1
    verbose_name = "featured idea"
    verbose_name_plural = "featured ideas"
    
    # Grappelli options
    sortable_field_name = "order"
    
class IdeaInline(admin.TabularInline):
    model = Idea.categories.through
    extra = 1
    verbose_name = "idea"
    verbose_name_plural = "ideas"
    
    # Grappelli options
    sortable_field_name = "order"

        
class CategoryGroupAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name','description')
    
    inlines = [
         CategoryInline,
    ]    
   
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'admin_thumbnail_view', 'group',)
    ordering = ['group', '-order']
    exclude = ('order',)
    inlines = [
         FeaturedCategoryIdeaInline,
         IdeaInline,
         CategoryItemInline
    ]
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(CategoryGroup, CategoryGroupAdmin)