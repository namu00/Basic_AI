#############################################
# Image Save using Pillow
#############################################

import numpy as np
from PIL import Image

image = Image.open('../images/img_041.png')
print(type(image)) # <class 'PIL.PngImagePlugin.PngImageFile'>

# image.show()

np_img = np.array(image)

print(type(np_img))
print(np_img.shape, np_img.ndim, np_img.size, np_img.dtype)
# Cautions: shape (680, 1024, 3) -> H, W, C

# numpy to PIL
image2 = Image.fromarray(np_img) # NumPy array to PIL image
print(type(image2))

# for save
image.save('test.bmp', 'bmp')
# image.save('test.jpg', 'jpg')
# image.save('test.png', 'png')