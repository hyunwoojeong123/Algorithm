# 10:37~10:45
def solution(s):
    answer = 0
    N = len(s)
    i = 0
    str_answer = ''
    while i < N:
        if s[i].isdigit():
            str_answer += s[i]
        else:
            if s[i] == 'z':
                str_answer += '0'
                i += 3
            elif s[i] == 'o':
                str_answer += '1'
                i += 2
            elif s[i] == 't':
                if s[i + 1] == 'w':
                    str_answer += '2'
                    i += 2
                elif s[i + 1] == 'h':
                    str_answer += '3'
                    i += 4
            elif s[i] == 'f':
                if s[i + 1] == 'o':
                    str_answer += '4'
                    i += 3
                elif s[i + 1] == 'i':
                    str_answer += '5'
                    i += 3
            elif s[i] == 's':
                if s[i + 1] == 'i':
                    str_answer += '6'
                    i += 2
                elif s[i + 1] == 'e':
                    str_answer += '7'
                    i += 4
            elif s[i] == 'e':
                str_answer += '8'
                i += 4
            elif s[i] == 'n':
                str_answer += '9'
                i += 3

        i += 1
    answer = int(str_answer)
    return answer