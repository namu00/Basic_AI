import numpy as np
from PIL import Image


#Print Red
Red = np.zeros((600,800,3),dtype=np.uint8)
Red[:,:,0] = np.ones((600,800))*255
#Red[:,:,0] = 255
image2 = Image.fromarray(Red)
print(type(image2))
image2.show()

#Print Green
Green = np.zeros((600,800,3),dtype=np.uint8)
Green[:,:,1] = np.ones((600,800))*255
image2 = Image.fromarray(Green)
print(type(image2))
image2.show()

#Print Blue
Blue = np.zeros((600,800,3),dtype=np.uint8)
Blue[:,:,1] = np.ones((600,800))*255
image2 = Image.fromarray(Green)
print(type(image2))
image2.show()
