def count(n):
	count = str(list(range(n+1))).count('1')
	return count

print(count(1000))