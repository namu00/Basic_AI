텃밭 = [[0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0]]

def solution(텃밭):
    넓이 = len(텃밭[0])
    높이 = len(텃밭)
    텃밭합 = [[0] * 넓이 for i in range(len(텃밭))]
    for i in range(0, 높이):
        for j in range(0, 넓이):
            if 텃밭[i][j] == 0:
                텃밭합[i][j] = 1
            else:
                텃밭합[i][j] = 0
    
    for i in range(1, 높이):
        for j in range(1, 넓이):
            if 텃밭합[i][j] == 1:
                텃밭합[i][j] = min(텃밭합[i-1][j-1], min(텃밭합[i-1][j], 텃밭합[i][j-1])) + 1

    maxValue = 0
    x = 0
    y = 0
    for i in range(0, 높이):
        for j in range(0, 넓이):
            if maxValue < 텃밭합[i][j]:
                maxValue = 텃밭합[i][j]
                x = i
                y = j
                
    print(maxValue, x, y)
    print(maxValue, 'X', maxValue)
    
    for i in range(x - (maxValue - 1), x + 1):
        for j in range(y - (maxValue - 1), y + 1):
            텃밭[i][j] = '#'

    return 텃밭
    
solution(텃밭)