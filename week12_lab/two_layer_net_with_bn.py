# coding: utf-8
import sys, os
sys.path.append(os.pardir)  # 부모 디렉터리의 파일을 가져올 수 있도록 설정
import numpy as np
from common.layers import *
from common.gradient import numerical_gradient
from collections import OrderedDict
import pickle

class TwoLayerNet:
    def __init__(self, input_size, hidden_size_list, output_size,
        activation='relu', weight_init_std='relu', weight_decay_lambda=0, 
        use_dropout = False, dropout_ration = 0.5, use_batchnorm=False):
        self.activation = activation
        self.input_size = input_size
        self.output_size = output_size
        self.hidden_size_list = hidden_size_list
        self.hidden_layer_num = len(hidden_size_list)
        self.use_dropout = use_dropout
        self.weight_decay_lambda = weight_decay_lambda
        self.use_batchnorm = use_batchnorm
        self.dropout_ration = dropout_ration
        self.params = {}

        # 가중치 초기화
        self.__init_weight(weight_init_std)

    def make_layer(self, train_flg=False):
        # 계층 생성
        activation_layer = {'sigmoid': Sigmoid, 'relu': Relu}
        self.layers = OrderedDict()
        for idx in range(1, self.hidden_layer_num+1):
            self.layers['Affine' + str(idx)] = Affine(self.params['W' + str(idx)],
                                                      self.params['b' + str(idx)])
            if self.use_batchnorm:
                if train_flg:
                    self.params['gamma' + str(idx)] = np.ones(self.hidden_size_list[idx-1])
                    self.params['beta' + str(idx)] = np.zeros(self.hidden_size_list[idx-1])
                
                self.layers['BatchNorm' + str(idx)] = BatchNormalization(self.params['gamma' + str(idx)], self.params['beta' + str(idx)])
                
            self.layers['Activation_function' + str(idx)] = activation_layer[self.activation]()
            
            if self.use_dropout:
                self.layers['Dropout' + str(idx)] = Dropout(self.dropout_ration)

        idx = self.hidden_layer_num + 1
        self.layers['Affine' + str(idx)] = Affine(self.params['W' + str(idx)], self.params['b' + str(idx)])

        self.last_layer = SoftmaxWithLoss()

    def __init_weight(self, weight_init_std):
        """가중치 초기화
        
        Parameters
        ----------
        weight_init_std : 가중치의 표준편차 지정（e.g. 0.01）
            'relu'나 'he'로 지정하면 'He 초깃값'으로 설정
            'sigmoid'나 'xavier'로 지정하면 'Xavier 초깃값'으로 설정
        """
        all_size_list = [self.input_size] + self.hidden_size_list + [self.output_size]
        for idx in range(1, len(all_size_list)):
            scale = weight_init_std
            if str(weight_init_std).lower() in ('relu', 'he'):
                scale = np.sqrt(2.0 / all_size_list[idx - 1])  # ReLUを使う場合に推奨される初期値
            elif str(weight_init_std).lower() in ('sigmoid', 'xavier'):
                scale = np.sqrt(1.0 / all_size_list[idx - 1])  # sigmoidを使う場合に推奨される初期値
            self.params['W' + str(idx)] = scale * np.random.randn(all_size_list[idx-1], all_size_list[idx])
            self.params['b' + str(idx)] = np.zeros(all_size_list[idx])

    def predict(self, x, train_flg=False):
        for key, layer in self.layers.items():
            if "Dropout" in key or "BatchNorm" in key:
                x = layer.forward(x, train_flg)
            else:
                x = layer.forward(x)

        return x

    def loss(self, x, t, train_flg=False):
        """손실 함수를 구한다.
        
        Parameters
        ----------
        x : 입력 데이터
        t : 정답 레이블 
        """
        y = self.predict(x, train_flg)

        weight_decay = 0
        for idx in range(1, self.hidden_layer_num + 2):
            W = self.params['W' + str(idx)]
            weight_decay += 0.5 * self.weight_decay_lambda * np.sum(W**2)

        return self.last_layer.forward(y, t) + weight_decay

    def accuracy(self, X, T):
        Y = self.predict(X, train_flg=False)
        Y = np.argmax(Y, axis=1)
        if T.ndim != 1 : T = np.argmax(T, axis=1)

        accuracy = np.sum(Y == T) / float(X.shape[0])
        return accuracy

    def numerical_gradient(self, X, T):
        """기울기를 구한다(수치 미분).
        
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
        loss_W = lambda W: self.loss(X, T, train_flg=True)

        grads = {}
        for idx in range(1, self.hidden_layer_num+2):
            grads['W' + str(idx)] = numerical_gradient(loss_W, self.params['W' + str(idx)])
            grads['b' + str(idx)] = numerical_gradient(loss_W, self.params['b' + str(idx)])
            
            if self.use_batchnorm and idx != self.hidden_layer_num+1:
                grads['gamma' + str(idx)] = numerical_gradient(loss_W, self.params['gamma' + str(idx)])
                grads['beta' + str(idx)] = numerical_gradient(loss_W, self.params['beta' + str(idx)])

        return grads
        
    def gradient(self, x, t):
        # forward
        self.loss(x, t, train_flg=True)

        # backward
        dout = 1
        dout = self.last_layer.backward(dout)

        layers = list(self.layers.values())
        layers.reverse()
        for layer in layers:
            dout = layer.backward(dout)

        # 결과 저장
        grads = {}
        for idx in range(1, self.hidden_layer_num+2):
            grads['W' + str(idx)] = self.layers['Affine' + str(idx)].dW + self.weight_decay_lambda * self.params['W' + str(idx)]
            grads['b' + str(idx)] = self.layers['Affine' + str(idx)].db

            if self.use_batchnorm and idx != self.hidden_layer_num+1:
                grads['gamma' + str(idx)] = self.layers['BatchNorm' + str(idx)].dgamma
                grads['beta' + str(idx)] = self.layers['BatchNorm' + str(idx)].dbeta

        return grads
    
    def print_params(self):
        for key, val in self.params.items():
            # params[key] = val
            # print('key: ', key, 'val: ', val)
            print(key)
        # for key, val in self.layers.items():
        #     print(key)
        #     if 'BatchNorm' in key:
        #         print('a: ', key, val.running_mean, val.running_var)
            
    def save_params(self, file_name="params.pkl"):
        params = {}
        for key, val in self.params.items():
            print(key, end=' ')
            params[key] = val
        with open(file_name, 'wb') as f:
            pickle.dump(params, f)
        
        file_name = file_name.replace('.pkl', '_running.pkl')

        params = {}
        for key, val in self.layers.items():
            print(key)
            if 'BatchNorm' in key:
                print('a: ', key, val.running_mean, val.running_var)
                params[key] = (val.running_mean, val.running_var)
        with open(file_name, 'wb') as f:
            pickle.dump(params, f)

    def load_params(self, file_name="params.pkl", params_flag=True):
        if params_flag:
            with open(file_name, 'rb') as f:
                params = pickle.load(f)
            for key, val in params.items():
                # print(key, end=' ')
                self.params[key] = val
        else:
            file_name = file_name.replace('.pkl', '_running.pkl')
            with open(file_name, 'rb') as f:
                params = pickle.load(f)
            for key, val in self.layers.items():
                print(key)
                if 'BatchNorm' in key:
                    running = params[key]
                    val.running_mean = running[0]
                    val.running_var = running[1]

if __name__ == '__main__':
    network = TwoLayerNet(input_size=784, hidden_size_list=[100], output_size=10)
    print(network.params)
    a = network.params.copy()
    network.save_params("test_params.pkl")
    network.params = {}
    network.load_params("test_params.pkl")
    print(network.params)
    b = network.params.copy()

    # if a.all() == b.all():
    #     print('PASS')