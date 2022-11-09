import os
import time
import numpy as np
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
    k = np.random.randn(i)
    k * k

print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간