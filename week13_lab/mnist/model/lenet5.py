# coding: utf-8
import sys, os

sys.path.append(os.pardir)  # 부모 디렉터리의 파일을 가져올 수 있도록 설정
import pickle
import numpy as np
from collections import OrderedDict
from common.layers import *
from common.gradient import numerical_gradient


class LeNet5:
    """단순한 합성곱 신경망

    conv - relu - pool - affine - relu - affine - softmax

    Parameters
    ----------
    input_size : 입력 크기（MNIST의 경우엔 784）
    hidden_size_list : 각 은닉층의 뉴런 수를 담은 리스트（e.g. [100, 100, 100]）
    output_size : 출력 크기（MNIST의 경우엔 10）
    activation : 활성화 함수 - 'relu' 혹은 'sigmoid'
    weight_init_std : 가중치의 표준편차 지정（e.g. 0.01）
        'relu'나 'he'로 지정하면 'He 초깃값'으로 설정
        'sigmoid'나 'xavier'로 지정하면 'Xavier 초깃값'으로 설정
    """

    def __init__(self, input_dim=(1, 28, 28),
                 conv_param_1={'filter_num': 6, 'filter_size': 5, 'pad': 2, 'stride': 1},
                 conv_param_2={'filter_num': 16, 'filter_size': 5, 'pad': 0, 'stride': 1},
                 conv_param_3={'filter_num': 120, 'filter_size': 5, 'pad': 0, 'stride': 1},
                 weight_init_std=0.01):

        # 가중치 초기화 filter_num, input_dim[0], filter_size, filter_size
        self.params = {}
        self.params['W1'] = weight_init_std * \
                            np.random.randn(6, 1, 5, 5)
        self.params['b1'] = np.zeros(6)
        self.params['W3'] = weight_init_std * \
                            np.random.randn(16, 6, 5, 5)
        self.params['b3'] = np.zeros(16)
        self.params['W5'] = weight_init_std * \
                            np.random.randn(120, 16, 5, 5)
        self.params['b5'] = np.zeros(120)
        self.params['W6'] = weight_init_std * \
                            np.random.randn(120, 84)
        self.params['b6'] = np.zeros(84)
        self.params['W7'] = weight_init_std * \
                            np.random.randn(84, 10)
        self.params['b7'] = np.zeros(10)


        # 계층 생성
        self.layers = OrderedDict()
        # C1 : 컨볼루션 연산
        self.layers['Conv1'] = Convolution(self.params['W1'], self.params['b1'],
                                           conv_param_1['stride'], conv_param_1['pad'])
        self.layers['ReLU_1'] = Relu()
        # S2 : 풀링 계층 (LeNet에서는 평균풀링을 사용했으나, 여기서는 최대풀링)
        self.layers['Pool2'] = Pooling(pool_h=2, pool_w=2, stride=2)
        # C3 : 컨볼루션 연산
        self.layers['Conv3'] = Convolution(self.params['W3'], self.params['b3'],
                                           conv_param_2['stride'], conv_param_2['pad'])
        self.layers['ReLU_2'] = Relu()
        # S4 : 풀링 계층
        self.layers['Pool4'] = Pooling(pool_h=2, pool_w=2, stride=2)
        # C5 : 컨볼루션 연산
        self.layers['Conv5'] = Convolution(self.params['W5'], self.params['b5'],
                                           conv_param_3['stride'], conv_param_3['pad'])
        self.layers['ReLU_3'] = Relu()
        # F6 : Affine 계층 120 -> 84
        self.layers['Affine6'] = Affine(self.params['W6'], self.params['b6'])
        self.layers['ReLU_4'] = Relu()
        # F7 : Affine 계층 + 활성화 함수는 softmax  84 -> 10
        self.layers['Affine7'] = Affine(self.params['W7'], self.params['b7'])

        self.last_layer = SoftmaxWithLoss()


    def predict(self, x):
        for layer in self.layers.values():
            x = layer.forward(x)

        return x

    def loss(self, x, t):
        """손실 함수를 구한다.

        Parameters
        ----------
        x : 입력 데이터
        t : 정답 레이블
        """
        y = self.predict(x)
        return self.last_layer.forward(y, t)

    def accuracy(self, x, t, batch_size=100):
        if t.ndim != 1: t = np.argmax(t, axis=1)

        acc = 0.0

        for i in range(int(x.shape[0] / batch_size)):
            tx = x[i * batch_size:(i + 1) * batch_size]
            tt = t[i * batch_size:(i + 1) * batch_size]
            y = self.predict(tx)
            y = np.argmax(y, axis=1)
            acc += np.sum(y == tt)

        return acc / x.shape[0]

    def numerical_gradient(self, x, t):
        """기울기를 구한다（수치미분）.

        Parameters
        ----------
        x : 입력 데이터
        t : 정답 레이블

        Returns
        -------
        각 층의 기울기를 담은 사전(dictionary) 변수
            grads['W1']、grads['W2']、... 각 층의 가중치
            grads['b1']、grads['b2']、... 각 층의 편향
        """
        loss_w = lambda w: self.loss(x, t)

        grads = {}
        for idx in (1, 2, 3):
            grads['W' + str(idx)] = numerical_gradient(loss_w, self.params['W' + str(idx)])
            grads['b' + str(idx)] = numerical_gradient(loss_w, self.params['b' + str(idx)])

        return grads

    def gradient(self, x, t):
        """기울기를 구한다(오차역전파법).

        Parameters
        ----------
        x : 입력 데이터
        t : 정답 레이블

        Returns
        -------
        각 층의 기울기를 담은 사전(dictionary) 변수
            grads['W1']、grads['W2']、... 각 층의 가중치
            grads['b1']、grads['b2']、... 각 층의 편향
        """
        # forward
        self.loss(x, t)

        # backward
        dout = 1
        dout = self.last_layer.backward(dout)

        layers = list(self.layers.values())
        layers.reverse()
        for layer in layers:
            dout = layer.backward(dout)

        # 결과 저장
        grads = {}
        grads['W1'], grads['b1'] = self.layers['Conv1'].dW, self.layers['Conv1'].db
        grads['W3'], grads['b3'] = self.layers['Conv3'].dW, self.layers['Conv3'].db
        grads['W5'], grads['b5'] = self.layers['Conv5'].dW, self.layers['Conv5'].db
        grads['W6'], grads['b6'] = self.layers['Affine6'].dW, self.layers['Affine6'].db
        grads['W7'], grads['b7'] = self.layers['Affine7'].dW, self.layers['Affine7'].db

        return grads

    def save_params(self, file_name="params_Lenet.pkl"):
        params = {}
        for key, val in self.params.items():
            params[key] = val
        with open(file_name, 'wb') as f:
            pickle.dump(params, f)

    def load_params(self, file_name="params_Lenet.pkl"):
        with open(file_name, 'rb') as f:
            params = pickle.load(f)
        for key, val in params.items():
            self.params[key] = val

            j = 1

        for i, key in enumerate(['Conv1', 'Conv3', 'Conv5', 'Affine6', 'Affine7']):
            self.layers[key].W = self.params['W' + str(i + j)]
            self.layers[key].b = self.params['b' + str(i + j)]
            if j < 3:
                j += 1