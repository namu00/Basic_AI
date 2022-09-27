# Prob2. palindrome

def check_palindrome(sentence):
    str = ''
    
    for c in sentence:
        if c != '.' and c != ' ':
            str += c
    
    size = len(str)
    for i in range(size // 2):
        if str[i] != str[size - 1 - i]:
            return False
    
    return True

if __name__ == '__main__':
    print('palindrome')
    sentence = input('문장를 입력하세요 : ')
    decision = check_palindrome(sentence)
    print('string of input : %s, palindrome : %s' % (sentence, decision))
