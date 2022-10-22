#미세먼지 좋음, 보통을 구분하는 이진회귀-분류 모델입니다.(자작 데이터)
#Grade 0: 미세먼지 농도 좋음
#Grade 1: 미세먼지 농도 보통

import csv
import os
import platform
import numpy as np
from matplotlib import pyplot as plt

#Data Extraction from CSV
Data = []
with open('fine_dust.csv','r') as fp:
    rdr =  csv.reader(fp)
    for d in list(rdr)[1:]:
        Data.append(d)
    Data = np.array(Data,dtype=np.int32)
print(Data)
y = Data[:,0] #정답 데이터
x = Data[:,1] / max(Data[:,1])  #미세먼지 농도 데이터
print("CSV Data:\n",Data)
print("type: ",type(Data),"\nShape: ",Data.shape)

#Prediction Function Define Section
def sigmoid(x):
    return 1/(1 + np.exp(-x))

#Learning Section
eps = 1e-10
alpha = 100 #Learning Rate
epoch = 50000 #Try Count
w = 1
b = 1

costs = []

for i in range(epoch):
    _y = sigmoid(w*x + b) #Prediction

    _cost =  (y*np.log(_y + eps) + (1 - y)*np.log(1 - _y + eps))
    _cost *= -1
    _cost = _cost.mean() #Cost
    costs.append(_cost)
    if _cost <= 0.0005:
        break

    #Gradient Descent Optimize
    w = w - alpha * np.mean((_y - y)*x)
    b = b - alpha * np.mean((_y - y))

    if i % 50 == 0:
        if platform.system() == "Windows": os.system("cls") #Clear Screen in Windows
        else: os.system("clear") #Clear Screen in Linux Or Others
        print("Num Of Try: %d, Error: %.5f" %(i, _cost))

print("Weight: ",w)
print("Bias: ",b)


sig_x = np.linspace(0,max(x),100)
sig_y = sigmoid(w*sig_x + b)

plt.subplot(1,2,1)
plt.title("Costs")
plt.xlabel("Epoch")
plt.ylabel("Error")
plt.plot(costs)

plt.subplot(1,2,2)
plt.title("Regression Data")
plt.xlabel("Fine Dust Concentration")
plt.ylabel("Good or Above Normal")
plt.scatter(x*max(Data[:,1]),y)
plt.plot(sig_x*max(Data[:,1]),sig_y)
plt.show()

input = int(input("미세먼지 농도를 입력하세요:")) / max(Data[:,1])
res = sigmoid(w*input + b)

if 1 - np.abs(res) < np.abs(res):
    print("미세먼지의 예측 농도는 보통 이상입니다.")
else:
    print("미세먼지의 예측 농도는 좋음입니다.")