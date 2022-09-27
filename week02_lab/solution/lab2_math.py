# sin(x)
import math

def derivative_of_sin(x):
    return math.cos(x)

if __name__ == '__main__':
    x = 2.0
    y = derivative_of_sin(x)
    print('x is ', x, 'derivative of sin(x): ', y)

    x = math.pi / 2
    y = derivative_of_sin(x)
    print('x is ', x, 'derivative of sin(x): ', y)

    x = 0
    y = derivative_of_sin(x)
    print('x is ', x, 'derivative of sin(x): ', y)

    while True:
        x = input('input x: ')
        x = float(x)
        y = derivative_of_sin(x)
        print('x is ', x, 'derivative of sin(x): ', y)