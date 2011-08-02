from django.contrib import admin
from grappelli.sites import GrappelliSite
admin.site = GrappelliSite()
admin.autodiscover()

admin.site.groups = {
    0: {
        'name': 'Content',
        'classes': '',
        'show_apps': True,
        'apps': ['portfolio', 'posts', 'contacts', 'comments']
    },
    1: {
        'name':'Organization',
        'classes': '',
        'show_apps': False,
        'apps': ['categories', 'tagging',]
    },
    2: {
        'name':'Presentation',
        'classes': '',
        'show_apps': False,
        'apps': ['maestro','sites',]
    },
    3: {
        'name': 'Users & Profiles',
        'classes': ['collapse-closed'],
        'show_apps': False,
        'apps': ['auth']
    },
    4: {  
        'name': 'Admin Options',
        'classes': ['collapse-closed'],
        'show_apps': False,
        'apps': ['grappelli']
    },
}
