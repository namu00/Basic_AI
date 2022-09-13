input = input("입력: ")

v = list(input.strip().split())
v = [int (i) for i in v]

if v != sorted(v):
	print("NO")
	
else:
	print("YES")