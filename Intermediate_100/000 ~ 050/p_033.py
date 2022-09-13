data = input("Input: ").split(' ')
print("출력: ", end='')

for i in range(len(data) -1 , -1, -1):
	print(data[i], end=' ')