with open("week04/list.txt",'r',encoding = 'utf-8') as fp:
    data = fp.readlines()

number_list = []
for d in data:
    number_list.append(int(d.replace("\n","").replace(" ","")))

print("min: %d max: %d" % (min(number_list) , max(number_list)))