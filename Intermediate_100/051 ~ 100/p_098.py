import re
def solution(i):
    idx = re.split("[0-9]번: ", i)
    idx = idx[1:]
    for i in range(len(idx)):
        idx[i] = idx[i].replace(" ", "").split(",")
        for j in range(len(idx[i])):
            idx[i][j] = int(idx[i][j])
    answer = []
    for i in idx:
        for j in i:
            if j in answer:
                pass
            else:
                answer.append(j)
    return answer


i = "1번: 3,1 2번: 4 3번: 2,1,3 4번: 2,1,3,4"
print(solution(i))
