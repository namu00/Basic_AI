# calculator v1

if __name__ == '__main__':
    while True:
        x, y, op = input().split()
        # print(x, y, op)
        x = int(x)
        y = int(y)
        
        if op == '+':
            z = x + y
        elif op == '-':
            z = x - y
        elif op == '*':
            z = x * y
        elif op == '/':
            z = x / y
        else:
            print('need correct operator')
        
        print('value is : ', z)