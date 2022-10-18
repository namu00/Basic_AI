#############################################
# Image Concatnation
#############################################

import numpy as np
from PIL import Image

img = Image.open('../images/img_041.png')
print(type(img)) # <class 'PIL.PngImagePlugin.PngImageFile'>

# img.show()

print(img.mode)
print(type(img))
print(img.size)

bands = img.getbands()
print(bands)

np_img = np.array(img).copy()
print(np_img.shape, np_img.ndim)

############################################
# (680, 1024, 3) 3  (H, W, C), ndim = 3
############################################

# 3D -> 4D
np_img = np_img[np.newaxis, :, :, :]
print('This is 4D shape(N, H, W, C): ', np_img.shape)

np_img = np.concatenate((np_img, np_img), axis=0)
print('This is 4D shape(N, H, W, C): ', np_img.shape)

# How to solve it? 100 images concatnation (100, H, W, C)

# How to solve it? 1000 images concatnation (1000, H, W, C)