user = input("입력값: ")
num = int(user) - 20
if num > 255:
    print(255)
elif num < 0:
    print(0)
else:
    print(num)