# coding: utf-8
import sys, os
sys.path.append(os.pardir)  # 부모 디렉터리의 파일을 가져올 수 있도록 설정

import numpy as np
import matplotlib.pyplot as plt
from dataset.fashion_mnist import load_fashionMNIST
from model.two_layer_net import TwoLayerNet

# 데이터 읽기
(x_train, t_train), (x_test, t_test) = load_fashionMNIST(normalize=True, one_hot_label=True)

network = TwoLayerNet(input_size=784, hidden_size=50, output_size=10)

# 파라미터 로드
path_dir = './ckpt'
file_name = "twolayernet_params.pkl"
network.load_params(os.path.join(path_dir, file_name))

network.make_layer()

test_acc = network.accuracy(x_test, t_test)
print("test acc | " + str(test_acc))
