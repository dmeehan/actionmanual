# contacts/views.py


from django.views.generic.list_detail import object_list, object_detail

from actionmanual.contacts.models import *

def person_detail(request, slug):
    person = Person.objects.filter(slug=slug)
    return object_detail(request, 
                       queryset=person,
                       slug = slug,)
                       
def org_detail(request, slug):
    org = Organization.objects.filter(slug=slug)
    return object_detail(request, 
                       queryset=org,
                       slug=slug,)