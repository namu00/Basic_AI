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
(x_train, y_train), (x_test,y_test) = load_mnist(flatten=True, normalize=True)

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
print(y_hot)
print(y_hot.shape)

#Learning
def softmax(x):
    if x.ndim ==2:
        x = x.T
        x = x - np.max(x,axis=0) #normalize by max value
        y = np.exp(x) / np.sum(np.exp(x), axis= 0) #softmax function
        return y.T

    x = x - np.max(x)
    return np.exp(x)/np.sum(np.exp(x))
    
def learning(w,x,b,learning_rate=200):
    m = x.shape[0]
    epoch = 10000
    eps = 1e-20
    costs = 0
    for i in range(epoch):
        _y = np.dot(w,x) + b
        predict = softmax(_y)

        cost = y_hot * np.log(predict + eps)
        cost = -cost.mean()
        costs = cost

        if cost < 0.000005: break
        w_grad = (1/m)*np.dot(x.T, (predict - y_hot))
        b_grad = (1/m)*np.sum(predict - y_hot)

        w = w - learning_rate*w_grad
        b = b - learning_rate*b_grad
    return w,b,costs
#w = np.ones()
cost = 0
x_train = x_train.reshape(x_train.shape[0],28,28)
for i in range(30):
    os.system("cls")
    print("1 Session = 10000epoch")

    print("Session Number: %3d, Cost: %0.5f" %(i, cost))
    

print(y_hot.shape)