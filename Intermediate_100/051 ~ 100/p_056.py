nationWidth = {
	'korea': 220877, 
	'Rusia': 17098242, 
	'China': 9596961, 
	'France': 543965, 
	'Japan': 377915,
	'England' : 242900,
}

w = nationWidth['korea']
nationWidth.pop('korea')
l = list(nationWidth.items())
gap = max(nationWidth.values())
item = 0

for i in l:
    if gap > abs(i[1] - w):
        gap = abs(i[1] - w)
        item = i
print(item[0],item[1]-220877)