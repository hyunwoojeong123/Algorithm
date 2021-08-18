def solution(gems):
    answer = []
    ans_len = 987654321
    record = dict()
    inc = 0
    N = len(gems)
    full = len(set(gems))
    for each in set(gems):
        record[each] = 0

    s, e = 0, 0
    record[gems[s]] = 1
    inc = 1

    while e < N and s <= e:
        # print(s,e,inc,record)
        if inc == full:
            if e - s < ans_len:
                answer = [s + 1, e + 1]
                ans_len = e - s

            record[gems[s]] -= 1
            if record[gems[s]] == 0:
                inc -= 1
            s += 1

        else:
            e += 1
            if e == N:
                break
            record[gems[e]] += 1
            if record[gems[e]] == 1:
                inc += 1

    return answer