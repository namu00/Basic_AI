# coding: utf-8
import sys, os
sys.path.append(os.pardir)  # 부모 디렉터리의 파일을 가져올 수 있도록 설정
import numpy as np
from dataset.mnist import load_mnist
from PIL import Image


def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()

(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)
print(x_train.shape, t_train.shape, x_test.shape, t_test.shape)

img = x_train[0]
print(type(img))
print('img information: ', img.shape, img.max(), img.min())
label = t_train[0]
print(label)  # 5
print(type(label))
print('label information: ', label.shape, label.max(), label.min())

print(img.shape)  # (784,)
img = img.reshape(28, 28)  # 형상을 원래 이미지의 크기로 변형
print(img.shape)  # (28, 28)

img_show(img)

