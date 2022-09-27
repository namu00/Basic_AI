def calc(string):
    args = string[:-1]
    op = string[-1]
    result = 0

    if op == "-":
        result = int(args[0])
        for a in args[1:]:
            result -= int(a)

    elif op == "+":
        for a in args:
            result += int(a)

    elif op == "*":
        result = 1
        for a in args:
            result *= int(a)

    else:
        try:
            result = int(args[0])
            for i in range(1,len(args)):
                result /= int(args[i])
        except:
            print("0 Division Error!")
            exit()
    print("Output: ",result)

data = None
with open("week03/input.txt",'r',encoding='utf-8') as f:
    data = f.readlines()

for d in data:
    d = d.replace("\n","")
    print("text contents: ",d)
    d = d.split(" "); calc(d)
    print()
    