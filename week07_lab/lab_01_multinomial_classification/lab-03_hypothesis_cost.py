import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd

iris = sns.load_dataset("iris")

x = iris.iloc[:,0:4].values
print(x.shape)
y = iris.iloc[:,4].values
print(y.shape)
print(y)

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

y = encoding.copy()

# 붓꽃 데이터 : 4개
# 클래스 개수 : 3개
dim = 4
nb_classes = 3

print('x shape: ', x.shape, 'y shape: ', y.shape)
# x : (150, 4)
# y : (150, 3)

# w : (4, 3)
# b : (3,)
w = np.random.normal(size=[dim, nb_classes]) 
b = np.random.normal(size=[nb_classes])

print('w shape: ', w.shape, 'b shape: ', b.shape)

# x (150, 4) * w (4, 3) + b (150, 3)(broad-casting) => predict(150, 3) <=> y_hot(150, 3)

def cross_entropy_error(predict, target):
    delta = 1e-7
    return -np.mean(target * np.log(predict + delta))

def softmax(x):
    if x.ndim == 2:
        x = x.T
        x = x - np.max(x, axis=0)
        y = np.exp(x) / np.sum(np.exp(x), axis=0)
        return y.T

    x = x - np.max(x) # 오버플로 대책
    return np.exp(x) / np.sum(np.exp(x))

hypothesis = softmax(np.dot(x, w) + b)
print('hypothesis: ', hypothesis.shape)

# hypothesis:  (150, 3)

eps = 1e-7

# 방법 1
cost = y * np.log(hypothesis + eps)
cost = -cost.mean()
print('cost: ', cost)

# 방법 2
cost = cross_entropy_error(hypothesis, y)
print('cost: ', cost)