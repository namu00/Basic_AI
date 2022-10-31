import sys
import os
import numpy as np
import pickle
from mnist import load_mnist
from PIL import Image
import matplotlib.pyplot as plt

sys.path.append(os.pardir)
(x_train, t_train), (x_test,t_test) = load_mnist(flatten=True, normalize=False)

print(x_train.shape)
print(t_train.shape)
print(x_test.shape)
print(t_test.shape)

img_array = x_train[59999].reshape(28,28)
img = Image.fromarray(np.uint8(img_array))
img.show()