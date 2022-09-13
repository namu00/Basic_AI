a = input().split(' ')
n, k = a


def sol(n, k):
    i = 0
    q = [i for i in range(1,n+1)]

    while len(q) > 2:
        if i > len(q)-1:
            i -= len(q)
        q.pop(i)
        i += k
        i -= 1
    print(q)
sol(int(n),int(k))