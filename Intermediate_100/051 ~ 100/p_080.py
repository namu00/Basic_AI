from itertools import combinations

input = input().split(',')
d = int(input())
print(list(map(''.join, combinations(input, d))))