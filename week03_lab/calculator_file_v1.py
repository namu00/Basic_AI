# calculator file v1
import sys

if __name__ == '__main__':

    fp = open('input.txt', 'rt')
    fp_content = fp.readlines()
    
    for content in fp_content:
        # print(content)
        # print(type(content))
        x, y, op = content.split()
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
        
        print(f'{x} {op} {y} = {z}')