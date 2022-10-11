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

x = data[:, 0]
y = data[:, 1]

w = np.random.uniform(low=1, high=10)
b = np.random.uniform(low=0, high=10)
print('w: ', w, 'b: ', b)

y_hat = w * x + b

error = (y_hat - y) ** 2
print('error: ', error)
print('shape: ', error.shape)

cost = error.mean()
print('cost: ', cost)