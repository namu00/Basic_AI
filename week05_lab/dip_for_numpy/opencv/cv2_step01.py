import numpy as np
from PIL import Image
import cv2

image = cv2.imread('../images/baby.png', cv2.IMREAD_COLOR) # for Gray : cv2.IMREAD_GRAY
print(type(image))

# cv2.imshow('Image', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

np_img = image.copy()

print(type(np_img))
print(np_img.shape, np_img.ndim, np_img.size, np_img.dtype)

''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''

image = cv2.imread('../images/img_041.png', cv2.IMREAD_COLOR)
print(type(image))

cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

np_img = image.copy()

print(type(np_img))
print(np_img.shape, np_img.ndim, np_img.size, np_img.dtype)
# (680, 1024, 3) 3 2088960 uint8  -> H, W, C

# for save
# image.save('test.bmp', 'bmp')
# image.save('test.jpg', 'jpg')
# image.save('test.png', 'png')