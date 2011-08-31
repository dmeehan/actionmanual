# categories/imagespecs.py

from imagekit.specs import ImageSpec 
from imagekit import processors 

# First we define our "processors". ImageKit ships with four configurable
# processors: Adjustment, Resize, Reflection and Transpose. You can also
# create your own processors. Processors are configured by subclassing and
# overriding specific class variables.

class ResizeAdminThumbnail(processors.Resize):
    width = 32
    height = 32
    
class ResizeSmall(processors.Resize):
    width = 32
    height = 32
    
class ResizeMedium(processors.Resize):
    width = 64
    height = 64

class ResizeLarge(processors.Resize):
    width = 128
    height = 128
    
class Enhance(processors.Adjustment):
    contrast = 1.2
    sharpness = 1.1

class PNGFormat(processors.Format):
    format = 'PNG'
    extension = 'png'

    
# Next we define our specifications or "specs". Image specs are where we define
# the individual "classes" of images we want to have access to. Like processors
# image specs are configured by subclasses the ImageSpec superclass.
    
class AdminThumbnail(ImageSpec):
    access_as = 'admin_thumbnail'
    pre_cache = True
    processors = [ResizeAdminThumbnail, PNGFormat]
    
class Small(ImageSpec):
    pre_cache = True
    processors = [ResizeSmall, PNGFormat]

class Medium(ImageSpec):
    pre_cache = True
    processors = [ResizeMedium, PNGFormat]

class Large(ImageSpec):
    pre_cache = True
    processors = [ResizeLarge, PNGFormat]
