import sys, os
sys.path.append('./dataset')
import numpy as np
from dataset.mnist import load_mnist

(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, flatten=True, one_hot_label=False)

print(x_train.shape)
print(t_train.shape)

print(x_test.shape)
print(t_test.shape)
