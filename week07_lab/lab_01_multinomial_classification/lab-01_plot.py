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
plt.show()
iris.info()