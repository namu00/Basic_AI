def doong(l,k):
    answer = ["pass" for i in range(len(k))]
    for i in range(len(k)):
        p = 0
        while p<len(l)-1:
            p += k[i]
            l[p-1]-=1
            if l[p-1]<0:
                answer[i] = "fail"
            
    print(answer)