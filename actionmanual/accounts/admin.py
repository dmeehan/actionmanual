# accounts/admin.py

from django.contrib import admin
from actionmanual.accounts.models import *
from actionmanual.portfolio.models import Idea

class IdeaInline(admin.TabularInline):
    model = Idea
    extra = 1

    # Grappelli options
    allow_add = True
    classes = ('collapse closed',)
    
class UserProfileAdmin(admin.ModelAdmin):
    inlines = [ IdeaInline, ]
    
admin.site.register(UserProfile)