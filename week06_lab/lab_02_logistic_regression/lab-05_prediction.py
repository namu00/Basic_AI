import numpy as np
from matplotlib import pyplot as plt

# Score
# 0 : Fail, 1 : Pass
data = np.array([
    [45, 0],
    [50, 0],
    [55, 0],
    [60, 1],
    [65, 1],
    [70, 1]
])

# x = data[:, 0] / 100
x = data[:, 0]
y = data[:, 1]

def sigmoid(x):  # 시그모이드 함수 정의
    return 1/(1+np.exp(-x))

w = np.random.uniform(low=0, high=20)
b = np.random.uniform(low=-20, high=10)
print('w: ', w, 'b: ', b)

num_epoch = 10000

learning_rate = 0.5

costs = []

eps = 1e-5

for epoch in range(num_epoch):
    hypothesis = sigmoid(w * x + b)

    cost = y * np.log(hypothesis + eps) + (1 - y) * np.log(1 - hypothesis + eps)
    cost = -1 * cost
    cost = cost.mean()

    if cost < 0.0005:
        break

    w = w - learning_rate * ((hypothesis - y) * x).mean()
    b = b - learning_rate * (hypothesis - y).mean()

    costs.append(cost)

    if epoch % 5000 == 0:
        print("{0:2} w = {1:.5f}, b = {2:.5f} error = {3:.5f}".format(
            epoch, w, b, cost))

print("----" * 15)
print("{0:2} w = {1:.5f}, b = {2:.5f} error = {3:.5f}".format(epoch, w, b, cost))


# # 예측
w = 3.22098
b = -185.16264
x = 45 # True : 0
pred_y = sigmoid(w * x + b)
print(pred_y)

x = 60 # True : 1
pred_y = sigmoid(w * x + b)
print(pred_y)

x = 52 # True : 0
pred_y = sigmoid(w * x + b)
print(pred_y)

x = 58 # True : 1
pred_y = sigmoid(w * x + b)
print(pred_y)
