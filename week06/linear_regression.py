import numpy as np 
from matplotlib import pyplot as plt 

data = np.array([[100, 20], 
		[150, 24], 
		[300, 36], 
		[400, 47], 
		[130, 22], 
		[240, 32],
		[350, 47], 
		[200, 42], 
		[100, 21], 
		[110, 21], 
		[190, 30], 
		[120, 25], 
		[130, 18], 
		[270, 38], 
		[255, 28]])

lr = 0.5 #Learning Rate
w = 1
b = 1

def predict_function(x):
    return w*x + b

epoch = 50000
eps = 1e-10
x_max = max(data[:,0])
y_max = max(data[:,1])
x = data[:,0] / max(data[:,0])
y = data[:,1] / x_max

for i in range(epoch):
    temp = []

    predict_result = predict_function(x)

    error = (y - predict_result)**2
    cost = error.mean()

    if cost < 0.00005:
       break

    w = w - lr * ((predict_result - y) * x).mean()
    b = b - lr * ((predict_result - y)).mean()

    # if i % 50 == 0:
    #     print("epoch: %d,  error: %f" % (i, cost))
x_real = x*max(data[:,0])
y_real = y*x_max


x_plot = x_real
y_plot = predict_function(x) * x_max

plt.scatter(x_real,y_real)
plt.plot(x_plot, y_plot)
plt.show()