import math
import re

def diff(x):
    return math.cos(x)

if __name__ == "__main__":
    pi = math.pi
    temp = None
    input = input("Input: ")

    operator = re.compile('.*[+\-\*\/].*')

    if input.find("PI") != -1 :                   #If It has keyword named "PI", Processing Under Block
        if re.match(r'[0-9]PI',input) != None:    #If Input String be like 2PI, 1PI, -1PI ...etc, Processing Under Block
            temp = input.split("PI")[0]
            print("Output: ",diff(float(temp)*pi))
            exit()
        elif re.match(r'\-[0-9]PI',input):
            temp = input.split("PI")[0]
            print("Output: ",diff(float(temp)*pi))
            exit()
        elif input == "-PI":
            print("Output: ", diff(-pi))
            exit()    
        elif input == "PI":
            print("Output: ",diff(pi))
            exit()
        else:
            input = input.replace("PI",str(math.pi))
    
    if re.match(operator,input) != None:        #Operator Processing
        if input.find('+') != -1: 
            temp = input.split("+")
            temp = float(temp[0]) + float(temp[1])
        elif input.find('-') != -1:
            temp = input.split("-")
            temp = float(temp[0]) + float(temp[1])
        elif input.find('*') != -1:
            temp = input.split("*")
            temp = float(temp[0]) * float(temp[1])
        else:
            temp = input.split("/")
            temp = float(temp[0]) / float(temp[1])
        print("Output: ",diff(temp))
    else:
        print("Output: ",diff(float(input)))