from itertools import permutations

user_input = input()
k = int(input())
l = [i for i in user_input]

print(max(list(map(''.join, permutations(l, k)))))