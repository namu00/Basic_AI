#############################################
# Color Image Split & Merge using PILLOW
#############################################

import numpy as np
from PIL import Image

img = Image.open('../images/img_041.png')
print(type(img)) # <class 'PIL.PngImagePlugin.PngImageFile'>

# image.show()

print(img.mode)
print(type(img))
print(img.size)

bands = img.getbands()
print(bands)

# split the image
r, g, b = img.split()

# r is PIL object
print(type(r))
print(r.size)
print(r.mode)

# Compare with PIL & numpy
np_r = np.array(r)
np_g = np.array(g)
np_b = np.array(b)

# PIL to numpy
np_img = np.array(img)
print(np_img.shape, np.ndim)

np_red = np_img[:, :, 0]   # 0 channel is red
print(np.array_equal(np_r, np_red))

np_green = np_img[:, :, 1]   # 1 channel is green
print(np.array_equal(np_g, np_green))

np_blue = np_img[:, :, 2]   # 2 channel is blue
print(np.array_equal(np_b, np_blue))

# Merge Image
merge_img = Image.merge('RGB', (r, g, b))
merge_img.show()


