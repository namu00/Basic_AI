#diff(1/(1+exp(-x))) == exp(-x)/(1+exp(-x))
import math

def diff(x):
    ga = f(x)
    return ga*(1-ga)

def f(x):
    return 1/(1+math.exp(-x))
input = int(input("입력 : "))
print("출력 : ",diff(input))
