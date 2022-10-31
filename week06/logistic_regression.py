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
    [70, 1],
    [69, 1],
    [53, 0],
    [59, 0]])

x = data[:,0]
x = x / max(x)

y = data[:,1]

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

w = 1
b = 1
epoch = 50000
learning_rate = 100
eps = 1e-5

for n in range(epoch):
    _predict = sigmoid(w*x + b)
    
    error = y * np.log(_predict + eps) + (1 - y)*np.log(1 - _predict + eps)
    error *= -1
    cost =  error.mean()

    if cost < 0.0005:
        break

    w = w - learning_rate * ((_predict - y) * x).mean()
    b = b - learning_rate * (_predict - y).mean()

    # if n%50 == 0:
    #     print("try: %5d , error: %.5f " % (n, cost))

x_cord = np.linspace(0,max(data[:,0]),100) / max(data[:,0])
y_cord = sigmoid(w*x_cord + b)

plt.scatter(data[:,0],data[:,1])
plt.plot(x_cord* max(data[:,0]),y_cord)
plt.axis([40, 75, -0.1, 1.1])
plt.show()