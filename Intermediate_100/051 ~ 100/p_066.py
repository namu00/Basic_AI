def solution(전체블록, 규칙):
    answer = []
    for 부분블록 in 전체블록:
        answer.append(블록순서체크(부분블록, 규칙))
    return answer

def 블록순서체크(부분블록, 규칙):
    임시변수 = 규칙.index(규칙[0])
    for 문자 in 부분블록:
        if 문자 in 규칙:
            if 임시변수 > 규칙.index(문자):
                return '불가능'
            임시변수 = 규칙.index(문자)
    return '가능'

전체블록 = ['ABCDEF', 'BCAD', 'ADEFQRX', 'BEDFG', 'AEBFDGCH']
규칙 = 'ABCD'

print(solution(전체블록, 규칙))