#diff(1/(1+exp(-x))) == exp(-x)/(1+exp(-x))
import math

def diff(x):
    return math.exp(-x)/(math.pow((1 + math.exp(-x)),2.0))

input = int(input("입력 : "))
print("출력 : ",diff(input))