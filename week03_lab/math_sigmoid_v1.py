# sin(x)
import math

def derivative_of_sigmoid(x):
    return function_sigmoid(x) * (1 - function_sigmoid(x))

def numerical_diff(f, x):
    h = 1e-4 # 0.0001
    return (f(x+h) - f(x-h)) / (2*h)

def function_sigmoid(x):
    return 1 / (1 + math.exp(-x))
    
if __name__ == '__main__':
    while True:
        x = input('input x: ')
        x = float(x)
        y = numerical_diff(function_sigmoid, x)
        z = derivative_of_sigmoid(x)
        abs_diff = abs(y - z)
        print('x is ', x, 'derivative of sin(x): ', z, 'numerical diff: ', y, 'abs diff: ', abs_diff)