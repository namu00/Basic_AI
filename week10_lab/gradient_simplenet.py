# coding: utf-8
import sys, os
sys.path.append(os.pardir)  # 부모 디렉터리의 파일을 가져올 수 있도록 설정
import numpy as np
from common.functions import softmax, cross_entropy_error
from common.gradient import numerical_gradient


class simpleNet:
    def __init__(self):
        self.W = np.random.randn(2,3) # 정규분포로 초기화

    def predict(self, x):
        return np.dot(x, self.W)

    def loss(self, x, t):
        # print('t shape: ', t.shape)
        z = self.predict(x)
        # print('z shape: ', z.shape)
        y = softmax(z)
        # print('y shape: ', y.shape)
        loss = cross_entropy_error(y, t)

        return loss

x = np.array([0.6, 0.9])
t = np.array([0, 0, 1])

net = simpleNet()

f = lambda none: net.loss(x, t)
# def f(none):
#     return net.loss(x, t)

dW = numerical_gradient(f, net.W)

print('dW: ', dW)
print('dW(shape): ', dW.shape)