def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        tp = ''
        for j in range(n)[::-1]:
            if arr1[i] & (1 << j) or arr2[i] & (1 << j):
                tp += '#'
            else:
                tp += ' '
        answer.append(tp)
    return answer