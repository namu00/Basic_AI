#############################################
# Image Concatnation
#############################################

import numpy as np
from PIL import Image

img = Image.open('../images/img_041.png')
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
# (680, 1024, 3) 3  (H, W, C), ndim = 3
############################################

# Case 1
np_img_1 = 255 - np_img

img2 = Image.fromarray(np_img_1)
img2.show()

# Case 2
np_img_2 = 255 - np_img[:,:,0]
print(np_img.shape)
np_img[:, :, 0] = np_img_2
print(np_img.shape)
img2 = Image.fromarray(np_img)
img2.show()