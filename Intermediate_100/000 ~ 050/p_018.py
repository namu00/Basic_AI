import numpy
scr = input("score: ").split(" ")
scr = list(map(int, scr))
print(int(numpy.mean(scr)))