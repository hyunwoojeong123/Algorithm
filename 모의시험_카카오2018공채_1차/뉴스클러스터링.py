def solution(str1, str2):
    answer = 0
    pair1,pair2 = [],[]
    N1 = len(str1)
    N2 = len(str2)
    for i in range(N1-1):
        temp = str1[i:i+2].lower()
        if temp.isalpha():
            pair1.append(temp)
    for i in range(N2-1):
        temp = str2[i:i+2].lower()
        if temp.isalpha():
            pair2.append(temp)
    P1 = len(pair1)
    P2 = len(pair2)
    visited = [False for _ in range(P2)]
    Gyo = 0
    for i in range(P1):
        for j in range(P2):
            if visited[j]:
                continue
            if pair1[i] == pair2[j]:
                visited[j] = True
                Gyo += 1
                break
    Hab = P1 + P2 - Gyo
    if Gyo == 0 and Hab == 0:
        answer = 1
    else:
        answer = Gyo/Hab
    answer = int(answer*65536)
    return answer