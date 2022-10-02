#############################################
# Image Save using Pillow
#############################################

import numpy as np
from PIL import Image

image = Image.open('../images/img_041.png')
print(type(image)) # <class 'PIL.PngImagePlugin.PngImageFile'>
