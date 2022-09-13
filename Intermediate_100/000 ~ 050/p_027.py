keys = input().split()
values = map(int, input().split())

result = dict(zip(keys, values))
print(result)