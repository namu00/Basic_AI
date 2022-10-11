#############################################
# NCHW? NHWC?
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
np_img2 = np.array(img).copy()

############################################
# (680, 1024, 3) 3  (H, W, C), ndim = 3
############################################

# 3D -> 4D
np_img = np_img[np.newaxis, :, :, :]
print('This is 4D shape(N, H, W, C): ', np_img.shape)

# NHWC -> NCHW
np_img = np.transpose(np_img, (0, 3, 1, 2))
print('This is 4D shape(N, C, H, W): ', np_img.shape)

# NCHW -> NHWC
np_img = np.transpose(np_img, (0, 2, 3, 1))
print('This is 4D shape(N, H, W, C): ', np_img.shape)


# 3D -> 4D
np_img2 = np_img2[np.newaxis, :, :, :]
print('This is 4D shape(N, H, W, C): ', np_img2.shape)

np_img2 = np.swapaxes(np_img2, 1, 3) # N C W H
np_img2 = np.swapaxes(np_img2, 2, 3) # N C W H
print('This is 4D shape(N, C, H, W): ', np_img2.shape)


