def solution(ads):
    answer = 0
    ads.sort()
    sec = ads[0][0]
    for i, v in enumerate(ads):
        index, value = -1, 0
        if v[0] <= sec:
            if value < (sec + 5 - v[0]) * v[1]:
                index = i
                value = (sec - v[0]) * v[1]
        else:
            break
    ads.pop(index)
    answer += value
    sec += 5
    return answer
print(solution([[0, 1], [0, 2], [6, 3], [8, 4]]))