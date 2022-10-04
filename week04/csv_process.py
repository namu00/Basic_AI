import csv
import numpy

def d_sum(list):
    sum = 0
    for d in list:
        sum += int(d)
    return sum

def d_mean(list):
    s = sum(list)
    return s/len(list)

f = open("week04/input.csv",'r')
data = f.readlines()
f.close()

s = []
mean_d = []

for d in data[1:]:
    m = list(map(int,d.replace("\n","").split(",")[1:]))
    #sum.append(str(numpy.sum(m)))
    #mean.append(str(numpy.mean(m)))
    s.append(str(d_sum(m)))
    mean_d.append(str(d_mean(m)))


d_write = data[1:]

for i in range(len(d_write)):
    d_write[i] = d_write[i].replace("\n",",")
    d_write[i] += s[i] + "," + mean_d[i] + "\n"

f = open("week04/output.csv",'w')
f.write((data[0].replace("\n",",") + "합계,평균\n"))
f.writelines(d_write)
f.close()