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

# 0~1 값에 근사화 -> 정규화
# x = data[:, 0] / 100
# y = data[:, 1] / 100
x = data[:, 0] / 100
y = data[:, 1] / 100

# 최대 반복 횟수
num_epoch = 2000

# 학습율 (learning_rate)
learning_rate = 0.2

costs = []
# random 한 값으로 w, b를 초기화 합니다.
w = np.random.uniform(low=1, high=5)
b = np.random.uniform(low=0, high=5)
print('w: ', w, 'b: ', b)

for epoch in range(num_epoch):
    y_hat = w * x + b

    error = ((y_hat - y)**2)
    cost = error.mean()

    if cost < 0.0005:
        break

    w = w - learning_rate * ((y_hat - y) * x).mean()
    b = b - learning_rate * (y_hat - y).mean()

    costs.append(cost)

    if epoch % 5 == 0:
        print("{0:2} w = {1:.5f}, b = {2:.5f} error = {3:.5f}".format(
            epoch, w, b, cost))

print("----" * 15)
print("{0:2} w = {1:.5f}, b = {2:.5f} error = {3:.5f}".format(epoch, w, b, cost))


plt.figure(figsize=(10, 7))
plt.plot(costs)
plt.xlabel('Epochs')
plt.ylabel('Costs')
plt.show()

# # data = np.array([[100, 20],
# #                 [150, 24],
# #                 [300, 36],
# #                 [400, 47],
# #                 [130, 22],
# #                 [240, 32],
# #                 [350, 47],
# #                 [200, 42],
# #                 [100, 21],
# #                 [110, 21],
# #                 [190, 30],
# #                 [120, 25],
# #                 [130, 18],
# #                 [270, 38],
# #                 [255, 28]])

# # 검산
# w = 0.09230
# b = 0.11330
# x = 150 # True : 24
# y_predict = x / 100 * w + b
# print(y_predict * 100)

# x = 300 # True : 36
# y_predict = x / 100 * w + b
# print(y_predict * 100)

# x = 400 # True : 47
# y_predict = x / 100 * w + b
# print(y_predict * 100)


