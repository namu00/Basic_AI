# Problem Lab04-1

import math

def derivative_of_relu(x):
    if x < 0:
        return 0
    else:
        return 1

def numerical_diff(f, x):
    h = 1e-10 # 0.0001
    return (f(x+h) - f(x-h)) / (2*h)

def function_relu(x):
    return max(0, x)

if __name__ == '__main__':
    while True:
        x = input('input x: ')
        x = float(x)
        y = numerical_diff(function_relu, x)
        z = derivative_of_relu(x)
        abs_diff = abs(y - z)
        print('x is ', x, 'derivative of relu(x): ', z, 'numerical diff: ', y, 'abs diff: ', abs_diff)
