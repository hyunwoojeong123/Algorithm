def solution(gems):
    answer = []
    ans_len = 987654321
    gems_set = set(gems)
    M = len(gems_set)
    N = len(gems)
    takes = dict()
    for gem in gems_set:
        takes[gem] = 0
    s = e = cnt = 0
    while True:
        #print(s,e,takes)
        if cnt == M:
            if ans_len > e - s:
                answer = [s, e]
                ans_len = e - s
        if cnt >= M:
            takes[gems[s]] -= 1
            if takes[gems[s]] == 0:
                cnt -= 1
            s += 1

        elif e == N:
            break
        else:
            takes[gems[e]] += 1
            if takes[gems[e]] == 1:
                cnt += 1
            e += 1


    return answer

gems = ['AA', 'AB', 'AC', 'AA', 'AC']
print(solution(gems))