#############################################
# Color Image Split & Merge using PILLOW
#############################################

import numpy as np
from PIL import Image

# img = Image.open('../images/img_041.png')
# print(type(img)) # <class 'PIL.PngImagePlugin.PngImageFile'>
#
# # image.show()
#
# print(img.mode)
# print(type(img))
# print(img.size)
#
# bands = img.getbands()
# print(bands)
#
# # split the image
# r, g, b = img.split()
#
# # r is PIL object
# print(type(r))
# print(r.size)
# print(r.mode)
# np_r = np.array(r)
# np_g = np.array(g)
# np_b = np.array(b)
#
# np_r[:, :] = 0
# np_g[:, :] = 0
# np_b[:, :] = 255
#
# r = Image.fromarray(np_r)
# g = Image.fromarray(np_g)
# b = Image.fromarray(np_b)
#
# merge_img = Image.merge('RGB', (r, g, b))
# merge_img.show()


# Question 1: Red Display (768, 1024, 3)
np_r = np.zeros((768, 1024), dtype=np.uint8)
np_r.fill(255)
np_g = np.zeros((768, 1024), dtype=np.uint8)
np_b = np.zeros((768, 1024), dtype=np.uint8)

r = Image.fromarray(np_r)
g = Image.fromarray(np_g)
b = Image.fromarray(np_b)

merge_img = Image.merge('RGB', (r, g, b))
merge_img.show()

# Question 2: Green Display (768, 1024, 3)


# Question 3: Green Display (768, 1024, 3)



