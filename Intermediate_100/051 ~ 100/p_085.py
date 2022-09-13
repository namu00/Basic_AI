def solution(n):
    answer='1'
    if n == 1:
        return answer
    for i in range(1,n):
        answer = rule(answer)
    return answer
def rule(n):
    num_l = max([int(i) for i in n])
    d = [str(i)+str(str(n).count(str(i))) for i in range(1,num_l+1)]
    return ''.join(d)