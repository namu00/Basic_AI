# coding: utf-8
import sys, os
sys.path.append(os.pardir)  # 부모 디렉터리의 파일을 가져올 수 있도록 설정

import numpy as np
import matplotlib.pyplot as plt
from dataset.cifar10 import load_cifar10
from model.lenet5 import LeNet5

# 데이터 읽기
(x_train, t_train), (x_test, t_test) = load_cifar10(normalize=True, flatten=False, one_hot_label=True)

# network = TwoLayerNet(input_size=784, hidden_size=50, output_size=10)
network = LeNet5(input_dim=(3, 32, 32),
                  conv_param_1={'filter_num': 6, 'filter_size': 5, 'pad': 0, 'stride': 1},
                  conv_param_2={'filter_num': 16, 'filter_size': 5, 'pad': 0, 'stride': 1},
                  conv_param_3={'filter_num': 120, 'filter_size': 5, 'pad': 0, 'stride': 1},
                  weight_init_std=0.01)

# 매개변수 가져오기
path_dir = './ckpt'
file_name = "lenet5_params.pkl"
network.load_params(os.path.join(path_dir, file_name))
print("Parameter Load Complete!")

test_acc = network.accuracy(x_test, t_test)
print("test acc | ", format(test_acc*100, ".4f"), '%')