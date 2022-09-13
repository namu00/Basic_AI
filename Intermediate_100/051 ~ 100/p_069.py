#골드바흐의 추측
def cal():
    n=10000*2
    primes=[]    
    a = [False,False] + [True]*(n-1)

    for i in range(2,n+1):
      if a[i]:
        primes.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False
            
    return primes


a = cal()

#골드바흐파티션
n = int(input())
l = []
k = []	

for i in range(2, n//2+1):    
    if i in a and n-i in a:
        l.append(i)
        l.append(n-i)

for i in range(0,len(l)-1,2):
    k.append(l[i+1]-l[i])
    
index = k.index(min(k))*2
print(l[index], l[index+1])