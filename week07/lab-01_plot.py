import numpy as np
from matplotlib import pyplot as plt

# Score
# 0 : Fail, 1 : Pass
data = np.array([
    [45, 0],
    [50, 0],
    [55, 0],
    [60, 1],
    [65, 1],
    [70, 1],
])

# plt.plot(data[:, 0], data[:, 1])
plt.scatter(data[:, 0], data[:, 1])
plt.title("Pass/Fail vs Score")
plt.xlabel("Score")
plt.ylabel("Pass/Fail")
plt.grid()
# plt.axis([0, 420, 0, 50])
plt.show()
