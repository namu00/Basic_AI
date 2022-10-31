import numpy as np
from matplotlib import pyplot as plt

# 아래 코드를 실행하기 위해서는 pip로 seaborn과 pandas를 설치한다.

# pip install seaborn
# --> 위 커맨드로 pandas도 설치됨
import seaborn as sns
import pandas as pd

sns.set(style="ticks", color_codes=True)
iris = sns.load_dataset("iris")
g = sns.pairplot(iris, hue="species", palette="husl")
# plt.show()
# iris.info()

# 1. 데이터 획득하기
x = iris.iloc[:,0:4].values
print(x.shape)
y = iris.iloc[:,4].values
print(y.shape)
print(y)

# 2. 선택
# # 정규화 방법
# x_max = x.max(axis=0)
# x_normal = x / x_max

# 3. 원 핫 인코딩 (one-hot encoding)
label = []
# 0 : 'setosa'
# 1 : 'versicolor'
# 2 : 'virginica'

for name in y:
    if name == 'setosa':
        label.append(0)
    elif name == 'versicolor':
        label.append(1)
    elif name == 'virginica':
        label.append(2)

print(label)
print(x)

# one-hot encoding
num = np.unique(label, axis=0)
print(num)
num = num.shape[0]

encoding = np.eye(num)[label]
print(encoding)

y_hot = encoding.copy()
# x : 입력 데이터, y : 출력(클래스) 데이터 - one-hot encoding
print(label[0], y_hot[0])
print(label[-1], y_hot[-1])
