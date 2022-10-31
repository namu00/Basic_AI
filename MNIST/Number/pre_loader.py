#For making dataset for Machine Learning.

import sys
import os
import numpy as np
import pickle
from mnist import load_mnist
from PIL import Image
import matplotlib.pyplot as plt

#Load mnist Data
sys.path.append(os.pardir)
(x_train, y_train), (x_test,y_test) = load_mnist(flatten=True, normalize=False)

# print(x_train.shape)
# print(y_train.shape)
# print(x_test.shape)
# print(y_test.shape)

#One-Hot Encoding
no_of_ans = np.unique(y_train).shape[0]
print(no_of_ans)

index = []
for i in y_train:
    index.append(i)

y_hot = np.eye(no_of_ans)[index]
print(y_train.shape)
print(y_hot.shape)