def sol(n):
    n = list(str(n))
    answer = 0
    count = 1
    d = {3 : 1, 6 : 2, 9 : 3}
    
    while n:
        answer += d[int(n.pop())] * count
        count *= 3
        
    return answer