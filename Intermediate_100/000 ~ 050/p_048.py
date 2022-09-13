a = input()
b = []

for i in a:
	if i.islower():
		b.append(i.upper())
	else:
		b.append(i.lower())
	
for i in b:
	print(i, end='')