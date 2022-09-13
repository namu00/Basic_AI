flag = [] #지뢰 없이 깃발만 있는 리스트
minesweeper = [] #지뢰를 찾은 리스트
for i in range(5):
    flag.append(input('깃발 값과 함께 입력하세요 :').split(' '))


inputList = []
for i in range(5):
    inputList.extend(input().split())
for i in range(25):
    if inputList[i] == "1":
        inputList[i] = "f"
        if i // 5 != 0:
            inputList[i - 5] = "*"
        if i // 5 != 4:
            inputList[i + 5] = "*"
        if i % 5 != 0:
            inputList[i - 1] = "*"
        if i % 5 != 4:
            inputList[i + 1] = "*"
for i in range(25):
    if i % 5 != 4:
        print(inputList[i], end = "")
    else:
        print(inputList[i], " ")

print(flag)
print(minesweeper)