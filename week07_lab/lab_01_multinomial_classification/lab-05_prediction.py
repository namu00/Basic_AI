import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd

# 주교재 : chapter 4
def softmax(x):
    if x.ndim == 2:
        x = x.T
        x = x - np.max(x, axis=0)
        y = np.exp(x) / np.sum(np.exp(x), axis=0)
        return y.T

    x = x - np.max(x) # 오버플로 대책
    return np.exp(x) / np.sum(np.exp(x))

iris = sns.load_dataset("iris")

x = iris.iloc[:,0:4].values
print(x.shape)
y = iris.iloc[:,4].values
print(y.shape)
print(y)

# # 정규화 방법
# x_max = x.max(axis=0)
# x_normal = x / x_max

# x = x_normal.copy()

label = []
# 0 : 'setosa'
# 1 : 'versicolor'
# 2 : 'virginica'

for name in y:
    if name == 'setosa':
        label.append(0)
    elif name == 'versicolor':
        label.append(1)
    elif name == 'virginica':
        label.append(2)

print(label)
print(x)

# one-hot encoding
num = np.unique(label, axis=0)
num = num.shape[0]

encoding = np.eye(num)[label]
print(encoding)

y = np.array(label)
y_hot = encoding.copy()

# 붓꽃 데이터 : 4개
# 클래스 개수 : 3개
dim = 4
nb_classes = 3

print('x shape: ', x.shape, 'y shape: ', y.shape)
# x : (150, 4)
# y : (150, 3)

w = np.loadtxt('weights.txt', delimiter=',')
b = np.loadtxt('bias.txt', delimiter=',')

x_iris = iris.iloc[:,0:4].values
x = x_iris[0]
print('x: ', x)

# x = (1,4) 
# w = (4,3)
# b = (1,3)
# y = (1,3)
t = np.dot(x, w) + b
z = softmax(t)
# print(z.shape)
print('t: ', t, 'z: ', z)
prediction = np.argmax(z)
print('prediction: ', prediction)
print('label: ', y_hot[0])

# x = x_iris[100]
x = x_iris[-1]
print('x: ', x)

t = np.dot(x, w) + b
z = softmax(t)
# print(z.shape)
print('t: ', t, 'z: ', z)
prediction = np.argmax(z)
print('prediction: ', prediction)
print('label: ', y_hot[-1])

x = x_iris[100]
print('x[100]: ', x)

t = np.dot(x, w) + b
z = softmax(t)
# print(z.shape)
print('t: ', t, 'z: ', z)
prediction = np.argmax(z)
print('prediction: ', prediction)
print('label: ', y_hot[100])