input = input("Input: ").split(" ")
args = input[:-1]
op = input[-1]
result = 0

if op == "-":
    for a in args:
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