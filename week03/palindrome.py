def verify(string):
    rev = string[::-1]
    if rev == string: return True
    else: return False

input = input("Key Word: ").replace(".","").replace(" ","")
print("Result: ",verify(input))