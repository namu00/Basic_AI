def f(x):
    return max(0,x)

def g(x):
    if x <= 0: return 0
    else: return 1

data = float(input("입력: "))
print("출력: ",g(data))