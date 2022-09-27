import csv
import numpy

f = open("week04/input.csv",'r')
data = f.readlines()
f.close()

sum = []
mean = []

for d in data[1:]:
    m = list(map(int,d.replace("\n","").split(",")[1:]))
    sum.append(str(numpy.sum(m)))
    mean.append(str(numpy.mean(m)))

d_write = data[1:]

for i in range(len(d_write)):
    d_write[i] = d_write[i].replace("\n",",")
    d_write[i] += sum[i] + "," + mean[i] + "\n"

f = open("week04/output.csv",'w')
f.write((data[0].replace("\n",",") + "합계,평균\n"))
f.writelines(d_write)
f.close()