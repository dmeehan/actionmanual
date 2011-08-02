# portfolio/imagespecs.py

from imagekit.specs import ImageSpec 
from imagekit import processors 

# First we define our "processors". ImageKit ships with four configurable
# processors: Adjustment, Resize, Reflection and Transpose. You can also
# create your own processors. Processors are configured by subclassing and
# overriding specific class variables.

class ResizeAdminThumbnail(processors.Resize):
    width = 120
    height = 67
    crop = True
    
class EnhanceSmall(processors.Adjustment):
    contrast = 1.2
    sharpness = 1.1
    
class ResizeMax(processors.Resize):
    width = 960
    
class ResizeLarge(processors.Resize):
    width = 620
    height = 350
    crop = True
    
class ResizeMedium(processors.Resize):
    width = 460
    height = 258
    crop = True
    
class ResizeSmall(processors.Resize):
    width = 140
    height = 105
    crop = True
    
class ResizeHomeSmall(processors.Resize):
    width = 160
    height = 120
    crop = True
    
# Next we define our specifications or "specs". Image specs are where we define
# the individual "classes" of images we want to have access to. Like processors
# image specs are configured by subclasses the ImageSpec superclass.
    
class AdminThumbnail(ImageSpec):
    access_as = 'admin_thumbnail'
    pre_cache = False
    processors = [ResizeAdminThumbnail, EnhanceSmall]
    
class Max(ImageSpec):
    pre_cache = False
    processors = [ResizeMax]
    
class Large(ImageSpec):
    pre_cache = False
    processors = [ResizeLarge]

class Medium(ImageSpec):
    pre_cache = False
    processors = [ResizeMedium]
    
class Small(ImageSpec):
    pre_cache = False
    processors = [ResizeSmall]
    
class HomeSmall(ImageSpec):
    pre_cache = False
    processors = [ResizeHomeSmall]