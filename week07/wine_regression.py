import numpy as np
from matplotlib import pyplot as plt
import csv

wine_data = []

#CSV Read Section
with open('wine.csv','r') as fp:
    rdr = csv.reader(fp)
    for i in rdr:
        wine_data.append(i)
    wine_data = wine_data[1:]
wine_data = np.array(wine_data)


#One-Hot Encoding Section
num = np.unique(wine_data[:,0],axis=0)
encoding = np.eye(len(num))

label = []
for wine in wine_data[:,0]:
    if wine == '1': label.append(0)
    elif wine == '2': label.append(1)
    else: label.append(2)

y_hot = np.eye(len(num))[label]  #Answer array

#Function Define Section
def softmax(x):
    if x.ndim ==2:
        x = x.T
        x = x - np.max(x,axis=0) #normalize by max value
        y = np.exp(x) / np.sum(np.exp(x), axis= 0) #softmax function
        return y.T

    x = x - np.max(x)
    return np.exp(x)/np.sum(np.exp(x))

def cros_entropy(predict, target):
    delta = 1e-7
    return -np.mean(target * np.log(predict + delta))

#Learning Section

#-------------행렬 크기 정리-------------#
#입력값 x는 (전체 데이터 개수) x (구분기준 개수)
#정답 y는 (전체 데이터 개수) x (정답 개수)
#가중치 w는 (구분기준 개수) x (정답 개수) 
#가중치 b는 (전체 데이터 개수) x (정답 개수)
#y = wx + b
#-------------행렬 크기 정리-------------#

learning_rate = 0.00005
epoch = 500000
eps = 1e-7

w = np.ones([13,3],dtype=float)
b = np.ones([3,],dtype=float)

x = np.array(wine_data[:,1:],dtype=float)
m = x.shape[0]
costs = []
for num in range(epoch + 1):
    _predict = np.dot(x ,w) + b
    _predict = softmax(_predict)

    cost = y_hot * np.log(_predict + eps)
    cost = -cost.mean()

    if cost < 0.000005:
        break

    w_grad = (1/m)*np.dot(x.T, (_predict - y_hot))
    b_grad = (1/m)*np.sum(_predict - y_hot)

    w = w - learning_rate * w_grad
    b = b - learning_rate * b_grad

    costs.append(cost)

    if epoch % 50 == 0:
        print("{0:2} error = {1:.5f}".format(num, cost))
    
print("----" * 15)
print("{0:2} error = {1:.5f}".format(epoch, cost))

np.savetxt('weights.txt', w, delimiter=',')
np.savetxt('bias.txt', b, delimiter=',')

plt.figure(figsize=(10, 7))
plt.plot(costs)
plt.xlabel('Epochs')
plt.ylabel('Costs')
plt.show()

x = x[100]
print(x)
t = np.dot(x, w) + b
print(t)
z = softmax(t) 
print(z)
prediction = np.argmax(z)
print("Kind of Wine: %d" % prediction)