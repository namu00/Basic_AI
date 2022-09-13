data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]

res = []
for l in data:
    for c in l:
        res.append(c*1.00014)
print(res)