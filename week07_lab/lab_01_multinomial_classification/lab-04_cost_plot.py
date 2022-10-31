import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd

iris = sns.load_dataset("iris")

x = iris.iloc[:,0:4].values
print(x.shape)
print(type(x))
y = iris.iloc[:,4].values
print(y.shape)
print(y)

# # 정규화 방법
x_max = x.max(axis=0)
x_normal = x / x_max

x = x_normal.copy()
print(x)

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

w = np.random.normal(size=[dim, nb_classes])
b = np.random.normal(size=[nb_classes])

print('w shape: ', w.shape, 'b shape: ', b.shape)

# w : (4, 3)
# b : (3,)

# 주교재 : chapter 4
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

#num_epoch = 1000000000000000000000000000000000
learning_rate = 0.01
costs = []

m, n = x.shape
print(type(m))
epoch = 0;
while True: #for epoch in range(num_epoch):
    epoch += 1
    # z = x@w + b or
    z = np.dot(x, w) + b
    # print(z.shape)
    hypothesis = softmax(z)
    # print('hypothesis: ', hypothesis.shape)
    
    # cost = -np.mean(np.log(hypothesis[np.arange(len(y)), y]))
    # or 
    cost = y_hot * np.log(hypothesis + eps)
    cost = -cost.mean()

    if cost < 0.00005:
        break

    # https://towardsdatascience.com/softmax-regression-in-python-multi-class-classification-3cb560d90cb2
    # Calculating the gradient of loss w.r.t w and b.
    w_grad = (1/m)*np.dot(x.T, (hypothesis - y_hot))
    b_grad = (1/m)*np.sum(hypothesis - y_hot)

    w = w - learning_rate * w_grad
    b = b - learning_rate * b_grad

    costs.append(cost)

    if epoch % 50 == 0:
        print("{0:2} error = {1:.5f}".format(epoch, cost))

print("----" * 15)
print("{0:2} error = {1:.5f}".format(epoch, cost))

# np.savetxt('./lab_08_multinomial_classification/weights.txt', w, delimiter=',')
# np.savetxt('./lab_08_multinomial_classification/bias.txt', b, delimiter=',')

np.savetxt('weights.txt', w, delimiter=',')
np.savetxt('bias.txt', b, delimiter=',')

plt.figure(figsize=(10, 7))
plt.plot(costs)
plt.xlabel('Epochs')
plt.ylabel('Costs')
plt.show()

# Prediction Example
# x_iris = iris.iloc[:,0:4].values
# x = x_iris[0]
# print(x)

# # x = (1,4) 
# # w = (4,3)
# # b = (1,3)
# # y = (1,3)
# t = np.dot(x, w) + b
# z = softmax(t)
# # print(z.shape)
# print('t: ', t, 'z: ', z)
# prediction = np.argmax(z)
# print('prediction: ', prediction)

# # x = x_iris[100]
# x = x_iris[-2]
# print(x)

# t = np.dot(x, w) + b
# z = softmax(t)
# # print(z.shape)
# print('t: ', t, 'z: ', z)
# prediction = np.argmax(z)
# print('prediction: ', prediction)

