#############################################
# Image Concatnation
#############################################

import numpy as np
from PIL import Image

img = Image.open('../images/monarch.png')
print(type(img)) # <class 'PIL.PngImagePlugin.PngImageFile'>

img.show()

print(img.mode)
print(type(img))
print(img.size)

bands = img.getbands()
print(bands)

np_img = np.array(img).copy()
print(np_img.shape, np_img.ndim)

############################################
# (512, 768, 3) 3  (H, W, C), ndim = 3
############################################

