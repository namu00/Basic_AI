# coding: utf-8
import sys, os
# sys.path.append(os.pardir)  # 부모 디렉터리의 파일을 가져올 수 있도록 설정
import numpy as np
import matplotlib.pyplot as plt
from dataset.mnist import load_mnist
from two_layer_net_with_bn import TwoLayerNet

use_batchnorm = True

# 데이터 읽기
(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

# This network is based on multi_layer_net_extend.py
network = TwoLayerNet(input_size=784, hidden_size_list=[50], output_size=10, 
                                    weight_init_std='relu', use_batchnorm=use_batchnorm)

if use_batchnorm == True:
    # 파라미터 로드
    network.load_params("twolayernet_2_params_with_bn.pkl", params_flag=True)
    # 로드된 파라미터를 바탕으로 network 생성
    network.make_layer(train_flg=False)
    # Running Mean/Var 로드
    network.load_params("twolayernet_2_params_with_bn.pkl", params_flag=False)
else:
    # 파라미터 로드
    network.load_params("twolayernet_2_params_without_bn.pkl", params_flag=True)
    # 로드된 파라미터를 바탕으로 network 생성
    network.make_layer(train_flg=False)
    # Running Mean/Var 로드
    network.load_params("twolayernet_2_params_without_bn.pkl", params_flag=False)

test_acc = network.accuracy(x_test, t_test)
print("test acc | " + str(test_acc))
