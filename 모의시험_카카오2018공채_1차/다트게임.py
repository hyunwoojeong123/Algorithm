def solution(dartResult):
    answer = 0
    N = len(dartResult)
    results = []
    tp = []
    i = 0
    while i < N:
        each = dartResult[i]
        if each.isdigit():
            if tp != []:
                results.append(tp)
                tp = []
            if each == '1' and i != N-1 and dartResult[i+1].isdigit():
                tp.append(10)
                i += 1
            else:
                tp.append(int(each))
        elif each == 'S' or each == 'D' or each == 'T':
            tp.append(each)
        elif each == '*' or each == '#':
            tp.append(each)
        i += 1
    results.append(tp)
    # print(results)
    NR = len(results)
    scores = [-12345 for _ in range(NR)]
    for i in range(NR):
        result = results[i]
        score = result[0]
        if result[1] == 'S':
            score = score
        if result[1] == 'D':
            score = score * score
        if result[1] == 'T':
            score = score * score * score
        if len(result) == 3:
            if result[2] == '*':
                score = 2 * score
                if i != 0:
                    scores[i-1] *= 2
            if result[2] == '#':
                score = -score
        scores[i] = score
    for i in range(NR):
        answer += scores[i]
    return answer