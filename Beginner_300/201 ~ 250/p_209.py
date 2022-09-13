def message1():
    print("A")

def message2():
    print("B")
    message1()

message2()

#B
#A