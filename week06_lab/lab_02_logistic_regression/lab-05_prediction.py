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

# 예측
w = 344.90054
b = -198.30700
x = 45 # True : 0
x = x / 100
pred_y = sigmoid(w * x + b)
print('x = ', x*100, 'pred: ', pred_y)

x = 60 # True : 1
x = x / 100
pred_y = sigmoid(w * x + b)
print('x = ', x*100, 'pred: ', pred_y)

x = 52 # True : 0
x = x / 100
pred_y = sigmoid(w * x + b)
print('x = ', x*100, 'pred: ', pred_y)


x = 57 # True : 1
x = x / 100
pred_y = sigmoid(w * x + b)
print('x = ', x*100, 'pred: ', pred_y)

x = 57.5 # True : 1
x = x / 100
pred_y = sigmoid(w * x + b)
print('x = ', x*100, 'pred: ', pred_y)

x = 58 # True : 1
x = x / 100
pred_y = sigmoid(w * x + b)
print('x = ', x*100, 'pred: ', pred_y)

x = 59 # True : 1
x = x / 100
pred_y = sigmoid(w * x + b)
print('x = ', x*100, 'pred: ', pred_y)
