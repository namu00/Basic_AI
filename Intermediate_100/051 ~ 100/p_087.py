name = 'A C B D'.split(' ')
point = list(map(int, '70 10 55 40'.split(' ')))

def hojun(x):
    return x[1]

def sol(name, point):
    d = {}
    z = [[i, j] for i, j in zip(name, point)]
    z = sorted(z, key=hojun, reverse=True)
    
    for i in range(len(z)):
        d[z[i][0]] = i+1
    return d

print(sol(name, point))
