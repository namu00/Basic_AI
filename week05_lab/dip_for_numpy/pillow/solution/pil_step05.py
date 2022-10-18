#############################################
# Dimension Expansion using numpy
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

img_gray = img.convert('L')
# img_gray.show()

img_gray = np.array(img_gray)

print(img_gray.shape) # H, W

# 2D -> 3D
img_gray_3d = img_gray[:, :, np.newaxis]
print(img_gray_3d.shape)   # H, W, C(=1)

# 3D -> 4D
img_gray_4d = img_gray_3d[np.newaxis, :, :]
print(img_gray_4d.shape)   # N(=1), H, W, C(=1)

# 4D -> 3D
img2_3d = img_gray_4d[0, :, :, :]
print(img2_3d.shape)

# 3D -> 2D
img2_2d = img2_3d[:, :, 0]
print(img2_2d.shape)

# Exception
# img2_3d
# pil_img = Image.fromarray(img2_3d)  # FAIL
pil_img = Image.fromarray(img2_2d)  # PASS
pil_img.show()    # This is Gray Image (One Channel)

# 1CH -> 3CH
# img2_3d  (H, W, C=1)
new_img_3d = np.concatenate((img2_3d, img2_3d, img2_3d), axis=2)
print(new_img_3d.shape)

pil_img3 = Image.fromarray(new_img_3d)  # PASS
pil_img3.show()  # This Color Image (Three Channel)


