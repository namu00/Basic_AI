import os
import time
import platform
start = time.time()  # 시작 시간 저장

system = platform.system()
for i in range(20000):
    if i % 100 == 0:
        if system == "Windows":
            os.system("cls")
        else:
            os.system("clear")
            print("Operating System: ", system)
        print(i)
    k = i ** i
    # l = k ** k
    # m = l ** l
    # a = m ** m
    # b = a ** a
    # c = b ** b
    # d = c ** c

print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간