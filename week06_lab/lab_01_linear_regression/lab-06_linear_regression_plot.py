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

# 예측
w = 0.09230
b = 0.11330
org_x = np.linspace(0, 420, 100)
pred_x = org_x / 100  # 정규화
pred_y = w * pred_x + b
pred_y = pred_y * 100 # 정규화 반대 과정

plt.scatter(x, y) 
plt.title("Time / Distance")
plt.xlabel("Delivery Distance (meter)")
plt.ylabel("Time Consumed (minute)")
plt.plot(org_x, pred_y)
plt.axis([0, 420, 0, 50])
plt.show()



