def solution(n):
    people = 0
    total = 0
    while(True):
        total = people*(people-1)/2
        if n<total:
            break
        people+=1
    times = int(people-(total-n)-1)
    return [times,people]