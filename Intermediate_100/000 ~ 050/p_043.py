a = int(input())
b = []
while a:
    b.append(str(a % 2))
    a = int(a / 2)

b.reverse()
print(''.join(b))