from django import forms

from actionmanual.portfolio.models import Idea, Image

class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        exclude = ['user', 'slug', 'status', 
                   'enable_comments', 
                   'moderate_comments',
                   'featured', 'location',
                   'location_name', 'zip_code', 
                   'address',
                   'website', 'copyright', 
                   'tags', 'categories']


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user', 'author', 'public',
                   'order', 'copyright', 'slug',
                   'content_type', 'object_id',]
