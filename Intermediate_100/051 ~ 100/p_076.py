import numpy as np

squre = 5
find = 3

mines = [[1, 0, 0, 1, 0],
          [0, 1, 0, 0, 1],
          [0, 0, 0, 1, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 1, 0, 0]]

s = 0
for i in range(squre - find + 1):
    for j in range(find):
        if np.sum(mines[i:find+i, j:find+j]) > s: 
            s = np.sum(mines[i:find+i, j:find+j])
print(s)