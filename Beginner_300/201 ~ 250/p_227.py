def print_mxn(line, num):
    chunk_num = int(len(line) / num)
    for x in range(chunk_num + 1) :
        print(line[x * num: x * num + num])

print_mxn("아이엠어보이유알어걸", 3)