# 새로 작성된 코드
limit = float(input())
count = int(input())
weight = []
limit_num = 0

for i in range(count):
    weight.append(int(input()))

weight.sort()
sum = 0
for d in weight:
    sum += d
    if sum < limit:
        limit_num +=1

print(limit_num)