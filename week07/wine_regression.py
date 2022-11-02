import numpy as np
from matplotlib import pyplot as plt
import csv
import os

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

def get_ans(index): #Functions for Verifying
    d = x[index]
    # print("Input Data: ",d*value_max)
    # print("Right Answer: ",y[index] + 1)
    t = np.dot(d, w) + b
    # print(t)
    z = softmax(t) 
    return np.argmax(z)

def learning(w,x,b):
    m = x.shape[0]
    eps = 1e-17

    learning_rate = 1000
    epoch = 10000
    for num in range(epoch + 1):
        _predict = np.dot(x ,w) + b
        _predict = softmax(_predict)

        cost = y_hot * np.log(_predict + eps)
        cost = -cost.mean()

        if cost < 0.000000005:
            break

        w_grad = (1/m)*np.dot(x.T, (_predict - y_hot))
        b_grad = (1/m)*np.sum(_predict - y_hot)

        w = w - learning_rate * w_grad
        b = b - learning_rate * b_grad

        costs.append(cost)

    print("error = %.10f" %(cost),end='  ')

    np.savetxt('weights.txt', w, delimiter=',')
    np.savetxt('bias.txt', b, delimiter=',')

    return(w,b,costs)
    

#-------------행렬 크기 정리-------------#
#입력값 x는 (전체 데이터 개수) x (구분기준 개수)
#정답 y는 (전체 데이터 개수) x (정답 개수)
#가중치 w는 (구분기준 개수) x (정답 개수) 
#가중치 b는 (전체 데이터 개수) x (정답 개수)
#y = wx + b
#-------------행렬 크기 정리-------------#
if __name__ == "__main__":

    wine_data = []

    #CSV Read Section
    with open('wine.csv','r') as fp:
        rdr = csv.reader(fp)
        wine_data = np.array(list(rdr)[1:],dtype = np.float32)

    #Normalize Section
    value_max = np.max(wine_data[:,1:])
    x = wine_data[:,1:] / value_max


    #One-Hot Encoding Section
    label = []
    for ans in wine_data[:,0]:
        if ans == 1: label.append(0)
        elif ans == 2: label.append(1)
        else: label.append(2)
    y = np.array(wine_data[:,0])

    num = np.unique(label,axis=0)
    print(num)
    num = num.shape[0]
    print(num)

    encoding = np.eye(num)[label]
    y = np.array(label)
    y_hot = encoding.copy()

    try:
        w = np.loadtxt('weights.txt',delimiter=",")
        b = np.loadtxt('bias.txt',delimiter=',')
    except:
        w = np.ones((13,3))
        b = np.ones((178,3))    
    costs = []
    Try = 0
    while True:
        Try += 1
        print("Learning Session: %10d " % Try,end = ' ')
        w,b,cost = learning(w,x,b)
        costs.append(cost)
        Correct_Rate = 0 
        for i in range(len(y)):
            if get_ans(i) == y[i]: Correct_Rate += 1
        os.system("cls")
        print("Correct Rate: %.10f" % (Correct_Rate / len(y)))
        if Correct_Rate == len(y): break
        

    print("-----Learning Done!-----")
    print("Data Set Classification Correct Rate: %.3f %%" % 100.0) #학습 데이터를 입력으로 넣었을 때의 정답률
    #plt.subplot(4,4,1)
    # plt.plot(costs)
    # plt.title("Cost")
    # plt.xlabel('Epochs')
    # plt.ylabel('Costs')
    # plt.show()

    # title = ["","","Alcohol","Malic.acid","Ash","Acl","Mg","Phenols","Flavanoids","Nonflavanoid.phenols","Proanth","Color.int","Hue","OD","Proline"]
    # for k in range(1,14):
    #     plt.subplot(4,4,k)
    #     t = x[:,(k-1)]
    #     for i in range(len(y)):
    #         if y[i] == '1': plt.scatter(t[i],y[i], c="red", s=10)
    #         elif y[i] == '2': plt.scatter(t[i],y[i], c = "blue", s=10)
    #         else: plt.scatter(t[i],y[i],c="green", s=10)
    #     plt.title(title[k])
    # plt.show()

    