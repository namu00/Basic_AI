data = {}
with open("매수종목2.txt",'r',encoding='utf-8') as fp:
    d = fp.readlines()
    for s in d:
        k,v = s.split(" ")
        data[k] = v
print(data)