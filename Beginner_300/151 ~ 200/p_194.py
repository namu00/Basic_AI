data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
res = []
for line in data:
    sub = []
    for column in line:
        sub.append(column * 1.00014)
    res.append(sub)
print(res)