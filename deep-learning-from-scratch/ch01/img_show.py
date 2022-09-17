# coding: utf-8
import matplotlib.pyplot as plt
from matplotlib.image import imread

if __name__ == "__main__":
    # sys.path.append('./deep-learning-from-scratch/dataset')
    img = imread('../dataset/cactus.png') # 이미지 읽어오기
    # img = imread('./deep-learning-from-scratch/dataset/cactus.png') # 이미지 읽어오기
    plt.imshow(img)

    plt.show()