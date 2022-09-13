#64번 이상한 엘리베이터
N = int(input())
result = 0

while True:
    if N%7 ==0:
        result += N//7
        print(result)
        break
    N -= 3
    result += 1
    if N < 0:
        print(-1)
        break