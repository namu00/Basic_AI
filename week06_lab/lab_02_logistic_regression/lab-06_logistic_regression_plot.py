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

# text file input/output

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

    # reference : https://nlogn.in/logistic-regression-and-its-cost-function-detailed-introduction/
    w = w - learning_rate * ((hypothesis - y) * x).mean()
    b = b - learning_rate * (hypothesis - y).mean()

    costs.append(cost)

    if epoch % 5000 == 0:
        print("{0:2} w = {1:.5f}, b = {2:.5f} error = {3:.5f}".format(
            epoch, w, b, cost))

print("----" * 15)
print("{0:2} w = {1:.5f}, b = {2:.5f} error = {3:.5f}".format(epoch, w, b, cost))


# # 예측
w = 3.22902
b = -185.41300
x = 45 # True : 0
pred_y = sigmoid(w * x + b)
print(pred_y)

x = 60 # True : 1
pred_y = sigmoid(w * x + b)
print(pred_y)

x = data[:, 0]
y = data[:, 1]

org_x = np.linspace(0, 100, 100)
pred_y = sigmoid(w * org_x + b)

plt.scatter(x, y) 
plt.title("Pass/Fail vs Score")
plt.xlabel("Score")
plt.ylabel("Pass/Fail")
plt.plot(org_x, pred_y, 'r')
# plt.axis([0, 420, 0, 50])
plt.show()