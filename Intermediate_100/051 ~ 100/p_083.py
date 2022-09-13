
def math(e):
    m = {
        ')':'(',
        '}':'{',
    }
    stack = []
    for i in e:
        if i in '({':
            stack.append(i)
        elif i in m:
            if len(stack) == 0:
                return False
            else:
                t = m[i]
                if t != stack.pop():
                    return False
    return len(stack) == 0

while 1:
    order = input('데이터 입력(1), 프로그램 종료(2) :')
    if order == '1':
        ex = input('데이터를 입력하세요 :')
        print(math(ex))
    else:
        break