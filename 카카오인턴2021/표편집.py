# 7:45~8:20 8:45~9:25
# 8:55 정확성 통과 - 45분
# 9:25 정답 - 1:15분
def solution(n, k, cmd):
    answer = ''
    check = ['O'] * n
    prv = [-1] + [i for i in range(n)]
    nxt = [i + 1 for i in range(n - 1)] + [-1]
    # print(prv,nxt)
    name = ['무지', '콘', '어피치', '제이지', '프로도', '네오', '튜브', '라이언']
    pos = k
    stack = []
    for each in cmd:
        # print(each, '실행')
        if each == 'C':
            check[pos] = 'X'
            stack.append(pos)
            pnxt = nxt[pos]
            pprv = prv[pos]
            nxt[pprv] = pnxt
            prv[pnxt] = pprv
            if pnxt != -1:
                pos = pnxt
            else:
                pos = pprv
        elif each == 'Z':
            recover = stack.pop()
            check[recover] = 'O'
            pnxt = nxt[recover]
            pprv = prv[recover]
            nxt[pprv] = recover
            prv[pnxt] = recover
        elif each[0] == 'D':
            d = int(each[2:])
            while d > 0:
                d -= 1
                pos = nxt[pos]

        elif each[0] == 'U':
            d = int(each[2:])
            while d > 0:
                d -= 1
                pos = prv[pos]
        # print('실행후 위치와 배열', pos,name[pos], check)
    for each in check:
        answer += each
    return answer
